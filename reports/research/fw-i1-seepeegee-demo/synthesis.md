# 006.32：从“见第88页”追到原图与解释归属

核验日期：2026-11-01（Australia/Sydney）。执行：Codex，AI 定点考据与整合；非人工审校。只修 `fw-i1-006-13` 内 `i1-seepeegee`，不声称重审全段、全章或其余注释。

## 已完成的决定

采用“见第88页”这一具名研究读法，补清 **Moret 1911 年版第88页后、无页码图版 X**。纠正原书链接。图题与地点已看扫描；原交稿“木雕”缺证，删去。Troy 把此联系归给 Maciej Slomczynski，不能把邻段 Atherton 的署名挪来；也不能据此封定首位发现者。

注释现标 `supported`，只指列出的图版事实与具名解释获支持。正文不改，段落仍 `revised`，`reviewers` 仍空，续译断点不动。未证明 Joyce 使用哪一册书、阅读路径或唯一原意。

固定输入与问题见 [workpack.json](workpack.json)，逐主张账见 [evidence.json](evidence.json)，前后注释与采用决定见 [adoption-candidates.json](adoption-candidates.json)。[研究输入包](../../workpacks/fw-i1-006-13.research-v2.json) 保存当前合并段及三项基线。旧工作包坐标已过时，保留追溯，不回填哈希掩盖改动。本轮只重核 006.30–32 局部文字，不宣称全段重新 source-ready。

## 可重走的证据链

### 1. 先核原词，暂不替解释找引文

[Faded Page 转录](https://www.fadedpage.com/books/20180126/html.php) 是 Viking 1958 年第八印本见证，不能冒称逐字核了1939初版。网页工具缓存可读 006.30–32；已独立摘录这三行所需局部，与公共稿比对，文字相等。见 [短摘录](witnesses/fw-006-30-32.json) 与 [比对记录](captures/fw-006-collation-input.json)。

同一 URL 直接 HTTP 请求却转到书目页：200、题名正确、19273 字节，仍没有目标串。取证工具如实退出1；见 [失败记录](captures/fadedpage-http.json)。两次访问不能混说成同一响应。“取得网页”与“取得原词”分两关。

006.33 另含字母图形。此处短摘录停在 006.32，不为当前文字模型对该图形的处理背书，也不改动其后正文或语音。

### 2. 查具名研究，逐句核署名

[Mark L. Troy，1976年博士论文的 HTML 重印](http://www.rosenlake.net/fw/Troy-Mummeries/troybook.htm)，读目录、电子版说明、导论相关段及 **Osiris, Mummified and Roused** 小节。网页标 Eric Rosenbloom 于2002年整理，明说 OCR 尚有错字；目录页码仅供近似定位。小节目录起页32、图II记页33，不冒称核了1976纸本这两页。

正文主句明确提 Mr. Slomczynski，前言交代其全名 Maciej。随后的 Atherton 私人通信段讨论 `fado`，不是图版发现署名。因此，采用“**Troy 将此联系归给 Slomczynski**”，不采用“Atherton 发现”，也不扩大成“已查明最初发现者”。电子文中另把图版说成面对88页；须继续查原书，不能止于转述。

当轮成功读取公开 HTTP 版本，正文保存在仓库外临时目录；工具只提交 [响应指纹和短锚句](captures/troy-http.json)。HTTPS 出现证书／网关问题，未关闭证书验证。HTTP 记录不具加密传输保证。取证 JSON 本身只证明当时取回及检出锚句；上下文归属来自上述实际阅读，下一位核查者仍须重开相关段。

Peter Chrisp 的博客与 Troy 镜像不是新证据票数：前者明引 Troy，后者属同一文本，均归 `troy-1976` 同源组。

### 3. 追到 Moret 1911 原书图版

旧来源 ID `roisetdieuxd00more` 的 Archive 元数据只返回空对象，不能据此声称已核图。用 [Archive 官方题名／作者搜索](https://archive.org/advancedsearch.php?q=title%3A%28Rois+et+dieux%29+AND+creator%3A%28Moret%29&output=json&rows=10) 找到 `roisetdieuxdgyp00moregoog`，核 [文件与版本元数据](https://archive.org/metadata/roisetdieuxdgyp00moregoog)，再下载该项 PDF。没有改用1937重印本。

实际看过以下扫描页，页数从1起计：

- **PDF15：**扉页列 A. Moret、Rois et dieux d’Égypte、Paris、Librairie Armand Colin、1911。
- **PDF116：**正文页首实印88；它不是图版。
- **PDF117：**无页码图版，版号 Planche X。横排，顺时针转90度后核图题：*Veillée funèbre d’Osiris-Ounnefer mort*；括号注明 Abydos、temple de Séti I。
- **PDF119：**正文实印89；PDF118为插页背面。

因此，以“**第88页后图版 X**”定位最清楚；同时保留 Troy “面对88页”的表述作为评论定位，避免误导读者去找 PDF 第88页。可从 [扫描本](https://archive.org/details/roisetdieuxdgyp00moregoog) 或 [PDF第117页](https://archive.org/download/roisetdieuxdgyp00moregoog/roisetdieuxdgyp00moregoog.pdf#page=117) 复核。图像与图题支持浮雕图版、人物与地点；没有木材依据。不把“尚无木材证据”写成已证明绝非木材。

下载 URL、最终 URL、PDF SHA256、字节数、转向与看图范围存 [扫描记录](captures/moret-scan.json)。整部扫描书只暂存于仓库外，未提交。

### 4. 三语比较保留实查层级

**英文：**具名研究解释与原书图版已核本题局部；未查手稿、书信与 Slomczynski 首发。

**中文：**实查“芬尼根＋莫雷＋88”“芬尼根的守灵夜＋第88页”等，返回范围内未取得直接相关学术全文或既有译本原页。不编戴从容、梁孙杰的译句、页码；也不声称中文无人研究此处。

**日文：**[大島由紀夫2018年论文机构记录](https://oacis.repo.nii.ac.jp/records/1525) 可核作者、题名、卷14、页105–122及摘要。摘要说明有逐字译也有撮述，文种为概要，不是全译本。搜索索引显示印刷107页有 Moret／88 的联系，但官方PDF与CORE下载受阻。本轮只记题录、摘要与索引线索，不声称亲读原页、脚注或参考文献，更不能算第二份独立确证。下一步只需补合法可读PDF的107页及书目。

各式检索、阅读层级与受阻处均在 evidence.json。三语状态完整，不等于三语证据齐全。

## 复演命令

先读新版 [可复现考据](../../../.ai/skills/joyce-research/references/reproducible-investigation.md)。下列命令从仓库根目录执行，输出到临时目录，不覆盖本轮历史记录。

~~~bash
python3 .ai/skills/joyce-research/scripts/verify_evidence.py capture \
  --url http://www.rosenlake.net/fw/Troy-Mummeries/troybook.htm --allow-http \
  --needle 'Mr. Slomczynski has discovered' --out /tmp/fw-troy-retrieval.json

python3 .ai/skills/joyce-research/scripts/verify_evidence.py compare \
  --candidate manuscript/chapters/I-1.json --segment-id fw-i1-006-13 \
  --witness reports/research/fw-i1-seepeegee-demo/witnesses/fw-006-30-32.json \
  --start 'Well, Him a being' --end 'platterplate.' --out /tmp/fw-006-collation.json

python3 .ai/skills/joyce-research/scripts/verify_evidence.py compare \
  --candidate reports/workpacks/fw-i1-008-06.json \
  --witness reports/research/fw-i1-seepeegee-demo/witnesses/fw-008-insertion-check.json \
  --start 'This is his big wide harse.' --end 'This is an inimyskilling inglis,' \
  --out /tmp/fw-008-insertion-check.json
~~~

第三条在本轮**退出1**，准确检出旧交稿多出的两句。见 [反例记录](captures/fw-008-insertion-rejected.json)。这说明拦截生效，不能把结果改成“比对已通过”。前两条在本轮成功；日后网页或稿件变动可能失败，须保留新记录再查原因。外部摘录要重开来源核，不得从项目 original 倒填 provenance。

扫描 PDF 可先按 captures/moret-scan.json 下载，再用已安装的 PyMuPDF／系统阅读器打开指定页。渲染参数见技能参考；实际打开图像才算核图。缺依赖时选现成阅读器，不把安装框架当研究成果。

## 本轮技能验证与边界

旧技能压力基线已正确拒绝无据放行，不能写成“基线代理犯错”。真实问题来自此前交稿与格式工具的盲区；新版把容易遗漏的取回、定位、比对步骤变成可执行流程。

另一执行者依新版技能复演：008增句拦截、script 独占锚句、日文题录不得升成正文证据，判断均符合边界。合成夹具仅作测试，不是真实文献；本次也不是 Gemini 实测。复演者重取 Troy 时 DNS／502 失败，未假称重新读到全文。

复演另发现 hidden 属性中的锚句会误算。已先加失败测试，再修解析器；它现排除该属性及子元素。浏览器CSS／JS仍另核，工具不会证明屏幕可见或学术判断成立。工具也不能识破伪造见证、自报核图或错误归属，仍须重开来源。结构检查、工具测试、AI复演与人工审校分别记，详见 [validation.json](validation.json)。
