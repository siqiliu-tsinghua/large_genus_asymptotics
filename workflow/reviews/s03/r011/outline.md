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

