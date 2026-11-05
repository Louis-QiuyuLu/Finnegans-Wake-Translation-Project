# III.3、III.4 定点修订与自检

本轮按维护者授权回写章稿，保留初译。先独立读Gemini交稿，再定点修订；以下复核属于修订者自检，不冒充人工审校或另一位执行者复核。

## 输入与证据界限

- 入口：AGENTS.md、EDITORIAL_GUIDE、SOURCES、MANUSCRIPT_FORMAT；translate-chapter、roles及review-translation、review-protocol。
- 基线：reports/reviews/inputs/books-II-IV-20261105/manuscript/chapters/。两章修订前字节均与冻结输入相同。
- Gemini处置账：冻结根reports/revisions/gemini-book-III-disposition-ledger.json。本轮只作来历索引；resolved、标题或issues_count不当作已核证明。
- 原文字据：每段original及同章source_text；外部词源、历史人物、宗教典籍、制度史未检索，相关旧说缩窄或标uncertain。joyce-fp仅支持出现字词，不足以证明外部史实。
- 比对完整英文时先解析HTML实体，去空白与页码标记；III.3仅见24处连字符，III.4仅见6处连字符差别，未见其他字面差别。详见source-comparison.json。本轮不改original或source_text，也未独立重划页行。

## 修订要点

- 补回整串漏译：III.3的479、484、489、494、524、529、534、539、544、549起段；III.4的576、581、586起段。补正文，不用剧情概要顶替问答、服饰、货币、地名或神学论辩。
- 纠正否定与方向：not to forget、if it does not occur again、turn a Roman、as much sinned against as sinning、either man or mouse。
- 撤亲属及法律增写：halfbrother不擅定同父异母；quarterbrother不改表亲；darling不改女儿；撤嫡子、确切服役惩罚与无息票据等无据细节。
- 补Vulva四次、WXYZ/PQRS两组字母、原文点字空缺、地点人名与若干数字。
- 全部144条旧注逐条读取；撤未独立核实的page_col_line，避免旧精确数字冒充定位。保留段级locator与range。外说标待核，若有明确误导则改写，例如Gels不是已核德语少女、Marcantonio不能凭同名认定雕版家及入狱事由、Big Butter Boost不指定广告机构。

## 逐段范围与处置

### III-3

- 修订前SHA256：`f658b10842bfa5c0ac755cf657d20e835a0a47c5b660d77225c9ad337995a0a7`
- 修订后SHA256：`7208c10f5e570bca629fb8097e9d4122933e95c6be8cc1d96eb913975bd0a824`

- `fw-iii3-474-01`（474.01–478.36）：全文、译文及6注已读。gloaming是暮色，不补破晓；darling only one未指明女儿，撤去亲属增写。注释处置及原/新文本见actions.json编号1,2,54。
- `fw-iii3-479-01`（479.01–483.36）：全文、译文及6注已读。Vulva四次重复不是圣女纯洁；补Shaum/Sameas后的连续盘问及答复；hand纠正为笔迹；everliking a liked不支持彼此相斥。注释处置及原/新文本见actions.json编号3,4,5,55。
- `fw-iii3-484-01`（484.01–488.36）：全文、译文及6注已读。补整段Bruno/Nola问答，保留对立循环，不以概述代替；补两组字母，不能压成四字母；432无年份单位，不擅添年代。注释处置及原/新文本见actions.json编号6,56,78,79。
- `fw-iii3-489-01`（489.01–493.36）：全文、译文及6注已读。halfbrother不能在此擅定同父异母及异姓；补去名目和押韵歌及其后问答；撤无据情报剧情。注释处置及原/新文本见actions.json编号7,8,57。
- `fw-iii3-494-01`（494.01–498.36）：全文、译文及6注已读。补议会排拒、童谣及转回父亲的整串问答；撤无据铜币奉献情节；not to forget否定反转。注释处置及原/新文本见actions.json编号9,10,58。
- `fw-iii3-499-01`（499.01–503.36）：全文、译文及6注已读。本次主动作与问答对照未见须补大段；不因风格偏好整段换词。注释处置及原/新文本见actions.json编号59。
- `fw-iii3-504-01`（504.01–508.36）：全文、译文及6注已读。保留原文5 pints 73与族裔指控，不以非常规血液抹除。注释处置及原/新文本见actions.json编号11,60。
- `fw-iii3-509-01`（509.01–513.36）：全文、译文及6注已读。保留heirs/years重叠，不只保年龄；watching brief非已提交辩护状，与注释一致。注释处置及原/新文本见actions.json编号12,61,80。
- `fw-iii3-514-01`（514.01–518.36）：全文、译文及6注已读。不以概述替换原文点字空缺；补unleventh十一月词形。注释处置及原/新文本见actions.json编号13,14,62。
- `fw-iii3-519-01`（519.01–523.36）：全文、译文及6注已读。补as much sinned against as sinning双向关系。注释处置及原/新文本见actions.json编号15,63。
- `fw-iii3-524-01`（524.01–528.37）：全文、译文及6注已读。补智慧愚妄问答、三人/两女及母亲指代、迷恋与照水自赏；撤无据诺拉身份。注释处置及原/新文本见actions.json编号16,64。
- `fw-iii3-529-01`（529.01–533.36）：全文、译文及6注已读。还原less than a seventh pro mile，不擅添水；turn a Roman方向译反；补厨房、衣装、舞蹈拟声与收台重开盘问整串漏译。注释处置及原/新文本见actions.json编号17,18,19,65。
- `fw-iii3-534-01`（534.01–538.36）：全文、译文及6注已读。Lapsang不是立顿品牌；Nine dirty years中ninety回声；九十岁老翁，不断言九岁；true thousand保two thousand回声而不膨胀为千万；补贫屋死亡、雪茄亲族、酒馆、老少形貌与自述转折；if it does not occur again否定不得删；保原文反常威胁；quarterbrother不可擅定表亲。注释处置及原/新文本见actions.json编号20,21,22,23,24,25,66。
- `fw-iii3-539-01`（539.01–543.36）：全文、译文及6注已读。补税赋、货币、宗派战事、军事委任、城防与施惠自夸连续漏译；closet在住所卫生清单语境是便所。注释处置及原/新文本见actions.json编号26,27,67。
- `fw-iii3-544-01`（544.01–548.36）：全文、译文及6注已读。carried out未写抬出棺木，撤增写；补完整纹章、箴言、群婚/合制/三二一论及同时存在声明。注释处置及原/新文本见actions.json编号28,29,68。
- `fw-iii3-549-01`（549.01–554.10）：全文、译文及6注已读。rest from平行两组主客，不将异教徒变为王子所属；bissed/trissed返场喝彩非嘘声；补Jelupa名目；补原稿以省略号抹去的服饰、施济论、船运、厕所、大学碑塔、街道及选举完整长串。注释处置及原/新文本见actions.json编号30,31,32,33,69。
### III-4

- 修订前SHA256：`805aa1c9058804c4d6d45f021469160bb74db6cd386b6391124c3b80247c9bbc`
- 修订后SHA256：`f89563089e6ede302a1d111552b76f6f32f0243e7edc9789390f2e41299c2f1a`

- `fw-iii4-555-01`（555.01–559.36）：全文、译文及6注已读。补另一罪名deretane denudation的露臀内容；不抹去选择关系；撤无据劳役与国王五世身份；eight and eight sixtyfour未标秒；保棋盘数字不增时长；cankle此处为candle变形，不能抬脚踝照见楼梯；lovers lost property offices失物招领，不是失窃情人物业。注释处置及原/新文本见actions.json编号34,35,36,70,81,82。
- `fw-iii4-560-01`（560.01–563.37）：全文、译文及6注已读。保brooder/cissiest/auntybride亲属词叠置，不只变恋人；补齐童谣名目；either ...or不得译为既非；flesh非飞禽。注释处置及原/新文本见actions.json编号37,38,39,71。
- `fw-iii4-564-01`（564.01–567.36）：全文、译文及6注已读。本次主动作与问答对照未见须补大段；不因风格偏好整段换词。注释处置及原/新文本见actions.json编号72。
- `fw-iii4-568-01`（568.01–571.36）：全文、译文及6注已读。mic/mac/mick并列保原文，不增嫡庶及确定兄弟身份。注释处置及原/新文本见actions.json编号40,73。
- `fw-iii4-572-01`（572.01–575.36）：全文、译文及6注已读。is considered不是法庭既成裁决；保to lowest degree字面，不额外定亲等近远；明确when converted所指未来婚配人，避免把安妮塔当归化者；ordinary教会语境不当司法常任法官；without issue未写无息；保无所出双关。注释处置及原/新文本见actions.json编号41,42,43,44,45,74。
- `fw-iii4-576-01`（576.01–580.36）：全文、译文及6注已读。property in corpse关乎将尸体作财产，而非尸骨主体产权；lame of his ear无腿瘸，不转交身体属性；补原稿以省略号切掉的两位肖像、灯、服饰、售卖与地名行程；撤把戏拟mamy mancipium当真实母亲家父权制度。注释处置及原/新文本见actions.json编号46,47,48,75,83。
- `fw-iii4-581-01`（581.01–585.36）：全文、译文及6注已读。补省略号抹掉的双子女儿、骑乘、行星流言、洪水藏处、售蕾与巡警整串正文。注释处置及原/新文本见actions.json编号49,76。
- `fw-iii4-586-01`（586.01–590.30）：全文、译文及6注已读。补弗雷德/詹姆斯西娜的动作、酒单、吉米应答及海点回顾/天气问句；a dozen generations anterior to themselves不是数十代；the infidels复数指潜逃两人，不指被留下者；Tag为收尾舞台语，撤去无据天明；不把末句扩成封闭宏观解释。注释处置及原/新文本见actions.json编号50,51,52,53,77。

## 验证与未决

- `python3 scripts/project.py check` 已通过：17章、177段、1088注；格式检查不证明译义无误。
- 另核：两章章级字段、source_text、全部ID/坐标/source_id/original/draft/alternatives未改；reviewers全空，status为revised。只改分配章稿与本报告目录。
- 各段已完成本轮全文主干对照与定点修订；Joyce声形叠合、跨作品互文及外语词源并未全部解定。未核外说仍须研究；AI补译也仍待另一执行者复核。不得据本报告写reviewed或宣称全部典故已证。
- 本轮不改coverage及coverage_review，不推进进度，不生成派生文件，不提交、不push。整合者须读取实际差异，再统一构建与检查。
