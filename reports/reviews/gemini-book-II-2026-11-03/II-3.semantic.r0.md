# II.3 语义审校报告（r0）

## 输入
- role: ai_review；executor: OpenAI Codex / review_book_ii_3；revision_round: 0。
- draft / workpack: `reports/reviews/inputs/gemini-book-II-2026-11-03/manuscript/chapters/II-3.json`；sha256: `f495511eeaa099f23cd20aef3ea83d09b5ee643264561cd60caf9e19749b422b`。
- 冻结清单: `reports/reviews/inputs/gemini-book-II-2026-11-03/manifest.json`；sha256: `cf897e49c4f4de390d9579eba0820f308fad0a387c08e94feb1bd43709c4d630`。
- 冻结来源表 sha256: `707e0358bd04a1b30f4fe6f213eb6f49f9e993cd0e242b3c5c809cb0c432881d`；冻结术语表 sha256: `46e5486f2e52f7aabd7758c1aa202fe7d3df71c81ed3aa950910be03bb095f96`。
- source_id: joyce-fp。见证按来源表为 Faded Page 转录的 Viking Press 1958 年第八印本；不冒称初版扫描核阅。
- original_sha256：每段分列于下。指纹按原字串 UTF-8 字节计算，无末尾新增换行。

## 范围与查阅
- 已完整分十二批读取并对照十二段 original、translation 与全部72注，共26423个英文空格分词。长清单、连续对话及否定条件另行定点回读；本报告不以中文篇幅短作漏译证据。
- 读过 AGENTS.md、docs/EDITORIAL_GUIDE.md、docs/SOURCES.md、docs/MANUSCRIPT_FORMAT.md、review-translation/SKILL.md 及 review-protocol.md，亦核冻结 glossary/terms.json 与来源表中 joyce-fp 登记。
- 页码来自同一冻结章 source_text 的 source-page 锚点，只用于本地定点定位。未重核1939版精确行号；下列段坐标沿录入值，不表示已逐行复算。
- 已读父任务统一比较记录 `reports/reviews/gemini-book-II-2026-11-03/source-comparison.json`（sha256: `68a43310f1ed5cbd58e04c76e659ad3a608aea78a60ac9b82edb3292c3664c8a`）中 II.3 摘要与差异列表：源HTML／文字与2026-11-01外部转录抽取相合，段内37处差异均属行末断字合并。本报告不将这些差异称作成片英文缺录；此项沿用父任务计算，未自行重开外部HTML或扫描本。
- 本执行者未读外部底本网页、扫描页、词源词典或剧目书目；父任务统一核外部见证。本轮不把未查的研究当证据。72注全部只引 joyce-fp 且标 proposal：可支持原文存在该字串，不能独自证明词源、地名、历史与剧目事实。
- 已逐条阅读注释，但尚未逐项完成外部事实核证。尤其 R-II3-15 须补剧目证据。其余未列为缺陷的历史注也不算已证实。
- 未审 draft、alternatives、音频、生成稿或跨章承接；未改公共章稿、来源、断点或音频。AI审校不充作人工审校，不能填写公共 reviewers。

## 各段已核范围与限度
### fw-ii3-309-01 / 309.01–314.36
- 已核：该段 original、translation 全文；注 ii3-tribalbalbutience, ii3-brides-eye-stammpunct, ii3-hiberio-miletians, ii3-tolvtubular, ii3-no-concern-guinness, ii3-tumbled-famas。
- original_sha256: `bff59b4270317adc047deeea22ee1bf30f0eb3ed8e160205fa155c0c2aaece71`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-315-01 / 315.01–320.36
- 已核：该段 original、translation 全文；注 ii3-butcheler-artsed, ii3-shufflebotham, ii3-burniface, ii3-publin, ii3-prepatrickularly, ii3-pukkelsen。
- original_sha256: `de1748d10d05ef42d352548f6c2e9666cf6247b038b4b63284a6c547029f3d42`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-321-01 / 321.01–326.36
- 已核：该段 original、translation 全文；注 ii3-husbands-capture, ii3-glasthule, ii3-boehernapark, ii3-wazwollenzee, ii3-irinwakes, ii3-emptybolly。
- original_sha256: `9f6acacdf2578317c409c41238fae2b5a45caa2881929be17a307082f6719131`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-327-01 / 327.01–332.36
- 已核：该段 original、translation 全文；注 ii3-tina-bat-talur, ii3-filius-cara, ii3-pianutunar, ii3-dollimonde, ii3-norgeyborgey, ii3-kaemper-daemper。
- original_sha256: `be902c510bfc8a5ef0904e5fefd62e191dbc9a9e740bd4fbd8922635eea60dad`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-333-01 / 333.01–338.36
- 已核：该段 original、translation 全文；注 ii3-szeszame-open, ii3-pad-podomkin, ii3-slowjaneska, ii3-katekattershin, ii3-chang-li-meng, ii3-bruyant-the-bref。
- original_sha256: `b182635a8c21f400ce2646eea8f0fa67cfe70e1261244876acae2a53e653204e`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-339-01 / 339.01–344.36
- 已核：该段 original、translation 全文；注 ii3-cheloven, ii3-molodeztious, ii3-chromean, ii3-polikoffs, ii3-toadlebens, ii3-krumlin。
- original_sha256: `e448a86c76c2b72e67b33f5ed18b112006b1291999d953927137a94dfe4862cc`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-345-01 / 345.01–350.35
- 已核：该段 original、translation 全文；注 ii3-irmenial, ii3-gospolis, ii3-creamtartery, ii3-novgolosh, ii3-burkeleys, ii3-bompromifazzio。
- original_sha256: `85dc08070d96ac29c1d1d1c0feebac1a6c9b66eb48c8c85accac39d6f809dbb3`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-351-01 / 351.01–356.36
- 已核：该段 original、translation 全文；注 ii3-knout-knittrick, ii3-chorney-choplain, ii3-arcdesedo, ii3-woodbine-willie, ii3-banzaine, ii3-bonhamme。
- original_sha256: `81909bfac20cb221719862a2b5a3140356c2a9111334aff40fc129cf65e69ea7`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-357-01 / 357.01–362.36
- 已核：该段 original、translation 全文；注 ii3-aubeyron, ii3-bismillafoulties, ii3-cunstuntonopolies, ii3-meschiameschianah, ii3-perseoroyal, ii3-fenegans。
- original_sha256: `c786e638f56c765c6c80658b430ce1d71b92b9f6a1095e3b51aa6a4e2f7fed36`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-363-01 / 363.01–368.36
- 已核：该段 original、translation 全文；注 ii3-almayne, ii3-missaunderstaid, ii3-kinahaun, ii3-registower, ii3-bacchulus, ii3-tunpother。
- original_sha256: `ec9f5fbff6026443c394aeb65680086b9fdf184099296985954d0dc1828f762b`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-369-01 / 369.01–375.36
- 已核：该段 original、translation 全文；注 ii3-brunos, ii3-bellchimbers, ii3-carolan, ii3-dieudonney, ii3-pandoria, ii3-paullabucca。
- original_sha256: `3d8320748563943b6e412b5c1302044d2f28a926f2057b1eca04696cb124ba8a`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。
### fw-ii3-376-01 / 376.01–382.30
- 已核：该段 original、translation 全文；注 ii3-roderick-oconor, ii3-obryan-macbruiser, ii3-clontarf, ii3-hymernians, ii3-maccormick, ii3-clanruckard。
- original_sha256: `818c699c45e967e60e722409e33b1d15e804293bbe55202d9b515bf704a11264`。
- 限度：只核冻结英文及中文之间的语义、词形、声形与注释主张；外部事实未逐条外核，精确行号未重算。未列问题不等于词义、典故已穷尽。

## 问题
优先级 P1：须先改的实质语义、出处或覆盖问题；P2：局部词项、数字或待定读路。是否阻断另见 blocks_integration，不由优先级自动推断。

### R-II3-01 — 漏译／无据增补
- 位置：`fw-ii3-309-01`；第309–310页；段坐标 `309.01–314.36`。精确行号未复核。
- 原文锚：equipped with supershielded umbrella antennas ... Bellini-Tosti coupling system ... capable of capturing skybuddies, harbour craft emittences, key clickings, vaticum cleaners。
- 当前中文／声明：此和谐凝聚引擎（名唤鼹鼠）由一处弹仓电池（称作敏敏-冰冰便携电池）驱动，经由地下管道输送烈酒与电讯。
- 问题：收音设备、耦合系统、扬声器及接收声响清单只剩泛称。译文添入原文没有的酒管输送、都柏林晚风及众生低鸣。技术描写同人体、酒馆的叠合随之消失。
- 依据：原文列明 Bellini-Tosti、vitaltone speaker、接收对象、eclectrically filtered、增益控制及频段；现译找不到这些句子的对应。原文没有“地下管道输送烈酒与电讯”。
- 定点建议：逐分句补回器件、连接及声响清单；删除无原文锚的景物。不能用酒馆场景概述替代。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-02 — 误词／术语
- 位置：`fw-ii3-309-01`；第309页；段坐标 `309.01–314.36`。精确行号未复核。
- 原文锚：Hiberio-Miletians and Argloe-Noremen。
- 当前中文／声明：希伯来-米利都血脉。
- 问题：把 Hiberio 直接写作“希伯来”，换入无文本支持的民族指称；同段注 ii3-hiberio-miletians 却释作爱尔兰古传后裔，正文与注自相抵牾。
- 依据：本处字形为 Hiberio，未写 Hebrew；本项目当前注也未提出希伯来读法。只凭混词不能静默加入这一血统。
- 定点建议：正文撤回“希伯来”；重核 Hibernia／Milesian 读路后定词。若另主张希伯来联想，须补字形、声音或文献依据。
- priority: P2；disposition_required: qualify。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-03 — 无据增补／漏译
- 位置：`fw-ii3-309-01`；第310–311页；段坐标 `309.01–314.36`。精确行号未复核。
- 原文锚：Culsen, the Patagoreyan ... pullupped the turfeycork ... out of Lougk Neagk。
- 当前中文／声明：巴塔哥尼亚酋长，在风暴席卷之荒原一口饮尽整皮囊马奶酒。
- 问题：把拔起湖中 turfeycork 的动作改写成喝马奶酒。新增荒原、风暴、皮囊；Lougk Neagk 及动作对象不见。
- 依据：pullupped、turfeycork、out of Lougk Neagk 都在当前英文中；马奶酒无对应词。Patagoreyan 多义未核，不能据其音似地名补完整游牧剧情。
- 定点建议：保留拔起对象及湖名；另注 Culsen、Patagoreyan 等待核读法。删去马奶酒和附加场景。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-04 — 漏译／误词／无据增补
- 位置：`fw-ii3-309-01`；第312–313页；段坐标 `309.01–314.36`。精确行号未复核。
- 原文锚：Lorimers and leathersellers ... fletcherbowyers, girdlers, mercers, cordwainers and first, and not last, the weavers。
- 当前中文／声明：马具匠与皮革商，制皮匠与盐商，白镋匠与壁纸涂工，教区文书，造箭匠与铸钟匠，齐聚一堂，吵嚷叫骂，杯盏交错。
- 问题：工匠清单截断；girdlers、mercers、cordwainers、weavers 全无对应。“铸钟匠”也不对应 bowyers。“首先、并非最后”的织工强调消失，换成吵嚷杯盏场面。
- 依据：原文清单连续，结尾明确另强调 weavers。译文以“齐聚一堂”收束，并未逐项转达。
- 定点建议：补齐制带、布商、鞋匠、织工等项；核 bowyer，保留排列与末项反转。删除替正文收尾的酒宴景物。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-05 — 漏译
- 位置：`fw-ii3-309-01`；第314页；段坐标 `309.01–314.36`。精确行号未复核。
- 原文锚：who caused the scaffolding to be first removed ... who ... removed the planks they were wanted。
- 当前中文／声明：由此清算流质胆量之代价，金银测计官，将硬币散碎堆入舱底，秤杆微翘，账目分明。轰隆！。
- 问题：在计价与雷鸣之间删去脚手架、木板移除及冲突证词，连同提问、回答和踢向证人的动作。跌落前的具体叙述断裂。
- 依据：原文由“who caused the scaffolding”追问何人移除，并写“drew a kick at witness but (missed)”；当前中文径跳“轰隆”。
- 定点建议：补回询问、回答、证人及踢空动作。指代存疑可注，不可以账目分明代替。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-06 — 漏译
- 位置：`fw-ii3-315-01`；第319页；段坐标 `315.01–320.36`。精确行号未复核。
- 原文锚：where's Horace's courtin troopsers? —I put hem behind the oasthouse ... I carsed his murhersson goat in trotthers。
- 当前中文／声明：凭其鸟喙之笼套，理查三世，以为汝之腰围愈发粗壮，恰合其公鹿之安逸。海流顺其巨人般咽喉奔涌而下。
- 问题：关于裤子去向的问答整块消失。“我把它放在烘焙房后面”及山羊穿裤子的后续也未转达。中文直接跳到吞咽海流，再添“上公堂、牢狱”等。
- 依据：原文有明确问句、Pukkelsen 回答及 goat in trotthers。是否还有词形叠义，不影响裤子、处所、山羊这三项均须处理。
- 定点建议：逐句补回问答与山羊裤装。删除“我定要向公堂讨回公道，叫尔等尝尝牢狱滋味”等无锚补笔。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-07 — 人称／人物关系
- 位置：`fw-ii3-315-01`；第317页；段坐标 `315.01–320.36`。精确行号未复核。
- 原文锚：Allkey dallkey, sayd the shop's housebound, for he was as deep as the north star。
- 当前中文／声明：万事顺遂，店中主妇言道，因她深沉若北极星。
- 问题：把 he 改成“她”，又将 shop’s housebound 锁定为主妇，悄悄另造发言人。
- 依据：该分句显写 he；“店中主妇”不是字面的唯一释法。当前稿没有说明人称变换。
- 定点建议：保留男性指代；重核 housebound／husband 双关，不凭“店中”补女主人。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-08 — 误译／无据增补
- 位置：`fw-ii3-315-01`；第318页；段坐标 `315.01–320.36`。精确行号未复核。
- 原文锚：a mouse, a mere tittle, trots off with the whole panoromacron picture。
- 当前中文／声明：一只小鼠，微末微尘，携整块干酪疾速逃遁，钻入墙隙享受横财。
- 问题：把 picture 变成干酪，再添钻墙、横财。原文小与全景的对举改成常见偷食故事。
- 依据：原文动作对象为 whole panoromacron picture；没有 cheese、墙缝或横财。
- 定点建议：恢复“全景／全幅画面”这一对象，保留 mouse、tittle 与宏大画面的尺度反差。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-09 — 漏译／梗概替正文
- 位置：`fw-ii3-321-01`；第324–325页；段坐标 `321.01–326.36`。精确行号未复核。
- 原文锚：the outlook for tomarry (Streamstress Mandig) beamed brider ... Giant crash in Aden ... Burial of Lifetenant-Groevener Hatchett ... Anna Lynchya Pourable! One and eleven。
- 当前中文／声明：混乱焦点聚集，众人围拢窥探。正如我等专栏撰稿人在上月闲谈讲道中之预言，流言四溢。鸟群飞掠，飞禽翔集，古兆坐实逼近之婚典。
- 问题：整段天气预报、新闻及售卖广告串列缩成流言、鸟兆与婚典。低压、降水、局部毛雨、亚丁事件、葬礼和价格等各自有词锚，现译未转达。
- 依据：原文从 predicted 接续长段天气用语，再切新闻和广告；不是一句“流言四溢”。现译也添“众人围拢窥探”“喜鹊登枝”。
- 定点建议：逐类补回播报内容、数目、短句与切换节奏。婚礼双关可保留，不能吞掉播报表层。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-10 — 否定／语气反向
- 位置：`fw-ii3-321-01`；第326页；段坐标 `321.01–326.36`。精确行号未复核。
- 原文锚：and be danned to ye。
- 当前中文／声明：愿汝受福。
- 问题：诅咒改成祝福，使施洗段落丢掉冒犯、混杂语气。
- 依据：danned 明显与 damned 相邻；不论是否兼有丹麦词形，不能直接译成受福，且本处没有 bless。
- 定点建议：保留诅咒或保守呈现双关，注记不能仅按庄严施洗礼理解。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-11 — 漏译／无据增补
- 位置：`fw-ii3-327-01`；第330–331页；段坐标 `327.01–332.36`。精确行号未复核。
- 原文锚：Knock knock. War's where! Which war? The Twwinns ... Woos without! Without what? An apple ... And you Tim Tommy Melooney, I'll tittle your barents if you stick that pigpin upinto meh!。
- 当前中文／声明：叩门，叩门，重重叩响命运门环，喜报频传。……听那新婚密室里床榻之吱呀与娇喘，老妇在门外窃听偷笑。
- 问题：连续叩门问答删成喜报；谁在门外、哪场战争、孪生与苹果的词链均不见。Tim Tommy 的直接警告也消失，换成老妇窃听、青年吹哨与众神俯瞰的性爱梗概。
- 依据：原文有至少三组 knock knock 与紧跟的问答，且有明确第二人称警告。原文没有上述老妇、青年和众神旁观场面。
- 定点建议：逐组恢复问答与说话对象；保留 pigpin／barents 等未决词。删除代替原文的完整旁观剧情。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-12 — 漏译／列表
- 位置：`fw-ii3-327-01`；第331页；段坐标 `327.01–332.36`。精确行号未复核。
- 原文锚：from your tarns, thwaites and thorpes, withes, tofts and fosses, fells, haughs and shaws, lunds, garths and dales。
- 当前中文／声明：听那新婚密室里床榻之吱呀与娇喘，老妇在门外窃听偷笑，青年在街角吹响口哨，众神自天际俯瞰。
- 问题：连续地貌、聚落词清单没有中文对应，亦无注说明。该清单夹在婚配、族群、度量等词链中，不能用性爱宏论略过。
- 依据：当前英文逐列 tarns 至 dales；现译从问句跃到“借由我等基督教化”。
- 定点建议：按序转达各词；若译名待核，先留音形并记录损失，勿全删清单。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-13 — 无据增补／越界接续
- 位置：`fw-ii3-327-01`；第332页；段坐标 `327.01–332.36`。精确行号未复核。
- 原文锚：Enterruption. Check or slowback. Dvershen.。
- 当前中文／声明：就在这当口，杂耍舞台上的滑稽双丑赫然登场亮相：巴特与塔夫！两位从污秽泥泞战壕里死里逃生的退伍老兵。
- 问题：原段以插断、制止／回退、转向三句收束。中文其后添整段人物履历、克里米亚舞台与即将枪击将军的预告，替下一段先定人物身份、叙事顺序及演出事实。
- 依据：所引英文后本段即止。后文确出现 butt／taff，也不能反向证明这些新增句子属于此处正文。
- 定点建议：删去新增预告整段；只处理原有三句及其广播／舞台含义。后文信息留在后文。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-14 — 数目
- 位置：`fw-ii3-333-01`；第338页；段坐标 `333.01–338.36`。精确行号未复核。
- 原文锚：thirty two eleven。
- 当前中文／声明：三十三号十一番。
- 问题：thirty two 误成三十三。
- 依据：当前英文写 thirty two，非 thirty three。该数还可能与全书重复数字相连，不能任意增一。
- 定点建议：恢复三十二；另存其 32／11 读法与语境，不添“号、番”作唯一格式。
- priority: P2；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-15 — 出处／外部事实
- 位置：`fw-ii3-333-01`；第338；note ii3-chang-li-meng页；段坐标 `333.01–338.36`。精确行号未复核。
- 原文锚：Chang-li-meng ... that man d'airain。
- 当前中文／声明：法国十九世纪流行魔术与杂耍剧目《大金人》（L'homme d'airain）中角色戏名。
- 问题：注将一个具体年代、国家、剧名及角色身份写成既成事实，却只引 joyce-fp 原著。proposal 不能替这串书目事实供证。此次未核该剧是否存在，不据印象判成假文献。
- 依据：冻结来源表 joyce-fp 是英文见证，不是该剧的剧目档案、书目或研究。原文只有词形，并未交代十九世纪或戏名。
- 定点建议：补可重开核查的剧目／书目与页段；未补前撤去事实断言，仅记字形及待核读路。父任务外检尚未取得法国剧角色原页；另有 Charlemagne／mandarin 线索，但未核原论证，故本报告不据此另定典故。
- priority: P1；disposition_required: qualify。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-16 — 漏译／专名清单
- 位置：`fw-ii3-339-01`；第342页；段坐标 `339.01–344.36`。精确行号未复核。
- 原文锚：Mr Whaytehayte's three buy geldings Homo Made Ink, Bailey Beacon and Ratatuohy。
- 当前中文／声明：向怀特海特先生之三匹阉马展示鹰隼之道。
- 问题：三匹马的名字全删，失去赛马播报中具体参赛对象及音形线索。
- 依据：原文逐项列 Homo Made Ink、Bailey Beacon、Ratatuohy；现译只剩数量。
- 定点建议：保留三名，按可核读法音译或留原名；不得以“三匹阉马”算整句完整。
- priority: P2；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-17 — 数目／声形
- 位置：`fw-ii3-345-01`；第347页；段坐标 `345.01–350.35`。精确行号未复核。
- 原文锚：elve hundred and therety and to years。
- 当前中文／声明：千三百二十载。
- 问题：将 eleven hundred and thirty-two 的近音次序改成一千三百二十。至少丢掉 elve hundred 与 therety／to 的现有组合。
- 依据：原词依序 elve hundred / therety / to，未写 thirteen hundred / twenty。与本章开头 patent number 1132 还能互校；本报告不以此断定全部象征。
- 定点建议：按一千一百三十二这一首要读路修数；若主张另一年数，须解释每个词形，不能静默换序。
- priority: P2；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-18 — 军阶／误词
- 位置：`fw-ii3-351-01`；第351页；段坐标 `351.01–356.36`。精确行号未复核。
- 原文锚：I was a bare prive without my doglegs。
- 当前中文／声明：我乃无拘无束之下士。
- 问题：把 prive 的 private 读路改成下士；又用“无拘无束”吸收 bare／without，使裸身、无装饰或无犬腿的多义线索不见。
- 依据：军旅上下文支持 private；下士另属 corporal，原文此处未写该军阶。doglegs 的具体所指本轮未定。
- 定点建议：至少撤回下士这一擅定军阶；保留 private、bare、without 的现有关系，注记 doglegs 未决。
- priority: P2；disposition_required: decide。
- blocks_integration: false；可先登记读法，单独此项不阻断。

### R-II3-19 — 漏译／时间与情态
- 位置：`fw-ii3-357-01`；第359页；段坐标 `357.01–362.36`。精确行号未复核。
- 原文锚：he wassand no better than he would have been before he could have been better than what he warrant after。
- 当前中文／声明：彼并不比往昔更好。
- 问题：六项指控中第五项压成单一今昔比较。would have been、before he could have been、after 的回折全失；正文也未注明采取哪一路句法。
- 依据：原文不只有“比过去更好”，而反复套比较、可能性、前后。Joyce 的困惑不授权删掉这些关系。
- 定点建议：重列比较双方、时间先后与情态，再定中文；保留纠缠感，必要时短句并注句法损失。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-20 — 动作方向倒置
- 位置：`fw-ii3-363-01`；第363页；段坐标 `363.01–368.36`。精确行号未复核。
- 原文锚：upsadaisying coras pearls out of the pie。
- 当前中文／声明：将珍珠塞入馅饼之中。
- 问题：out of 被改成塞入，取出变放入。
- 依据：动词串或有其他双关，明确介词 out of 的方向仍不能无据反转。
- 定点建议：恢复从馅饼取／捞出珍珠这一方向；Cora 与 pearls 的隐义另注。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-21 — 条件否定倒置／误词
- 位置：`fw-ii3-363-01`；第368页；段坐标 `363.01–368.36`。精确行号未复核。
- 原文锚：never to ate the sour deans if they weren't having anysin on their consients。
- 当前中文／声明：若良心有愧切莫吞食酸黄瓜。
- 问题：weren’t having anysin 是“没有罪”的条件，现译改成“有愧”。此外 sour deans 直接变酸黄瓜，也无 pickle／cucumber 字锚。
- 依据：if 从句含 weren’t 与 anysin，主句含 never；两处否定须分别处理。sour deans 至少保留 deans 字形，若读 sardines 则更不能定成黄瓜。
- 定点建议：先校正条件否定；重核 sour deans 的酸／教长／鱼类读路，正文取保守法，注列其余。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-22 — 漏译／人物关系
- 位置：`fw-ii3-369-01`；第373页；段坐标 `369.01–375.36`。精确行号未复核。
- 原文锚：Begetting a wife which begame his niece by pouring her youngthings into skintighs。
- 当前中文／声明：将青春脂膏注入紧身衣中纳为新妇。
- 问题：删掉妻子变成 niece 的关系变化，把整句缩成娶新妇。
- 依据：which begame his niece 明写在关系从句中；是否影射具体人物未核，但 niece 这一亲属称谓不能消失。
- 定点建议：补回妻子／侄女的关系转折，并保留讹拼及主体存疑；不为它补实在家谱。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-23 — 无据增补／声形
- 位置：`fw-ii3-376-01`；第379页；段坐标 `376.01–382.30`。精确行号未复核。
- 原文锚：With seven hores always in the home of his thinkingthings ... Two Idas, two Evas, two Nessies and Rubyjuby。
- 当前中文／声明：七重风暴常驻其脑海思绪，无声冥想之殿堂。两个艾达，两个夏娃，两个内茜与鲁比。
- 问题：把 hores 定成风暴，英文无 storm 对应；紧跟的七个女性名额也与风暴断开。hours／whores 的近音至少须重核，不可另造天气。
- 依据：原文 seven 与 Two＋Two＋Two＋一名连读；词形 hores 不提供“风暴”这个常义。本报告仅指读路损失，不断言七名对应实在人物。
- 定点建议：撤回风暴；保留七个形象与思绪空间的关系，在注中说明 hores 的时刻／娼妓近音待核。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-24 — 误词
- 位置：`fw-ii3-376-01`；第379页；段坐标 `376.01–382.30`。精确行号未复核。
- 原文锚：The rye is well for whose amind but the wheateny one is proper lovely。
- 当前中文／声明：黑麦固然合意，大麦麦芽尤显甘美。
- 问题：wheateny 的 wheat 指向小麦，现译换成大麦，且又加麦芽。
- 依据：原文与 rye 构成谷物对举；此处没有 barley 或 malt，不能因酒馆背景替换原料。
- 定点建议：改回小麦读路；如主张其他隐语，须补证据。
- priority: P2；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-25 — 动作／因果倒置
- 位置：`fw-ii3-376-01`；第381页；段坐标 `376.01–382.30`。精确行号未复核。
- 原文锚：on footback, owing to the leak of the McCarthy's mare。
- 当前中文／声明：在众人骑马步行各自奔赴泥泞城堡之后，彼等借麦卡锡母马之踪迹沿蜿蜒小径离去。
- 问题：把足行的 footback 添成骑马步行，又将 leak／lack 的缺马原因变成借母马踪迹离去。人员如何散去的因果重写。
- 依据：footback 与 horseback 相互作弄；owing to 明列原因。leak 本身不是踪迹，且英文没有循踪一词。
- 定点建议：保留足行与缺马／漏失的讹词关系，勿补骑乘和循踪。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-26 — 计量／出处
- 位置：`fw-ii3-376-01`；第382页；段坐标 `376.01–382.30`。精确行号未复核。
- 原文锚：considerably more than the better part of a gill or naggin of imperial dry and liquid measure。
- 当前中文／声明：其总量远超一吉尔或一夸脱之度量。
- 问题：把 naggin 无说明换成 quart 对应的“夸脱”。原文单位不同；本轮未外核 naggin 各地区实际容量，不能补造精确换算。
- 依据：当前文本是 naggin，非 quart；本次冻结来源亦未给量制释义。
- 定点建议：先保留 naggin 音译并补可靠量制辞书；取得版本、地区与容量后再定中文，不直接改夸脱。
- priority: P2；disposition_required: qualify。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

### R-II3-27 — 覆盖声明／验收
- 位置：`chapter`；第全章页；段坐标 `309.01–382.30`。精确行号未复核。
- 原文锚：coverage: complete / coverage_review。
- 当前中文／声明：逐段英中对读并补全……全篇完整译文与注释。
- 问题：当前“全篇完整”声明与上列可逐句指出的遗漏冲突。英文原文齐备，不能代替中文正文完整。
- 依据：R-II3-01、04、05、06、09、11、12、16、19、22 均给出目前未译或改写的具体正文锚，非按中英字数比例推断。
- 定点建议：整合者先登记实际漏项并修复，再做中文覆盖复核；在此之前撤回或限定完整声明。报告本身不改覆盖状态。
- priority: P1；disposition_required: fix。
- blocks_integration: true；现稿须改或补证，不能按完整中文放行。

## 中文复核
- 现稿反复添“巍峨、浩渺、万古、至高、苍茫、天地”等无原文锚的修饰。问题先在语义增写，不能仅当文风润色。上列增写须先删，再检查“之／其／彼等”、多层定语、无必要复数及长句。
- 例如原文“Business. His bestness. Copeman helpen.”译成“正经行当，立身之本，不负先祖血汗。他之极致，出神入化，名扬四海。商贾相助，利市大兴，货如轮转。”其中先祖血汗、名扬四海等均无词锚。短促分镜反成套语扩写。不能借余光中规范再抹去Joyce原有重复与停顿。

## 结论
- 当前版本：**needs_revision**。十二段语义对读已完成；外部事实与版本逐行校勘尚未完成。无一“整章通过”结论。
- 共27项：26项阻断，另1项（R-II3-18）登记选择。本报告仅列可定点处置的问题，不充作全章重译。
- 优先补正文遗漏、纠正方向与否定，再删除无锚剧情，最后核数字、计量及事实注。现稿即有章末独饮与枪击故事，也不能凭梗概齐备认作正文覆盖完整。
- 尚待父任务统一核外部底本；未得底本不妨碍上述英中对照问题成立。修订后须逐项说明采用、未采用、补证或延期，并绑定新稿SHA。
- 附：`II-3.evidence.json` 保存输入指纹、逐段读完范围及稳定问题编号。
