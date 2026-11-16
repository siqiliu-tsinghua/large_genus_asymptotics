# Singularity analysis and Hodge integrals at fixed defect

Scientific interface for the complete Section 8 author draft. Live
review, freshness and acceptance status belongs to workflow/state.json.
This document is not an approval or a reviewer signature.

## Scope and assembly

The entry begins by naming Theorem thm:fixed-defect, then explains
the four steps connecting exact Borel transport, singularity
propagation, coefficient recovery and background comparison.
It assembles the six assigned subsection files without new inputs.
The final result is exactly the asymptotic equivalence eq:gh11;
no relative O(1/g) rate is claimed for that theorem.

The mathematical dependencies are s07 and approved Appendix B,
with their s06/s02/s01 closure. The approved Appendix B supplied at
assignment was r002, snapshot
411761e7652ee98e65b32c35dc51dd0e494169ffa3ed4851646ebb200deb0871.
This is historical provenance; current acceptance belongs to the
workflow. There is no dependence on WP Sections 3--5, Appendix A,
an unpublished numerical calculation, or a future appendix.

## Inherited objects and exact inputs

| Object or input | Original location and actual use |
| --- | --- |
| g,n, moduli stacks, rational Chow and stack integration, lambda classes | Introduction; inherited directly without a new setup |
| g_2, b_g(h), b_g, z_{0,1}, rho, scalar b, Hodge j-family and ell | Introduction; original meanings preserved; rho=12R is used in the last normalization |
| psi, logarithmic kappa, delta and ordered branches | s02.2, in particular eq:s02:lambda-one-grr and eq:s02:ordered-boundary; supply 12 lambda_1=kappa_1+delta on the unmarked stack and the one-node factors |
| Hodge restriction and Mumford relation | eq:s02:hodge-normalization, eq:s02:hodge-factorization and eq:s02:chern-exponential; give the boundary splitting and c_t c_-t=1 |
| beta_g, Phi,w,x_*,R | s06.1--s06.2; eq:s06:beta-asymptotics, eq:s06:critical-data and eq:s06:critical-derivatives fix all constants |
| Exact top vertices and saddle | eq:s06:exact-vertex, eq:s06:vertex-bound, eq:s06:additive-saddle; supply h=0 and its fixed-marking bounds |
| Fcal,Gcal, their (g,h) components, theta,x,v_theta | s07.1--s07.2; exact potentials and inverse specialization; t_0=x remains the zero descendant time throughout |
| T_{g,h,n} | eq:s07:kappa-integrals and eq:s07:specialization; raw exponential kappa integral on each stable target |
| L_{g,h}, indexed calligraphic L_h | s07.3--s07.4; x derivative of Gcal and Borel normalization (2g+h-2)! |
| Exact inverse sine and Borel transport | eq:s07:inverse-miura, eq:s07:borel-one, eq:s07:linear-kernel, eq:s07:quadratic-kernel and eq:s07:borel-transport |
| Inverse radius and characteristic geometry | prp:b:inverse-budget, lmm:b:cone-transport, prp:b:tube, crl:b:remote; supply full complex domains, including regular negative-center patches |
| Endpoint class and local recovery | lmm:b:linear-endpoint, lmm:b:quadratic-endpoint, lmm:b:local-transport, prp:b:common-domains; justify actual singularity propagation and fixed derivatives |
| Primitive and coefficient bound | lmm:b:primitive, lmm:b:coefficient-bound, prp:b:primitive-bound; control the free-energy constant and its marked derivatives |

Ordinary B_n remains the Bernoulli family. The unindexed signed loop
functional of the WP route is not used. No new macro or package is needed.

## New notation, first definitions and scope

| Symbol | First main-text location | Type, scope and reason |
| --- | --- | --- |
| x_{*,theta}, R_theta | eq:s08:critical-data | Small real-analytic critical branch/value of w_theta; x_{*,0}=x_*, R_0=R. These match B's technical notation; Section 8 precedes B in the assembled paper |
| H,theta_H,r_H,gamma_H,nu | crl:s08:domains | Fixed finite layer cap H>=1, positive thresholds and a real 1/2<nu<1; inherited B estimates are uniform only for this cap and fixed angular margins |
| S | crl:s08:domains and subsequent local arguments | Explicit local distance R_theta-x; complex on the continued sectors; never an alias for delta |
| P_h(theta,x),P_h(x) | eq:s08:leading-expansion; eq:s08:principal-recurrence | Unique actual positive-endpoint square-root coefficient, h>=1; latter is theta=0. Repeated in transport and coefficient recovery; its possible complex zeros are never divided out |
| E_h(theta;x,y) | eq:s08:leading-expansion | Actual value remainder, with scale and fixed-derivative bounds in eq:s08:leading-bounds; not a new potential |
| Calligraphic B(x) | eq:s08:transport-integral | Convergent transport integral on 0<=x<R; B(R)=0 by extension. Distinct from Bernoulli B_n; its powers encode ordered integrals |
| Y_0,H_a | Before lmm:s08:bessel-constant | Second-kind Bessel function on the positive real axis and harmonic numbers for integer a>=0; confined to the exact constant evaluation |
| D_{g,h} | eq:s08:degree; extension before prp:s08:intersections | Repeated coefficient degree g_2+h, initially g>=h>=1, then h=0 on unmarked stable targets. Does not rename g_2 |
| Calligraphic F_h^+(theta;x,y) | eq:s08:inverse-borel-definition | Borel series of Fcal-Gcal with factorial D_{g,h}!, h>=1; superscript selects positive inverse-operator powers, not positivity |
| T_{g,h} | Before prp:s08:intersections | Recurring unmarked shorthand T_{g,h,0}, g>=2 and 0<=h<=g |
| T_{g,h}^delta | eq:s08:node-definition | Same unmarked family with one boundary divisor insertion; avoids reusing the ILW field U |
| p,xi | Before prp:s08:background | Quotient projective bundle p:P(E)->Mbar_g and c_1(O(1)), confined to 8.5; base classes are explicitly pulled back |
| C_k | eq:s08:mixed-intersections | Local mixed intersection sequence, integer 0<=k<=D_{g,h}, used only in the background-comparison proof |

Grouped dummy scopes: m>=1 indexes kernel branches; k>=1 indexes
the inverse-sine terms; a=2k-2 is a nonnegative Taylor degree and
N' an input coefficient degree. The path variables u,s and angular
parameters are bound in their respective integrals. In the two-point
lemma Y is the normalized complex variable, N a positive integer,
and A_+,A_- complex amplitudes. The marked bound uses only fixed
n in {0,1,2} and M=2g-3+h+n. In the node proof G is an integer
component genus, i a component defect, and a,c its nonnegative
coefficient degrees. In 8.5 real a,c in the quoted ample-cone
criterion have only that sentence's scope, t is a local formal
Chern variable, and j is a Chern-class index. Geometry uses r,r_H
or a fixed positive c; epsilon retains its formal Hodge meaning.
The recovered-singularity proof writes its endpoint distance S-y
directly, without introducing an alias or reassigning t_0.

## Exported results

1. lmm:s08:inverse, eq:s08:inverse-singularity,
   eq:s08:perturbed-inverse: unique dominant inverse singularity
   with normalized coefficient z_{0,1}/sqrt(2), uniform small-theta
   Morse expansion and continuation at the other circle points.
2. crl:s08:domains, eq:s08:dented-domains: common actual
   doubly dented analytic regions for a fixed finite set of layers;
   all kernel sums and full characteristic integrals are normal.
3. lmm:s08:seed, lmm:s08:propagation,
   eq:s08:theta-recurrence, eq:s08:principal-recurrence:
   exact seed and integral recurrence for the actual coefficients.
   The positive m=1 linear branch and lower characteristic end
   supply the principal term; other branches are lower order.
4. lmm:s08:ordered-integrals, eq:s08:ordered-integrals:
   P_h=B^(h-1)/((h-1)!(x_*-v_0)) and integral P_h=B(0)^h/h!.
5. lmm:s08:bessel-constant, eq:s08:bessel-constant:
   B(0)=1/(z_{0,1}J_1(z_{0,1}))=1/(2R), with endpoint
   subtraction and a summable factorial bound.
6. lmm:s08:inverse-kernel, eq:s08:inverse-kernel: exact
   direct-derivative inverse-sine Borel kernel, alternating
   (-1)^(m-1), outer m^-2 and a plus between shifts. Derivatives
   are taken before evaluation.
7. prp:s08:recovered-singularity,
   eq:s08:recovered-singularity: additive inverse-square-root
   expansion, uniform for complex x near zero, small theta>=0
   and fixed nu; the proof controls the full path including the
   critical-center initial segment. For u=tau y with
   |u|<=C|S-y|, the center distance S-y+u and both endpoint
   distances S-y, S-y+2u are comparable to |S-y| in a strictly
   smaller critical cone. B's actual cone extension and
   eq:b:common-bounds with one center derivative give the
   integrand bound O(|S-y|^((h-3)/2)); its path length gives
   O(|S-y|^((h-1)/2)). This uses complex cone bounds, not an
   inverse-disk assertion.
8. lmm:s08:transfer, eq:s08:two-point-transfer: uniform
   two-singularity coefficient formula with additive O(N^-nu).
   The actual parity makes the two dominant terms add.
9. prp:s08:intersections, eq:s08:intersection-asymptotic,
   eq:s08:intersection-ratio, eq:s08:marked-bound: positive
   unmarked asymptotic and fixed n=0,1,2 absolute upper bounds
   for every allowed stable target. Genus-one logarithms are
   excluded from the large-genus primitive bound and covered
   separately as finite stable cases. No growing-valence assertion.
10. lmm:s08:one-node, eq:s08:one-node,
    eq:s08:node-bound: exact stack-normalized decomposition and
    entire genus/defect sum O_h(T_{g,h}/g), not a fixed-split bound.
11. lmm:s08:nef: full Hodge-bundle nefness on the compactification,
    determinant nefness, ample kappa_1, smooth-cover descent.
12. prp:s08:background, eq:s08:background:
    b_g(h)=12^(-D)D!T_{g,h}(1+O_h(1/g)). Effective delta,
    mixed Hodge index and the one-node bound control every
    background power simultaneously.
13. subsec:s08:06, eq:s08:final-factorials,
    eq:s08:combined-ratio: complete proof of the Introduction's
    thm:fixed-defect / eq:gh11, retaining the two factorial
    ratios before taking their limits.

There are 13 principal statements immediately followed by proofs,
one final theorem proof, 33 numbered equations and one short
post-proof source remark. These are author-draft counts, not
claims of reviewer approval.

## Verified primary sources and conversions

- DLMF 10.8.2: harmonic-number expansion of Y_0; the J_0 multiple
  vanishes at z_{0,1}. DLMF 10.5.2: Wronskian, giving
  J_1(z_{0,1})Y_0(z_{0,1})=2/(pi z_{0,1}). The series and
  identity were inspected at the official equation pages; no
  alternate Bessel-zero notation is introduced.
- FO90, Section 2: indented-contour transfer method. The locally
  cached author preprint has reversed PDF page order; rendered
  PDF pages 22 and 21 (printed pages 4--5) were actually read.
  The manuscript cites Section 2 and proves its own uniform
  two-point specialization, rather than inventing a published
  theorem locator.
- Fuj78, Main Theorem (0.6), printed pages 779--780: nef relative
  dualizing direct image over a projective curve.
- Kaw81, Theorem 5, printed page 254: smooth projective-base
  semipositivity with a normal-crossing discriminant and
  unipotent monodromy. Semistable reduction and finite-curve
  descent are stated in the application.
- LX26b, Proposition 4.4 and proof (4.2)--(4.3): full boundary
  Hodge-bundle nefness by labeled partial normalization. This
  supplements the generically smooth family input; determinant
  nefness alone is not used as a substitute.
- CH88, Theorem (1.3), printed pages 457--458: ample criterion
  a lambda_1-c delta for a>11c>0; (a,c)=(12,1) gives kappa_1.
  The weaker outside-boundary slope statement is not substituted.
- LX26b, Proposition 6.1 at m=0: smooth projective generically
  finite cover, with positive rational stack degree and projection
  formula. Ample approximation occurs upstairs; ampleness of
  a generically finite pullback is not assumed.

All these keys are already in the settled bibliography. Internal
lecture notes and coordinator computations are leads or independent
checks, not citations or unproved inputs.

## Limits and outstanding work

The mathematical draft is complete at the author level and ready
for a common frozen review. Native compilation, actual page
inspection and independent mathematical/academic/readability
review remain coordinator/reviewer work. The transfer error gives
only relative o(1); no uniform growing h, growing marking count,
next fixed-defect coefficient or relative O(1/g) theorem is exported.
No unresolved source or shared-input request is known.

## Closing conjecture and finite-data diagnostics

- rmk:s08:further-asymptotics is appended after the complete proof in
  06_proof.tex. It conjectures only the h=1 limit
  g*(rho^2*b_g(1)/(24*g^2*b_g)-1)
  -> -2+J_1(z_{0,1})^2/2+pi^2*z_{0,1}^2*J_1(z_{0,1})^4/2.
  It introduces no new mathematical symbol or numbered equation.
  The proved exports above remain unchanged: no higher fixed-defect
  coefficient or stronger remainder is proved by this Remark.
- The old 33 numbered equations, 13 principal statements and 14 proofs
  are unchanged. The original proof is a literal byte prefix of the
  extended 06_proof.tex. The closing conjectural Remark is additional
  to the original post-proof source remark.
- LiuData26 supplies the selected exact rational observations at
  g=2,...,20, fixed source commit
  88dd4a501ecf3fbc124a823ad1589911f86a14e5. The source's general
  g>14 validation caveat remains in the bundle provenance; agreement
  of two extractions is not independent validation of the integrals.
- checks/run.py uses only the archived checks/selected_h1.json and
  mpmath 1.3.0 at 100 decimal digits. Its candidate comes directly
  from the Bessel values, not fitting. The adjacent extrapolation is
  g*residual(g)-(g-1)*residual(g-1), the intercept of the line against
  1/g through the two consecutive genera. This residual notation is
  descriptive code/documentation only, not a new paper symbol.
- The actual run is recorded in checks/verification.json; generated
  output is confined to build/s08-higher-check/results.json.
  Output SHA256:
  de9e0fa164787e403842fcdbb13caa6b5da652b101e787277bed5d36094751b1.
  Code SHA256:
  404074e96f6299ebaf2047a963b1f8e1d24d511a8c30155ba5bd82f5c6531035.
  Selected-data SHA256:
  9e4370649bae7db217ac41fa5197f4756dc618a7d8805688688240df3d7e825a.
  The check is computation_only. Proving the refinement and obtaining
  higher terms for general fixed h remain open.
