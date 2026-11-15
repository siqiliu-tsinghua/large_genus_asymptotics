# s06 source preparation

Original academic reviewer: `/root/s02_academic`; 2026-11-15.
Scope: Theorem `thm:top-hodge`, outline 6.1–6.4 and the lecture's
Sections 3.1–3.3. This is source preparation, not a manuscript review.
Only **FP03, MaZ00 and DLMF** need adding. Suggested complete entries
are in `entries.bib`; FP00 and KMZ96v1 already suffice for the other
literature inputs. No shared file has been changed.

## 1. The lambda-g theorem and one-point coefficients

**FP03.** The primary publisher record is
<https://annals.math.princeton.edu/2003/157-1/p03>:
Carel Faber and Rahul Pandharipande, *Hodge integrals, partition matrices,
and the lambda-g conjecture*, Annals of Mathematics **157**(1) (2003),
97–124, DOI `10.4007/annals.2003.157.97`.
The fixed readable source is <https://arxiv.org/pdf/math/9908052v3>;
arXiv identifies v3 (2004-02-12) as the published version. The PDF's
first-page header incorrectly says 156 (2002); retain the verified
publisher/article metadata, not that header.

Theorem 1 is on PDF p.4 / journal p.100, after the scope on p.3 / p.99:
`G>=1`, `N>=1`, nonnegative descendant exponents, and total degree
`sum a_i=2G-3+N`. It proves

\[
 \int_{\overline{\mathcal M}_{G,N}}\lambda_G\prod_i\psi_i^{a_i}
 =\left(\int_{\overline{\mathcal M}_{G,1}}
                   \lambda_G\psi_1^{2G-2}\right)
       \frac{(2G-3+N)!}{\prod_i a_i!}.
\]

Section 0.2 explicitly uses rational Chow intersection numbers; the result
needed here is numerical, not a new cycle-class identity between moduli
spaces. For `G=0`, use the genus-zero formula (1), PDF p.2 / p.98,
on stable `N>=3`, with `lambda_0=1` and **define beta_0=1**. This is
not an integral on the nonexistent stable space `Mbar_{0,1}`. A stable
unmarked `G>=2` vertex is handled after adding forgetting markings;
do not apply the multipoint formula literally with `N=0`.

**FP00.** In the existing local PDF, Theorem 2 and (6) are on PDF p.3
/ journal p.175; the one-point definition with value one at genus zero
is (3), PDF p.2 / p.174. Setting its formal parameter `k=0` gives

\[
 \sum_{G\geq0}\beta_G z^{2G}=\frac{z/2}{\sin(z/2)}.
\]

The source calls these coefficients `b_G`; translate them to our
**beta_G**, since `b_g` already denotes the unmarked top-Hodge family.
FP00 discusses the multipoint formula as a conjectural Virasoro consequence;
its Theorem 2 proves the one-point generating formula. Credit the
multipoint proof to FP03, not to FP00.

FP00 Section 4.2, Lemma 1, PDF p.22 / journal p.194, gives, for `G>=1`,

\[
 \beta_G=(1-2^{1-2G})\frac{|B_{2G}|}{(2G)!}
 =2(1-2^{1-2G})\zeta(2G)(2\pi)^{-2G}.
\]

The second equality can use DLMF (25.6.2). Its Dirichlet series (25.2.1)
for real `s>1` gives `zeta(2G)=1+O(4^{-G})` directly, so
`beta_G=2(2pi)^(-2G)(1+O(4^{-G}))` and
`beta_{G-1}/beta_G=(2pi)^2(1+O(4^{-G}))`. The exact generating series
fixes `beta_1=1/24`, `beta_2=7/5760`; the asymptotic is not an input
for small-genus vertices.

## 2. Exact vertex reduction and existing genus-zero credit

The accepted Section 2 inputs are `crl:s02:kappa-exponential`,
`lmm:s02:forgetting-inversion`, `lmm:s02:rational-tail-degree`,
`lmm:s02:hodge-normalization`, `crl:s02:defect-allocation` and
`prp:s02:boundary-exponential`. Their KMZ96v1 and geometric credits
remain at the original statements/proofs; they need not be reintroduced
as external results each time.

The whole-kappa exponential inversion creates a new-point weight
`psi*(1-exp(-psi))`. Together with the lambda-g multinomial,

- each old `exp(-s_i psi_i)` yields `J_0(2sqrt(s_i x))`;
- each new point yields `x*(1-Phi(x))`, where
  `Phi(x)=sum (-1)^a x^a/(a!(a+1)!)`;
- summing `(m+k)!/k!*(1-Phi)^k` gives `m!*Phi^(-m-1)`.

Thus the proposed coefficient extraction follows from the existing
inversion and FP03; give this derivation rather than claiming FP03 itself
states a kappa/Bessel vertex theorem. New powers are at least two and
annihilate the old-cotangent pullback tails. Do **not** add another
`exp(-psi_new)` by importing the different background-pullback calculation
from Section 5: it is already incorporated in the whole-exponential
inversion. For a stable type, `m=2G-3+n>=0`; in the global unmarked
application keep the established name `g_2`.

**Classical inverse function.** KMZ96v1's Introduction, PDF p.3,
(0.8), already gives the genus-zero inverse series

\[
 y(t)=\sum_{N\geq3}\frac{v_N}{(N-2)!(N-3)!}t^{N-2},\qquad
 t=\sqrt y\,J_1(2\sqrt y),\quad v_N=\int\kappa_1^{N-3}.
\]

Its (0.9) also discusses the corresponding asymptotics. The paper attributes
the underlying earlier result to Zograf. Avoid a new-priority claim for
the genus-zero inverse function or its Bessel critical behavior.

**MaZ00.** The primary journal record is
<https://aif.centre-mersenne.org/item/AIF_2000__50_2_519_0/>;
the published PDF is
<https://www.numdam.org/article/AIF_2000__50_2_519_0.pdf>.
The correct DOI is **10.5802/aif.1764**. Theorem 4.1, journal p.525
/ PDF p.8, expresses the kappa generating function by the descendant
potential and the Schur-polynomial change of variables. Section 6,
(17), journal p.528 / PDF p.11, defines
`x_0=-j_0 J_0'(j_0)/2`; Proof 6.3, p.530 / PDF p.13, analyzes the
inverse of `x(y)=-sqrt(y) J_0'(2sqrt(y))` and its square-root singularity,
including (25). Hence its **x_0 is our R**, and its `j_0` is our
`z_{0,1}`. Its volumes are unscaled powers of kappa: our genus-zero
exponential integral is its `V_{0,N}/(N-3)!`.

There is an actual source sign misprint: published (17) prints
`y_0=-j_0^2/4`. The same sign occurs in arXiv:math/9902051v2 (PDF p.9),
where the constants are nevertheless called positive. Its derivative
`x'(y)=J_0(2sqrt(y))` and first-root argument require the **positive**
point `j_0^2/4`. This correction is an inference from the displayed
function, not a claimed published erratum. Cite the correct `x_0/R`
formula and the inverse analysis; define and prove our positive `x_*`
independently. Page images `MaZ00-p528.png` and `MaZ00-p530.png`
preserve the exact source evidence.

MaZ00 Theorem 6.1 is **fixed genus, number of markings tending to infinity**.
It supplies classical context, not an all-type uniform bound for the
Hodge tree sum. The exact genus-zero reduction is numerical; it asserts
no Chow-class equality between different moduli spaces.

## 3. DLMF facts and exact local translation

The official citation page <https://dlmf.nist.gov/help/cite> currently
specifies Release **1.2.8 of 2026-09-15** and the editor list used in
`entries.bib`. That whole-library entry also covers the optional zeta
locators above. Its printed root URL uses `texttt`, requiring no new
`url` or `hyperref` package.

- <https://dlmf.nist.gov/10.21.E15>, (10.21.15), gives the product for
  `J_nu`, in particular at `nu=1`:
  `Phi(x)=product_{k>=1}(1-4x/j_{1,k}^2)`.
- <https://dlmf.nist.gov/10.21.E2>, (10.21.2), gives, for `nu>=0`,
  `j_{nu,1}<j_{nu+1,1}<j_{nu,2}<...`. Thus
  `z_{0,1}<j_{1,1}`, so every zero of Phi lies beyond `x_*` on the
  positive real axis.
- <https://dlmf.nist.gov/10.6.E6>, (10.6.6), with `k=1,nu=1`, gives
  `(z J_1(z))'=z J_0(z)`.
  <https://dlmf.nist.gov/10.6.E3>, (10.6.3), gives `J_0'=-J_1`.

Consequently, in the paper's variables,

\[
 w'(x)=J_0(2\sqrt x),\qquad
 w''(x_*)=-\frac{2J_1(z_{0,1})}{z_{0,1}}<0,\qquad
 R=\frac{z_{0,1}J_1(z_{0,1})}{2}=\rho/12.
\]

The entire-circle strict modulus inequality and its Gaussian strengthening
follow from that product; they are deductions to show here, not another
DLMF theorem. Interpret root-containing expressions by their entire
power series. The all-stable-type vertex bound, complete tree tail,
retained two-term saddle expansion and elliptic-tail correction remain
the paper's arguments to supply and review.

## 4. Scientific boundaries and saved material

Use the Section 2 Hodge normalization on labelled products: graph cycles
force the top Hodge pullback to vanish, leaving stable trees. Do not claim
an automorphism-equivariant graph-cycle quotient is trivial on a quotient
stack; the accepted labelled-product identity already suffices. The tree
tail must bound the complete edge/genus/valence sum, not just each fixed
tree. No HMT or Section 3–5 numerical correction is needed for this route.

A useful finite-genus calibration is
`12*b_2=beta_2+beta_1^2/2`, hence `b_2=1/5760`; the half is the
automorphism exchanging two identical elliptic vertices. This checks
the beta-versus-b notation and factorial/12 normalization without using
a large-genus approximation at genus one.

Downloaded originals:

- `refs/Faber_Pandharipande_2003_Lambda_g_v3.pdf`:
  SHA256 `5915b2ad1fa3aa89f582064fb86bb8ca291a082d59f0f33a3d575b865e9bf51a`.
- `refs/Manin_Zograf_2000_Invertible_CohFT.pdf`:
  SHA256 `6e1472bff0db3d9f36c446e6a34273964ad16b9d1b9c2d7774ef11b49f3416a9`.

This directory contains extracted primary text, the two cited source-page
images, selected DLMF formula/HTML records and the MaZ00 v2 comparison
copy. The lecture was used only to locate relevant claims. None of these
preparation records signs an evolving s06 manuscript or changes workflow
status.
