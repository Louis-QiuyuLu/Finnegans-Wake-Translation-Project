#!/usr/bin/env python3
"""串行续生成第一卷；冻结原文，保留现有有效录音。"""
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
from scripts.generate_audio import AUDIO_DIR, atomic_json, audio_is_current, load_segments, original_hash

PRIORITY = ['fw-i3-067-28', 'fw-i3-069-30', 'fw-i3-072-17']


def now():
    return datetime.now(timezone.utc).isoformat()


def book_one(chapters_dir=None):
    return [s for s in load_segments(chapters_dir) if s['chapter'].startswith('I.')]


def check_originals(frozen, current):
    expected = {s['id']: original_hash(s) for s in frozen}
    actual = {s['id']: original_hash(s) for s in current}
    if expected != actual:
        changed = sorted(sid for sid in expected.keys() | actual.keys() if expected.get(sid) != actual.get(sid))
        raise RuntimeError('原文已改变，停止批处理；请核对后另建运行目录: ' + ', '.join(changed))


def build_queue(segments, audio_dir=AUDIO_DIR):
    pending = [s for s in segments if not audio_is_current(s, audio_dir)]
    rank = {sid: i for i, sid in enumerate(PRIORITY)}
    return sorted(pending, key=lambda s: (rank.get(s['id'], len(rank)), segments.index(s)))


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
    args = parser.parse_args()
    if not 1 <= args.attempts <= 3 or args.segment_timeout <= 0:
        parser.error('attempts 须为1至3；timeout 须大于0')
    args.run_dir.mkdir(parents=True, exist_ok=True)
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    lock = (AUDIO_DIR / '.batch.lock').open('a')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit('已有音频批处理运行')
    lock.seek(0)
    lock.truncate()
    lock.write(str(os.getpid()) + '\n')
    lock.flush()
    state_path = args.run_dir / 'state.json'
    frozen_path = args.run_dir / 'originals.json'
    candidate_dir = (args.run_dir / "candidates").resolve()
    child = None
    state = {'pid': os.getpid(), 'started_at': now(), 'status': 'starting', 'current_segment': None,
             'device': args.device, 'review_status': 'pending', 'candidate_dir': str(candidate_dir), 'parameters': {'model': args.model, 'ref': args.ref,
             'speed': args.speed, 'steps': args.steps, 'segment_timeout': args.segment_timeout,
             'attempts': args.attempts}, 'successes': [], 'failures': [], 'fallbacks': []}

    def save():
        state['updated_at'] = now()
        atomic_json(state_path, state)

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
            frozen = book_one()
            atomic_json(frozen_path, frozen)
        check_originals(frozen, book_one())
        official_queue = build_queue(frozen, AUDIO_DIR)
        queue = [s for s in official_queue if not audio_is_current(s, candidate_dir)]
        state['total_book_I'] = len(frozen)
        state['already_current'] = len(frozen) - len(official_queue)
        state['already_quarantined'] = len(official_queue) - len(queue)
        state['pending'] = [s['id'] for s in queue]
        state['status'] = 'running'
        save()
        print(f"{now()} PID={os.getpid()} 第一卷共{len(frozen)}段；待生成{len(queue)}段，device={args.device}", flush=True)
        for segment in queue:
            check_originals(frozen, book_one())
            sid = segment['id']
            if audio_is_current(segment, AUDIO_DIR) or audio_is_current(segment, candidate_dir):
                state['pending'].remove(sid)
                save()
                continue
            state['current_segment'] = sid
            state['original_sha256'] = original_hash(segment)
            for attempt in range(1, args.attempts + 1):
                log_path = args.run_dir / f'{sid}-pid-{os.getpid()}-attempt-{attempt}-{state["device"]}.log'
                command = [sys.executable, '-u', str(ROOT / 'scripts/generate_audio.py'), '--segment', sid,
                           '--model', args.model, '--ref', args.ref, '--device', state['device'],
                           '--speed', str(args.speed), '--steps', str(args.steps),
                           '--expected-original-sha256', original_hash(segment), '--audio-dir', str(candidate_dir)]
                state.update({'attempt': attempt, 'segment_log': str(log_path), 'command': command})
                print(f'{now()} 开始 {sid} attempt={attempt} device={state["device"]} log={log_path}', flush=True)
                began = time.monotonic()
                with log_path.open('a', encoding='utf-8') as output:
                    child = subprocess.Popen(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
                    state['child_pid'] = child.pid
                    save()
                    while child.poll() is None:
                        check_originals(frozen, book_one())
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
