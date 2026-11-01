# I.4／I.5 定点修订复核

## 输入

- role: `ai_review`；executor: Codex 子代理 `audit_i4_i5_latest`。本轮只核实际差异及相邻上下文；不重开全章审校，不改公共稿。
- 初审报告：`/private/tmp/fw-book-I-intake-20261102/review-I4-I5.md`；SHA256 `a495e9f141393460db6b500f91ab56c711a71decef50fa2788502e07ae790ab2`。初审已读20段原译和115条注释；未改部分沿用该报告的实际核阅范围及限度。
- 处置账：`/private/tmp/fw-full-source-20261101/reports/revisions/book-I-codex-integration-20261102.json`；本轮读取时 SHA256 `23d73432fd2459bc6dcf5d48e23d27f3a36d017a7a2d6ac07415f99877d365b9`。以实际JSON差异核落实，不凭处置账中的“已解决”放行。
- 修订轮次：这是上述初审意见后的定点修订复核；不据文件名推断整批此前统一轮次。
- 当前 `I-4`：`/private/tmp/fw-full-source-20261101/manuscript/chapters/I-4.json`；SHA256 `8eb90aaa7a069ccb660ffd194c9fe66b14829698c433586d2dea1089ff4c37bb`。
- 对照冻结 `I-4`：`/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-4.json`；SHA256 `203fba375d3cee585ed72398c32e51f316df9a5f77022b5bd39ffb333fea2940`。
- 当前 `I-5`：`/private/tmp/fw-full-source-20261101/manuscript/chapters/I-5.json`；SHA256 `89f8f0b9d6c110f69479ee03094cdfcf77d0a931034b2e4dfc3b8842145385f5`。
- 对照冻结 `I-5`：`/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-5.json`；SHA256 `a25499f274e3991ca822f4066202a43115a7bafee86717bf19eb582f37203e92`。

## 实际核对范围

逐项对比两版JSON，确认所有段落的 `id`、`original`、`draft`、`locator`、`range`、`source_id` 均未改。I.4实际改动限四处译文、五条注释；I.5限章末一段两处译文及一条注释。另有章级 `source_text` 与 `coverage_review` 变化；新增 `source_text.html_sha256` 与初审所读完整见证相符，覆盖说明也已改为有明确限度的AI核对记录。

实际联读：I.4 `fw-i4-075-01` 爆破数量上下文、`fw-i4-088-35` 吸烟问答前后、`fw-i4-090-34` 轰回住所至群女谴责的完整收束句、`fw-i4-093-22` 问候与祈使句；四条事实错注及其原文所在句。另读新增 `i4-shun-the-punman-drinkbattle` 说明。I.5联读 `fw-i5-123-30` 制信至狐狸／鹅句群、对应四老注，以及末句完整括号和谢姆出场。

未核：外部学术来源、词源与中日译本；原版图形和生成读本的视觉呈现；首审已明列、且本轮未改的合理歧义。本轮不将这些未核范围写作“均已证实”。完整图版由整合者另行验收，本代理没有看图。

## 逐项处置复核

### I4-R01b：已解决

`eleven and thirty wingrests (circiter)`现译“约四十一翼展”，恢复相加数值。相邻爆破动作未改。`fix`已落实，当前无阻断。

### I4-R07b：已解决

原文问 `whether she minded ...`，答 `Not if he barkst into phlegms`；现译“介不介意他当场吸烟？不介意，倘若他咳得痰沫迸发。”`Not`已回到“不介意”，不再成为“只要他不咳……”的反向限制；无据“血”字也已撤。措辞仍可收紧，火焰声形也未尽取，但这属于已允许的择译，不再以此阻断。

### I4-R08b：已解决

现译在鬼屋后补入“他在那鬼屋里拉了出来（zoo）”，对应 `where ... he shat in (zoo)`；又补“鹿肉以扫，怯得像鸽子，又像博托姆那儿的鹿”，对应 `venuson Esau ... dovetimid ... dears at Bottome`。后接“泥泞的金妖怪（dun）”仍依 `muddy goalbind ... (dun)`造词取声形，不凭这个不寻常比喻判成新增物种或新增事件。

新注明确区分排泄字面与 `he sat in` 听觉候选，说明正文暂取一路，zoo／dun其余关系待考。该取舍没有伪称双关已经全部查实。初审指出的主要动作与比喻均有对应；相邻群女斥责未丢。当前无阻断，不要求另因词语偏好重译。

### I4-R09b：已解决

`Get into my way!`现译“到我这条路上来！”，已撤“休要”，恢复进入方向。问候与后续话语保留。当前无阻断。

### I4-N01：四项均已解决

- 酒馆注撤去本段没有的 Old Sot's Hole，补 Conway's Inn at Blackrock；四站顺序现与小说原句相符，并注明不据此确认营业史。
- 猪与风信子注改为“控方声称”赴集市携带，不再称牵猪持花出庭；人名拆拼仍明示项目推测。
- 战场词形改为 `Yetstoslay`，与本段原文一致。
- 池水注撤去“四尺半”，改为“很可能有几尺深”，并录 `very possibly several feel of demifrish water`。未再增加确定水深。

这些是对原文关系的定点更正，无须据此重开外部史实考据。当前无阻断。

### I5-R08b：已解决

现译“这便是峡湾卡姆赫尔松当年在女人国同索尔德鲁部众一道时的制信伟业”，不再并列“格赖姆斯”，也无“失落神学”限定；对应原句唯一专名 `Fjorgn Camhelsson`。四老注同步删去额外人名。前后署敬、附言、未饮之杯与狐狸／鹅句群保留。当前无阻断。

### I5-R08c：已解决

末句已撤“（等我告诉你！）”，原括号 `Sez you!`所对应的“亏你说得出口！”仍存，随后直接引出“执笔人谢姆”。未新增发言，章末出场节拍不再受该增补干扰。当前无阻断。

## 结论

- 当前版本：`ready`，仅指本轮列明的修订处、受影响注释与相邻上下文。
- 初审所列实质问题均已解决；实际差异未引入新的实质缺陷。本轮无未决阻断项。
- 可将本报告与绑定旧稿的初审报告合读，作为当前两章AI文本审校记录；不得单凭这份局部复核宣称已重审全章全部外部词源或图版。
- 两章保持 `revised`，没有新增人工审校署名。本代理只写本报告，未改公共稿、来源、断点或产物。
