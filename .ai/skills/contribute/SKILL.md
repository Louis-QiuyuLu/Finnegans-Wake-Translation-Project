---
name: contribute
description: "Use when incorporating reader corrections, editing the canonical Finnegans Wake manuscript, preparing a contribution, or synchronizing reviewed project changes to GitHub and the online reader."
---

# 合入修订与同步 GitHub

先读 `AGENTS.md`、`CONTRIBUTING.md`、本批报告与现有差异。路径均从仓库根目录起算。

## 定位与修订

1. 用户指出译句时，用段落 ID 或页行定位 `manuscript/chapters/*.json`。对照当前原文、译注和上下文，不直接改 `polish/dev/` 或其他生成稿。
2. 先辨错译、异译还是中文修订。说明字面、背景及取舍；语义不明且会改变正文时才询问，独立工作照常推进。
3. 保留原文、初译、来源和真实审校状态。底本更正须登记依据；新注释不能借旧来源掩盖未核判断。
4. 沿用用户已经授权的翻译、修订和同步范围，不因参考项目另设重复确认。新操作超出授权时，再说明具体动作与所需决定。

## 验证

```bash
python3 scripts/project.py check
python3 -m unittest discover -s tests -v
python3 scripts/project.py build
python3 scripts/project.py check-artifacts
```

改阅读器逻辑时另跑 `node --test tests/test_reader_model.cjs`。核差异中的原文、ID、来源、状态、断点、生成稿与新增文件；不提交 `dist/`、整部外部电子书缓存或凭据。

## 同步

- 普通外部贡献用分支与 PR，分支可用 `codex/` 前缀。用户已授权向自有仓库连续同步时，沿用约定的发布分支。
- 提交前读取远端最新版本。若远端已变，合并他人改动并重查；更新引用须匹配刚读过的提交，不强推覆盖。
- GitHub 连接器具备写入能力时优先用它；没有凭据时不得把本地提交说成已上传。
- 提交说明写明章、页行、底本、实质修改、验证结果和未决问题。不编造模型、费用、token 或人工审校记录。
- 确认远端稿件和部署结果。Pages 尚在构建便报构建中；网页尚未更新便不声称已经上线。

公开读本由 `main` 自动构建；本机试改不等于仓库修订。最终交付给出可用网页或提交链接，以及下一断点。
