---
name: prepare-source
description: "Use when preparing or checking a Finnegans Wake source passage, importing EPUB or HTML, resolving edition differences, or assigning page-line coordinates before translation."
---

# 核对底本与分段

先读项目根目录 `AGENTS.md`、`docs/SOURCES.md`、`progress/checkpoint.json` 与目标章稿。路径均从仓库根目录起算。完整阶段和单写者约定见 `docs/SKILLS_ARCHITECTURE.md`。

## 输入与交付

输入须含章号、待译起点、文字见证与页行依据。续译从断点锚句开始；若锚句对不上，先查差异，不跳到后文。

交付 `reports/workpacks/<segment-id>.json`，从 `templates/workpack.json` 填写。模板为空的字段须用实际核对结果补齐，不能当作已交稿。至少含：

- `chapter`、`id`、`locator`、`range`、`source_id`、`original`；段落字段沿用 `docs/MANUSCRIPT_FORMAT.md`。
- `source_checks`：实际查过的 URL、版本、核对结果及差异。未查原页便写明。
- `questions`：词形、声音、句法、典故与待核事项。
- `terms`：本段相关旧译名、暂定新译名及理由。只取相关条目。
- `previous_segment_id`、`next`、`next_original`：前段 ID 与下一段坐标、锚句。
- `schema_version: 1`、`baseline`：读入的章稿、来源表、术语表路径及 SHA-256，供合入前辨认版本。
- `research_decision`：本批是否需要研究及理由。阶段、负责人、交稿和未决项另记 `reports/batches/<batch-id>.json`，从 `templates/batch.json` 填写，不放进冻结的输入包。

这是交接资料；先不向章稿插入缺少译文的半成品。来源新增项交整合者写入 `sources/catalog.json`。

输入包核好后冻结。后续阶段变化只改批次记录；原文、范围或证据输入确需更正时，保留旧包，另存 `<id>.v2.json` 等版本，并在批次记录指向实际采用包。审校保留它实际读过的包和指纹，不用重算掩盖版本变更。

## 核对顺序

1. 分清通行页行与具体刊本。Faded Page 当前见证为 Viking 1958 年第八印本；JJDA 的 1939、2010 年版须分别核对。
2. 按完整自然段分批，通常一至两段。网页折行不能充当原书行号。去掉排版断字前先核词形，保留作者错拼与缀词。
3. 对照正文起止、标点、重音符号与段界；异文记入工作包。两个转录站一致，也不等于已经查过纸本。
   可按 [外部见证比对](../joyce-research/references/reproducible-investigation.md) 运行 `verify_evidence.py compare`。内部 original 的哈希一致不证明无增句；只核局部须明列范围。网页返回 200 但锚句缺失，先按取证失败处理。
4. 列出可成立的读法，再找原始资料、可靠词典或具名研究。社区注解只作线索；查不到便存疑。
5. 为新增来源登记具体页面与用途。不要把仅看过书目写成读过正文，不凭记忆引用既有中译。

完整录入、差异分类与验收规则见 [底本交接约定](references/source-contract.md)。EPUB、HTML、扫描件和特殊版式按 [导入与校勘](references/import-and-collation.md) 处理。

## 研究交接

新词源、跨作指认、重大典故或中日英解释冲突，交 `.ai/skills/joyce-research/SKILL.md`。给出原句、坐标、候选主张、已有来源与希望影响的译句，不只交一个无上下文单词。

语义未决不等于原文未核。原文确定后可先交来源包，把研究问题单列；关键原文或范围未定则不能称 `source_ready`。研究者不得借新解释静默更换见证本。

## EPUB 与特殊排版

有 EPUB 时先看目录和 OPF 阅读顺序，区分封面、版权页、正文及附录；必要时在临时目录解包。现有 HTML 足够核对时，无须另装转换工具。转出 Markdown 只是中间稿，最终仍按 JSON 章稿录入。

不能按文件位置跳过首尾篇章。《守灵夜》首尾含正文且相互接续。保留有文义作用的字母符号、图形、边注和版面关系；普通 JSON 段落容不下时，先说明所需格式，不静默删去。

## 关口与失败

整合者须重新打开工作包核：锚句、完整自然段、版本、坐标、原文、来源和下一起点。`project.py check` 不查此包，不能拿公共稿的格式检查代替这一步。

请求超时先重试同一小页或换可核的机构入口；不要因转录站暂不可达改用另一个版本拼接。只有二手见证时注明限度，原页缺失不补假页码。重复失败或语义无法辨认时保留工作包、当前锚句和所缺资料，主断点不前移。

交付后转入 [translate-chapter](../translate-chapter/SKILL.md)。
