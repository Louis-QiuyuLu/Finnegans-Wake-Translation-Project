# 阅读器第三方资源

- `opencc-1.4.2.js`：原样取自 npm `opencc-js@1.4.2/dist/umd/full.js`。上游：https://github.com/nk2028/opencc-js 。MIT 许可见 `licenses/OpenCC-JS-MIT.txt`；词库与其他来源说明见 `licenses/OpenCC-JS-THIRD-PARTY.md`，附 Apache 2.0 许可全文。
- 思源宋体、思源黑体：通过 jsDelivr 加载固定版本 `source-han-vf@0.1.1` 的分片 CSS 与 WOFF2；字体族分别为 `Source Han Serif VF`、`Source Han Sans VF`。本机已装思源字体时优先使用。本仓库未改写字体。上游：https://github.com/adobe-fonts/source-han-serif 、https://github.com/adobe-fonts/source-han-sans 。SIL OFL 1.1 许可见 `licenses/Source-Han-*-OFL.txt`。
- 霞鹜文楷屏幕版：通过 jsDelivr 加载 `lxgw-wenkai-screen-webfont@1.7.0/lxgwwenkaiscreen.css`，字体族为 `LXGW WenKai Screen`。上游：https://github.com/lxgw/LxgwWenKai ，网页分片：https://github.com/chawyehsu/lxgw-wenkai-webfont 。字体采用 SIL OFL 1.1，见 `licenses/LXGW-WenKai-OFL.txt`。

字体按字形范围下载，`font-display: swap` 保证正文先显示；网络不可达时回退到本机开源字体或系统通用字体。简繁切换在本机运行 OpenCC（`cn` → `tw`），回到简体时恢复缓存原文，不执行反向转换。它不改章稿、编辑框、导出内容或仓库文件。
