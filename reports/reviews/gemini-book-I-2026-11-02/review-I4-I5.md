# Gemini 新稿 I.4／I.5 独立审校

## 输入

- role: `ai_review`；executor: Codex 子代理 `audit_i4_i5_latest`。不是人工审校；未改公共 `reviewers`。
- 当前两章段落均为 `revised`，人工审校署名为空。
- 冻结目录：`/private/tmp/fw-book-I-intake-20261102/`。文件指纹与该目录 `manifest.json` 相符。
- workpack：未另收初译工作包；以本次分配、冻结清单和完整文字见证界定范围。
- revision_round：未从分配材料确认统一轮次，不自行将“integrated”解释成某一轮。旧 `I-4-I-5.semantic.r0.md` 只用于追溯问题；本报告重新绑定下列输入。
- source_id：`joyce-fp`；见证为 Faded Page 转录的 Viking Press 1958 年第八印本，不称1939年初版逐字校勘。
- I.4：`/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-4.json`；075.01–103.11；SHA256 `203fba375d3cee585ed72398c32e51f316df9a5f77022b5bd39ffb333fea2940`。
- I.5：`/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-5.json`；104.01–125.23；SHA256 `a25499f274e3991ca822f4066202a43115a7bafee86717bf19eb582f37203e92`。
- 冻结清单 `manifest.json`：SHA256 `cc0049b9315b07bb1f2905c2a5903abef845cc653ce7c466e87a610c7bef13da`。
- 冻结来源表 `sources/catalog.json`：SHA256 `57025779cf622a30911fab51363b463cf87d3e796021f2415ec10f753b3030a5`。
- I.4完整见证：`/private/tmp/fw-full-source-20261101/manuscript/chapters/I-4.json`；文件 SHA256 `2f0e5e7b682aca2f95bbd5182ad234695ab0e586354006c1b9eae642247df144`；其 `source_text.html` 原字串 SHA256 `e32cd778990c3b6a75cc56379b3fdb8e6c7b0b58d5c820c1f39fca6754f9dfff`。
- I.5完整见证：`/private/tmp/fw-full-source-20261101/manuscript/chapters/I-5.json`；文件 SHA256 `a92ed4db35aded329d1e6cae506fd31cbc6dfe4130665f5de26707be027f7b64`；其 `source_text.html` 原字串 SHA256 `291440b17f692a5028ce4ccf9eb92b1557acb585e81b557f774cf3af1c2e20b0`。
- 原始工作包 `/private/tmp/fw-full-source-with-ref.zip`：SHA256 `42612decf1404c978d950f1b0cc4c5b9bf87c2d6428cc7fba1f0d2ce83ce3be5`。本轮查了ZIP清单，未把它解压写入仓库。

## 范围与实际查阅

已读项目 `review-translation/SKILL.md`、`references/review-protocol.md`、`EDITORIAL_GUIDE.md`、`SOURCES.md`、`MANUSCRIPT_FORMAT.md`，以及旧 I.4／I.5语义报告。逐段读完I.4全部12段与I.5全部8段 `original`、`translation`；读完78＋37条注释正文，核词目与所在段原文关系。另读本次冻结交接清单、处置账及覆盖说明；其中“已修完”不代替本次核对。

对完整 `source_text.html` 提取文本，去除页码标记与空白，再与两章按序串起的 `original` 比较。未发现整句缺失；差异限于行末断字连字符、H下标记法及图形转写。该比较只用于定位，放行判断仍来自原译对读。I.5第121页 `returns inhibited, with some half-halted suggestion,` 已在本稿，第二个F位置也已补入。没有沿用旧稿漏句判断。

未核：1939年初版扫描；完整学术注本、词典及中日译本原页；所有外部历史、词源与图像主张。只从本地见证核过文字，不冒称本轮重开了注释所涉外部来源。未目验ZIP内三个相关字形图片，因此不验收其方向、字体与读本渲染。所有注释现标 `proposal`／`uncertain`，合理联想可保留；但分级不能替输入中不存在的词句作证。

## 已解决的旧问题

- I4-R01：077页水雷、TNT、氨罐、缆索、引信箱、衬砌和七塔均已译回；数量另见下列R01b。
- I4-R02／R03：每日七十条鱼、贵妇搬运主语、080页木匠／火祭司与送回木桶等直接话语已回正文。未再出现查拉图斯特拉替代该段。
- I4-R06／R07／R08／R09／R11／R12：十八尊号、一对扁豆的相似关系、臭风信子、A／O与虚点、大亚细亚、sevenscore moons主干错误均已改。A／O标点形态仍为谜面，没有再填“惊雷／谜团”。
- I5-R01至R07的大量删落已补：题名中的无据高崖已撤；孔子、布鲁斯兄弟、蜘蛛、算术马，信封／衣饰比喻，凯文与圣杯、波士顿家书，熔化后仍是马，水印与反复schwrites，石匠与对方、签名论述、政治释读，真实作者到流变文本的论证，Hec／Δ、理想失眠读者与字母学例证，版本缩略号、纸牌、Tunc长括号、732笔、Duff-Muggli／Tung-Toyd的关系均有正文对应。未再以提要顶替这些句群。
- I5-R08：制信、署敬、附言、未饮之杯、狐狸与鹅、后半名单已经恢复；“四维空间”确定断言及“作者身份昭雪”已撤。但补回句群时仍添了原文没有的人名，见R08b。

这些修复是真实改进，不因新增问题而撤销。但它们不能证明当前稿已无实质缺陷。

## 仍须修改

### I4-R01b：十一加三十误成十一至三十

- 位置：`fw-i4-075-01`，077页；`translation`。
- 原句：`up ahoy of eleven and thirty wingrests (circiter)`。
- 译句：“距右舷约十一至三十翼展”。
- 问题：`eleven and thirty`采用倒装数词相加，译稿把41变为11–30区间。`circiter`容许约数，不能把加法改成范围。wingrests的造词可保留歧义，数字关系仍须准确。
- 建议：改为约四十一，并保留度量词的异样；不要求借此重译爆破句群。
- disposition_required: `fix`；blocks_integration: `false`（局部数值，须改但不单凭此项阻断整章）。

### I4-R07b：吸烟答句新增否定条件

- 位置：`fw-i4-088-35`，089页；`translation`。
- 原句：`Askt to whether she minded whither he smuked? Not if he barkst into phlegms.`
- 译句：“曾否问过那位小姐，介不介意他当场吸烟？只要他不咳出血痰，自然无妨。”
- 问题：`Not`回答是否介意；`if`后没有否定。现译把它移入条件句，成为“不咳出……才无妨”。这改变容许条件，还给`phlegms`加了原文未明写的“血”。`barkst into phlegms`可兼顾咳痰与burst into flames声形，不能靠新增“不”来译顺。
- 建议：恢复“不介意；即使／倘若……”的关系，并保留咳痰与燃烧声形可竞争的读法。无需定死唯一双关。
- disposition_required: `fix`；blocks_integration: `true`（否定关系反转）。

### I4-R08b：轰回住所后仍漏主动作

- 位置：`fw-i4-090-34`，093页；`translation`，并关联 `i4-shun-the-punman-drinkbattle`。
- 原句：`biss Drinkbattle's Dingy Dwellings where (for like your true venuson Esau he was dovetimid as the dears at Bottome) he shat in (zoo), like the muddy goalbind who he was (dun), the chassetitties belles conclaiming...`
- 译句：“当场轰回醉战鬼屋；对这些赠错温存的赐予者，他满口嘲弄致谢；而那群丰乳俏女郎则同仇敌忾……”
- 问题：中文从回屋跳到群女谴责，`where ... he shat in (zoo) ... (dun)`整个动作与双关没有对应；Esau、鸽／鹿羞怯、Bottome也随之消失。这不是省去一个可有可无的专名。原文把排泄字面与坐下等声形挤在一起；不能因有多义而略过。
- 建议：补回该动作及其围绕的羞怯比喻、zoo／dun声形，具体择译可另留注释；无须替全段建立确定人物身份。
- disposition_required: `fix`；blocks_integration: `true`（主要动作漏译）。

### I4-R09b：祈使句译成反义

- 位置：`fw-i4-093-22`，095页；`translation`。
- 原句：`How do you do, todo, North Mister? Get into my way!`
- 译句：“你好哇，北地大老爷，近来可好？休要挡我去路！”
- 问题：`Get into my way!`正面命令进入／挡在路中；译稿增添禁止词“休要”。即使认为它戏拟通常的`Get out of my way`，也应保留作者写出的反常方向，而非替作者改回惯用句。
- 建议：恢复进入／迎到路上的命令；典故或反语解释另存候选。
- disposition_required: `fix`；blocks_integration: `true`（动作方向与否定相反）。

### I4-N01：注释仍改写原文事实，proposal不能化解冲突

- `fw-i4-082-30`／`i4-dublin-pub-crawl-four-taverns`：注称“原文依次列出 Old Sot's Hole、……红牛……善妇……亚当夏娃”。本段实际顺序是Ruadh Cow、Good Woman、`Conway's Inn at Blackrock`、Adam and Eve's。Old Sot's Hole不在本段或I.4见证全文；Conway反遭漏列。请按本段更正四站，不以推测分级保留错误目录。
- `fw-i4-084-28`／`i4-tykingfest-rabworc-pedigree-pig`：注称“手持风信子并牵引……猪出庭”；原句在`middlewhite fair in Mudford`后接`ellegedly with a pedigree pig (unlicensed) and a hyacinth`，此处是集市指控，未说牵猪持花出庭。请改回声称赴集市时携带；同时分清控方指控与已定事实。
- `fw-i4-097-28`／`i4-lilypond-whitlock-piece-of-wood`：注把池水定为“仅四尺半”，原句是`very possibly several feel of demifrish water`。没有“四尺半”数值，且删掉`very possibly`。请保留几尺及不确定语气，或补其他明确见证并登记版本差异。
- `fw-i4-086-32`／`i4-filth-of-november-tournay`：注写`Yetstanhavel`，本段及完整见证均为`Yetstoslay`。这不是学说分歧，请更正词形。
- 类别：出处／无据增补／词形。
- disposition_required: `fix`；blocks_integration: `true`（至少前两项把小说场景与原文清单改写成另一事实；可逐注定点修，不需全章重查外部文献）。

### I5-R08b：新添“失落神学的格赖姆斯”，还写入注释

- 位置：`fw-i5-123-30`，124页；`translation`与`i5-four-old-men-jeromesolem-riddle`。
- 原句：`The lettermaking of the explots of Fjorgn Camhelsson when he was in the Kvinnes country with Soldru's men.`
- 译句：“这便是失落神学的格赖姆斯与峡湾卡姆赫尔松当年在女人国同索尔德鲁部众一道时的制信伟业。”
- 注句：“在前文补入格赖姆斯与峡湾卡姆赫尔松（Fjorgn Camhelsson）在女人国……”
- 问题：冻结original与完整1958见证只有Fjorgn Camhelsson；没有额外并列的人物“格赖姆斯”，也没有“失落神学”这项限定。译稿增添一位合作者，注释又把新增内容当作“前文”复述。两处互引不能产生依据。即使“格赖姆斯”来自某种解读，也须给出词形与证据，并保留为候选，不能凭空并列一人。
- 建议：撤去无据人名及限定，重核整句对应；注释同步删除。已补回其他署敬、附言与狐狸／鹅句群，可保留。
- disposition_required: `fix`；blocks_integration: `true`（无据人物及关系）。

### I5-R08c：章末新增话语

- 位置：`fw-i5-123-30`，125.23；`translation`。
- 原句末尾：`... (kak, pfooi, bosh and fiety, much earny, Gus, poteen? Sez you!) Shem the Penman.`
- 译句末尾：“……赚了不少吧，格斯，私酿威士忌？亏你说得出口！）——（等我告诉你！）执笔人谢姆。”
- 问题：前一括号已译出Sez you；后加“（等我告诉你！）”无当前原文依据。它构成新的叙述者发言，改变末尾出场节拍。章末覆盖说明自称“剔除一切无底本依据的增补词句”，与实文冲突。
- 建议：删除新增括号；若另有见证，先列清版本，不静默混入。
- disposition_required: `fix`；blocks_integration: `true`（新发言无据，且处在章末接缝）。

## 保留的合理歧义与未核项

不因偏好要求重译：HCE／ALP人物映射、数词与月相旁义、印度教及基督教意象叠合、首字母历史背景、牛—屋—驼的字母表联想、Tunc图版与吻词、732日数联想、Duff-Muggli伪书目人物音形等。当前候选已统一降级；本轮不将未重开外部资料的一般学说当成阻断理由。注释仅列`joyce-fp`足以支持字面，不等于已证实所有历史词源；日后若升格断言，须逐条补证。

I4-R10那句`Well, even should not ... bring the true truth to light ...`可讨论反问与条件倒装。当前“即便……未能……然而……”有收窄句法之嫌；本轮不据此单独阻断，建议另列异读，不要求为措辞偏好重启全段。中文普遍偏繁，仍见“具备／实质”等赘语与过密“的／们”；在不抹平原文连缀的前提下可收紧。此类润色也不充当阻断理由。

## 逐段核对结论

- I.4 `075-01`：爆破与七塔已补；R01b数值待改。`077-28`：旧频率与主语项已改。`080-20`：祭司及驱赶话语已补。`082-30`：正文主要动作已存，N01酒馆注待改。`084-28`：正文主要指控与动作有对应，N01出庭注待改。`086-32`：十八词与孩童等旧项已改，N01词形待改。`088-35`：R07b。`090-34`：R08b。`093-22`：虚点已改，R09b。`095-27`：围猎等主要序列有对应，条件句异读留待选择。`097-28`：Asia Major与传闻语气旧项已改，N01水深待改。`100-05`：朔望月、彩色名单、租约歌谣、巴比伦章尾主要序列均有对应。
- I.5 `104-01`：逐项题名已读。`107-08`：耐心、孔子与马、否定推论及信封比喻已恢复。`110-22`：家书、马底片与母鸡等已恢复。`113-23`：签名、精神分析、政治释读与语域反问已恢复。`116-36`：作者与流变论证已恢复。`119-10`：字母学、失眠读者与121漏句已恢复，图形未作视觉验收。`121-29`：手稿代号、r牌局、Tunc长括号、花押与伪书目已恢复。`123-30`：主要旧漏段已恢复；R08b、R08c仍须改。

## 结论

当前版本：两章均 `needs_revision`，不能作为“检查没问题”推送。I.4有主要动作遗漏、否定／方向倒置和注释文本冲突；I.5仍有无据人物及章末新发言。先修本文列明的实质项，另交冻结修订稿和逐项处置，再定点复核受影响段落、注释与章末接缝。未改公共章稿、来源表、断点、覆盖状态或生成产物。

本次覆盖全章文本对读，但不证明每个外部典故、词源或图形已核实。两章`coverage_review`中“全部审校问题已订正”“剔除一切无据增补”等绝对声明，应随修订改写，不能用于绕过所列问题。

## original_sha256

按各段 `original` 原字串UTF-8字节计算，不追加换行：

- `fw-i4-075-01`／075.01–077.27：`097abccd736ec6f69f0959197ea8a5b367062ef14ce67524024451be51dce93f`
- `fw-i4-077-28`／077.28–080.19：`d3ccd06f12f63a8ef9523af1d72ef434f596230d9e2cac1882e5ad868fb947d3`
- `fw-i4-080-20`／080.20–082.29：`c61fbcad1cb8ae2e3a55d4271de71f7d6e65a7e645035ad03d663aa1f52aea8d`
- `fw-i4-082-30`／082.30–084.27：`72ed86d1794566853313bd7587886bcc9c44cbca595c6b062141081ba57e0a41`
- `fw-i4-084-28`／084.28–086.31：`c37281c4a640ca25c809d3e24df650fa6db3f64cae165b3478228acfaafb1e71`
- `fw-i4-086-32`／086.32–088.34：`cd52ef31b0c5a66f1c8db937d0e8cf35f6348bf5ebeb3c723108e99eed436f6a`
- `fw-i4-088-35`／088.35–090.33：`5ed7cb95ba493d517807f1e41d0887657066e72b7012001b981787f5b41c8d66`
- `fw-i4-090-34`／090.34–093.21：`c24816b776eb59cb872c36a0e2b8640922afdbea4704fee995fadf195cf3fa9b`
- `fw-i4-093-22`／093.22–095.26：`3c2f098ba3f6553a0207d16ba23ff07083bc88934b2649041c3fd7a48dd371b9`
- `fw-i4-095-27`／095.27–097.27：`99d01320ddb2b7e03dd1413b80196a594ff925e4133a793174920dcf477684c1`
- `fw-i4-097-28`／097.28–100.04：`04b9b3f89a7f6de12c977108c236174a80557d9a2429f7836506253d8ea5f24b`
- `fw-i4-100-05`／100.05–103.11：`ce276a9c7e6c2aea5db24b9c4d74b08e081905cbf5990c7ce72db04f34c76c35`
- `fw-i5-104-01`／104.01–107.07：`06789b4e0b769809dad4ebb444eaee152f22da48cf7f35e59099a8ce0f8af68c`
- `fw-i5-107-08`／107.08–110.21：`2d5696546a582364338bfd801985381278cf59a026ad01a6ce0f493a243bac39`
- `fw-i5-110-22`／110.22–113.22：`dfe0edaffd8d23b44d243a88528a8b8c99c1e31445312a2edd8aa3d6f4dbfab9`
- `fw-i5-113-23`／113.23–116.35：`3eef46dea12283ef5a6ba31bc2602cc86a646860ab625a29c68f31f90188d4d9`
- `fw-i5-116-36`／116.36–119.09：`95bfc33474aacd614ed0a65d8e473b78203ce608e22c5ad3450b6f925273f1b5`
- `fw-i5-119-10`／119.10–121.28：`a0c0e917deee470f28926938dc3886ed4ee7dfeca1a7aed1300b4a59e52ed935`
- `fw-i5-121-29`／121.29–123.29：`9ccf1bf966017faf1ca0d5eaa31bbeaf7f753a84b83fd04e89a7c9d4526d70d5`
- `fw-i5-123-30`／123.30–125.23：`38365c3cc4e8016459b8006957d45c3c0ac77c33940f51f8f06068c683d634ba`
