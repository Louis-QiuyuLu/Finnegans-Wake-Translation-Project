# 本仓库协作规则

## 中文编辑

严格遵循余光中《中文的常态》。用实义动词，减少弱动词；少用「的」；避免「之一」；减少「被」字句；删除空话；不用多余的复数后缀；缩短句子。译文、注释、文档、提交说明与答复均须检查。

## 稿件与译注

1. 开始前阅读 `docs/EDITORIAL_GUIDE.md`、`docs/SOURCES.md` 与目标章稿。
2. 原文、译文、译注和译名以 `manuscript/chapters/*.json`、`sources/catalog.json`、`glossary/terms.json` 为准。其他阶段目录由工具生成。底本工作包、初译交稿、审校报告和上下文摘要存于 `reports/`，不绕过章稿直接发布。
3. 每段保留固定 ID、页行坐标与底本来源。纠正录入错误时写明依据，不静默混入其他版本。
4. 注释逐条给出处。推测标 `proposal`，存疑标 `uncertain`。不得虚构词源、文献、页码、查阅记录或译者署名。
5. 先查词形、声音与上下文，再动笔。多义处不能只留单义释文；译法损失写进注释。
6. 初译用 `draft`，修订用 `revised`。只有真实审校者检查后才能写 `reviewed` 并填写 `reviewers`。
7. 有试译不等于整章完成；`coverage: complete` 须有覆盖核对说明 `coverage_review`。
8. 首尾接缝两处联动检查。未核对全章，不擅补叙事关系。
9. 续译前先读 `progress/RESUME.md` 和 `progress/checkpoint.json`。从锚句续接，不跳过正文。每轮更新断点；每章完整录入并核对覆盖后，生成 `progress/chapters/` 章节记录，与稿件一起提交。

## 项目技能入口

以下技能随仓库保存；按任务读取对应 `SKILL.md`，无需安装到全局目录。路径从仓库根目录起算。

- 核底本、导入 EPUB／HTML、划页行：`.ai/skills/prepare-source/SKILL.md`。
- 开始或继续翻译：`.ai/skills/translate-chapter/SKILL.md`，另读其 `references/roles.md`。
- 核译义、出处、中文和异译：`.ai/skills/review-translation/SKILL.md`。
- 保存、恢复、章末覆盖核对：`.ai/skills/checkpoint/SKILL.md`。
- 合入读者意见、检查和同步：`.ai/skills/contribute/SKILL.md`。

顺序为：核底本 → 初译 → 审校与修订 → 保存断点 → 检查并同步。整合者统一回写公共章稿；委派任务须明确输入、输出与可写文件，并保留他人改动。

## 验证与提交

```bash
python3 scripts/project.py check
python3 -m unittest discover -s tests -v
python3 scripts/project.py build
python3 scripts/project.py check-artifacts
```

提交时包含更新后的便读稿、译注和进度清单。不得提交密钥、口令、整部外部电子书缓存或 `dist/`。首次工程初始化沿用 main；后续修改可用 `codex/` 前缀分支，通过 PR 审阅。
