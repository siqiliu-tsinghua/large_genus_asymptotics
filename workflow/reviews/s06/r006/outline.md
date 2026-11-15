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

