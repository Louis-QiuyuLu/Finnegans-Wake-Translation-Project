#!/usr/bin/env python3
"""用本机 GPT-SoVITS 模型生成英文段落音频；发音拆读属于近似方案。"""
import argparse
from contextlib import contextmanager
import fcntl
from datetime import datetime, timezone
import tempfile
import hashlib
import shutil
import json
import os
from pathlib import Path
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
TOOLS_DIR = ROOT / "tools/gpt_sovits"
AUDIO_DIR = ROOT / "audio"

MODEL_DIRS = [
    ROOT / "models/Vertin",
]


def find_model_dir(preferred=None):
    for d in ([Path(preferred)] if preferred else MODEL_DIRS):
        if (d / "Vertin-e10.ckpt").exists() and (d / "Vertin_e2_s154_l32.pth").exists():
            return d
    raise FileNotFoundError("未找到模型，请用 --model-dir 指定模型目录。")


def load_segments(chapters_dir=None):
    chapters_dir = Path(chapters_dir) if chapters_dir else ROOT / "manuscript/chapters"
    segments = []
    for chapter_file in sorted(chapters_dir.glob("*.json")):
        with open(chapter_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        for seg in data.get("segments", []):
            segments.append({
                "id": seg["id"],
                "chapter": data["id"],
                "locator": seg.get("locator", ""),
                "original": seg["original"],
            })
    return segments


def checkpoint_model_kind(checkpoint, detected):
    config = checkpoint.get("config", {})
    config = config if isinstance(config, dict) else vars(config)
    model = config.get("model", {})
    model = model if isinstance(model, dict) else vars(model)
    model_version = model.get("version")
    rank = checkpoint.get("lora_rank", 0)
    weights = checkpoint.get("weight", {})
    if (model_version == "v4" and isinstance(rank, int) and rank > 0
            and any(key.startswith("cfm.") and ".lora_A." in key for key in weights)):
        return ("v2", "v4", True)
    return tuple(detected)


def init_tts_pipeline(model_dir, variant="vertin", device="cpu"):
    os.chdir(TOOLS_DIR)
    sys.path.insert(0, str(TOOLS_DIR))
    sys.path.insert(0, str(TOOLS_DIR / "GPT_SoVITS"))

    import torch
    torch.set_num_threads(8)
    if device == "mps" and not torch.backends.mps.is_available():
        raise RuntimeError("MPS 不可用")
    print(f"正在加载模型，device={device}", flush=True)

    from GPT_SoVITS.TTS_infer_pack.TTS import TTS, TTS_Config

    if variant == "sisyphus":
        t2s_ckpt = model_dir / "Vertin-Sisyphus-v95.ckpt"
        if not t2s_ckpt.exists():
            t2s_ckpt = model_dir / "Vertin-Sisyphus-e9.ckpt"
        if not t2s_ckpt.exists():
            t2s_ckpt = model_dir / "Vertin-e10.ckpt"
        vits_pth = model_dir / "Vertin_e2_s154_l32.pth"
    elif variant == "vertin2":
        t2s_ckpt = model_dir / "Vertin2-e15.ckpt"
        vits_pth = model_dir / "Vertin2_e3_s237_l32.pth"
    else:
        t2s_ckpt = model_dir / "Vertin-e10.ckpt"
        vits_pth = model_dir / "Vertin_e2_s154_l32.pth"

    config_dict = {
        "custom": {
            "device": device,
            "is_half": False,
            "version": "v4",
            "t2s_weights_path": str(t2s_ckpt),
            "vits_weights_path": str(vits_pth),
            "bert_base_path": "GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large",
            "cnhuhbert_base_path": "GPT_SoVITS/pretrained_models/chinese-hubert-base",
        }
    }
    tts_config = TTS_Config(config_dict)
    # Legacy ZIP LoRA files lack the newer two-byte version header. The upstream
    # size heuristic then misidentifies this 72 MB v4 adapter as a full v1 model.
    # Correct this exact path from its metadata, without editing source or weights.
    import importlib
    module = importlib.import_module("GPT_SoVITS.TTS_infer_pack.TTS")
    from process_ckpt import load_sovits_new
    detector = module.get_sovits_version_from_path_fast
    detected = detector(str(vits_pth))
    kind = checkpoint_model_kind(load_sovits_new(str(vits_pth)), detected)
    if kind != tuple(detected):
        print(f"权重元数据兼容: {tuple(detected)} -> {kind}; {vits_pth}", flush=True)
        target = vits_pth.resolve()
        def compatible_detector(path):
            return kind if Path(path).resolve() == target else detector(path)
        module.get_sovits_version_from_path_fast = compatible_detector
    try:
        pipeline = TTS(tts_config)
    finally:
        module.get_sovits_version_from_path_fast = detector
    print(f"模型加载完成，device={pipeline.configs.device}", flush=True)
    return pipeline


def validate_group_audio(text, duration_sec, mean, rms):
    # Broad anomaly bounds, not a substitute for listening or transcription.
    maximum = max(12.0, 1.4 * len(text.split()) + 3.0)
    if duration_sec <= 0 or duration_sec > maximum:
        raise RuntimeError(f"合成时长异常，隔离待查: {duration_sec:.2f}s / {text[:100]}")
    if rms <= 0 or abs(mean) / rms >= 0.95:
        raise RuntimeError(f"合成波形近乎直流或无声，隔离待查: {text[:100]}")


def synthesize_segment(tts, original_text, ref_audio, prompt_text, speed=1.05, steps=32):
    """
    分意群合成并按标点符号与语法意群注入自然呼吸停顿，按既有方案加入停顿，效果须实听。
    """
    import numpy as np
    from scripts.joyce_phonetics import segment_into_sense_groups

    sense_groups = segment_into_sense_groups(original_text)
    sr = 48000
    chunks = []

    # 段首微停 (0.06s)
    chunks.append(np.zeros(int(sr * 0.06), dtype=np.int16))

    for idx, (group_text, pause_sec) in enumerate(sense_groups):
        print(f"意群 {idx + 1}/{len(sense_groups)}: {group_text[:100]}", flush=True)
        if idx == len(sense_groups) - 1:
            pause_sec = max(pause_sec, 0.40)
        if group_text.strip() and all(
                char.isspace() or unicodedata.category(char).startswith("P") for char in group_text):
            print(f"纯标点意群，保留 {pause_sec:.2f}s 停顿。", flush=True)
            chunks.append(np.zeros(int(sr * pause_sec), dtype=np.int16))
            continue
        inputs = {
            "text": group_text,
            "text_lang": "en",
            "ref_audio_path": str(ref_audio),
            "prompt_text": prompt_text,
            "prompt_lang": "en",
            "top_k": 15,
            "top_p": 1.0,
            "temperature": 0.70,
            "text_split_method": "cut0",  # 已由意群预切分，内部不再二次碎切
            "batch_size": 1,
            "speed_factor": speed,
            "sample_steps": steps,
            "fragment_interval": 0.0,
            "return_fragment": False,
        }

        group_audio = None
        for out_sr, fragment in tts.run(inputs):
            sr = out_sr
            group_audio = fragment

        if group_audio is not None and len(group_audio) > 0:
            values = group_audio.astype(np.float64)
            validate_group_audio(group_text, len(group_audio) / sr, float(values.mean()),
                                 float(np.sqrt(np.mean(values * values))))
            chunks.append(group_audio)
        else:
            raise RuntimeError(f"意群未生成语音: {group_text[:100]}")

        chunks.append(np.zeros(int(sr * pause_sec), dtype=np.int16))

    if not chunks:
        return sr, np.zeros(0, dtype=np.int16)

    return sr, np.concatenate(chunks)


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def original_hash(segment):
    return hashlib.sha256(segment["original"].encode("utf-8")).hexdigest()


@contextmanager
def audio_index_lock(audio_dir):
    audio_dir = Path(audio_dir)
    audio_dir.mkdir(parents=True, exist_ok=True)
    # Keep the lock inode in place; deleting it would split concurrent writers.
    with (audio_dir / ".index.lock").open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def atomic_json(path, data):
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix="." + path.name + ".", suffix=".tmp", delete=False) as handle:
        temporary = Path(handle.name)
        try:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def _register_audio_unlocked(segment, audio_dir):
    path = Path(audio_dir) / "index.json"
    index = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"engine": "GPT-SoVITS", "language": "en", "tracks": []}
    entry = {"segment_id": segment["id"], "file": segment["id"] + ".mp3",
             "original_sha256": original_hash(segment)}
    index["tracks"] = [t for t in index["tracks"] if t["segment_id"] != segment["id"]] + [entry]
    index["tracks"].sort(key=lambda t: t["segment_id"])
    atomic_json(path, index)


def register_audio(segment, audio_dir):
    with audio_index_lock(audio_dir):
        _register_audio_unlocked(segment, audio_dir)


def audio_is_current(segment, audio_dir=AUDIO_DIR):
    audio_dir = Path(audio_dir)
    with audio_index_lock(audio_dir):
        index_path = audio_dir / "index.json"
        if not index_path.exists():
            return False
        index = json.loads(index_path.read_text(encoding="utf-8"))
        matches = [t for t in index.get("tracks", []) if t["segment_id"] == segment["id"]]
        if len(matches) != 1:
            return False
        track = matches[0]
        path = audio_dir / track["file"]
        return (track.get("original_sha256") == original_hash(segment)
                and path.is_file() and path.stat().st_size > 0)


def publish_audio(segment, candidate, audio_dir=AUDIO_DIR, current_segments=None):
    candidate = Path(candidate)
    if not candidate.is_file() or candidate.stat().st_size == 0:
        raise ValueError("MP3 文件为空")
    with audio_index_lock(audio_dir):
        current = load_segments() if current_segments is None else current_segments
        matches = [s for s in current if s["id"] == segment["id"]]
        if len(matches) != 1 or matches[0]["original"] != segment["original"]:
            raise RuntimeError(f"原文已改变，停止登记: {segment['id']}")
        candidate.replace(Path(audio_dir) / (segment["id"] + ".mp3"))
        _register_audio_unlocked(segment, audio_dir)


def main():
    parser = argparse.ArgumentParser(description="生成 Vertin 英文原文朗读音频")
    parser.add_argument("--force", action="store_true", help="强制覆盖已生成的音频")
    parser.add_argument("--segment", type=str, default="", help="仅生成指定的段落 ID")
    parser.add_argument("--model", type=str, default="sisyphus", choices=["sisyphus", "vertin", "vertin2"], help="模型版本（默认 sisyphus 经《西西弗神话》微调的沉稳哲理英音）")
    parser.add_argument("--speed", type=float, default=1.05, help="语速因子（默认 1.05，默认合成语速1.05倍）")
    parser.add_argument("--steps", type=int, default=32, help="CFM 采样步数（默认 32，采样步数不保证特定音质）")
    parser.add_argument("--ref", type=str, default="sisyphus2", help="参考音频名称（默认 sisyphus2《西西弗神话》深沉澄澈英音）")
    parser.add_argument("--model-dir", type=Path, help="本机模型目录；默认 models/Vertin")
    parser.add_argument("--device", choices=["cpu", "mps"], default="cpu")
    parser.add_argument("--expected-original-sha256", help="批处理冻结原文指纹；不符则中止")
    parser.add_argument("--audio-dir", type=Path, default=AUDIO_DIR, help="输出目录；批处理另存候选录音")
    args = parser.parse_args()
    audio_dir = args.audio_dir.resolve()

    model_dir = find_model_dir(args.model_dir)

    # 1. 注入发音词典
    from scripts.joyce_phonetics import update_engdict_hot
    update_engdict_hot(TOOLS_DIR)

    # 2. 读取参考音频与提示文本
    ref_audio = model_dir / f"references/{args.ref}.wav"
    ref_text_file = model_dir / f"references/{args.ref}.txt"
    if not ref_audio.exists():
        raise FileNotFoundError(f"缺少参考音频文件: {ref_audio}")

    if ref_text_file.exists() and ref_text_file.stat().st_size > 0:
        prompt_text = ref_text_file.read_text(encoding="utf-8").strip()
        prompt_source = str(ref_text_file)
    elif args.ref == "e3":
        prompt_source = "builtin:e3"
        prompt_text = "I've signed a peace agreement with O'Connor, and the price of breaking it is death. Yes."
    else:
        prompt_source = str(model_dir / "references/e1.txt")
        prompt_text = Path(prompt_source).read_text(encoding="utf-8").strip()

    audio_dir.mkdir(parents=True, exist_ok=True)
    segments = load_segments()
    if args.segment:
        segments = [s for s in segments if s["id"] == args.segment]
        if len(segments) != 1:
            raise ValueError(f"段落不存在或重复: {args.segment}")
    if args.expected_original_sha256:
        if len(segments) != 1 or original_hash(segments[0]) != args.expected_original_sha256:
            raise RuntimeError("原文与批处理冻结指纹不符")

    print(f"找到 {len(segments)} 个段落需处理。音色参考: {args.ref}，设定语速: {args.speed}x，CFM步数: {args.steps}")
    tts_pipeline = None

    import soundfile as sf

    for i, seg in enumerate(segments, 1):
        sid = seg["id"]
        mp3_path = audio_dir / f"{sid}.mp3"


        if not args.force and audio_is_current(seg, audio_dir):
            print(f"[{i}/{len(segments)}] {sid} ({seg['locator']}) 录音非空且原文指纹相符，跳过。")
            continue

        print(f"[{i}/{len(segments)}] 正在生成 {sid} ({seg['locator']})...")
        if tts_pipeline is None:
            tts_pipeline = init_tts_pipeline(model_dir, variant=args.model, device=args.device)

        sample_rate, full_audio = synthesize_segment(
            tts_pipeline,
            seg["original"],
            ref_audio,
            prompt_text,
            speed=args.speed,
            steps=args.steps,
        )

        if len(full_audio) == 0:
            print(f"警告: {sid} 未生成任何音频数据！")
            continue

        # Both temporary media files stay on the destination filesystem.
        with tempfile.TemporaryDirectory(prefix=".generate-", dir=audio_dir) as temporary:
            wav_path = Path(temporary) / "speech.wav"
            candidate = Path(temporary) / "speech.mp3"
            sf.write(str(wav_path), full_audio, sample_rate)
            filter_str = "highpass=f=60,equalizer=f=200:t=q:w=1.2:g=1.5,loudnorm=I=-21:TP=-1.5:LRA=3"
            subprocess.run([
                shutil.which("ffmpeg") or "ffmpeg", "-y", "-i", str(wav_path),
                "-af", filter_str, "-codec:a", "libmp3lame", "-b:a", "192k", str(candidate)
            ], stdout=subprocess.DEVNULL, check=True)
            provenance = {
                "segment_id": sid, "original_sha256": original_hash(seg),
                "audio_sha256": file_hash(candidate), "review_status": "pending",
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "actual_device": str(tts_pipeline.configs.device),
                "model_version": tts_pipeline.configs.version,
                "prompt_text_source": prompt_source,
                "prompt_text_sha256": hashlib.sha256(prompt_text.encode("utf-8")).hexdigest(),
                "parameters": {"model": args.model, "ref": args.ref, "speed": args.speed,
                               "steps": args.steps, "sample_rate": sample_rate,
                               "duration_sec": len(full_audio) / sample_rate},
                "assets": [{"path": str(path), "sha256": file_hash(path)} for path in
                           [Path(tts_pipeline.configs.t2s_weights_path),
                            Path(tts_pipeline.configs.vits_weights_path), ref_audio]
                           + ([Path(prompt_source)] if Path(prompt_source).is_file() else [])],
            }
            atomic_json(audio_dir / (sid + ".provenance.json"), provenance)
            publish_audio(seg, candidate, audio_dir)

        size_kb = mp3_path.stat().st_size / 1024
        duration = len(full_audio) / sample_rate
        print(f"[{i}/{len(segments)}] 完成 {sid} -> {mp3_path.name} ({duration:.2f}s, {size_kb:.1f} KB)")

    print("全部音频处理完成！")


if __name__ == "__main__":
    main()
