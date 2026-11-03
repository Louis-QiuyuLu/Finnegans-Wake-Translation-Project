# 后三卷英文语音工作包

本批依据已发布的 `manuscript/chapters/*.json → source_text`，准备第二、三、四卷英文朗读。三个工作包位于 `audio/source-queues/II.json`、`III.json`、`IV.json`。

II：4章、181页、297项、62182词。III：4章、188页、188项、66774词。IV：1章、36页、36项、12724词。共9章、405正文页、521项、141680词；词数按空白分隔计，扣掉页码及正文脚注跳转号，不等于文学书目标准词数。

## 输入与覆盖

工作包只存章号、页码、文字角色、字符起止及指纹，运行时从公共章稿取文，不另存整书文本副本。每页依次为正文、左旁注、右旁注、脚注，分轨输出；这是本项目的朗读顺序选择。正文脚注跳转编号不读，脚注自身编号保留一次。图形另存清单，不把图像说明冒充作者正文读出。每项至多600词，词形、连字符及标点不自动校改。

`fw-source-*` 是源语音任务ID，独立于中文译注的 `fw-i*` ID。它们不填入 `segments`，不改变 `coverage`，也不推进 `progress/checkpoint.json`。第四卷仍只有原有篇末中文样稿，不因全卷英语队列就变成已译。

工作包每次加载都重新核章稿英文指纹、分轨范围、顺序和逐项原文指纹。删除任务、改起止、换底本或丢章都会拒绝继续；只改中文译文不会使英语任务失效。需要改分块大小或英语底本时，另存工作包和运行目录，先保留旧稿，不换哈希掩盖变化。

重建工作包：

```bash
python3 scripts/prepare_audio_source.py
```

重新生成后应与原工作包逐字节一致；确有底本变更时先说明差异。当前范围与实测耗时见 [准备记录](../reports/source-import/later-books-audio-preparation-20261102.json)。

## 准备好的生成入口

用户随后授权后三卷并发运行；保留第一卷原进程。以下命令须在项目根目录运行，用现有虚拟环境、Vertin模型及e1参考。第一卷沿用 `audio/.batch.lock`；后三卷分别用 `audio/.source-II.lock`、`.source-III.lock`、`.source-IV.lock`。同卷跨运行目录仍互斥，不同卷可并发。

本轮后三卷各用2个CPU线程，分开运行：

```bash
.venv/bin/python -u scripts/audio_batch.py --source-queue audio/source-queues/II.json --run-dir /private/tmp/fw-source-II-20261102 --model vertin --ref e1 --device cpu --threads 2
.venv/bin/python -u scripts/audio_batch.py --source-queue audio/source-queues/III.json --run-dir /private/tmp/fw-source-III-20261102 --model vertin --ref e1 --device cpu --threads 2
.venv/bin/python -u scripts/audio_batch.py --source-queue audio/source-queues/IV.json --run-dir /private/tmp/fw-source-IV-20261102 --model vertin --ref e1 --device cpu --threads 2
```

每条命令结束后先查退出码及该卷 `state.json`。失败时先处理日志，再续跑，不能把 `complete_with_failures` 当作整卷完成。运行目录的 `originals.json` 会冻结重建后的文字和来源绑定，作为断点资料，不提交仓库。恢复同一运行目录会核冻结原文并跳过已存在的现稿候选。上述命令在前台执行；工作包及脚本可以保存，但后台启动须另存日志，不因本文件存在就声称任务已运行。

只试单项时，复制工作包中的实际ID，显式指定隔离输出目录：

```bash
.venv/bin/python scripts/generate_audio.py --source-queue audio/source-queues/II.json --segment fw-source-ii1-219-main-001 --audio-dir /private/tmp/fw-source-II-smoke --model vertin --ref e1 --device cpu
```

源语音模式不准写正式 `audio/` 播放索引。候选、索引和生成凭据都先存隔离目录；这些ID尚未接入网页的中文段落播放器，不能直接塞进正式 `audio/index.json`。采用前须另核原文、解码、波形、完整性和读音，再按页／分轨接入读本。工作包就绪不表示已经生成、听校或上线。

## 耗时估算

当前50段CPU成功记录共33614词、约17.82小时，平均每词1.91秒；最近10段约1.90秒，速度接近。第一卷余约4.1万词（包含当前在跑段及一个待重试段），预计还需18–28小时。后三卷纯推理基准约75小时，计入分块初始化与波动，预留约3–4天；同机串行把第一卷余量和后三卷跑完，约4–5天。

上述数字来自并发启动前的单进程基准，不代表四进程并发后的工期。并发后需根据首批实耗重新估算，不能按四倍提速推断；也不含完整听校、修订和发布等待。机器休眠、负载与重试都会改变用时。估算时本机生成60/91段，采用29/91段，新候选尚未逐段验收。
