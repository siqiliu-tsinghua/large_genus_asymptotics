# S07-SHARED：defer 流程恢复审查

审核角色：原 workflow_review 会话。

结论：通过。未发现本次新增改动的阻断项；该命令可用于暂存 s07 尚未冻结的首次初稿，再逐节处理共享输入变化。

## 范围与依据

只读审查 `scripts/workflow.py`、`workflow/PROTOCOL.md`、`tests/test_workflow.py` 的本次差异，并检查既有 mutation、start、writer 绑定和依赖新鲜度门禁。未审核本节数学正文，也未更改真实工作流状态、源码、共享输入或旧档案。

`defer` 在 mutation 锁内要求目标为唯一活动单元、调用 ID 与原绑定 writer 相同、状态为 drafting、从未有 submission、没有 accepted 记录且具有 outline_heading。非空原因写入事件后，仅将该单元改回 planned 并释放 active_unit；正文文件、角色映射和历史均保留。s01 基线、审核中、返工中及已验收后重开的章节均无法借此退回首次计划状态。

`start` 的依赖验收与指纹检查没有被放宽；原 writer 绑定也没有被清除或替换。因此恢复工作不会沿用失效前置的旧验收，不会把未通过审核转换成通过。协议明确暂存期间停止该初稿编辑，前置处理完成后由原 writer 会话恢复。

## 验证

- 独立运行 `python -B -m unittest discover -s tests -v`：35 项测试全部通过。新增五项测试覆盖文件与 ID 保留、原因和身份拒绝、基线与冻结历史保护、审核和返工保护，以及恢复时仍拒绝陈旧前置。
- 在 `build/` 下的隔离 fixture 运行真实 CLI：省略 `--reason` 返回非零且状态不变；错误 writer 返回非零且状态不变；合法 defer 保留 writer、保存去除首尾空白的原因，并释放活动位。
- 隔离 CLI 验证前后，真实 `workflow/state.json` 的 SHA-256 一致。
- 只读确认生产 s07 仍为 drafting、round 0、没有快照；本次没有在生产执行 defer。

未发现必须补充的代码修复。此次结论仅认可新增恢复路径；共享输入变化后的章节仍须依既有协议由原角色重新提交、审核和验收。
