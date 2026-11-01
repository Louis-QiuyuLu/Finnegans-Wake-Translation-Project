# 《芬尼根的守灵夜》中文注疏 by Louis.Akisame with LLM

**James Joyce · Finnegans Wake**

[在线阅读](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/) · [从开篇读起](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/chapters/I-1.html) · [续译断点](progress/RESUME.md)

循河入梦，逐字寻声。

动机源于现代物理学一段奇妙的命名渊源。以博闻强识为人熟知的物理学家默里·盖尔曼（Murray Gell-Mann），向来精于在人文意象与前沿科学间织造隐喻——他曾借佛教解脱苦难的“八正道”（Noble Eightfold Path），借喻基于 $\mathrm{SU}(3)$ 对称性整理介子与重子的“八重法”分类体系；而在构想构成强子的更深层基本粒子模型时，他起初脑海中只有类似“kwork”的声音，迟迟未定下拼写。直到翻开晦涩难解的《芬尼根的守灵夜》，他在第383页撞见如海鸟啼鸣般的诗句：“Three quarks for Muster Mark!”。冷僻的嘶鸣既具海鸥呼号的声色，又恰好契合强子由三枚亚原子粒子构成的架构，就此定格为物理学界最著名的粒子命名：quark（夸克）。

[盖尔曼自述](https://www.webofstories.com/play/murray.gell-mann/116) · [Harald Fritzsch 的回忆与物理说明](https://cerncourier.com/a/strong-interactions/)

在这个注意力稀缺的时代，或许这种科学与文学的互文，能让人静下心来，体会洗尽铅华的真实与美。

这个工程逐段翻译《芬尼根的守灵夜》，保存底本、初译、修订、译注与异译，再从同一份稿件生成网页和 EPUB。

参考 [QriDoki 的《追忆似水年华》翻译工程](https://github.com/QriDoki/in-search-of-lost-time-translation-project)，另设页行定位、证据分级与首尾联动审校。自编构建工具、阅读器与试译另行编写，第三方库与字体按上游许可使用；项目技能借鉴参考工程的分工与交接流程，按《守灵夜》改写。

## AI 译文说明

《芬尼根的守灵夜》（*Finnegans Wake*）是 James Joyce 于 **1939 年**出版的长篇小说。全书**四卷十七章**，通行分页到第 **628 页**，正文从第 3 页开始。它将多语词形、谐音、典故与梦境叙事织在一起；[文字见证](https://www.fadedpage.com/books/20180126/html.php) · [JJDA 卷章说明](https://jjda.ie/f/ff/fdra/fnbdetails.htm)

本工程沿用原著四卷，不另拟卷名：

1. **第一卷（I）**：八章，通行页码 **3–216**。
2. **第二卷（II）**：四章，通行页码 **219–399**。
3. **第三卷（III）**：四章，通行页码 **403–590**。
4. **第四卷（IV）**：一章，通行页码 **593–628**。

原著卷章与纸本装帧分开记录：全译本可以分装三册，仍覆盖原著四卷十七章。本项目最终中文总字数待全译后统计。

### AI 翻译、用量与费用

使用 **GPT-6.1 Sol 与 Gemini4 Argon** 辅助初译、检索、注释、审校和中文修订，模型名称由维护者提供。Gemini 交过初译与候选稿，Codex 执行复核及部分整合；采用范围以公共章稿和绑定版本的报告为准。每段保存原文、初译、当前采用稿与备选译法；每条注释登记出处和证据层级。三语研究按具体疑问开展，不表示每条注释都已完成英、中、日核证。

以下为本项目记录，更新于 **2026-11-02**。尚未核算的项目先标“暂记”，待实际日志或账单汇总后补齐。

| 项目 | 当前记录 | 记录依据 |
| --- | --- | --- |
| AI 工具 | **GPT-6.1 Sol、Gemini4 Argon** | 维护者提供的模型名称；交稿与复核过程见 `reports/` |
| 调用版本与参数 | **暂记：待核日志** | 逐次调用记录尚未汇总 |
| 累计 token | **暂记：待核算** | 分列输入、输出及缓存用量，避免重复累计 |
| 总用时 | **暂记：待核算** | 区分翻译／审校用时与工程开发、等待时间 |
| 费用 | **暂记：待核算** | 以实际账单为准；赠额、订阅与按量费用分别注明 |
| 人工审校 | **尚无署名记录** | 以章稿 `reviewers` 为准 |
| 人工阅读进度、预计完成日期 | **暂记：待维护者补充** | 以实际阅读和修订记录为准 |

审校按“初译 → 研究核证 → 独立审校 → 中文修订”衔接，每段至多两轮定点修订。未解决的误译、漏译或来源问题继续保留为未完成；AI 审校与人工审校分别登记。中文修订遵循余光中《中文的常态》，同时保留原著刻意造词、重复和断句。

项目由 [Louis-QiuyuLu](https://github.com/Louis-QiuyuLu) 维护。**欢迎诸位参与阅读，批评斧正，核对出处，讨论异译并提交调整** 在线读本可调阅读设置，也可在本机试改译文与注释，再通过 GitHub 提交修订。

### 当前进度

截至 **2026-11-02**，英文底本已录入**四卷十七章、619个正文页**，网页与 EPUB 均可阅读，保留14份字形、乐谱及几何图资源。英文经过机械抽取与完整性校验，尚未逐页人工校勘；[录入记录](reports/source-import/full-english-2026-11-01.json)列明来源、页码与指纹。

中文共 **92段、573条注释**。其中第一卷 **I.1–I.8 · 003.01–216.05** 为 **91段、569注**，另有第四卷篇末样稿 **1段、4注**。第一卷已核文本连续覆盖，各段均为 `revised`、`reviewers: []`，**尚无人工终审署名**。

Gemini 最新交稿已补回旧稿长清单、问答、寓言与章尾。Codex 复核 I.2–I.8 后，定点修正动作／否定反译、漏失动作、无据人名、数值和注释文本冲突；原文、初译、段落ID及范围保留。初审报告与定点复核分开保存，未把机械检查算作学术审校。见 [整合处置](reports/revisions/book-I-codex-integration-20261102.json)、[独立审校与复核](reports/reviews/gemini-book-I-2026-11-02/)。

**下一起点：II.1 · 219.01。** 第二卷尚未录入中文；临时底本包未获本轮逐段验收。外部典故、词源、既有译本及精确行号仍有复核限度，逐批交审时继续核实。

旧 r1/r2 交稿、冻结快照及当时 `blocked` 裁定保持原样，只作版本追溯。本轮新稿采用范围以上述整合记录及绑定稿件为准，不能把旧结论或新文件名当作验收。详细状态见 [进度清单](publish/PROGRESS.md) 与 [续译断点](progress/RESUME.md)。

### 底本

当前采用 **Faded Page 电子转录本**作文字见证。其扉页列明 **Viking Press 1958 年第八印本，已纳入作者勘误**；定位沿用通行 **1939 年版页码与页行**。另与 FinnegansWiki 转录对照，并查 JJDA 版本资料。[见证本扉页与转录说明](https://www.fadedpage.com/books/20180126/html.php)

原著、具体版本、作者自释、研究意见与社区注解分别登记。引用 JJDA 时注明 1939 或 2010 年版；底本异文与解释分开处理。详见 [底本说明](docs/SOURCES.md) 与 [来源表](sources/catalog.json)。

### 翻译工作流

| 序号 | 阶段 | 权威字段与阶段产物 | LLM 理解语义 |
| --- | --- | --- | --- |
| 1 | 录入英文、核对底本与分段 | 全章 `source_text`、分段 `original`、来源表、底本工作包 | 全本录入无；分段核句法与异文时按需使用，另作逐字复核 |
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

全书十七章英文均可阅读。每章顶部展开「全章英文」，按原书页码跳转；已有完整中文的章节默认收起此栏。英文保留原作旁注、脚注回链和图版，版面随屏幕调整，不冒充纸本影印。

中文可读第一卷八章，以及第四卷篇末片段：

- **I.1–I.8 · 003.01–216.05**：91段修订待审稿，569条注释。
- **IV · 628.15–628.16**：篇末样稿，1段、4注；与开篇对读。

各段均待人工终审，不能当作定稿。先读 [第一章](polish/dev/I-1.md)、[第二章](polish/dev/I-2.md)，译注另见 [annotations/](annotations/)。后续从 [II.1续译断点](progress/RESUME.md) 起，按实际交审范围推进。

## 英文朗读

在线读本已接入 **9 段 GPT-SoVITS 英文朗读**，在对应段落上方播放，可暂停、拖动进度并调音量；语速放在顶部「阅读设置」。一次只播放一段，音频按需加载。

两对共行段落的录音已按顺序拼接。未登记或原文已改的旧录音不进入网页，没有音频的段落不显示播放器。合成读音有近似处理，页面标为「GPT-SoVITS · 重返未来1999 瓦尔汀」。

本轮现场登记共12份：九份既有录音通过原文绑定、文件指纹、时长及完整解码检查；三份 I.3 旧录音仍对应修订前原文，未随本批发布，也未靠换指纹冒充重生。生成队列优先处理这三段，再补第一卷缺失录音。本机旧版 LoRA 权重识别错误已修，CPU／MPS 短句对照通过；新录音先存待审目录并附生成凭据，再经核验采用。见[运行修复记录](reports/source-import/tts-runtime-repair-2026-11-02.json)。逐词转写与音质听校尚未完成。见 [现场核对记录](reports/source-import/audio-intake-2026-11-02.json) 与 [朗读说明](audio/README.md)。

### 朗读模型

网页将音色标为 **Vertin（《重返未来：1999》瓦尔汀）**。音频在本机预先生成，再转成 MP3；读者直接在网页播放，无需安装模型或提供 API 密钥。[生成脚本](scripts/generate_audio.py)当前将 GPT-SoVITS 推理版本配置为 **v4**；`audio/index.json` 未逐段登记所用权重或训练来源，不能仅凭当前脚本确定九段既有录音各自用了哪份模型。

脚本默认参数为 `--model sisyphus --ref sisyphus2 --speed 1.05 --steps 32`。`sisyphus` 是脚本中的模型选项：优先加载 `Vertin-Sisyphus-v95.ckpt`，缺少时依次尝试 `Vertin-Sisyphus-e9.ckpt`、`Vertin-e10.ckpt`，搭配 `Vertin_e2_s154_l32.pth` 声学权重。也可用 `--model vertin` 或 `--model vertin2` 切换；权重、参考音频及完整训练记录未随仓库提供，不据文件名宣称已验证训练来源、准确率或音质。

[Vertin 音色页](https://www.ai-hobbyist.com/thread-159886-1-4.html) · [《西西弗神话》英语朗读](https://www.bilibili.com/video/BV1fSE4zBEox/)。

默认参考音频 `references/sisyphus2.wav` 必须另备，缺失时脚本会中止；仅有原版 Vertin 权重与 `e1` 参考音频时，按 [朗读说明](audio/README.md) 显式指定参数。**网页首次播放默认1×**，与生成脚本的合成速度参数分别控制。

合成前按意群切分文本，再为 Joyce 生造词与多语拼缀补入[近似发音方案](scripts/joyce_phonetics.py)。

## 本地读本与电子书

构建读本与 EPUB 仅需 **Python 3.9 或以上版本**。无需 API 密钥，也不调用付费翻译服务；重新生成语音另需 GPT-SoVITS 环境、模型与 FFmpeg，见 [朗读说明](audio/README.md)。

```bash
python3 scripts/project.py check
python3 -m unittest discover -s tests -v
python3 scripts/project.py build
python3 -m http.server 8000 --directory dist/site --bind 127.0.0.1
```

打开 `http://127.0.0.1:8000`。顶部「阅读设置」可调字号、行距、字体、版心宽度与左右留白，并提供纸张、浅色、护眼、深色四套配色。字体采用开源思源宋体、思源黑体与霞鹜文楷；顶部「简体／繁體」按钮切换网页字形，也可在设置内选择。切换只改显示，章稿、编辑框和修订导出保留原文。设置记在当前浏览器，恢复默认时保留本机修订。读本另有双语段原文开关、折叠译注、译稿检索、译名表，支持手机与键盘操作。站内资源采用相对链接，适配 GitHub Pages 项目路径；开源字体从固定版本 CDN 按需加载，许可与来源见 [第三方资源说明](site/vendor/README.md)。

展开段落下方「修订本段」，可改译文及译注，保存后在本页预览。修订保存在当前浏览器，可导出整章 JSON；点击「复制修订并打开 GitHub」，在编辑页全选、粘贴、查看差异并提交。**修订合入 `main`、通过 Pages 构建并部署后，公共读本才会更新。** 导出与提交前会联网核对仓库现稿；公共稿若已更新，先刷新并对照，再继续处理本机修订。

电子书生成于 `dist/finnegans-wake-zh.epub`。网页与 EPUB 都从同一份稿件构建，注释可往返跳转。构建工具会检查站内锚点及 EPUB 内部链接。

`Check and build` 工作流在 `main` 推送、拉取请求或手动运行时检查并构建；成功后提供名为 `finnegans-wake-reader` 的下载包，保留30天。下载并解压即可找到网页和 EPUB。推送 `v*` 标签时，另一个工作流会核标签与 `book.config.json` 版本一致，检查通过后生成 GitHub Release。Pages 启用方式见 [开发说明](DEVELOPMENT.md)。

网页构建仅需 Python。修改阅读器代码时另用 Node.js 22 以上版本运行 `node --test tests/*.cjs`，检查修订合并、阅读设置与音频切换。

## 工程目录

```text
manuscript/chapters/   唯一编辑入口：十七章 JSON 稿件
sources/catalog.json  底本、版本见证与参考资料
glossary/terms.json   暂定译名及采用理由
manuscript/source-assets/ 原著字形、乐谱与几何图
raw-md/               自动生成：十七章英文便读稿
translated-md/        自动生成：初译便读稿
polish/dev/           自动生成：当前修订稿
annotations/          自动生成：独立译注
publish/              进度与发布说明
progress/             续译锚句、未决问题与章节断点
docs/                 译注规范、底本说明、实施设计
prompts/              翻译与审校工作单
.ai/skills/           底本、翻译、审校、断点与同步技能
reports/              工作包、交稿、审校、录入指纹与处置记录
scripts/import_source.py 英文全本导入与来源指纹
scripts/project.py    检查、生成、网页及 EPUB 构建
site/                 阅读器样式与交互
tests/                数据规则与产物链接测试
```

完整英文单独存 `source_text`，不推进翻译断点。双语段保存三个阶段：`original` 是原文，`draft` 是初译，`translation` 是当前读本采用稿。不要直接修改自动生成目录；改好 JSON 后运行 `python3 scripts/project.py generate`。详见 [贡献指南](CONTRIBUTING.md) 与 [稿件格式](docs/MANUSCRIPT_FORMAT.md)。

## 译注原则

先听声音，再辨句法，最后查典故。正文尽量保留语言动作；中文无法兼顾的双关写入注释，重要异译另存。引文记录页行与见证本；初版、后期勘误本和 2010 年版不能混用。

详见 [译注规范](docs/EDITORIAL_GUIDE.md) 与 [底本说明](docs/SOURCES.md)。

## 许可与署名

原创中文试译及译注采用 **CC BY-NC-SA 4.0**；工程代码采用 **MIT**。Joyce 原著、外部注释和第三方资料不纳入本项目许可。Faded Page 标明原著在加拿大属公有领域；本项目已按维护者要求抽取全书正文及必要图版；未提交外部电子书下载缓存。使用、扩录或发布原文时，请按所在地规则核对权利。

本仓库起步稿由 AI 辅助整理、试译和注释。`reviewers` 为空表示尚无人工审校记录；不得凭自动检查把试译改成已审校。

完整范围见 [LICENSE.md](LICENSE.md)。贡献译文时请注明署名方式与资料出处。
