# 《芬尼根的守灵夜》中文注疏 by Louis.Akisame with LLM

**James Joyce · Finnegans Wake**

[在线阅读](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/) · [从开篇读起](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/chapters/I-1.html) · [续译断点](progress/RESUME.md)

循河入梦，逐字寻声。

动机源于现代物理学一段奇妙的命名渊源。以博闻强识为人熟知的物理学家默里·盖尔曼（Murray Gell-Mann），向来精于在人文意象与前沿科学间织造隐喻——他曾借佛教解脱苦难的“八正道”（Noble Eightfold Path），借喻基于 ```math\mathfrak{su}(3)```对称性整理介子与重子的“八重法”分类体系；而在构想构成强子的更深层基本粒子模型时，他起初脑海中只有类似“kwork”的声音，迟迟未定下拼写。直到翻开晦涩难解的《芬尼根的守灵夜》，他在第383页撞见如海鸟啼鸣般的诗句：“Three quarks for Muster Mark!”。冷僻的嘶鸣既具海鸥呼号的声色恰好契合强子由三枚亚原子粒子构成的构架，就此定格为物理学界最著名的粒子命名：quark（夸克）。在这个注意力稀缺的时代，或许这种科学与文学的互文，能让人静下心来，体会洗尽铅华的真实与美。

这个工程逐段翻译《芬尼根的守灵夜》，保存底本、初译、修订、译注与异译，再从同一份稿件生成网页和 EPUB。

参考 [QriDoki 的《追忆似水年华》翻译工程](https://github.com/QriDoki/in-search-of-lost-time-translation-project)，另设页行定位、证据分级与首尾联动审校。代码和试译均重新编写；项目技能借鉴其分工与交接流程，按《守灵夜》改写。

## AI 译文说明

《芬尼根的守灵夜》（*Finnegans Wake*）是 James Joyce 于 **1939 年**出版的长篇小说。全书**四卷十七章**，通行分页到第 **628 页**，正文从第 3 页开始。它将多语词形、谐音、典故与梦境叙事织在一起；[文字见证](https://www.fadedpage.com/books/20180126/html.php) · [JJDA 卷章说明](https://jjda.ie/f/ff/fdra/fnbdetails.htm)

本工程沿用原著四卷，不另拟卷名：

1. **第一卷（I）**：八章，通行页码 **3–216**。
2. **第二卷（II）**：四章，通行页码 **219–399**。
3. **第三卷（III）**：四章，通行页码 **403–590**。
4. **第四卷（IV）**：一章，通行页码 **593–628**。

原著卷章与纸本装帧分开记录：全译本可以分装三册，仍覆盖原著四卷十七章。本项目最终中文总字数待全译后统计。

### AI 翻译、用量与费用

使用 **Codex** 辅助初译、检索、注释和中文修订。每段保存原文、初译、当前采用稿与备选译法；每条注释登记出处和证据层级。英、中、日研究用于核对跨作品联系、译名及异译，具体流程见下方项目技能。

以下为本项目记录，更新于 **2026-10-31**。尚未核算的项目先标“暂记”，待实际日志或账单汇总后补齐。

| 项目 | 当前记录 | 记录依据 |
| --- | --- | --- |
| AI 工具 | **Codex** | 当前工程与译注工作记录 |
| 模型及版本 | **暂记：待核日志** | 汇总实际调用模型及版本 |
| 累计 token | **暂记：待核算** | 分列输入、输出及缓存用量，避免重复累计 |
| 总用时 | **暂记：待核算** | 区分翻译／审校用时与工程开发、等待时间 |
| 费用 | **暂记：待核算** | 以实际账单为准；赠额、订阅与按量费用分别注明 |
| 人工审校 | **尚无署名记录** | 以章稿 `reviewers` 为准 |
| 人工阅读进度、预计完成日期 | **暂记：待维护者补充** | 以实际阅读和修订记录为准 |

审校按“初译 → 研究核证 → 独立审校 → 中文修订”衔接，每段至多两轮定点修订。未解决的误译、漏译或来源问题继续保留为未完成；AI 审校与人工审校分别登记。中文修订遵循余光中《中文的常态》，同时保留原著刻意造词、重复和断句。

项目由 [Louis-QiuyuLu](https://github.com/Louis-QiuyuLu) 维护。**欢迎诸位参与阅读，批评斧正，核对出处，讨论异译并提交调整** 在线读本可调阅读设置，也可在本机试改译文与注释，再通过 GitHub 提交修订。

### 当前进度

截至 **2026-11-01**，第一卷第一章已完成初译与连续覆盖核对。当前保存 **27 段试译及修订稿、230 条译注**；其中 I.1 为 **26 段、226 条注释**，另有篇末样稿。**尚无人工审校署名**。

- **顺序完成范围**：I.1 · **003.01–029.36**，共27页；已作AI首轮校订，未作人工终审。
- **首尾对读样稿**：IV · **628.15–628.16**，不计入顺序完成范围。
- **下一起点**：I.2 · **030.01**。底本准备、研究示例和技能文档不计作已完成译文。

本轮纠正博物馆段增漏、对话词形及错位坐标；新增104条注释已逐项缩限为项目试读或待考，未核史实与语源不写成定论。旧交稿和隔离稿保留追溯。核查范围见 [全章复核报告](reports/reviews/gemini-I-1-complete-integration.r1.md) 与 [覆盖账](reports/reviews/gemini-I-1-complete-coverage.json)。

详细状态见 [进度清单](publish/PROGRESS.md) 与 [续译断点](progress/RESUME.md)。人工阅读与审校逐段留名，完成日期按实际进展补记。

### 底本

当前采用 **Faded Page 电子转录本**作文字见证。其扉页列明 **Viking Press 1958 年第八印本，已纳入作者勘误**；定位沿用通行 **1939 年版页码与页行**。另与 FinnegansWiki 转录对照，并查 JJDA 版本资料。[见证本扉页与转录说明](https://www.fadedpage.com/books/20180126/html.php)

原著、具体版本、作者自释、研究意见与社区注解分别登记。引用 JJDA 时注明 1939 或 2010 年版；底本异文与解释分开处理。详见 [底本说明](docs/SOURCES.md) 与 [来源表](sources/catalog.json)。

### 翻译工作流

| 序号 | 阶段 | 权威字段与阶段产物 | LLM 理解语义 |
| --- | --- | --- | --- |
| 1 | 核对底本与分段 | `original`、`sources/catalog.json`、底本工作包 | **按需**：核句法与异文；抽取后逐字复核 |
| 2 | 生成原文 Markdown | `raw-md/` | 无，工具直接投影原文 |
| 3 | 逐段初译 | `draft`、`translated-md/` | **有** |
| 4 | 研究、修订与注释 | 三语证据账、译名增量、`notes`、`annotations/` | **有** |
| 5 | 中文修订与润色 | `translation`、`polish/dev/`、`alternatives` | **有**；人工审校另留名 |
| 6 | 渲染 HTML 与打包 EPUB | `dist/site/`、EPUB、CI/CD 产物 | 无，工具构建与检查 |

JSON 章稿保存原文、初译和采用稿，Markdown、网页与 EPUB 从中生成。三语研究按疑问触发；某语资料不可得便记录限度，不凑引文。研究结论经整合者逐项采用，才进入注释或备选译法。

每轮保存下一页行、原文锚句与未决问题；每章录全并核对覆盖后，再标整章完成。以后重译仍按四卷十七章组织，保留固定段落 ID、初译及旧版取舍，不覆盖历史记录。

### 版本控制与审校记录

- **版本与变更**：每次提交写明范围、底本、实质改动、检查结果和未决问题。可查 [GitHub 提交记录](https://github.com/Louis-QiuyuLu/Finnegans-Wake-Translation-Project/commits/main/) 与 [首版工程说明](publish/RELEASE_NOTES.md)。
- **稿件阶段**：`original` 保留文字见证，`draft` 保留初译，`translation` 保存当前采用稿；备选译法另存，历史取舍随提交保留。
- **审校状态**：`draft` 为试译，`revised` 为修订待审；真实人工核过底本、出处与中文，并在 `reviewers` 留名后，才标 `reviewed`。
- **恢复与同步**：工作包、初译、审校报告和公共稿绑定实际版本；稿件、来源、生成稿及断点一并提交。GitHub Pages 从公共稿自动更新。
- **首尾接缝**：修改开篇或篇末时连读两处；篇末保留未完成句法，不补成封闭结尾。

### 中文世界过往的翻译项目

下表将“进度”和“近况”分列。只记已核资料，不把书目介绍当作读过译本全文。

| 翻译项目 | 译者 | 进度 | 近况与出版记录 | 翻译工作持续时长 |
| --- | --- | --- | --- | --- |
| **戴从容译注本（简体）** | **戴从容** | **全译注释本，三册** | 译林出版社、华东师范大学出版社于 **2025 年 8 月**出版。[《文艺报》译者访谈](https://wyb.chinawriter.com.cn/content/202607/31/content84784.html) | **18 年**，据译者自述 |
| **梁孙杰译本（繁体）** | **梁孙杰（梁孫傑）** | **全译本，上、中、下三册** | 书林出版；**2025 年 1 月**举行全译本发布会；此前已有节译。[师大发布会公告](https://www.giect.ntnu.edu.tw/index.php/2024/12/18/20241218/) · [出版社译者访谈](https://www.bookman.com.tw/news/detail/43) | **约 12 年**，据师大说明；早期片段尝试另计 |

### 日文世界的译介与全译

铃木幸夫、大泽正佳等曾参与局部译介；柳濑尚纪的全译本于 **1991–1993 年**分册刊行。**1991 年是前册刊行年份，完结册出版于 1993 年 10 月 20 日**，因此此处将全译刊行完成记为 **1993 年**。[CiNii 书目](https://ci.nii.ac.jp/ncid/BN06806679) · [河出书房新社完结册书目](https://www.kawade.co.jp/np/isbn/9784309202280/)

| 翻译项目 | 译者（已核署名） | 进度 | 近况与出版记录 | 翻译工作持续时长 |
| --- | --- | --- | --- | --- |
| **《フィネガン徹夜祭》译解** | **铃木幸夫（鈴木幸夫）等** | 局部译介、译解连载 | 国会图书馆收录 **1969 年 12 月**《早稻田文学》第 11 回记录。[国会图书馆书目](https://ndlsearch.ndl.go.jp/books/R000000004-I190139) | 起讫尚未核全 |
| **《フィネガンズ・ウェイク》选译** | **大泽正佳（大沢正佳／大澤正佳）等** | 选译 **5 篇** | 收入集英社 **1978 年 6 月**《世界の文学》卷 1。[国会图书馆书目](https://ndlsearch.ndl.go.jp/books/R100000002-I000001378445) | 尚未核实 |
| **柳濑尚纪全译本** | **柳濑尚纪（柳瀬尚紀）** | **四卷全译，装为《I・II》《III・IV》两册** | 河出书房新社 **1991–1993 年**刊行，完结册于 **1993 年 10 月 20 日**出版。[CiNii 书目](https://ci.nii.ac.jp/ncid/BN06806679) · [出版社书目](https://www.kawade.co.jp/np/isbn/9784309202280/) | **约 8 年**，据出版社说明 |

已有译本可用于具名对读，比较声音、多义和文化背景。引用具体译句须核版本、页码与原页；只有访谈、题录或摘要时，明确查阅限度。

### 项目技能

参考目录包含贡献、EPUB 转 Markdown、多角色翻译三类技能。本项目保留章节协调、分段交稿、相关术语、独立审校和上下文衔接，扩为七项。各技能附交接格式、失败条件和按需参考文档。[参考技能目录](https://github.com/QriDoki/in-search-of-lost-time-translation-project/tree/main/.ai/skills) · [本项目架构与阶段关口](docs/SKILLS_ARCHITECTURE.md)。

1. [prepare-source：核对底本与分段](.ai/skills/prepare-source/SKILL.md)。
2. [joyce-research：英中日研究与跨文本比较](.ai/skills/joyce-research/SKILL.md)。
3. [maintain-glossary：译名、变体与增量合并](.ai/skills/maintain-glossary/SKILL.md)。
4. [translate-chapter：逐段译注](.ai/skills/translate-chapter/SKILL.md)，附 [角色约定](.ai/skills/translate-chapter/references/roles.md)。
5. [review-translation：审校译义、出处与中文](.ai/skills/review-translation/SKILL.md)。
6. [checkpoint：保存断点与上下文](.ai/skills/checkpoint/SKILL.md)。
7. [contribute：合入修订与同步 GitHub](.ai/skills/contribute/SKILL.md)。

技能存于仓库 `.ai/skills/`，由 [AGENTS.md](AGENTS.md) 指引读取，无需全局安装。以 [底本包模板](templates/workpack.json) 固定输入，以 [批次模板](templates/batch.json) 保存状态；译者交完整段落对象，审校者绑定实际交稿版本，整合者统一回写 JSON 章稿。工作包、研究主张、初译、审校记录与摘要存于 `reports/`。《守灵夜》须保留首尾正文、字母符号与有文义作用的排版。

三语研究比较原著、书信、手稿、笔记、学术解释和既有译本，逐项记录证据、异议与译法影响。只见书目或摘要便说明查阅限度；三语没有引文配额，某语资料不可得也不凑结论。研究主张经采用决定后，才进入注释或备选译法。声形相似不能独自证明互文，AI 审校也不能代替人工署名。

技能格式、交接场景和当前工具限制见 [验收记录](reports/skills-validation.md)。

## 现在可以读什么

当前读本收录二十七段试译及修订稿，附二百三十条译注：

- **I.1 · 003.01–029.36**：第一章全篇，包括博物馆、编年史、穆特／朱特对话、恶作剧女王与劝卧告别；三处旋转字母在网页与EPUB中另存并重绘。
- **IV · 628.15–628.16**：篇末片段，接回开篇。

全书四卷十七章已建目录；第一章初译已录全并核覆盖。各段均待人工审校，不能当作定稿。进度见 [进度清单](publish/PROGRESS.md)。

顺序译注从第一卷第一章开始。每轮保存页行断点，每章保存章节记录；下次先读 [续译断点](progress/RESUME.md)，从指定锚句接续。

先读 [开篇试译](polish/dev/I-1.md)、[末尾试译](polish/dev/IV.md)，再看 [开篇译注](annotations/I-1.json)。

## 英文朗读

在线读本已接入 **9 段 GPT-SoVITS 英文朗读**，在对应段落上方播放，可暂停、拖动进度并调音量；语速放在顶部「阅读设置」。一次只播放一段，音频按需加载。

两对共行段落的录音已按顺序拼接。007.16段因原文改字，旧录音暂缓；没有录音的段落不显示播放器。合成读音仍有近似处理，页面标明 AI 合成。音频登记、继续生成与构建规则见 [朗读说明](audio/README.md)。

### 朗读模型

朗读采用 **GPT-SoVITS v4**，以 **Vertin（《重返未来：1999》角色音色）**合成英文原文。音频在本机预先生成，再转成 MP3；读者直接在网页播放，无需安装模型或提供 API 密钥。

[生成脚本](scripts/generate_audio.py)默认选择 `sisyphus`：在 [Vertin](https://www.ai-hobbyist.com/thread-159886-1-4.html) 基础上，以[《西西弗神话》](https://www.bilibili.com/video/BV1fSE4zBEox/)英语朗读语料微调语义与韵律，尝试保留沉稳英音及长句停顿。脚本优先加载 `Vertin-Sisyphus-v95.ckpt`，缺少时依次尝试 `Vertin-Sisyphus-e9.ckpt`、原版 `Vertin-e10.ckpt`，搭配 `Vertin_e2_s154_l32.pth` 声学权重；也可用 `--model vertin` 或 `--model vertin2` 切换。文件名 `v95` 不代表朗读准确率或音质评分。

合成前按意群切分文本，再为 Joyce 生造词与多语拼缀补入[近似发音方案](scripts/joyce_phonetics.py)。

## 本地读本与电子书

仅需 **Python 3.9 或以上版本**。无需 API 密钥，也不调用付费翻译服务。

```bash
python3 scripts/project.py check
python3 -m unittest discover -s tests -v
python3 scripts/project.py build
python3 -m http.server 8000 --directory dist/site --bind 127.0.0.1
```

打开 `http://127.0.0.1:8000`。顶部「阅读设置」可调字号、行距、字体、版心宽度与左右留白，并提供纸张、浅色、护眼、深色四套配色。字体采用开源思源宋体、思源黑体与霞鹜文楷；顶部「简体／繁體」按钮切换网页字形，也可在设置内选择。切换只改显示，章稿、编辑框和修订导出保留原文。设置记在当前浏览器，恢复默认时保留本机修订。读本另有原文开关、折叠译注、本章检索、译名表，支持手机与键盘操作。站内资源采用相对链接，适配 GitHub Pages 项目路径；开源字体从固定版本 CDN 按需加载，许可与来源见 [第三方资源说明](site/vendor/README.md)。

展开段落下方「修订本段」，可改译文及译注，保存后在本页预览。修订保存在当前浏览器，可导出整章 JSON；点击「复制修订并打开 GitHub」，在编辑页全选、粘贴、查看差异并提交。提交后会自动更新公共读本。导出与提交前会联网核对仓库现稿；公共稿若已更新，先刷新并对照，再继续处理本机修订。

电子书生成于 `dist/finnegans-wake-zh.epub`。网页与 EPUB 都从同一份稿件构建，注释可往返跳转。构建工具会检查站内锚点及 EPUB 内部链接。

每次 GitHub 检查通过后，Actions 提供名为 `finnegans-wake-reader` 的下载包。下载并解压即可找到网页和 EPUB。推送 `v*` 标签时另生成 GitHub Release。Pages 启用方式见 [开发说明](DEVELOPMENT.md)。

网页构建仅需 Python。修改阅读器代码时另用 Node.js 22 以上版本运行 `node --test tests/*.cjs`，检查修订合并、阅读设置与音频切换。

## 工程目录

```text
manuscript/chapters/   唯一编辑入口：十七章 JSON 稿件
sources/catalog.json  底本、版本见证与参考资料
glossary/terms.json   暂定译名及采用理由
raw-md/               自动生成：原文便读稿
translated-md/        自动生成：初译便读稿
polish/dev/           自动生成：当前修订稿
annotations/          自动生成：独立译注
publish/              进度与发布说明
progress/             续译锚句、未决问题与章节断点
docs/                 译注规范、底本说明、实施设计
prompts/              翻译与审校工作单
.ai/skills/           底本、翻译、审校、断点与同步技能
reports/              实际批次的工作包、初译、审校记录与摘要
scripts/project.py    检查、生成、网页及 EPUB 构建
site/                 阅读器样式与交互
tests/                数据规则与产物链接测试
```

稿件保存三个阶段：`original` 是原文，`draft` 是初译，`translation` 是当前读本采用稿。不要直接修改自动生成目录；改好 JSON 后运行 `python3 scripts/project.py generate`。详见 [贡献指南](CONTRIBUTING.md) 与 [稿件格式](docs/MANUSCRIPT_FORMAT.md)。

## 译注原则

先听声音，再辨句法，最后查典故。正文尽量保留语言动作；中文无法兼顾的双关写入注释，重要异译另存。引文记录页行与见证本；初版、后期勘误本和 2010 年版不能混用。

详见 [译注规范](docs/EDITORIAL_GUIDE.md) 与 [底本说明](docs/SOURCES.md)。

## 许可与署名

原创中文试译及译注采用 **CC BY-NC-SA 4.0**；工程代码采用 **MIT**。Joyce 原著、外部注释和第三方资料不纳入本项目许可。Faded Page 标明原著在加拿大属公有领域；本项目未镜像该站整部电子书。使用、扩录或发布原文时，请按所在地规则核对权利。

本仓库起步稿由 AI 辅助整理、试译和注释。`reviewers` 为空表示尚无人工审校记录；不得凭自动检查把试译改成已审校。

完整范围见 [LICENSE.md](LICENSE.md)。贡献译文时请注明署名方式与资料出处。
