# Section 8 r001 readability handoff

- Reviewer: `/root/s02_readability`, original readability role, actually bound to s08.
- Snapshot: `376e26aba67c4b70f8ca635464c6b17beb4fd20806344c41da8fde23c9c8a9cd`.
- Verdict: **changes_requested**.
- Open issues: `READABILITY-001`, `READABILITY-002` (both minor).
- Resolved issue IDs: `[]` (first formal s08 round).

本轮完整联读六个新小节、入口、冻结提纲、接口、作者交接及 review_focus；只回查必要前置定义和接口，没有把附录 B 的旧 pass 当作第8节的验收。实际逐页查看 native PDF 第27–37页，并抽看第53页参考文献。私有截图仅在 `build/s08-preparation/readability-s08-r001/`。

阅读主线可用：入口先说明证明 Theorem 1.4，再介绍四步路线；正向 m=1 分支保持端点距离、特征线下端恢复平方根的机制在使用处得到说明。有序积分解释了 1/h! 的来源；逆正弦核显示阶乘分母的转换；镜像贡献和允许次数的奇偶性明确给出因子二。边界证明先核对归一化与两个 1/2，再用倒二项式和控制全部亏格/亏损拆分。最后保留两份阶乘比，说明两个 g^h 和常数24的来源，同时区分最终 o(1) 与背景比较的 O_h(1/g)。

全部13个主陈述紧接证明，14个证明包括最后具名定理证明。长证明已有实际功能分段，必要假设不藏于可跳过的 Remark；短的来源 Remark 放在转移证明之后。新临界点、阈值及域在第8节先定义是适当的，因为实际稿件顺序中第8节先于附录 B；不应以工作流先审过 B 为由要求删去这些定义。

需要原作者局部返工：

1. **READABILITY-001** — `04_coefficient_transfer.tex:91–142`，Proposition 8.8 证明，PDF 第32–33页。局部端点距离 `t_0=S-y` 与第7节固定的零时间 `t_0=x` 冲突。改用作用域明确的其他距离名，或直接写 `S-y`，并同步局部记号记录；不改既有零时间、不改数学意义及共享输入。
2. **READABILITY-002** — `05_background_comparison.tex:215–219`，Proposition 8.13 收尾，PDF 第37页。结证方框被挤成靠左的独立一行，紧接8.6标题。仅局部缩短/重排收尾或调整该处结证位置，使方框正常随末行靠右；保留所有估计与引用，勿动既定共享 proof-spacing、10pt、版心或书目设置。新稿需实际复看第37页及8.6衔接。

已核验54项归档/live 输入、submission artifacts、精确 snapshot，以及 source/PDF/entry/helper 哈希。Source SHA256 `d85268f907c49a3f7f8da0b2df68407a2a7da826fddf4493524d7533bd4b2a7f`；PDF SHA256 `916aeb78405e3889fe64227bc9c3046509ae465a334f7c44316d3153fa6b3ba5`。严格诊断及 overfull/layout 列表为空，但实际目视仍发现上述结证位置问题。既有10pt、无showkeys、书目续行顶格及一般证明后留白设置保持。`python scripts/validate.py --unit s08` 通过；独立计数为33个编号式、13个主陈述、14个证明。

本轮只写自己的两份报告及 ignored 截图，未改正文、状态、其他角色报告或冻结输出。协调者收齐三份意见后交原作者统一返工；原会话保留用于新快照复审。STOP。
