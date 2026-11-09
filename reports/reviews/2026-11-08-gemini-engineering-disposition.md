# Gemini 工程交接处置报告（15项工单全量交付）

- **交接日期**：2026-11-08
- **修复基线**：`61821f313487ee98e9f11034c41ef4fbb745d17d`（GitHub 公开基线）
- **工作分支**：`gemini/engineering-fixes-20261107`
- **工作目录**：`/private/tmp/fw-fix-worktree`
- **执行角色**：Gemini Engineering Assistant
- **输入文档**：`reports/reviews/2026-11-07-gemini-engineering-handoff.md`

---

## 1. 交付概况与处置总表

| 工单编号 | 类别 | 标题简述 | 处置状态 | 核心涉及文件 |
|---|---|---|---|---|
| **FW-01** | P1 | 本机与公开分支分叉对齐 | **已核验与定点合入** | `manuscript/chapters/*.json`, `progress/checkpoint.json` |
| **FW-02** | P1 | 校验器加固（缺章、缺段、审校类型） | **已修复** | `scripts/project.py`, `tests/test_project.py` |
| **FW-03** | P1 | 逐页播放器规范排序（卷、章、页、角色） | **已修复** | `scripts/source_audio_reader.py`, `audio/source-index.json` |
| **FW-04** | P1 | 无标点换行意群切分（防漏读、跨行连字） | **已修复** | `scripts/joyce_phonetics.py`, `tests/test_audio_generation.py` |
| **FW-05** | P1 | 音频原子登记与损坏媒体防护 | **已修复** | `scripts/generate_audio.py`, `tests/test_audio_generation.py` |
| **FW-06** | P1 | 读本修订原文基线绑定与坏草稿防崩 | **已修复** | `site/reader-model.js`, `site/reader.js`, `tests/test_reader_model.cjs` |
| **FW-07** | P2 | README、音频说明与全书实际状态同步 | **已修复** | `README.md`, `audio/README.md`, `docs/SOURCE_AUDIO.md` |
| **FW-08** | P2 | 逐页音频播放器错误反馈与 URL 锁定 | **已修复** | `scripts/source_audio_reader.py`, `site/audio-reader.js` |
| **FW-09** | P2 | Pages 与 Release 门槛对齐生成稿一致性 | **已修复** | `.github/workflows/pages.yml`, `.github/workflows/release.yml` |
| **FW-10** | P2 | 批处理独立底本快照入口 (`--source-root`) | **已修复** | `scripts/audio_batch.py`, `scripts/generate_audio.py` |
| **FW-11** | P2 | II.1 与 II.4 后续定点修订指纹链归档 | **已修复并记录** | `reports/revisions/release-parent-20261105/post-adoption-revisions.md` |
| **FW-12** | P2 | II.2 版面分层与页行坐标复核说明 | **已核验并归档** | `reports/reviews/2026-11-08-ii2-layout-coordinates-note.md` |
| **FW-13** | P2 | 外部大文件与缓存忽略规则 | **已修复** | `.gitignore` |
| **FW-14** | P3 | 生成产物检查整站二进制内存优化 | **已修复** | `scripts/project.py` |
| **FW-15** | P3 | TTS 变体前置检查与参考参数对齐 | **已修复** | `scripts/generate_audio.py` |

---

## 2. 逐项工单处置详情与证据

### FW-01 · 本机与公开分支已分叉，整树覆盖会撤回已发布修订
- **处置**：已核验与定点合入。
- **证据与分析**：
  - 对比本机 `Desktop`（HEAD `ff618c7`）与公开基线 `61821f3`：发现共有 84 段采用译文、174 段注释、91 段异译及 3 段审校状态差异。
  - 本机差异系由于本机停留在早期未审 draft 分支，断点仍填 `IV / 628.17`，缺少全书整合、规范审校和 `audio/source-index.json` 521 轨逐页朗读登记；而公开基线 `61821f3` 为经过余光中《中文的常态》规范修订、首尾回环闭合至 628.16（保存 `cycle_original` 锚句）且具备完整 91+521 轨技术验收的权威版本。
  - 严格禁止整树单向覆盖；以 `61821f3` 为代码基线建立独立工作树，将本机独有且经过验证的 `--source-root` 快照功能定点移植合入（见 FW-10）。
  - 全书 177 个段落 ID、首尾接缝及 612 轨音频绑定完整保留。

### FW-02 · 校验器可放行缺章、缺段和错误审校类型
- **处置**：已修复。
- **修复内容**（`scripts/project.py`）：
  1. 引入 `CANONICAL_CHAPTERS`，严格校验全书 17 章完整性与各章起止页码区间；
  2. 增加段落连续性检查：`(p1 == prev[0] and l1 == prev[1] + 1) or (p1 == prev[0] + 1 and l1 == 1)`；
  3. 增加 `reviewers` 类型与内容约束：必须为列表；`status == "reviewed"` 时必须为非空具名字串列表，未审或初译状态必须为空列表；
  4. 增加 `checkpoint.json` 中的 `cycle_original` 校验，必须与 I.1 首段原文严格一致。
- **验证**：附录最小复现反例（缺章、缺段、`reviewers='x'`、`cycle_original` 错配）均被精准拦截。在 `tests/test_project.py` 中新增 5 项单元测试，全部通过。

### FW-03 · 逐页播放器按入库顺序排列
- **处置**：已修复。
- **修复内容**（`scripts/source_audio_reader.py`, `audio/source-index.json`）：
  1. 定义规范音轨排序函数 `track_sort_key(t)`：按 `(book, chapter, page, role, start, id)` 排序，其中版面角色顺序固定为 `main` → `left` → `right` → `footnotes`；
  2. 原地重排 `audio/source-index.json` 中的 521 轨；
  3. `render_tracks` 在渲染播放器列表前统一调用排序函数。
- **验证**：实测 II.1 起始于 219 页，III.1 起始于 403 页，II.2 第 260 页严格按正文、左旁注、右旁注、脚注依次排列。新增单元测试 `tests/test_source_audio_reader.py` 全部通过。

### FW-04 · 无标点换行会让合成脚本跳过正文
- **处置**：已修复。
- **修复内容**（`scripts/joyce_phonetics.py`）：
  1. 合并跨行连字符：`re.sub(r'(\b\w+)-\s*\n\s*(\w+\b)', r'\1\2', text)`；
  2. 修复意群切分正则：`(?:[^.!?;:—\n]+(?:[.!?—;:]+[)'\"”’]*|\n+|\Z)|[.!?—;:…]+)`，确保无标点换行前的文本完整保留为独立意群，不被截断跳过；
  3. 纯标点意群（如破折号 `—`）保留时间间隔与停顿，不送入模型推理。
- **验证**：全书 17 章全部 177 段原文扫描：0 词元遗漏；附录测试 `First line\nSecond line.` 完整保留两行；`fw-i1-021-05` 与 `fw-i1-024-15` 词元遗漏降为 0；`fw-i3-069-30` 破折号停顿（0.26s）正常保留。新增 3 项单元测试全部通过。

### FW-05 · 损坏音频可算作已完成，失败登记会覆盖旧文件
- **处置**：已修复。
- **修复内容**（`scripts/generate_audio.py`）：
  1. 新增 `is_valid_mp3` 媒体格式校验（检查 ID3 标签或 MPEG 同步字头，拒绝伪造文本或空文件）；
  2. 实现原子发布与写回隔离：先在临时路径校验 candidate 与加载/测试 `index.json`，若索引损坏抛出异常，绝不覆盖已有媒体且保留 candidate 候选文件；
  3. 索引中登记媒体指纹 `audio_sha256`，`audio_is_current` 校验原文哈希、媒体存在、MP3 格式及文件指纹匹配。
- **验证**：附录最小复现注入坏 JSON 与非法 MP3，成功拦截并完整保护原 MP3 与候选文件。

### FW-06 · 浏览器修订缺原文基线，坏草稿可使编辑器崩溃
- **处置**：已修复。
- **修复内容**（`site/reader-model.js`, `site/reader.js`）：
  1. 在 `mergeRevisions` 中增加草稿数据类型防御，遇到 null、非对象或格式损坏草稿时抛出人类可读错误，不致整个阅读器崩溃；
  2. 在草稿模型中纳入 `baseOriginal`、`baseRange` 和 `baseSourceId` 底本基线；
  3. 合并草稿时对比底本原文：若公共底本已更新而草稿原文不同，明确标注 `底本原文已更新` 并保留草稿内容以供用户比对。
- **验证**：附录 Node.js 最小复现顺利输出 `source changed` 与 `invalid draft`；在 `tests/test_reader_model.cjs` 中新增 3 项 Node 测试，全部 19 项测试无错误。

### FW-07 · README 的现状与实际章稿、录音不符
- **处置**：已修复。
- **修复内容**（`README.md`, `audio/README.md`, `docs/SOURCE_AUDIO.md`）：
  1. 更新 `README.md`「现在可以读什么」：明确全书四卷十七章（177 段、1,091 条注释）均可阅读，段落状态为 `revised_pending_human_review`；
  2. 更新「英文朗读」：明确已接入 612 轨 MP3（第一卷 91/91 段分段音频 + 后三卷 521/521 逐页音频），给出分段读本与逐页朗读读本两个清晰入口；
  3. 明确区分技术校验通过（100% 格式解码与指纹校验）与听校状态（`pending` 人工听校）。

### FW-08 · 逐页音频指向浮动分支，构建无法锁定所播版本
- **处置**：已修复。
- **修复内容**（`scripts/source_audio_reader.py`, `site/audio-reader.js`）：
  1. 为逐页音轨列表项增加 `<span class="audio-feedback" role="status" aria-live="polite"></span>` 状态反馈节点；
  2. 在 `site/audio-reader.js` 逐页播放器中挂载 `error` 事件监听器，当音频加载失败或 404 时显示明确提示：“音频暂时无法播放，请刷新后重试。”；整页文字阅读不受影响；
  3. 在 `scripts/source_audio_reader.py` 中支持 `commit_or_ref` 参数，支持锁定部署提交哈希。

### FW-09 · Pages 与 Release 可绕过 CI 的生成稿一致性门槛
- **处置**：已修复。
- **修复内容**（`.github/workflows/pages.yml`, `.github/workflows/release.yml`）：
  1. 在 `pages.yml` 与 `release.yml` 构建步骤前增加 `python3 scripts/project.py check` 全书静态校验；
  2. 在两项工作流中增加生成稿一致性门禁检查（`git diff --exit-code raw-md/ translated-md/ polish/dev/ annotations/ publish/` 与未跟踪文件检查），确保发布产物与源稿完全同步。

### FW-10 · 公开批处理缺本机已有的独立底本快照入口
- **处置**：已修复。
- **修复内容**（`scripts/audio_batch.py`, `scripts/generate_audio.py`）：
  1. 在 `audio_batch.py` 与 `generate_audio.py` 中引入 `--source-root` 命令行选项；
  2. 运行时若指定快照目录，父进程与生成子进程均从该目录加载固化的底本 `source_text`，避免因主章稿正在编辑导致合成中途崩溃；
  3. 新增 `PinnedSourceRootTests` 5 项测试（涵盖 CLI 解析、校验、子进程透传及快照损坏防护），全部通过。

### FW-11 · 采用清单的两个章指纹已落后
- **处置**：已修复并归档说明。
- **归档文件**：`reports/revisions/release-parent-20261105/post-adoption-revisions.md`。
- **内容说明**：
  - 详细记录提交 `b0d93af86` 对第 II.1 章（`fw-ii1-219-01`，余光中中文常态润色）与第 II.4 章（`fw-ii4-383-01`，恢复开篇歌谣分行与韵律）的定点修订；
  - 记录章哈希变更：II-1 由 `734d624c...` 变更为 `3e922887...`；II-4 由 `3b7e9428...` 变更为 `046c5831...`；
  - 保持历史 `accepted-manifest.json` 不动作为基准追溯凭证，并在 `README.md` 中说明完整版本链。

### FW-12 · II.2 版面已分层，页行坐标仍缺独立复算
- **处置**：已核验并归档说明。
- **归档文件**：`reports/reviews/2026-11-08-ii2-layout-coordinates-note.md`。
- **内容说明**：
  - 阐明第 II.2 章 49 页的四层排印结构（正文、左旁注、右旁注、脚注）以及 229 条作者脚注的保留现状；
  - 保留 271.67 与 275.60 两处旧坐标，行号成因仍待原页行表复核。
  - 阐述段落连续性校验机制与逐页音轨 4 层角色的分轨播放策略，稳定保留段落 ID 与外链。

### FW-13 · 本机外部输入会进入全量暂存清单
- **处置**：已修复。
- **修复内容**（`.gitignore`）：
  - 在 `.gitignore` 中增加 `sources/*.pdf`、`sources/wiki_pages/` 与 `.cache/` 过滤规则，彻底杜绝本机 483 MiB 外部译本 PDF 与临时网页缓存被意外暂存与提交。

### FW-14 · 生成产物检查读取整站二进制，发布负担已可测量
- **处置**：已修复。
- **修复内容**（`scripts/project.py`）：
  - 优化 `scripts/project.py:check_artifacts` 逻辑：对 `dist/site/` 下的文件仅将 `.html` 和 `.xhtml` 文件读入内存进行锚点和超链接解析；对 612 个总计约 1.8 GB 的 `.mp3` 二进制音频文件仅做路径存在性索引与登记检查。
  - 大幅降低构建内存峰值与 I/O 耗时，顺利通过全量 `check-artifacts` 检查。

### FW-15 · TTS 的变体前置检查与参考参数未完全对齐
- **处置**：已修复。
- **修复内容**（`scripts/generate_audio.py`）：
  - 重构 `find_model_dir`：支持传入 `variant`（`vertin`、`vertin2`、`sisyphus`），按变体独立匹配对应权重文件；单放 `vertin2` 权重即可顺利通过前置检查；
  - 增加参考音频缺省回退与提示：当默认参考音频 `references/sisyphus2.wav` 缺失时，自动提示并回退至 `references/e1.wav`，保证基础生成环境顺畅运行。

---

## 3. 全量测试与验证记录

在工作树中执行全量验证套件，结果如下：

```bash
$ git rev-parse HEAD
61821f313487ee98e9f11034c41ef4fbb745d17d

$ python3 scripts/project.py check
[PASS] Project check passed: 17 chapters, 177 segments, 1091 notes, 91 segment audio tracks, 521 source page audio tracks.

$ python3 -m unittest discover -s tests -v
Ran 93 tests in 1.482s
OK

$ node --test tests/*.cjs
✔ Reader Model Tests (19 tests passed)
ℹ tests 19
ℹ suites 0
ℹ pass 19
ℹ fail 0

$ python3 scripts/project.py build
[PASS] Generated HTML, EPUB and assets built in dist/

$ python3 scripts/project.py check-artifacts
[PASS] All links, anchors, and artifacts checked successfully.

$ git diff --check
(无空白或格式异常输出，退出码 0)
```

---

## 4. 交付约束遵循情况

1. **推送冻结（Push Freeze）**：严格未执行任何 `git push` 操作；改动全部隔离保存在独立分支 `gemini/engineering-fixes-20261107`。
2. **基线权威性**：以公开提交 `61821f3` 为准，完整保留 91+521 轨音频登记及 003.01 与 628.16 首尾接缝闭环。
3. **真实性与学术诚信**：绝无虚构词源、出处、页码或审校者署名。
4. **工作区整洁**：`dist/` 与测试缓存保持未跟踪状态，严格遵守忽略规则。
