# I.2–I.3 改注定点复核

## 输入

- role: ai_review。
- executor: OpenAI Codex，原 I.2–I.3 审校子任务实际执行者；不是人工审校。
- date: 2026-11-02。
- workpack: 父任务要求只核整合稿改注及相邻文，不重跑全章或外部研究。
- 前报告：`/private/tmp/fw-book-I-intake-20261102/review-I2-I3.md`；SHA256 `8a2ad3da6052dc6e5df175f08fe3e5a22c8a5865fd3ea001583781dcbef5369b`，保持不动。
- 新稿 I.2：`/private/tmp/fw-full-source-20261101/manuscript/chapters/I-2.json`；SHA256 `7abc29fe830ef5126bc2bfd0ff1f37b50ea64e9988d7ff9dda10a1fc6c039b4c`。
- 新稿 I.3：`/private/tmp/fw-full-source-20261101/manuscript/chapters/I-3.json`；SHA256 `49b31a6c40aed28f27162e41fe8cfeb250faed64e91d4944df50b8ae78c30424`。
- source_id / locator: joyce-fp；本次定点复核 `fw-i3-065-34` / `065.34–067.27` 中棺材、手竖琴句群。
- 该段 original_sha256：`bde84de05d2a408d0a9b7997b14f7c92c18e48592bf5fcb6593a75368d5d450d`，与前次冻结稿相同。

## 范围与差异

已按段 ID 和字段比对两章前次冻结稿与本次整合稿。I.2 全10段没有字段差异；I.3 全12段仅 `fw-i3-065-34.notes` 一处变化，具体为 `n-i3-66-coffin-handharp.text` 删去错误硬币括语。原文、初译和当前译文均未改。章级新增 `source_text` 并改写 `coverage_review`，不据这些说明追加语义验收。

实际重读改后整注及相邻原文、译文，自 `The coffin, a triumph of the illusionist's art` 至 `To proceed.` 前；相邻连环信封注与段末证人注没有改动。未重跑全章通读，没有新增外部研究。

未核范围沿用前报告：精确行号、初版影像、逐注外部事实全面复验。本执行者本次仍未目验乐谱；父任务另核谱面与读本呈现，不能把该工作记在本报告名下。

## 问题处置

### R-I3-NEW-01：已解决

- 旧注：「handharp，兼涉爱尔兰十先令硬币俗称 half-a-crown / harp」。
- 新注：「handharp」。错误面值与无据硬币联想一并删去，没有仅改数字后保留未经证实的词源链。
- 相邻原文仍作 `at first blench naturally taken for a handharp`；译文仍作「乍看之下自然让人当成了一架手竖琴」。删注未改变正文动作，也未引入新人物、币物或关系。
- `certainty: proposal`、lemma 与 `source_ids` 均未改。
- disposition: fixed。
- blocks_integration: false。

本次已核差异未见须改问题。

## 结论

- 当前版本：**ready**，限本报告绑定的整合稿、前报告实际核过且未变的文字范围，以及本次改注。
- I.2 沿用前报告文字语义结论。I.3 原阻断项 R-I3-NEW-01 已解除；无需再开全章重译。
- 本报告与前报告共同构成语义验收依据；谱面、坐标、来源及整卷工程检查由父任务分别收口。本次不改章稿、断点、来源，不推送。
