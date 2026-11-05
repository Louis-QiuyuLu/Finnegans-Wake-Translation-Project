# 第二卷第一章 II.1 独立语义审校 r0

## 输入
- role: ai_review；executor: OpenAI Codex 子代理 `/root/review_book_ii_1`；不是人工终审，也不是初译者自检。
- revision_round: 0。只审冻结版本，只写本报告及同名 evidence JSON；不改章稿、来源、断点、音频，不推送。
- workpack: `reports/reviews/inputs/gemini-book-II-2026-11-03/`；manifest SHA256: `cf897e49c4f4de390d9579eba0820f308fad0a387c08e94feb1bd43709c4d630`。
- draft: `reports/reviews/inputs/gemini-book-II-2026-11-03/manuscript/chapters/II-1.json`；SHA256: `5b6225652a5802915450a993519bbfbd1eea4315bd372475313001249af764d0`。
- frozen sources/catalog.json SHA256: `707e0358bd04a1b30f4fe6f213eb6f49f9e993cd0e242b3c5c809cb0c432881d`。
- frozen glossary/terms.json SHA256: `46e5486f2e52f7aabd7758c1aa202fe7d3df71c81ed3aa950910be03bb095f96`。
- source_id: `joyce-fp`；Faded Page 所列 Viking Press 1958年第八印本转录，不能改称1939初版逐字见证。
- original_sha256（十段原字串顺次拼接、不另加换行）: `8c1f31c8a97ee05aa37dc76a5c00c0b4790e447eac4b825e4666b44a3854fb2b`。逐段指纹见下。

## 范围与查阅
- 分五批完整读取10段 original、translation、全部60注，共14186个按空白分隔的英文词。逐句检查动作、主客、否定、指代、数量和连接；不以字数比判漏译。
- 读过仓库 AGENTS.md、docs/EDITORIAL_GUIDE.md、docs/SOURCES.md、docs/MANUSCRIPT_FORMAT.md、review-translation/SKILL.md 及 references/review-protocol.md；读取冻结来源表 joyce-fp 记录与全份冻结术语表。
- 本地 source_text 的页锚用来定本报告页码。**全部精确行号均未重核**；保留所给 locator 只作输入标识，不视为已验的逐行坐标。
- 将 source_text 排除页码标签、去空白后，与10段 original 顺次合并比较。仅12处行末连字符不同：sojest-iveness、wor-rawarrawurms、no-vembrance、nar-rowed、might-whomight、accomoda-tionnooks、wib-frufrocksfull、nudge-meroughgorude、brooch-bronze、spouse-founderess、hooker-crookers、雷词 too-ry。差别均是 original 删除连字符。此次比较未发现英文正文词句缺段，但不能证明扫描页校勘或所有去连字符选择正确。
- 外部资料未由本子代理重新打开；以下三项由父任务实际定点查阅后转交，见同目录 `evidence.json` 的 E-SPAE／E-CITIES／E-SHROVE，清楚标出来源与限度：
  - [Dictionary of the Scots Language, spae](https://dsl.ac.uk/entry/snd/spae)：I v.1 Combs(ix)，spae-wife 为 female fortune-teller；历史引例写 spaewife。用于R-II1-16。
  - [UCC CELT, The Second Battle of Moytura](https://celt.ucc.ie/document/T300011/)：§§1–7，四城学艺、从各城携出圣物。用于R-II1-15；不据此证明 Joyce 意图。
  - [Dictionary.com, Shrove Sunday](https://www.dictionary.com/browse/shrove-sunday)：Sunday before Ash Wednesday。用于R-II1-02；普通字面Sundy／Sunday也已足以指出星期错换。
- 未核：原刊扫描、全章版本差异、任何既有中译、录音、全部外语词源与学术典故。未声称查阅词典、手稿、论文或扫描页。来源表登记访问日期不等于本轮已读。

## 逐段核对记录
- `fw-ii1-219-01`；219.01–222.36；original SHA256: `860de0328509813a4b672b6b0f33d85da71dc8bc955d3a869435b4053d6f4811`。原文、当前中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描。本段问题：R-II1-01, R-II1-15。
- `fw-ii1-223-01`；223.01–226.36；original SHA256: `c54ad61d6c899e2d96d0ef3c192fa68448a2ffd038b372d9605df443abe64eef`。原文、中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描；逐注限度见下，未另立正文硬错。
- `fw-ii1-227-01`；227.01–230.36；original SHA256: `e47ff20b8ede475dc76f878fdc10294a8405995f652300bdb340b7b4444c904a`。原文、当前中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描。本段问题：R-II1-02。
- `fw-ii1-231-01`；231.01–234.36；original SHA256: `e0a332db7fb189ca882d9d9b30b9894b41dea76ea5094c24964b376515409d5c`。原文、当前中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描。本段问题：R-II1-03, R-II1-04。
- `fw-ii1-235-01`；235.01–238.36；original SHA256: `7ffc24d241a01d86d4e5f43560eeb3685e5ba0a3510a7a3d94536453f4e52e6a`。原文、中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描；逐注限度见下，未另立正文硬错。
- `fw-ii1-239-01`；239.01–242.36；original SHA256: `e45afd40baa77d9bd46e598160c731800a6b4d87e05aee220ab8da815e5bce94`。原文、当前中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描。本段问题：R-II1-05, R-II1-16。
- `fw-ii1-243-01`；243.01–246.36；original SHA256: `4dbff8d74f59db84e7ed593e80d11a5e1132792c3d1ec8415b22c1eab2ced881`。原文、中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描；逐注限度见下，未另立正文硬错。
- `fw-ii1-247-01`；247.01–250.36；original SHA256: `daaf7e04233fa1623e880f2f83ccddd3405efe91ef58980e66a387a86c0af213`。原文、当前中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描。本段问题：R-II1-06, R-II1-07。
- `fw-ii1-251-01`；251.01–254.36；original SHA256: `aaa91bf613f63439f0923297be63a91fe0f8eea9fa70020b7bc52e96bc981e99`。原文、当前中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描。本段问题：R-II1-08, R-II1-09, R-II1-10。
- `fw-ii1-255-01`；255.01–259.10；original SHA256: `abcee69d0a23ee8788e5758f6e5492ad01cb6cfd19df793d3cbb23f649f72944`。原文、当前中文、6注均完整读完；与邻段接缝连读。未核精确行号、外部词源与扫描。本段问题：R-II1-11, R-II1-12, R-II1-13, R-II1-14。

## 问题
优先级：P1会改变正文事实、动作、关系或注释事实；P2限于局部语义、数字回声或尚待选择的双关。`blocks_integration`只约束当前译注，不代替人工审校。

### R-II1-01 [P1]
- ID／页与所给坐标：`fw-ii1-219-01`；220页；所给219.01–222.36；精确行号未重核。
- 原文短锚：`a month's bunch of pretty maidens`。
- 当前中文：「整整一月十二名娇媚少女」。
- 类别：无据增补／数量。
- 问题／依据：month's bunch 没写 twelve。「一月」不能推出十二少女；同段注 ii1-mime-title-trio 又断言二十八位同伴，两处人数冲突。
- 必要修复建议：删去「十二名」，保留按月成束／月相之歧义。若选定人数，另交来源并协调正文与注释。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-02 [P1]
- ID／页与所给坐标：`fw-ii1-227-01`；227页；所给227.01–230.36；精确行号未重核。
- 原文短锚：`Shrove Sundy MacFearsome`。
- 当前中文：「在忏悔星期二……向麦克菲尔森宣泄净尽」。
- 类别：误译／日历。
- 问题／依据：Sundy 明示 Sunday；译文换成 Tuesday。即使整串兼作人名，也不能凭常见 Shrove Tuesday 静默改星期。
- 必要修复建议：恢复星期日层，并保留人名缀合；若拟写忏悔星期二，须另列其声音线索，不能替换 Sunday。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-03 [P1]
- ID／页与所给坐标：`fw-ii1-231-01`；232页；所给231.01–234.36；精确行号未重核。
- 原文短锚：`as her lucky for the Rio Grande`。
- 当前中文：「充作驶向里约热内卢之幸运星」。
- 类别：误译／地名。
- 问题／依据：Rio Grande 与 Rio de Janeiro 并非同名。此稿既不保留 Grande，又凭空选定巴西城市。原文只写 Rio Grande；本轮不替它判定具体河流、港口或船歌出处。
- 必要修复建议：恢复 Rio Grande 的音形或按核实地名翻译；另注可能的歌谣关系。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-04 [P2]
- ID／页与所给坐标：`fw-ii1-231-01`；232页；所给231.01–234.36；精确行号未重核。
- 原文短锚：`a glaciator to submerger an Atlangthis`。
- 当前中文：「冰川封冻亚特兰蒂斯」。
- 类别：误译／主要动作。
- 问题／依据：submerger 的淹没动作换成封冻。glaciator 可引入冰川层，却不能吞掉 submerge。
- 必要修复建议：同句兼留冰川／冰期施动者与沉没动作；不必为求顺口只留冰冻。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-05 [P1]
- ID／页与所给坐标：`fw-ii1-239-01`；239页；所给239.01–242.36；精确行号未重核。
- 原文短锚：`we are but yours ... we shall ope to be ores`。
- 当前中文：「我等……尚属汝之雏鸟……终有一日……化作汝之所属」。
- 类别：误译／指代与转折。
- 问题／依据：当前中文把前后两端都译成归你所有。英文以 yours 对 ores，后者至少保留 ours 的明显声形；后文又紧接 amanseprated、maidfree。中文抹去转折，并把女声对自身归属的诉求交还对方。ores 仍可兼矿石、whores等读法，本轮不裁为单义。
- 必要修复建议：恢复 yours 与 ores／ours 的对照；注中列其他声形读法，不把 ours 擅换 yours。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-06 [P2]
- ID／页与所给坐标：`fw-ii1-247-01`；248页；所给247.01–250.36；精确行号未重核。
- 原文短锚：`Six thirteens at Blanche de Blanche's`。
- 当前中文：「布兰奇·德·布兰奇家十三对佳丽」。
- 类别：误译／数量分组。
- 问题／依据：Six thirteens 的 six 消失，另加原文没有的「对」。十三对是二十六，六个十三的表层数式是七十八；但本轮不据此判定实际人数。
- 必要修复建议：保留「六个十三」或同等数式，并研究场所／价钱等潜在读法；不要自行变成十三对人物。
- disposition_required: fix。
- blocks_integration: false。

### R-II1-07 [P1]
- ID／页与所给坐标：`fw-ii1-247-01`；247页；所给247.01–250.36；精确行号未重核。
- 原文短锚：`apple, bacchante ... quasimodo ... xray, yesplease, zaza, philomel, theerose`。
- 当前中文：「苹果绿、女祭司红……卡西莫多赭……X光青、应承粉、扎扎绯红、夜莺灰、茶香玫瑰粉」。
- 类别：声形漏失／无据增补。
- 问题／依据：英文从 apple 到 zaza 按 A–Z 排列，随后另添 philomel、theerose。中文不注字母顺序，且给每个词强配确定色号；quasimodo=赭、xray=青、yesplease=粉、zaza=绯红，在已给正文与60注中均找不到依据。前文 tints 只建立色彩语境，不能证明每项色值。
- 必要修复建议：补记 A–Z 列举结构。区分可查色名、词义与自拟色彩；无证据的色号删去或明列为本项目补偿，不写成原词固定意义。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-08 [P2]
- ID／页与所给坐标：`fw-ii1-251-01`；252页；所给251.01–254.36；精确行号未重核。
- 原文短锚：`grandson's grandson's grandson's grandson / grandmother of the grandmother of his grandmother's grandmother`。
- 当前中文：「其玄孙之曾孙／其曾祖母之曾祖母」。
- 类别：误译／代数与重复。
- 问题／依据：原文两条链各重复四次 grandson／grandmother。grandson 每次隔两代，中文「玄孙之曾孙」只到第七代；「曾祖母之曾祖母」也不能对上四重 grandmother。更重要的是四重回声与对称关系一并消失。
- 必要修复建议：按原链逐层保留，或核清亲属称谓后译；不得用不等价的代数缩写。
- disposition_required: fix。
- blocks_integration: false。

### R-II1-09 [P2]
- ID／页与所给坐标：`fw-ii1-251-01`；251页；所给251.01–254.36；精确行号未重核。
- 原文短锚：`I is a femaline person ... U unisingular case ... for the prize of a thou`。
- 当前中文：「“我”乃阴性之身……“汝”，乃独一单数之格……为千金重赏」。
- 类别：声形／人称链。
- 问题／依据：thou 可兼作 thousand 的口语缩写，故「千金」未必全错；但相邻 I、O、U、person、gender、case 明写语法人称游戏。只留赏金读法，且无注释存 thou=汝，丢掉近处呼应。
- 必要修复建议：可保留金钱一路，但注出 thou 的第二人称层及 I／O／U 链；或正文双关补偿。
- disposition_required: decide。
- blocks_integration: false。

### R-II1-10 [P2]
- ID／页与所给坐标：`fw-ii1-251-01`；254页；所给251.01–254.36；精确行号未重核。
- 原文短锚：`Longabed ... the herblord the gillyflowrets so fain fan to flatter about`。
- 当前中文：正文「领主」；注 ii1-herblord-gillyflowrets「描摹少女群芳对肖夫之顶礼膜拜」。
- 类别：指代／无据剧情；uncertain。
- 问题／依据：该长段刚出现 largely longsuffering laird、heavy Humph with airy Nan，又称 Longabed、more than man，接下段 Father of Truants。注释却径把 herblord 锁为肖夫，未解释父亲／巨人线索。这不足以判定肖夫必错，但现注把未证身份写死。
- 必要修复建议：暂不锁定肖夫；交代本段父亲、巨人、群芳的交叠。若坚持肖夫，须给具体句法或研究依据。
- disposition_required: qualify。
- blocks_integration: false。

### R-II1-11 [P1]
- ID／页与所给坐标：`fw-ii1-255-01`；256页；所给255.01–259.10；精确行号未重核。
- 原文短锚：`what happened to our eleven in thirtytwo antepostdating the Valgur Eire`。
- 当前中文：「在爱尔兰通俗纪年之前三十年我们那十一人究竟发生何事」。
- 类别：误译／数字与关系。
- 问题／依据：thirtytwo 是32，现译成30。antepostdating 同时缀接前后定年，译文只剩「之前」，还把含混串语定成某纪年前三十年的事件。
- 必要修复建议：先恢复11与32，再保留 ante／post 两向定年歧义；有史事解释时另注，不凭解释改数字。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-12 [P2]
- ID／页与所给坐标：`fw-ii1-255-01`；257页；所给255.01–259.10；精确行号未重核。
- 原文短锚：`pleating a pattern Gran Geamatron showed them`。
- 当前中文：「编织女地质学家向其展示之……图案」。
- 类别：无据增补／人物身份。
- 问题／依据：Gran Geamatron 未明说 geologist，也未引入一位从事地质研究的女子。译文将陌生名号直接替换为职业身份，注释又未交代此取舍；pattern 的近处语境反而要求保留几何／织图层的可能。此处不裁断唯一词源。
- 必要修复建议：保留名号或审慎处理其词形；若主张地质学家，先说明如何从 Geamatron 推出此职业，再外核。
- disposition_required: qualify。
- blocks_integration: false。

### R-II1-13 [P2]
- ID／页与所给坐标：`fw-ii1-255-01`；259页；所给255.01–259.10；精确行号未重核。
- 原文短锚：`Grant sleep in hour's time, O Loud!`。
- 当前中文：「主啊，恩赐片刻安眠！」。
- 类别：误译／时间关系。
- 问题／依据：in hour's time 指一小时后／到时入睡的时间距离；「片刻安眠」改成睡眠时长很短。正文不再保留 hour。
- 必要修复建议：恢复入睡时点与 hour；如主张戏拟 hour／our 等，再注声音层。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-14 [P1]
- ID／页与所给坐标：`fw-ii1-255-01`；259页；所给255.01–259.10；精确行号未重核。
- 原文短锚：`That they do ming no merder.`。
- 当前中文：「免生混浊污秽。」。
- 类别：漏译／否定的行为对象。
- 问题／依据：ming 可带混合、臭味等层，但 merder 的 murder／杀戮声形十分显著。译文只保留污秽，整个禁止伤人杀戮的行为层消失；现注未记录损失。本轮不据此判作唯一词源。
- 必要修复建议：在祈愿中兼留不作恶／不杀戮与 ming 的声形；至少注出为何正文只留污秽。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-15 [P1]
- ID／页与所给坐标：`fw-ii1-219-01`；219页；所给219.01–222.36；精确行号未重核。
- 原文短锚：`Findrias, Murias, Gorias and Falias / ii1-four-coroners-cities`。
- 当前中文：注「达南神族……自北方带来的四座神异之城与四大圣物」。
- 类别：出处／事实错置。
- 问题／依据：注释把神族从北方「带来」的宾语写成四座城和圣物。父任务实读 CELT《The Second Battle of Moytura》§§1–7：神族在四城学艺，从各城带出石、矛、剑、鼎，未带走四城。来源只能证明神话文字，不直接证明 Joyce 的借用意图。
- 必要修复建议：把学艺之城与携走之物分开写；补神话具体出处。对应爱尔兰四省与全书老者仍须单列为本项目解释。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-16 [P1]
- ID／页与所给坐标：`fw-ii1-239-01`；242页；所给239.01–242.36；精确行号未重核。
- 原文短锚：`spawife / ii1-cooley-couley-manna`。
- 当前中文：正文「占卜娇妻」；注「spawife 指温泉占卜妇」。
- 类别：词义／无据词源事实。
- 问题／依据：父任务实读 DSL spae 条目 I v.1 Combs(ix)：spae-wife=a female fortune-teller，历史引例含 spaewife。注释将 spa 拆为温泉，额外添加场所义；原文没有温泉语境，所引 joyce-fp 也不支持此词典释义。
- 必要修复建议：删「温泉」，写女占卜者；若另提 spa 谐音，只能另列有据读法，不能混入基本释义。
- disposition_required: fix。
- blocks_integration: true。

### R-II1-17 [P1]
- ID／页与所给坐标：`多段；具体注ID见逐注登记`；219–259页；精确行号未重核；精确行号未重核。
- 原文短锚：`外部事实均只列 source_ids: [joyce-fp]`。
- 当前中文：例如「St. Alto 公元八世纪定居巴伐利亚之爱尔兰隐修圣徒」「对应……温德姆·路易斯《时间与西方人》」「Höllenfeuerstein，燧石或硫磺石」。
- 类别：出处／证据分层。
- 问题／依据：60注均标 proposal 并只引原著见证。可见词形与本项目阅读可据原著提出；圣徒传记、神话人物、德语词典义、思想史归属、具名前作章目却是可核事实，不能因整注标 proposal 而免交出处。三例当前皆未有实际支持它们的来源；不据此断言它们全部为假。
- 必要修复建议：按逐注登记补定点来源，或删／存疑具体外部事实。解释与事实分句，列清哪项来源支持哪句；不必为纯粹文本联想强加学术署名。
- disposition_required: qualify。
- blocks_integration: true。

## 漏译与无据增补清单
- 本轮未确认整句或整段完全缺译；不按中英篇幅推定漏译。已确认的局部损失是R-II1-04的淹没动作、R-II1-06的six与分组、R-II1-07的A–Z顺序、R-II1-08的亲属链重复、R-II1-11的32与ante／post对照、R-II1-13的hour时间关系、R-II1-14的murder层。R-II1-09的thou人称层可通过注释补偿。
- 无据增补／误定：R-II1-01十二少女，R-II1-03里约热内卢，R-II1-05汝之所属，R-II1-07逐项确定色号，R-II1-12女地质学家。它们不是普通中文润色。
- 工作段接缝明确重复见R-II1-18。另已连读219／223段的 `Sammy, call / on`，不在未定其词形与声音层时另报剧情错误。

### R-II1-18 [P2] 跨工作段重译同一位置
- ID／页与所给坐标：`fw-ii1-247-01`（247.01–250.36）与 `fw-ii1-251-01`（251.01–254.36）；250／251页接缝；精确行号未重核。
- 原文短锚：`Will any dubble dabble / on the bay?`。
- 当前中文：前段末「可有人愿在都柏林湾涉水双倍对赌」，后段首「在都柏林湾？」。
- 类别／问题：正文重复；英文只有一次 on the bay，中文因分段两次安插同一位置词。Dublin也由译者补出，并非bay的字面地名。
- 必要修复建议：两段联动，删去一处重复。若保留都柏林地名，另说明本项目的语境选择。
- disposition_required: fix；blocks_integration: false。此处可随邻段修订一并处理，不独自阻断全章。

## 60注逐条登记
以下全部逐字读取。能从当前原文辨认的声形或结构可以保留proposal；「未核」意指没有实际外部见证，不暗指事实已经证伪。R-II1-17只要求处理外部事实，不强迫把每条文学联想查成定论。
- `ii1-feenichts-playhouse`：可留文本联想；Phoenix戏院与德语gar nichts两项外部／拆词事实未核，不得合称已证词源。
- `ii1-genesius-archimimus`：圣人职司、罗马archimimus丧礼职责均需独立来源；本轮未核。
- `ii1-four-coroners-cities`：须改带城断言，见R-II1-15；省份／老者对应仍是解释。
- `ii1-soundscript-polyglot`：可据字串辨Celt、Hellene、Teuton等；Zend规范称谓未外核。
- `ii1-mime-title-trio`：标题可核；人物身份及二十八同伴未由本段坐实，且与正文十二冲突，见R-II1-01。
- `ii1-chuffy-nangel-sword`：nangel／soard／light与天使剑光有文本支持；明确米迦勒、谢姆及跌落凡间须存解释限度。
- `ii1-rainbow-colors-roll`：七项清单可核；内衣、天芥菜紫确切谜底属解释，未亲读研究来源。
- `ii1-holytroopers-isot`：声形联想可留；is it given you的具体重构未外核，不当词源事实。
- `ii1-guess-monbreamstone`：moon／brimstone属可见联想；「褐红宝石」及确切黄色未给证据。
- `ii1-guess-hellfeuersteyn`：德语Höllenfeuerstein及其「燧石或硫磺石」义未核；须词典支持或删断言。
- `ii1-guess-coral-pearl`：Van Diemen地名史未外核；粉红橙色不是原句已定答案。
- `ii1-raynbow-cadenza`：R-A-Y-N-B-O-W链在原文可见；把O/W固定为靛青／紫需说明补偿，非词形直接释义。
- `ii1-wiles-of-winsure`：可作温莎妇人联想；未亲核莎剧文本／具名研究。
- `ii1-epistol-hibruws`：Epistle to Hebrews声形可见；Hibernians与作者身份属解释。
- `ii1-ulysses-parody-titles`：各题串已逐项读；逐一配前作十二章及Ukalepe=Telemachus等未核前作／研究，不作已证目录。
- `ii1-four-provinces-composite`：可辨四省缀形；「乃至天下苍生」为解释，地名拼写未外核。
- `ii1-sindbook-peoples`：sin-book可见；Sindbad、天主教祈祷书、所指即本书三层未外核，应逐层存疑。
- `ii1-castle-throwen-baroque`：树石词形可见；Hamlet、Howth、Babel、Vico四层没有各自证据，不合并为已证典故。
- `ii1-rattle-juniverse`：少年／宇宙／摇铃联想可留；指定谢姆意识萌发属解释。
- `ii1-joshua-croesus`：人名声形清楚；旧约关系、吕底亚身份应补事实来源。
- `ii1-jove-chronides`：神谱与Summ的推演须分开；本轮未核神话来源。
- `ii1-contrite-attrition`：神学两种痛悔的定义未外核；不得凭原著链接称定义已核。
- `ii1-adelphus-brother`：希腊语形式、拉丁化说法、戏院关联未外核；可留兄弟联想。
- `ii1-hopops-goholden`：叠音与金光可见；戴胜鸟、hopes是可保留的候选，不能排尽其他语音层。
- `ii1-salat-nabis`：salat／Nabi／Fatiha词义与宗教事实须独立来源；光明神明=肖夫属解释。
- `ii1-holiodrops-heliotrope`：heliotrope／holy／drops联想可留，不据此坐实「神秘汁液」。
- `ii1-xanthos-thrice`：希腊语词义与阿喀琉斯神马传说未外核；原文可见三次呼喊。
- `ii1-gizzygazelle-bimboowood`：gazelle联想可见；「幽邃童话树林」属于补景，且跨段Tark’s未分析；不当定景。
- `ii1-teomeo-daurdour`：断为盖尔语叹词未给原词或词典；降uncertain或只说明听感。
- `ii1-wych-elm-ranelagh`：Manelagh改接Ranelagh、树种与ALP化身各需依据；未亲核地名／研究。
- `ii1-vania-ecclesiastes`：与Vanitas串语联想明显；拉丁原句与俄语名事实未亲核。
- `ii1-cooley-couley-manna`：spawife释义有明确待改事实，见R-II1-16；Cooley牛争与Man岛关系另需来源。
- `ii1-tarks-bimboowood`：bamboo／bimbo可作proposal；「承接第四段」不准确：按冻结JSON为第五段末承第六段，勿把工作段号当书内结构。
- `ii1-brood-blackmail-allbigenesis`：blackmail及创世纪／阿尔比声形可读；阿尔比派教义背景未核，写作反抗属解释。
- `ii1-master-of-snakes`：伊甸、阿波菲斯、帕特里克三条典故均未外核，不能一串并证。
- `ii1-wintermantle-pointefox`：fox与冬披风可见；「都柏林红狐狸地名」未给具体地名或来源，不可当已证。
- `ii1-ani-mama-bustles`：Ani Mama／ALP可作解释；Anu神话事实与连接未核。
- `ii1-zoravarn-lhorde`：lord／governor-general联想可见；tsar与波斯统帅链无词形拆解或词典，待补证。
- `ii1-durant-coverture`：法律术语与妻子财产权范围未外核；不要把时代与法域未分的概括升为完整法律结论。
- `ii1-maccumhal-funeral`：foots确可支持付账层；Hetman、MacCumhal身份事实未外核。
- `ii1-jeremy-chastenot-coulter`：Jeremy、coulter、chastenot可按词形推演；「指代谢姆」仍是身份解释。
- `ii1-danger-solitude-pause`：断句本身可核；「点明少女……宿命」超过句面，保留为proposal即可，不据此重写剧情。
- `ii1-timekiller-spacemaker`：时间／空间对举可核；Wyndham Lewis书名与确切关联须读具体来源。
- `ii1-elmstree-to-stene`：tree／stone声形可留；ALP／HCE映射需语境，「最核心」删虚泛排行。
- `ii1-holy-santalto`：St. Alto年代、国籍、居地与alto santo词形均未外核；此注不可仅凭Joyce正文放行事实。
- `ii1-subliminal-personality`：潜意识／人格词面可核；Freud、Myers与人格分裂概念的思想史归属须资料，不笼统并列。
- `ii1-piebold-nig`：piebald nag联想可留；「孤注一掷最后一搏」为场景解释，勿写确定心理。
- `ii1-dubble-dabble-bay`：double／dabble声形可留，末接on the bay已连读；中文勿在接缝重复两次都柏林湾。
- `ii1-attila-goths-scourge`：Attila／Hun／God-scourge声形明显；五世纪与上帝之鞭称号未亲核史源。
- `ii1-apophotorejected-thrust`：Thrust from light与apo／photo可对读；希腊词根须词典，不据此添加神坛。
- `ii1-jocubus-nic-jay`：Jacob／Nick可作声形候选；直接等同肖恩／谢姆、只取鸟雀游戏不足以穷尽赌博语境，待补说明。
- `ii1-foul-deed-thoughts`：恶念／imagination词形可核；Imogen人名联想未给作品关系，留proposal。
- `ii1-impluvium-visitation`：impluvium建筑释义未外核；「灾祸搜检」不宜一并写成词义。
- `ii1-herblord-gillyflowrets`：花名词义未外核；肖夫身份未定，见R-II1-10。
- `ii1-thunderword-seven-lukkedoeren`：实算词目100个ASCII字母；「第七」未通查另六个雷词；丹麦语短语未亲核词典。
- `ii1-come-indoor-scoffynosey`：归家责斥可据原文；「市井俗语」若指已有固定俗语，缺词典／用例，应改本句场景说明。
- `ii1-play-schouwburgst-curtain`：终场收幕可据正文；莎剧具体致辞与荷兰语剧院义未亲核，不说定本典故已证。
- `ii1-loud-hear-us-litany`：英文字串Lord／Loud联想清楚；中文引文第二句写「基督，垂听」而括号英文仍为Lord，内部不符；须核祷文再引。
- `ii1-tree-stone-vico-formula`：六组树石介词层叠已核；「全书最著名」「维柯终局」「永恒死寂」均非此句可证，且与前注循环说未协调，宜删排行并存解释限度。
- `ii1-ha-he-hi-ho-hu-mummum`：a-e-i-o-u与合唇声可核；母亲／mime／沉寂为proposal，不当唯一含义。

## 完成声明与结论
- 当前版本：**needs_revision**。十段和60注均完成本轮文本语义审查；外部证据与版本校勘未完成。
- `coverage: complete`：内部英文拼接支持已录入整章的范围判断；本报告不据译义错误径自否定录入覆盖。章级 coverage_review 所说「逐段英中对读并补全译文与注释」不能转写成逐句无漏或译注可放行。上述动作、数字、指代和注释事实仍须修。
- 十段 status 均为 draft，reviewers 均为空；这一点与AI初译身份相符。本报告不授权改成 reviewed，也不填写人工署名。
- 阻断项：R-II1-01–05、07、11、13–17。先修正文硬错、删无据事实或补证；不必整章重译。R-II1-06、08、18宜修，但不单凭数字字面或局部重复阻断；R-II1-09、10、12保留为可选择／可存疑项，不因学术分歧无限延长审查。
- 中文整体多用「之」「乃」「盖因」「我等」「汝」及堆叠定语，常把原文轻快戏谑写成古奥说明。本轮不按偏好另立几十条风格缺陷。定点修订时删空架子、缩句，保留Joyce刻意重复；不得以顺口为由再删动作或归并人物。
- 报告适用范围仅限上述SHA。输入一旦改动，整合者须记录逐项处置，并将相关句、相邻接缝和受影响注释交复核。
