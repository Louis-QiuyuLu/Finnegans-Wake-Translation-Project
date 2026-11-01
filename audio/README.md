# 英文朗读

网页播放离线生成的 GPT-SoVITS 英文 MP3，无需运行本机模型或开放推理服务。每段使用浏览器原生播放、暂停、进度及音量控件；顶部阅读设置可选语速。音频按需加载，一次只播放一段。

`index.json` 登记九段已采用录音。`original_sha256` 绑定网页对应原文，防止后续改字后静默沿用旧录音；初次登记不等于逐字转写或音质审校。合成使用近似读音，不代表作者指定读法。页面标签为「GPT-SoVITS · 重返未来1999 瓦尔汀」，提示文字注明 AI 合成。首次播放默认1×；手动选择的语速只保存在当前浏览器。

`original_sha256` 校验原文字串，不校验 MP3 文件内容。当前清单没有逐段记录 MP3 哈希、时长、模型权重或训练来源，不能单凭原文指纹确认录音完整或反推模型。两份合并录音另经文件哈希与时长复核，见 [阶段复核记录](../reports/reviews/gemini-book-I-2026-11-01/PHASE1-R1B-REVIEW.md)。

005.13–006.12 和006.13–007.15各由两份现有录音按顺序拼接，重编码为192kbps；未重新生成语音。007.16–008.04的原文修正Brunto，旧录音暂未登记。测试片段、参考音频、模型、训练集与GPT-SoVITS工具目录不随网站发布。

构建只复制清单内MP3；缺失、空文件或原文字串改变会中止检查。段落没有录音时，不显示空播放器。EPUB保留文字，不嵌入网页播放器或音频。

## 继续生成

生成语音另需完整的 GPT-SoVITS v4 环境及其预训练组件、PyTorch、NumPy、SoundFile，以及支持 `libmp3lame` 的 FFmpeg。它们不属于读本构建所需的 Python 标准库环境。

工具放在 `tools/gpt_sovits`，模型默认放 `models/Vertin`，也可用 `--model-dir` 指定**绝对路径**。当前目录检查要求同时存在 `Vertin-e10.ckpt` 与 `Vertin_e2_s154_l32.pth`；使用 `vertin2` 时还需该变体的两份权重。

脚本默认选 `sisyphus`，按 `Vertin-Sisyphus-v95.ckpt` → `Vertin-Sisyphus-e9.ckpt` → `Vertin-e10.ckpt` 回退，声学权重仍为 `Vertin_e2_s154_l32.pth`。默认参考为 `references/sisyphus2.wav`，不是仓库自带资源；缺失时不会自动换成 `e1.wav`，而会中止。参考提示文本优先读同名 `.txt`，除 `e3` 特例外，缺失或为空时改读 `references/e1.txt`。使用者应核对提示文本与参考录音一致。

若已备好原版 Vertin 权重及 `references/e1.wav`、`references/e1.txt`，可显式运行：

```bash
python3 scripts/generate_audio.py --model-dir /path/to/model --model vertin --ref e1 --segment fw-i1-007-16 --force
```

`--segment` 须指向公共章稿中实际存在的段落。已有同名 MP3 时，脚本默认跳过；`--force` 会覆盖该段音频。成功生成后，脚本登记该段原文与文件，保留其他记录。原文更改后须重新生成，不能只换清单指纹。

合成默认 `--speed 1.05 --steps 32`；网页默认播放1×是另一项设置。脚本先按意群合成，再经滤镜与响度处理转成192kbps MP3；参数不代表音质已获验证。`scripts/joyce_phonetics.py` 保存合成试验的发音近似方案，修改后须实听，不能当作已核定的语音词典。本次文档核对未重新运行模型或生成录音。
