# 开发与发布

## 环境

网页与 EPUB 构建使用 Python 3.9 以上版本及标准库。阅读器逻辑测试另需 Node.js 22 以上版本；不用安装第三方包或 Pandoc。

```bash
make check
make test
make build
make serve
```

没有 `make` 时，使用 README 中对应命令。`make serve` 仅在本机 `127.0.0.1:8000` 提供预览。

## 构建

`scripts/project.py` 提供四个命令：

- `check`：检查稿件 ID、页行、出处、状态与整章覆盖说明。
- `generate`：从 JSON 生成各阶段便读稿、独立译注、进度清单。
- `build`：先生成便读稿，再构建静态网页和 EPUB，最后检查内部链接。
- `check-artifacts`：单独检查现有构建产物。

可用 `--out /目标目录` 指定产物路径。`dist/` 不提交；便读稿提交到版本库，便于直接审阅。

EPUB 采用 EPUB 3：首个 ZIP 项为未压缩 `mimetype`，含 OPF 清单、spine、导航、正文及注释往返链接。工具会解析 XML 并核对链接；这不等于第三方 EPUBCheck 认证。正式版发布前，仍应在目标阅读器试读。

## GitHub Actions

`ci.yml` 在推送和 PR 时执行检查、测试、构建，并核对生成稿与断点是否同步，包括尚未跟踪的新文件。成功后上传 `finnegans-wake-reader` 下载包，保留 30 天。

`release.yml` 在推送 `v*` 标签时重做检查和构建，将 EPUB 和网页 ZIP 附到 GitHub Release。先更新 `book.config.json` 中版本与日期，再打对应标签。标签必须与配置版本一致；发布说明见 `publish/RELEASE_NOTES.md`。

`pages.yml` 在 `main` 更新时自动部署网页，也可手动触发：

1. 打开仓库 Settings → Pages，将 Source 设为 GitHub Actions。
2. 打开 Actions → Deploy reader to Pages → Run workflow，选择 `main`。
3. 部署完成后，以工作流返回地址为准。默认项目地址为 `https://louis-qiuyulu.github.io/Finnegans-Wake-Translation-Project/`。

网页使用相对路径，不需改写仓库名或配置根路径。工作流使用仓库自动令牌，不需要个人访问令牌。

## 改动阅读器

改 `site/style.css` 或 `site/reader.js` 后重新构建。稿件正文按纯文本转义；不要直接在 JSON 中插入 HTML。检索只查本章已录入段落，涵盖原文、译文和译注；不会搜索尚未录入的原著。

主题、字号、行距、字体、版心及阅读开关保存在浏览器本地。手机目录默认收起；关闭脚本仍能阅读全部正文和注释。

## 网页修订

「修订本段」可修改当前译文及注释正文，保留原文、初译、注释类别与来源 ID。保存后预览，也可导出整章稿件。修改后的段落回到 `revised`，清除原审校署名，等待重新审校。

公共网页以 GitHub 稿件为准。读者可复制整章修订稿并打开对应 GitHub 编辑页，粘贴后提交；维护者直接提交，其他读者通过 PR 贡献。提交成功后，Pages 自动重新部署。本机修订若基于旧稿，导出前须对照现稿确认；未提交修订不会改动公共内容或现有 EPUB。
