# Introduction and abstract r001 readability handoff

- Reviewer: `/root/s02_readability`, original readability role, actually bound to s01.
- Snapshot: `04eabebf2ad9f5337e18bb4caf276664e2a6a2b48a9e4db8ccb4a52e4f8f17bb`.
- Verdict: **changes_requested**.
- Open issue: `READABILITY-001` (minor).
- Resolved issue IDs: `[]` (first formal s01 round).

已完整联读摘要、203行引言、接口、作者交接、职责/共享约定和本轮 focus；沿用早期试写及后续完整正文语境，但未把试写 pass 当作本次整节验收。144词摘要与原作者 proposal 逐字一致，ILW 已展开。所有四个完整定理、六个编号公式及从 g,n 到归一化括号的数学 setup 均独立比对为原字节不变。

首次定义及信息位置清楚：稳定范围、周环/复余维、Hodge 丛与秩约定、栈积分及稳定子权重在第一积分前给出；忘点映射、低亏格例外、积分族与齐次次数随后引出。没有把 psi、kappa 或 Chern-character 符号提前塞入引言，也未添加新的记号别名。j-family/ell、g_2、Bessel 零点、标量 b 与小写积分族的用途保持统一。

背景按数学作用组织，没有成为单纯文献清单。第一路线区分全图尾项、自环重求和与有限 core 计算；第二路线说明顶 Hodge 精确式、Bessel、ILW 输运和两处主奇点。Section 2 后可直接进入 Sections 6–8 的阅读路径明确。附录 A/B 分工可辨，C 只承担 genus 2/3 精确核查及复现指引，有限数据没有被当作渐近证明；条件性 resurgent 预测也只被称为事后对照。

唯一需要局部返工的问题为 **READABILITY-001**：摘要说 “four regimes”，引言 `section.tex:5–12` 却说 “We study two regimes”，二者在联排第1页相邻而没有说明层级。请仅在新增动机段说明四个结果情形归入两大类指标设置，消除数量口径的表面冲突；保留已定摘要、四个定理和原数学 setup，不需要新增符号或重写整节。

实际查看了原生 unit preview 第1–4页以及标题/摘要/S1 联排 companion 第1–5页。公式和标签均可读，段落密度与书目续行版式正常，未发现另需返工的排版问题。标准 unit preview 确实不含摘要；摘要版面判断来自协调者随后提供的独立 native companion，原 preview 未被替换。

已核验17项 frozen/live 输入、artifacts、Engine 指纹、精确 snapshot 及原生收据。Source SHA256 `e39ea3eb4e2ceb460aad736b66876a766c19922c86c54e371bfa3e08615ce3b4`；unit PDF SHA256 `c16034bdd1e568f4430daab9521b5e6f8c676ecae2cd8367c618e96866a44b76`。Companion `build/reviews/s01/r001/frontmatter/frontmatter.pdf` SHA256 `fcc6c6727480135a73700388f47c91de3796865f3267a5319840892045fae7c6`；其 snapshot/source、PDF/entry/helper 哈希、实际摘要输入及 main 仅替换章节装配均核实。两份收据的 strict/layout 诊断为空，`python scripts/validate.py --unit s01` 通过。

私有截图仅在 `build/closing-writing/readability-s01-r001/`。本轮只保存自己的两份报告和 ignored 查看产物，未改源、状态、旧记录、其他报告或冻结输出；未验收 C 或代签旧九单元的后续刷新。收齐三类意见后交原作者局部返工。STOP，保留原会话。
