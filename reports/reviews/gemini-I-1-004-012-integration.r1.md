# I.1 / Gemini 整合修订第一轮定点复核

## 输入

- role: ai_review
- executor: Codex 子代理 /root/review_project；AI 定点复核，不作人工审校署名。
- 日期：2026-11-01；revision_round: 1。
- draft：manuscript/chapters/I-1.json；SHA256：`fabf34db40630589d45bed2910c0797056fbdfb729ca6108653a9fc24b44a7f1`。
- sources：sources/catalog.json；SHA256：`4061d25afc979fe53755c4096e73d6467234c8397751be1cfd9e561129242937`。
- glossary：glossary/terms.json；SHA256：`46e5486f2e52f7aabd7758c1aa202fe7d3df71c81ed3aa950910be03bb095f96`。
- 前轮报告：reports/reviews/gemini-I-1-004-012-integration.r0.md；SHA256：`226e827c8022c7083096f447c465695f50cd1c3292cbb97f3c3940dbbc92d5aa`。
- r0 冻结输入：reports/reviews/inputs/gemini-I-1-2026-11-01.json；SHA256：`cb66a5d482281284b8e422766cd4dd07fc0131f31d79456e27651363402ec2d1`。
- source_id: joyce-fp；本轮保留的新译文字范围为 004.01–008.04，合并后七个对象。旧第 3 页三段未改。

## 范围与方法

本轮只核 R0 问题处置、合并与隔离结果，以及本轮改动是否引入漏字、漏注、初译覆盖或状态错误。不扩大三语研究，不重译全段。底本事实与外部文献沿用 R0 已核依据；本轮没有重新浏览原书、手稿或论文。

实际比较新旧 original、draft、translation、修改注释、相关来源条目、隔离稿和断点。另用字段比对确认：两组原文按旧稿顺序合并；除 ah 逗号、shoutmost、Brunto 三处已批准录文修正外，没有其他新增原文变化。两组合并后的 draft 各保留原两份初译，以空行衔接；注释 ID 与顺序完整。初译未遭采用稿覆盖。

未独立重核 TTS 文件、拼接音质、全站构建或播放器代码；音频清单由父任务另行验收，不纳入本报告的通过范围。

## R0 问题处置

### R-01：隔离有效，原稿质量问题仍留待修

fw-i1-008-06 已从公共章稿移除。reports/quarantine/fw-i1-008-06.json 与 r0 冻结对象逐字段相同，未借移目录改写或伪称修好。公共稿不再发布混录博物馆段。

- disposition: 隔离；本轮发布范围解除阻断。
- blocks_integration: false（仅对截至 008.04 的公共稿）。
- 仍未解决：隔离稿整句插入、替换、漏录及相应中文须另行修复；不得恢复即发布。

### R-02：共行范围与断点已修

005.13 与旧 005.27 合成 005.13–006.12；006.13 与旧 006.32 合成 006.13–007.15。原文顺序完整，没有为规避重叠而跳过共享物理行。保留对象仍用 fw-i1-005-13、fw-i1-006-13；旧对象可追 r0 冻结输入。

fw-i1-007-16 已改为 007.16–008.04。checkpoint.next 为 [8,5]，锚句为 Penetrators are permitted into the museomound free.；没有越过隔离缺口。公共章稿仍标 partial，不称整章覆盖完成。

- disposition: 已解决（公共稿范围）。
- blocks_integration: false。
- 隔离稿中旧坐标不充新底本证明；恢复时仍须重录重核。

### R-03：录文及中文对应已修

005.11 恢复 ah 后逗号；合并稿用 shoutmost；007.22 第二处恢复 Brunto。中文也分别保留布龙托、布伦托，未把两种原拼重新合成一个名字。

- disposition: 已解决（公共稿范围）。
- blocks_integration: false。
- 010.24 起隔离稿的细项未修，不属于本轮已放行范围。旧 007-16 音频未列入新清单；本报告未亲自核音频文件。

### R-04：撤回无据定址

正文以巴罗诺斯音译 baronoath，不再写拉斯法纳姆。i1-shopalist 改为 proposal，删完全重合的断言，并明说具体对应待核、不能作严格地图。没有把社区 Howth 线索直接替换成另一项地理定论。

- disposition: 已解决；地名研究限度保留。
- blocks_integration: false。

### R-05：撤回错误署名及未核图版细节

i1-seepeegee 改为 uncertain；移除 Atherton 考定、木雕材质及唯一图像、发现者等断言，只保留 pg 88 读路与社区所提 Moret 线索。moret-egypt.use 明说原交稿曾声称核页，本轮不能把它当作已查图版的证据。

这次没有另行编填 Slomczynski 或 Troy 原页；未核原书和转引原文的局限仍在。正文第八十八页可作为已明示限度的试译保留。

- disposition: 已解决（错误署名与查阅夸大）；原页核验仍待研究。
- blocks_integration: false。

### R-06：伪 HCE 藏头已撤

i1-fatherfornicationists 改为 proposal，明确该词串不组成 HCE 藏头，也不凭此确认人物身份。其余声形只作为本项目读路。

- disposition: 已解决。
- blocks_integration: false。

### R-07：颜色矛盾已修

正文改为日轮承第二色、映作银白，不再添金。i1-scutschum 说明第二色回指 argent，helio 日轮声影另标项目判断；没有借颜色修正宣称其余纹章词源全获验证。

- disposition: 已解决。
- blocks_integration: false。

### R-08：provost 主体已恢复

中文保留那位长官及嘲弄动作。i1-nabir 说明具体人物待核，把 between／Bedouin 声影留在注内，不再用游民取代长官身份。

- disposition: 已解决。
- blocks_integration: false。

### R-09：来源与解释层级已拆开

quran-tur-48-49 指向具体经句；tirmidhi-877 指向圣训。i1-whitestone、i1-sustainer 只作文本对读，不以平行措辞宣称 Joyce 取材路径已证。cubehouse、nabir、ansars 等未核词链改为 proposal。quran-arafat.use 也承认首页不能担保整串典故。

- disposition: 已解决（本轮约定的出处边界与分级）。
- blocks_integration: false。
- 仍未核：神名、洁齿木、全部阿拉伯语等语词链及具体传播路径；本轮没有把它们重新升级为事实。

### R-10：Dunne 错链已纠正

dooley-hennessy 改为 Gutenberg 22537；记录首刊 1898 年与所据转录扉页 1899 年，限定仅核序言末部、ON STRATEGY 开头两人关系，并撤回旧 10803 错链。条目明示原书不能单独证明 Joyce 每处互文。

- disposition: 已解决（来源记录）。
- blocks_integration: false。
- i1-mrdooley 所在段仍隔离；不能因换对来源链接就恢复该混录段。

### R-11：指定解释已限缩，来源性质已更正

已逐项复核 i1-brekkek、i1-stutteringhand、i1-buildung、i1-cropherb、i1-shize、i1-teetootal、i1-mastabatoom、i1-priamolim、i1-graceglutton、i1-finnagain、i1-phoenish：均改为 proposal 或 uncertain；删去原词已核、特定正式礼文与全书谜底已定等断言，保留实际缺证范围。Cropherb 中文也从嚼草巨兽限缩为嚼草者，没有留下依赖唯一巨兽指认的正文。

bylina-buslaev 改成百科条目及检索线索，明确未核古俄语史诗；ibsen-solness.use 限 Archer／Gosse 英译与题录，不再声称查过挪威语原文。

- disposition: 已解决（指定各项降级与来源层级）。
- blocks_integration: false。
- 这不是对全部其余 supported 注释的逐项外证认证；R0 未核范围继续保留。

### R-12：末段隔离有效

reports/quarantine/fw-i1-010-25.json 与 r0 原对象逐字段相同，已从公共章稿撤出；当前断点未跳过前段缺口。

- disposition: 隔离；本轮发布范围解除阻断。
- blocks_integration: false（截至 008.04 的公共稿）。
- 仍未解决：隔离稿的词形、身份、数字与历史指认须另行定点修订，本报告不授予其通过。

## 回归检查

本轮未见修订引入新的阻断问题。核对结果：

- 旧 003 页三段逐字段不变。
- 新公共稿保留七个对象，原文合并无遗漏；全部注释 ID 与原顺序保留。
- draft 保留初译；translation 承接本轮修订。合并没有把修订稿回填为初译。
- 保留的新增对象均为 revised，reviewers 为空；未冒充人工 reviewed。
- 两段隔离稿未混回公共章稿；所有公共注释 source_ids 均可解析。可解析只作为关联检查，不代替来源支持判断。
- 连续范围止于 008.04，下一坐标 008.05；coverage 仍为 partial。

## 结论与限度

- 当前版本：**ready，限 R0 已列问题的第一轮定点复核，以及截至 008.04 的 revised AI 试译**。
- R0 的公共稿阻断项已经修正或由撤出范围解除；隔离原稿的问题没有因此解决。
- 仍未逐条核实所有词源、语言能力相关判断、地方史、歌谣、手稿、图版和中日译本。原页图符也未复原；不得称本稿已完整保留底本版面符号。
- 不授予整章完成、全部注释经外证认证或人工审校状态。构建、网站、TTS 文件与音质由相应验收记录覆盖。
- 本轮不要求第二轮整段修订。后续新证据或改变解释时，再绑定实际新输入定点复核；不能沿用本报告替更改后的稿件背书。

## 所核原文字串指纹

- fw-i1-004-01 / 004.01–004.17：`b42f8443789a4b58c65a1c6445c8b80d48c3cfc3a7691753f41fded0b8d9f85e`。
- fw-i1-004-18 / 004.18–005.04：`bb09224e3a9830a229ff4a461dfc38be5d1e6b1541f995f5918b94bb5e1d8103`。
- fw-i1-005-05 / 005.05–005.08：`60a21d444f247e892baff7cc6a4a9cbbf8246b6107c0b92d66cadf7e2aabadfd`。
- fw-i1-005-09 / 005.09–005.12：`4ca62d55ec175629155d57818c540c9743098e1d2846831c28e65d6d9bd78d60`。
- fw-i1-005-13 / 005.13–006.12：`0011e071c878a9b1a9a9b9c77008ed40b0fc1791316be79ab837a8a4b5f56085`。
- fw-i1-006-13 / 006.13–007.15：`80b5e6e0b60464f8bdecc17684862e8ae35bbac40bec9c5977dafd7b0347f311`。
- fw-i1-007-16 / 007.16–008.04：`69fa1a801b388ed9c59114b585251f99c42877441068f483f6bbfd4f893f67df`。
