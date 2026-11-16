# LAYOUT-TWEAKS：窄范围协调辅助

已先于本轮源码编辑捕获真实工作树基线：`build/layout-tweaks-20261116/baseline.json`，包含 8,362 个文件哈希、十个实际 accepted/fresh 快照及原角色，保留上一轮尚未提交的成果。HEAD 为 `6ebf35034d61bc1bbf3a4a64126e9eec60636939`；捕获时来源哈希为 `ac1263c003ad140c49f99dbb94a523b6a360394826f9442b64d05e6a6afc8420`。本轮不是回到 Git HEAD 重建来源。

唯一新辅助脚本为 `build/layout-tweaks-20261116/coordinate.py`，仅供协调者审读后执行。它不调用 agent，不生成作者 ACK 或审核结论，不修改生产工具、旧 helper/pin/档案，不自动 Git 提交。

## 范围与实际当前状态

只允许 AI 文件精确替换 multi-agent→multi-subagent；main 只在 abstract 与 sections 之间插入一次 tableofcontents；footer 只替换 vfill→vskip 2em。context/outline 的布局说明及 S1 接口可更新，实际数学 outline 片段、其他九节所有文件和既有历史保持基线。S1 只新增 layout_handoff.md；其余九位作者只写本任务目录内的 UID_writer.md。所有原角色 ID 保持不变。

协调者已通过公共 CLI 实际冻结 S1 r009，快照为 `23a01eee352c86a70308c495c6bac5ce6c3888e75852b573e0a8bcb50f9f315a`，此前已实际完成标准 S1 依赖预览及 focused validate。不要再次 start、bind writer、submit、invalidate，或改动冻结材料。

为继续这份真实 in_review 轮次，代码提供 **adopt**：核对新轮次及 freshness，复用 source_hash、strict/with-dependencies 条件和 PDF 哈希均相符的真实既有预提交收据；不重新提交。共同版式稿从同一冻结来源实际构建，明确记录其在实际 submit 之后补充生成，不声称它先于冻结。

```text
python -B build/layout-tweaks-20261116/coordinate.py pin
python -B build/layout-tweaks-20261116/coordinate.py adopt s01
```

## 后续流程

adopt 输出原审核者的真实 followup_task 参数。协调者必须实际执行工具调用并等待真实报告；prepared 参数不构成已经调用 agent。报告只需检查三项外观差异、来源守恒与新精确快照，复用原数学判断，不重算、不重新研究文献或重读证明。

```text
python -B build/layout-tweaks-20261116/coordinate.py reports s01
python -B build/layout-tweaks-20261116/coordinate.py accept s01
```

其余九节按 s02、s03、a、s04、s05、s06、s07、b、s08 顺序，每节 start→实际原作者 followup/外部 ACK/STOP→freeze→实际原三位审核者 followup→reports→accept。start 对已经活动的 drafting 单元不会重复 start/bind。freeze 使用标准生产单节依赖预览和 `validate --unit UID`，已有实际匹配标准构建可复用。不要在下游元数据仍陈旧时运行整稿 validate。

所有正式报告均由公共验证方法核对实际单元、轮次、原 ID、新 snapshot 和完整证据；accept 真实登记并调用公共 accept，仍实际构建。有失败意见时用 record 收齐登记，再由协调者按原公共 revise 流程交回原作者，不能把旧 pass 复制成新 pass。

## 只做一份共同版式证据

共同稿直接使用当前 main 的 abstract、TOC、全部十节、bibliography 和新 footer，只在忽略目录替换装配输入。它明确是 layout companion，后续九节当时尚未通过本轮元数据审批。实际重复 XeLaTeX/BibTeX 至 aux 稳定且没有 rerun 警告，检查本地 FLS 输入、430 个标签与正文/文末版式；页数不固定。协调者真实查看 TOC 和文末作者信息一次，后续审核复用此证据。没有定制单节预览系统或重复文末图片。

十节实际重新验收且 fresh 后：

```text
python -B build/layout-tweaks-20261116/coordinate.py final
```

final 才实际执行完整 validate、严格主稿构建、官方导出和隔离编译，核对其全文与标签和已评共同稿一致。`submission/paper.tex` 从本次白名单建立之初就是唯一明确的生成稿例外；若它变化，必须匹配官方 export SHA、当前 source_hash 及十节真实新验收。不会重现上一轮导出后被旧白名单误拦的问题。日志使用新随机目录，不覆盖已有执行日志。

本会话只写了本轮基线、新脚本及本报告，并做语法和只读 check；未运行状态变更、agent 调用、构建或测试。基线保存后已及时通知协调者可以编辑。收到协调者将审读并执行的通知后，不再修改脚本。

STOP。
