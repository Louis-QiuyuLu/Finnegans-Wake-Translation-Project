# I.1 / Gemini 004.01–012.17 独立 AI 审校报告

## 输入

- role: ai_review
- executor: Codex 子代理 /root/review_project；独立于 Gemini 初译及其自检，无人工署名。
- 日期：2026-11-01；revision_round: 0。
- draft：reports/reviews/inputs/gemini-I-1-2026-11-01.json；SHA256：`cb66a5d482281284b8e422766cd4dd07fc0131f31d79456e27651363402ec2d1`。它是审校开始时 manuscript/chapters/I-1.json 的逐字节副本。
- 审校开始时 sources/catalog.json SHA256：`d160e67ad9837c577b4df984ec3e5fbe955cf518f28a2c167c7046c42f6d5836`；glossary/terms.json SHA256：`46e5486f2e52f7aabd7758c1aa202fe7d3df71c81ed3aa950910be03bb095f96`。本报告只覆盖当时所读来源记录，不自动覆盖后续整合稿。
- source_id: joyce-fp；Viking 1958 年校正版转录，沿通行页行；未核 1939 初版扫描件。
- 十一份工作包与交稿的 original 均和冻结章稿相同，交稿 translation 也相同；各项指纹见附录。交接相同不等于录文正确。
- 审校者只写本报告，未改章稿、工作包、来源、断点或音频。公共稿若已修订，须由整合处置记录另绑新指纹。

## 范围与查阅

已通读十一段新增 original、translation 与 107 条新注。旧 003 页三段及旧 41 注不在本轮复审范围。逐段核底本文字、主要动作、否定、主客、起止与坐标，并追查关键争议来源。Gemini 自检报告不作外证。

实际查阅：

- [Faded Page](https://www.fadedpage.com/books/20180126/html.php)：第 4–12 页待审范围及第 13 页接续位置；只查在线转录，未查纸本影像。
- [FinnegansWiki 第 4 页](https://www.finnegansweb.com/wiki/index.php/Page_4)、[第 5 页](https://www.finnegansweb.com/wiki/index.php/Page_5)、[第 6 页](https://www.finnegansweb.com/wiki/index.php/Page_6)、[第 7 页](https://www.finnegansweb.com/wiki/index.php/Page_7)、[第 8 页](https://www.finnegansweb.com/wiki/index.php/Page_8)：核原排折行；第二转录不充初版扫描件。
- 具体社区词目 Baronoath、Cropherb、Of the second、How hoth、See peegee ought he ought、Platterplate、Danu U'Dunnell's；只支持下列窄判断。
- Gutenberg 10803、22537 题录；22537 的 PREFACE、ON STRATEGY 局部；另核 4070 为 Ibsen 英译的题录，未读挪威语原本。
- [《古兰经》52:48–49](https://quran.com/at-tur/48-49)、[Jami` at-Tirmidhi 877](https://sunnah.com/tirmidhi:877)：核所列经文和圣训，不冒称通读经注。
- Moret 相关目录与社区具体转引。未成功打开 Moret 原书第 88 页或图版、Troy 原文；不能写成亲查这些原页。大学检索片段不充论文全文。

未逐条独立核完全部多语词源、地方史、纹章原典、歌曲原谱、手稿、中日译本及全书人物对应。107 条新注全部标 supported；阅读过它们不等于全部出处通过。格式 check 也不能补足外证。

## 问题

### R-01 — 博物馆段整句混录与漏译

- 词目／位置：fw-i1-008-06，original／draft／translation；约 008.21–008.28、009.01–02、010.07–11。
- 类别：底本／漏误译／无据增补。
- 问题与依据：Faded Page 白马句后直接接 three lipoleum；稿内多出 first in the ditch、gay first lipoleum boy 两句。008.28 的 Delian alps 又换成 Peppers 白马与 Creon 两句。009.01–02 的 Awful Grimmest Sunshat Cromwelly 及 Looted 换成 Tilsiter 酒瓶。010.07–11 拾起泥中半帽、印度人恼怒、把帽挂马尾三句全部缺失。中文已随错误底本增译、漏译动作。
- 建议：按声明见证重录整段，登记差异，再修中文与译注。若实际另用某版，须先登记真实版本及异文依据，不能仍称 joyce-fp 原样录文。
- disposition_required: fix
- blocks_integration: true。不能只润中文或降 note 等级。该 ID 当前无音频，不要求撤销不存在的文件。

### R-02 — 共行分段与起止坐标

- 词目／位置：新增段落的 range／locator。
- 类别：底本／坐标。
- 依据：Faded Page 对照上述原排转录。前九段实际起止为：
  - 004.01–004.17；004.18–005.04；005.05–005.08；005.09–005.12。
  - fw-i1-005-13：005.13–005.26，止于 Heed! Heed!。
  - fw-i1-005-27：实际从 **005.26** 中段 It may half been 起，至 006.12；005.27 已是 some say。
  - fw-i1-006-13：006.13–**006.30**，止于行中 same thing。
  - fw-i1-006-32：实际从 **006.30** 中段 Well, Him 起，至 007.15；006.32 已是 peep, see。
  - fw-i1-007-16：007.16–**008.04**；008.05 已开始 Penetrators。
  - 若恢复见证，博物馆段实际为 **008.05–010.23**。混录稿不能凭端点授予准确覆盖。
  - fw-i1-010-25 含 Phew!，故实际从 **010.24** 至 012.17；What a warm time 才起于 010.25。
- 建议：现 schema 禁止闭区间重叠，可合并 005.13 与 005.27 为 005.13–006.12；合并 006.13 与 006.32 为 006.13–007.15。保留旧 ID、工作包和修订历史，不伪移行号规避检查。
- disposition_required: fix
- blocks_integration: true。
- 断点：修好前九段后，应止于 **008.04**，下一锚句为 **008.05 / Penetrators are permitted into the museomound free.**。
- 音频：合并对象可按实有内容顺序拼接并更新关联；标签修改不证明覆盖新文字。

### R-03 — Brunto 误录及排印细项

- 词目／位置：fw-i1-007-16 original，007.22；另见 005-09、006-13、010-25。
- 类别：底本／声形。
- 问题：见证为 Bronto loved and Brunto has a lean on，稿内却两次写 Bronto，抹掉不同词形。
- 建议：第二处恢复 Brunto，核声形与对应音频。另恢复 005.11 的 ah 后逗号；006.18 的 shout-most 与见证 shoutmost 不同。010-25 的 toom-cracks、Bindme-rollingeyes、life-work、mourn-him 均与该见证合写不同；lordyheirs 对应见证 lordy heirs。不能无说明混用两个站点的排印习惯。
- disposition_required: fix
- blocks_integration: true（Brunto）；其他为可定点清理的录文差异。
- 音频：先不发布 fw-i1-007-16 错误词形的旧音频；逗号及排印差异另核实际发音，不机械重制。

### R-04 — 无据把 baronoath 定成拉斯法纳姆

- 词目／位置：fw-i1-006-32 translation；i1-shopalist。
- 类别：无据增补／出处。
- 问题：正文定为拉斯法纳姆，注释又称身体与四至地理“完全重合”。所列入口没有对应证据。[具体词目](https://www.finnegansweb.com/wiki/index.php/Baronoath) 列 Howth、Baron of Howth 及向东读路，没有该南郊地名。
- 建议：无进一步资料时正文暂音译；注写“社区联系霍斯及霍斯男爵，地理对应待核”，标 uncertain，删“完全重合”。社区线索不能直接升级成完成地理校勘。
- disposition_required: fix / qualify
- blocks_integration: true，至撤回正文无据定址；不需整段重译。仅改中文地名不影响原文音频。

### R-05 — Moret 注释归错发现者，未核原图却写成考定

- 词目／位置：i1-seepeegee；moret-egypt。
- 类别：出处／过度断言。
- 问题：注写 J. S. Atherton 考定，但没有其具体文献。[具体词目](https://www.finnegansweb.com/wiki/index.php/See_peegee_ought_he_ought) 转引 Mark L. Troy，将发现归 Mr. Slomczynski；未归 Atherton。Moret 原书图页和 Troy 原文本轮均未成功打开。
- 建议：保留 pg 88 声音读路；改为具名转引，说明未核原书页、图版与转引原文，标 uncertain。删除“考定”及未核木雕材质等细节。正文第八十八页可作为有明示限度的试译保留。
- disposition_required: qualify
- blocks_integration: true，至更正署名及查阅范围。

### R-06 — here here how hoth 不是 HCE 藏头

- 词目／位置：i1-fatherfornicationists。
- 类别：出处／声形。
- 问题：该词串的首字母不构成 HCE；开篇 Howth Castle and Environs 的真藏头不能担保此处也有。所引 fw-howth 是开篇词目。[How hoth](https://www.finnegansweb.com/wiki/index.php/How_hoth) 另列 how hath、How Howth、口吃式 H-H-Howth。
- 建议：删除假藏头断言；Howth 声影与父亲／巨人读法分别限定为有归属的解释。
- disposition_required: fix / qualify
- blocks_integration: true（可证伪断言）；主要中文动作可保。

### R-07 — of the second 回指银白，中文却添金色

- 词目／位置：fw-i1-005-05 translation；i1-scutschum。
- 类别：漏误译。
- 问题：前列色名为 vert、argent；按现注采用的纹章规则，[of the second](https://www.finnegansweb.com/wiki/index.php/Of_the_second) 回指第二色 argent，即银／白。“金阳第二色相”与之冲突。
- 建议：去金，或改与银白相容的表达；太阳声义不自动等于金色。
- disposition_required: fix
- blocks_integration: true（可定点修正）；不须重译全段，其他纹章词源不由此一并通过。

### R-08 — provost 主体漏掉，游民取而代之

- 词目／位置：fw-i1-005-13 translation；i1-nabir。
- 类别：漏误译／人物关系。
- 问题：like that provost scoffing bedoueen… 的 provost 在中文消失，变成“贝都因游民”。bedoueen 的声影不能取代原句主体与 between 关系。
- 建议：保留长官／教务长及嘲弄动作；贝都因声影留注。具体是谁另待资料，不补实名。
- disposition_required: fix
- blocks_integration: true。

### R-09 — 经文、圣训、项目拆词混挂首页

- 词目／位置：quran-arafat；i1-cubehouse、i1-whitestone、i1-sustainer、i1-nabir、i1-ansars。
- 类别：出处／分级。
- 问题：Quran.com 首页不能定位并支持克尔白、告别演说、玄石、洁齿木、瓦哈比与全部多语链。玄石降世与变黑故事属圣训，不能冒称《古兰经》经句。
- 已核窄依据：52:48–49 支持起立、夜间及星退时颂赞；Tirmidhi 877 支持玄石来自天园、原白而因罪变黑，其英译喻白如乳。它们不独自证明 Joyce 的实际取材路径。
- 建议：拆成实际查到的具体经句与圣训来源，只支持对应事实；Al-Qayyum、miswak、语词链与人物指认未核项删断言或改 proposal／uncertain。不能整串都写 supported。
- disposition_required: fix / qualify
- blocks_integration: true（当前过宽出处声明）；限缩后可保试译，不须无限查书。

### R-10 — Dunne 来源 URL 指向另一作者作品

- 词目／位置：dooley-hennessy；i1-mrdooley。
- 类别：出处。
- 问题：[10803](https://www.gutenberg.org/ebooks/10803) 实为 Robert Kerr 航海旅行史第二卷，和所标 Dunne 作品不符。
- 可用替代：[22537 题录](https://www.gutenberg.org/ebooks/22537)、[正文](https://www.gutenberg.org/cache/epub/22537/pg22537-images.html)。PREFACE 末部可核两人关系；ON STRATEGY 开头为 Dooley 回答 Hennessy 提问。本轮只读这些局部。扉页为 1899 年，另列首版 1898 年及印次；须区分首刊与所据见证。
- 建议：更正链接、见证与实际查阅范围。人物存在可获支持；不能只换对 URL 就断言 Joyce 此处全部借用关系已证。
- disposition_required: fix
- blocks_integration: true。这是确认错引，不是暂时打不开。

### R-11 — 可降级收口的具体注释

- 类别：出处／过度断言。
- disposition_required: qualify
- blocks_integration: false，前提是删无据确定语气并明示局限；若仍确定断言则须继续修订。

- i1-brekkek：Frogs／κοάξ 只支持蛙声部分，不能一并担保 Ualu 与 Quaouauh 全部释义。保拟音差别，后两声串解释待核，自己的声读标 proposal。
- i1-stutteringhand：施工、写作、造物迟疑属解释；共济会特定手势无具体外证。可保项目兼读，手势说标未核。
- i1-buildung：正文某某河较保守；黄河、Saône 链本轮未核，须 uncertain，不能整注 supported。
- i1-cropherb：当前定成约伯记巨兽；[具体词目](https://www.finnegansweb.com/wiki/index.php/Cropherb) 还列牧食、草、驼、驴、驼背等竞争读路。可保嚼草者形象，巨兽指认降为项目提议。
- i1-shize、i1-teetootal：Molly Brannigan、Phil the Fluther's Ball 须各有实际歌词来源，不能仅挂另一首 Finnegan’s Wake。未核原歌时保可能回声，标 uncertain。
- i1-mastabatoom、i1-priamolim：若称某短句是民谣原词，须核实际版本；未核则改项目声形比较，不保直接引文标签。
- i1-graceglutton：可保常见饭前谢恩句对读；英国圣公会公祷书这一归属缺具体页，不能冒充已核正式版本。
- i1-finnagain、i1-phoenish：保局部回返读路，删“标题之谜彻底点破”等全书总论；本轮没有核全书。
- bylina-buslaev：URL 是 Wikipedia 条目，不是所标 Novgorod 史诗原文；改题名与来源性质，不用 primary 包装百科。
- ibsen-solness：4070 真实相关，但为 Archer／Gosse 英译；来源用途须限题录及英译，不称查过挪威语全文。

### R-12 — 末段尚未放行

- 词目／位置：fw-i1-010-25；i1-piltdowns、i1-lumproar、i1-humptyshell 等。
- 类别：底本／出处／无据增补。
- 问题：全段对照未见 R-01 那种整句替换、插入及大段动作缺失；仍有 R-02、R-03 的坐标和词形项。正文把 Herrschuft Whatarwelter 固定为威灵顿公爵、frumpty 固定为七十次，现有来源未给这些断言的核定位置。七赤盾家徽及化石造假讽拟亦不可只靠近音或后世知识当作者意图。
- 建议：暂留待修稿；先恢复见证，再限缩身份、数字与历史断言。不越过 008.05 缺口推进断点。
- disposition_required: fix / qualify
- blocks_integration: true（本段未修），不授予全段通过。

## 各段放行范围

- fw-i1-004-01：needs_revision。基础动作与底本未见其他阻断；R-06 及相关 R-11 须修。
- fw-i1-004-18：partial_review。主要译义、底本未见整句缺漏；R-11 的手势、河名等须限缩，其他语言链未全部实核。
- fw-i1-005-05：needs_revision。修 R-07；不要求整段重译。
- fw-i1-005-09：partial_review。主要译义未见阻断；恢复逗号、限缩全书总论，可保试译；礼仪、歌谣并未逐项外核。
- fw-i1-005-13：needs_revision。R-02、R-08、R-09。
- fw-i1-005-27：needs_revision。R-02；其余主要动作未见新阻断，按 R-11 限缩引歌。
- fw-i1-006-13：needs_revision。R-02、R-03；按 R-11 限缩歌谣原词和总论。
- fw-i1-006-32：needs_revision。R-02、R-04、R-05。底本另有图符；本轮只见附图入口，未核形态，纯文字稿不得据本报告称已完整保留版面符号，须留来源说明或另行处理。
- fw-i1-007-16：needs_revision。修 Brunto、终点 008.04；旧音频先不发布。其他身份与地理只按有明示存疑的试译处理。
- fw-i1-008-06：needs_revision，阻断合入；先修 R-01。
- fw-i1-010-25：needs_revision，阻断合入；R-12 及连续缺口未解。

## 结论

- 当前版本：**needs_revision**。
- 最早的大规模底本不可信起点：**008.05 / Penetrators…**。此前可定点修正，不要求全批重译。
- 修好前九段后，连续止点为 **008.04**；未修前不自动放行错误坐标与 Brunto 误录。
- 除 provost、baronoath、金／银项，008.05 之前未见另一处须整段重译的主要动作／否定漏译。未核词源和宏观解释可明示存疑，不把 AI 试译冒称学术定稿。
- 音频依整合者清点，止于007-16所在段；008-06、010-25无音频。合并可顺序拼接，Brunto须另处理；中文修改是否影响音频，须按音频实读字段判断。
- 整合者逐项记采用、补证、降级或延期，另绑新稿 SHA256。不得把此报告冻结指纹换成新稿后沿用全部通过。风格偏好不启动新一轮全段翻译。

## 附录：冻结工作包与交稿指纹

### fw-i1-004-01

- workpack: reports/workpacks/fw-i1-004-01.json；sha256: `c446c148447454d4ca7f45c84e704e2d9c611d8311a57551b7927de787926e9f`。
- draft: reports/drafts/fw-i1-004-01.json；sha256: `cf2efbda4fe26fcb6671cc58025d12d3918795ff50be3a8e936e681714a7f8d9`。
- original_sha256: `b42f8443789a4b58c65a1c6445c8b80d48c3cfc3a7691753f41fded0b8d9f85e`。

### fw-i1-004-18

- workpack: reports/workpacks/fw-i1-004-18.json；sha256: `7300513b0c7ae4bee0d3cf38b88362615e2b111d4ce6f9b507885ada6673ede1`。
- draft: reports/drafts/fw-i1-004-18.json；sha256: `f794339013d9395d3ac37938aa0316fad80647bfe5153e516630ea440b5c2799`。
- original_sha256: `bb09224e3a9830a229ff4a461dfc38be5d1e6b1541f995f5918b94bb5e1d8103`。

### fw-i1-005-05

- workpack: reports/workpacks/fw-i1-005-05.json；sha256: `049ee7423d1eaa5f437a5b4c8f40d2b895680341d19042b1ef11e3beaef83f09`。
- draft: reports/drafts/fw-i1-005-05.json；sha256: `10f561f6e3ff3b53812a7d79c6ad23355a72aa7458de5742bf2f4382e0174b71`。
- original_sha256: `60a21d444f247e892baff7cc6a4a9cbbf8246b6107c0b92d66cadf7e2aabadfd`。

### fw-i1-005-09

- workpack: reports/workpacks/fw-i1-005-09.json；sha256: `b5bd555fa57c3c5c1bebabde0498c041dc092e640bc77e890f2394068cd36322`。
- draft: reports/drafts/fw-i1-005-09.json；sha256: `28e0346ea6eabc0b252c9522985e5d5aa4cb256bf6170ed8f4887ba6c1d24530`。
- original_sha256: `d889cea751e09ef9daaa80752c84153360fd605f2862469a62c128d89347b51d`。

### fw-i1-005-13

- workpack: reports/workpacks/fw-i1-005-13.json；sha256: `7d737d72aeec7e677587f58846c69bb0baa30563ed90f85d4a5320a7d5c7597a`。
- draft: reports/drafts/fw-i1-005-13.json；sha256: `132db4f98f511dfaca21dbd24d8cc5997b00b873ff948cee7aaea70504698c4c`。
- original_sha256: `3875431c91b67c0f911bcb4052d2028dbfc249a1324f491078184c81de7786df`。

### fw-i1-005-27

- workpack: reports/workpacks/fw-i1-005-27.json；sha256: `16fcd89d1a84cfde0f75f819a68d41676d936aa7c50772c2f869375d25edbd84`。
- draft: reports/drafts/fw-i1-005-27.json；sha256: `d7802f2bdded5d2d0e7d6ec5bd3ffe712f99622ee87b88d4b4a6d4c4a7f25d53`。
- original_sha256: `f96d70d431c2f93c86fa2f147b6fab021e19ec2c57380bddd571d4d3a48ab574`。

### fw-i1-006-13

- workpack: reports/workpacks/fw-i1-006-13.json；sha256: `7c41830bd268667d76b8aba71c5670c8423b1c34eab7fb512ce27d8ebe209bbd`。
- draft: reports/drafts/fw-i1-006-13.json；sha256: `f7890a8b653f7dc9f4a073b72ea83f0474e6b61f809b8a4fc54d5aeae2b641e9`。
- original_sha256: `0e698fa1eddaba42e4dc1195287fbb5f6cb1cbb137be157d5ea6860d1e589490`。

### fw-i1-006-32

- workpack: reports/workpacks/fw-i1-006-32.json；sha256: `58b93d24edeaae52d11169710be11bde493e4c0ea544ede45eb67ae5d8f730b0`。
- draft: reports/drafts/fw-i1-006-32.json；sha256: `7ddae3c78d8ec0348beb1e0c4a9211649df666f715efa76bc300a64c5c96832a`。
- original_sha256: `658c0bb5ebabbc5aedf1fd154ab36e82a2635ce3b1538aabf68361503ecaf733`。

### fw-i1-007-16

- workpack: reports/workpacks/fw-i1-007-16.json；sha256: `b9b3204d056505a015de55a53d655a8f14614bd276d768e03f099e534c5d274f`。
- draft: reports/drafts/fw-i1-007-16.json；sha256: `59b2abbbe52209bb6be1ea29e11b792f4461fdeb5c11dea6229db0023d028dbc`。
- original_sha256: `da715f6f5360ecc8b68d11ac9eb1183fedacdd5f6e7d6bc86c790cc03b8f4ae9`。

### fw-i1-008-06

- workpack: reports/workpacks/fw-i1-008-06.json；sha256: `04d92022cf0f6e4136fec3c21bc8c3ca1dec098e53fe70372b5961fb4826153a`。
- draft: reports/drafts/fw-i1-008-06.json；sha256: `ea73dcff4fd3024c1fa65e5b9019750b255fcb33a83d3e4e8913af943bff22d6`。
- original_sha256: `009a5f1341035ca549938e500e4301354fe617f9bcd1f7557e52592ddfc9aefa`。

### fw-i1-010-25

- workpack: reports/workpacks/fw-i1-010-25.json；sha256: `1a6f603488487a7d9a40d9230599c7843a3c1ac32d1927cac7954459d203f790`。
- draft: reports/drafts/fw-i1-010-25.json；sha256: `5d548811e8fcc50490bd2ea7251046ba4f904b8a94d5d10aef02ab2c6c55da80`。
- original_sha256: `31195db5f9a48d64f59d646f691e03a531e7cc1f14ec2a7c4f0944e2bc7727dc`。

