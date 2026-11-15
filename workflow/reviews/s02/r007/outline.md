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

