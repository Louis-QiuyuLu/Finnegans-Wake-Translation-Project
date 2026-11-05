# III.1—III.2 定点修订与复核

- role: self_check（本执行者核冻结稿后亲自修订，再核改处；不冒称人工独立审校）
- executor: Codex AI 子任务 /root/release_book_iii_a
- revision_round: 2（首轮修硬错与漏文，第二轮复核改处、清理注释与数字否定）
- stage: pending_review；本分配范围 ready_to_integrate，须由主整合者验收。
- 未改英文、初译 draft、ID、页行坐标、来源ID、全章source_text、覆盖状态与进度。所有16段均为 revised，reviewers 为空。

## 输入与版本

冻结稿：`reports/reviews/inputs/books-II-IV-20261105/manuscript/chapters/`。本目录的 `*.before.json` 是冻结稿等值快照，另行序列化，故文件SHA不同；已逐对象确认相等。Gemini账只用于定位旧声称，不作通过证明。

### III-1
- 冻结输入 SHA256：`62e971d7991953afdff8ddb0b20279948b829af72fb8561e99cc2138f63cff76`
- 等值快照 SHA256：`66f13193a51ad5433c3aec70e6f3b0a36adf13b0d4e94c3d53cab798ac77b1ce`
- 修订章稿 SHA256：`5b13bb62bbb277b520fd4205b5f93a23295ce841bc8ae2d7deef5068e2eda93f`

### III-2
- 冻结输入 SHA256：`42fb8132a795309cfa791ff79a2d9145cd656e5cc4f76e9ac5a12b891b5f0428`
- 等值快照 SHA256：`05e45463e5a39eb7bed1b6af5669d2b87e7aaa16ae262aec2e42f3ea46406b6e`
- 修订章稿 SHA256：`07ae0ba1733b91b87c9cf576f43b270dc7b5c90708a29a7e907e8534876a3c8b`

## 实际查阅与范围

已读 AGENTS、EDITORIAL_GUIDE、SOURCES、MANUSCRIPT_FORMAT、review-translation 及审校协议、translate-chapter 及角色合同。逐段通读所分配16段完整原文、现译及96条注释。核固定英文、顺序、接缝、人物动作、数字否定、漏译与无据增写；另以独立 source_text 作全文范围比对。III.1三处与III.2五处仅差行末ASCII连字符；III.2另带首部429页标，均未据此改原文。

实际证据是冻结稿与本地完整英文见证 `joyce-fp`，未重开外部辞典、论文、乐谱、档案或图版。因此不声称完成词源／典故外证审查；旧注仅引原著却断定生平、校史、神话体系、节期、复合语源或精确出处，均收窄为可见语境并标 uncertain，明显声形试读留 proposal。96条旧注的精确 page_col_line 未经原刊逐行核对，本轮撤下；段落 locator/range 原样保留。完整注释ID和原文逐段SHA见 verification.json。

## 逐段问题与处置

### R-III1-01 / fw-iii1-403-01 / 403.01–407.36
- 词目／依据：`Hark / Shaun! / Gregory and Lyons`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：删除沙丘、淹溺者、公园、邮袋、松饼、冻颤贫弟等无据剧情；恢复地上爬行滑行小物、柴火与地下嗡声的呼应，四人之后的补锅匠驴子自嘲，以及肖恩本人站在叙述者面前的祝祷。补 handleaf fallen，纠正一百六十来与饮酒句。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III1-02 / fw-iii1-408-01 / 408.01–412.35
- 词目／依据：`exhaust as winded hare / sixty odd ... a week / grocery beans`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：恢复草地歇息、重担、自述职分、发信许可问答、麦克布莱克二人、遗传职分、火山与河流等出路、邮资机与公开信问答、圣职豁免、祷告与念珠、邮局文具遭山羊吞食等缺口。每周六十多纠正每日六十；删除热茶、落锅、跑步悬空、绝未拆信等改造剧情。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III1-03 / fw-iii1-413-01 / 413.01–416.36
- 词目／依据：`Mrs Sanders / Gracehoper / Floh and Luse and Bienie and Vespatilla`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：撤火灾、遗产托管、侯爵夫人、公园与威灵顿喝茶等无据叙事；恢复姐妹、医学女儿、肥胖吃药、遗嘱椅垫及转款对象。蚱蜢寓言恢复四名求偶者与口器／附肢、肌群、追娶埋绑、衣装商店、宙斯虫棺女伴、配方、鼓乐与曲名、科学和艺术问答；删除传统囤粮寓言替代。补其病贫、求宿、啃记录与时空、脑中蟋蟀和发中莱布尼茨。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III1-04 / fw-iii1-417-01 / 417.01–420.36
- 词目／依据：`Ondt / Greek! / Letter ... for Hek`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：恢复蚱蜢走巷、未来再遇的疑问，翁特服饰、食物与四女动作；卢丝纠正莉维亚。复核诗歌全28行；去重复笑句，保留空间与时间收束。补希腊话—罗马身分—闭眼倒读／翻译诸语—脚茧痛—文字批评的整串自夸。信函补最终交给赫克；未把该28行诗认定为已获哲学史佐证。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III1-05 / fw-iii1-421-01 / 421.01–424.36
- 词目／依据：`31 Jun. 13, 12 / slanguage / Well it is partly my own`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：日期不归并为1912年；恢复十倍词语的提问、闻名／犹豫反驳、处罚与禁闭细节、完整寓言追问及帽子蜂房一口、消息渠道、诺尔借贷、草原百合、女子叫嚷与抄写者睡椅、遣辞牙痛等长训辞；撤电车索赔，补想加入道明会；Kingdom of Heaven去无据「邮名簿」。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III1-06 / fw-iii1-425-01 / 425.01–428.27
- 词目／依据：`could use worse / only for / mooherhead`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：去无据五十倍；恢复聪明与书架的原问题、他自夸却不肯费力的转折。撤床头场景与埃林芳华，母亲只按言及母亲理解。原文滚桶、熄灯、送别与祝愿顺序保留。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-01 / fw-iii2-429-01 / 429.01–433.36
- 词目／依据：`twentynine hedge daughters / eight and fifty pedalettes`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：恢复警员抱瓶直睡、29名夜校女儿、58小脚划拍、树下警告与游戏、姑娘围绕嗅闻揉发摸袋、四组宠物、品衣饰与后钩开口、爱万物的长括号。撤路面长靴驻足因果及幽暗苍鹰深潭。训诫末尾保持同下一段相接。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-02 / fw-iii2-434-01 / 434.01–437.36
- 词目／依据：`Whalebones / after ... poetries`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：删除原文没有的公用吸管、柠檬水小厮、剧院松扣补妆三句。保留全段长训诫、画家与画名、饮酒场所、锻炼与房客清单；睡衣／和服不改成东瀛海难。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-03 / fw-iii2-438-01 / 438.01–441.36
- 词目／依据：`marriage slump / prominent married member / Brahaam`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补婚配价目、文明数目、与显赫已婚成员交接、传票与伴游身份。原文始终嵌在假设，未改成既成事实。Brahaam保留叠名，不径改巴兰。书目训辞按原顺序保留。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-04 / fw-iii2-442-01 / 442.01–445.36
- 词目／依据：`balm of Gaylad / Wolf the Ganger / swing for`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补药膏歌声献媚、教堂与婚配摸索、捣脸、宣礼夜喊等威胁；补沃尔夫、逃礼拜堂／旅馆问话、上门、铁路灌木、夺帽、锁鞋、裁吊袜带、主教与合法快感等遗漏整串。swing for纠正为自己可能为袭击上绞架，非把情敌送上绞架。枕上呼吸的是你的名字。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-05 / fw-iii2-446-01 / 446.01–449.36
- 词目／依据：`Abelite union / Burn only / vanity of Vanissy`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补归途苏尔／诺尔／王郡女郡、珍珠、贫民窟与义卖、寄养儿、三卫士、轮班与衬衫、合力工作。Burn only纠正为只烧爱尔兰货，保留煤炭例外。恢复虚荣万物消失、我不急、鸭子、蓝狐与寻得心上人便愿折返的独白。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-06 / fw-iii2-450-01 / 450.01–454.36
- 词目／依据：`off the key / examhoops / Goodbye`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补不走调、麦科马克喉、升降号、荒野有毒植物及鸟巢、考试双科、全部法新投资私酿酒等清单。补完整告别、硬币、行间读信、署名待续与大笑跃喉；金蛋句去倒置为母鸡，原文尾部home-made只留未完成语，接下段hurricanes。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-07 / fw-iii2-455-01 / 455.01–459.36
- 词目／依据：`Hereweareagain Gaieties / Sosy / not sester Maggy`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补后世余兴戏、皇家发火与丑角戏、全空间果壳、家常菜／芥末／本地牡蛎／烫茶与午餐，消除原稿直接跳到道谢的整段遗漏。恢复维生素列词与x/o组合。补镜中同伴、祷珠、玛奇梦话、涂麻疹泥胡、袜靴头发、Sosy／sassy与scorns／schools／ithel／athel，恢复「不是玛吉修女」否定。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-08 / fw-iii2-460-01 / 460.01–464.36
- 词目／依据：`under the libans / Erin go Dry / Mark my use`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补树木、静水反照、匈牙利玛格丽特、远处杰克、鲑鱼、闰年、等候茶饼、圣烛节与别恼等缺口。Erin go Dry纠正为永干，非永不干。补用／雇／抄／骗、威尔士灯、美人鱼火、剃头长描写。克拉达clasp保留握手，不直接化为戒指锁扣。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-09 / fw-iii2-465-01 / 465.01–468.36
- 词目／依据：`three shillings a pullet / p.p. a mimograph`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补给教士价钱、看吻十字架、双唇、耳坠、卷发诗人、尾流苏、土地与骨肉族属等清单；补复写摹本、罗马诸名、福建传教考试、P/F、手势／女人／语法长戏仿。视觉改不信，保留听觉不疑的对举。Tempos fidgets译时间躁动，束缚在迦太基下不抹成自由飞鸟。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

### R-III2-10 / fw-iii2-469-01 / 469.01–473.25
- 词目／依据：`last fireless words / twentyaid add one / nucleus`；完整原文见同ID，UTF-8 SHA见 verification.json。
- 已核范围：本段 original、translation、全部 notes；首尾同相邻段连读。
- 原问题及采用处置：补祝辞、解散、报数、烟、肥皂箱尾声、28加1的姑娘及跃起欢呼／跌落诅咒，接车马原长列。补和平名串尾项。恢复灯向四方赞辞、服务灵魂的光核、尚有12人存活、长年苦忍与等待回归的祈愿，避免原稿把灯直接跳接成历史训诫。
- disposition_required: fix / qualify；上述正文修正已采用。注释撤回无外证的确定断言，另留待核。
- 修改字段：translation、notes、status、reviewers。draft 原样。
- blocks_integration: false（就列明问题，硬错已改；词源解释已降级，不据此重写正文）。

## 结论与未决项

所分配16段已通读，列明的漏误译与无据剧情已修。没有用梗概替换本文；补文保留各清单顺序与括号层次。此稿仍是 AI revised，未获真实人工审校，也不等于词源全解。多语复合词、虫名、声形、曲目与书目谐音仍有中文损失，96条注释已明确查阅限度；外部论证另待研究，不把猜测当事实。未改其他章、sources、进度，不提交或push。

验证：`python3 scripts/project.py check` 通过（17章、177段、1088注，reviewed为0）。两章JSON可解析；初译、英文、ID与坐标逐字段相同；完整英文范围比对通过。全库测试、构建、生成产物与远端验收由主整合者统一执行。本报告仅绑定上列终稿SHA。
