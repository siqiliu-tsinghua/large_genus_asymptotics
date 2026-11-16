# 撤回不再需要的末尾附录

正文删除一个已经验收的末尾附录时，不删除其来源、原作者会话、审核报告或验收收据，也不手工修改 state.json。协调者运行：

    python -B scripts/workflow.py retire c --reason "Editorial removal: optional known low-genus examples are not used by the proofs."

命令只允许撤回已验收、快照仍有效、没有在用依赖者的末尾附录；必须先结束当前工作单元。它保留原验收与所有历史记录，记入撤回原因，将该单元标为 retired，并重新生成装配文件。retired 单元不属于论文、不阻塞其后正常验收，也不进入最终单文件导出；不可通过 start 恢复。

引言和其他仍在论文中的章节如需实质修改，仍分别交回原作者、由原审核者审核。不能把附录撤回解释成其数学内容未曾写作或未曾审核，也不能把保留的历史源文件交付为论文的一部分。
