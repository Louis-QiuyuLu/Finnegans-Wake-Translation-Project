# 稿件格式

唯一编辑入口是 `manuscript/chapters/*.json`。字段必须使用标准 JSON，不能写注释或尾逗号。可复制 [段落模板](../templates/segment.json)，填写后插入目标章 `segments`。

## 章

`id` 使用 `I.1` 至 `I.8`、`II.1` 至 `II.4`、`III.1` 至 `III.4`、`IV`。`pages` 是通行页码范围，首尾均计入。`title` 只是卷章编号，不为原著杜撰章名。

`coverage` 分 `not_started`、`partial`、`complete`。最后一项须配 `coverage_review`，说明谁依据什么版本核对全章。不得以有稿段数推算全文百分比。

## 全章英文 `source_text`

`source_text` 独立保存全章英文，不创建缺少中文的假段落。`coverage`、`segments` 与续译断点仍只记录中文译注进度。

- `status: imported`：机械录入，不能写成已审校。
- `source_id`：已登记的文字见证；`imported`：实际录入日期。
- `pages`：章内逐页列表；须与章级 `pages` 首尾范围完全相符。
- `html`：限于书籍排版的 XHTML 片段；保留正文、原作脚注、旁注和图形，不含站点导航或脚本。
- `html_sha256`：UTF-8 片段指纹；`text_sha256`：解析实体后、去除空白的正文指纹，只核抽取损失，不证明语义或空格正确。
- `assets`：片段所用图版名，正文中以 `images/文件名` 引用，实物存 `manuscript/source-assets/`；构建时改写为站内或 EPUB 路径。

页码锚点固定为 `source-page-003` 等，不据此虚填页行。续译时从此见证抽取完整自然段，再核页行并建立工作包；现有双语段 `original` 不随全本重导自动改变。全章导入用 `scripts/import_source.py`，细节见 [导入与校勘](../.ai/skills/prepare-source/references/import-and-collation.md)。`raw-md/` 从全章英文生成；中文阶段稿仍从 `segments` 生成。

## 段

- `id`：全库唯一、仅含小写字母、数字和连字符。提交后尽量不改，避免旧链接失效。
- `locator`：如 `003.01–003.03`；`range` 对应 `[3, 1, 3, 3]`，为闭区间。
- `source_id`：指向 `sources/catalog.json`。
- `original`：见证本文字。段内不沿网页换行，不自动纠正 Joyce 错拼。
- `draft`：初译；`translation`：当前读本采用稿。
- `status`：`draft`、`revised` 或 `reviewed`；`reviewers`：真实审校者姓名或公开账号。
- `notes`：注释列表；`alternatives`：其他译法及理由。
- `source_figures`：有文义作用的旋转字母，独立保存，不塞进朗读文字。每项列 `anchor`（原文唯一锚句）、`letter`（E或F）、`rotation`（顺时针90、逆时针-90）、`replace`（替换近似字符，或紧接锚句插图），另记 `locator`、`source_id` 与核图依据。网页与EPUB用内嵌SVG重绘，便读原文稿用方括号说明方向；不是原刊字形的影印。朗读仍按 `original`，不念图形。

段落须按页行排序，坐标不能重叠。若要细分同一行，先保留整行范围并在同一段解释，不创建重复闭区间。

## 注释

`id` 全库唯一；`lemma` 为所论词句；`kind` 为类别；`certainty` 为证据层级；`text` 为注释正文；`source_ids` 至少填一项且可解析。类别与分级见 [译注规范](EDITORIAL_GUIDE.md)。

脚注按整段附列，以词目对应原文；当前版本不在中文词语上强制绑定浮窗。网页点击编号会展开对应注释；EPUB 使用原生注释与返回链接。

## 更新便读稿

```bash
python3 scripts/project.py check
python3 scripts/project.py generate
```

自动生成稿不要手改。若删除最后一段、移动章文件或更改 ID，须同时清理失效的旧便读稿，并在 PR 说明链接变动。
