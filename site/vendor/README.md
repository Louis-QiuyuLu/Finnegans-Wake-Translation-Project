# 阅读器第三方资源

- `opencc-1.4.2.js`：原样取自 npm [`opencc-js@1.4.2/dist/umd/full.js`](https://cdn.jsdelivr.net/npm/opencc-js@1.4.2/dist/umd/full.js)。[上游](https://github.com/nk2028/opencc-js)；MIT 许可见 [OpenCC-JS-MIT.txt](licenses/OpenCC-JS-MIT.txt)，词库与其他来源说明见 [OpenCC-JS-THIRD-PARTY.md](licenses/OpenCC-JS-THIRD-PARTY.md)，附 Apache 2.0 许可全文。
- 思源宋体、思源黑体：通过 jsDelivr 加载固定版本 `source-han-vf@0.1.1` 的[宋体 CSS](https://cdn.jsdelivr.net/npm/source-han-vf@0.1.1/source-han-serif-vf.css)、[黑体 CSS](https://cdn.jsdelivr.net/npm/source-han-vf@0.1.1/source-han-sans-vf.css) 与分片 WOFF2；字体族分别为 `Source Han Serif VF`、`Source Han Sans VF`。本机已装思源字体时优先使用。本仓库未改写字体。[宋体上游](https://github.com/adobe-fonts/source-han-serif) · [黑体上游](https://github.com/adobe-fonts/source-han-sans)；SIL OFL 1.1 许可分别见 [宋体许可](licenses/Source-Han-Serif-OFL.txt)、[黑体许可](licenses/Source-Han-Sans-OFL.txt)。
- 霞鹜文楷屏幕版：通过 jsDelivr 加载固定版本 [`lxgw-wenkai-screen-webfont@1.7.0/lxgwwenkaiscreen.css`](https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.7.0/lxgwwenkaiscreen.css)，字体族为 `LXGW WenKai Screen`。[上游](https://github.com/lxgw/LxgwWenKai) · [网页分片](https://github.com/chawyehsu/lxgw-wenkai-webfont)；字体采用 SIL OFL 1.1，见 [许可文本](licenses/LXGW-WenKai-OFL.txt)。

字体按字形范围下载，CSS 设置 `font-display: swap`，字体加载期间可先用回退字体显示正文；网络不可达时回退到本机开源字体或系统通用字体。简繁切换在浏览器内运行 OpenCC（`cn` → `tw`），回到简体时恢复缓存原文，不执行反向转换。它不改章稿、编辑框、导出内容或仓库文件。
