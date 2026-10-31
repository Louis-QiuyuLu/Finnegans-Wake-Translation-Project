# 问题工作包、查阅层级与逐主张证据账

供全部研究使用。路径从仓库根目录起算；研究包须关联 docs/SKILLS_ARCHITECTURE.md 所定 schema_version=1 工作包及 baseline 三项版本。建议每批存 reports/research/<segment-id>/workpack.json、evidence.json 与 synthesis.md。目录只是本技能交接格式，不会自动进入读本。

## 先拆问题，再找资料

记录触发疑问的原词、左右句法、重复声音与现有译法。把问题写成能由材料区分的选择。例如“这个词能否同时保留否定与重来”，比“替回环理论找引文”可检验。先核否定、主语、动作与时态；宏观主题不能替代句法。

每题列当前假设与最强竞争解释。两说都能解释的现象，不能区分两说；另查惯用语、共同来源、抄录、排印与偶合。

检索前写支持条件、削弱条件与译法所缺材料。反例出现后保留旧假设及修正；无直接证据便保多义，不以断言填空。

## 两条轴分别记

来源性质与阅读程度不能混成单一分数。机构托管证明来源可追，不自动保证解释正确；社区转录可能传递真实信件，却仍不能冒充查过手稿。

来源性质用以下标签，可并列，但每层主张须分清：

- primary_text：作品本身，注明刊本、印次、编辑、文字见证；扫描、转录和校订读本分别记。
- author_statement：可定位的书信、访谈或作者说明。核日期、收件人、写作阶段、所谈范围；自释不自动证明外部史实，也不穷尽作品意义。
- genetic：笔记、草稿、打字稿、清样、校订层。区分原物、影像、编者辨读及补写，保存馆藏号和稿层关系。
- scholarship：具名论文、专著、学位论文或编辑论述。书评、会议摘要、新闻与同行评议论文不得混称。
- reference：词典、历史地图、目录、曲谱等。核适用语言、时代和释义范围，不能凭现代词典反证早期用法必不存在。
- translation：译文、译者序跋与译注。可证明译者怎样处理，不能直接证明 Joyce 原意。
- community_lead：维基、读书会、论坛等。先找它所引原出处；找不到便保留转引链和不确定性。

可访问程度 access 使用 online_full、partial、metadata_only、abstract_only、paywall、login_required、unavailable。它回答现在能取得什么，不回答读完多少。

实际阅读 read_state 使用 discovered、metadata_read、abstract_read、passage_read、full_text_read、blocked。读过论文中相关三页，写 passage_read，另列 read_ranges；不能因全文可下载便写 full_text_read。搜到一段摘要，只能概括摘要明说的论点；不能据此复述论证过程、脚注或反例。

PDF 有封面、目录、书评或审查要旨时，先辨文种。记录 printed_pages 与 file_pages，避免把文件第 4 页称为论文第 4 页。OCR 只算检索层；关键引文、重音、删改或生僻字须看影像。没有影像便标 transcription_only 或 ocr_unverified。

## 工作包字段

下面可直接复制。空数组表示尚未取得，不代表查无材料；null 表示尚未知。填真实值后交接，不保留示例问题当作研究结论。

~~~json
{
  "schema_version": 1,
  "workpack_ref": "reports/workpacks/fw-i1-003-04.json",
  "baseline": {"manuscript": null, "sources": null, "glossary": null},
  "package_id": "fw-i1-003-04-research",
  "segment_ids": ["fw-i1-003-04"],
  "witness": {"source_id": "joyce-fp", "locator": "003.04–003.14"},
  "scope": {"question_ids": ["q1"], "languages": ["en", "zh", "ja"], "exclusions": []},
  "questions": [{
    "id": "q1", "lemma": "passencore", "question": "否定与重来能否并存？",
    "hypothesis": "两层同时参与句法", "alternatives": ["只需通常否定便可解释"],
    "would_support": ["可定位的作者自释与现行句法相容"],
    "would_weaken": ["自释仅适用于已删稿层"], "translation_impact": "核还未与再返能否同留"
  }],
  "language_passes": [], "queries": [], "source_records": [],
  "evidence": [{
    "evidence_id": "e1", "source_id": null, "exact_location": null,
    "read_state": "discovered", "observation": null,
    "relation": "context_only", "scope_limit": null
  }],
  "claims": [{
    "claim_id": "c1", "question_id": "q1", "claim_text": null,
    "claim_type": "interpretation", "evidence_ids": [], "counterevidence_ids": [],
    "interpretation": null, "reasoning": null, "remaining_gap": null,
    "independence_group": null, "decision": "unresolved", "translation_impact": null
  }],
  "comparisons": [], "negative_results": [], "open_questions": []
}
~~~

baseline 实填各项 path 与 sha256，承接当批固定输入；示例中的 null 尚不能通过交接验收。研究稿不另抄整段 original，以 workpack_ref 回到已核底本包。

language_passes 每项记 language、scope、status、limitations。status 可用 searched、blocked、not_requested；不能把 blocked 写成 searched_no_results。queries 每项记 question_id、language、入口 URL、精确检索式、筛选条件、日期、实际查看结果范围及下一步。无需伪造完整命中数；界面不显示便记 null。

source_records 每项至少含 source_id、title、creator、date_or_edition、language、stable_url、accessed、source_kind、access、read_state、read_ranges、locator_system、transcription_status、cited_via 与 limitations。署名未知写 null；不把网站机构误填论文作者。来源表将来可简化，研究账必须保留查阅层级。

## 一条主张一条账

claims 每项写：claim_id、question_id、claim_text、claim_type、evidence_ids、counterevidence_ids、interpretation、reasoning、remaining_gap、independence_group、decision、translation_impact。claim_type 区分字面事实、词义、历史事实、作者自释、编辑辨读、解释及互文主张。复合断言拆开，不让可靠前半句替后半句担保。

evidence 每项写 evidence_id、source_id、exact_location、read_state、observation、relation、scope_limit。relation 用 supports、contradicts、qualifies、context_only；网页提过相同名字而没有谈当前词，通常只是 context_only。短引文另记 quote 与 quote_language；不必为每项复制原句。

同一论文在两个数据库出现，只算一个文本。中文论文转引英语专著，日文文章又转引同一专著，须放进同一 independence_group；先追源，再判断各家是否另有论证。原著与评论不作简单票数比较。没有读到某位学者本人文字，只能写“甲文转引乙”，不能写“乙证明”。

## 异议与负面结果

每个实质判断保留最强异议及处理：接受、部分接受、证据不足、与当前问题无关。论点不同不等于错误；异文、研究对象或术语口径可能不同。无法定夺时交并列读法与各自后果。

negative_results 写 query_id、查阅范围、结果、局限与可再查路径。“在某入口按这些变体未找到相关记录”只限定本次搜索；不能写“日文没有研究”“早期作品从未出现此词”。正文不可得写访问失败，不写反证。排除一说时须说明哪条证据与它矛盾；沉默通常只表示缺证。

负面结果要交可重走的范围与下一步，不只写“待考”。无足够支持时缩窄结论、降级注释或删无据解释。
