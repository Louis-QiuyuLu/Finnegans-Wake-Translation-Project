#!/usr/bin/env python3
"""用本机 GPT-SoVITS 模型生成英文段落音频；发音拆读属于近似方案。"""
import argparse
import hashlib
import shutil
import json
import os
from pathlib import Path
import subprocess
import sys

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


def load_segments():
    chapters_dir = ROOT / "manuscript/chapters"
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


def init_tts_pipeline(model_dir, variant="vertin"):
    os.chdir(TOOLS_DIR)
    sys.path.insert(0, str(TOOLS_DIR))
    sys.path.insert(0, str(TOOLS_DIR / "GPT_SoVITS"))

    import torch
    torch.set_num_threads(8)

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
            "device": "cpu",
            "is_half": False,
            "version": "v4",
            "t2s_weights_path": str(t2s_ckpt),
            "vits_weights_path": str(vits_pth),
            "bert_base_path": "GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large",
            "cnhuhbert_base_path": "GPT_SoVITS/pretrained_models/chinese-hubert-base",
        }
    }
    tts_config = TTS_Config(config_dict)
    return TTS(tts_config)


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
            chunks.append(group_audio)

        # 末尾标点停顿
        if idx == len(sense_groups) - 1:
            pause_sec = max(pause_sec, 0.40)

        chunks.append(np.zeros(int(sr * pause_sec), dtype=np.int16))

    if not chunks:
        return sr, np.zeros(0, dtype=np.int16)

    return sr, np.concatenate(chunks)


def register_audio(segment, audio_dir):
    audio_dir = Path(audio_dir)
    path = audio_dir / "index.json"
    index = json.loads(path.read_text()) if path.exists() else {"engine":"GPT-SoVITS", "language":"en", "tracks":[]}
    entry = {"segment_id":segment["id"], "file":segment["id"]+".mp3", "original_sha256":hashlib.sha256(segment["original"].encode()).hexdigest()}
    index["tracks"] = [t for t in index["tracks"] if t["segment_id"] != segment["id"]] + [entry]
    index["tracks"].sort(key=lambda t: t["segment_id"])
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description="生成 Vertin 英文原文朗读音频")
    parser.add_argument("--force", action="store_true", help="强制覆盖已生成的音频")
    parser.add_argument("--segment", type=str, default="", help="仅生成指定的段落 ID")
    parser.add_argument("--model", type=str, default="sisyphus", choices=["sisyphus", "vertin", "vertin2"], help="模型版本（默认 sisyphus 经《西西弗神话》微调的沉稳哲理英音）")
    parser.add_argument("--speed", type=float, default=1.05, help="语速因子（默认 1.05，默认合成语速1.05倍）")
    parser.add_argument("--steps", type=int, default=32, help="CFM 采样步数（默认 32，采样步数不保证特定音质）")
    parser.add_argument("--ref", type=str, default="sisyphus2", help="参考音频名称（默认 sisyphus2《西西弗神话》深沉澄澈英音）")
    parser.add_argument("--model-dir", type=Path, help="本机模型目录；默认 models/Vertin")
    args = parser.parse_args()

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
    elif args.ref == "e3":
        prompt_text = "I've signed a peace agreement with O'Connor, and the price of breaking it is death. Yes."
    else:
        prompt_text = (model_dir / "references/e1.txt").read_text(encoding="utf-8").strip()

    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    segments = load_segments()
    if args.segment:
        segments = [s for s in segments if s["id"] == args.segment]

    print(f"找到 {len(segments)} 个段落需处理。音色参考: {args.ref}，设定语速: {args.speed}x，CFM步数: {args.steps}")
    tts_pipeline = None

    import soundfile as sf

    for i, seg in enumerate(segments, 1):
        sid = seg["id"]
        mp3_path = AUDIO_DIR / f"{sid}.mp3"
        wav_path = AUDIO_DIR / f"{sid}.wav"

        if mp3_path.exists() and not args.force:
            print(f"[{i}/{len(segments)}] {sid} ({seg['locator']}) 音频已存在，跳过。")
            continue

        print(f"[{i}/{len(segments)}] 正在生成 {sid} ({seg['locator']})...")
        if tts_pipeline is None:
            tts_pipeline = init_tts_pipeline(model_dir, variant=args.model)

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

        sf.write(str(wav_path), full_audio, sample_rate)

        # 转换为广播级高品质 MP3 (192k) 并注入人声母带滤镜：
        # 沿用既有滤镜参数，不声称经过原声声学验证：温润胸腔共振（200Hz +1.5dB）、消除3.2kHz砂砾高频沙哑、统一声学响度（-21.0 LUFS，LRA=3）
        filter_str = "highpass=f=60,equalizer=f=200:t=q:w=1.2:g=1.5,loudnorm=I=-21:TP=-1.5:LRA=3"
        subprocess.run([
            shutil.which("ffmpeg") or "ffmpeg", "-y", "-i", str(wav_path),
            "-af", filter_str,
            "-codec:a", "libmp3lame", "-b:a", "192k", str(mp3_path)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        register_audio(seg, AUDIO_DIR)

        if wav_path.exists():
            wav_path.unlink()

        size_kb = mp3_path.stat().st_size / 1024
        duration = len(full_audio) / sample_rate
        print(f"[{i}/{len(segments)}] 完成 {sid} -> {mp3_path.name} ({duration:.2f}s, {size_kb:.1f} KB)")

    print("全部音频处理完成！")


if __name__ == "__main__":
    main()
