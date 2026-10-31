# 跨作品、遗传材料与跨译本：三种比较分开做

先决定比较对象和可证主张。文本相似支持列为对照，不独自证明作者有意互文、来源关系或影响方向。译者的相同选择也可能来自同一本注释书。

## A. 跨作品比较

为 Dubliners、A Portrait of the Artist as a Young Man、Ulysses、Finnegans Wake 各建对象卡。至少填 work、edition、editor_or_translator、witness_url、locator_system、exact_locator、context_scope、read_state。底本不同便另建卡，不把 FW 页行套给 Ulysses。

定位惯例须随实际版本记录：Dubliners 可用篇名加刊本页、段落锚句；Portrait 用章及版本页、段落；Ulysses 若用 episode.line，注明具体行号版，1922 年分页另列；FW 用当前见证的通行页行，并说明校订版差别。电子位置只能作为附加位置，不冒充印刷页码。

执行次序：

1. 把候选相似分成原字、声音、句法、意象、人物命名或场景结构。逐字核两边及各自邻段；不要从摘句直接推全书主题。
2. 记录差异：谁发声、动作关系、时态、否定、语体和位置。共同有河、父亲或夜，不足以独自提出借用关系。
3. 查共同外部来源、惯用语与偶合。一个稀有短语比宽泛母题更可区分解释，但仍须核版本和时间。
4. 区分首次发表、实际写作和后改日期。晚印本中的句子未必晚写；早期作品也可能在后版改过。日期不明便保留区间或 unknown。
5. 先给 parallel_observed；若有来源或遗传链再讨论 source_relation_supported。论证缺口留在 inference_gap，不用一个总置信分掩盖。

只比较本题涉及的作品，不凑齐四作；无命中只限定已搜版本与变体。

## B. 书信、手稿与笔记比较

这条线追生成顺序，不替 A 线补一段想象中的阅读心理。对象卡另添 archive、shelfmark、folio、draft_level、dating_basis、hand、transcription_editor、uncertain_readings。

把源书、笔记摘录、草稿、清样、成书列成实际可核节点；缺哪一段便留空。编者箭头、疑字、删文与补字照其说明读取。笔记旁边出现同一人名，不能自动视为当前成稿词的来源。作者事后自释也不能无条件填回所有早期稿层。

每次比较写“哪项形式如何改了”及它改变何种读法。把删去的双关留作生成史观察，不能再无条件塞进成稿正文。仅查数字转录时标 transcription_only；需要原图才能判断的笔迹或行序，就暂停该项判断。

## C. 跨译本比较

先建 translation_card：work、translator、title_as_printed、publisher、year、edition_or_printing、volume、isbn、source_edition、page、access、read_state、coverage。译者自述所据底本尚未核时，标 declared_source_edition，不改成已证底本。

逐段对齐英文、中文、日文范围。原作一段可能跨译本多页，译注也可能另册；用首尾锚句确认，不能按等长段落或数字页码对齐。只持有节译、访谈摘句或书评引句，就只比较可见范围，并标 cited_via。

分开记录：否定与动作、词义多路、声音节奏、字形版面、文化提示、正文与注释分工。每项写 retained、shifted、lost 或 added，随后给实见依据。不要以“更忠实”“更流畅”代替分析，也不因两译相同就判第三译错误。没有共同原页时不排高下。

引录只取所需短句，注明版与位置。只读评论便只谈评论，不能编译句或把评论页码冒充译本页码。自产异译署“本项目备选译法”。

## 可复制比较记录

此记录附在研究包 comparisons；实际使用填对象卡，不以示例状态充当完成。

~~~json
{
  "comparison_id": "cmp-1",
  "question_id": "q1",
  "mode": "cross_work",
  "objects": [{
    "object_id": "object-1", "work": null, "edition": null,
    "witness_url": null, "locator_system": null, "exact_locator": null,
    "read_state": "discovered", "context_scope": null
  }],
  "alignment": {"unit": "passage", "basis": null, "limits": []},
  "observed_similarity": [],
  "observed_difference": [],
  "shared_source_alternatives": [],
  "chronology": [],
  "relation": "unresolved",
  "evidence_ids": [],
  "inference_gap": [],
  "translation_impact": null
}
~~~

mode 可用 cross_work、genetic、translation。relation 可用 parallel_observed、source_relation_supported、relation_rejected、unresolved；这只是研究判断，不能直接替换章稿 certainty。即使取得借阅卡，也不能由“可能读过”跳到“此句取自”。

## 退出与失败

缺任一比较对象的版本、实际位置或文本时，不交“完成比较”；交缺项和可执行下一步。只有宽泛相似时缩窄为对照事实。论证被反例削弱时保留否定结果及修正，不把旧结论悄悄移入脚注。比较无需强迫原作消歧；若译法须择一路，明说取舍与损失。
