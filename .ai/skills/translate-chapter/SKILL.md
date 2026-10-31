---
name: translate-chapter
description: "Use when starting or resuming sequential Finnegans Wake translation in this repository, assigning a paragraph batch, resolving a stalled translation handoff, or preparing a draft for separate review."
---

# 逐段译注

先确认本次任务：初译、续译、定点修订，还是章末核对。路径均从仓库根目录起算。公开稿以 `manuscript/chapters/*.json` 为准；工作包、初译与报告只是交接资料。不要改生成目录来交稿。

## 入口与按需阅读

整合者先读 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md`、`docs/SOURCES.md`、`docs/MANUSCRIPT_FORMAT.md`、`progress/RESUME.md`、`progress/checkpoint.json` 和目标章稿。核断点、章稿末段、底本锚句是否相接。IV 篇末样稿不计入顺序进度。

- 首次调度或角色交接：读 [角色与写入归属](references/roles.md)。小批次也沿用这些边界，不必为每个角色另开代理。
- 生成工作包、恢复中断、输入变化或任务失败：读 [冻结与恢复](references/packets-and-recovery.md)。
- 译者首次接段，或处理声形、句法与中文损失：读 [译者工作法](references/translating.md)。
- 没有核过页行与原文：先用 [prepare-source](../prepare-source/SKILL.md)，不把空译文插入章稿。

## 本轮工作

1. **取连续范围。** 通常一至两个完整自然段；长段可分任务研究，交稿仍覆盖整段。不要按词数截断句法、雷鸣词或版面单位。章节按原书顺序推进；当前章未核清正文覆盖，不启动下一章顺序翻译。
2. **备小包。** 每段工作包沿用 `templates/workpack.json`，含固定 ID、坐标、来源、原文、实际核对记录、相关术语与下一锚句。冻结章稿、来源表、术语表基线；另给相关前文摘要、相邻段落和具体问题。只取本段所需资料，不让每位译者重读全书。
3. **先分问题，再动笔。** 普通释义、已核旧术语和不影响译法的细节在包内处理。会改变句法、译词或注释事实的多语词源、典故、作者自释及跨作品照应，交 [joyce-research](../joyce-research/SKILL.md)。研究按 `claim`、`evidence`、`interpretation`、`translation_impact` 分开；整合者核过证据才供正文采用。检索不到可留 `uncertain`，不为追求全解无限扩查。
4. **初译落盘。** 译者只写指定 `reports/drafts/<id>.json` 和交接说明，完整承接工作包 ID、坐标、原文与来源。`draft` 留初译；`translation` 为采用稿；初次 `status` 用 `draft`，`reviewers` 留空。每条注释须有可解析来源，取舍与损失须可追溯。
5. **冻结后独立审校。** 译者完成交稿，再交 [review-translation](../review-translation/SKILL.md)。审校者检查指定版本，只交报告。审校进行时不改该输入；任何新交稿另存版本，并使旧审校结论停止适用于新稿。自检不冒充独立审校。
6. **至多两轮定点修订。** 先改漏译、误译、版本混用与无据断言，再改声形和中文。每轮针对问题编号交新版本，不覆写初译。第二轮后仍有实质缺口，留下未完成交付；不能借轮次上限放行。只剩风格偏好便交付，不反复换同义词。
7. **单一整合者回写。** 对照最新公共稿，逐字段合入本批变化，保留他人新增内容。术语建议交 [maintain-glossary](../maintain-glossary/SKILL.md)，不能用本段清单覆盖全表。整合者统一更新章稿、来源、术语和断点，再用 [checkpoint](../checkpoint/SKILL.md) 保存真实进度。

## 收口门槛

交稿须能解析、范围完整、原文与工作包相符，来源能解析；审校或自检范围须明示。已有报告只在输入版本相符时有效。不能以文件非空、任务返回成功或 `project.py check` 通过代替这些检查；当前工具不核报告语义，也不证明连续覆盖。

原文未核、漏译、伪造来源或冲突尚未解决，阻断该段合入及顺序断点。单条词源或解释存疑，若正文已有保守译法且注明限度，可随初译保存。独立审校暂缺时保留 `pending_review` 工作阶段；授权范围只要求初译，可由整合者合入 `draft`，但不报全流程已完成。AI 修订用 `revised`；只有真实人工审校后才可写 `reviewed` 并留姓名或公开账号。

整章 `coverage: complete` 另须逐项核对全章正文，写 `coverage_review`。首尾改动联读 003.01 与 628.15–628.16，不补成封闭叙事。图形、边注或排版若参与文义，保留并交待格式缺口；不能照搬其他书项目删图或跳过首末规则。

回复交付路径、实际阶段、已合入范围、未决项和下一锚句。仅整合者按 [contribute](../contribute/SKILL.md) 执行已获授权的验证与同步；没有远端结果，不报已上线。
