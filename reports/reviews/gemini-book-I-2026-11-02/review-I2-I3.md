# I.2–I.3 冻结新稿独立审校

## 输入

- role: ai_review。
- executor: OpenAI Codex，I.2–I.3 独立审校子任务；不是人工审校。
- date: 2026-11-02。
- workpack: 本轮未另配标准工作包；父任务指定冻结目录 `/private/tmp/fw-book-I-intake-20261102/`，以章文件与下列指纹绑定范围。
- revision_round: 本轮为新冻结稿验收，不据文件名推断旧稿经历几轮修订；旧报告仅供核销问题。
- source_id: joyce-fp；Faded Page 转录的 Viking 1958 年第八印本。没有亲查1939年初版扫描。
- draft I.2: `/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-2.json`；sha256: `a22bcb0889f6ed9303193f3ca899279499ad45006a0005ff52da13a9034c639d`。
- full-source I.2: `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-2.json`；文件 sha256: `1084d548c48dac960ab1dd1094c533c05b6cfb54ec2ac1fcee204f9c378611a5`；`source_text.html` UTF-8 sha256: `733fc0cd635028ed14f808bc1d802117daa46730751fadf4d5a7ff01e1ec83fc`。
- draft I.3: `/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-3.json`；sha256: `dc7e21f84d486816bccefacd099fdbbe3753fec10bbd39abbe76ef4610e27372`。
- full-source I.3: `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-3.json`；文件 sha256: `41f80d57fea0a0cbe03ac272592ad5b49fa4083849e07228bbce857ccab05d2a`；`source_text.html` UTF-8 sha256: `be38fe06f681a9e5922606e5526d7af59735a19ea4e7f54c9a4e549b3984f8ac`。

## 结论

- 当前版本：**needs_revision**。
- **blocks_integration: true**：I.3 的 R-I3-NEW-01 是新增注释中的硬事实错误。改掉这一处，再核新稿差异，可定点收口；不需要重译两章。
- I.2 已核文字范围未见须阻断合入的漏误。I.3 旧报告所列成片节译、人物结局丢失、错词生注、四连否定消失等问题，在本次冻结稿中均已补正。本轮没有为了措辞偏好重开这些问题。
- 这份结论仅绑定上述输入。音乐图像、精确行号及外部词源尚有下述限度；不能将本报告转写成「人工已审」或「全卷毫无问题」。

## 范围与实际查阅

已实际逐段通读 I.2 全10段、I.3 全12段的 `original` 与 `translation`，并读完 I.2 全57注、I.3 全58注。逐句核主要动作、主客、否定、时间限制、引语归属、名单和长括号，不以字数或 lemma 子串命中充当语义验收。

另将两章全部 `original` 与全本 `source_text.html` 展平文本作逐差分核对，再人工分辨页码标记、行末断字、文字异文与图形。I.3 除页界与行末断字合并外，未见实词差异。I.2 余下差异为行末断字、`outs ide/outside` 分字、倒转 E 图形及乐谱处文字排法。本轮未据此静默改动原文。

实际查阅：

- Downloads 项目 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md`、`docs/SOURCES.md`、`docs/MANUSCRIPT_FORMAT.md`。
- `.ai/skills/review-translation/SKILL.md` 及 `references/review-protocol.md`。
- `.ai/skills/joyce-research/SKILL.md`、`references/evidence-workpack.md` 与 `references/reproducible-investigation.md`；仅为定点核注，不作三语学术综述。
- 上列冻结章稿与全本 `source_text`；旧 `I-2-I-3.semantic.r0.md`（工具输出有截断，旧问题仅作索引，没有将截断处当成已读全文）、`I-3.primary-collation.json` 对应词形差异。
- 皇家造币厂半克朗说明页面，实际打开正文第7行，读取面值。`read_state: passage_read`；不是依据搜索标题作结论。
- 爱尔兰中央银行 Old Irish Coins 页，实际打开正文第390–404行，核旧币制与竖琴图案背景；该页没有为本稿 handharp 语源提供依据。

未核：

- 未重新获取Faded Page全文；本轮按父任务指定的本地全本HTML转录比对。未亲查1958印本或1939初版影像，未证明每段所标精确行号。
- 未看第44页谱面影像，未核四小节、旋律、音高与谱面呈现。I.2 新稿已经明说只收文字提示与曲名、不渲染谱面；父任务须另验这一覆盖处理，不能借本报告确认乐谱无缺。注 `i2-thunderword-two` 中「1939年版」与「四小节」也未获本轮图像核实。
- 本轮全部注释均作原文锚句、主张边界及内部语义检查；未逐条重新打开词典、历史档案、歌曲原谱、法条或具名研究。注释标 `proposal` 可保留有语境支点的解释分歧，不表示其中外部事实已全部核准。
- 未对照中、日译本原页。曾尝试打开1885法案第11条的英、爱官方网址，两处均未成功；没有据失败断言法条内容。

## 问题

### R-I3-NEW-01 / fw-i3-065-34 / 065.34–067.27

- 词目／字段：`handharp`；注释 `n-i3-66-coffin-handharp`。
- 类别：注释硬事实错误、无据跨词关联。
- 原句：`The coffin, a triumph of the illusionist's art, at first blench naturally taken for a handharp`。
- 当前译句：「那具棺材堪称幻术师技艺的杰作，乍看之下自然让人当成了一架手竖琴」。这句正文无需因本条改动。
- 当前注句：「handharp，兼涉爱尔兰十先令硬币俗称 half-a-crown / harp」。
- 问题：half-a-crown 是二先令六便士，绝非十先令。原句只支持手竖琴词面；所列 `joyce-fp` 并不支持这里补出的具体面值及俗称链。整注标 `proposal` 不能把已错的面值留作可成立解释。
- 依据／evidence：[皇家造币厂半克朗页面](https://production.royalmint.com/shop/monarch/king-george-vi/The-Making-of-Modern-Britain-George-VI-Half-crown/) 第7行明列面值为 two shillings and sixpence；本轮实际打开正文。该材料只核币值，不证明 Joyce 在 `handharp` 中暗藏哪种硬币。
- interpretation：手竖琴、棺材与后接雅巴尔／犹巴尔／土巴该隐的词形链，可以继续保留为项目解释。硬币联想目前没有可定位支持。
- translation_impact／建议：直接删去「兼涉爱尔兰十先令硬币俗称 half-a-crown / harp」这一括语即可。若要保留硬币联想，另补准确币名、面值与可定位的词义证据；不要只把十改成二点五便称已证实全部语源链。
- disposition_required: fix。
- blocks_integration: true；这是公开译注的事实错误，修正范围只限该注，不要求扩大修订。

## 旧问题定点核销

以下均依据本次实际读到的原译对应，不复用旧稿的通过标签。

### I.2

- `fw-i2-030-01`：`humour which William the Conk ... had inherited ... from his greataunt Sophy` 已明确译为幽默连同白发、短指从母系太姑母传来；没有倒置继承对象。谱系注亦已说明叙述者排除旧说。
- `fw-i2-031-33`：饥瘦散工称「好汉弗莱公爵」、老友称「钦伯斯」，关系分开；无据施粥动作已删。
- `fw-i2-033-14`：看守饮酒与提出指控、两女证词分歧、减轻情节均有对应；注已不再坐实醉酒窥视或三国角色。
- `fw-i2-034-30`：姜条混淆长括号、酸盐甜苦清单、骨肌血肉生机清单、肘弯夹手套、脱帽与 `any hygienic day to this hour` 均有对应。
- `fw-i2-036-35`：Arvanda 应承及情郎告别括语已补。
- `fw-i2-038-09`：食物禁语、布丁誓语、Mère Aloyse／Jesuphine、握手效忠、两鼻之差、第三名 Drummer Coxon 均已译出；赛史注已声明小说戏拟，不当真实赛报。
- `fw-i2-039-28`：十八月求医、三院路线与失败，酒肆名录、Lisa O'Deavis／Roche Mongan 同卧关系、队尾索钱原话均已补回。
- `fw-i2-042-17`：群像、传单、命名、呼应、雷词后的 `Ardite, arditi!`、Music cue 及曲名均有文字对应；谱面仍属未核范围。
- `fw-i2-045-01`：歌谣各节、副歌及重唱次序有对应；司法注已保留未来式与歌中咒骂性质。
- `fw-i2-046-01`：`caught his death of fusiliers` 现译保留要命风寒与枪兵的撞合；六年刑期仍在副歌起哄层，没有改成正式已决裁判；末尾复活否定在。

### I.3

- `fw-i3-048-01`：Osti-Fosti 结局未明、A'Hara 阵亡、Paul Horan 入院、Sordid Sam 遭床伴脚踢而死、Langley 无踪消失、神职者与讲坛关系，均已逐项译出。旧稿凭空插入的历史串场已不见。
- `fw-i3-050-33`：三个逃学童请求复述、空酒瓶射击、重装武器与怀表、世界语三句、服饰清单、眼睛要求轮替、击倒德埃斯特的手，均有对应；没有把汉弗莱写作决斗死者。
- `fw-i3-053-07`：原问现为利亚尔币价码；多语交谈逐轮保留，举帽、信誉誓言与邀人仿效动作均在。旧金表求售、破产和白嘴鸦剧情已删。
- `fw-i3-055-03`：列车复述、旅人群像、服饰与烟酒食物招牌、形式因追问、四地应答均已译出，不再以主题梗概替代。
- `fw-i3-057-16`：三兵、女伶、昆虫心理学家、七教堂清道夫、洗车的劳里均有话语或动作对应；Ginger Jane 不再凭空变为隔街女证人。
- `fw-i3-059-27`：各组市民证词、17岁传道女、Sylvia 的伟大／悲剧问话与惩罚说、水兵及二女对话均已补齐；没有旧伪引文「她落下一滴泪」剧情。
- `fw-i3-061-28`：开头疑问、流亡再婚、原罪转嫁、蒙面袭击、`not ... but ...` 来历排除、四句 `No such ...` 否定以及末尾城门被捕疑问均在。不可再沿旧报写作四连否定仍漏。
- `fw-i3-063-20`：醉汉自辩、Behan 证词与声响差别、降雨、火枪手转场及两女亲昵整段唱词均在；旧假友人词形、Chepgone 脸形剧情已不见。
- `fw-i3-065-34`：连环信封、Edenberry、手竖琴与棺材、证人踢门争议均有译文；新出现的硬币注误见 R-I3-NEW-01。
- `fw-i3-067-28`：服石炭酸属于正文已有动作；旧 `fw-i3-067-28-n02` 已删除，现注明确撤回罗拉·蒙特斯定案与「普遍轻生方式」说。不能因正文仍译石炭酸，误判伪注尚存。
- `fw-i3-069-30`：来客三层威胁、十一点半至两点时段、温室内聆听与辱骂名单逐项有对应；`Deposed, but` 保留跨段句法。
- `fw-i3-072-17`：承接 `but anarchistically`，未顶嘴、可拨电话、投石后收手离去、围城收场与石冢苏醒、末尾短句均有对应。未再将「无人」与独眼巨人主客倒置。

旧词形复核：`Eyrawyggla`、`Bucklovitch`、`Calomnequiller's`、`malpractices`、`yearschaums`、`Curchies`、`latitudinous baver`、`Maeromor Mournomates`、`fireleaved`、`propenomen is`、`Sevenchurches`、`Edenberry`、`carcasses` 均与指定全本HTML对应上下文相合。此处列词只是索引；本轮已读取各处句群与中文，未用命中名单代替通读。

## 每段 original_sha256

以下均按冻结稿 `original` 原字串 UTF-8 计算，不附加换行。

- `fw-i2-030-01` / `030.01–031.32`：`dab89a84c1b6e4090bbb42c4eb0a45e83ec6d09c73c364915e79114dea0ac72e`。
- `fw-i2-031-33` / `031.33–033.13`：`49c8345f77aeb9f2d858491eb9760f5e564cb8c86b6c9464f9c4d3526455e3c7`。
- `fw-i2-033-14` / `033.14–034.29`：`ca93795542d76b7cbf711b482dce3c138c922562fda1b58a8ae155391ccfc319`。
- `fw-i2-034-30` / `034.30–036.34`：`1da02f74a720c05f6bc8b7853ddd307c2dec16e4e607a281db3ef4a3ef46ab39`。
- `fw-i2-036-35` / `036.35–038.08`：`455d0bea70483958cbe3749bd4e6eea6f1aa67a5d089290f1862666ffe54f130`。
- `fw-i2-038-09` / `038.09–039.27`：`3b4a5824506491f89b9bbc03e0265262aa98015e7e4fb07bcefec780fd585231`。
- `fw-i2-039-28` / `039.28–042.16`：`1389cacc9fce601bda1da4bd48386e71191c596ae04f09d150281c5126c654a7`。
- `fw-i2-042-17` / `042.17–044.24`：`39a930257f65af0f178b808484174fca5808d35355069e11aa0eb429323c8bf6`。
- `fw-i2-045-01` / `045.01–045.30`：`4034ed67c172ac9e0167f9cbb5fa53359471e9e48ba441a1ed7f116f7ee449ba`。
- `fw-i2-046-01` / `046.01–047.29`：`48dd1e1da90978c742fceabd7be219a07d89194347d45129a112f57ee854e121`。
- `fw-i3-048-01` / `048.01–050.32`：`16034641c403b9fc4952ea25a5f08eff3185efebb9f85adc4b2c24e68a48963e`。
- `fw-i3-050-33` / `050.33–053.06`：`cb2c91cd7cfb7e7fda55a2ee276adc17a6d8e9e42d3559c24a8254dc606b6fef`。
- `fw-i3-053-07` / `053.07–055.02`：`b1789c2424c26f5735e5e9e3d15afc558c8e56beac2717f32ade7b4b73995486`。
- `fw-i3-055-03` / `055.03–057.15`：`98a0279e34046e774f6221fb5a08ba753f86e6b8beedc8db027e5a4d89078cfa`。
- `fw-i3-057-16` / `057.16–059.26`：`0fbd8e9f1375166f9c963c16bd2e4f175ecd3c20378dc7978a14bef3624be6a9`。
- `fw-i3-059-27` / `059.27–061.27`：`d9949f8f8e4dbf8d323b581434e1a0556c242998019e7db0d78f7954c1cecfdb`。
- `fw-i3-061-28` / `061.28–063.19`：`ff748809601bd93627cac39a9aa25d4e35639a32ef6248d55a085bfcbffe156a`。
- `fw-i3-063-20` / `063.20–065.33`：`203eb50e6afc9b44c312d672d53376a6860f39ef1a586f55e791101e64432a9e`。
- `fw-i3-065-34` / `065.34–067.27`：`bde84de05d2a408d0a9b7997b14f7c92c18e48592bf5fcb6593a75368d5d450d`。
- `fw-i3-067-28` / `067.28–069.29`：`7ec001a0cc1f234eacf2af43139572ca2dff4f32d1b739946686a0cf84df4e84`。
- `fw-i3-069-30` / `069.30–072.16`：`a016176fe659772a551f0e83e4725afbaed74894658212d42937fb28a553ed20`。
- `fw-i3-072-17` / `072.17–074.19`：`c57d4a93bf4ca0e7fcc465d673fab738f56da089d69eb202124239fba1eea929`。

## 交回

先处理 R-I3-NEW-01，交新稿SHA与差异。未改文字可沿用本报告实际核过的范围；只需复核改注及其上下文。第44页乐谱、精确行号与来源版本断言交父任务单列验收。本执行者只写本报告，没有改章稿、断点、来源，也没有推送。
