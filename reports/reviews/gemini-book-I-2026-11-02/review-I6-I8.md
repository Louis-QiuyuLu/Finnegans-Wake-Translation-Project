# Gemini 新稿 I.6–I.8 独立审校

## 输入

- role: `ai_review`。
- executor: Codex 子代理 `/root/audit_i6_i8_latest`。这是 AI 独立审校，不是人工审校。
- 实际待审稿：`/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-6.json`、`I-7.json`、`I-8.json`。仅审这三份冻结稿。
- 英文见证：`/private/tmp/fw-full-source-20261101/manuscript/chapters/` 同名 JSON 的 `source_text.html`；交接指明为 Faded Page 1958 第八印本转录。没有亲查印本扫描或原 ZIP，也未引入其他版本。
- workpack: 本次没有另获独立工作包；以上完整英文 JSON 是核覆盖依据。不得把旧报告的 SHA 换成新稿 SHA。
- revision_round: 交接未附可核修订轮次账；本报告不据此授权增加修订轮次。
- 文件 SHA256 如下。`original_sha256` 按每段 `original` 原字串 UTF-8 字节计算，列于末尾。
- `/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-6.json`：`fc9525c141ea2dd828591585ab63656f70ea50adc5a54259caa027ee130e4913`。
- `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-6.json`：`04aa9041a59d8479f37b97dddd34e07d1ed2160fb43fc2af295f792d1b9e8f56`。
- `/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-7.json`：`fa78912d688b3d30be12065e1a8629090ea17cd3707334dfe1d6cb0cbce07c56`。
- `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-7.json`：`9507e0f6612fa36094f5391f211370690c53e5ecf732b9d64e99d1ca8b714b5d`。
- `/private/tmp/fw-book-I-intake-20261102/manuscript/chapters/I-8.json`：`600873f1331ce0748406c4c34bdab6fac6c5ddb32aa2c823cfdf322cd6ad58da`。
- `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-8.json`：`57d3982adc54bb97cfe8e5802177b08c566fa15f7334a8cc5c34cba27514e2da`。

## 范围与查阅

已读项目 `AGENTS.md`、`docs/EDITORIAL_GUIDE.md`、`docs/SOURCES.md`、`docs/MANUSCRIPT_FORMAT.md`；已读指定 `review-translation/SKILL.md` 及 `references/review-protocol.md`，并参考旧 `reports/reviews/gemini-book-I-2026-11-01/I-6-I-8.semantic.r0.md` 的问题清单。旧结论没有套用到新稿。

实际逐段读完 23 段英文、23 段中文；核句间动作、否定、问答、清单与衔接。另读全数 113 注：I.6 为 56 注（40 `proposal`、16 `uncertain`），I.7 为 36 注（全 `proposal`），I.8 为 21 注（全 `proposal`）。检查了词目、主张、分级与正文关系，没有将来源 ID 或分级标签当作外部证据。

另将三章全部 `original` 连读串与完整英文 `source_text.html` 对照。去掉 HTML 标记、分页标识、空白及连字符后，I.6、I.7 全文一致；I.8 只余 `C_{3}` 与 HTML 下标 `C3` 的表示差异，再归一此处便一致。此核对用于排查成片英文遗漏；不证明印本逐字校勘、坐标行数或版面准确。中文覆盖判断来自实际英中阅读，不靠字数或归一比较。

未核：1939 初版扫描、1958 实物印本、手稿稿层、已有中译原页；113 注中的外部词源、历史事实、学者观点、引文出处尚未逐项重开原典核验。本报告不能充当完整出处审校。尤其不因 `proposal` 或 `uncertain` 就声称其中事实已获证实。

## 覆盖复核

新稿确已补入旧稿大量删节；不能继续笼统指为“梗概代正文”。本次全文阅读未再发现旧稿那类整块问答、寓言、清单或章尾删除。

I.6：

- `fw-i6-126-01`：第一问开头至多姆纳尔呼唤，豆茎、日常事务正反复列、建筑、礼物与七鸽舍均有中文。
- `fw-i6-129-27`：第一问次段，政治身份、二十四表亲、婚丧、几何、战事等连串均已展开。
- `fw-i6-133-01`：遗产之问、保险险种、党派、数字及自然循环清单已译；旧“造孽”误换“遗产”已修。
- `fw-i6-136-09`：第一问末段、父母与物件、安徒生及伊凡、时墓对照与谜底均已译。
- `fw-i6-139-15`：第2–8问均已译。四城次序为 Delfas、Dorhqk、Nublid、Dalway，四段独白及合声已恢复；第六问五段拟声、第八问动词顶真链已恢复。
- `fw-i6-143-03`：第九问变色链、第十问上半部挑逗、妆饰、诗与教士讽刺均已译。
- `fw-i6-146-17`：第十问下半部 Ada 至 Thelma 点名、婚约、耳语、衣饰、誓词与锁匠笑声均已译。
- `fw-i6-148-33`：第十一问题干与拒绝、dime/cash、Bitchson/Winestain、Talis/Qualis 例证、教授实验与寓言开场均已译。
- `fw-i6-152-18`：穆克思出行、溪流、格莱普斯、问候、询时、量身与容量、引书论证、教会争执和末尾互骂均已译；旧稿另造酷刑场面已清掉。
- `fw-i6-157-08`：小云女引人注意不成、暮色、两妇抱走两人、树石、化泪与课堂收束均已译；`could not all hear` 已改“未能尽闻其声”。
- `fw-i6-159-24`：流放岛屿、长树名插段、世界语、乳品论辩、餐桌、布鲁图斯／卡西乌斯及哲学争论均已译。
- `fw-i6-163-29`：毛发、歌唱、肖像、帽盒、公共花园与电影、ABC三人团、婚誓、逐客与第十二问答均已译。末尾否定仍有 N-02。

I.7：

- `fw-i7-169-01`：身体数字清单、宇宙谜题与各个猜答、饮食排除清单、酒与肉铺广告均已恢复，没有再移放到游戏段。
- `fw-i7-172-11`：拒不自杀四句、电报、canaille/Low Swine、沙龙、见风转舵、雨夜拖行、尾诗均已译。
- `fw-i7-175-29`：童戏全串、避战、酒吧自夸、望远镜撞枪口、蓝皮书幻象和病痛噪声长串均已译。
- `fw-i7-180-34`：模仿签名与伪造支票、插入广告、写作与自画像、室内物件及吊袜带身份清单均已译；没有再以普通脏屋物件换掉原清单。
- `fw-i7-184-11`：厨房配料与八道蛋食、出版抵制、拉丁造墨和三处英文插嘴、皮肤写史、巡警问答均已译。造墨保留脱衣露臀、掌中排便、置器、呼求双圣、唱诗、撒尿、混合、煮及冷却次序。
- `fw-i7-187-24`：Justius 训斥、身体和生殖责难、众女子、炖菜、职业与流亡、纯洁青年、赈款、药剂、流言接力、死亡骨均已译；财富否定仍有 N-03。
- `fw-i7-193-31`：Mercius 的王权、I/you 代词交错、母河消息、桥堰地点及举杖后哑者开口均已译；没有再把举杖提前。

I.8：

- `fw-i8-196-01`：开篇互答、洗衣、HCE名号出身、婚配、驳船与抵岸、安娜招人、老汉困坐、奉食遭拒、歌唱和末尾长歌均已译。托盘条件句见 N-04。
- `fw-i8-201-21`：111儿女、纸牌数列、情史追问与互纠、Michael Arklow抚发亲吻、Burn/Wade、猎犬、童年落水、衣物与铃裤腿均已译，没有再以206–207页沐浴段错置替代。
- `fw-i8-205-16`：报刊、借袋、洗浴妆饰及服装，继而完整派礼长串均有对应。逐项追到 Gipsy Lee、Chummy、Piccolina、三人拼图、Johnny Walker、Standfast Dick、Pavl、Seumas王冠、Sunny Twimjim十字架、Camilla等四人、Kate、Hosty、Coppinger、Infanta、Maggi、断头衫与绳吊带、Shemus O'Shaun地图剑邮票、众酒客、猪膀胱气球，再到 Pruda Ward 至 Marie Xavier Agnes Daisy Frances de Sales Macleay 的少女名单与月光花／血脉。此处“一千零一个”已修复，不再误用111；后续肥皂、蓝靛、圣经、碎瓷片及水流闲谈也已译。
- `fw-i8-213-11`：213–216尾段完整读到最后 `Night!`。拧衣、两岸铺衣、衣物数列、儿女去向、四老汉灰驴、灯火与告别、七房与七色、三时态、听不清、脚不动、榆树／石头对句均已译；末尾中文未补出两个 `of` 后消失的宾语。

以上确认文本覆盖有所恢复，不等于每个混合词只剩单一正确解法，也不等于下列误译可以略过。

## 实质问题

### N-01：第一问将“侵入者”换成“侵犯领地”

- 位置：`fw-i6-126-01`，126.01–129.26。
- 原句：`forbids us our trespassers as we forgate him;`
- 译句：“禁止我们侵犯他的领地，正如我们早已将他遗忘在门外”。
- 类别：漏误译／无据增补。
- 问题：`trespassers` 指人；句中 `us / our trespassers` 的关系消失，改成“我们”实施侵犯，又新添“他的领地”。这不只是《主祷文》双关的损失，而是对象与行动换位。原句戏改祷词，可保留不顺，但不能静默将人改成领地。
- 建议：重核 `forbids us our trespassers`，保留禁阻、我们、我们的冒犯者三层关系；祷词回声和不合常语处另注。删去无依据的领地。
- disposition_required: `fix`。
- blocks_integration: `true`；需要恢复人物与动作关系。

### N-02：第十一问末尾把不愿说反成急欲说

- 位置：`fw-i6-163-29`，163.29–168.14；注 `i6-brother-foot-him-out`。
- 原句：`though it broke my heart to pray it, still I'd fear I'd hate to say!`
- 译句：“纵使祈求这般结局会教我心碎欲裂，我只怕依然恨不能亲口说出那句话！”
- 类别：漏误译／正文与注释冲突。
- 问题：“恨不能”表示急欲实现，反转 `hate to say` 的不愿或难于说出口。此处紧接逐客的 `ay!` 与亲兄弟假设，尾句犹疑具有结构作用。当前同段注释已写“在否定套否定中流露出手足难断的犹疑”，正文却走向迫切说出。
- 建议：保留“只怕／恐怕”与“不忍／不愿说出口”的迟疑；如何处理套叠和未尽感可另选，不将其改为“恨不能”。
- disposition_required: `fix`。
- blocks_integration: `true`；影响十一问拒绝与十二问同一体谜底之间的转折。

### N-03：Justius 把不富有改成家底丰厚

- 位置：`fw-i7-187-24`，187.24–193.30。
- 原句：`accomplished women, indeed fully educanded, far from being old and rich behind their dream of arrivisme, if they have only their honour left`
- 译句：“她们皆是才艺双全的女子，确实受过完备教育，绝非年老色衰，在发迹幻梦背后自有丰厚家底（纵使只剩名节）”。
- 类别：漏误译／否定范围。
- 问题：译文只否定“年老”，却肯定“丰厚家底”。原句 `far from being old and rich` 的否定也管到 `rich`；后接“只剩名节”更不支持实有丰厚家底。当前中文还添入“色衰”。
- 建议：让否定明确覆盖 `old and rich`，并保留 `if they have only their honour left` 的退让／条件关系；不强定这群女子富有。
- disposition_required: `fix`。
- blocks_integration: `true`；将原人物经济处境写反。

### N-04：安娜奉食段条件句出现逆向双重否定

- 位置：`fw-i8-196-01`，196.01–201.20。
- 原句：`and if he didn't peg the platteau on her tawe, believe you me, she was safe enough.`
- 译句：“要不是他没把托盘砸在她脑门上，相信我，她才算捡回一条命。”
- 类别：漏误译／动作否定／中文。
- 问题：原句的条件是“他没有把托盘砸向她”，结果为“她还算安全”。“要不是他没……”否定整个“不砸”的事实，后接“她才算捡回一条命”，让条件与结果失配。此处应明白交代砸与未砸，不让读者靠猜想倒换否定。
- 建议：可按“只要他没把托盘砸在她……，信我的话，她就还算安全”一类句法恢复条件。`tawe` 的音形或“安全”语气可继续保留异解。
- disposition_required: `fix`。
- blocks_integration: `true`；当前条件句不能准确传递家暴动作是否发生及其后果。

## 注释限度与不阻断项

1. 新稿已撤掉旧“全标 supported”的处理，也清掉旧造词目、假 Stephan 墨水买不起之类正文。不能继续用旧附录指责这些已删内容。
2. `i6-brother-foot-him-out` 已正确指出迟疑；N-02 应让正文与其相合，不必重开整段研究。
3. `i6-cornwallis-west`、`i6-aquila-rapax`、`i6-de-rore-coeli`、`i6-cusanus-philosophism`、`i6-ubi-lingua-nuncupassit` 等已标 `uncertain` 并说明原典未核。本次未将其外部认定放行，也不因存在保守存疑就阻断正文。
4. Mercius 与 Mercury 的联系、ABC及乳品各层叠合、各河名音影等多标 `proposal`。本次不把可成立的异解、音译选择或所失的一层双关升为阻断问题；未亲核具名研究原页，不替“研究界常将……”背书。后续出版仍须把这些研究归属补成可追索出处，或改成明确的本项目推测。
5. 中文仍常用“兼”“般”“之”等解释性连接，也有长句；若要另做中文精修，应保留原句动作与刻意连缀。单纯同义措辞不列缺陷，不据此要求全章重译。

## 结论

- 当前版本：`needs_revision`。
- I.6：覆盖已实质恢复；N-01、N-02 待定点修正。
- I.7：长清单、造墨与两段独白均已恢复；N-03 待修。
- I.8：礼物全串与213–216尾段均已恢复；N-04 待修。
- 本轮未再查见旧稿成片梗概或跳段，故不据旧问题继续判为“未全译”。但四处实质误译仍在，不能写 `ready`，也不能把“覆盖已恢复”转写成“内容无问题”。
- 注释外部出处仍有上述未核范围；本报告未宣称完整出处审校通过。
- 交回整合者：对四个问题各记采用、未采用或补证依据，绑定修订稿 SHA，再作定点复核。没有修改章稿、来源、覆盖标记、断点或审校署名；没有执行推送。

## original_sha256

I-6：

- `fw-i6-126-01`：`f3fab540d81d164b781d1453fdfd1621c144b21f033c3b59a1d9411f90f6f3fe`。
- `fw-i6-129-27`：`8cc5d76cb57e8ecc29ada94f6c2d192efb23214a95b2a0e5f60f71bed511d667`。
- `fw-i6-133-01`：`2727064045752f823dc2b36966eb0f1bc8984fd805f0cb95cbfe44933cea2a25`。
- `fw-i6-136-09`：`a634f1f535e69652317af045ac1e57f629bce7e16cf12567cc93ef1ae728570f`。
- `fw-i6-139-15`：`4a3d48f3ddc275c64d45dcbd194fc53bf0240055a14619422d6448a617e6027d`。
- `fw-i6-143-03`：`ddfa4f372cc2980c527ada05abb5c822519cefa811af9570a2e081977ecc524c`。
- `fw-i6-146-17`：`5fb7a0aaa9c338bcbbafce497733c17f7852ec9e8565bbec592b754765b97507`。
- `fw-i6-148-33`：`d7325780c89062ea79bf6691de5df344e8f777d2951d07fd3df60d0d4e6e20c0`。
- `fw-i6-152-18`：`a4fdc62e7f31ebb0909fe9687e111e2dc51b3caedd4b751943a2319f066dadfe`。
- `fw-i6-157-08`：`a671d34e2bba2f4561dd548477c1fcba6ed7046e14987bd506229ee347aa7fb3`。
- `fw-i6-159-24`：`a0185e5e13ee358fe17f69904852b99749067e824e0e2ee284d19d0ba2cb84b7`。
- `fw-i6-163-29`：`38c6c0a277cc00bfe98036aa51e3a86f9b96750bc66bae98a11e517bd57f4699`。

I-7：

- `fw-i7-169-01`：`10df3630eb3d63ba96ddeddae842061bfb15e470a22633b0733846df0aa37e46`。
- `fw-i7-172-11`：`1713846dbcb3afb13ae8a451eb63379f29e20a39eb9ba4af8915bd0ca8b84fe4`。
- `fw-i7-175-29`：`b13b7e3671e7575de3a4c4380b33866cfa5cd6a6192221e6eefd126ced183369`。
- `fw-i7-180-34`：`49a6002d5990dadfdf9a7ec2c1883378682d35f5b9504b51ca00baf95e82a89f`。
- `fw-i7-184-11`：`d7f3b70fc5e050c34bb7963425f8f5de001f20de4c650d04094d6cf0c066402c`。
- `fw-i7-187-24`：`f14e17539917bb290e43ff46fc191bbd581a11e797b925ad70fb5c5363146e11`。
- `fw-i7-193-31`：`3fe2a0d1d8afbc0d443a35aa68819b5857963239a6521bafbb6f8886ef2ff443`。

I-8：

- `fw-i8-196-01`：`70056db7b12cc54ee10dc7693cf065663159cdf80cd487794e114ce387b1518e`。
- `fw-i8-201-21`：`2e525b6f0c9508cf9ecce208ecaef9d100168518051fb0f59b13050452e7c101`。
- `fw-i8-205-16`：`db28d192fafdbce647f479c5cc8556e8acd54def6c706b209472c26824014ce8`。
- `fw-i8-213-11`：`da003e44253a44e64f04cf9510445a200357f98ac72087a797cd97d7619dade8`。
