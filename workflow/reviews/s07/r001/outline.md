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

