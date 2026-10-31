---
name: review-translation
description: "Use when reviewing a Finnegans Wake draft, checking bilingual fidelity, evaluating annotations and sources, correcting Anglicized Chinese, or comparing verified alternative translations."
---

# 审校译文与注释

先读 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md` 与本批工作包、初译、相关来源。路径均从仓库根目录起算。

## 审校次序

1. **底本**：核起止、词形、标点、版本与原排页行。注明直接查阅和仅据转录之处。新版本读法不能静默替换当前见证。
2. **译义**：逐句核动作、否定、主从、指代和语气；圈出漏译与无据增补。对模糊句法保留分歧，不把解释塞作叙事事实。
3. **声形**：核复合词、重音、节奏、人物／地名叠影和跨段照应。汉语舍掉哪层，注释须明说。首尾改动须联读 003.01 与 628.15–628.16。
4. **出处**：逐注确认来源支持什么。原著、档案、研究意见和社区猜测分开。无法核实的词源、人名或语言链删去断言，降为 `proposal` 或 `uncertain`。
5. **中文**：朗读后删翻译腔。用实义动词，少「的」，不用「之一」凑判断，不添多余「们」；减少被动和空话。不能借润色消除 Joyce 刻意的歧义。
6. **异译与状态**：已有中译只比较核过的原页；项目备选须标项目署名。AI 校对不算人工审校。

## 交付

写 `reports/reviews/<segment-id>.md`，包含范围、所读资料、核对限度、具体问题、建议和未决事项。每项用「词目／问题／依据／建议」交代；有实质问题才提出修改，不为凑数造缺陷。

审校者只写报告，章稿由整合者回写。整合者保留 `draft`，修订 `translation`，并在报告记录采用、未采用及理由。最多两轮定点修订；只剩风格偏好便交付。

AI 实际修订后可标 `revised`，`reviewers` 仍空。`reviewed` 须真实人工核对并留名。自动检查不能证明译义正确。

完成后交 [checkpoint](../checkpoint/SKILL.md)，不能仅因报告存在便判定整章完成。
