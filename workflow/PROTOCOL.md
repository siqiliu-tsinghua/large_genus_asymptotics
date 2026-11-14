# 逐节写作与审核协议

本流程以一个 section 为验收单元。section 内各 subsection 分文件写作，整节在同一个快照上接受数学、可读性和学术规范三类审核。协调者负责状态和工具调用；作者与审核者各自保留本节会话，后续返工与复审复用真实 agent ID。

## 状态与文件

工作状态依次为 planned、drafting、in_review；若有不通过的报告，转为 changes_requested，再经 revising 回到下一轮 in_review；全部通过后为 approved。原有引言初始为 baseline，仍可在后续显式开启修订。

workflow/state.json 是脚本维护的状态记录。每轮材料放在 workflow/reviews/单元/r001/ 等目录；其中 submission.json 冻结文件指纹，math.json、readability.json、academic.json 保存各审核者的报告，author_response.json 保存原作者逐条答复。不同轮的记录不覆盖。

sections/单元/INTERFACE.md 与正文一起提交。它必须列明本节导出的记号、结果及标签、完整假设、引用来源和仍未解决的问题。只有经过验收的结果可在后文当作已建立的输入。

写作次序由 workflow/sections.json 的依赖决定，不必等于最终排版次序。建议先完成 s02、s03、附录 A，再写 s04、s05、s06、s07、附录 B、s08，最后写附录 C；每次仍只开启一个单元。附录 A 的系数计算供 s04 使用，附录 B 的分析估计供 s08 使用，因此需要先完成相应附录。预览始终保留目标章节和附录编号，最终正文仍按第 1–8 节、附录 A–C 排版。

## 首次写作

以下示例 ID 必须替换为 collaboration 工具实际返回的值，不能把示例字符串写成真实分配。

    python scripts/workflow.py status
    python scripts/workflow.py start s02
    python scripts/workflow.py dispatch s02 writer

dispatch 输出一个 collaboration.spawn_agent 调用。协调者执行该调用，收到真实 ID 后立即绑定：

    python scripts/workflow.py bind s02 writer --agent-id /root/s02_writer

writer 只修改自己的 section 目录，填写 INTERFACE.md，并在协调者指定的交接文件中记录已完成事项、主要推理、已查文献、风险和验证命令。首次提示不附带全部历史，由作者按路径读取本节提纲和必要上下文。

## 提交和冻结

作者完成后，协调者先构建单节并检查，再冻结本轮：

    python scripts/build.py --unit s02
    python scripts/validate.py
    python scripts/workflow.py submit s02 --agent-id /root/s02_writer

submit 会拒绝正文和接口中的 WORKFLOW-TODO 占位，记录当前文件指纹并生成本轮提交材料。审核范围包含章节文件、共享前言和文献、AGENTS.md、协议与角色文档、当前章节提纲以及前置章节接口与正文。脚本递归追踪显式的本地 TeX 输入、宏包、类、图片和文献文件；动态输入必须显式加入 shared_inputs，编译时另用 .fls 记录检查是否遗漏了本地输入。论文输入不能放在被忽略的 refs/ 或 build/ 中。任一相关文件变化都会使本轮审核失效。

每轮 source/ 保存原始文件，outline.md 保存本节提纲，unit_definition.json 保存单元定义，changes.diff 保存与上轮的差异。这些审核材料全部有内容校验，登记报告或验收前会重新核对；不得修改已冻结材料。报告模板供填写，不作为审核结论。提交先在临时目录准备，完整后再发布；若写入中断，重新执行原 submit 命令即可重试，旧的未完成目录会保留为被忽略的恢复材料，不覆盖正式历史。

## 三类审核

分别生成审核派发参数：

    python scripts/workflow.py dispatch s02 math
    python scripts/workflow.py dispatch s02 readability
    python scripts/workflow.py dispatch s02 academic

首次调用各自的 spawn_agent，并把返回的真实 ID 绑定到同名角色。作者已提交，保持其会话可复用。可在工具额度内并行运行三类审核；分批运行也不会改变审核归属。

每位审核者按对应 role 文件的检查表填写本轮 JSON 报告。dispatch 会提供准确的报告路径、轮次、快照和模板。审核者完成后，由协调者登记：

    python scripts/workflow.py record-review s02 math
    python scripts/workflow.py record-review s02 readability
    python scripts/workflow.py record-review s02 academic

报告必须使用绑定的真实 agent ID、正确的单元与轮次、同一快照和完整检查表。pass 要求没有未解决 issue；changes_requested 至少列出一个具体 issue。每个 issue 含稳定 ID、位置、严重程度、问题和可执行的修改要求。参考生成的模板。

审核期间保持正文冻结。即使先收到一份失败报告，也应先收齐本轮三份报告，再进入返工，避免作者与其余审核者处理不同版本。

## 原作者返工与原审核者复审

    python scripts/workflow.py revise s02 --agent-id /root/s02_writer
    python scripts/workflow.py dispatch s02 writer

这次 dispatch 输出 collaboration.followup_task，target 必须是原 writer。脚本提供上一轮差异、全部 issue 和答复模板；作者沿用原上下文逐条处理，不重新开启会话。

作者填写上一轮目录中的 author_response.json，每个 issue 必须回应，说明修改或解释，以及涉及的文件。修订完成后：

    python scripts/workflow.py submit s02 --agent-id /root/s02_writer

脚本生成下一轮及新快照。再次 dispatch 三个审核角色时，输出的是发给原 reviewer ID 的 followup_task。原审核者核对自己的旧问题和新差异：旧 issue 要么继续列出，要么进入 resolved_issue_ids，不能无说明地消失。

返工使旧 pass 失效。三位原审核者都要对新快照签署结论；可读性或文献方面的局部修改仍需数学审核者检查是否改变含义。复审提示只附增量材料，角色职责和已读研究背景沿用原会话。

## 验收与默认装配

三份报告均通过后：

    python scripts/workflow.py accept s02

accept 再次核对所有报告、作者答复和文件指纹，实际运行静态检查及集成预览构建，再写入 approved 和构建收据。构建失败不验收。默认装配包含连续通过的正文前缀，再附上连续通过且其依赖都已纳入的附录前缀。正文尚未全部完成时，已验收的支撑附录也可随当前正文出现；最终次序和编号不变。依赖失效或重新进入写作状态时，相应正文及后续部分暂时退出默认装配。

本轮 build/preview PDF 可包含当前单元及其前置依赖，按目标编号排版。验收使用严格构建，未解析的引用或文献会阻止验收；引用必要的后续附录时，先调整依赖并完成该附录。整稿构建还要检查完整的跨章节引用。首次设置中已有引言和摘要的 asdf 是历史占位；新提交不能保留这种占位。

## 会话、所有权与恢复

bind 的角色映射在本节首次绑定后不允许更换；同一 agent 不能占据本节两个角色，也不能跨节改任其他角色。原会话仍可用时，可以跨节复用同一角色：先把真实 ID bind 到新节的相同角色，再 dispatch，脚本就会生成 followup_task；未绑定时才生成首次 spawn_agent。会话复用依靠真正的 collaboration 工具，脚本只记录和校验，不直接调用 API 或自动创建子进程运行模型。

真实工具调用后再登记 ID。若 spawn 失败，不应登记虚构 ID；重新 dispatch 未绑定的角色即可。若发送 followup 失败，先检查原 ID 和会话是否仍可用，不要改映射绕过。

每轮保留交接、源文件快照和差异，便于上下文压缩后继续使用原 agent。进程重启或会话丢失时，文件记录不能替代原会话身份；说明不可恢复的事实后再决定如何重建，禁止静默冒充原作者或原审核者。

只有协调者修改全局文件和工作流状态。审核报告登记后有内容校验；报告被改动、依赖变化或共享规则变化，都会阻止旧签字验收。已经 approved 的单元有实质修改时，用原角色重新 start 并审核；若因此影响依赖章节，status 会标出陈旧结果，后者也需重新审核。

若审核期间共享输入或依赖意外变化，先停止针对旧快照的工作。协调者记录原因，作废本轮并把工作交回原作者：

    python scripts/workflow.py invalidate s02 --agent-id /root/s02_writer --reason "Shared input changed during review"
    python scripts/workflow.py dispatch s02 writer

invalidate 保留旧轮次、已登记的意见和全部角色 ID；允许尚未收齐报告时恢复。作者仍须回应所有已登记的 issue，再重新 submit；复审仍由原审核者完成。它用于恢复失效或中断的轮次，不能把未通过的审核转成通过。若遗留 workflow/.lock，先确认没有正在运行的状态命令，再删除该锁文件；不要删除状态或审核历史。

## 验证脚本

    python scripts/validate.py
    python scripts/build.py
    python -m unittest discover -s tests -v

validate 检查受版本管理文本的 LF、JSON、章节文件和输入路径，以及已登记的内容收据。测试覆盖身份约束、并发工作单元限制、快照失效、失败返工、原审核者复审和验收门槛。
