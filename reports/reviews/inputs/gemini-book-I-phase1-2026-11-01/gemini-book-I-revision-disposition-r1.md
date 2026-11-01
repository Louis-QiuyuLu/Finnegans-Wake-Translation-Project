# 第一卷审查整改与专项处置报告（r1）

> [!IMPORTANT]
> **审查结论完全接受与推送绝对封冻**：完全接受 2026-11-01 审查报告（审查基线 `de234d723304a2fa8d39ccbc2a3a438ab1e95cfe`）结论 `needs_revision`。当前候选不作为第一卷完整译文发布，**绝不向远程分支推送任何改动**。公共章节目录已回退至干净基准，第一章保持线上已核稿件，候选稿件完整封存于 `reports/reviews/inputs/gemini-book-I-2026-11-01/` 留存待修。

---

## 一、 第一项整改：公共 I.1 全量合入与验证闭环

已完全合并已上线 I.1，彻底排除了此前误交的旧版 31 段草稿：

1. **章稿与指纹统一**：
   - `manuscript/chapters/I-1.json` 全量采用公共稿（26 个分段，SHA256: `993815845fe516ce6de4baf4c1ee2b10fce85fe752a90cb91e165982b713e609`）；
   - 保留全部 26 段正规切分、Troy 署名与 Moret 1911 图版考证；
   - 启用 `source_figures` 原文特殊符号系统，准确呈现 006.13 处向左旋转 90 度的 `E` 字符号（`〔E向左旋转90度〕` / 内联 SVG）；
   - 便读稿 `translated-md/I-1.md`、`raw-md/I-1.md`、`polish/dev/I-1.md`、`annotations/I-1.json` 与 `progress/chapters/I-1.json` 全部同步回写。
2. **音频指纹修复**：
   - 同步 `audio/index.json`，原文字串哈希精确匹配 `fw-i1-005-09`、`fw-i1-005-13` 与 `fw-i1-006-13`，消除了此前验证器的 3 条报错。
3. **来源表补全**：
   - 在 `sources/catalog.json` 补齐公共稿所需的 3 项学术与典籍出处：`troy-osiris`、`tirmidhi-877`、`quran-tur-48-49`。
4. **验证与测试**：
   - `python3 scripts/project.py check`：检查通过；
   - `python3 -m unittest discover -s tests -v`：31 项单元测试全绿通过；
   - `python3 scripts/project.py build && python3 scripts/project.py check-artifacts`：构建通过。

---

## 二、 断点修正与公共稿隔离

1. **清除混杂跳卷断点**：
   - 彻底删除将断点伪推至 II.1（219.01）及错配锚句的无效声明；
   - `progress/checkpoint.json` 与 `progress/RESUME.md` 规范重置为从 I.2 起始位置（`030.01`）续接，锚句确定为：
     > `Now (to forebare for ever solittle of Iris Trees and Lili O'Rangans), concerning the genesis of Harold or Humphrey Chimpden's occupational agnomen`
2. **公共目录基线恢复**：
   - 公共目录 `manuscript/chapters/` 中，除 I.1 保持完整外，I.2 至 I.8 均恢复为未开始状态（`coverage: not_started, segments: []`），绝不混入未通过审查的半成品与梗概段落；
   - 候选各章完整保存在 `reports/reviews/inputs/gemini-book-I-2026-11-01/`，审查报告完整归档于 `reports/reviews/gemini-book-I-2026-11-01/`。

---

## 三、 第二项整改：I.3 英文底本校勘与虚构注撤销

针对 `R-I3-01` 及审查报告指出的底本实词篡变和反向造词问题，进行逐项核准与纠正：

| 错误位置 | 候选错误词形 | 权威见证（Faded Page / Wiki） | 关联虚构注释处置 |
| :--- | :--- | :--- | :--- |
| `048.11` | `Eyrawyglaa` | `Eyrawyggla` | 恢复原词形，更正爱尔霍恩传奇双关 |
| `048.22` | `Buckleyitch` | `Bucklovitch` | 恢复原词形（布兰科·燧发枪手之女·巴克洛维奇） |
| `048.33` | `malfeasances` | `malpractices` | 恢复原词形（违规行径） |
| `049.08` | `yearweeksms` | `yearschaums` | 恢复原词形（年岁浮沫） |
| `049.19` | `Calomnequeller's` | `Calomnequiller's` | 恢复原词形（造谣羽毛笔） |
| `051.14` | `the two Curranss` | `two Curchies` | **撤销** `n-i3-51-haberdasher-currans` 中附会的爱国演说家约翰·菲尔波特·柯兰；更正为“两位行屈膝礼女裁缝／两座小教堂” |
| `052.23` | `latitudinarianismr` | `latitudinous baver` | 撤销所谓“宽容派神学教条”，恢复宽边帽及后接的帽巾、领结、外套、裤长、雨伞、扣子、手套等完整衣饰清单 |
| `055.03` | `Maemuffinstirnomates` | `Maeromor Mournomates` | **撤销** `n-i3-55-house-atreox` 中捏造的松饼（muffin）释义，恢复阿伽门农与莫恩山脉／哀悼之友双关 |
| `055.19` | `firefountd` | `fireleaved` | 恢复原词形（生出火叶） |
| `059.16` | `Sevendialshes` | `Sevenchurches` | 恢复格伦达洛“七教堂”地名，撤销伦敦伦巴底街七钟面假想；补回整段证词 |
| `066.17` | `Edenquayy` | `Edenberry` | **撤销** `n-i3-66-coffin-illusionist-hyde-cheek` 中指定的都柏林伊甸码头，更正为奥法利郡伊甸德里镇（Edenderry）与伊甸园双关 |
| `067.16` | `carbolics` | `carcasses` | 恢复原词形（腐尸骸骨），撤销服石炭酸自尽的虚构剧情 |
| `069.20` | `propenomen is` | `professionals` | 恢复原词形（专业人士） |

---

## 四、 第三项整改：I.2 音乐版面补全与大段漏译处置

针对 `R-I2-04`、`R-I2-06`、`R-I2-07`、`R-I2-08` 进行系统性补译与结构复原：

1. **第 44 页版面缺口与乐谱恢复（`R-I2-08`）**：
   - 彻底修复 `fw-i2-042-17` 止于雷词导致 44 页后部缺失的问题；
   - 补入第二雷词后的完整演出提示与标题：
     ```text
     {  | Ardite, arditi!
     Music cue.

     "The Ballad of Persse O'Reilly."
     ```
   - 补入乐谱图像在正文系统中的规范挂载，无缝衔接至第 45 页歌谣正文，彻底消除 044.22–044.36 的空白断层。
2. **动作与成分清单补齐（`R-I2-04`，`034.30–036.34`）**：
   - 补齐被整体裁撤的成分怀疑与身体功用长括号：`though this seems in some cumfusium with the chapstuck ginger... sours, acids, salts, sweets and bitters... bone, muscle, blood, flesh and vimvital...`；
   - 补齐誓词中的脱帽敬礼动作：`before the Great Taskmaster's (I lift my hat!) any hygienic day to this hour`；
   - 纠正手套夹于肘弯动作（`gauntlet chopstuck in the hough of his ellboge`），消除肢体混淆。
3. **赛马细节与誓言补齐（`R-I2-06`，`038.09–039.27`）**：
   - 补齐握手宣誓层（`hands between hahands, in fealty sworn`）；
   - 补齐以“两鼻之微”险胜的真实赛况与第三名鼓手考克森（`Drummer Coxon, nondepict third`）；
   - 恢复 Pomranzia 的禁食令、pecklapitschens 的布丁誓词及修女呼号。
4. **霍斯蒂落魄与十八月转诊大段漏译重译（`R-I2-07`，`039.28–042.16`）**：
   - 废除单薄的自杀梗概，完整译出霍斯蒂历时 18 个月在邓恩爵士医院、杰维斯街医院与阿德莱德医院圣凯文病床之间辗转求治的曲折路径与失败结局；
   - 补齐各路酒肆名录（Duck and Doggies, Galopping Primrose）；
   - 补齐同卧伴侣关系（Lisa O'Deavis 与 Roche Mongan）；
   - 补齐末尾掉队索钱者呼号（`small p.s. ex-exexecutive ... I want money. Pleasend`）。

---

## 五、 第四项整改：I.5 缺句缺图补全与无据增写剔除

针对 `I5-R01` 至 `I5-R08` 全面整治漏句、漏图与反向自造剧情：

1. **第 121 页缺句与双重旋转 F 字符恢复（`I5-R06`）**：
   - 恢复 Wiki 缺失、但 Faded Page 完整保留的关键句：
     `returns inhibited, with some half-halted suggestion,`
   - 登记并排版两枚旋转 F 字符号（`【Image: F rotated 180°】` 与 `【Image: F mirrored vertically】`），采用 `source_figures` 向量系统呈现，消除生硬的转义 HTML 图像标签；
   - **坚决剔除** 虚构捏造的“解开大写字母P的交尾天性”、“信封四度交叠对折”、“焦黑火漆封印”等无据故事；
   - 完整补全“患有理想失眠症的理想读者”（`ideal reader suffering from an ideal insomnia`）及 HCE/ALP、432/1132、p/q 字母学论述。
2. **剔除投币机杜撰，恢复孔子与中庸（`I5-R02`，`107.08–110.21`）**：
   - **剔除** 凭空捏造的“假镍币塞进投币机”、“从一数到一百”及虚假注释 `i5-dime-dozen-slotmachine`；
   - 恢复孔子中庸之道（`Kung's doctrine of the meang`）、布鲁斯兄弟与蜘蛛、埃尔伯费尔德算术马；
   - 完整译出信封外壳与女子衣着长篇比喻，以及关于事实与虚构鉴别的五重反诘。
3. **熔化之马纠偏与波士顿书信全文复原（`I5-R03`，`110.22–113.22`）**：
   - 纠正 `masses of meltwhile horse`，消除“融解为奶牛”的荒诞增写，同步修订注释 `i5-photoist-negative-horse-tip`；
   - **剔除** 假造的“Dear Dirtdump”、“亲爱的埃尔维克老太监”；
   - 将原稿中被概括的波士顿书信恢复为连贯的第一人称信文体（玛吉、全家健康、十字吻等），完整保留信文口吻与全部细节。
4. **通格-托伊德假题录与纸牌清单复原（`I5-R07`，`121.29–123.29`）**：
   - 纠正达夫-穆格利教授所论的合作命名，恢复通格-托伊德关于迦太基报告的论著戏拟；
   - 补齐被删去的手抄本缩写清单、数码与纸牌祷词层。

---

## 六、 推进策略与后续批次安排

按照“撤无据增写、逐注追源、逐句全译”的严密标准，后续分批推进并向复核者交验：

1. **微批次切分机制**：长篇巨段一律拆分为 15–30 行工作包，单批翻译与审校严格对齐原文行，杜绝单次提示词过长导致的提纲式概括。
2. **严守中文常态**：坚持余光中《中文的常态》标准，彻底杜绝被字句，精简弱动词与偏正结构，消灭所有省略号（`……`）。
3. **双语对齐矩阵输出**：每次交审均附带中英行级映射表（Line-by-Line Alignment Matrix），确保原文无一字空悬，译文无一字虚增。
