# I.1 全章交稿整合复核 r1

## 输入与范围

- role: ai_review / 修订后定点复核；执行者Codex，非人工审校。
- 原交稿：reports/reviews/inputs/gemini-I-1-complete-2026-11-01/manuscript__chapters__I-1.json；SHA256见r0，未覆盖原文件。
- 当前稿：manuscript/chapters/I-1.json；SHA256 `993815845fe516ce6de4baf4c1ee2b10fce85fe752a90cb91e165982b713e609`。
- revision_round: 1；问题承接 [r0](gemini-I-1-complete-integration.r0.md)，也承接此前008页隔离稿问题，不冒充新报告已自动解决旧缺陷。

## 实际核查

通读第一章新增尾稿与104条注释，按Faded Page所标Viking1958年第八印本的工具缓存转录核003.01–029.36完整文字；下载FinnegansWiki003–030正文辅助核页行与下一锚句。未核1939纸本。缓存、HTML、图片只在仓库外暂存；[覆盖账](gemini-I-1-complete-coverage.json) 保存来源、指纹、短锚句、差异与范围。

全章26段，27页、960个通行页行坐标，范围连续且无重叠。将三处旋转字母计入后，9773个空白分词与缓存全文对照相等，仅保留三个明确申报的行末连字符选择：开篇雷词、great-grandhotelled、niece-of-his-in-law。该数字只用于核本次覆盖，不是权威全章词数。未删除其他标点、重音或增添英文句子。

## 问题处置

- **R-01 已修。** 保留线上003.01–008.04修订及006.32图版考据；只接新尾稿。英文朗读仍用既有登记轨道，原朗读文字未变。
- **R-02 已修。** 删008页两句多文及相应译句，恢复Delian alps和Cromwelly／Looted语串；补010页拾帽、欲投炸弹、挂帽到马尾的三句及中文。不把新英文覆盖进去后仍沿用漏译中文。
- **R-03 已修。** 依所选见证纠正intellible、growlsy、wrongstoryshortener、sutton、patwhat、umscene及后段多处替换、漏词和实体残留。重译穆特／朱特对话，保留原文怪词与未定读法，不按旧稿“人物真的化为泥土”等释义倒写原作。
- **R-04 已修。** 008起点改008.05；Phew归010.24。对话合为016.10–018.16；恶作剧女王长句合为021.05–023.15；劝卧长段合为024.15–027.21。稳定ID尽量保留，归并表见 [处置记录](../revisions/gemini-I-1-complete-disposition.r1.json)。
- **R-05 已限缩。** 104条新注逐项重写，分别用proposal／uncertain。删鲸鱼救荒等未核具体史实、未查原语整句、假书目署名、全书唯一主旨等断言。保留原作可见声形与明确标注的候选联系，不借一般百科条目证明Joyce意图。当前采用只引实际读到的作品与页转录，未导入Sidney伪题录等新条目。原稿保存在输入快照。
- **R-06 已修。** coverage标complete只指全章初译录入及覆盖核对，绝非人工终审。三处旋转字母已逐图查看，另存source_figures并在网页、EPUB内嵌SVG重绘，便读稿说明方向；不是原刊字形影印。已在030.01实际核下一锚句，并转断点到I.2。

正文另改猜数、Nizam音译和缘起长链等：不把month／windies译成确定31扇窗，不把quaintlymine定为门牌29，不静默把Nizam改Nisan；保留原文death在birth之前的次序。所有实改与旧译均存处置记录，初译draft保留。

## 验证

- `python3 scripts/project.py check`：通过；17章，1章录全，全库27段、230注，人工reviewed仍0。
- `python3 -m unittest discover -s tests -v`：31项通过。
- `node --test tests/*.cjs`：15项通过。
- `python3 scripts/project.py build`、`check-artifacts`：通过。
- 三处图形网页显示、角色名称与方向已实际查看。EPUB声明含SVG资源，遵循 [EPUB 3.3 的svg属性要求](https://www.w3.org/TR/epub-33/#sec-item-property-svg)。

## 结论

**ready，限初译发布及本轮首轮校订。** 003.01–029.36可整体上线；不标reviewed，不填人工姓名。

仍待人工通读、逐项词源与历史考据，以及中日译本原页比较。proposal／uncertain并不证明其猜测成立；今后取得原页再定点修订。旧输入、旧隔离稿、先前审校和本轮覆盖账均保留，不把r1当最终学术定稿。
