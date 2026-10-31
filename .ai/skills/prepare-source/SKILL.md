---
name: prepare-source
description: "Use when preparing or checking a Finnegans Wake source passage, importing EPUB or HTML, resolving edition differences, or assigning page-line coordinates before translation."
---

# 核对底本与分段

先读项目根目录 `AGENTS.md`、`docs/SOURCES.md`、`progress/checkpoint.json` 与目标章稿。路径均从仓库根目录起算。

## 输入与交付

输入须含章号、待译起点、文字见证与页行依据。续译从断点锚句开始；若锚句对不上，先查差异，不跳到后文。

交付 `reports/workpacks/<segment-id>.json`，至少含：

- `chapter`、`id`、`locator`、`range`、`source_id`、`original`；段落字段沿用 `docs/MANUSCRIPT_FORMAT.md`。
- `source_checks`：实际查过的 URL、版本、核对结果及差异。未查原页便写明。
- `questions`：词形、声音、句法、典故与待核事项。
- `terms`：本段相关旧译名、暂定新译名及理由。只取相关条目。
- `previous_segment_id`、`next`、`next_original`：前段 ID 与下一段坐标、锚句。

这是交接资料；先不向章稿插入缺少译文的半成品。来源新增项交整合者写入 `sources/catalog.json`。

## 核对顺序

1. 分清通行页行与具体刊本。Faded Page 当前见证为 Viking 1958 年第八印本；JJDA 的 1939、2010 年版须分别核对。
2. 按完整自然段分批，通常一至两段。网页折行不能充当原书行号。去掉排版断字前先核词形，保留作者错拼与缀词。
3. 对照正文起止、标点、重音符号与段界；异文记入工作包。两个转录站一致，也不等于已经查过纸本。
4. 列出可成立的读法，再找原始资料、可靠词典或具名研究。社区注解只作线索；查不到便存疑。
5. 为新增来源登记具体页面与用途。不要把仅看过书目写成读过正文，不凭记忆引用既有中译。

## EPUB 与特殊排版

有 EPUB 时先看目录和 OPF 阅读顺序，区分封面、版权页、正文及附录；必要时在临时目录解包。现有 HTML 足够核对时，无须另装转换工具。转出 Markdown 只是中间稿，最终仍按 JSON 章稿录入。

不能按文件位置跳过首尾篇章。《守灵夜》首尾含正文且相互接续。保留有文义作用的字母符号、图形、边注和版面关系；普通 JSON 段落容不下时，先说明所需格式，不静默删去。

交付后转入 [translate-chapter](../translate-chapter/SKILL.md)。
