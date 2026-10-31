# 可复现考据：从疑问到可采用注释

适用：旧注含精确页码、图像、发现者、陌生词源，或来源虽能打开却未必支持断言。先读 evidence-workpack.md；本文件补操作，不另改其字段。命令从仓库根目录执行，工具只需 Python 3 标准库，不依赖某款模型或搜索 API。

## 1. 把复合断言拆开

先冻结章稿、来源表、术语表三项 SHA256，记日期、段落 ID 与范围。后续改稿另记输出版本，不覆盖输入指纹。每题分别问：

1. 原词究竟怎样拼、怎样读？现稿是否多字、少字或移了行号？
2. 所指物是否存在？图题、材质、印刷页、插页与文件页各是什么？
3. 谁写了这项解释？作者明说、引述他人、私人通信和项目推断分别归谁？
4. 这些材料只证明“某人这样读”，还是另有 Joyce 使用此书的证据？
5. 中文须保留什么声音、歧义？注内须说明什么损失？

为最强竞争解释列可检验条件。词音相近不独自证明借用；图像存在不独自证明 Joyce 看过；相邻段落出现另一人名，不许借给本条主张。

## 2. 检索有顺序，也有收束条件

先核作品局部，再追具名评论所引原书。找到可用证据后定点补缺，不无限扩成全书书目。实质研究依次留下 en／zh／ja 检索记录；找不到相关全文也交真实结果。

- **en：**原词精确检索 → 具名论文／专著章节 → 其脚注或原书扫描。发现者署名、版本和页码分别查。网页重印须核原作者、重印者、原出版年与 OCR 说明。
- **zh：**同时试「芬尼根／芬尼根的守灵夜／芬尼根守靈夜」、研究对象译名与英文名。未取得戴从容、梁孙杰等译本原页，不凭报道填译句与页码。
- **ja：**试「フィネガンズ・ウェイク／フィネガンズ・ウエイク」、英文原词、作者片假名及机构库。区分概要、译注、论文、学位审查要旨。概要不是全译；题名不是论证。

每个检索式记入口、日期、查看范围、命中与下一步。只得题录便停在 metadata_read；只得索引摘录便不补脚注。一本论文的原站、镜像与三语转述须连回同源组。

## 3. 先验网页是否真把材料交给你

工具：`.ai/skills/joyce-research/scripts/verify_evidence.py`。

~~~bash
python3 .ai/skills/joyce-research/scripts/verify_evidence.py capture \
  --url https://www.fadedpage.com/books/20180126/html.php \
  --needle 'see peegee ought he ought' \
  --out /tmp/fw-faded-retrieval.json
~~~

它保存请求与最终 URL、状态、内容类型、字节数、响应 SHA256、题名和锚句次数；不保存整部正文，不自动填写 read_state。返回 1 表示未通过检索条件，0 只表示成功取得含锚句的文字。

解析器排除 script、style、template 和带 hidden 属性的内容；它不运行浏览器 CSS／JavaScript。PASS 不证明屏幕实际呈现正文，题名命中也不能升作 passage_read，仍须打开材料核上下文。

真实示范中，该地址曾返回 HTTP 200 书目页，正文锚句缺失。网页工具缓存却能读到正文。两种访问分别记，不能用缓存所见冒称当前下载结果。若工具只显示缓存转录，另存短摘录，注明 capture_method、版本、查看位置与转录局限。

HTTPS 证书失败，记错误。不得关闭证书验证。原出处确有公开 HTTP 版本时，可明确选它并加 `--allow-http`，记录传输未加密；脚本不自动降级 HTTPS。登录、付费、验证码或限流后可换合法公开入口，不能绕过访问控制。

图书 ID 无效时，先查目录或官方元数据搜索，不把空 JSON 认作有效书目。例如：

~~~text
https://archive.org/advancedsearch.php?q=title%3A%28Rois+et+dieux%29+AND+creator%3A%28Moret%29&output=json&rows=10
https://archive.org/metadata/roisetdieuxdgyp00moregoog
~~~

核 title、creator、date、publisher、原扫描提供者与文件清单。1911 和 1937 年见证分别登记，不拿重印本暗换初版。

## 4. 外部见证比对，不能只比两份项目文件

把**实际从外部读到**的短原文写入 witness JSON。至少含 text、basis=external_witness、source_id、url、edition、locator、capture_method。方法只选 web_tool_cached_transcription、downloaded_transcription、manual_scan_transcription，并另记获取时间、工具位置及图形／断字局限。

不可从项目 original 复制后倒填来源。脚本无法识破这种伪造，核查者须重新打开来源。书页、扫描和网站三者差异由人判断。

~~~bash
python3 .ai/skills/joyce-research/scripts/verify_evidence.py compare \
  --candidate manuscript/chapters/I-1.json --segment-id fw-i1-006-13 \
  --witness reports/research/fw-i1-seepeegee-demo/witnesses/fw-006-30-32.json \
  --start 'Well, Him a being' --end 'platterplate.' \
  --out /tmp/fw-006-collation.json
~~~

工具仅合并 Unicode 空白，不删重音、不改大小写、不换引号、不猜连字符。锚句须各自唯一且顺序正确。失败须看逐词 diff，再查影像；不为清除 diff 批量改拼写。局部相等只证明局部文字相等，不能给全段、全章或未编码图形放行。

示范还保存 008 页插句反例：内部文件即使 SHA 一样，对照外部转录仍会出现增句。命令见示范 synthesis.md。将工具输出与观察分开写；退出 1 的反例可表示工具正确拦住差异，不得改写为论文已审。

## 5. 扫描图版必须看图

下载暂存到仓库外，记原 URL、最终 URL、字节数、SHA256；不提交整书 PDF／EPUB。先核扉页年份，再逐页核目标页与插页。记录：

- printed_pages：书上实印页码；无页码图版注明图版号和前后正文页。
- file_pages：PDF 从 1 起计页数；代码索引另列从 0 起计，禁止混称。
- image_observation：亲眼可见的图题、人物位置、版式；历史身份或材料质地另寻依据。
- transcription_status：image_checked／transcription_only／ocr_unverified，说明各自范围。

PyMuPDF 若已安装，可这样渲染；未安装可用系统 PDF 阅读器或现有 pdftoppm，不必为研究安装整套框架。

~~~python
import fitz
doc = fitz.open('/tmp/roisetdieuxdgyp00moregoog.pdf')
# 实例参数，不能套到别的版本：此 PDF 第117页是图版X。
doc[116].get_pixmap(matrix=fitz.Matrix(2, 2).prerotate(90)).save('/tmp/moret-plate-x.png')
~~~

渲染后实际打开图片。OCR 找不到不证明页面没有文字；图片加载成功也不等于看过。不得只读 OCR 就断言“木雕”、人物身份或图版方向。正文页 88、其对页、页后插图和 PDF 第 88 页须分别核对。

## 6. 逐主张回写与验收

每条 claim 关联已读 evidence；每项 evidence 关联版本、定位、reading level 和来源依赖。观察、释义、互文路径与接受史分开。亲查原图可支持图版事实；Troy 的解释只能按其明确范围归给 Troy，不替 Joyce 作阅读证明。

回传三件：evidence.json（证据与未决项）、synthesis.md（取舍与复现命令）、adoption-candidates.json（候选与采用范围）。证据账沿用 evidence-workpack.md 字段；新增 retrieval、file_sha256、file_pages 等字段只补细节。

交整合者前逐问：

1. 下一位执行者能否按 URL、版本、页码、锚句重找材料？打不开时，是否知道当时实际看过什么？
2. 有无把网页成功、目录命中或 SHA 一致写成学术结论？
3. 图像断言有无图像观察？署名断言是否核了原句主语？
4. 三语转引是否误当三份独立证据？缺失材料有无假装查过？
5. 候选能否独立阅读？是否留存最强异议及正文译法损失？
6. 输入是否已改？局部核查是否越界升成整段审校、人工署名或断点推进？

## 真实示范与复演

读 [006.32 图版考据](../../../../reports/research/fw-i1-seepeegee-demo/synthesis.md)，依账重走：FW 局部转录 → Troy 相关小节 → Moret 扉页、页 88、图版 X → 三语状态 → 候选采用。它示范一条注释，不为其余 125 条背书。

复演须交实际命令输出和本轮失败记录，不能复制示范时间、哈希或“已查阅”。输入变动后重跑限定范围；网页改变后保留旧取证，再写新记录。测试命令：

~~~bash
python3 -m unittest discover -s tests -p test_research_evidence.py -v
~~~

测试只验证取证与比对工具。学术判断仍由原页、逐项论证与实际核查者承担。
