# I.1 全章交稿审校 r0

## 输入

- role: ai_review
- executor: Codex；与 Gemini 初译分开执行，非人工审校。
- draft: reports/reviews/inputs/gemini-I-1-complete-2026-11-01/manuscript__chapters__I-1.json
- draft_sha256: 00cbae2ea64a05ff4c2caaa535a455c5d30c7b94895bc018c9d3a94e8110fc94
- source_catalog_sha256: 72c06e3c6567c125d6afad8d72840d978d466c22b1772d5d7ee9276cc23f2fdd
- revision_round: 0
- baseline: 线上 0d1ad8f；本轮沿用此前已核的003.01–008.04稿，不用旧副本覆盖。

## 范围与查阅

逐页取得 FinnegansWiki 003–030 转录，另读 Faded Page 工具缓存第一章全文及030.01起句。两者分别记录；不冒称纸本逐页校勘。工具缓存中对话表格、页分界和图形有格式损失，须另核，不按网页行号强分原书行。

通读新交稿008–029译文、注释；前段沿用既有r1和006.32考据修订。现有Gemini报告只有概括性赞语、来源ID存在检查，不能代替原文、具体文献和逐项问题核查。

## 问题

### R-01：旧副本倒退

候选重新拆开005、006自然段、退回错误页行，并覆盖006.32已核图版考据。保留当前公共稿至008.04，只整合新尾稿；保留旧ID迁移记录。blocks_integration: true；disposition_required: fix。

### R-02：008页增句、替换与漏句

沿用前次审校所列问题：仍多出 first in the ditch 等两句；Delian alps 改成另一串不存在于见证的文字；Awful Grimmest Sunshat Cromwelly. Looted. 换成 Tilsiter 酒瓶；010页拾帽、挥帽三句共约58词未译。以实际Faded Page局部及Wiki重核并回写原文、译文；不只换英文。blocks_integration: true；disposition_required: fix。

### R-03：016–018对话词形与漏词

indelible／grout／wrongs shortener／sure／what 等与所列见证不符；后段漏 olde、wone，Countlessness of、flick as flowflakes 等遭替换；还有HTML实体残留。须依所选文字见证逐句修订，并重核中文；恢复原对话排式。blocks_integration: true；disposition_required: fix。

### R-04：其他词形与坐标

逐段对照发现 Dyfflinarsky、michindaddy、abramanation、'Tisraely 等差异；部分属行末断字，部分实改了词。区分后保存改录依据。008起点实际是008.05。21／22、25／26两处截在句中；合并完整段落再配坐标。blocks_integration: true；disposition_required: fix。

### R-05：注释超出已读材料

104条新注多把拟读写成定论。例：1132鲸鱼救荒具体年份与地点未核；“精确铺排十二因缘”与正文实际次序不符；Nizam直接当Nisan；芬尼根时代“彻底合拢”；把目录链接伪题为Sidney1576回忆录；把耳语、商号、家族与政治讽刺逐一定名。逐注缩到可见词形与本项目试读，缺专门研究则proposal／uncertain，删除无据史实与伪引文。不得用“来源已登记”放行。blocks_integration: true；disposition_required: fix。

### R-06：覆盖声明与断点

003–029共27页，非“全部29页”。现稿不能声称Viking1939／Faded／Wiki纸页逐行全核。全章须交逐段覆盖账，说明对话转录、断字及图形近似；核030.01实际锚句后再切到I.2。coverage与人工reviewed分开。blocks_integration: true；disposition_required: fix。

## 结论

needs_revision。保留本轮完整输入，按上述问题合并修订，再作r1复核。不得把本报告或Gemini旧报告写成人工审校，也不凭完整字段直接发布。
