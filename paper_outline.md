# 纯 Hodge 积分大亏格渐近：全文结构与定稿计划

本文证明 Introduction 中的 Theorems 1.1–1.4。第 1–8 节与附录 A、B 已完成逐节写作和三类审核；当前工作是以 Git 提交 fa2f374 为基线做全文收尾。旧提纲及旧作者交接保留在 Git 和冻结档案中，其中的“待补”不再代表当前证明状态。具体在用轮次、签字与快照有效性以 scripts/workflow.py status 为准。

四个主定理的陈述保持不变。Theorem 1.1 的二阶输入、核心贡献及严格余项已在第 4 节和附录 A 中完成；Theorem 1.2 保持固定插入指标的展开及其余项；Theorem 1.3 保持原两项公式和相对余项；Theorem 1.4 仍只断言固定离顶差的渐近等价。第 4、6 节的额外系数 Remark 按用户要求省略计算细节，第 8 节的高阶项明确为猜想，这些均不提高四个主定理的证明精度。

## 材料覆盖与证明依赖

| 目标 | 已完成的论证位置 | 主要输入 |
| --- | --- | --- |
| Theorem 1.1 | 第 4 节，附录 A | 第 2 节几何恒等式、第 3 节全图估计、精确 WP 递推和有限核心计算 |
| Theorem 1.2 | 第 5 节 | 第 3–4 节的图估计与矩规则、奇 Chern 特征过滤、Chern 类恒等式 |
| Theorem 1.3 | 第 6 节 | 第 2 节、lambda_g 公式、精确顶点、Bessel 分析和完整树尾估计 |
| Theorem 1.4 | 第 7–8 节，附录 B | 第 2、6 节的精确输入、ILW 专门化、复域与核估计、系数转移和背景比较 |

第 6–8 节不使用 WP 修正系数。第 6 节可在第 2 节之后直接阅读。附录 A、B 分别提供前一条 WP/稳定图路线和后一条 ILW/复分析路线所需的技术论证。附录 C 不属于论文，四个证明均不以其中的低亏格数值为前提。

## 第 2 节 Notation and geometric identities

直接继承引言的积分、次数、稳定范围和归一化约定。全局符号首次定义在引言或本节实际需要之处，不能把协作接口的完整符号表抄成正文开头。g_2、Hodge 下标 j_1,…,j_ell 和其余选字规则见 workflow/context.md。

### 2.1 Intersection conventions and normalization

形式指数按顶次取值，说明指数积分与幂积分的阶乘换算及固定插入的范围。g、n、模空间、Hodge 丛和引言积分族不再重复定义。

### 2.2 Tautological classes and the GRR formula

按 psi、对数 kappa、Chern 特征的顺序引入，并给出余维和 factorial 规范。Mumford GRR 包括标记项和有序节点的半因子；准确解释与 FP00 非对数 kappa 的换算。普通 B_n 保留给 Bernoulli 数。总 Chern 类重写和低次例子为第 5 节服务。

### 2.3 Gluing maps and restrictions of Hodge classes

回顾 GP03 的稳定图术语并明确 flags/腿约定差异；用归一化和留数证明 Hodge 丛边界限制。平凡商丛在标记图乘积上理解，不忽略图自同构的循环空间作用。顶类只保留树，固定离顶差按第一 Betti 数分配。

### 2.4 Boundary exponentials and forgetting markings

ABCDGLW 的边界指数公式给出边核和图自同构权。有理尾次数消失与 KMZ 的置换/分拆反演给出指数 kappa 专门化；保留新标记 psi 的 kappa 拉回修正。区分新插入从一次和从二次开始的不同作用。来源 Remark 在证明后，有限图权核对采用 Example。

## 第 3 节 Uniform asymptotics for stable graph sums

把第 2 节的精确图公式转为第一、第二定理共同需要的一致展开。入口引用已得到的图公式和度数关系，解释先重求和大顶点自环、再按离开大顶点的复杂度展开的原因。

### 3.1 Weil–Petersson inputs in a common convention

统一 WP 体积、后裔、绝对阶乘尺度及椭圆规范。固定标记展开、全类型上界、允许价数增长的 HMT 一致余项各有不同用途，分别署名和换算；不能用固定 n 结论代替全图求和所需的增长价数估计。

技术输入 W26 固定为已核验的 v4。W26v5 作为新版全阶绝对体积展开的背景文献另列，不将 v4 的 profile 定位自动换到新版。

### 3.2 The boundary deformation and the loop contribution

精确联系边界变形 Z_g、WP 体积和引言积分。半边函数 f 与自环函数 S 解释首项 e^{S(u)}；u 的复参数和根号表示按其整级数理解。

### 3.3 A uniform vertex bound and concentration on a large vertex

统一全类型顶点界，并对逐图取绝对值后的总和给出无大顶点和大复杂度尾界。带标签半边配对、高斯矩和阶乘分拆界共同控制完整图集；不能把逐个固定图的估计当作总和估计。

### 3.4 Finite cores and summable remainders

收缩自环时恢复大顶点亏格、保持复杂度，并精确分离 2^p p! 自同构因子。控制全部合法自环尾、后裔尾、核心展开余项和带固定装饰的适用性。按加法一致展开处理首项可能为零的情形。

## 第 4 节 Powers of the first Hodge class

Theorem 1.1 的完整证明已经完成，不再把二阶系数称作候选值或待补工作。第 3 节承担一致尾估计，附录 A 提供精确系数、矩和完整核心表，本节组合这些输入。

### 4.1 Signed loop moments

从成对半边权定义绝对收敛的带符号线性泛函，保留同一自环两端的相关性。它不是概率期望，也不同于引言的标准化 Hodge 括号。

### 4.2 The leading term and the first correction

分别计算 q=0、q=1 核心及体积修正，准确转换相对 Z_g/V_{g,0} 与绝对 Z_g/F_g。用户已指定把 9/(8g) 排为 (9/8)g^{-1}。

### 4.3 The second correction

使用完整 profile、相关矩、低复杂度顶点和 q=2 的 13 个核心。各组贡献来自文内规则和精确输入，不以旧表的代数相加代替推导。绝对体积二阶系数由递推重建；EGGLS 的有条件预测只作独立核对。

尊重新版 W26v5 已给出包括无标记情形的更一般绝对展开这一背景；本文对所需特定 WP 系数的重建不作首创声明。四个纯 Hodge 定理与该背景结果区分叙述。

### 4.4 Proof of Theorem 1.1

恢复阶乘与引言尺度，用完整图尾收束严格余项。证明后的高阶系数 Remark 是用户授权的补充计算说明，其省略细节不改变主定理原有精度。

## 第 5 节 Fixed degree Hodge insertions

本节用第 3–4 节的工具处理固定 Hodge 指标；不导入无必要的一般高阶公式。

### 5.1 A filtration by odd Chern characters

按奇 Chern 特征的权重过滤总 Chern 类，明确固定指标和因子数。用整个装饰图集的界消去超出所需精度的权重。

### 5.2 The two leading coefficients of a single character

把自由标记和指定旗/自环贡献分开计算，清楚说明 labeled-source 计数、GRR 权重、忘点和 factorial 换算。

### 5.3 Proof of Theorem 1.2 and examples

Chern 类代数约化后得到固定乘积展开，说明 g^{-1} 项消失并保留原余项。例子用于解释低次插入，不新增未证明的通用结论。

## 第 6 节 The top Hodge class and Bessel asymptotics

先明确本节证明 Theorem 1.3，再解释精确顶点、完整树尾、Bessel 鞍点和椭圆叶修正的策略。这条路线不依赖 WP 修正系数。

### 6.1 Top Hodge intersections and exact vertices

准确引用 FP03 的 lambda_g 公式，推导精确顶点并覆盖低亏格/零亏格例外。区分 beta_g、积分 b_g 与标量修正常数 b。

### 6.2 The Bessel critical point and a uniform coefficient bound

保留 z_{0,1}、rho 等引言记号；KMZ/Manin–Zograf 提供历史反函数与 Bessel 背景。导出全类型系数界并明确所需参数域。

### 6.3 Stable trees and their tails

对所有树型和亏格分拆给出尾界，分离非椭圆一边项。末尾已有自足的 genus-two Example，由 sine series 和两棵树直接推出 b_2；无需从已撤回的 C 导入该数值。

### 6.4 The first correction and proof of Theorem 1.3

鞍点和椭圆叶贡献给出原两项渐近。证明后的进一步系数 Remark 按用户要求省略计算细节，不升级已证明的统一余项。

## 第 7 节 Linear Hodge potentials and transport at fixed defect

固定离顶差路线的精确代数部分。本文的 genus/defect、ILW 变量和 Borel 规范在需要处首次定义；不能混淆 WP 的 F_g 与线性势的书法字母。

### 7.1 The linear Hodge potential and the first ILW flow

精准引用 Buryak 的 ILW 结果，写出参数和符号换算，保留 string/dilaton 异常项的消去。

### 7.2 A specialization producing the kappa background

用第 2 节忘点公式得到实际 kappa 专门化，按次数处理固定 genus 的恒等式和有限 jets。

### 7.3 Exact recursions and their integration constants

给出输运递推、自由能积分常数和反函数恢复的文内论证；不能把未知常数交给低亏格数值或程序拟合。

### 7.4 One Borel normalization for all fixed defects

统一 factorial Borel 变换，推导 Beta/Dirichlet 核。明确形式恒等式、固定 genus 解析结论与后续统一复域之间的界限。

## 第 8 节 Singularity analysis and Hodge integrals at fixed defect

组合第 7 节精确输运与附录 B 的解析估计，完成 Theorem 1.4；不把背景比较的误差阶冒充主奇点转移的误差阶。

### 8.1 Analytic domains of the inverse Bessel function

在共同复域上选择反函数分支，保留特征线和两侧主奇点的几何限制。

### 8.2 Propagation of the leading singularity

端点分拆和统一核估计传播主奇项，并给出足够的余项与共同凹域。

### 8.3 The transport constant and its factorial

计算输运常数与 h!，区分 x=t_0 和 S-y 的端点距离，避免局部变量遮蔽已有含义。

### 8.4 Inverting the sine transform and transferring coefficients

恢复原始系数时同时处理两处主奇点，完整控制 genus 卷积和原函数恢复；准确引用 FO90 的转移方法。

### 8.5 Comparing the kappa and Hodge backgrounds

用 nef 交数论证控制整个背景变化，明确有限覆盖及原始文献的适用范围。

### 8.6 Proof of Theorem 1.4

恢复阶乘、固定 h 的归一化和常数 24；结论保持相对 o(1) 的渐近等价。最后的 h=1 高阶项明确为猜想，数值表直接引用 LiuData26 的固定提交，只作证据。证明该猜想和确定一般固定 h 的后续项属于后续研究，不是本稿待补的主证明。

## 附录安排与材料取舍

### 附录 A Coefficients and finite cores

A.1 的精确 profile/volume 重建、A.2 的相关矩规则、A.3 的低复杂度顶点推导、A.4 的完整 1/3/13 核心枚举、自同构与积分规则已经写入论文。保留所有必要数学依据；程序只帮助作者核算，不是读者的证明附件。文献定位采用实际版本，W26 的 Appendix C.1 是外部文献定位。

### 附录 B Analytic estimates for transport kernels

保留共同反函数域、正规收敛、两端点估计、局部输运和负实轴原函数的完整证明。主文保留有效假设与结果的作用，不把 B 的统一估计简化为只对固定路径或逐个核项的估计。

### 附录 C Exact low-genus values

已撤回，不编入论文或单文件投稿源。旧来源和审核记录仅内部保留。已知低亏格值不作为主证明的前提，正文数值观察直接引用公开数据。此标题仅为历史工作单元提供定位，不是重新写作任务。

## 定稿范围与交付

1. 清除协作文档中的过期任务状态，保留审核原则、原始证据和历史归档。
2. 逐节润色英文、衔接及版面；已有数学对象直接沿用，局部新对象先定义。陈述后直接接证明，历史与 credit 放证明后的 Remark。
3. 核对书目元数据、实际采用的版本、精确文献定位和规范换算。公开数据只作明确标记的数值证据。用户已决定保留现有署名与通用格式，不补作者单位、邮箱、致谢/基金或指定期刊模板。
4. 由原作者与原三类审核者逐节完成新快照，再联读完整论文，核对四个定理的依赖、固定参数、误差精度、记号与全文归属。
5. 严格编译完整稿；交付目录只含一个内嵌宏、图示与参考文献的 TeX；复制到隔离目录实编并比较正文及标签。内部源、程序、协作文档和历史记录不作为论文附件。

根目录的旧编译产物归档到 build，日常以 build/main.pdf 为准。最终提交记录可复核的源版本和实际验证结果。所有源码使用 UTF-8、LF 和文件末尾换行。当前真实状态以 workflow.py status 为准，本文档不预签尚未完成的定稿审核。
