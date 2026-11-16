# ACK-AI-DISCLOSURE：生成稿的精确收尾例外

只读确认：旧 guard.scope 的 Git 白名单不含 `submission/paper.tex`，该文件也不在原 138-file pin 中。正式导出改变它后，旧 `round.py check-final` 会在 check_pin→scope 被拦截。因此不能直接沿用先前准备报告中的最后一条命令，更不能声称该旧 CLI 已通过。

本次仅新增忽略目录中的 `build/ack-ai-20261116/finalize.py` 及本报告，未修改三个已 pin 脚本、pin、旧 summary、生产工具、论文、共享源或状态。新脚本只供协调者审读后显式执行。

## 准确处理

1. 必须先有全部十节的实际新验收，原角色报告均对当前精确快照通过且 fresh，无活动单元；逐份核对实际报告、验收收据和本轮 summary。尚未完成的刷新不能由收尾脚本代办。
2. 导出前调用原 check_pin，完整原 source/manifest/Git/旧档案约束必须实际通过。记录原 pin、baseline、request、状态字节、实际 source_hash 和完整未过滤的 Git delta 文件哈希。
3. 真实依次执行生产 validate、完整严格 build、export、独立编译。每步后逐项核对 138 个 pin 文件、原 baseline/request、原角色、状态与实际验收、source_hash 均未改变；Git 工作树相对执行前只能新增或改变这一份 `submission/paper.tex`，其 SHA 必须等于官方 export 收据。没有 monkeypatch guard、Git 或工作流。
4. 独立编译必须是真实生产命令成功，结果绑定同一生成源与 source_hash，PDF 哈希匹配、无项目运行时输入、文本一致、标签仍为 430。最后直接调用未修改的 `round.final_comparison` 函数，实际比较主稿、单 TeX 独立编译稿与已评 S1 companion 的全文和标签；不运行或冒称通过旧 check-final CLI。
5. 每次执行使用新的 `finalizations/时间-随机标识/` 保存真实命令退出码、日志、逐步不变量及前后收据/产物副本。不会覆盖旧 summary；若已有 `final-comparison.json` 则拒绝执行。中断后保留真实失败记录，不自动回滚生成源、不伪造成功、不盲目重跑一次性入口。

## 协调者用法

全部刷新完成后、最终 Git 提交之前：

```text
python -B build/ack-ai-20261116/finalize.py --check-only
python -B build/ack-ai-20261116/finalize.py --execute
```

check-only 只读检查，不写日志、构建或导出。execute 才会运行真实管线；源码、审核及 pin 不变，唯一对外生成文件例外是明确授权的单 TeX。它不自动提交 Git。若导出后发生失败，先检查该唯一执行目录中的 failure.json 和真实命令日志，由协调者决定后续恢复，不能通过修改旧 pin 或旧报告“恢复通过”。

本会话只做了语法、CLI help、纯路径差异检查，并再次确认三个旧脚本仍匹配原 pin；未执行生产检查管线、编译、导出、独立验证或状态命令。本报告是工具收尾说明，不是论文审批。

STOP。
