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

