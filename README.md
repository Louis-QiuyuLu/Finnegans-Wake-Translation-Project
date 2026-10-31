# 《芬尼根的守灵夜》中文译注工程

**James Joyce · Finnegans Wake**

[在线阅读](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/) · [从开篇读起](https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/chapters/I-1.html) · [续译断点](progress/RESUME.md)

循河入梦，逐字寻声。这个工程逐段翻译《芬尼根的守灵夜》，保存底本、初译、修订、译注与异译，再从同一份稿件生成网页和 EPUB。

参考 [QriDoki 的《追忆似水年华》翻译工程](https://github.com/QriDoki/in-search-of-lost-time-translation-project)，另设页行定位、证据分级与首尾联动审校。代码和试译均重新编写，未复制参考项目内容。

## 现在可以读什么

首版 v0.1.0 收录两段试译，附十二条译注：

- **I.1 · 003.01–003.03**：从 riverrun 开始，读到 Howth Castle and Environs。
- **IV · 628.15–628.16**：篇末片段，接回开篇。

全书四卷十七章已建目录；尚无整章译完。两段均待人工审校，不能当作定稿。进度见 [进度清单](publish/PROGRESS.md)。

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

展开段落下方「修订本段」，可改译文及译注，保存后在本页预览。修订保存在当前浏览器，可导出整章 JSON；点击「复制修订并打开 GitHub」，在编辑页全选、粘贴、提交。提交后会自动更新公共读本。公共稿已更新时，页面会提示先对照现稿，避免旧修订覆盖新稿。

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
