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

