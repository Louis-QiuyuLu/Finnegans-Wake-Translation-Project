#!/usr/bin/env python3
"""串行续生成英文录音；默认第一卷，也可读取底本语音工作包。"""
import argparse
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts.generate_audio import AUDIO_DIR, atomic_json, audio_is_current, load_audio_segments, load_segments, original_hash

PRIORITY = ['fw-i3-067-28', 'fw-i3-069-30', 'fw-i3-072-17']


def now():
    return datetime.now(timezone.utc).isoformat()


def book_one(chapters_dir=None):
    return [s for s in load_segments(chapters_dir) if s['chapter'].startswith('I.')]


def check_originals(frozen, current):
    expected = {s['id']: (original_hash(s), s.get('source_binding')) for s in frozen}
    actual = {s['id']: (original_hash(s), s.get('source_binding')) for s in current}
    if expected != actual:
        changed = sorted(sid for sid in expected.keys() | actual.keys() if expected.get(sid) != actual.get(sid))
        raise RuntimeError('原文已改变，停止批处理；请核对后另建运行目录: ' + ', '.join(changed))


def published_audio_is_current(segment, audio_dir):
    if segment.get("source_binding"):
        return audio_is_current(segment, audio_dir, published_source=True)
    return audio_is_current(segment, audio_dir)


def build_queue(segments, audio_dir=AUDIO_DIR):
    pending = [s for s in segments if not published_audio_is_current(s, audio_dir)]
    rank = {sid: i for i, sid in enumerate(PRIORITY)}
    return sorted(pending, key=lambda s: (rank.get(s['id'], len(rank)), segments.index(s)))


def acquire_batch_lock(audio_dir, source_segments=None):
    if source_segments is None:
        name = ".batch.lock"
    else:
        books = [segment.get("source_binding", {}).get("book") for segment in source_segments]
        if not books or any(book not in ("II", "III", "IV") for book in books) or len(set(books)) != 1:
            raise ValueError("底本语音队列须属于同一已核卷号：II、III或IV")
        name = f".source-{books[0]}.lock"
    audio_dir = Path(audio_dir)
    audio_dir.mkdir(parents=True, exist_ok=True)
    lock = (audio_dir / name).open("a")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        lock.close()
        raise SystemExit(f"已有音频批处理运行：{name}")
    lock.seek(0)
    lock.truncate()
    lock.write(str(os.getpid()) + "\n")
    lock.flush()
    return lock


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', type=Path, required=True)
    parser.add_argument('--source-snapshot', type=Path, help='冻结工作包根目录；只比对第一卷原文')
    parser.add_argument('--device', choices=['mps', 'cpu'], default='cpu')
    parser.add_argument('--model', default='vertin', choices=['vertin', 'sisyphus', 'vertin2'])
    parser.add_argument('--ref', default='e1')
    parser.add_argument('--speed', default=1.05, type=float)
    parser.add_argument('--steps', default=32, type=int)
    parser.add_argument('--attempts', default=2, type=int)
    parser.add_argument('--segment-timeout', default=21600, type=int)
    parser.add_argument('--source-queue', type=Path, help='核验过的底本语音工作包')
    parser.add_argument('--source-root', type=Path, help='独立英文快照根目录；须与 source-queue 同用')
    parser.add_argument('--threads', type=int, default=8, help='每个合成进程的PyTorch CPU线程数，默认8')
    args = parser.parse_args()
    if args.threads <= 0:
        parser.error('threads 须为正整数')
    if args.source_root is not None:
        if args.source_queue is None:
            parser.error("--source-root 须与 --source-queue 同用")
        args.source_root = args.source_root.resolve()
    if args.source_queue is not None:
        args.source_queue = args.source_queue.resolve()
        if args.source_snapshot:
            parser.error('source-queue 与第一卷 source-snapshot 不能同时使用')
    if not 1 <= args.attempts <= 3 or args.segment_timeout <= 0:
        parser.error('attempts 须为1至3；timeout 须大于0')
    def load_current():
        if args.source_queue is None:
            return book_one()
        if args.source_root is not None:
            return load_audio_segments(args.source_queue, source_root=args.source_root)
        return load_audio_segments(args.source_queue)

    # Validate the selected source and queue before using its book as a lock domain.
    validated_source = load_current() if args.source_queue is not None else None
    args.run_dir.mkdir(parents=True, exist_ok=True)
    lock = acquire_batch_lock(AUDIO_DIR, validated_source)
    state_path = args.run_dir / 'state.json'
    frozen_path = args.run_dir / 'originals.json'
    candidate_dir = (args.run_dir / "candidates").resolve()
    child = None
    state = {'pid': os.getpid(), 'started_at': now(), 'status': 'starting', 'current_segment': None,
             'device': args.device, 'lock_file': str(lock.name), 'review_status': 'pending', 'candidate_dir': str(candidate_dir), 'parameters': {'model': args.model, 'ref': args.ref,
             'speed': args.speed, 'steps': args.steps, 'segment_timeout': args.segment_timeout,
             'attempts': args.attempts, 'threads': args.threads}, 'successes': [], 'failures': [], 'fallbacks': []}

    def save():
        state['updated_at'] = now()
        atomic_json(state_path, state)

    if args.source_queue is not None:
        state['source_queue'] = str(args.source_queue)
        if args.source_root is not None:
            state['source_root'] = str(args.source_root)
        state['source_book'] = validated_source[0]['source_binding']['book']

    def stopped(signum, frame):
        raise KeyboardInterrupt(f'signal {signum}')

    signal.signal(signal.SIGTERM, stopped)
    signal.signal(signal.SIGINT, stopped)
    try:
        if frozen_path.exists():
            frozen = json.loads(frozen_path.read_text(encoding='utf-8'))
        elif args.source_snapshot:
            frozen = book_one(args.source_snapshot / 'manuscript/chapters')
            atomic_json(frozen_path, frozen)
        else:
            frozen = load_current()
            atomic_json(frozen_path, frozen)
        check_originals(frozen, load_current())
        official_queue = build_queue(frozen, AUDIO_DIR)
        queue = [s for s in official_queue if not audio_is_current(s, candidate_dir)]
        state['total_segments'] = len(frozen)
        if args.source_queue is None:
            state['total_book_I'] = len(frozen)
        else:
            state['total_source_segments'] = len(frozen)
        state['already_current'] = len(frozen) - len(official_queue)
        state['already_quarantined'] = len(official_queue) - len(queue)
        state['pending'] = [s['id'] for s in queue]
        state['status'] = 'running'
        save()
        scope = "底本语音队列" if args.source_queue is not None else "第一卷"
        print(f"{now()} PID={os.getpid()} {scope}共{len(frozen)}段；待生成{len(queue)}段，device={args.device}", flush=True)
        for segment in queue:
            check_originals(frozen, load_current())
            sid = segment['id']
            if published_audio_is_current(segment, AUDIO_DIR) or audio_is_current(segment, candidate_dir):
                state['pending'].remove(sid)
                save()
                continue
            state['current_segment'] = sid
            state['original_sha256'] = original_hash(segment)
            for attempt in range(1, args.attempts + 1):
                log_path = args.run_dir / f'{sid}-pid-{os.getpid()}-attempt-{attempt}-{state["device"]}.log'
                command = [sys.executable, '-u', str(ROOT / 'scripts/generate_audio.py'), '--segment', sid,
                           '--model', args.model, '--ref', args.ref, '--device', state['device'],
                           '--speed', str(args.speed), '--steps', str(args.steps), '--threads', str(args.threads),
                           '--expected-original-sha256', original_hash(segment), '--audio-dir', str(candidate_dir)]
                if args.source_queue is not None:
                    command += ['--source-queue', str(args.source_queue)]
                    if args.source_root is not None:
                        command += ['--source-root', str(args.source_root)]
                state.update({'attempt': attempt, 'segment_log': str(log_path), 'command': command})
                print(f'{now()} 开始 {sid} attempt={attempt} device={state["device"]} log={log_path}', flush=True)
                began = time.monotonic()
                with log_path.open('a', encoding='utf-8') as output:
                    child = subprocess.Popen(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
                    state['child_pid'] = child.pid
                    save()
                    while child.poll() is None:
                        check_originals(frozen, load_current())
                        if time.monotonic() - began > args.segment_timeout:
                            child.terminate()
                            try:
                                child.wait(10)
                            except subprocess.TimeoutExpired:
                                child.kill()
                                child.wait()
                            break
                        time.sleep(3)
                        save()
                result = child.returncode
                state['child_pid'] = None
                child = None
                if result == 0 and audio_is_current(segment, candidate_dir):
                    state['successes'].append({'segment_id': sid, 'device': state['device'],
                                               'completed_at': now(), 'log': str(log_path),
                                               'candidate': str(candidate_dir / (sid + '.mp3')), 'review_status': 'pending',
                                               'original_sha256': original_hash(segment),
                                               'parameters': dict(state['parameters']),
                                               'provenance': str(candidate_dir / (sid + '.provenance.json'))})
                    if 'source_binding' in segment:
                        state['successes'][-1]['source_binding'] = segment['source_binding']
                    print(f'{now()} 完成 {sid}', flush=True)
                    break
                state['failures'].append({'segment_id': sid, 'attempt': attempt, 'device': state['device'],
                                          'returncode': result, 'log': str(log_path), 'at': now()})
                if state['device'] == 'mps':
                    state['fallbacks'].append({'from': 'mps', 'to': 'cpu', 'segment_id': sid,
                                               'failed_log': str(log_path), 'at': now()})
                    state['device'] = 'cpu'
                    print(f'{now()} MPS 尝试失败；此后改用CPU，见 {log_path}', flush=True)
                save()
            else:
                state.setdefault('failed_segments', []).append(sid)
            state['pending'].remove(sid)
            save()
        state['status'] = 'complete_with_failures' if state.get('failed_segments') else 'complete'
        state['current_segment'] = None
        save()
        return 1 if state.get('failed_segments') else 0
    except BaseException as error:
        state['status'] = 'stopped' if isinstance(error, KeyboardInterrupt) else 'failed'
        state['error'] = str(error)
        print(f'{now()} 停止: {error}', flush=True)
        raise
    finally:
        if child is not None and child.poll() is None:
            child.terminate()
            try:
                child.wait(10)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait()
        state['child_pid'] = None
        save()
        lock.close()


if __name__ == '__main__':
    sys.exit(main())
