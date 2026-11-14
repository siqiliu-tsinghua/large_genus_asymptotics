# 纯 Hodge 积分大亏格渐近的后续章节提纲

本文的写作目标是完整证明 Introduction 中的 Theorems 1.1–1.4。后续正文宜围绕两条证明路线组织：第一条由 Weil–Petersson 交数和稳定图展开得到纯 $\lambda_1$ 及固定低指标插入的渐近；第二条由 $\lambda_g$ 公式、Bessel 临界点和线性 Hodge 势的 ILW 方程得到顶类及固定离顶差的渐近。

建议保留 Introduction 中四个定理的顺序。第 2 节统一几何约定，第 3 节建立供前两个定理共同使用的估计，第 4、5、6 节分别完成前三个定理，第 7、8 节共同完成第四个定理。第 6 节只依赖第 2 节，可在引言的阅读指南中作为较短的独立入口。

当前最明确的待补工作是第一定理的二阶系数：第二版讲义显式算到 $g^{-1}$；$g^{-2}$ 的候选值和分组贡献来自较早的计算笔记。需要重建各组计算及其文献输入，再与统一余项估计合并。以下出现的引理、命题编号均为拟定结构，尚不表示相应证明已经完成。

## 材料覆盖与证明依赖

| 目标 | 现有材料中的主要位置 | 正文需要完成的组织 |
| --- | --- | --- |
| Theorem 1.1 | 第二版讲义第 2 节；纯 $\lambda_1$ 笔记第 4 节及表 2 | 分开建立图尾估计、有限核心展开和显式系数计算，补齐二阶系数的完整计算链 |
| Theorem 1.2 | 第二版讲义第 6.1–6.3 节 | 将一般装饰图估计与 $\mathrm{ch}_3$ 的两项计算分开，随后用 Chern 类恒等式收束 |
| Theorem 1.3 | 第二版讲义第 3.1–3.3 节 | 先给精确顶点公式，再给树尾估计，最后计算无边项与椭圆尾 |
| Theorem 1.4 | 第二版讲义第 4–5 节 | 将精确 ILW 递推、复解析估计、常数计算和背景比较拆成独立模块 |

前两个定理共用第 3 节，但第二定理不需要第一定理的二阶系数。第三定理的证明不使用大亏格 WP 体积渐近。第四定理使用第三定理证明中的 Bessel 归一化和第 2 节的忘点公式，不依赖前两个定理的显式修正系数。这样的依赖关系应在引言末尾说明，以免读者误以为所有证明构成一条不可分割的长链。

## 第 2 节 Notation and geometric identities

本节解决三个问题：积分采用什么规范，节点和忘点如何作用于 Hodge 类，以及指数积分如何恢复成原始幂积分。证明中局部使用的 ILW 和 Borel 变量留到第 7 节定义；全局记号在此固定。

### 2.1 Intersection conventions and normalization

本节直接继承引言在首次使用处明确的全局交数、次数及归一化约定，从形式指数的次数截断、指数积分与幂积分的换算等本节实际任务切入。引言已固定的 $g,n,\overline{\mathcal M}_{g,n},a_g,b_g(h),b_g,\langle P\rangle_g,N_g,g_2$ 不在正文开头重讲或列清单；必要的信息保留在协作接口中供核对。重要定义只有在有助于理解当前论证时才简短回顾或回指。$3g-3$ 直接写出，不另设别名。WP 公式中反复使用的常数在首次需要时再定义为

$$
\alpha=2\pi^2.
$$

若 $Q$ 的余维为 $w$、$L$ 为除子且 $0\leq w\leq3g-3+n$，首先写出反复使用的换算

$$
\int_{\overline{\mathcal M}_{g,n}}Qe^{cL}
=\frac{c^{3g-3+n-w}}{(3g-3+n-w)!}
\int_{\overline{\mathcal M}_{g,n}}QL^{3g-3+n-w}.
$$

用一个简短的记号表说明哪些指标固定、哪些随 $g$ 增长。尤其区分固定的插入指标、固定的离顶差 $h$，以及图求和中会增长的顶点价数和自环数。误差项允许依赖固定插入与固定截断阶。

写作与审核遵守 workflow/context.md 的记号约定。新符号在全文首次使用前定义，已有定义不逐节重复；以下为内部选字规则，不应复制成正文清单。Hodge 类下标固定用 $j_1,\ldots,j_\ell$，$\ell$ 是该乘积的因子数。标记编号用 $i$，列表位置或局部求和指标可用 $k$；图的自环数用 $p$，核心复杂度用 $q$。不把 Bessel 零点改称 $j$，不把 $\ell$ 用作自环数。新增专名须具有反复使用的独立作用；单次出现的短表达式直接写出，局部符号的类型、范围和作用域须在首次使用前交代。

不再用讲义中的字母 $A$ 表示 $2\pi^2$，也不在不同章节把 $D$ 同时用于 $3g-3$ 和 $2g-3$。一点 Hodge 系数统一记作 $\beta_g$，避免与第三定理中的修正常数 $b$ 混淆。两个不同的顶点积分分别加上 WP 和 top 上标。

### 2.2 Tautological classes and the GRR formula

沿用引言中 Hodge 丛 $\mathbb E$ 及其 Chern 类 $\lambda_j$ 的定义。本小节先依次引入引言尚未定义的 $\psi$ 类、$\kappa$ 类和 Chern 特征，再陈述 GRR 及其推论。

**余切线丛与 psi 类。** 令 $\varpi:\mathcal C_{g,n}\to\overline{\mathcal M}_{g,n}$ 为万有稳定曲线，$s_i$ 为第 $i$ 个标记截面，$\omega_\varpi$ 为相对对偶化层。定义

$$
L_i=s_i^*\omega_\varpi,\qquad \psi_i=c_1(L_i).
$$

说明 $L_i$ 在 $[C;p_1,\ldots,p_n]$ 处的纤维是 $T_{p_i}^*C$；随后证明中的后裔插入即为这些 $\psi_i$ 的幂。

**Kappa 类。** 令 $\pi:\overline{\mathcal M}_{g,n+1}\to\overline{\mathcal M}_{g,n}$ 为忘去最后一个标记并稳定化的映射。在已定义的 $\psi$ 类基础上，采用对数 $\kappa$ 约定

$$
\kappa_a=\pi_*(\psi_{n+1}^{a+1}),\qquad a\geq0.
$$

**Chern 特征。** 写 $\mathrm{ch}_a=\mathrm{ch}_a(\mathbb E)$。若 $x_1,\ldots,x_g$ 为 $\mathbb E$ 的形式 Chern 根，则

$$
\mathrm{ch}_a=\frac1{a!}\sum_{\nu=1}^g x_\nu^a\quad(a\geq1),
\qquad
c_t(\mathbb E)=\sum_{j=0}^g\lambda_jt^j
=\prod_{\nu=1}^g(1+tx_\nu).
$$

统一说明 $\psi_i$、$\kappa_a$、$\mathrm{ch}_a$ 的复余维分别为 $1,a,a$，且 $\mathrm{ch}_1=\lambda_1$。在列出 GRR 前，引入模叠上的总边界除子类 $\delta$，用 $t/(e^t-1)=\sum_{k\geq0}B_kt^k/k!$ 定义普通字体的 Bernoulli 数；积分统一使用小写 $a_g,b_g(h),b_g$，不另设字体来区分两者。

**引用结果 2.2，Mumford 的 GRR。** 按本节的对数 $\kappa$ 约定写出带标记公式，包括 $-\sum_i\psi_i^a$ 和有序节点推前的 $1/2$。特别给出

$$
12\lambda_1=\kappa_1+\delta-\sum_{i=1}^n\psi_i,\qquad
\mathrm{ch}_{2a}=0\quad(a\geq1).
$$

引用 [Mum83, §5, (5.2), Corollary (5.3)] 及 [FP00, §1.1, Theorem (Mumford)]。FP00 的 $\kappa$ 使用非对数对偶化层；说明它等于本文 $\kappa_a-\sum_i\psi_i^a$，并解释换算；参见 [FP00, §1.3, (16)]。不把稳定映射虚基本类版本的 Proposition 1 当作本文公式未经换算的直接出处。

**引理 2.3，总 Chern 类的重写。** 从形式 Chern 根直接推导

$$
c_t(\mathbb E)=
\exp\left(\lambda_1t+
\sum_{\substack{a\geq3\\a\ {\rm odd}}}(a-1)!\,\mathrm{ch}_a\,t^a\right).
$$

紧接着列出 $\lambda_2=\lambda_1^2/2$ 和 $\lambda_3=\lambda_1^3/6+2\mathrm{ch}_3$。这两个例子为第五节的切入作准备。

### 2.3 Gluing maps and restrictions of Hodge classes

开头说明本小节回顾经典材料：稳定图术语与黏合乘积采用 [GP03, Appendix A.1]，Hodge 丛约定参照 FP00。明确 GP03 将配对半边与腿分开、半边上的对合无固定点；本文的 flags 包括腿，腿对应对合固定点。其余差异在相关定义处清楚说明，不把不同约定笼统说成完全相同。

定义稳定图、腿、半边、价数、图自同构群和黏合映射。写清

$$
g=\sum_v g_v+b_1(\Gamma),\qquad
\sum_v(2g_v-2+n_v)=2g-2+n.
$$

**引理 2.4，Hodge 丛的边界限制。** 用归一化曲线上的留数解释正合列

$$
0\longrightarrow\bigoplus_v\mathbb E_v
\longrightarrow\xi_\Gamma^*\mathbb E
\longrightarrow\mathcal O^{b_1(\Gamma)}
\longrightarrow0
$$

在标记图乘积覆盖上的含义，并据此得到总 Chern 类的乘法公式。平凡商丛的陈述限于该乘积；图自同构在循环空间上的作用可以非平凡。

**推论 2.5，顶类与离顶差的分配。** $\lambda_g$ 的限制只保留树；对于 $\lambda_{g-h}$，可能出现的项满足

$$
b_1(\Gamma)\leq h,\qquad
\sum_v h_v=h-b_1(\Gamma),\qquad
\xi_\Gamma^*\lambda_{g-h}
=\sum_{\sum h_v=h-b_1(\Gamma)}\prod_v\lambda_{g_v-h_v}.
$$

这条推论同时解释第六节为何只需求树，以及第八节不可分离节点为何把差指标从 $h$ 改为 $h-1$。完整 Hodge 丛在边界上的处理可参照 [LX26b, Proposition 4.4] 中的归一化论证。

### 2.4 Boundary exponentials and forgetting markings

本小节的引理、命题陈述后直接接证明。来源、credit、版本与记号换算移入证明后的简短 Remark，图权重核对放入有单一用途的 Example；忘点约定和忘去一个标记时所需的代数比较按功能模块化，但保留所有必要定义与证明。原始版本标识放入参考文献，用精确定位的引用代替正文中的裸 arXiv 编号。

**命题 2.6，边界指数的稳定图公式。** 引用 [ABCDGLW23, Lemma 3.10, (3.18)–(3.22)]，给出本文所需的专门化。用节点法丛的第一 Chern 类 $-\psi_+-\psi_-$ 解释单边核

$$
K_a(x,y)=\frac{1-e^{-a(x+y)}}{x+y}
=\int_0^a e^{-t(x+y)}\,dt.
$$

说明这是形式幂级数恒等式，并用一个自环和一条分离边展示自同构因子。图公式归于原作者；本文只证明本问题的换算和局部解释。

**引理 2.7，有理尾的次数消失。** 先给出忘去一个标记时的余切类和对数 $\kappa$ 类比较式及其代数证明。若每个新标记都带正次 $\psi$ 插入，则含一个旧标记或不含旧标记的被压缩有理尾分别有维数 $k-1$ 或 $k-2$，而 $k$ 个新标记的插入次数至少为 $k$。由此消去相关边界修正；$\kappa_1$ 的拉回仍保留 $-\sum\psi_{\mathrm{new}}$，不能将这一项同时消去。

**引理 2.8，忘点的置换公式与分拆反演。** 引用 [KMZ96v1, Theorem 2.2, (2.6), Lemma 2.2.1, (2.8)]，写出推前公式及其反演。至少详细演示

$$
\kappa_a\kappa_c
=\pi_{2*}(\psi_{n+1}^{a+1}\psi_{n+2}^{c+1})
-\pi_{1*}(\psi_{n+1}^{a+c+1}).
$$

**推论 2.9，指数 kappa 的专门化。** 再推导

$$
e^{\kappa_1}
=\sum_{k\geq0}\frac1{k!}\,
\pi_{k*}\prod_{i=1}^k
\psi_{n+i}(1-e^{-\psi_{n+i}}).
$$

明确区分两种次数条件：每个新标记的次数至少为一足以消去上述有理尾边界项；指数专门化的每个新因子从二次开始，忘点后余维至少为新标记数，因此固定亏格时求和有限。后续证明直接引用引理 2.7，并在附加 $\kappa_1$ 背景时保留新 $\psi$ 项。

## 第 3 节 Uniform asymptotics for stable graph sums

本节建立第一、第二定理共同使用的分析工具。开头先解释现象：大顶点上的每个固定数目自环都能贡献首阶，因此应先对自环重求和；剩余小顶点的总复杂度才决定逆亏格的阶数。随后给出使这幅图景严格成立的估计。

### 3.1 Weil–Petersson inputs in a common convention

定义

$$
V_{G,n}(\mathbf y)
=\int_{\overline{\mathcal M}_{G,n}}
\exp\left(\alpha\kappa_1+\frac12\sum_iy_i^2\psi_i\right),
\qquad V_{G,n}=V_{G,n}(\mathbf0),
$$

其中 $\mathbf y=(y_1,\ldots,y_n)$ 为非负实边长；$L_i$ 继续表示第 2.2 节的余切线丛。同时定义标准化后裔

$$
[\tau_{\mathbf d}]_{G,n}
=\prod_i2^{2d_i}(2d_i+1)!!
\int e^{\alpha\kappa_1}\prod_i\psi_i^{d_i}.
$$

在一个带明确来源的命题中汇集三种不同用途的输入：

| 输入 | 来源 | 在本文中的用途 |
| --- | --- | --- |
| 固定 $n$ 的体积展开及 $c_1(n)$ | [MZ15, Theorem 1.2, Remark 1.3, Corollary 1.5] | 识别显式系数 |
| 全部稳定类型的体积和后裔上界 | [SW25, Lemmas 14, 18]，后裔非负界参见 [W26, Lemma 6.1] | 控制整个图和 |
| 后裔比与两种体积比的一致余项 | [HMT25, Theorem 4.2, A1, A3, A4] | 允许价数和自环数增长，并正当交换展开与求和 |

把 HMT 的原始阈值和误差的多项式依赖至少完整转述一次，再抽出本文在 $n=O(\log g)$ 区域使用的简化版本。WP 绝对常数由 [LX26, Corollary 1.2] 输入，并同时注明 [W26, Corollary 1.2] 的独立结果。

单列 $\overline{\mathcal M}_{1,1}$ 的规范检查：本文的 $V_{1,1}=\pi^2/12$。原文中可能采用的椭圆对合规范，需要在引用时换算。

### 3.2 The boundary deformation and the loop contribution

设

$$
F_g=\frac{(2g-3)!(4\pi^2)^{2g-3}}{\sqrt g},\qquad
Z_g(u)=\int_{\overline{\mathcal M}_g}
e^{\alpha\kappa_1+\alpha u\delta}.
$$

先建立精确关系

$$
Z_g(0)=V_{g,0},\qquad
\frac{Z_g(1)}{F_g}=\frac{a_g}{N_g}.
$$

定义 WP 顶点函数 $W^{\rm WP}_{G,n}(\mathbf t)=\int e^{\alpha\kappa_1-\sum t_i\psi_i}$。后裔展开的首阶半边函数为

$$
f(t)=\sum_{r\geq0}\frac{(-t/2)^r}{(2r+1)!}
=\frac{\sin\sqrt{t/2}}{\sqrt{t/2}}.
$$

以 $p\geq0$ 表示自环数，用固定自环数的计算引出

$$
S(u)=\frac12\int_0^{\alpha u}f(t)^2\,dt
=\operatorname{Cin}(2\pi\sqrt u),\qquad
\sum_{p\geq0}\frac{S(u)^p}{p!}=e^{S(u)}.
$$

根号表达式按 $u$ 的整级数解释。这一段提供首项的几何动机；全体图的渐近结论放在完成下面估计之后。

### 3.3 A uniform vertex bound and concentration on a large vertex

**引理 3.1，统一顶点界。** 在半边参数的固定有界集上建立

$$
|W^{\rm WP}_{G,n}(\mathbf t)|
\leq C B^n(4\pi^2)^{2G-3+n}
\frac{\Gamma(2G-2+n)}{\sqrt{2G-2+n}},
$$

其中 $C,B$ 不依赖 $G,n$。低复杂度的有限例外直接核对。

令 $H=2g-2$。复杂度大于 $H/2$ 的顶点若存在便唯一；称它为大顶点，并记其余顶点的复杂度之和为 $q$。

**命题 3.2，图尾估计。** 对每个固定 $M$，没有大顶点的图和 $q\geq M$ 的图，其绝对总贡献为

$$
O_{\mathcal K,M}(F_g g^{-M}),
$$

其中 $u$ 位于固定紧集 $\mathcal K$。

长证明拆成三个引理：带标签的半边配对与图自同构权；高斯矩控制配对数后的指数生成函数界；复杂度分拆的阶乘尾界。本节给出完整估计及区间拆分，不依赖尚未验收的附录。这里必须估计逐图取绝对值后的总和，才能用于带符号边核。

### 3.4 Finite cores and summable remainders

**引理 3.3，固定复杂度下的核心有限性。** 令 $p$ 为大顶点上的自环数。收缩这些自环，并相应增加大顶点的亏格，保持顶点复杂度后，固定 $q$ 只剩有限种核心，并有

$$
|\operatorname{Aut}\Gamma|
=2^pp!\,|\operatorname{Aut}\Gamma_{\rm core}|.
$$

**引理 3.4，自环尾与后裔尾。** 对 $p>\log g$ 的合法图给出任意固定逆幂阶的尾界；对保留的自环数和后裔次数验证 HMT 的阈值。说明如何把展开系数延伸后的求和尾一并控制。

**命题 3.5，可逐项求和的核心展开。** 对每个固定截断阶 $K\geq0$，固定核心的余项应最终达到

$$
g^{-K-1}\frac{C^{p+1}(1+p)^s}{p!}
$$

这样的可求和形式，而不是停在带 $(\log g)^s$ 损失的界。于是得到 $Z_g(u)/V_{g,0}$ 在紧集上的任意固定阶展开，其首项为 $e^{S(u)}$。

**推论 3.6，有限阶导数和带固定装饰的适用性。** 说明局部一致性如何允许 Cauchy 求导。对固定 $r$ 条编号外腿及独立复参数，证明相应的 $Z_{g,r}(u;\mathbf t)/V_{g,r}$ 展开，首项为 $e^{S(u)}\prod_{i=1}^r f(t_i)$。带腿计数使用截断指数多项式的导数，不能无端增加一个 $g^r$ 损失；换回 $F_g$ 才有体积尺度带来的 $g^r$。这是加法形式的一致展开，不能除以可能为零的首项，特别是 $f(\alpha)=0$。固定外腿 psi 插入由参数求导处理；额外指定旗或边的求和须明示允许的核、次数、计数和多项式损失，未核实的任意装饰不作笼统承诺。第五节再逐项核对具体 Chern-character 装饰的适用性。

## 第 4 节 Powers of the first Hodge class

本节完成 Theorem 1.1。开头用一段证明导读说明：第三节已将问题化为有限种核心和绝对收敛的自环矩；首项来自 $q=0$，一阶修正来自 $q=0,1$，二阶修正来自 $q=0,1,2$。WP 端点提供绝对归一化。

### 4.1 Signed loop moments

定义单自环权

$$
w_{ab}=\frac12\int_0^\alpha
\frac{(-t/2)^{a+b}}{(2a+1)!(2b+1)!}\,dt.
$$

用一个引理给出自环数、总后裔次数和低次数半边数的联合矩生成函数。它是带符号求和的代数记号，应明确写出绝对收敛性；不赋予它概率分布的含义，也不把同一自环的两个半边当作独立变量。

正文展示导数或分部积分如何得到两个代表性的矩，其余所需矩列入附录。二阶计算需要辨别低次数半边时，保留足够的次数计数变量。

### 4.2 The leading term and the first correction

**命题 4.1，首项与一阶系数。** 在一致余项的支持下，先完成 $e^{S(1)}$。再分别给出纯自环图的一阶修正和三个 $q=1$ 核心的首项。

| 图的类型 | 对 $e^{S(1)}/g$ 的相对系数 |
| --- | --- |
| 纯自环图的一阶修正 | $\frac1{12}-\frac{65}{6\pi^2}$ |
| 椭圆尾 | $\frac1{24}+\frac1{6\pi^2}$ |
| 有理三价顶点以三条边连到大顶点 | $\frac{32}{3\pi^2}$ |
| 带自环的有理三价顶点，以一条边连到大顶点 | $1$ |

用小图配合自同构数解释后三行；逐项相加得到 $9/8$。将体积修正和后裔修正分别归于 [MZ15] 和 [W26, Lemma 7.2, Appendix C.1]，把从原文复杂度变量换成 $g^{-1}$ 的步骤写明。

### 4.3 The second correction

**拟证明的计算命题 4.2，二阶系数。** 按

$$
\gamma_2=Q_{0,2}+Q_{1,1}+Q_{2,0}
$$

组织计算：$q=0$ 展到二阶，$q=1$ 展到一阶，$q=2$ 只取首项。所有其他图由命题 3.2 以 $M=3$ 控制。

旧笔记表 2 给出的待重建分组值如下，直接写出 $\pi^2$ 及其幂，不另设常数别名：

| 分组 | 候选贡献 |
| --- | --- |
| $Q_{0,2}$ | $\frac{43}{288}-\frac{469}{36\pi^2}+\frac{5665}{72\pi^4}$ |
| $Q_{1,1}$ | $\frac{73}{288}-\frac{1843}{144\pi^2}-\frac{6565}{36\pi^4}$ |
| $Q_{2,0}$ | $\frac{1849}{1152}+\frac{3737}{144\pi^2}+\frac{7465}{72\pi^4}$ |

三行的有理代数和确为 $257/128+1/(8\pi^2)$，其中 $\pi^{-4}$ 项相消。需要补足的是每行的推导：从精确 WP 递推重建所需的 $c_2$ 和后裔二阶系数，计算低复杂度顶点多项式，并核对核心的自同构数。旧笔记报告 $q=2$ 有 13 个核心同构类，附录应逐张列出并复核此计数。

将所需输入整理成一个命题，并对后裔低次数的特殊情形保留原递推中的区分。采用 [MZ15, §2] 所列的精确递推，亦见 [HMT25, Theorem 4.3]；逐阶提取的算法可参照 [Hua25, §§2.1, 3]。体积二阶系数应与 [EGGLS24, (6.10)] 的已有显式表达式核对并注明来源。本文只使用所需有限阶的递推与系数，不依赖旧笔记涉及的高阶系数环判断。

### 4.4 Proof of Theorem 1.1

汇总前述两个计算命题，恢复 $a_g/N_g=Z_g(1)/F_g$，并输入 $C_{\rm WP}=1/\sqrt\pi$。最后的定理证明控制在几段内，逐项指出首项、两个系数和 $O(g^{-3})$ 余项的来源。

将 $Z_g(1)/V_{g,0}$ 的相对展开与 $Z_g(1)/F_g$ 的绝对展开严格区分；相对一阶系数需减去 $c_1(0)$。本节正文聚焦定理所需的二阶，不扩展到旧笔记中有文献争议的三阶系数。

## 第 5 节 Fixed degree Hodge insertions

本节完成 Theorem 1.2。切入点采用 $\lambda_3=\lambda_1^3/6+2\mathrm{ch}_3$：固定 Chern 类插入的前两个修正由一个奇 Chern 特征控制。先用装饰图给出其余项的阶数，再计算 $\mathrm{ch}_3$，即可得到任意固定乘积。

### 5.1 A filtration by odd Chern characters

**引理 5.1，固定插入的阶数界。** 对固定奇数 $a_i\geq3$，令 $w=\sum_i a_i$，证明

$$
\left\langle\prod_{i=1}^r\mathrm{ch}_{a_i}\right\rangle_g
=O(g^{r-w}).
$$

将证明分为两个模块：带标签源变量的精确图展开；固定装饰对第三节绝对界的影响。用忘点分拆数和大顶点上的自由新标记数记录增长，解释每个 $\mathrm{ch}_a$ 带来 $g^{1-a}$ 的尺度。

**推论 5.2，三阶精度的代数约化。** 沿用引言的 $P(\lambda)=\prod_{k=1}^{\ell}\lambda_{j_k}$、$F(j)$ 和 $G(j)$，由引理 2.3 得到

$$
F(j)\langle P\rangle_g
=1+2G(j)\langle\mathrm{ch}_3\rangle_g+O(g^{-4}).
$$

这里 $\langle\lambda_1^kQ\rangle_g=\langle Q\rangle_g$ 是精确恒等式。含一个 $\mathrm{ch}_a$、$a\geq5$ 或至少两个非平凡奇特征的项，统一由引理 5.1 控制。总权小于三时相应项省略。

### 5.2 The two leading coefficients of a single character

**引理 5.3，单源的自由标记和装饰边。** 对一个源专门写出 GRR 的顶点项与边项。需要的一阶修正分成阶乘归一化、增添标记后的体积比、后裔修正和指定自环的权。说明 $q=1$ 核心上自由标记的共同因子为何在分子分母中相消。

**引理 5.4，三角函数导数的递推。** 由

$$
8tf''+12f'+f=0
$$

计算 $f^{(k)}(\alpha)$。可令 $X_k=(8\pi^2)^kf^{(k)}(\alpha)$，把有限代数化简写成一个短表。

**命题 5.5，所需的单插入展开。**

$$
\langle\mathrm{ch}_3\rangle_g
=\frac{2\pi^2-21}{9g^2}
+\frac{2(\pi^2-10)}{3g^3}
+O(g^{-4}).
$$

正文详细计算这一命题。一般奇 Chern 特征的一阶修正、$\mathrm{ch}_5$ 的显式系数和连通差，可作为补充结果处理。

### 5.3 Proof of Theorem 1.2 and examples

将命题 5.5 代入推论 5.2，恢复引言中的 $F(j),G(j)$，直接完成证明。随后给出三个短核对：只含 $\lambda_1,\lambda_2$ 的情形由 Mumford 关系精确确定；单个 $\lambda_3$ 检查修正系数；两个固定 Chern 类说明三阶精度内为何只出现各指标的线性求和。

本节不需要计算第一定理的 $\gamma_2$。证明的核心是归一化分子分母的共同项相消，以及混合插入的统一阶数界。

## 第 6 节 The top Hodge class and Bessel asymptotics

本节完成 Theorem 1.3。证明导读应先说明：$\lambda_g$ 把稳定图限制为树；$\lambda_g$ 定理把每个顶点化为单变量系数；统一树尾界使首个修正只需计算无边项和椭圆尾。这给读者一条不经过第三至第五节的完整证明路线。

### 6.1 The lambda g theorem and an exact vertex formula

**引用结果 6.1，Faber–Pandharipande 的 $\lambda_g$ 定理。** 写出

$$
\int_{\overline{\mathcal M}_{G,N}}\lambda_G\prod_i\psi_i^{a_i}
=\beta_G\,\frac{(2G-3+N)!}{\prod_i a_i!},
\qquad \sum_i a_i=2G-3+N,
$$

并明确稳定范围和 $G=0$ 时的解释。[FP03, Theorem 1] 提供多点公式，[FP00, Theorem 2] 提供一点系数的生成函数

$$
\sum_{G\geq0}\beta_Gz^{2G}=\frac{z/2}{\sin(z/2)},\qquad
\beta_G\sim 2(2\pi)^{-2G}.
$$

**命题 6.2，精确顶点提取。** 令

$$
\Phi(x)=\frac{J_1(2\sqrt x)}{\sqrt x},\qquad
W^{\rm top}_{G,n}(\mathbf s)=
\int\lambda_Ge^{\kappa_1-\sum_i s_i\psi_i},\qquad
m=2G-3+n.
$$

这里 $m$ 只表示通式的系数提取阶数 $2G-3+n$。在无标记整体积分中代入 $G=g,n=0$ 时，使用引言的 $g_2$，不把它重新命名。由引理 2.8 及 $\lambda_g$ 定理逐步推导

$$
W^{\rm top}_{G,n}(\mathbf s)
=\beta_Gm![x^m]\Phi(x)^{-m-1}
\prod_{i=1}^nJ_0(2\sqrt{s_ix}).
$$

**推论 6.3，亏格零约化。** 顶点公式也给出

$$
W^{\rm top}_{G,n}(\mathbf s)
=\beta_GW^{\rm top}_{0,\,2G+n}(\mathbf s,0,\ldots,0).
$$

在这里介绍与 [KMZ96]、[MaZ00] 的联系：相应的亏格零反函数和 Bessel 临界点已有文献来源。本文需要完成的是在当前 Hodge 图和中的应用、树尾控制及边界修正。

### 6.2 The Bessel critical point and a uniform coefficient bound

沿用引言中的 $z_{0,1}$ 和 $\rho$，定义

$$
x_*=\frac{z_{0,1}^2}{4},\qquad
w(x)=x\Phi(x)=\sqrt xJ_1(2\sqrt x),\qquad
R=w(x_*)=\frac{z_{0,1}J_1(z_{0,1})}2=\frac{\rho}{12}.
$$

**引理 6.4，唯一主鞍点。** 证明 $w'(x)=J_0(2\sqrt x)$，故 $w'(x_*)=0$ 且 $w''(x_*)\ne0$。用 Bessel 的乘积公式和零点交错性给出整圆上的模估计。引用 DLMF 10.21.15、10.21.2；根号形式均按整幂级数理解。

**引理 6.5，统一顶点界。** 对全部稳定类型和 $s_i\in[0,1]$，证明

$$
|W^{\rm top}_{G,n}(\mathbf s)|
\leq C^{n+1}\beta_G\frac{m!R^{-m}}{\sqrt{m+1}}.
$$

常数独立于顶点亏格和价数，是随后对全部树求和的关键。

### 6.3 Stable trees and their tails

**命题 6.6，树展开及按边数的余项。** 从命题 2.6 和推论 2.5 得到 $b_g$ 的精确树表达。利用

$$
\sum_v(2g_v-3+n_v)=g_2-|E|,\qquad
\sum_{k=0}^{M}k!(M-k)!\leq3M!
$$

及平面根树的计数上界，证明全部 $|E|\geq2$ 的图合计为主尺度的 $O(g_2^{-2})$。一边树中，两侧亏格都至少为二的总贡献也要给出更强的阶乘卷积界。

这样，余项是整个图和的余项；不会把“每棵固定树很小”直接当作“所有这些树的和很小”。

### 6.4 The first correction and proof of Theorem 1.3

**引理 6.7，无边项的二项鞍点展开。** 展开相位和幅度，保留计算首个修正所需的高斯矩，得到

$$
[x^m]\Phi(x)^{-m-1}
=\frac{R^{-m}}{J_1(z_{0,1})\sqrt{2\pi m}}
\left(1+\frac{-1/4+1/(6z_{0,1}^2)}m+O(m^{-2})\right).
$$

解释奇半整数阶项因对称积分而消失，并给出可积的统一余项。

**引理 6.8，椭圆尾的贡献。** 用 $\beta_1=1/24$ 和

$$
\int_0^1J_0(2\sqrt{sx})\,ds=\Phi(x)
$$

计算其相对于无边首项的修正，系数为 $\pi^2J_1(z_{0,1})^2/6$。

将两种贡献相加，再乘回幂积分的阶乘与 $12$ 的幂次；用 $\beta_g=2(2\pi)^{-2g}(1+O(4^{-g}))$ 恢复引言的形式。结尾逐一对应第三定理中 $b$ 的三项来源。

可先用 $g=2$ 做一个完整的精确例子：无边项为 $\beta_2$，唯一一边树有两个相同的椭圆顶点，权为 $\beta_1^2/2$。恢复幂积分得到 $b_2=(\beta_2+\beta_1^2/2)/12=1/5760$，同时检查对称因子和阶乘规范。

## 第 7 节 Linear Hodge potentials and transport at fixed defect

本节为 Theorem 1.4 建立精确递推。开头说明固定离顶差 $h$ 意味着 Chern 指标 $g-h$ 随亏格增长，需要采用线性 Hodge 势。第八节负责将这里的形式恒等式转成渐近结论。

### 7.1 The linear Hodge potential and the first ILW flow

**引用结果 7.1，Buryak 的定理及本文的变量换算。** 从记录单个 $\lambda_j$ 的 Hodge 势出发，定义

$$
z=\hbar\varepsilon,\qquad \eta=\varepsilon^{-1},\qquad
\mathcal F=\sum_{g,h}z^g\eta^h\mathcal F_{g,h}.
$$

写清 $\hbar^g\varepsilon^j=z^g\eta^{g-j}$，因此 $\eta$ 的次数记录离顶差。采用 [Bur15, Theorem 1.1, (1.1)–(1.2)] 的亏格权重，定义

$$
\mathcal G=
\frac{\sin(\sqrt z\,\partial_x/2)}{\sqrt z\,\partial_x/2}\mathcal F,
\qquad U=\partial_x^2\mathcal G,\qquad x=t_0.
$$

所需的第一流为

$$
\partial_{t_1}U
=U\partial_xU+
\eta\sum_{k\geq1}c_kz^k\partial_x^{2k+1}U,\qquad
c_k=\frac{|B_{2k}|}{(2k)!}.
$$

并给出逆正弦变换，系数正是第六节的 $\beta_k$。专门说明这里的线性 Hodge 势与纯 $\lambda_1$ 的指数势各自的定义，防止沿用旧笔记中不同势函数的参数规范。

### 7.2 A specialization producing the kappa background

**命题 7.2，忘点专门化。** 取

$$
t_d^*=\frac{(-1)^{d-2}}{(d-1)!}\quad(d\geq2),
\qquad t_1=-\theta.
$$

用引理 2.8 推导，对稳定的目标空间，

$$
\partial_x^n\mathcal F_{g,h}(0;0)
=T_{g,h,n}:=
\int_{\overline{\mathcal M}_{g,n}}\lambda_{g-h}e^{\kappa_1}.
$$

在此专门化下，亏格零解 $v_\theta$ 是

$$
w_\theta(v)=w(v)+\theta v
$$

在零点附近的反函数。说明为何 $\theta$ 作为辅助参数有用：它给精确递推提供特征线，并使解析估计能够在一个共同区域内进行。

### 7.3 Exact recursions and their integration constants

令 $L_{g,h}=\partial_x\mathcal G_{g,h}$，$\mathscr D=\partial_{t_1}-v\partial_x$。

**引理 7.3，积分常数的确定。** 用 string、dilaton 方程把每个固定亏格项写成逆函数各阶导数的有限表达式；在这些表达式中，从 $U$ 的方程积分到 $L_{g,h}$ 时的常数可由几何初值确定。把亏格一的对数项单独处理。

**命题 7.4，固定差的精确输运。** 分开写出 $h=1$ 的线性初层，以及 $h\geq2$ 时由 $h-1$ 层驱动的线性项和差指标分拆产生的二次项。给出反向特征线

$$
(\theta,x)\longmapsto
(\theta+\sigma,\;x+\sigma v_\theta(x))
$$

与其无穷端的衰减条件。证明从特征线积分恢复解的精确性。

**引理 7.5，第一差层的对数核。** 用 Lagrange–Bürmann 反演得到

$$
L_{g,1}(\theta;x)
=c_g(2g-1)![y^{2g-1}]
\log\frac{v_\theta(x+y)-v_\theta(x)}{y}.
$$

这是后续奇点分析的显式初值。仅有第一流的场变量还不足以直接恢复所有自由能常数；第八节另行控制 $L_{g,h}$ 的原函数。

### 7.4 One Borel normalization for all fixed defects

直接采用统一的变换

$$
\mathcal L_h(\theta;x,y)=
\sum_{g\geq h}(2\pi)^{2g}L_{g,h}(\theta;x)
\frac{y^{2g+h-2}}{(2g+h-2)!},
\qquad h\geq1.
$$

低亏格种子按稳定性单列。说明分母的选取使各差层的主奇性统一为平方根，且

$$
\mathcal L_h(\theta;x,-y)=(-1)^h\mathcal L_h(\theta;x,y).
$$

**命题 7.6，Borel 核的精确积分方程。** 用 Beta 积分将递推写成平移的线性核与二次卷积核，并检验它们的参数和阶乘。正文展示主核，附录列出完整换指标计算。这一步仍属于精确恒等式；解析区域和极限交换由下一节证明。

## 第 8 节 Singularity analysis and Hodge integrals at fixed defect

本节完成 Theorem 1.4，是全文最长的证明。开头先给四步路线：确定反函数及 Borel 核的共同解析区域；递推主奇项的系数；通过逆正弦变换和奇点转移得到 $\kappa_1$ 背景的渐近；用一个节点的估计和交数对数凹性返回 $\lambda_1$ 背景。

### 8.1 Analytic domains of the inverse Bessel function

**引理 8.1，反函数的主奇点。** 对 $v=w^{-1}$，证明其收敛半径为 $R$，在主临界值附近有

$$
v(x)=x_*-\frac{z_{0,1}}{\sqrt2}\sqrt{1-x/R}+O(1-x/R).
$$

证明圆周其余点的延拓，并建立小 $\theta$ 下共同适用的反函数区域。应明确给出单叶性、允许的复角域及其在核平移与特征线输运下的保持性质。

该模块的作用是保证后续局部展开能用于系数转移。正文保留区域的几何解释；具体 Bessel 级数界和远端圆盘估计可放入附录 B。

### 8.2 Propagation of the leading singularity

**命题 8.2，Borel 核的主奇项及一致余项。** 将第二版讲义中较长的 Lemma 4.2 拆成以下三个引理：

1. 初层对数差商的展开及其一致导数界。
2. 线性核的主分支、积分端点和远端输运的估计。
3. 二次卷积的较低阶奇性，以及递推后余项的保持。

采用距离 $S=R-x$ 和归一化距离 $1-y/S$；后者直接写出，不占用边界类已有的符号 $\delta$。结论应同时控制 $x$ 的小复邻域、两个奇点 $y=\pm S$ 和余项的有限阶导数。可沿用任意固定 $1/2<\nu<1$ 的余项尺度，并验证两阶导数界足以支持后续转移。

在 $\theta=0$，主平方根的系数应满足

$$
P_1(x)=\frac1{x_*-v(x)},\qquad
P_h(x)=\frac1{x_*-v(x)}
\int_x^R P_{h-1}(s)\,ds.
$$

正文详细解释第一正向线性分支为何产生这条递推，以及二次核为何无法在积分域内同时触及两个主奇点。对 $x$ 趋近临界值时的积分端点必须保留一致估计。

### 8.3 The transport constant and its factorial

**引理 8.3，主系数递推的闭式。** 定义

$$
\mathcal B(x)=\int_x^R\frac{ds}{x_*-v(s)}.
$$

证明

$$
P_h(x)=
\frac{\mathcal B(x)^{h-1}}
{(h-1)!(x_*-v(x))},
\qquad
\int_0^R P_h(x)\,dx=\frac{\mathcal B(0)^h}{h!}.
$$

这里应明确展示定理中 $1/h!$ 的来源：它来自主奇项递推中的有序积分。

**引理 8.4，常数的 Bessel 求值。** 将变量换成 $x=w(u)$，先得到

$$
\mathcal B(0)=
\int_0^{x_*}\frac{J_0(2\sqrt u)}{x_*-u}\,du.
$$

再用 $Y_0$ 的调和数展开及 Bessel Wronskian 恒等式证明

$$
\mathcal B(0)=\frac1{z_{0,1}J_1(z_{0,1})}=\frac1{2R}.
$$

引用 DLMF 10.8.2 和 10.5.2，并给出端点可积性及逐项积分的依据。避免把这个决定最终常数的步骤压缩成一句特殊函数恒等式。

### 8.4 Inverting the sine transform and transferring coefficients

**引理 8.5，未卷积项及自由能常数。** 在负实轴上由几何势的有限表达式确定原函数，证明 $\mathcal G_{g,h}(0;0)$ 相对于所求主尺度小一阶。将近端、有限中段和负无穷远端分别估计。这里完成从 $L_{g,h}$ 回到自由能的常数核对。

**命题 8.6，逆正弦变换的主奇项。** 令 $D_{g,h}=g_2+h$。$\mathcal F_{g,h}-\mathcal G_{g,h}$ 的 $D_{g,h}!$ 归一化 Borel 级数，在 $y=R$ 的主项为

$$
\frac{z_{0,1}}{2\sqrt2 R}\frac{\mathcal B(0)^h}{h!}
(1-y/R)^{-1/2}.
$$

根据幂次的奇偶性写出 $y=-R$ 的镜像项。两个奇点对所提取系数的贡献相加，产生的因子 $2$ 要与 $\beta_g$ 的归一化一起核对。

引用 [FO90] 的奇点转移方法，并在本文给出适用于两个主奇点的简短转移引理；验证带缺口复域、圆周其余部分的延拓和余项条件。仅在实轴上的渐近等价不足以直接代入转移定理。

**推论 8.7，$\kappa_1$ 背景的无标记渐近及标记上界。** 写 $T_{g,h}=T_{g,h,0}$，得到

$$
\frac{T_{g,h}}{T_{g,0}}
\sim\frac1{h!}
\left(\frac{\mathcal B(0)}R\right)^h g_2^h.
$$

同时提取固定 $n=0,1,2$ 的一致界。令 $M=g_2+h+n$，所需形式为

$$
|T_{g,h,n}|
\leq C_h\beta_g\frac{M!R^{-M}}{\sqrt{M+1}}.
$$

原函数估计、主奇点的两个贡献和这些带标记上界是三个不同的输出，分别给出引用位置。无需为后面的背景比较证明任意增长价数的顶点界。

### 8.5 Comparing the kappa and Hodge backgrounds

沿用上一小节定义的 $D_{g,h}=g_2+h$，令

$$
U_{g,h}=\int_{\overline{\mathcal M}_g}
\lambda_{g-h}\delta e^{\kappa_1}.
$$

**引理 8.8，一个节点的估计。** 将 $\delta$ 展成分离与不可分离节点：不可分离项使用 $(g-1,2,h-1)$ 的标记界；分离项使用两侧差指标之和为 $h$ 的标记界。用阶乘卷积控制全部亏格分配，证明

$$
\frac{|U_{g,h}|}{T_{g,h}}=O_h(g^{-1}).
$$

**引理 8.9，射影丛中的 nef 交数。** 在参数化一维商的 $p:\mathbb P(\mathbb E)\to\overline{\mathcal M}_g$ 上令 $\zeta=c_1(\mathcal O(1))$。此处 $p$ 仅表示本引理中的投影，和图计数中自环数的作用域分开。对 $0\leq j\leq g$，由 Mumford 关系和射影丛公式得到

$$
p_*\zeta^{g-1+j}
=[t^j]c_{-t}(\mathbb E)^{-1}=\lambda_j.
$$

把 $\lambda_{g-h}$ 提升为 $\zeta^{2g-h-1}$。完整 Hodge 丛的 nef 性采用 Fujita–Kawamata 半正性在边界上的适用形式，参见 [LX26b, §4.2]；$\kappa_1=12\lambda_1-\delta$ 的 ample 性引用 [CH88, Theorem (1.3)]。这里需要的是向量丛 $\mathbb E$ 的 nef 性。

**命题 8.10，整个背景误差的控制。** 令 $L=12\lambda_1$、$K=\kappa_1$，对 $0\leq k\leq D_{g,h}$ 考虑混合交数

$$
C_k=\int_{\mathbb P(\mathbb E)}
\zeta^{2g-h-1}L^kK^{D_{g,h}-k}.
$$

由 Hodge 指标不等式及 nef 极限得到 $C_k^2\geq C_{k-1}C_{k+1}$。结合 $\delta=L-K$ 的有效性和引理 8.8，推导

$$
1\leq\frac{C_{D_{g,h}}}{C_0}
\leq\left(1+\frac{U_{g,h}}{D_{g,h}T_{g,h}}\right)^{D_{g,h}}
\leq\exp\left(\frac{U_{g,h}}{T_{g,h}}\right)
=1+O_h(g^{-1}).
$$

因此

$$
b_g(h)=12^{-D_{g,h}}D_{g,h}!\,T_{g,h}
\bigl(1+O_h(g^{-1})\bigr).
$$

本命题解释了为何一个节点的估计足以控制整个背景替换。按这条路线展开，可将稳定图中高阶边界项的总影响转为交数不等式。

### 8.6 Proof of Theorem 1.4

分别对 $h$ 和 $0$ 使用命题 8.10。先保留指数积分与幂积分的阶乘差，写成

$$
\frac{b_g(h)}{b_g}
\sim
\frac{(g_2+h)!}{12^hg_2!}\,
\frac1{h!}
\left(\frac{\mathcal B(0)}R\right)^hg_2^h
\sim
\frac1{h!}\left(\frac{6g_2^2}{\rho^2}\right)^h.
$$

最后用 $g_2/g\to2$ 得到引言的 $(24g^2/\rho^2)^h/h!$。说明两个 $g^h$ 分别来自指数积分的渐近和恢复幂积分的阶乘比。$h=0$ 单独作为恒等情形。

本节的主奇点转移给出相对 $o(1)$；背景比较给出相对 $O_h(g^{-1})$。最终结论保持引言中的渐近等价形式。

## 附录安排与材料取舍

### 附录 A Coefficients and finite cores

收录第四节所需的 WP 二阶输入、低复杂度顶点多项式、自环矩和 $q\leq2$ 的核心表。每张图列出顶点类型、边连接、自同构阶数、所取展开精度和贡献。先给完整的计算规则，再展示汇总表。

对 Theorem 1.1，真正需要的截断精度如下：

| 核心复杂度 | 大顶点展开到哪一阶 | 小顶点所需类型 |
| --- | --- | --- |
| $q=0$ | 二阶 | 无 |
| $q=1$ | 一阶 | $(0,3),(1,1)$ |
| $q=2$ | 首阶 | 单个 $(0,4)$ 或 $(1,2)$，或两个复杂度一的顶点 |
| $q\geq3$ | 使用统一尾界 | 无需逐图计算 |

小顶点的边界多项式可用低亏格交数直接计算，并与文献体积表交叉核对。候选二阶系数的正式计算应能独立于旧笔记中未附带的程序复查。

### 附录 B Analytic estimates for transport kernels

收录第八节共同复域的详细构造、Bessel 级数中的显式界、远端特征线积分、负实轴原函数的远端估计，以及 Beta 积分产生核的完整换指标。主文保留每条引理的完整假设、结论和在证明链中的作用。

第八节的主奇项递推、端点机制和背景比较是主要论证，应在正文展开。附录承担长度较大但结构单一的估计。

### 附录 C Exact values and reproducible checks

保留少量检查规范的精确数据，例如 $a_2=1/2880$、$a_3=1/90720$，以及 $\lambda_3$ 插入和固定离顶差的归一化残差。说明数据来源、固定提交、提取方式和所用精度，明确区分精确有理数比较与有限窗口外推。

旧笔记所述的提取脚本、核心枚举程序和 JSON 数据目前没有随四份 PDF 出现在本项目中。若论文保留可复现的计算声明，应补齐相应文件并重新运行。已有表格可以作为待核对的计算记录。

下列材料适合留作后续工作，或只在篇末简短讨论：一般奇 Chern 特征的全部高阶系数；$g^{-5}$ 的连通差；Schubert 插入；$\kappa_1/12$ 背景下固定低指标插入的推广；纯 $\lambda_1$ 的热算子和余弦 loop equation；有标记的纯 $\lambda_1$ 渐近猜想。它们各有独立价值，但不是证明引言四个定理所必需的步骤。

## 引用与归属

每项外部输入第一次使用时，应同时给出作者、固定版本、定理或公式位置、适用假设以及到本文记号的换算。引用定理可写成明确署名的 recalled theorem；本文的专门化、核心计算和余项证明分别陈述。

几项尤其需要明确的归属是：GRR 来自 Mumford；边界指数的通用图恒等式来自 Andersen 等；忘点的循环公式来自 Kaufmann–Manin–Zagier；顶类交数来自 Faber–Pandharipande；WP 固定标记数展开、一致估计和绝对常数有不同文献来源；ILW 方程来自 Buryak；Bessel 临界点的历史背景来自 KMZ 和 Manin–Zograf；系数转移采用 Flajolet–Odlyzko 的分析方法。

以下是正文核心引用的建议清单。条目中的定位对应所链接的版本；正式生成参考文献时再统一书目信息和引用键。

| 引用键 | 原始文献与定位 | 使用位置 |
| --- | --- | --- |
| Mum83 | D. Mumford, [Towards an Enumerative Geometry of the Moduli Space of Curves](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1983b--EnumGeomModuli-NC.pdf), 1983，§5，(5.2)、(5.3) | 第 2 节的 GRR 与 Chern 类关系 |
| Wol86 | S. A. Wolpert, [Chern forms and the Riemann tensor for the moduli space of curves](https://doi.org/10.1007/BF01388794), 1986 | WP 类的规范 |
| Mir07 | M. Mirzakhani, [Weil–Petersson volumes and intersection theory on the moduli space of curves](https://doi.org/10.1090/S0894-0347-06-00526-1), 2007，Theorem 1.1 | 体积多项式与交数的换算 |
| ABCDGLW23 | J. E. Andersen, G. Borot, S. Charbonnier, V. Delecroix, A. Giacchetto, D. Lewański, C. Wheeler, [Topological recursion for Masur–Veech volumes](https://arxiv.org/html/1905.10352v3), Lemma 3.10，(3.18)–(3.21)；刊于 JLMS 107 (2023), 254–332 | 第 2、3、5、6 节的精确图公式 |
| KMZ96v1 | R. Kaufmann, Yu. Manin, D. Zagier, [Higher Weil–Petersson volumes of moduli spaces of stable n-pointed curves](https://arxiv.org/html/alg-geom/9604001v1), 1996，指定预印本版本的 Theorem 2.2 及循环公式 | 第 2、5、6、7 节的忘点与参数变换 |
| GP03 | T. Graber, R. Pandharipande, [Constructions of nontautological classes on moduli spaces of curves](https://arxiv.org/html/math/0104057v2), Appendix A.1 | 第 2.3 节回顾稳定图及黏合乘积，明确半边和腿的约定差异 |
| FP00 | C. Faber, R. Pandharipande, [Hodge integrals and Gromov–Witten theory](https://arxiv.org/html/math/9810173), Invent. Math. 139 (2000), 173–199，Proposition 1、Theorem 2 | 带标记 GRR、一点 Hodge 系数 |
| FP03 | C. Faber, R. Pandharipande, [Hodge integrals, partition matrices, and the lambda g conjecture](https://annals.math.princeton.edu/2003/157-1/p03), Ann. of Math. 157 (2003), 97–124，Theorem 1 | 第 6 节的顶类多点交数 |
| MZ15 | M. Mirzakhani, P. Zograf, [Towards large genus asymptotics of intersection numbers on moduli spaces of curves](https://arxiv.org/abs/1112.1151), GAFA 25 (2015), 1258–1289，Theorem 1.2、Remark 1.3、Corollary 1.5 | 固定标记数展开与一阶系数 |
| Hua25 | X. Huang, [Asymptotic coefficients of Weil–Petersson volumes in the large genus](https://arxiv.org/html/2501.06421v1), v1，§§2.1、3 | 第 4 节所需的精确递推与系数算法 |
| EGGLS24 | B. Eynard, E. García-Failde, P. Gregori, D. Lewański, R. Schiappa, [Resurgent asymptotics of Jackiw–Teitelboim gravity and the nonperturbative topological recursion](https://arxiv.org/html/2305.16940), Ann. Henri Poincaré 25 (2024), 4121–4193，(6.10) | 体积二阶系数的已有表达式与交叉核对 |
| SW25 | Y. Shen, Y. Wu, [Arbitrarily small spectral gaps for random hyperbolic surfaces with many cusps](https://arxiv.org/html/2203.15681v4), v4，Lemmas 14、18 | 统一体积上界 |
| HMT25 | W. Hide, D. Macera, J. Thomas, [Spectral gap with polynomial rate for Weil–Petersson random surfaces](https://arxiv.org/html/2508.14874v2), v2，Theorem 4.2，A1、A3、A4 | 第 3、5 节的一致余项 |
| LX26 | K. Liu, H. Xu, [Uniform asymptotics and the Weil–Petersson constant](https://arxiv.org/html/2610.33752v1), v1，Corollary 1.2 | WP 绝对常数 |
| W26 | Q. Wang, Z. Li, B. Qiu, S. Wang, Y. Zhong, K. Chen, R. Xia, [Uniform large-genus asymptotics of Weil–Petersson volumes](https://arxiv.org/html/2610.35492v4), v4，Corollary 1.2、Lemma 6.1、Lemma 7.2、Appendix C.1 | 绝对常数、后裔上界和显式一阶修正 |
| MaZ00 | Yu. Manin, P. Zograf, [Invertible cohomological field theories and Weil–Petersson volumes](https://arxiv.org/html/math/9902051), Ann. Inst. Fourier 50 (2000), 519–535，Theorem 4.1、式 (17)、Theorem 6.1 | 第 6、7 节的反函数和 Bessel 背景 |
| Bur15 | A. Buryak, [Dubrovin–Zhang hierarchy for the Hodge integrals](https://arxiv.org/html/1308.5716v4), CNTP 9 (2015), 239–271，Theorem 1.1、(1.1)–(1.2) | 第 7 节的线性 Hodge 势和 ILW |
| DLMF | NIST, [Bessel Functions](https://dlmf.nist.gov/10)，10.21.15、10.21.2、[10.8.2](https://dlmf.nist.gov/10.8.E2)、[10.5.2](https://dlmf.nist.gov/10.5.E2) | 第 6、8 节的特殊函数恒等式 |
| FO90 | P. Flajolet, A. Odlyzko, [Singularity analysis of generating functions](https://algo.inria.fr/flajolet/Publications/FlOd90b.pdf), SIAM J. Discrete Math. 3 (1990), 216–240 | 第 8 节的复奇点与系数转移 |
| CH88 | M. Cornalba, J. Harris, [Divisor classes associated to families of stable varieties, with applications to the moduli space of curves](https://numdam.org/item/10.24033/asens.1564.pdf), 1988，Theorem (1.3) | 第 8 节的 $\kappa_1$ 正性 |
| LX26b | K. Liu, H. Xu, [Balancing tautological intersection numbers](https://arxiv.org/html/2610.39462), §4.2，Proposition 4.4；追溯 Fujita–Kawamata 半正性 | 边界上的 Hodge 向量丛 nef 性 |

旧研究笔记中的 Li–Wang 两人版本，应按实际采用的 W26 v4 更新作者和公式定位。早期笔记中把 WP 绝对常数列作猜想的历史状态，也应按上述两篇 2026 年预印本更新。MZ15 的固定标记数结果、一致估计以及绝对常数的确定，各自只承担其已经建立的内容。

## 写作推进顺序

1. 先固定第 2 节的约定和引文版本，给四个引言定理补上稳定的 LaTeX 标签。
2. 完成第 6 节这条较短的独立证明，核对 Bessel 常数、栈因子和阶乘恢复。
3. 写第 3 节的统一图估计，同时形成第四节需要的核心分类规则。
4. 优先重建第 4.3 节的二阶系数计算。这是当前第一定理相对于第二版讲义新增的实质任务。
5. 用第三节的工具完成第五节的单源计算和代数约化，不必等待全部二阶核心表完成。
6. 完成第 7 节的精确变量换算及积分常数，再按第 8 节的模块逐项写出解析证明与背景比较。
7. 最后整理附录、补齐可复现文件，并重写 Introduction 中的相关工作、证明概览和文章结构段落。

正式正文中，每个大定理证明前安排一个完整段落说明输入、核心机制和步骤之间的衔接；每个技术命题结尾指出它具体支持哪个后续步骤。主定理的最终证明只负责组合已经建立的模块，展开计算与长估计各自有清晰的引用位置。

## 本地笔记的使用位置

| 本地材料 | 在提纲中的作用 |
| --- | --- |
| [第二版讲义](refs/hodge_large_genus_lecture-v2.pdf) | 第 3 节对应其 §2.1–2.4；第 4 节对应 §2.5–2.6，并补算二阶；第 5 节对应 §6.1–6.3 的所需部分；第 6 节对应 §3.1–3.3；第 7、8 节对应其 §§4–5 |
| [第一版讲义](refs/hodge_large_genus_lecture-v1.pdf) | 第 1 节的几何解释、第 3 节较短的证明导读及阅读路径，可帮助改写第二版过于密集的段落 |
| [纯 lambda1 渐近笔记](refs/lambda1_asymptotics.pdf) | §4.3 和表 2 为二阶系数提供候选分组；§6 列出的换序难点，由本提纲第三节集中处理；数据与外推进入附录 C |
| [2026 年 10 月 27 日研究笔记](refs/lambda1_hodge_research_notes_2026-10-27.pdf) | §§1、4–5 用于核对不同势函数、参数、阶乘和低亏格种子；§§6–9 的 loop 路线与有标记猜想保留为后续工作 |
