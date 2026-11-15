# Section 6 writing brief

Target: the unchanged Introduction theorem `thm:top-hodge` / `eq:g111`.
Use the outline's four subsections and the accepted Section 2 geometry.
The route must remain independent of the WP estimates in Sections 3--5.
Source preparation: `academic/source_memo.md`, verified primary PDFs in refs.
The bibliography additions FP03, MaZ00 and DLMF are already final.
The actual references.bib additionally has BIB-002's literal outer group
around the DLMF key; all three new keys have been actually cited and
strictly rendered together with the current alpha style. Do not replace
this compatible key with the unprotected preparation-file spelling.

## First definitions and exact vertices

Open with why lambda_g removes cycles and leaves trees, not a list of old
definitions. Keep g_2=2g-3, b_g, scalar b, z_{0,1}, rho and j_i/ell unchanged.
The beta_G one-point coefficients must not be renamed b_G. Define beta_0=1
as a convention and beta_G via the one-point integral for G>=1; there is no
stable Mbar_{0,1}. The FP03 multipoint theorem is numerical and applies for
G>=1,N>=1; its genus-zero formula uses stable N>=3 and lambda_0=1.

Derive the exact coefficient formula from the WHOLE kappa exponential:
psi_new*(1-exp(-psi_new)) at each forgotten point, not an additional
negative exponential from the different Section 5 pullback calculation.
Old cotangent pullback tails vanish by the established positive-psi lemma.
The new-point series is x*(1-Phi(x)); the old one is J_0(2sqrt(s_i*x)).
After the x^k shift, sum (m+k)!/k!*(1-Phi)^k to m!*Phi^(-m-1).
This sum is coefficientwise finite. For n=0,G>=2 the k=0 term vanishes by
degree; every nonzero term permits use of the N>=1 multipoint theorem.
For a stable vertex m=2G-3+n>=0; only the global unmarked case uses g_2.
The genus-zero reduction is an equality of numerical generating functions,
not a Chow-class identification between different moduli spaces.

Credit the classical inverse function to KMZ96v1 (0.8), and MaZ00 Section 6
for its inverse analysis/critical value: its x_0 is our R. Its (17) prints a
negative y_0 although its derivative proof requires the positive value;
do not import that sign. Define x_* positively and prove the critical
point directly. Keep Phi distinct from the existing WP sine function f.

## Circle estimate and all-type bound

Define Phi and w=x*Phi by entire series. Set x_*=z_{0,1}^2/4 and
R=w(x_*)=rho/12. DLMF's product and interlacing imply Phi's positive zeros
all exceed x_*. On |x|=x_*, each product factor has its minimum modulus at
the positive point; the first factor alone gives a strict Gaussian
strengthening |Phi(x_* exp(i theta))|>=Phi(x_*) exp(a theta^2).
Cauchy plus the bounded J_0 factors gives the all-stable-type bound with
m!/sqrt(m+1), including m=0. The constant must be independent of G and n.
If complex-parameter compact bounds are stated, prove their dependence
explicitly rather than assuming fixed-n asymptotics are uniform in n.

## Tree tail and a correction to the notes

Keep the exact 1/Aut tree formula and restore powers only at the end:
12^(g_2)*b_g/g_2! is the lambda_g exponential integral. A tree with E
edges has E+1 vertices, sum m_v=g_2-E and E<=g_2. Rooting and ordering
children gives at most 4^E plane shapes; genus labels are fixed by the
shape and m_v. Dropping parity/stability restrictions only enlarges the
positive majorant after the beta factors are bounded.
Use the uniform beta_G comparison including G=0,1, the convolution
sum k!(M-k)!<=3M!, and product(m_v+1)>=M+1. The E-edge mass relative to
beta_g*g_2!*R^(-g_2)/sqrt(g_2+1) is bounded by
C^(E+1)*sqrt((g_2+1)/(g_2-E+1))*(g_2-E)!/g_2!.
The factorial ratio is at most (e/g_2)^E; hence summing all E>=K gives
O(g_2^(-K)) for each fixed K. This is a whole-tree/genus/valence bound.

IMPORTANT: the lecture's nonelliptic one-edge argument has a real degree
count error. At an endpoint of genus G>=2 and valence one,
m=2G-3+1=2G-2>=2, not >=3. The inverse-binomial convolution must begin
at 2. It is O(M^-2), and the extra (g_2-1)!/g_2! gives a sufficient
O(g_2^-3) relative contribution. Do not copy the asserted O(g_2^-4).
This does not alter the theorem's O(g_2^-2) remainder or first correction.

An optional useful exact example is g=2 (thus g_2=1): only the empty tree
and two identical elliptic vertices occur, so
b_2=(beta_2+beta_1^2/2)/12=1/5760. This checks the stack half and 12 power.

## Saddle and elliptic contribution

The independent finite check `root_math_check.py` was executed. It derives
the circular phase and amplitude from w'=J_0 and the Bessel equation,
obtaining the correction -1/4+1/(24*x_*)=-1/4+1/(6*z_{0,1}^2).
Its JSON is preparation evidence, not a proof or a formal signature.

Write the actual Cauchy integral. Split at |theta|=m^(-2/5) and rescale
t=sqrt(m)*theta. To prove relative O(m^-2), retain enough Taylor orders
to exhibit BOTH odd half-order polynomials (m^-1/2 and m^-3/2); log phase
through order five and amplitude through order three suffice. Bound the
remaining error by m^-2 times an integrable polynomial times a Gaussian.
Do not take an absolute O(m^-3/2) and then assert it cancels without an
explicit odd term. The outer arc is exponentially small by the circle
bound. State an additive leading-amplitude version for a fixed analytic
P (or a uniformly bounded fixed-neighborhood family); do not divide by P
when P(x_*) can vanish. Only P=1 and P=Phi are needed for this theorem.
For the Cauchy-integral statement require P analytic on a neighborhood of
the CLOSED disk |x|<=x_*, not merely near the positive critical point.
An independent exact-rational coefficient recurrence was also executed
at orders 20,40,80 (exact_saddle_check.json); it agrees with the first
correction, but is only a finite cross-check, never proof of the remainder.

For one edge use the ordered split with factor 1/2; for g>=3 the two
elliptic placements combine to beta_1 times the large-vertex integral.
Wtop_{1,1}=beta_1=1/24 and integral_0^1 J_0(2sqrt(s*x)) ds=Phi(x).
The large coefficient order is g_2-1, and beta_(g-1)/beta_g is
(2pi)^2*(1+O(4^-g)). The resulting relative coefficient is
pi^2*J_1(z_{0,1})^2/6. Combine it with the saddle correction, the whole
E>=2 tail and the corrected nonelliptic bound, then restore g_2! and 12
and beta_g=2*(2pi)^(-2g)*(1+O(4^-g)). Identify the three terms of scalar b.

Use modular statements and proofs, clear guides before long calculations,
and short post-proof credit/convention Remarks. Define new symbols before
use and document their purpose/scope in the interface. Avoid aliases for
g_2, pi^2, the Bessel zero, or the established integral families. An
explicitly scoped local leading exponential scale is acceptable if it
actually shortens several tree/saddle/elliptic comparisons.
