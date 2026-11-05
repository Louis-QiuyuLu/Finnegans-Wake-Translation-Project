# II.4 冻结稿审校报告

## 输入

- role: ai_review。
- executor: OpenAI Codex 父任务；AI审校，不是人工终审。
- revision_round: 0；本轮初次审查该冻结交稿。
- draft: `reports/reviews/inputs/gemini-book-II-2026-11-03/manuscript/chapters/II-4.json`；sha256: `84a484bcc01b3658663bad69dc0036dbf4c5cafd6284bad5fa89f9e48625e16b`。
- sources: 冻结 `sources/catalog.json`；sha256: `707e0358bd04a1b30f4fe6f213eb6f49f9e993cd0e242b3c5c809cb0c432881d`。
- glossary: 冻结 `glossary/terms.json`；sha256: `46e5486f2e52f7aabd7758c1aa202fe7d3df71c81ed3aa950910be03bb095f96`。
- source_id: joyce-fp；Faded Page 的Viking 1958年第八印本转录。
- 未另配标准段落工作包，以冻结章稿、manifest及段落原文指纹绑定。

## 范围与限度

已分四批完整读取4段original与translation，并读完24条notes；不把字数比当作漏译证明。以下每项均列原词与现译。对初译draft字段仅核与translation相同或不同，不另声称读过两个独立翻译。逐字外部版本校勘与中文语义判断分开。
本章source_text与历史外部HTML重新抽取结果完全一致；8处段落original差异均见source-comparison.json，属于断字连写。未发现本章英文成片缺录。
实际重新打开Faded Page全文转录并定位383、388页的相关句；另开FinnegansWiki p383作文字交叉检查。没有查看1939/1958纸本扫描，因此只列印刷页与冻结稿坐标，不虚填精确行号。
24注已核原词锚、主张边界及内部关联；全部只引joyce-fp。未逐条重开传说、钱币、Boucicault剧目、Gordon军史、Senchus Mor法史、Cross of Cong馆藏等原页，不能写作24注外部事实均已核准。仅标proposal不足以为确定年份、语源及材质担保；具名事实须另补来源。这不表示24注全错。

## 问题

### R-II4-01 / P1

- 段落／位置：`fw-ii4-383-01`；p383 开篇鸟歌；章稿声明范围 `383.01–386.36`。
- 类别：无据增写／动作丢失。
- 原文锚：`To see that old buzzard whooping about for uns shirt in the dark / And he hunting round for uns speckled trousers around by Palmerstown Park?`。
- 当前中文：「盼着狂风略作哀号；在杂乱的糠皮交易里贴地跛行；挑拣蜗牛细看哪头充当前马……蹑手蹑脚寻觅手推轮车……把衬衫晾在绳上」。
- 问题与依据：原文写老秃鹫在暗中呼寻衬衫、在Palmerstown Park周遭寻斑点裤。现译扩成糠皮交易、挑蜗牛、前马、箱笼、手推轮车与晾衫等连续动作，底本没有这些对应词句。同时make his money and mark改成面包与黄油，并另添高处干爽、苍穹等情境。不是保留双关所需的解释性注释，而是替换作者歌辞。
- 建议：撤掉无据动作；按原歌各行还原找衬衫、找斑点裤及money/mark的言语关系，双关补入注释。E-FW383已重开外部原著转录核词。
- disposition_required: fix。
- blocks_integration: true；影响正文事实、覆盖或句法，不是同义措辞偏好。

### R-II4-02 / P1

- 段落／位置：`fw-ii4-391-01`；p391 约翰尼段；章稿声明范围 `391.01–394.36`。
- 类别：漏译／替写剧情。
- 原文锚：`on account of her full bottom ... because he was so slow to borstel her schoon for her ... instead of backscratching her materfamilias proper ... all divorced and innasense interdict`。
- 当前中文：「因其旧日过犯而吓得魂飞魄散……在后甲板上窥见其亲密温存，在克利夫登之日，与全美之女子……在其膝头摩挲其身躯……如神明般巡游都柏林全城」。
- 问题与依据：臀部、刷鞋、侍奉女主人而未照料其母、离异与禁令等原有句链不见；现译插入后甲板、克利夫登、全美之女子、巡城等经历。不能以整章确有窥视主题为这些局部动作背书。
- 建议：按本句逐分句恢复，保留母亲/女主人的区别与离异/禁令，并撤掉没有原词对应的经历。
- disposition_required: fix。
- blocks_integration: true；影响正文事实、覆盖或句法，不是同义措辞偏好。

### R-II4-03 / P1

- 段落／位置：`fw-ii4-391-01`；p393 And still and all 之后；章稿声明范围 `391.01–394.36`。
- 类别：无据长篇增写。
- 原文锚：`at that time of the dynast days of old konning Soteric Sulkinbored and Bargomuster Bart, when they struck coil and shock haunts, in old Hungerford-on-Mudway`。
- 当前中文：「在全爱尔兰大瘟疫降临之前，在克隆塔夫恶战之后……手持粗粝木棍……特里斯坦双臂紧拥伊索尔德，将少女金发揽入怀中，热泪滚落，双唇颤动」。
- 问题与依据：此处原文接Soteric/Bargomuster、Hungerford、鱼类/羹汤与名声/帝国等连缀。现译加入瘟疫前后、四人青年涉水、具体拥吻、揽金发、热泪颤唇，后又添深吻永恒之印记。邻近主题相容不能替代局部文字依据。
- 建议：删去以上自行补写情节，逐句保留原有人名、地点、动作与反复；若某双关无法定读，正文取保守读法并明示损失。
- disposition_required: fix。
- blocks_integration: true；影响正文事实、覆盖或句法，不是同义措辞偏好。

### R-II4-04 / P1

- 段落／位置：`fw-ii4-391-01`；p394 末部，与下一段395开头联核；章稿声明范围 `391.01–394.36`。
- 类别：成片漏译／跨段句法断裂。
- 原文锚：`after having prealably dephlegmatised ... Aithne Meithne ... Engrvakon saga ... the allimmanence of that which Itself is Itself Alone ... intuitions of reunited`。
- 当前中文：「在遗忘前急于兜售，四位老人宛若大海之触手……那失落之恋情，那夜色中消逝之舟楫，直至万籁俱寂，星斗沉沦。」。
- 问题与依据：原文接清痰、耳/口语句、故事与名字链，继而进入高维、自我、物质与意识的连续句法。中文在兜售后改为抒情收束，原句群大量消失；下一段却突然从自我之域起译，丢掉reunited selfdom跨段连接。原文此处没有万籁俱寂、星斗沉沦的终止。
- 建议：补回兜售之后至reunited的全部句群，连读下一段selfdom；不要为一个人为四页分段另造故事结尾。
- disposition_required: fix。
- blocks_integration: true；影响正文事实、覆盖或句法，不是同义措辞偏好。

### R-II4-05 / P1

- 段落／位置：`fw-ii4-387-01`；p389 学院清单与后接括号；章稿声明范围 `387.01–390.36`。
- 类别：漏译／数字与限定丢失。
- 原文锚：`of Killorcure and Killthemall and Killeachother and Killkelly-on-the-Flure; this unitarian lady ... lived to a great age at or in or about the late No. 1132 or No. 1169, bis ... where she was seen by many and widely liked`。
- 当前中文：「爱尔兰最宏伟之四大学府，在罗洛翻滚之圆卷前施展统治……（这位贵妇，惊世绝色，高寿于菲茨玛丽环路）」。
- 问题与依据：四个Kill-地名/双关名称全无中文对应。后接贵妇括语将1132/1169、bis以及众人见过并喜爱等限定删掉，只剩主题提要。这里不裁四名称唯一词源，但不能整组抹去。
- 建议：依次补清单并保留数字、bis与限定；难解名称可音译加注，不得用“四大学府”概括替代。
- disposition_required: fix。
- blocks_integration: true；影响正文事实、覆盖或句法，不是同义措辞偏好。

### R-II4-06 / P2

- 段落／位置：`fw-ii4-387-01`；p388 弗兰芒舰队；章稿声明范围 `387.01–390.36`。
- 类别：时刻误作纪年。
- 原文锚：`on a lovely morning ... at about aleven thirty-two was it?`。
- 当前中文：「在洪水后明媚清晨尽数官方溺毙，时约一一三二年？」。
- 问题与依据：前文morning与at about使十一点三十二分的时刻层清楚可读；后面另有year及1132。现译只写年，吞掉时刻与纪年的相互叠映。E-FW388已重新定位该句。
- 建议：至少保留“约莫十一点三十二——是吧？”的时刻层；若保留1132纪年联想，另在注释说明，不用纪年取代时间。
- disposition_required: fix。
- blocks_integration: true；影响正文事实、覆盖或句法，不是同义措辞偏好。

### R-II4-07 / P2

- 段落／位置：`fw-ii4-387-01`；p389 高度量度；章稿声明范围 `387.01–390.36`。
- 类别：漏译／量纲缩减。
- 原文锚：`from his elevation of one yard one handard and thartytwo lines, before the four of us, in his Roman Catholic arms`。
- 当前中文：「立于一百三十二行高度之上，在吾等四人面前，将其揽入双臂」。
- 问题与依据：one yard被删；one handard/hand之声形层也消失。Roman Catholic arms的宗派词面无对应。是否带度量/典故混用可以存疑，不能在没有说明时把整串量度压成132行。
- 建议：恢复一 yard及其后数字/hand等可读层；arms保留双关余地，并记录宗派形容词的保留或损失。
- disposition_required: fix。
- blocks_integration: true；影响正文事实、覆盖或句法，不是同义措辞偏好。

## 分段核对记录

- 383段：已对鸟歌、四老饭前祷告、舞台/学校回忆及贵族拍卖清单；开篇鸟歌有R-II4-01，无据增写尚未撤，不能整体放行。
- 387段：已对服饰清单、神话/历史混写、反写人名、学院与贵妇括语、离婚作别；R-II4-05至07需补正。
- 391段：已对约翰尼/马库斯/马特句链、病榻与食物清单、Shandon钟声及末尾自我论述；R-II4-02至04为主要阻断。
- 395段：已完整对完selfdom接缝、亲热/比赛语汇、老者养老与诵读清单、祈祷/歌谣及章末未另发现足以确证的同类成片漏节。本次不把该局部未见新增硬错写成整段ready；上段衔接须联修，密集多义与典故仍待细查。

## 每段原文指纹

- `fw-ii4-383-01`：`3aaf51f9274b6a1c5493f2ef13820b9b5ce2d0808931e2c9bd2e9aa4bfc254ca`。
- `fw-ii4-387-01`：`31eb7b42065451993e6a4fcdc8d77abde3c648f4cec54d6adacd5c12d9a55067`。
- `fw-ii4-391-01`：`effce002c4793a42349f1faef6d5d3489c763e9494a375606df19c44b1a1070c`。
- `fw-ii4-395-01`：`96ca1a4bfc25689d40e1be1cb07e6503ecec7c4e9a347dbc475b86ba677aa118`。

## 结论

- 当前版本：**needs_revision**；`blocks_integration: true`。
- 7项均须定点处置。384–386、390、392等未逐项列出的生造词，不因报告未列问题便视作外部学术确认。
- 本次未改公共章稿、完成状态、断点、来源或录音。修订应另交版本，保留初译；不把本轮意见转成全文重写许可，更不先把complete当成已经审过。
