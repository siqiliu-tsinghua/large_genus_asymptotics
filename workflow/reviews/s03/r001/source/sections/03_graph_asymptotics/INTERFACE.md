# Uniform asymptotics for stable graph sums

Document role: scientific interface for the complete s03 author submission.
Live review and acceptance status are recorded in `workflow/state.json`.
This document exports the submitted statements and their hypotheses; it does
not confer approval or a proof of the four complete introductory targets.

## Dependencies and scope

The Introduction supplies the stack/Chow/complex-codimension conventions,
Hodge notation, lowercase integral families, normalized bracket, `N_g`,
`g_2=2g-3`, Bessel names and four target labels. These are inherited directly.
The s02 dependency is the approved r005 snapshot
`5634fa68be11f0aec6929967508aa7a9cb6b4140dddeba004534a06281f68f9d`.
Its psi, logarithmic kappa, boundary, stable-graph, gluing and automorphism
conventions are unchanged. We use its exact boundary formula, the unmarked
`12lambda_1=kappa_1+delta` and factorial conversion. All estimates in s03
are new analytic statements and do not follow from s02's finite-genus
identities alone.

All truncation orders, marking counts in fixed-marking claims, and requested
derivative orders are fixed before genus tends to infinity. Growing graph
types, valences and loop counts are covered only by the explicit uniform
bounds stated below. No symbol replaces `g_2` or the inherited Hodge indices
`j_1,...,j_ell`; `ell` remains their product length. Ordinary `B_m` remains
the Bernoulli family and Chow coefficients remain inside parentheses.

## Definitions and notation ledger

| Symbols | First location | Type, scope and purpose |
| --- | --- | --- |
| `alpha=2pi^2` | 3.1 opening | WP scale, used in every subsequent WP integral; first introduced where needed |
| `G,n`, `y_i`, `V_{G,n}(y)`, `V_{G,n}` | `eq:s03:wp-definition` | A stable vertex genus/marking pair, real nonnegative boundary lengths, length and cusp volumes; inherited stack integration |
| `d_i`, vector `d`, `|d|`, `[tau_d]_{G,n}` | `eq:s03:descendants` | Nonnegative integer descendant tuple and total degree; bracket zero beyond dimension, empty tuple gives `V_{G,0}` |
| `Gamma(k)` | Before `prp:s03:wp-inputs` | `(k-1)!` for positive integers; factorial notation in uniform bounds, not a graph |
| `c_r(n)` | `eq:s03:fixed-n-volume` | Fixed-n WP expansion coefficients, coherent in truncation; `c_1` explicit in `eq:s03:c-one` |
| `c_H` | Before `prp:s03:wp-inputs` | One fixed HMT integer greater than 600 and the constant in its Lemma 2.6; needed to retain the actual thresholds |
| `T_{G,n}`, `eta_r`, `epsilon_K` | `eq:s03:hmt-form` and its three cases | Local quantified notation for each of three separate HMT quantities, its coefficients and remainder; no new permanent names for the two ratio families |
| `K`, `D`, `a_i`, `m` in the input proof | 3.1 input statement/proof | Fixed nonnegative truncation, total descendant degree, nonnegative monomial exponents and their total; local bound indices, not half-edge parameters |
| `F_g`, `Z_g(u)` | `eq:s03:deformation` | WP factorial scale and polynomial boundary deformation, `g>=2`, `u` complex |
| `W^{WP}_{G,n}(t)` | `eq:s03:vertex-function` | Entire polynomial in complex half-edge parameters; WP vertex function distinct from later top-Hodge functions |
| `s_e`, `t_i`, `t_f` | `eq:s03:integrated-graph-formula` and vertex definition | Real unit-interval edge parameters and complex cotangent parameters; both flags of an edge share `alpha*u*s_e` |
| `f(t)`, `S(u)` | `eq:s03:loop-functions` | Entire half-edge and loop functions; sine quotient interpreted as a series; Cin identity first for real `u>=0`, then continued through `S` |
| `Z_Gamma(u)` | 3.3 opening | Complete summand in the exact integrated graph formula; used for absolute tails and core expansions |
| `k_v`, large vertex, `q` | Before `lmm:s03:pairing-majorant` | Positive vertex complexity `2g_v-2+n_v`, vertex above half the total, and total complexity away from it; graph-dependent, with `q` defined only when large vertex exists |
| `H` | Counting estimates in 3.3 and the two ratio/marked counting proofs | Temporary scalar `2g-2`, or explicitly `2g-2+r` in the fixed-labelled-leg extension. Local to these calculations; distinct from inherited flag set `H(Gamma)` |
| `C_0`, `sigma`, `X`, expectation `E` | `lmm:s03:pairing-majorant` | Compact-dependent constants and a half-normal variable with its explicit density; sums every labelled pairing at once |
| `P_m(x)`, `U_k(x)` | `eq:s03:counting-polynomials` | Local truncated exponential and factorial polynomial for valence sums; cap `n<=k+2` is retained |
| `T_{M,c}(H,x)`, `epsilon_0`, `eta` | `eq:s03:short-series` and proof | Local short-complexity series, small range constants; `c` is only 2 or 3 in this lemma |
| `1_A`, `epsilon`, Gaussian split points | `prp:s03:graph-tail` proof | Indicator of an event, small cutoff chosen after fixed majorant constants; split at `epsilon H` and `H^(1/4)` |
| `Gamma_c`, core type, `Gamma(p)` | 3.4 opening and `lmm:s03:finite-cores` | Graph with its distinguished large vertex, obtained by contracting its loops and increasing genus. Type excludes the forced large-genus label; `Gamma(p)` restores `p` loops when legal |
| `p`, `n_0`, `c`, `G,n` in a core | `eq:s03:core-parameters` | Nonnegative large-vertex loop count, core valence and fixed genus loss; unmarked `2c=q+n_0`, restored `(G,n)=(g-c-p,n_0+2p)` |
| `Q_K(p)`, `N`, `z` | `prp:s03:core-expansion` proof | Local polynomial majorant, number of finite ratio factors and coefficient variable; proves polynomial-in-p multiplication errors |
| `gamma_{Gamma_c,p,r}(u)` | `prp:s03:core-expansion` | Auxiliary entire core/loop coefficients, with factorially summable compact bounds; needed to construct the main coefficients |
| `gamma_k(u)` | `thm:s03:graph-expansion` | Entire coefficients of `Z_g/V_{g,0}`; `gamma_0=e^S`, constructed by finite cores and a normally convergent loop sum |
| `r`, external `t_i`, derivative `d_i` | `crl:s03:marked-extension`(i) | Fixed number of labelled legs, complex external parameters and fixed nonnegative psi derivative orders; additive expansion, including zeros of its leading term |
| `s`, `D_Gamma`, `C,C_1,B,T` | `crl:s03:marked-extension`(ii) | Fixed polynomial weight degree and an explicitly majorized family of graph contributions; constants uniform in genus and graph, allowed compact dependence |

Generic positive constants and bound indices have the scopes indicated by
their local statements. `c_H` and the core genus loss `c` are distinct.
The generic input coefficients `eta_r` are not a competing global family.
The source's integer monomial exponents are translated to `a_i`, reserving
`t_i` for analytic cotangent parameters. Real boundary lengths are `y_i`;
the inherited `L_i` still denotes a cotangent line bundle. The scalar `y`
in the q-tail proof is local to its auxiliary-weight argument.

## Exported statements

| Result / labels | Precise export |
| --- | --- |
| `prp:s03:wp-inputs`; `eq:s03:fixed-n-volume`, `eq:s03:c-one` | Every FIXED n and order, absolute WP expansion with leading constant `1/sqrt(pi)` and explicit first coefficient; this alone asserts no growing-n uniformity |
| `eq:s03:all-type-input` | Uniform volume bound at every stable type including complexity one, and coefficientwise descendant bound for n>=1; n=0 handled directly |
| `eq:s03:hmt-form`, `eq:s03:hmt-descendant`, `eq:s03:hmt-cusp`, `eq:s03:hmt-genus` | Exact HMT thresholds, coefficient bounds and polynomial remainders at every fixed order; A3 is the inverse cusp ratio; A1 has no independent total-degree threshold |
| `lmm:s03:exact-deformation`; `eq:s03:normalization-links`, `eq:s03:integrated-graph-formula` | Exact finite-genus graph formula for complex u and `Z_g(1)/F_g=a_g/N_g`; no analytic exchange is used |
| `lmm:s03:vertex-bound`; `eq:s03:vertex-bound` | Constants independent of genus/valence on each fixed bounded parameter set; real comparison lengths are `sqrt(2|t_i|)` |
| `lmm:s03:pairing-majorant`; `eq:s03:gaussian-majorant` | Entire absolute graph sum, including an absolute value inside edge integrals, dominated by one labelled composition/Gaussian expression; retains valence cap and square-root cancellation |
| `lmm:s03:short-series`; `eq:s03:short-series` | All interval estimates in-section for the factorial series at `c/H`, c=2,3; constants chosen before Gaussian absorption |
| `prp:s03:graph-tail`; `eq:s03:graph-tail` | For fixed M and compact complex u set, full absolute sum with no large vertex or q>=M is `O(F_g*g^-M)`; full sum `O(F_g)`; no Appendix input |
| `lmm:s03:finite-cores`; `eq:s03:core-parameters`, `eq:s03:core-automorphisms` | Finite core types at fixed q, genus-correct contraction, exact `2^p*p!` factor |
| `lmm:s03:loop-tail`; `eq:s03:loop-majorant` | Every legal loop count, even small vertex genus, bounded by `g^-q*C^(p+1)/p!`; p>log g negligible to every fixed inverse power |
| `lmm:s03:degree-moments`; `eq:s03:degree-moments`, `eq:s03:joint-degree-tail` | Exponential degree moments and joint loop/degree tails; permits summing HMT polynomial errors before replacing p or D by a logarithmic cutoff |
| `prp:s03:core-expansion`; `eq:s03:core-volume-path`, `eq:s03:core-expansion`, `eq:s03:summable-remainder` | Exact nonnegative-marking ratio path; all intermediate HMT thresholds checked; fixed-core expansion with per-p error `g^(-q-K-1) C^(p+1)(1+p)^s/p!` and coherent entire coefficients |
| `thm:s03:graph-expansion`; `eq:s03:graph-expansion`, `eq:s03:coefficient-rule` | Every fixed order for `Z_g/V_g0`, locally uniform complex expansion; entire gamma functions, leading `e^S`; fixed u derivatives preserve remainder order |
| `crl:s03:marked-extension`(i); `eq:s03:marked-deformation`, `eq:s03:marked-volume-scale` | Fixed r labelled legs, expansion normalized by `V_g,r`, ADDITIVE and locally uniform in r+1 complex variables; leading `e^S prod f(t_i)`; all fixed external psi/mixed derivatives |
| `crl:s03:marked-extension`(ii); `eq:s03:decoration-condition` | For the displayed graphwise positive majorant with polynomial loss H^s, full marked bad-graph sum `O(F_g*g^(r+s-M))`. Fixed leg allocation has no extra H^r loss. Does not assert an expansion for an unspecified internal decoration |

Subsection labels `subsec:s03:01`--`subsec:s03:04` and section label
`sec:s03` are stable. Source statement numbers and local result numbers
are different; downstream sections should cite the stable labels.

## Verified source mapping

- `Wol86`, Section 5.1, printed p. 138 / scan PDF p. 21: unmarked
  WP class including extended cohomology. Do not treat its short
  Corollary 5.11 as a literal factor formula or attribute all marked
  logarithmic conventions to the original unmarked statement.
- `Mir07`, Theorem 4.4, printed/PDF p. 14, and elliptic-involution
  discussion p. 4: boundary-length polynomial and the (1,1) exception.
  Our entire (1,1) polynomial is half its effective geometric polynomial.
  WP class normalization is sourced to Wol86 plus MZ15 Section 2.
- `MZ15`, bibliography's fixed preprint numbering: Section 2 / PDF p. 4
  for logarithmic brackets and lengths; Theorem 1.2 / pp. 1--2 and
  Remark 1.3 / p. 2 for the fixed-n expansion and first coefficient.
  Its originally undetermined absolute constant is supplied by the next
  two independent inputs, not asserted as proved in MZ15.
- `LX26`, Corollary 1.2 (1.8), PDF p. 3, and unmarked discussion in
  Section 9: constant `1/sqrt(pi)`. No extension of its higher-correction
  theorem to an unstated unmarked range is used.
- `W26`, Corollary 1.2, PDF p. 6: independent constant. Section 4.1 /
  p. 20, (4.4), (4.6), (6.1) / p. 31 and Lemma 6.1 (6.7) / p. 32:
  amplitude/bracket translation and all-degree normalized positivity.
  At Y=0 the common scaling is `4^(-(3G-3+n))`, independent of d.
- `SW25`, fixed v4, Lemma 14 / PDF p. 11 and Lemma 18 / p. 12:
  real-length estimate and all-type factorial bound; complexity-one
  types are checked in our convention.
- `HMT25`, fixed v2, (4.1), Theorem 4.2 A1/A3/A4, PDF pp. 27--28:
  descendants, inverse cusp ratio and genus-exchange ratio. Their
  positive-polynomial coefficients are written using total degree via
  the multinomial theorem. The integer c is called c_H; local eta_r
  avoids importing three unrelated source coefficient names. HMT's
  (1,1) geometric volume convention differs, but the large-genus
  inputs concern matching types; our all-type bases are separate.

All seven keys exist with the checked versions in the shared bibliography.
No raw version identifier occurs in manuscript prose. The exact graph
deformation follows s02; the global Gaussian tail, core summability and
entire coefficient construction are proved here, not attributed wholesale
to a volume source. Internal lecture notes were only preparation leads.

## Remaining work beyond this section

No known external-source gap is left open for the stated s03 results,
subject to independent whole-section review. The full draft and roadmap
are supplied. The next section must still compute genuine second-order
data: the second multidegree descendant and diagonal coefficients, q=1
first corrections, q=2 leading contributions, and the second absolute
fixed-n base-volume coefficient. This section supplies summability and
existence, not those numerical computations or the full Theorem 1.1.

W26 Lemma 7.2 and Appendix C.1, Lemma C.1, give fixed-marking profile
coefficients. Later use must identify them with HMT's unique coefficients
at each fixed tuple, convert `2G-2+n` to G, then invoke HMT's polynomial
remainders for growing valence. Their fixed-marking lemma alone does not
give that growing-n uniformity. Low-degree exceptions must be retained.
Concrete internal GRR decorations must satisfy the majorant condition
before using the exported weighted tail. The positive-new-psi condition
and surviving negative new-psi term in s02's forgetting comparison remain
in force when such markings represent kappa insertions.
