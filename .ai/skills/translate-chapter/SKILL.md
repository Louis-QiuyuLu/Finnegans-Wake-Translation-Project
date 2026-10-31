---
name: translate-chapter
description: "Use when translating or resuming Finnegans Wake in this repository, including sequential chapter work, paragraph batches, wordplay notes, and coordination of translation and review roles."
---

# 逐段译注

先读 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md`、`docs/MANUSCRIPT_FORMAT.md`、`progress/RESUME.md` 与当前断点。路径均从仓库根目录起算。

## 续译入口

1. 比对断点、章稿末段和底本锚句，确认顺序无缺口。IV 篇末样稿不计作前文已译。
2. 没有核对过的原文包，先用 [prepare-source](../prepare-source/SKILL.md)。每批取一至两个完整自然段，不按固定词数割断句法。
3. 只带入相关译名、前文摘要、相邻段落与本批资料。不得靠未读正文补人物关系或全书结论。

## 分工与写入

角色输入、文件归属和交付格式见 [角色约定](references/roles.md)。小批次可按阶段顺序执行；若调度子代理，翻译与审校分开，章节依次推进。

明确每个角色可写哪些文件。译者交完整段落对象，审校者交意见，整合者统一回写章稿、来源与断点。所有角色都须保留他人改动。并发数不得超过当前工具上限，不照搬参考项目十代理批次。

## 初译

- 先听声音，再辨句法，最后查典故。保留否定、时态、动作关系和刻意重复；不先改顺英文再翻译。
- 同时辨认字面、谐音和词形。多义不能全压进正文时，正文择取读路，注释交代其余读法及损失。
- `draft` 保存初译，`translation` 保存当前采用稿。后续修订不抹去初译。
- 每条注释填固定 ID、词目、类别、证据层级和可解析来源。`supported` 只表示来源支持判断；项目推读用 `proposal`，证据不足用 `uncertain`。
- 暂造译词须说明构词理由。新词不因这次采用便成全书定译；术语表只收需要跨段沿用的条目。
- 中文依余光中《中文的常态》修订。删弱动词、空话和多余「的」；缩短句子，同时保存原著刻意连缀、停顿与不完整状态。
- 比较现有译本须核原页并具名。不编造引文、页码或查阅记录。

## 审校与接续

交 [review-translation](../review-translation/SKILL.md) 核原文、出处、中文和译法损失。先处理误译、漏译与无据注释，再处理措辞。最多两轮定点修订；余下分歧写入报告，不为同义词反复重译。

AI 修订可用 `revised`，不得填人工 `reviewers` 或标 `reviewed`。每批合入后用 [checkpoint](../checkpoint/SKILL.md) 保存真实起点，再用 [contribute](../contribute/SKILL.md) 同步已获授权的仓库。未解决问题不自动消失；实质缺口未补齐，不推进断点。
