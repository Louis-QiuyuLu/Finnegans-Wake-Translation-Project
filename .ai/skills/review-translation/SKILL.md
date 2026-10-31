---
name: review-translation
description: "Use when reviewing a Finnegans Wake draft or revision in this repository, checking annotation evidence, diagnosing a disputed reading, or deciding whether a review still applies after its input changed."
---

# 审校译文与注释

先读 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md`、`docs/SOURCES.md`、`docs/MANUSCRIPT_FORMAT.md` 与指定工作包、待审稿和相关来源。路径均从仓库根目录起算。只审分配版本；只写报告，不改输入、公共章稿或断点。

报告格式、问题处置、过期重核与两轮收敛见 [审校协议](references/review-protocol.md)。同段初译者若随后自检，报告标 `self_check`；独立审校须由另一位实际执行者完成。AI 审校不等于人工审校。

## 核对次序

1. **输入与范围。** 先核 ID、坐标、来源和原文是否吻合工作包，记录工作包、原文与实际待审 JSON 的 SHA256。只核注释便声明局部范围；不能把局部复核写成全段通过。输入改动后，旧报告仅供追溯。
2. **底本与译义。** 核起止、词形、标点和见证版本；逐句核动作、否定、连接、指代、语气及刻意空缺。记录漏译、无据增补和强加关系。新版本不能静默换入，歧义不能因一种解释较顺便消失。
3. **声形与中文。** 核混合词、音形叠合、节奏、重复和语域；说明中文保留与舍弃哪层。依余光中规则删弱动词、空话、多余「的」「们」和不必要被动，缩短句子；不借润色抹掉原文连缀或未完成状态。改首尾须联读 003.01 与 628.15–628.16。
4. **逐注证据。** 确认每条来源究竟支持哪句；原著、档案、具名研究和社区线索分开。`supported` 不表示作者意图已证实。无据词源、人名关系和语言链删断言或降级；来源 ID 能解析不等于来源支持主张。
5. **术语与异译。** 术语表约束具体语境，不强制 HCE／ALP 每处同译或同一身份。问题交 [maintain-glossary](../maintain-glossary/SKILL.md) 形成增量。已有中译只比实际核过的原页；本项目备选须明示署名与取舍。

若既有证据不足且结论会改正文或注释，交 [joyce-research](../joyce-research/SKILL.md) 定点核查。研究交稿须分 `claim`、`evidence`、`interpretation`、`translation_impact`；核过证据再采信，不凭摘要升格事实。英、中、日研究互查可用于实质争议；普通释义与措辞不机械另开三语检索。

## 交付与放行

只写分配的 `reports/reviews/<id>.r0.md` 或 `.r1.md`、`.r2.md`。报告绑定输入，按稳定问题编号写「词目／问题／依据／建议／是否阻断」，列所读资料、实际核对范围、未核项与结论。无实质问题便直接说明，不凑缺陷，也不整段重译。

整合者与译者在交接说明逐项记录采用、未采用、补证或延期及理由；保留初译，另交修订版本。初译后最多两轮定点修订。两轮后仍漏译、混本或使用假来源，交 `blocked` 报告；只剩风格偏好或已明示的学术分歧，可收口。一般解释存疑已有保守译法时，可留 `uncertain`，不拖成无限研究。

AI 实际修订后公共稿可用 `revised`，不自填人工 `reviewers`。既有已审段落发生内容改动，整合者撤销当前稿的已审标记，历史留在版本记录。全段审校通过也不能证明整章覆盖；断点与章末由 [checkpoint](../checkpoint/SKILL.md) 另核。
