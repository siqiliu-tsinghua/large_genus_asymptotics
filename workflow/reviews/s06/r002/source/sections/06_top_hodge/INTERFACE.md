# The top Hodge class and Bessel asymptotics

Scientific interface for the complete s06 author draft. Live review and
acceptance status belongs to `workflow/state.json`; this interface is not
a review signature.

## Dependency and scope

Approved s02 r008 snapshot:
`389580d8ae9aaf5b35dee26978a8385c87e9c8fb63036825f76d2c566084ecab`.
The closure consists of s01 and s02. The proof uses no result, coefficient,
notation definition or unresolved label from the WP Sections 3--5 or
Appendix A. It proves the original `thm:top-hodge` / `eq:g111`, with
relative O(g_2^-2), and preserves every target constant and normalization.
The Bessel/genus-zero data below are available for future fixed-defect
work; no positive-defect asymptotic is proved here.

## Inherited notation

| Symbols | First definition / use here |
| --- | --- |
| g,n, Hodge classes, rational Chow and stack integration, lambda_0 | Introduction; conventions are inherited directly, without a new moduli setup |
| b_g, g_2=2g-3, J_n(z), z_{0,1}, rho, scalar b | Introduction, Theorem 1.3; none is renamed |
| j_1,...,j_ell, ell and other integral families | Introduction; these meanings are retained and not used for auxiliary indices |
| psi, logarithmic kappa_a, ordinary Bernoulli B_k | s02.2; kappa has the forgetting-point convention |
| MM_Gamma, graphs, flags, Aut Gamma, gluing, g_v,n_v | s02.3; all graph identities are on the labelled vertex product before its quotient |
| pi_k and the kappa exponential | s02.4, `eq:s02:kappa-exponential`; entire-background inversion rather than a second background pullback |

## New notation and scopes

| Symbol | First definition | Type, scope and purpose |
| --- | --- | --- |
| beta_G | `eq:s06:beta-definition` | One-point Hodge integral for integer G>=1; beta_0=1 is a convention, not an unstable integral. Distinct from b_g and scalar b |
| z in beta series | `eq:s06:beta-series` | Local formal variable; its index is unrelated to the fixed Bessel zero |
| zeta(s) | Proof of `thm:s06:lambda-g` | Riemann Dirichlet series for real s>1; used only for one-point estimates |
| Phi(x) | `eq:s06:phi` | Entire series sum (-1)^a x^a/[a!(a+1)!]; square-root notation means the series, with value one at zero |
| W^{top}_{G,n}(s) | `eq:s06:vertex-definition` | Stable top-Hodge exponential vertex, for complex n-tuple s; distinct from WP vertices |
| m=2G-3+n | Before `prp:s06:exact-vertex` | Nonnegative local coefficient order for a stable type. Global unmarked arguments use g_2, not a renamed m |
| x_*, w(x), R | `eq:s06:critical-data` | Positive first-zero argument, entire Bessel map x Phi(x), and positive critical value R=rho/12. Reserved Bessel R is used as planned |
| z_{1,k} | Proof of `lmm:s06:critical-circle` | kth positive zero of J_1, k>=1; translates the source's j_(1,k) without using Hodge indices |
| a,C | Circle/vertex estimates | Fixed positive bound constants, independent of stable type; no new global coefficient family |
| m_v, s_v in bold tuple form | Opening s06.3 | m_v=2g_v-3+n_v; the tuple at vertex v consists of shared edge parameters s_e in [0,1] |
| calligraphic T_g | `eq:s06:tree-scale` | Positive beta_g*g_2!*R^(-g_2)/sqrt(g_2+1), scoped to tree/saddle comparisons in s06.3--4 |
| E,M,K | Tree estimates | Nonnegative edge count, sum of vertex coefficient orders, and fixed positive tail threshold; M is not a new name for g_2 |
| P | `lmm:s06:saddle` | Local analytic amplitude on a neighborhood of the closed critical disk; unrelated to the Introduction's Hodge polynomial P(lambda) |
| x_theta, calligraphic A_P, calligraphic H | Saddle proof | Circular parametrization, amplitude and locally chosen logarithmic phase; only integer powers occur on the whole circle |
| t, calligraphic Q_1,Q_2,Q_3 | Before `eq:s06:local-saddle` | Real rescaled coordinate and three explicit Taylor-product polynomials. Both half-order polynomials are odd |

The fixed formal t and integer N in the classical-inverse Remark have
that Remark's scope only. Old degree indices and all summation ranges are
bound locally; no alias for pi^2 or for z_{0,1} is introduced.

## Exports and precision

| Label | Result and scope |
| --- | --- |
| `thm:s06:lambda-g`, `eq:s06:lambda-g` | Numerical multipoint formula for G>=1,N>=1 and nonnegative degrees summing to 2G-3+N; genus zero only on stable N>=3 |
| `eq:s06:beta-series`, `eq:s06:beta-asymptotics` | Exact one-point generating series; exponential asymptotics and ratio; uniform positive comparison for every G>=0 |
| `prp:s06:exact-vertex`, `eq:s06:exact-vertex` | Exact Bessel coefficient formula for every stable (G,n), including m=0 and the unmarked G>=2 case |
| `crl:s06:genus-zero`, `eq:s06:genus-zero` | Numerical equality Wtop_(G,n)=beta_G Wtop_(0,2G+n)(s,0,...,0), not an inter-moduli Chow-class equality |
| `lmm:s06:critical-circle`, `eq:s06:critical-derivatives`, `eq:s06:circle-bound` | Phi has no zero on the closed critical disk; nondegenerate positive saddle and strict Gaussian circle estimate |
| `eq:s06:phi-product` | DLMF product translated to Phi and positive z_(1,k) |
| `lmm:s06:vertex-bound`, `eq:s06:vertex-bound` | C^(n+1) beta_G m! R^(-m)/sqrt(m+1) bound for every stable type and s_i in [0,1], with C independent of G,n |
| `prp:s06:tree-tail`, `eq:s06:tree-expansion` | Exact stack-weighted stable-tree sum for 12^(g_2)b_g/g_2! |
| `eq:s06:tree-degree`, `eq:s06:edge-mass` | Sum m_v=g_2-E, E<=g_2; full E-edge/genus/valence absolute majorant, including all small types |
| `eq:s06:factorial-convolution` | Sum k!(M-k)!<=3M!, M>=0, iterated in the complete composition sum |
| `prp:s06:tree-tail` | Entire E>=K mass is O_K(T_g g_2^-K) for each fixed K>=1, using the all-range square-root bound sqrt(E+1) |
| `eq:s06:one-edge`, `lmm:s06:nonelliptic-tail` | Ordered split with half; all both-nonelliptic splits have relative O(g_2^-3). Endpoint orders start at 2 |
| `lmm:s06:saddle`, `eq:s06:additive-saddle` | Additive leading coefficient for a fixed analytic P on a neighborhood of the CLOSED disk, uniform for bounded families on one fixed neighborhood; valid at P(x_*)=0 |
| `eq:s06:cauchy`, `eq:s06:local-saddle` | Actual coefficient integral, outer-arc bound and integrable m^-2 local remainder with both odd half-orders explicitly retained |
| `eq:s06:two-term-saddle` | P=1 two-term asymptotic with correction -1/4+1/(24x_*)=-1/4+1/(6z_(0,1)^2), relative O(m^-2) |
| `lmm:s06:elliptic-leaf`, `eq:s06:elliptic-exact`, `eq:s06:elliptic-relative` | Exact elliptic-leaf coefficient and relative pi^2 J_1(z_(0,1))^2/(6g_2)+O(g_2^-2) |
| `eq:s06:combined-expansion`, `subsec:s06:04` | Complete proof of the original Theorem 1.3 and identification of all three terms in b |

There are nine principal results, immediately followed by proofs, and
26 numbered formula labels. The example b_2=1/5760 checks the stack half
and 12 conversion. The original theorem label/number remain unchanged.

## Literature and convention mapping

- `FP03`, Theorem 1 (journal p.100 / fixed PDF p.4): the positive-genus
  multipoint theorem; equation (1), p.98 / PDF p.2: stable genus zero.
  Its source-header journal typo is not used as bibliography metadata.
- `FP00`, Theorem 2, equation (6) (p.175 / PDF p.3): one-point series;
  Section 4.2, Lemma 1 (p.194 / PDF p.22): Bernoulli evaluation. Its b_G
  is explicitly translated to beta_G immediately after
  `eq:s06:beta-definition` in the body, citing (3)/(6). The multipoint
  proof is credited to FP03.
- `KMZ96v1`, (0.8): classical genus-zero inverse and earlier Zograf
  attribution. The Remark explicitly converts its raw kappa-power
  coefficient to Wtop_(0,N)(0)/(N-2)! by Lagrange inversion.
- `MaZ00`, Section 6, (17), Proof 6.3 of Theorem 6.1 (journal
  pp.529--530 / PDF pp.12--13): inverse/critical analysis. Both body
  citations identify the numbered Proof 6.3. Its x_0 is our R; the
  positive x_* is independently defined and proved here.
  The printed negative y_0 in (17) is not imported. No published erratum
  is asserted and no fixed-genus marking asymptotic is used as a uniform
  all-type estimate.
- `DLMF`, (10.21.15), (10.21.2), (10.6.6), (10.6.3): product, interlacing
  and derivative identities. Equations (25.6.2), (25.2.1) supply the zeta
  conversion/series in the one-point estimate. The Gaussian strengthening
  of the circle bound is proved here.
- s02 `crl:s02:kappa-exponential`, `lmm:s02:rational-tail-degree`:
  whole-background inversion with new weight psi*(1-exp(-psi)); no
  additional new-point exponential is inserted into that formula.
- s02 `crl:s02:defect-allocation`, `eq:s02:tautological-gluing`,
  `eq:s02:boundary-exponential`: labelled-product top-class tree restriction,
  logarithmic gluing and exact boundary weights. No equivariantly trivial
  cycle quotient on a graph quotient stack is asserted.

## Review boundary

The mathematical draft and roadmap are complete with no known source or
proof gap left as an input. The all-type estimate, whole-tree sum and
retained saddle remainder are proved in the text, rather than inferred
from finite coefficient checks. Independent frozen review is still needed.
Actual validation/build outcomes and author checks are reported in the
current handoff. No shared input, accepted chapter or old record is edited.
