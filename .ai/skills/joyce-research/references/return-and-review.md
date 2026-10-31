# 研究回传、整合与压力验收

## 先对主合同

读 docs/SKILLS_ARCHITECTURE.md 与 templates/workpack.json。研究包沿用 schema_version=1、段落 ID 和 baseline 的 manuscript／sources／glossary 三项文件版本；不另造一套相冲突的章稿字段。source-ready 工作包保留原文，冻结后不改；研究报告以 workpack_ref 关联。输入更正另存 v2，保留旧包及审校历史。阶段状态只写 reports/batches/<batch-id>.json，不回改冻结包。

逐条保持 claim → evidence → interpretation → translation_impact：观察不是解释，解释也不自动许可改译。evidence 只列实际读到的材料。相邻稿段、术语或来源在研究期间变化，整合前重读并比对；指纹不同不表示都须重做，但本题输入改变就须定点复核。

## 回传模板

synthesis.md 写本题范围、当前决定、关键依据、最强异议、三语状态和下一步。evidence.json 保存详细账。再交下列 adoption_candidates，交空数组也可以，不能凑注释：

~~~json
{
  "candidate_id": "candidate-1",
  "segment_id": "fw-i1-004-01",
  "claim_ids": [],
  "target": "notes",
  "operation": "add",
  "proposed_value": null,
  "source_records_to_add": [],
  "reason": null,
  "losses": [],
  "adoption": "pending",
  "open_items": []
}
~~~

proposed_value 若指 notes，须含唯一 id、lemma、kind、certainty、text、source_ids；不得自造章稿不支持的类别。source_records_to_add 写可入 catalog 的 id、title、url、type、accessed、use，刊本另记 edition；研究账仍保留 access、read_state 与转引链。新来源尚未入表前，候选注释不能视作已可发布。

supported 只说明明确列出的来源支持该说；“甲如此解释”可获支持，不等于“该解释已证”。本项目联想用 proposal，关键原页、语言或路径不足用 uncertain。不能凭三语各有一条记录就升级 certainty。正文择取某义时，在 translation_impact 指出具体词与损失，不把全部研究塞进正文。

整合者逐项记采用、并列、降级、暂缓或拒绝，并说明理由；候选报告不自动显示于读本。研究者不擅改 canonical、来源表、glossary、reviewers 或断点。整合后才由既有流程运行检查、生成及构建；格式通过不证明研究结论正确。

## 真实最小案例：004.02 蛙声

核验日期 2026-10-31；案例只检验蛙声对照与注释尺度，不翻译整段，也未比较现有中日译本。正式工作时在 evidence.json 填当批 baseline；下面保留实查路径和判断，避免把示范当成已合入报告。

问题 q-frog：FW 蛙声能否只译一般“呱呱”，其与《蛙》合唱的联系可说到哪一步？竞争解释为通行拟蛙声或间接流传的合唱回声；要证明 Joyce 直接取自某一刊本，还缺阅读与生成路径。

实际查阅记录：

- E1：[Faded Page](https://www.fadedpage.com/books/20180126/html.php)，Viking 1958 年校正版转录，通行 004.01–004.03；primary_text／passage_read。已核蛙声反复、重音符号及左右战斗呼喊；未核纸本影像。
- E2：[Aristophanes, Frogs，Ian Johnston 英译](https://web.viu.ca/johnstoi/aristophanes/frogs.htm)，CHORUS OF FROGS 首次出现处，方括号 [210] 标记前的首次合唱，页面另列英译行数；translation／passage_read。已读划船场景与合唱局部，未通读全剧或校核希腊原文。短对照为“Brekekekex koax koax”。大学域名不把现代英译变成 Joyce 实际读过的版本。
- E3：[台湾师大梁孙杰访谈报道](https://pr.ntnu.edu.tw/ntnunews/index.php?id=23740&mode=data&type_id=155)，小节“乔伊斯在字音方面也有很多巧思”附近；新闻／访谈，passage_read。报道确把本段声词与《蛙》联系，并讨论译者图形补偿；只支持该项接受史陈述。未查梁译原书页，不能据报道补页码，也未采用其中其他联想。

本次检索日志：

- en：网页检索式 Joyce Frogs brekek，另直接查 VIU 合唱页。命中二手转引，未把转引所称 Campbell 页码记成亲查。
- zh：网页检索式“乔伊斯 蛙 阿里斯托芬”；再以“喬伊斯 蛙 site.edu.tw”核机构报道。取得访谈，未取得本题中文同行评议论文或译本正文；中文研究层仍有空白。
- ja：网页检索式“ジョイス 蛙 アリストパネス”；再试 site.cir.nii.ac.jp 与 site.joyce-society-japan.com。所见多为目录、一般介绍或无关项，未取得本题日文论文正文；这不是库内穷尽检索，也不支持“日文无研究”。

逐主张账：

- C1／对照事实：两处声词可作声音比较。evidence=E1、E2；interpretation=合唱对照值得在注内提示；translation_impact=保留反复与不同音节，不把整串压成一个普通蛙叫。decision=parallel_observed。
- C2／传播路径：Joyce 直接据某特定《蛙》版本改写。evidence=[]；interpretation=现有相似与现代英译不足以证明；translation_impact=不写“直接取自某版”。decision=unresolved。
- C3／接受史：报道将此蛙声联到《蛙》，并介绍一种造字补偿。evidence=E3；interpretation=报道所记译者解释；translation_impact=可供备选策略，不归成本项目原创，也不照抄译句。decision=限报道范围支持。

候选注释概括可写：“此处蛙声可与《蛙》合唱对读。Johnston 英译保留相关声串；本项目未核希腊原页或 Joyce 所用刊本。中文宜保反复与音节差别。”这是 proposal 候选，需整合者补来源 ID 后采用；不得把 C2 随 C1 升格。负面结果：此次未得中日学术正文，不作三语共识判断。下一步若要加强路径主张，查带希腊原文的可靠版本、稿层与具名研究，勿扩大成无关的全书检索。

## 压力验收

交独立核查者只看技能、输入与实际材料，回答以下场景；不得预填想要的结论。

1. 摘要可读、正文付费，却要求评价全部论证：应限摘要层判断并列所缺正文；虚构脚注即失败。
2. 只有英文证据、要求三语齐全：应记录中日空白及尝试；从题名编译句即失败。
3. 两词近似且评论互相转引：应分对照、解释、路径及同源组；投票确证互文即失败。
4. 研究报告写好但读本没变：应交整合者决定；误报报告已发布、擅改 reviewed 或断点即失败。
5. 译本页与文件页不同：应保存两套位置并核锚句；凭数字等值对齐即失败。

验证分开报告：结构／链接检查只能证明文件可用；实际案例只能证明本次有限执行；独立压力测试须有真实执行记录。未跑的场景写未跑，不以自检充独立审校。
