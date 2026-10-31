---
name: maintain-glossary
description: "Use when a Finnegans Wake batch introduces a recurring name, acronym, or coined term, when a review disputes an existing glossary entry, or when glossary proposals conflict with a newer shared table."
---

# 术语增量与语境清单

先读 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md`、`docs/SOURCES.md`，再读指定工作包、相关旧条目和本轮建议。路径从仓库根目录起算。只做术语判断与交接，不翻正文、不改公共表或断点；整合者统一写 `glossary/terms.json`。

候选格式、现有字段兼容、变体与三方合并见 [增量合同](references/delta-and-merge.md)。没有新术语或范围冲突时，整合者沿用相关条目即可，不为每段固定启动维护任务。

## 输入与核对

1. 用工作包固定章号、段 ID、坐标和原文。记录 `baseline.glossary` 与实际所读术语表版本；候选须能指出来自哪段、哪版审校或哪条研究。
2. 筛跨段需要沿用的专名、字母组、复合词与构词约定。孤立普通释义留段注，不把词典全部搬进表。只检索本批词形及必要别名；小表可整读，大表按词形提取，不要求每次通读全书。
3. 分清既有条目在此处适用、此处例外、需补变体，还是确有事实错误。统一译名不等于强制同字同义；HCE／ALP 等字母组不能一律扩成固定人物名。
4. 核实际来源支持的范围。既有译本只证明有人这样译，不自动证明解释正确。地名、宗教、歌曲、历史机构等只查与本词相关问题；不套别书专名规则。
5. 会改变正文或注释、而现有证据不足的主张，交 [joyce-research](../joyce-research/SKILL.md) 定点核查。英、中、日研究用于互查；其他语言按实际词源再查。读回时分清 `claim`、`evidence`、`interpretation`、`translation_impact`，不把研究建议直接升成事实。

## 两份交付

只写分配的 `reports/glossary/<batch-id>.delta.json` 和 `<batch-id>.terms.md`。

增量 JSON 记录基线、逐条 `add/update` 操作、完整旧值与候选新值、依据、适用范围和受影响段落。保留未决冲突，不交整张替换表。候选 `after` 沿用现有 `term/translation/status/note/source_ids`；范围、变体定位和研究证据留在增量或写入 `note`，不能暗加公共字段。

精简清单只列本批实际出现词形、可用译法、范围、理由、来源及存疑处；同时列旧译修改、局部例外和未决项。无需修改便说明沿用哪些条目；没有候选操作可交空 `operations`，不能凑新词。只读部分章稿时，标题写「本批」，不能报「全章术语齐备」。

## 合入与完成

整合者比较派工旧值、当前表与候选值，保留不相关更新。不同任务同时改同一字段时，挂起该条，不因候选较新便覆盖。合并后重读 JSON，核无重复、无遗漏、来源可解析，条目数与实际新增相符；数量相符还须核旧条目与未改字段未丢失。

术语修订影响已译段落时，交具体 ID 和需要复核的词句；另派正文修订，不自动全书替换。新增来源尚未登记、范围未定或证据不足时，交未决项，可用暂译和限度说明；不能捏造来源使其通过检查。表损坏或并发写入无法核清时，停止合入，保留增量，不用旧副本恢复覆盖他人更新。

回复只报新增／修订／沿用／冲突数量、两个交付路径及受影响段落。数字来自实际操作；清单存在不等于公共表已更新，公共表更新不等于正文已复核。
