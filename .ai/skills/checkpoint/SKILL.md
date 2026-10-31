---
name: checkpoint
description: "Use when saving or resuming translation progress, approaching a context limit, completing a paragraph or chapter, or reconciling manuscript coverage with the next page-line anchor."
---

# 保存断点与上下文

先读 `progress/checkpoint.json`、`progress/RESUME.md`、当前章稿和本批报告。路径均从仓库根目录起算。

阶段和写入责任见 `docs/SKILLS_ARCHITECTURE.md`。断点表示连续合入边界，不能只按最近修改时间、非空稿件或最后出现的章节推算。

## 保存

1. 核对已合入的连续范围。完整段落须有原文、初译、当前译文和出处；未合入的工作文件不计入顺序进度。
2. 在实际底本核下一处坐标与锚句，写 `chapter`、`next`、`next_original`、`updated`。日期用本轮日期，不凭文件名猜进度。
3. `notes` 保留本批结论、存疑点及下一轮所需资料；旧问题未解决便留着。只写事实，不写「已完成」等空泛汇报。
4. 若中断在半段，保留工作包、初译及报告路径，并记最后核对锚句。主断点仍指向未完整合入的段落起点；下一轮先比对，避免重复插段。
5. 更新 `reports/context/<chapter-file-stem>.md`：本章已译范围、实际见过的人物／声形关系、暂定译名、尚未核实之处、下批范围及相关报告。摘要不扩写未读正文，不替代原文证据。

6. 在 `reports/batches/<batch-id>.json` 记录实际阶段、采用的包／稿／报告和未决项；不向冻结输入包回写状态。若公共稿与包的 `baseline` 不同，先查差异，不能仅更新指纹让旧审校看似适用于新稿。

恢复决策和章节摘要格式见 [恢复约定](references/recovery.md)。

## 章末

只有全章正文已录入，并依据指定见证逐项核过覆盖，才写 `coverage: complete` 和 `coverage_review`。抽样、非空文件、IV 篇末样稿均不能证明前章完成。核全章失败时保留缺口，不跳章。

`coverage` 与审校状态分别记录；整章录完不等于人工审校完成。

## 生成与交接

运行 `python3 scripts/project.py generate`，由工具更新 `progress/RESUME.md`、`progress/chapters/`、便读稿、译注与进度清单，不手改这些生成稿。

再按 [contribute](../contribute/SKILL.md) 检查并同步。向用户交代实际已译范围、尚未解决事项和下一锚句；同步成功后才报提交编号。目标为全书时，少量稿段不能算全书完成。

## 交付关口

整合者须在底本实际找到下一锚句，并核前一段结尾与本段开头没有漏接。现有检查器只要求断点大于当前章末段，不会核锚句含义、连续覆盖或研究状态；人工比对不得省略。

只有源码已合入而生成稿落后时，重新生成即可，不重译。只有工作稿而章稿未合入时，复用工作稿接审校，不移动主断点。远端稿比本地新时先合并，再重新核连续范围。部署失败与译文未完成分开记录，不删已经核过的稿件。
