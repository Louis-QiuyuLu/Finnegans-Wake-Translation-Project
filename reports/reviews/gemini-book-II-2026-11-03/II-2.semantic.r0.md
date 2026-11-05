# II.2 语义与译注审校报告 r0

## 输入

- role: ai_review
- executor: OpenAI Codex（实际独立审校代理；非人工审校）
- revision_round: 0
- workpack: 本任务未另配翻译工作包；以冻结稿及同根清单为输入。
- draft: `reports/reviews/inputs/gemini-book-II-2026-11-03/manuscript/chapters/II-2.json`
- draft_sha256: `92b5e3f9103804655e85163fe726a024b079d8914e72aed008102bd234ca47b4`
- manifest: `reports/reviews/inputs/gemini-book-II-2026-11-03/manifest.json`
- manifest_sha256: `cf897e49c4f4de390d9579eba0820f308fad0a387c08e94feb1bd43709c4d630`
- sources: 同冻结根 `sources/catalog.json`；sha256: `707e0358bd04a1b30f4fe6f213eb6f49f9e993cd0e242b3c5c809cb0c432881d`
- glossary: 同冻结根 `glossary/terms.json`；sha256: `46e5486f2e52f7aabd7758c1aa202fe7d3df71c81ed3aa950910be03bb095f96`
- source_id: `joyce-fp`。来源表登记 Faded Page 转录本，Viking Press 1958 年第八印本；不能改称1939年初版逐字影印。
- source_text.html 的实际 UTF-8 SHA256 与声明相符：`74b0327cfa2a472d3ce9c63277d62d28121aed6588c77bbf4b40576e1e6acc13`。
- 范围：`fw-ii2-260-01` 至 `fw-ii2-303-01`，稿内标 `260.01–308.55`。本报告只用页码与唯一锚句定位。未核印本逐行，不认可这些行号已经复算；某些页行数超过常用正文行数，更须另核旁注、脚注计行规则。

## 范围与查阅

已分六批读完十一段 `original`、`translation` 和全部六十六条 `notes`，并回看 `source_text.html` 的页码锚点、正文标签、`aside.sl`、`aside.sr`、`div.footnote` 及相关图像标签。没有凭字数判断漏译。各问题均给出英文锚句及当前中文或缺失接缝。

已读 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md`、`docs/SOURCES.md`、`docs/MANUSCRIPT_FORMAT.md`、`.ai/skills/review-translation/SKILL.md` 及 `references/review-protocol.md`。已读冻结来源表中 `joyce-fp` 的来源性质与冻结术语表；六十六条译注均只列 `joyce-fp`。

已实际看过仓库六幅小图：`Fbackward.jpg`、`Fforward.jpg`、`musicalbar.jpg`、`geometricdiagram.jpg`、`doodlesfamily.jpg`、`thumb_nose_forks.jpg`。几何图可见相交双圆、顶端 π、底端 P、左右 Aα 与 λL 等标记。图资产位于 `manuscript/source-assets/`；不是本任务另获冻结的印本扫描。这里只核资产内容与相邻文字，不据此宣称中文读本或 EPUB 已正确插图，也不宣称重现原刊材质与逐行位置。

未核：原刊逐页影像；已生成中文网页／EPUB实际显示；所有外部词源词典、学术文献、人物传记、歌曲或历史事件的原始出处。父任务负责外部底本与补证；其统一证据另交整合者。本报告不把父任务打开网页当作本人独立查阅。未重审 `draft` 备份与音频，不改公共章稿、状态、断点或来源。

`proposal` 可以标识解释，却不能免除语言、语系、人物身份、作品出处与印刷史等硬事实举证。以下不因全部注释只列原著而一概否定解释；只在主张越过所列证据时指出缺口。

## 问题

### R-II2-01：正文、左右旁注与原作脚注混层

- 位置／字段：全章 `translation`，例见 p264、p293、p297、p303、p306–307；`source_text.html` 可分别核 `p_II2`、`aside.sl`、`aside.sr`、`footnote`。
- 类别／优先级：结构、无据连接；P1。
- 原文／当前中文：p264 `Fossilisation, all branches.` 位于正文，现写「页缘：化石成石，万千枝脉」；p293 左旁注 `The Vortex. Spring of Sprung Verse. The Vertex.` 现接在「普遍之」之后，成「普遍之旋涡。断奏诗篇之源泉。顶点。虚浮贵族神秘未尽之言」；p306–307 左旁人名原与各道作文题平行，现先挪成两大串「页缘」名单，再译作文题，读者无法复原对应。
- 依据：冻结 HTML 的标签直接区分这些层；原文串接顺序不是单一叙述句法。当前稿有时写「页缘」，有时不写，还把脚注号接到下一段正文。版面层级与发言位置已发生变化。
- 建议：按页明确正文、左旁注、右旁注、原作脚注，并保留各自锚点。依可核版面表达平行关系，避免硬接成一句；人物归属另凭研究解释，不把每栏机械补成某人独白。尤其复核 R-II2-15、19。
- disposition_required: fix
- blocks_integration: true；现稿无法可靠区分叙述与评语。

### R-II2-02：把一句对白扩写成死亡场景

- 位置／字段：`fw-ii2-260-01`，p260，`translation`。
- 类别／优先级：无据增补；P1。
- 原文：`Am shot, says the bigguard.`
- 当前中文：「大汉倒地，大个子倒地；一枪击中胸膛；他倒在都柏林湾，波涛拍岸！」
- 问题／依据：原句保留 `says` 的发言行为，没有胸膛、海湾、波涛或连串倒地动作。即使另有歌谣互文，也不能未经注明便把外部歌词塞进正文。
- 建议：恢复短对白及说话者。若有歌谣依据，定点列出处，把延伸解释放译注。
- disposition_required: fix
- blocks_integration: true；新增关键动作与场景。

### R-II2-03：p260–262 原作脚注漏译，编号错挂

- 位置／字段：`fw-ii2-260-01`，p260–262，`translation`。
- 类别／优先级：漏译、结构；P1。
- 原文／当前中文：p261 脚注1 `When we play dress grownup ... clingarounds` 现标「第四注」；脚注2整串地址 `Kellywick, Longfellow's Lodgings ... Terra Firma`、脚注3 `Groupname for grapejuice.`、脚注4 `Bhing, said her burglar's head, soto poce.` 均找不到对应中文。现稿反而又以「第四注：他究竟如何？」把下一页正文问题当作脚注。
- 进一步锚句：p262 原脚注1 `Yussive smirte ... Gotahelv!`、2 `O Evol, kool in the salg ...`、3 `A goodrid croven ...`、4 `Apis amat aram. Luna legit librum. Pulla petit pascua.`、5 `And after dinn to shoot the shades.`、6 `Says blistered Mary Achinhead ...`、7 `Begge. To go to Begge ...` 均无对应译句。现「第二注：摇起班卓琴」「第三注：当她，其飞蝶」「第六注：造前预定之明觉」分别取自旁注、正文和右旁注，并非这些脚注。
- 另见：p260脚注1开头 `Rawmeash, quoshe with her girlic teangue.` 在「第一注：若老希律王……」之前缺失。
- 建议：按页及原注号补齐并重新挂接；不能仅删除中文号次来掩盖遗漏。
- disposition_required: fix
- blocks_integration: true；整组原作文字缺失。

### R-II2-04：数词误算，四百之数消失

- 位置／字段：`fw-ii2-264-01`，p264，`translation`。
- 类别／优先级：漏误译；P2。
- 原文：`bowed and sould for a four of hundreds of manhood in their three and threescore fylkers for a price partitional of twenty six and six`。
- 当前中文：「折腰受售，充作三乘二十另加六名军卒身躯，平分标价二十六先令六便士。」
- 问题／依据：`a four of hundreds` 的四百之数消失；`three and threescore` 按表层数词是三加六十，现译却写六十加六。政治或历史所指可以另查，不能先改变数值。
- 建议：先保存400、63、26与6的数词层次，再查 `fylkers` 和分割价格是否借指议席／地域。勿靠猜测补人物规模。
- disposition_required: fix
- blocks_integration: true；数量关系与讽喻支点变动。

### R-II2-05：教父改成叔父

- 位置／字段：`fw-ii2-264-01`，p266，原作脚注2，`translation`。
- 类别／优先级：人物关系；P2。
- 原文：`used to do odd jobs for my godfather, the Rev. B. B. Brophy of Swords`。
- 当前中文：「常为家叔索兹教区布罗菲牧师奔走杂务。」
- 问题／依据：`godfather` 指教父；「家叔」添加父系血缘与长幼关系。原句也未把 Swords 明定为此处所译「教区」。
- 建议：保留教父关系与牧师头衔，地名从严。
- disposition_required: fix
- blocks_integration: true；偷换亲属关系。

### R-II2-06：p270 脚注缺失，p271 连锁动作缩成改写

- 位置／字段：`fw-ii2-268-01`，p270–271，`translation`。
- 类别／优先级：漏译、动作关系；P1。
- 原文／当前中文：p270脚注1 `The gaggles all out.`、脚注2 `He's just bug nuts on white mate ... Lang Wang Wurm, old worbbling goesbelly.` 均无对应。中文由「源自其后条件式未来。其一：慷慨付款者方为巨子」跳到正文 `Lumpsome is who lumpsum pays`，把正文挂成注1，之后直接接脚注3、4。
- p271 原文：`the girl ... that list to the wind that lifted the leaves that folded the fruit that hung on the tree that grew in the garden Gough gave`。
- 当前中文：「此乃取悦少女之滑翔机……倾听抚叶之风，拢起垂挂于戈夫所赐园林之树梢果实。」
- 问题／依据：原句串联少女听风、风举叶、叶裹果、果悬树、树生园等环节；当前拆成「倾听」「拢起」片段，容易读成无主命令；中间动作及重复骨架也已抹去。p271左旁注 `Cliopatria, thy hosies history.` 也只剩克利奥帕特拉名字，后半句不见。
- 建议：补原作脚注；逐环保存动作发起者与重复，再作中文节奏调整。
- disposition_required: fix
- blocks_integration: true；缺少整句原注，连锁句主客关系改变。

### R-II2-07：p273–275 旁注缺项

- 位置／字段：`fw-ii2-272-01`，p273–275，`translation`。
- 类别／优先级：漏译；P1。
- 原文锚句：p273左旁注 `Femilies hug bank!`；p274左旁注 `Murdoch.` 与 `As Shakefork might pitch it.`；p275左旁注 `Two makes a wing at the macroscope telluspeep.`。
- 当前中文：p273在「工钱、积蓄与开销。页缘：七国统辖……」间无 `Femilies` 句；p274「致在圣约翰山斩断阵列之汉子」未保留 Murdoch；p275从「（难耕圣洁古老爱尔兰），一界侵入另一界」直接转正文，未见 `Two makes ...`。`As Shakefork ...` 在其应处也无对应。
- 依据：上述均在冻结 HTML 独立 `aside.sl` 中，原作已收入 `original`，不是待译者可删的编辑说明。
- 建议：逐项补回，并核旁注插入位置；未知姓名不借顺句删除。
- disposition_required: fix
- blocks_integration: true；作者文字遗漏。

### R-II2-08：p276、278 漏掉旁注地址与称谓

- 位置／字段：`fw-ii2-276-01`，p276、278，`translation`。
- 类别／优先级：漏译；P1。
- 原文锚句：p276 `For all us kids under his aegis.`；p278 `Uncle Flabbius Muximus to Niecia Flappia Minnimiss. As this is. And as this this is.`；`Dear Brotus, land me arrears.`。
- 当前中文：p276「然风暴将先于严父降临……麦粥与浓羹敲钟开饭」缺群童与庇护句；p278「灰衣修女池塘边之芦苇：啊诶哦，容我长叹」未保留叔父／侄女称谓与两句重复；「举世皆渴盼传递书信。猫儿呈国王……」中没有 `Dear Brotus` 一旁注。
- 依据：冻结 HTML 均列左旁注；姓名、收发信称谓与重复不能以正文概括代替。
- 建议：补译旁注，保留信件称谓；勿添加新的血缘解释。
- disposition_required: fix
- blocks_integration: true；作者文字遗漏。

### R-II2-09：p281–282 漏掉两条完整左旁注

- 位置／字段：`fw-ii2-280-01`，p281–282，`translation`。
- 类别／优先级：漏译；P1。
- 原文：p281 `A saxum shillum for the sextum but nothums for that parridge preast.`；p282 `Panoplous peregrine pifflicative pomposity.`。
- 当前中文：前者在「三分之舌」与「低语之任性」之间完全缺席；后者在「虚无四方心爱主教」与「其本源主教神灵」之间缺席。
- 依据：两句均在 `original`，冻结 HTML 明列 `aside.sl`。不能把难解双关删作零字。
- 建议：保留声形，至少交出可辨词簇与歧义注；不需此轮重译整段。
- disposition_required: fix
- blocks_integration: true；整句漏译。

### R-II2-10：「百数体系」注释无依据，数字自相矛盾

- 位置／字段：`fw-ii2-280-01`，p283原注1；`notes[ii2-family-arithmetic-100].text`，并及 `translation`。
- 类别／优先级：注释硬事实、无据增补；P1。
- 原文：`Twelve buttles man, twentyeight bows of curls, forty bonnets woman and ever youthfully yours makes alleven add the hundred.`
- 当前中文：「十二位豪饮汉，二十八缕卷发少艾，四十顶软帽老妪，加上永远年轻之汝，恰好凑足百数圆满。」
- 当前注释：「十二位酒客、二十八位彩虹少艾、四十岁盛年母辈，汇同四老与三子女，构筑百数圆满之维柯体系。」
- 问题／依据：原文未出现「四老与三子女」，`forty bonnets woman` 也未明说「四十岁」。译文写四十顶帽，注释却改成年龄。若按注释自己列项计算，12+28+40+4+3=87，并不等于100。原文可能有声形与计数游戏，当前注释却用确定体系替代待解难点。
- 建议：撤掉已坐实百数结构的口吻。先列文字数项及未解部分；找到具体研究才补人物群像解释，注明来源页码与算式。
- disposition_required: fix
- blocks_integration: true；注释内有可复算矛盾。

### R-II2-11：几何段把拉丁片段、谐语与知识事实混成定说

- 位置／字段：`fw-ii2-284-01`，p287；`notes[ii2-four-strange-tongues].text`。
- 类别／优先级：出处、无据语言归属；P2。
- 原文：`Basqueesh, Finnican, Hungulash and Old Teangtaggle, the only pure way to work a curse.`
- 当前中文：「巴斯克语、芬兰语、匈牙利语与古盖尔语，乃是施行咒诅唯一纯正之道。」
- 当前注释：「列举非印欧语系之怪异语言组合……与爱尔兰盖尔古语（Old Tongue/Teangtaggle）」。
- 问题／依据：原文列改造过的四个词形，未作语系判断。现注既把第四项确定成盖尔语，又将整组定为非印欧语系；只有原著来源，不能支持这组语言学事实。即便保留第四词的猜读，也须另核语系。
- 建议：将词形认读与语系分类分开；删除未经核实的整组归类。父任务补词典／语言学证据后定稿。
- disposition_required: fix
- blocks_integration: true；当前仍断言无据语言分类，不能只靠 `proposal` 标签放行。

### R-II2-12：p290 大片正文与原注失落

- 位置／字段：`fw-ii2-288-01`，p290，`translation`。
- 类别／优先级：漏译；P1。
- 原文范围：从 `of the synchronisms, all lauschening, a time also confirmed seven sincuries later by the quatren medical johnny, poor old MacAdoo MacDollett, with notary`，经 `after the first compliments ... Blinkensope's cuddlebath`、`such a coolcold douche as him ... doubling back`、`chemise de fer ... Multalusi`、`from Arklow Vikloe to Louth super Luck`，至 `on behalf of an oldest ablished firma of winebakers`。
- 当前中文接缝：「……麦考利夫、可怜麦克白与麦克吉姆利三位医官之水表计时）在葡萄烘焙商拉格里马与热米蒂公司之红尘俗世，其后其技艺衰退……」
- 问题／依据：中文从三医官计时直接跳到酒商公司；上述确认时刻、沐浴、再来、衣装与化名、地点等整串文字无对应，不是精简句法即可解释。原注3 `Old Mamalujorum and Rawrogerum.`、4 `Why have these puerile blonds those large flexible ears?`、5 `Pomeroy Roche ... Wreck of the Ragamuffin.`、6 `No wonder Miss Dotsh took to veils ...` 亦缺译；现稿只留该页注1、2、7。
- 建议：按此接缝补齐原文与四条原注，先逐句对齐，再检查悬置的 `if she then` 主句关系。
- disposition_required: fix
- blocks_integration: true；连续正文及整条原注失落。

### R-II2-13：几何作图丢掉标记与连线操作

- 位置／字段：`fw-ii2-293-01`，p294、296；`translation`，并参已看 `geometricdiagram.jpg`。
- 类别／优先级：漏误译、图文关系；P1。
- 原文／当前中文：`the copyngink strayedline AL ... stops ait Lambday` 后挂脚注1，现译「直线AL……停歇于兰姆达一：其一……」，把脚注1粘成「兰姆达一」。p296 `join alfa pea and pull loose by dotties and ... eelpie and paleale by trunkles`，现译「将阿尔法与佩连缀，拉扯虚线……以躯干连接鳗鱼派与淡麦酒」。
- 问题／依据：图内有 Aα、λL、π、P。该段一面说笑，一面规定点、圆、虚实连线。现稿把点名字母音串和作图指令主要当食物、躯干译去；只在段首留下「【图：几何图解】」，读者不能按中文复原正在画哪条线。「兰姆达一」还额外制造图中没有的编号。
- 建议：逐项核 A／L、α／λ、π／P 与 `alfa pea`、`eelpie`、`paleale` 的对应，正文保留可辨端点及连线类型；饮食双关入注。不要在本报告未确认的读音链上擅定最终算式。
- disposition_required: fix
- blocks_integration: true；主要几何动作不可复原。

### R-II2-14：`Mi vidim Mi` 注释用另一字串代释，未交代差异

- 位置／字段：`fw-ii2-293-01`，p297原注2；`notes[ii2-ugol-egal-ogle].text` 及 `translation`。
- 类别／优先级：语言、出处；P2。
- 原文：`Ugol egal ogle. Mi vidim Mi.`
- 当前中文：「角角相等，凝视相对。我们彼此相见。」
- 当前注释：「后半句为塞尔维亚-克罗地亚语‘我们彼此相见’（mi vidimo se）」。
- 问题／依据：原词形是 `Mi vidim Mi`，注释给出的范式却是 `mi vidimo se`，词尾与末词均不同。原著只能证明前者存在，不能证明后者就是其语言与句法。Joyce可混语，但不能借混语省略差异说明。
- 建议：逐词查词典、形态与代词指向；当前先撤确定语言及互见关系，说明拟读和词形距离。
- disposition_required: fix
- blocks_integration: true；当前以未核外语释义确定正文互见动作。

### R-II2-15：旁注切断肚脐与顶点，挤进正文空间关系

- 位置／字段：`fw-ii2-293-01`，p297，`translation`。
- 类别／优先级：无据连接、句法；P1。
- 原文主句：`till its nether nadir is vortically where (allow me aright to two cute winkles) its naval's ... napex will have to beandbe`；省略处是独立左旁注 `Prometheus or the Promise of Provision.`。
- 当前中文：「直至其底谷深渊旋涡般正对普罗米修斯或供应之许诺。（容我借双眼狡黠眨动）其肚脐之顶点注定所在之处。」
- 问题／依据：`where` 引空间从句；`naval's napex` 横跨旁注，仍属正文。当前让底部「正对普罗米修斯或供应之许诺」，把旁注变成空间对象，再割裂肚脐／顶点句。
- 建议：先接回主句，另列旁注；保留身体／几何叠合，不代作者添加动作对象。
- disposition_required: fix
- blocks_integration: true；改换主句关系。

### R-II2-16：p302 左旁注漏译，古印本长 s 成无据事实

- 位置／字段：`fw-ii2-298-01`，p302，`translation`；`notes[ii2-lifp-year-fends].text`。
- 类别／优先级：漏译、出处；P1。
- 原文／当前中文：独立左旁注 `Ensouling Female Sustains Agonising Overman.` 在原文 `all the ... clerricals` 间；中文「万分感谢自个儿之文书，再次恳求……」未译该注。
- 另：原作脚注 `Lifp year fends ... fouvenirs foft as fummer fnow`；现项目注断言「用十八世纪古印本长s（f）字体印刷」。冻结文字实际保存字母 `f`，未给十八世纪印本或字体证据；长 s 是 `ſ`，不能把二者不加说明地等同。
- 建议：补左旁注。字体说改为待核拟读，分别说明 f、s、长 s 的声形联想；若要称某种印本实况，提供可复看影像。
- disposition_required: fix
- blocks_integration: true；有原作漏句，也有未核印刷史断言。

### R-II2-17：`less is the pity` 反成「更为遗憾」

- 位置／字段：`fw-ii2-303-01`，p304，`translation`。
- 类别／优先级：否定／程度误译；P2。
- 原文：`And less is the pity for she isn't the lollypops she easily might be if she had for a sample Virginia's air of achievement.`
- 当前中文：「更为遗憾乃是，她绝非应有之甜心，倘若她具备弗吉尼亚功成名就之神采。」
- 问题／依据：`less` 改成「更」，`easily might be` 又写「应有」，同时改变程度与可能／应然语气。`lollypops` 的贬褒及 Virginia 所指仍可有分歧，但不能因此忽略明确比较词。
- 建议：保留「少些可惜」等较弱可惜程度及假设语气；查 `lollypops` 语域后再定中文。
- disposition_required: fix
- blocks_integration: true；评价方向改变。

### R-II2-18：p305 连续正文整段跳失

- 位置／字段：`fw-ii2-303-01`，p305至p306开头，`translation`。
- 类别／优先级：漏译；P1。
- 原文范围：`Thou in scanty shanty!! Thou in slanty scanty shanty!!! Bide in your hush! ... The law does not aloud you to shout. I plant my penstock in your postern ... Ave! ... Vale. Ovocation of maiding waters. ... I defend you to champ my scullion's praises. To book alone belongs the lobe. Foremaster's meed will mark tomorrow when we are making pilscrummage to whaboggeryin with staff, scarf and blessed wallet and our aureoles round our neckkandcropfs`。
- 当前中文接缝：「睡吧。汝在陋室！环抱我等头颈，沉重守护老爹，奉送甜美点心之长辈，将赐予我等诺布莱特惊喜。」
- 问题／依据：中文留第一次 `Thou in shanty!`，即跳到 p306 `aureoles round ...` 附近。重复递增、闭嘴命令、法律、笔杆、问候辞、称赞、书与耳叶、翌日巡礼、手杖围巾与钱袋均无对应；「环抱我等头颈」也失去所环绕者 `aureoles`。
- 建议：补回这段及两页接缝，保留三次递增呼喊、书信收束与翌日动作。
- disposition_required: fix
- blocks_integration: true；连续正文与主要动作失落。

### R-II2-19：p303 旁注成帕内尔动作对象；章末题单失去并行关系

- 位置／字段：`fw-ii2-303-01`，p303、306–308，`translation`。
- 类别／优先级：句法、结构；P1。
- 原文：正文 `how Chawleses Skewered parparaparnelligoes ... between brave Danny boy and the Connolly`；其中左旁注 `Conception of the Compromise and Finding of a Formula.`。
- 当前中文：「查尔斯之肉叉如何穿刺帕内尔派妥协构想与配方寻觅。在英勇丹尼与康诺利之间。」
- 问题／依据：旁注的「妥协构想与配方寻觅」成了「穿刺」宾语，介词短语则断成独句。p306–307将人名整批前置，虽多数名字还在，却切断姓名与作文题的可见配对；这不是完整保留原版多声部。
- 建议：恢复主句 `between` 关系，独列旁注；章末按页或题项保存人名与题目对应。沿 R-II2-01统一层级处理，勿另造剧情。
- disposition_required: fix
- blocks_integration: true；句法与对应关系变动。

### R-II2-20：p304–307 原作脚注多处漏失或只剩尾句

- 位置／字段：`fw-ii2-303-01`，p304–307，`translation`。
- 类别／优先级：漏译、原注挂接；P1。
- 原文／当前中文：p304注1 `A byebye bingbang boys! See you Nutcracker Sunday!`、注2 `Chinchin Childaman! Chapchopchap!` 不见；中文「其一：其计数之手伴随黑化剂升起」实际取自正文加右旁注。p305注1 `From three shellings. A bluedye sacrifice.`、注2 `Not Kilty. But the manajar was. He! He! Ho! Ho! Ho!`、注3 `Giglamps, Soapy Geyser, The Smell and Gory M Gusty.` 均缺。p306注2 `Strike the day off, the nightcap's on nigh. Goney, goney gone!` 缺。
- p307：注1 `Jests and the Beastalk with a little rude hiding rod.` 没有译成中文；现「其一：小溪潺潺……亲爱艾玛姨母」实际搬来 p306注1。注7 `He has toglieresti in brodo all over his agrammatical parts of face and as for that hippofoxphiz` 只剩尾部「不祥数字，洗礼迟到！」；注8 `Eh, Monsieur? Où, Monsieur? Eu, Monsieur? Nenni No, Monsieur!` 全缺，正文 `Eu` 也没有对应。
- 建议：按页建立原注清单，逐条补回及校号，保留问答与拟声。项目六条解释注不能代替原作这些脚注。
- disposition_required: fix
- blocks_integration: true；多条原作文字缺失。

### R-II2-21：词典、人物与学术来源未落实，不能用原著兜底

- 位置／字段：多段 `notes[].text`，具体ID见下；所有 `source_ids` 只列 `joyce-fp`。
- 类别／优先级：出处、硬事实；P2。
- 当前断言／原文边界：`ii2-booming-cursowarries` 把括号英文 `corsair` 释「巡洋舰」；`ii2-lutharius-sinobiled` 认定「西诺贝尔公爵」；`ii2-pappapassos-mammamanet` 给 `pappa passus` 配「父亲已逝去」并扩为维柯历史法则；`ii2-sangannons-dream-shannon` 称「爱尔兰传统民谣」却不列曲名；`ii2-run-phoenix-run` 断言凤凰公园赛马与猎犬赛事呼号；`ii2-buckley-russian-general-pumped` 添「望远镜与风箱机枪泵杀将军马匹与肉身」。各原锚句没有这些人物、史料与器械细节。
- 问题／依据：原著能支持这些字串出现，不能单凭字串证明所声称的词义、爵位、拉丁范式、歌曲身份、赛事历史和枪械行为。后几项还会把猜测转成阅读剧情。第一个括号词义须按普通词义核准，不能仅凭相近海军词汇蒙混。
- 建议：逐条引用具体词典或研究页，标明哪句证据支持哪项。补证前删掉硬事实断言或明记尚未核实；保留词形联想应缩在可见证据内。父任务统一外核可另作补证，但不得偷偷改成本报告已经查阅。
- disposition_required: fix
- blocks_integration: true；涉及具体词义与无据人物／剧情，尚未达到证据要求。不是要求一切解释都证明作者意图。

### R-II2-22：章末署名对应待核，位置说明有误

- 位置／字段：`fw-ii2-303-01`，p308，`translation`；`notes[ii2-jake-jack-sousoucie].text`、`notes[ii2-kish-anticheirst].text`。
- 类别／优先级：人物归属、语言、定位；P2。
- 原文：`from jake, jack and little sousoucie`。
- 当前中文：「出自杰克、雅各布与无忧无虑小妹」；注释按此顺序写「杰克（肖恩/凯夫）、雅各布（谢姆/多尔芬）」并把 `souci` 本身释成「无忧」。
- 问题／依据：原文区分 jake、jack；当前译名及角色配对未交代依据。此处不能只按译名发音判定谁是谁，也不据未核资料裁定现配对一定颠倒。`little sousoucie` 可以拟无忧，但须区分法语单词字义与改词解释。另 `ii2-kish-anticheirst` 称「第十段首条脚注」，实际当前章有十一段，该原注在末段 p308；这是可直接核对的位置错误。
- 建议：核 jake／jack 姓名关系与兄弟化名后解释对应；法语词义与双关分开写。位置改用 p308原注1，不用易过期段数。
- disposition_required: qualify
- blocks_integration: false；姓名角色先列未决拟读，不以此一项拖延已保守标明的解释；位置错同轮修正。

## 六十六条项目译注逐条核读记录

下面逐条记是否只需保留解释边界、是否含外核硬事实，或已触发问题。每项均已读其 `lemma`、`kind`、`certainty`、`text`、`source_ids`。未列阻断不代表外部考据已获通过；六十六条均为 `proposal`，均只引 `joyce-fp`。作者原作脚注另按上文核查，不能与项目译注混算。

### `fw-ii2-260-01`（6条）

- `ii2-unde-et-ubi`：已读。注内自列「身在何处」，开头却写「何处去」；正文也写去。宜依 ubi 的当前位置义定点核词，勿径增目的地。「古经院哲学范畴」未外核。
- `ii2-tomtittot-totalitarian`：已读。两端词形支持对照；童话名称及故事身份未外核。「政治强权演变尺度」仅作本项目解释。
- `ii2-broad-hairy-face`：已读。嘲辱措辞原文可核；「都柏林市井打油诗」需具体歌谣来源，HCE归属仅是拟读。
- `ii2-mater-mary-nipples`：已读。乳头与乳汁见原文；拉丁祷词及伊瑟角色归属未外核。不要用少女娇嗔概括全部语气。
- `ii2-booming-cursowarries`：已读。食火鸡与咒语词形联想可保留；corsair词义列 R-II2-21。
- `ii2-lutharius-sinobiled`：已读。路德／洛塔里奥可列声形候选；公爵身份缺证，见 R-II2-21。

### `fw-ii2-264-01`（6条）

- `ii2-archaic-zelotypia`：已读。与下一条重叠，可合并；兄弟学派、宗派争执属解释，未核来源。
- `ii2-odium-teleologicum`：已读。theologicum／teleologicum形式对照可见；神学术语典故需词典或研究支持。
- `ii2-anama-anamabapa`：已读。递增字串及 Mama／Papa 拟声有字面基础；「语言发生学」只作阐释，不当已证作者意图。
- `ii2-tarararat-ark`：已读。Ararat、Tara与bunk拟读未外核；「群童重归」为场景解释，不应反向扩写正文。
- `ii2-doss-in-manger`：已读。马槽和doss在原文；寓言、基督降生双典未外核，可列候选。
- `ii2-fathering-law`：已读。father-in-law拆读有词形基础；父权律法是解释，不等于新增亲属事实。

### `fw-ii2-268-01`（6条）

- `ii2-telltale-annaryllies`：已读。声音与Anna／花名联想属拟读；所谓 I.8开篇引文未独立重开该章核对，应核准确字串后加跨章定位。
- `ii2-arms-enlocked`：已读。双臂交挽原文可核；彩虹少女、姐妹环舞和镜像依恋未从本句确证。
- `ii2-understudy-understandings`：已读。词形及下装候选已读；角色归属和英语俗义待词典支持。
- `ii2-gymnufleshed-genuflection`：已读。genuflection／flesh形近音近可列拟读；gymnastics成分及修道学堂解释未外核。
- `ii2-deadleaf-brown-quicksilver`：已读。色彩、贴花见原文；「维柯式对应」没有随注证据，保留为项目解释即可。
- `ii2-slippering-snake-charmeuse`：已读。织物、蛇、滑动词形可核；伊甸园互文尚属提案。

### `fw-ii2-272-01`（6条）

- `ii2-leda-afraida`：已读。Leda词形明确；天鹅神话与ALP母体对应未外核，须分神话事实与解释。
- `ii2-pappapassos-mammamanet`：已读。拉丁词形／译义与维柯法则均未有可核来源；见 R-II2-21。
- `ii2-traduced-jinglish`：已读。traduced及混杂音串可见；translated对照与全书自指可作提案，不冒称词源。
- `ii2-nusances-dolphins`：已读。nuisances／dolphin／Dauphin可列候选；Dolph=谢姆与王太子名号需角色研究及词典，未核。
- `ii2-girdle-grow-garden`：已读。girdle/garden童谣拟读合理但曲目未外核；注称腰带渐紧，正文称渐宽，需交代尺度差别。
- `ii2-boyjones-herodotus`：已读。Herodotus词形拟读可见；Boy Jones潜宫史实尚无具体出处。

### `fw-ii2-276-01`（6条）

- `ii2-twoheaded-dulcarnons`：已读。阿拉伯语词源、亚历山大称号与《几何原本》I.47的传统均是硬事实，原著来源不能单独支持，须定点外核；未判其已错。
- `ii2-dove-without-gall`：已读。dove/gall原文可核；古代博物学传统及肖恩／兄弟对应未外核。
- `ii2-amum-amum-amen`：已读。三次重复及Amen/Mum联想有字串基础；ALP母性回声属解释。
- `ii2-surplice-money-bed`：已读。酬劳费义及婚礼／洗礼规费范围需词典或教会史来源；宗教与婚床联系可作提案。
- `ii2-wits-borrows-clothes`：已读。借衣对买床见原文；「穷书生谢姆」「兄弟富贵／流亡」无随注证据，不反写成确定剧情。
- `ii2-backslapping-gladhander`：已读。拍肩示好可核；「市侩政客」「肖恩钻营」属角色解释，宜收敛措辞。

### `fw-ii2-280-01`（6条）

- `ii2-bibelous-hicstory`：已读。醉酒、圣经、红胡子与异端读法需逐层限定；腓特烈一世身份及官方历史论未外核。
- `ii2-family-arithmetic-100`：已读。数字与人物体系冲突，见 R-II2-10。
- `ii2-run-phoenix-run`：已读。Phoenix原词可核；赛事呼号、HCE围捕剧情须另证，见 R-II2-21。
- `ii2-dreamoneire-dream`：已读。dream与oneiros拟读未有词典支持；「梦境本质」是解释，不称已证。
- `ii2-road-to-rouen-ruin`：已读。Rouen/ruin可听读比较；拿破仑战败与该地关系未见随注来源，勿据此补历史情节。
- `ii2-slash-the-pill`：已读。pill/pellet字形可核；外科、板球与投毒三联需逐项证明，当前仅作候选。

### `fw-ii2-284-01`（6条）

- `ii2-median-hce`：已读。hce/che/ech字母可核；父权解释属提案，无另增人名。
- `ii2-interecting-angles`：已读。intersecting/right及erecting叠读有词形基础；「性心理象征」保持解释口吻。
- `ii2-spider-wavetrap`：已读。改写诗句可作互文候选；Mary Howitt作者及确切引句尚未独立核文献。
- `ii2-four-strange-tongues`：已读。语言归属／语系断言见 R-II2-11。
- `ii2-fearmanagh-height`：已读。Fermanagh/fear形近可核；行政归属及北方战乱暗喻须分事实与解释。
- `ii2-family-umbroglia`：已读。imbroglio/umbra/umbrella拟读已读；意大利语准确词义与词源未外核，不能列为既定组合。

### `fw-ii2-288-01`（6条）

- `ii2-dillon-dollar-scholar`：已读。童谣具体字串与Dillon家族未外核；dillar不等于dime，正文／注头「一角钱」应另核，勿把声音改成确定币值。
- `ii2-plutonic-platonic-loveliaks`：已读。两个词形并列可核；冥界、地质与精神恋的联想须分层，未判全部坐实。
- `ii2-draw-the-line-somewhawre`：已读。画线／伦理划界有文本基础；母体解剖联系是下文解读，需保留提案边界。
- `ii2-buckley-russian-general-pumped`：已读。跨章传奇及器械、马匹细节未获支持，见 R-II2-21。
- `ii2-matter-of-brettaine`：已读。Matter/Brut形近联想可列；中世纪三大题材及亚瑟王传统未核原文献。
- `ii2-bussmullah-lord-wolsley`：已读。Bismillah/Wolseley候选已读；具体埃及远征历史未外核，姨母争吵属解释。

### `fw-ii2-293-01`（6条）

- `ii2-coss-cossist-algebra`：已读。代数术语及意大利语cosa词源需要历史词典；cause谐音只列候选。
- `ii2-somnione-sciupiones`：已读。西庇阿梦与意大利sciupare拟读需各核出处；「经院虚妄」是阐释。
- `ii2-ugol-egal-ogle`：已读。三语归属与Mi句法未经核准，见 R-II2-14。
- `ii2-sangannons-dream-shannon`：已读。河名／民谣混说且无曲名，见 R-II2-21。
- `ii2-chape-dona-speranza`：已读。Lady Wilde身份、笔名及chape两层义均需文献或词典；目前原作不能单独支撑。
- `ii2-whangpoos-paddle-sound`：已读。Whangpoo与黄浦拟读可列；泛全球水系论是解释。不得以译注代替原作拟声。

### `fw-ii2-298-01`（6条）

- `ii2-ambages-role`：已读。曲折与角色有字面基础；兄弟家庭伦理心理只作解释。
- `ii2-paa-lickam-apl`：已读。APL/LPA倒排可核；吮舐／母体联想以拟读保留。
- `ii2-this-is-an-her`：已读。原文句法倒错已读；说话者多尔芬、受话者凯夫及母体隐私认定需角色证据，不能直接当语法事实。
- `ii2-lifp-year-fends`：已读。长s印刷史无证，见 R-II2-16。
- `ii2-fouvenirs-foft-snow`：已读。重复f字母与改拼可核；「清齿音化」术语未解释具体音位，需避免泛称所有字母变化；少女纪念册场景仅作提案。
- `ii2-plumpduffs-pants`：已读。球衣、短裤拟读可列；具体橄榄球赛与兄弟拳脚不是原脚注单独证明的事实。

### `fw-ii2-303-01`（6条）

- `ii2-force-centres-kundalini`：已读。原左旁注列七处；Kundalini传统、七脉轮体系与此特殊列表是否完全对应未外核，不能只把清单套入泛称体系。
- `ii2-according-to-cocker`：已读。Edward Cocker与算术课本的俚语词源需词典或书目，未核。
- `ii2-jake-jack-sousoucie`：已读。姓名顺序、角色对应与法语说明见 R-II2-22。
- `ii2-thumb-on-nose-forks`：已读。已看资产：手势与交叉餐叉可见；「全书著名」无必要。三兄妹落款是解释，实际输出呈现另核。
- `ii2-kish-anticheirst`：已读。灯船／浅滩身份需地名史来源；「第十段」位置错见 R-II2-22。
- `ii2-drawings-on-the-line`：已读。几何线／晾衣绳候选可列；「圆满落幕」只是阐释，不能用来证明中文覆盖完整。

## 父任务定点补证（不算本人独立外部查阅）

报告成稿时读到父任务交回的 `reports/reviews/gemini-book-II-2026-11-03/evidence.json`，其当时 SHA256 为 `3a4b5137b172811c46f7ff14457660ee4a6b89d1238d947e2a8478a7a9d702a5`。以下只引用其具名查阅记录，限于普通事实，不据此确立 Joyce 唯一读法：

- `E-CORSAIR`：[Merriam-Webster, corsair](https://www.merriam-webster.com/dictionary/corsair)，父任务实读定义段：海盗／私掠者。支持 R-II2-21 纠正括号中「巡洋舰」；不证明 cursowarries 必定含 corsair。
- `E-PATIOR`：[Dickinson College Commentaries, patior](https://dcc.dickinson.edu/latin-core/patior)，父任务实读词形 `passus sum` 及 permit／endure。支持 R-II2-21 将「pappa passus＝父亲已逝」撤出规范拉丁语事实；仍可另列英语 passes 等声音拟读。
- `E-IRISH`：[Trinity College Dublin Irish Language Office](https://www.tcd.ie/gaeloifig/en/international.php/1000/)，父任务实读 Irish 为印欧语系凯尔特语支。支持 R-II2-11：若第四项认作盖尔语，就不能同时把四项统称非印欧语。不决定 Old Teangtaggle 究竟唯一指哪种语言。
- 统一证据把 `ii2-lutharius-sinobiled` 列 `unresolved`：尚未取得「西诺贝尔公爵」可定位来源。未取得不等于证明人物不存在；本报告只要求撤确定身份或补证。

## 各段核过范围与未核项

本节的「全段」均指冻结稿该段 `original`、`translation`、六条项目注，已逐项读完；也核了相关页码与版面标签。下列 SHA256 均按 `original` 原字串 UTF-8字节计算，不加换行，与清单相符。

### fw-ii2-260-01 / 稿内定位 260.01–263.48

- original_sha256: `b8b2a95f2fff348746aca4a7569e22cad21e9b1ed22cfb4dfcf68d563c95943c`
- 已核：全段英文首句 `unde et ubi. As we there are where are we are we there from tomti` 起，至 `e was a gay Lutharius anyway, Sinobiled. You can tell by their extraordinary clothes.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-02、R-II2-03、R-II2-21。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-264-01 / 稿内定位 264.01–267.56

- original_sha256: `d2995b09fd81ecc3f5f351c80d305bbecb7b45ed941a709fd74f33e52d46df01`
- 已核：全段英文首句 `archaic zelotypia and the odium teleologicum. Honour commercio's ` 起，至 `ketts. 6 All abunk for Tarararat! Look slipper, soppyhat, we've a doss in the manger.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-04、R-II2-05。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-268-01 / 稿内定位 268.01–271.67

- original_sha256: `4d58aaaa36d475fc24c903d476c201d726c05cfe2e4140c14130a3c108532717`
- 已核：全段英文首句 `if have faded from the fleur,1 their arms enlocked, (ringrang, th` 起，至 `hollymost applissiate a nice shiny sleekysilk out of that slippering snake charmeuse.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-06。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-272-01 / 稿内定位 272.01–275.60

- original_sha256: `41f3608faed1f065a792165b4529c3e963f55f96a493f2364f78150bb38130ab`
- 已核：全段英文首句 `Hoots fromm, we're globing. Why hidest thou hinder thy husband hi` 起，至 `k all to sheeks. 6 Traduced into jinglish janglage for the nusances of dolphins born.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-07、R-II2-21。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-276-01 / 稿内定位 276.01–279.52

- original_sha256: `dea5c4b1eae5802d1ec035d84d136150db9b8a17548f4694292a0ad8745f1108`
- 已核：全段英文首句 `other's weariness waiting to beadroll his own properer mistakes, ` 起，至 `ng friend and ah me sweet creature, what buys the bed while wits borrows the clothes.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-08。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-280-01 / 稿内定位 280.01–283.42

- original_sha256: `31b38ff6431fc86784241d175a44d0193aacc2ad04a57cdc7e6ec597d9d9435a`
- 已核：全段英文首句 `A scene at sight. Or dreamoneire. Which they shall memorise. By h` 起，至 `s more like his deed every die. 3 Slash-the-Pill lifts the pellet. Run, Phoenix, run!` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-09、R-II2-10、R-II2-21。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-284-01 / 稿内定位 284.01–287.38

- original_sha256: `b962f611e0a915f55f93df2771d6415399c13f9a9208e3a0c2dfdcb5e240c140`
- 已核：全段英文首句 `A stodge Angleshman has been worked by eccentricity. median, hce ` 起，至 `asqueesh, Finnican, Hungulash and Old Teangtaggle, the only pure way to work a curse.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-11。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-288-01 / 稿内定位 288.01–292.35

- original_sha256: `0886ab5c8de03eee087085545f48f93d1108830385289bf9b1add05114177b9f`
- 已核：全段英文首句 `for a dillon a dollar,1 chanching letters for them vice o'verse t` 起，至 `Brettaine and brut fierce. 3 Bussmullah, cried Lord Wolsley, how me Aunty Mag'll row!` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-12、R-II2-21。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-293-01 / 稿内定位 293.01–297.43

- original_sha256: `129d2394009517a65b6314e85e2ab9039549c86e1a7645276d6628b9ec98f58e`
- 已核：全段英文首句 `why my as likewise whis his. Coss? Cossist? Your parn! You, you m` 起，至 `is Sangannon's dream. 4 And all meinkind. 5 Whangpoos the paddle and whiss whee whoo.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-13、R-II2-14、R-II2-15、R-II2-21。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-298-01 / 稿内定位 298.01–302.49

- original_sha256: `b9c4c23341b2b83310df6f046fefeaba4e67aa85a13b6be8cd2ab0d259ad0ae3`
- 已核：全段英文首句 `Ambages and Their Rôle. Paa lickam laa lickam, apl lpa! This it i` 起，至 `rs foft as fummer fnow, fweet willings and forget-uf-knots. 3 Gag his tubes yourself.` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-16。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

### fw-ii2-303-01 / 稿内定位 303.01–308.55

- original_sha256: `7343b79a4c6d9372616bd3fdb714a79fd52aa1048165b9164449b1f8cb9ddc30`
- 已核：全段英文首句 `according to cocker. And this, pardonsky! is the way Romeopullupa` 起，至 ` for skool and crossbuns and whopes he'll enjoyimsolff over our drawings on the line!` 止；当前中文全文；六条项目注（上节逐条列出）。
- 判定：needs_revision；相关问题：R-II2-01、R-II2-17、R-II2-18、R-II2-19、R-II2-20、R-II2-21、R-II2-22。
- 未核：印本精确行号、外部典故与词源文献、人工署名与生成读本显示；上述图资产检查只覆盖已见图样。不存在以本段通过证明全章通过的结论。

## 结论与交接

- 当前版本：**needs_revision**。十一段全文及六十六条项目注已读；外部出处、逐页影像和生成读本显示仍属未核范围，不能写成全部考据已过。
- 阻断重点：R-II2-02无据死亡场景；R-II2-03、06–09、12、16、18、20漏掉正文或原作脚注；R-II2-01、13、15、19混淆版面层次或几何动作；R-II2-04、05、10、14、17、21误置数量、关系、语气或事实。R-II2-22的人物归属另列待核，位置错可直接修。
- 原稿 `coverage_review` 声称已补全正文、双栏与页脚。以上逐句漏项足以否定「完整译文」；本报告不改该字段，整合者须另行重核覆盖，不得据本次读完原文反证稿件完整。
- 修订只须定点补漏、复位、纠正已列事实与句法；不要求整章重译。所有新补译须再查对应原文与旁注位置。保留争议的词形解释，写清可见依据和损失；不为顺口而添故事。
- 本报告不授予人工 `reviewed`，不推进断点，不推送。修订稿应另存并绑定新 SHA256；外部补证另列实际来源、页码与查阅人，再由整合者逐项处置。
