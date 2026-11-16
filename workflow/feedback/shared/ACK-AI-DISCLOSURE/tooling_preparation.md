# ACK-AI-DISCLOSURE：调度与版式辅助工具准备

基线：`6ebf35034d61bc1bbf3a4a64126e9eec60636939`，具体材料见本轮 request.json 与 `build/ack-ai-20261116/baseline.json`。本会话只新增本报告和本轮忽略目录中的三个辅助脚本；没有修改论文、共享源、生产工具、状态或旧档案，没有执行 pin、编译或任何改变工作流状态的命令。本报告不是论文审核签字。

## 已准备的辅助代码

- `build/ack-ai-20261116/round.py`：协调者专用的显式分阶段 CLI。它调用真实 workflow CLI，检查原绑定 ID、实际作者 ACK 和真实新轮次报告；不会启动模型、编造工具返回、生成作者 ACK 或审核结论，也不代替协调者执行 collaboration 调用。
- `build/ack-ai-20261116/guard.py`：基线、输入范围、原身份、生产工具及 pin 检查。
- `build/ack-ai-20261116/preview.py`：本轮专用 native 预览和 S1 整稿版式伴随稿。不调用会重写 generated assembly 的整稿构建，不改工作流状态。

协调者已告知逐份审读代码并将执行 pin→freeze s01。自该通知起，本会话不再修改三个脚本，避免破坏 pin 中的辅助工具哈希。

## 范围与身份保护

1. 严格保留原 Introduction 文件的完整字节前缀，只允许在后面追加 manifest 指定的两个新输入。两个新文件各含一个不编号 subsection；S1 另可更新接口并新增 disclosure_handoff.md。其他九节的正文、接口、旧 handoff 和已有核算文件逐字节保持基线。
2. 共享允许项为 context、main、新 backmatter，以及协调者后来明确确认的 outline 两处外层请求/范围说明。每个单元实际读取的 outline 片段必须保持原哈希。manifest 只能给 S1 增加两个 subsection，并在 shared_inputs 末尾追加同一个 author_information.tex；其余结构不变。main 只增加 bibliography 之后、end document 之前的作者信息输入，保留原题名、署名、摘要等全部元信息。
3. 五个生产工具相对基线逐字节锁定；不改 scripts/workflow.py 或绕过其锁、依赖检查、提交、报告验证及实际验收构建。旧 Git 冻结记录不允许修改、删除或以重命名逃避检查。
4. 固定顺序为 s01、s02、s03、a、s04、s05、s06、s07、b、s08，只允许一个活动单元。原 writer 为 `/root/s02_writer`，三审核者为基线中相应 `/root/s02_math`、`/root/s02_readability`、`/root/s02_academic`；没有替换或重新绑定入口。
5. 外部 ACK 由原作者实际写入 `workflow/feedback/shared/ACK-AI-DISCLOSURE/UID_writer.md`；S1 使用自己的新 disclosure_handoff.md。ACK 须注明单元、任务名和原作者 ID。辅助代码只复制已有 ACK 到忽略目录、保存原路径和内容哈希，并明确告知审核者真实 ACK 路径，不生成或冒充作者文字。真实工具调用与会话归属仍由协调者实际操作确认。

## 预览与冻结的含义

旧 snapshot_pdf.py 使用的生产章节骨架会遗漏 main 的题名、摘要及文末地址。因此本轮 native 预览直接保留当前 main，只替换章节装配并设置原有节号/附录字母，包含 bibliography 后的地址输入。生产 accept 仍实际运行原有严格构建；本轮预览是补充证据，不替代该门槛。

S1 冻结后另外真实编译完整当前论文，包括后续九节仍未完成本轮元数据复审的旧数学正文。该 PDF 明确标为 **current-layout companion，而非整稿工作流审批**。代码不提前对这些后续单元调用 freshness 通过检查；先核对全部非 S1 文件与基线相同，再记录原始当前输入哈希、组合 source_hash、当时状态、基线签字快照及实际构建记录。三位 S1 审核者应同时检查新文字、末尾两个不编号 subsection，以及作者信息是否确在整稿最后一页底部；代码只保证输入位于 bibliography 后，底部视觉位置仍须真实查看。

每次实际编译检查所有 pass 的 FLS 本地输入，拒绝未冻结输入和退休 C，要求引用收敛、无严格诊断及 Overfull。PDF、TeX、文本、aux 与预览收据均有哈希；冻结 summary 将实际新 snapshot、作者 ACK 与原生/整稿版式证据绑定。后续九节审核只需检查真实白名单差异、新快照和元数据影响，可以沿用原数学推理，但必须重新独立签署完整报告，不复制旧 pass。

## 协调者使用顺序

S1 已经真实 start、派发并由原作者交付，**不要再次 start S1**。共享输入定稿、原作者 STOP 后：

```text
python -B build/ack-ai-20261116/round.py check
python -B build/ack-ai-20261116/round.py pin
python -B build/ack-ai-20261116/round.py freeze s01
```

freeze 真实构建 native、静态检查、提交，然后构建 S1 整稿 companion，输出本轮 summary 和三位原审核者的 followup_task 参数。协调者必须实际调用这些 collaboration 工具并等待各自真实报告；辅助脚本不会执行或声称执行了这些调用。

```text
python -B build/ack-ai-20261116/round.py reports s01
python -B build/ack-ai-20261116/round.py accept s01
```

accept 仅接受实际新快照的三份 pass，真实登记并真实调用生产 accept。对其余九节逐个执行 start UID→实际原作者 followup/外部 ACK/STOP→freeze UID→实际原三位审核者 followup→reports UID→accept UID。start 的输出是待协调者真实执行的工具参数，不是已经完成作者工作。

若有 changes_requested，先用 record UID 收齐并真实登记全部报告，再 revise UID 派回原作者。S1 在 writable 修订阶段可显式重新 pin，旧 pin 版本和旧轮次预览保留。其他九节若需要越出“文件不变”的实质修改，应停止本轮窄范围辅助流程，由协调者明确新范围；不得放宽白名单或伪造 pass。若 submit 后辅助预览因外部工具短暂失败，可用 previews UID 补充同一冻结轮的真实预览；已有 summary 不覆盖，已有相同 ACK 副本可安全核对重用。

## 最终一致性门槛

十节全部对本轮输入重新验收后，协调者另行运行真实完整严格构建、单 TeX 导出与独立编译，再执行：

```text
python -B build/ack-ai-20261116/round.py check-final
```

该步骤检查全部实际新验收、生产收据与 S1 companion 的同一 source_hash，并要求主 PDF、独立编译 PDF 提取的全文与已评 companion 字节一致，三者标签映射一致且仍为 430 个标签。它核验最终 source/PDF 哈希与单文件导出状态，不替代视觉审核或真实论文签字，也不会自动 Git 提交。应在最终提交、HEAD 仍为本轮基线时完成；辅助代码有意拒绝基线之后未经本轮解释的 HEAD。

## 本会话已做的窄验证

只运行语法检查、CLI help、只读 check 和无文件修改的纯检查：当前完整白名单通过；native 保留题名/摘要/署名/bibliography/地址；full companion 选择十个在用单元且不含 C。在内存中替换被读取的科学正文、生产工具或旧引言前缀字节时，保护检查均拒绝。未运行生产状态命令、构建、原科学核算或已有整套测试。

STOP：工具准备完成，所有实际工作流操作、原会话调用和真实构建交回协调者。
