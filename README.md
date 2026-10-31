# 《芬尼根的守灵夜》中文译注工程

**James Joyce · Finnegans Wake**

[在线阅读](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/) · [从开篇读起](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/chapters/I-1.html) · [续译断点](progress/RESUME.md)

循河入梦，逐字寻声。这个工程逐段翻译《芬尼根的守灵夜》，保存底本、初译、修订、译注与异译，再从同一份稿件生成网页和 EPUB。

参考 [QriDoki 的《追忆似水年华》翻译工程](https://github.com/QriDoki/in-search-of-lost-time-translation-project)，另设页行定位、证据分级与首尾联动审校。代码和试译均重新编写；项目技能借鉴其分工与交接流程，按《守灵夜》改写。

## AI 译文说明

《芬尼根的守灵夜》1939 年首次出版。全书四卷十七章，通行版正文从第 3 页延至第 628 页。它以多语造词、声音游戏和梦境叙事交织人物与历史；中文译注须兼顾句法、词形、声音和典故。首尾相接，也是全书结构的关键。[文字见证](https://www.fadedpage.com/books/20180126/html.php) · [JJDA 版本与导读](https://jjda.ie/f/fwhome.htm)

本工程依原著四卷组织稿件：

1. **第一卷（I）**：八章，通行页码 3–216。
2. **第二卷（II）**：四章，通行页码 219–399。
3. **第三卷（III）**：四章，通行页码 403–590。
4. **第四卷（IV）**：一章，通行页码 593–628。

### AI 参与与审校

使用 **Codex** 辅助逐段初译、检索、注释和修订。稿件分别保存原文、初译、当前译文与备选译法；每条注释登记出处及判断层级。中文修订遵循余光中《中文的常态》，同时辨认原著刻意造词、重复和断句。

模型版本、累计 token、总用时与费用，待统一日志核算后补记。实际稿件、审校状态和续译位置分别见 [进度清单](publish/PROGRESS.md)、章内 `reviewers` 与 [续译断点](progress/RESUME.md)。当前尚无人工审校记录，各段保留试译标记。

项目由 [Louis-QiuyuLu](https://github.com/Louis-QiuyuLu) 维护。**欢迎书友参与阅读、核对出处、讨论异译并提交修订。** 在线读本支持本机试改，确认后可通过 GitHub 提交。

### 底本

采用 **Faded Page 电子转录本**作当前文字见证，其扉页列出 **Viking Press 1958 年第八印本，已纳入作者勘误**；页行沿用通行坐标。另以 FinnegansWiki 对照录文，并查阅 JJDA 版本资料。原著、版本见证、研究解释与社区释义分开登记。详见 [底本说明](docs/SOURCES.md) 与 [来源表](sources/catalog.json)。

### 翻译工作流

1. **核对底本与分段**：登记见证本、出处和页行，将原文录入 `manuscript/chapters/`；保留固定段落 ID。
2. **整理原文便读稿**：从 `original` 自动生成 `raw-md/`，此步不调用模型理解或改写原文。
3. **逐段初译**：AI 辨认句法、词形及声音，初译存入 `draft`，便读稿生成于 `translated-md/`。
4. **修订与注释**：AI 辅助查证、比较读法，释义和出处存入 `notes`，另生成 `annotations/`；存疑处明说。
5. **中文修订与润色**：AI 辅助删翻译腔、调整节奏，当前译文存入 `translation`，便读稿生成于 `polish/dev/`；人工审校另留署名。
6. **构建与发布**：工具检查数据、锚点和内部链接，生成 HTML 与 EPUB；GitHub Actions 自动部署在线读本。

每轮保存段落断点；每章完整录入并核对覆盖后，保存章节记录。稿件、注释和断点一并同步 GitHub，方便下次从锚句接续。

### 项目技能

参考目录包含贡献、EPUB 转 Markdown、多角色翻译三类技能。本项目保留分段交稿、相关术语、独立审校和上下文衔接，整理为五项：[参考技能目录](https://github.com/QriDoki/in-search-of-lost-time-translation-project/tree/main/.ai/skills)。

1. [prepare-source：核对底本与分段](.ai/skills/prepare-source/SKILL.md)。
2. [translate-chapter：逐段译注](.ai/skills/translate-chapter/SKILL.md)，附 [角色约定](.ai/skills/translate-chapter/references/roles.md)。
3. [review-translation：审校译义、出处与中文](.ai/skills/review-translation/SKILL.md)。
4. [checkpoint：保存断点与上下文](.ai/skills/checkpoint/SKILL.md)。
5. [contribute：合入修订与同步 GitHub](.ai/skills/contribute/SKILL.md)。

技能存于仓库 `.ai/skills/`，由 [AGENTS.md](AGENTS.md) 指引读取，无需全局安装。续译依次执行五项；多人或多代理协作时，译者交完整段落对象，审校者交意见，整合者统一回写 JSON 章稿。工作包、初译、审校记录与摘要存于 `reports/`。参考项目按文件位置跳过首尾、删除图片及普鲁斯特角色设定，均不沿用；《守灵夜》须保留首尾正文、字母符号与有文义作用的排版。

### 中文译本

- **戴从容译注《芬尼根的守灵夜》**：简体中文全译注释本，三册，译林出版社、华东师范大学出版社于 **2025 年 8 月**出版。译者访谈称译注历时 **18 年**。[《文艺报》译者访谈](https://wyb.chinawriter.com.cn/content/202607/31/content84784.html)
- **梁孙杰（梁孫傑）译《芬尼根守靈：墜生夢始記》**：繁体中文全译本，书林出版，上、中、下三册；**2025 年 1 月**举行新书发布。译者以约 **12 年**概括自 2012 年前后持续翻译以来的历程，更早已有片段尝试。[台湾师范大学新书发布新闻稿](https://www.eng.ntnu.edu.tw/wp-content/uploads/2024/12/new-FW%E6%96%B0%E6%9B%B8%E7%99%BC%E8%A1%A8%E6%9C%83-%E6%96%B0%E8%81%9E%E7%A8%BF1210_%E5%AE%9A%E7%A8%BF.pdf) · [出版社所刊译者访谈](https://www.bookman.com.tw/news/detail/43)

### 日文译介

- **铃木幸夫（鈴木幸夫）等**：早期参与译介《フィネガン徹夜祭》。日本国立国会图书馆收录 **1969 年 12 月**《早稻田文学》第 11 回译解记录，署名铃木幸夫等。[国会图书馆书目](https://ndlsearch.ndl.go.jp/books/R000000004-I190139)
- **大泽正佳（大沢正佳／大澤正佳）等**：**1978 年 6 月**集英社《世界の文学》卷 1 收录《フィネガンズ・ウェイク》选译五篇。[国会图书馆书目](https://ndlsearch.ndl.go.jp/books/R100000002-I000001378445)
- **柳濑尚纪（柳瀬尚紀）**：河出书房新社译本分《I・II》与《III・IV》两册，于 **1991–1993 年**刊行；完结册 **1993 年 10 月 20 日**出版。全译完成年份据此记作 **1993 年**。[CiNii 书目](https://ci.nii.ac.jp/ncid/BN06806679) · [出版社完结册书目](https://www.kawade.co.jp/np/isbn/9784309202280/)

现有译本可用于具名对读，讨论如何处理声音、多义与文化背景。具体引用须核对版本和页码；这份书目介绍不代表已逐页查阅各译本。

## 现在可以读什么

首版 v0.1.0 当前收录四段试译，附四十五条译注：

- **I.1 · 003.01–003.24**：第 3 页按三段译出，包含首句、尚未发生的历史拼贴和坠落雷鸣。
- **IV · 628.15–628.16**：篇末片段，接回开篇。

全书四卷十七章已建目录；尚无整章译完。各段均待人工审校，不能当作定稿。进度见 [进度清单](publish/PROGRESS.md)。

顺序译注从第一卷第一章开始。每轮保存页行断点，每章保存章节记录；下次先读 [续译断点](progress/RESUME.md)，从指定锚句接续。

先读 [开篇试译](polish/dev/I-1.md)、[末尾试译](polish/dev/IV.md)，再看 [开篇译注](annotations/I-1.json)。注释分别标明「据来源」「译者判断」「存疑」，不会把一种读法写成唯一答案。

## 本地读本与电子书

仅需 **Python 3.9 或以上版本**。无需 API 密钥，也不调用付费翻译服务。

```bash
python3 scripts/project.py check
python3 -m unittest discover -s tests -v
python3 scripts/project.py build
python3 -m http.server 8000 --directory dist/site --bind 127.0.0.1
```

打开 `http://127.0.0.1:8000`。读本可调字号、行距、字体和版心，提供原文开关、折叠译注、本章检索、译名表与明暗主题；支持手机与键盘操作。所有资源采用相对链接，适配 GitHub Pages 项目路径。

展开段落下方「修订本段」，可改译文及译注，保存后在本页预览。修订保存在当前浏览器，可导出整章 JSON；点击「复制修订并打开 GitHub」，在编辑页全选、粘贴、查看差异并提交。提交后会自动更新公共读本。导出与提交前会联网核对仓库现稿；公共稿若已更新，先刷新并对照，再继续处理本机修订。

电子书生成于 `dist/finnegans-wake-zh.epub`。网页与 EPUB 都从同一份稿件构建，注释可往返跳转。构建工具会检查站内锚点及 EPUB 内部链接。

每次 GitHub 检查通过后，Actions 提供名为 `finnegans-wake-reader` 的下载包。下载并解压即可找到网页和 EPUB。推送 `v*` 标签时另生成 GitHub Release。Pages 启用方式见 [开发说明](DEVELOPMENT.md)。

网页构建仅需 Python。修改阅读器代码时另用 Node.js 22 以上版本运行 `node --test tests/test_reader_model.cjs`，检查修订合并与阅读设置。

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

中文遵循余光中《中文的常态》所倡导的简洁路数：用实义动词，少用「的」，删虚词，少写被动句，避免「之一」及不必要的复数后缀。原著刻意断句、重复、错拼或造词，先辨其用意，再决定怎样译。

详见 [译注规范](docs/EDITORIAL_GUIDE.md) 与 [底本说明](docs/SOURCES.md)。

## 许可与署名

原创中文试译及译注采用 **CC BY-NC-SA 4.0**；工程代码采用 **MIT**。Joyce 原著、外部注释和第三方资料不纳入本项目许可。Faded Page 标明原著在加拿大属公有领域；本项目未镜像该站整部电子书。使用、扩录或发布原文时，请按所在地规则核对权利。

本仓库起步稿由 AI 辅助整理、试译和注释。`reviewers` 为空表示尚无人工审校记录；不得凭自动检查把试译改成已审校。

完整范围见 [LICENSE.md](LICENSE.md)。贡献译文时请注明署名方式与资料出处。
