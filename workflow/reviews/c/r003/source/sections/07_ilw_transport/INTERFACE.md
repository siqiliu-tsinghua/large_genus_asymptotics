# Linear Hodge potentials and transport at fixed defect

Scientific interface for the complete s07 author draft. This document is
not an approval or review signature. Live submission, freshness and
acceptance status belongs to `workflow/state.json`.

## Dependency and scope

The scientific dependency closure is s01, s02 and s06. In particular,
this proof uses no WP graph-tail estimate, coefficient table or signed
loop calculation from Sections 3--5 or Appendix A.

Historical scientific provenance before the S07-SHARED update:

- s02 r009: `33ec1495090af03c99be89a5f5b272437f6d2792aaabb075bc9d4831c3cb2084`.
- s06 r003: `3bb0091152f459efb5cb63ee188e913e5e3e2ea163126c82245a77f52ad02ec7`.

These record historical scientific-source provenance. Those scientific
files were preserved during the completed shared-input refresh.
Current dependency approval and freshness belong to `workflow/state.json`.

The section proves exact formal identities and fixed-genus
characteristic integrals. It does not prove `thm:fixed-defect` or
`eq:gh11`. The Borel singularities, coefficient transfer, primitive
estimates and comparison of kappa and Hodge backgrounds belong to
Section 8.

## Inherited definitions and inputs

| Symbols / result | First definition and use here |
| --- | --- |
| g,n, moduli stacks, lambda classes, rational Chow coefficients and stack integrals | Introduction; no section-level restart |
| g_2=2g-3, b_g(h), b_g, z_{0,1}, rho,b | Introduction; exact unmarked kappa degree uses g_2+h, without renaming g_2 |
| psi_i and logarithmic kappa_a | Section 2.2; used in the raw descendant potential and forgetting specialization |
| B_n | Section 2.2, `eq:s02:bernoulli-convention`; ordinary Bernoulli numbers, never an integral family |
| `eq:s02:kappa-exponential` | Section 2.4; exact exponential forgetting identity, applied with parameter one and a pulled-back Hodge class |
| beta_G, beta_0=1, beta generating series | Section 6.1, `eq:s06:beta-definition`, `eq:s06:beta-series`; fixes the inverse-sine coefficients and genus-one value |
| lambda_g theorem | Section 6.1, `eq:s06:lambda-g`; fixes the entire eta^0 sector |
| Phi,w,x_*,R and zeta | Sections 6.1--6.2; w=u Phi(u) specializes W, while the previously defined zeta series normalizes the Bernoulli coefficients |

## New notation and first definitions

| Symbol | Definition label / location | Type, range, scope and reason |
| --- | --- | --- |
| t_d, bold t, x=t_0 | Before `eq:s07:hodge-potential` | Formal descendant times for integer d>=0; x remains the zero time throughout this route |
| hbar,epsilon | `eq:s07:hodge-potential` | Formal genus and Chern-degree parameters matching Buryak's positive epsilon^j convention |
| calligraphic F | `eq:s07:hodge-potential` | Stable, raw linear Hodge potential; not F_g or F(j) from the WP route |
| z,eta and F_{g,h} | `eq:s07:defect-variables` | z=hbar epsilon and eta=epsilon^-1; coefficient z^g eta^h contains lambda_{g-h}, g>=h>=0 |
| calligraphic G,G_{g,h},U | `eq:s07:miura` and the following sentence | Sine-transformed potential, its coefficients, and U=partial_x^2 G; formal operator series, no square-root branch |
| c_k | `eq:s07:ilw-coefficients` | Positive rational Bernoulli coefficients, integer k>=1, used in each transport layer |
| v and W(u) | `eq:s07:genus-zero-inverse` | Full-time formal inverse pair, W(v)=x, v with zero constant term; u is the local formal argument |
| theta | `eq:s07:times` | Formal auxiliary parameter t_1=-theta; for characteristic integrals also a fixed real theta>=0 with x locally complex |
| F_{g,h}(theta;x),G_{g,h}(theta;x) | After `eq:s07:times` | Evaluation at the displayed times; same coefficients as the full potential, not new potentials |
| T_{g,h,n} | `eq:s07:kappa-integrals` | Raw integral lambda_{g-h} exp(kappa_1), integers g>=h>=0,n>=0 with stable target |
| w_theta,v_theta | `eq:s07:specialized-inverse` | w_theta=w+theta u and its inverse germ at zero; coefficients rational in 1+theta |
| calligraphic I_d | `eq:s07:jets` | Shifted times, integer d>=1; separate typography avoids a Bessel-I notation collision |
| W_k | `eq:s07:jets` | kth u derivative of W evaluated at v, integer k>=1; finitely many inverse-function jets occur at each g,h |
| L_{g,h} | `eq:s07:transport-definitions` | partial_x G_{g,h}, g>=h>=1, with the same parenthesized notation after specialization |
| script D | `eq:s07:transport-definitions` | Full-time transport partial_{t_1}-v partial_x; specialized form -partial_theta-v_theta partial_x |
| X_sigma | Corollary `crl:s07:characteristic-recovery`, before `eq:s07:characteristic` | Characteristic coordinate x+sigma v_theta(x), real sigma>=0; fixed inverse value and branch |
| Lambda_theta(x,y) | `eq:s07:logarithmic-kernel` | Normalized log difference quotient, zero constant term in auxiliary increment y; reused in the first Borel layer, never a new Phi |
| calligraphic L_h | `eq:s07:borel` | Borel series, integer h>=1, factorial (2g+h-2)!; y now the independent formal Borel variable. Distinct type/scope from the earlier unindexed signed loop functional |
| calligraphic K | `eq:s07:linear-kernel` | Linear operator on a formal input with locally analytic x coefficients; theta held fixed and shifts read as Taylor series |
| calligraphic N_h | `eq:s07:quadratic-kernel` | Quadratic expression in positive layers summing to h, h>=2; it enters transport with the external factor 1/2 |

Bound indices g,n,j,d_i in the potential are explicitly scoped there;
j is a Hodge-class index. In the recursive sums, k is a positive
derivative/genus increment, i is a defect split, and g',g'' are ordered
genus splits. Neither ell nor g_2 is reused for these purposes.
The variables a,u,V,A in individual proofs are local. In the Borel
linear kernel, a=(1-tau)y/m is a local shift, m>=1 is an integer,
and tau lies in [0,1]. In the quadratic kernel t,tau are real variables
in [0,1]. The local degrees N,N',N_1,N_2 are nonnegative integers bound
in the coefficient verification. The indicator in the string
characteristic is defined at its first use. No separate Euler-operator
name is introduced: the formula uses 1+y partial_y.

## Exported exact results

1. `thm:s07:ilw`, `eq:s07:ilw`, `eq:s07:inverse-miura`:
   Buryak's first ILW flow in the z,eta variables and the inverse sine
   transformation with beta_k. It is an identity of numerical
   intersection-generating series, not a new identity of Chow classes.
2. `lmm:s07:top-sector`, `eq:s07:top-sector`:
   F_{g,0}=beta_g partial_x^{2g} F_{0,0} for g>=1 and
   G_{g,0}=0 for g>=1; U at eta=0 is the inverse v.
3. `lmm:s07:string`, `eq:s07:string`:
   the raw string term is x^2/2+z/24. The sine transformation cancels
   z/24; coefficients with g>=h>=1 obey the homogeneous equation.
   This is a main lemma with its geometric proof immediately following.
4. `prp:s07:specialization`, `eq:s07:specialization`:
   partial_x^n F_{g,h}(0;0)=T_{g,h,n} for stable targets.
   `eq:s07:unmarked` identifies the exact kappa power and factorial.
   It does not identify this background directly with b_g(h).
5. `lmm:s07:finite-jets`, `eq:s07:finite-jets`:
   for g>=2 and 1<=h<=g, the finite sum has d_i>=2,
   sum(d_i-1)=2g-3+h, hence n<=2g-3+h. Genus one is handled
   separately by `eq:s07:genus-one-seed`, F_{1,1}=G_{1,1}=-log W_1/24.
   Positive x derivatives are rational jets with denominator degree
   at least two and vanish when the higher jets vanish.
6. `prp:s07:transport`, `eq:s07:transport-one`,
   `eq:s07:transport-higher`:
   exact positive-defect transport, separately h=1 and h>=2.
   All integration constants from U to L vanish by the rational-jet
   kernel argument in the immediately following proof. This proposition
   contains only the full-time differential recursions.
7. `crl:s07:characteristic-recovery`, `eq:s07:characteristic`,
   `eq:s07:characteristic-one` and
   `eq:s07:characteristic-higher` recover L from its zero infinite-end
   value. For fixed integers g>=h>=1 they are convergent for real
   theta>=0 and x in a small complex neighborhood of zero, on the
   branch with fixed v_theta(x), and valid coefficientwise as formal
   Taylor identities. Derivatives are taken before evaluation on the
   characteristic. Its proof contains the jet shift, endpoint decay
   and integration argument. The Borel convergence citation points here.
8. `lmm:s07:first-kernel`, `eq:s07:first-kernel`:
   L_{g,1}=c_g(2g-1)! [y^{2g-1}] Lambda_theta for every g>=1.
   Removing log partial_x v_theta changes no positive coefficient.
9. `prp:s07:borel-transport`, `eq:s07:borel-one`,
   `eq:s07:borel-transport`:
   exact common-normalization Borel kernels. The proof contains the
   full Beta integrals, derivative orders and genus reindexing.
   The minimum degree is 3h-2, parity (-1)^h. Each scalar m sum is
   absolutely convergent, and each characteristic integral is taken
   only after fixing its output coefficient.

## Verified sources and conversions

- Bur15, fixed v4: Theorem 1.1, (1.1)--(1.2), PDF p.2.
  The source weight hbar^g epsilon^j becomes z^g eta^{g-j}.
  Its F^Hodge, tilde F^Hodge and u become our F,G,U.
  The inverse transformation and string-recovery discussion are also
  on PDF p.2. The precise string anomaly and its cancellation are
  derived in `lmm:s07:string`, rather than inferred from the field.
- Bur16, fixed v2: Theorem 1.1 and (1.2), PDF p.1; Section 2
  provides the shorter coefficient computation behind the ILW result.
  This is supporting source credit, not a second convention for the
  parameters or potentials.
- FP03 Theorem 1 and FP00 Theorem 2/(6) are used through the already
  proved and normalized s06 top-Hodge and beta-series exports.
- The forgetting identity is used through the s02 Chow proof and
  `eq:s02:kappa-exponential`, without an additional unverified source
  locator. String/dilaton operations, the genus-one logarithm, finite
  jets, characteristic endpoint and the two Beta kernels are proved
  in this section. The lecture notes supplied a route only.

## Remaining work and validation boundary

No known exact-algebraic gap remains in this author draft. This claim
is subject to independent frozen review. Required later analysis:
common inverse domains, full Borel convergence/continuation, endpoint
and remote-characteristic estimates, both dominant singularities,
primitive estimates for G, coefficient transfer, and the kappa versus
12 lambda_1 comparison. None is claimed as an export here.
