# Analytic estimates for transport kernels

Scientific interface for the complete Appendix B author draft. Live
review, freshness and acceptance status belongs to workflow/state.json;
this document is not an approval or review signature.

## Assembly and inputs

section.tex directly assembles five separate subsections:

1. 01_inverse_domains.tex -- inverse domains and characteristic geometry.
2. 02_regular_transport.tex -- normal convergence away from critical points.
3. 03_endpoint_bounds.tex -- linear and quadratic endpoint estimates.
4. 04_local_transport.tex -- local transport and common dented regions.
5. 05_negative_primitives.tex -- negative-axis primitive and coefficient bound.

The coordinator owns the corresponding manifest update. Inputs are s07
and its s06/s02/s01 closure. There is no dependency on Section 8,
Appendix C, WP graph asymptotics or a coefficient computation.
Historical scientific provenance at drafting:

- s06 r005: d507aaa3e42a76f2ad5aafed26f9589deca722c10f1b1521b1c2a1999d28eafd.
- s07 r003: f8d93be7cf973184112eda4d49a6b2f401ba75cb74708bf162660947737271c9.

Shared-only refreshes can preserve these scientific sources; current
approved snapshots remain a workflow matter. FORMAT-003 proof spacing
has no local override.

## Notation ledger

Inherited: w,Phi,x_*,R,beta_g from s06; w_theta,v_theta,L_{g,h},
calligraphic L_h,Lambda_theta,K,N_h, their exact normalization and
parity from s07. No basic setup is repeated. g_2, the Hodge j-family,
ell, ordinary Bernoulli B_n and scalar b keep their meanings.

| Symbol | First location | Type, scope and purpose |
| --- | --- | --- |
| x_{*,theta},R_theta | eq:b:critical-data | Small real-analytic critical branch and value; x_{*,0}=x_*, R_0=R, with no q alias |
| Blackboard D(c,r) | Before lmm:b:angular | Complex open disk, r>0 |
| M_k,calligraphic U_r,T_a | lmm:b:angular and proof | B.1-local derivative series, angular real-part function and Chebyshev polynomials; integers k,a>=0, real radius r. Calligraphic U is not the ILW field |
| a_*,theta_*,Omega_theta,D_theta | lmm:b:convex-domain, eq:b:omega, prp:b:inverse-budget | Fixed positive center, small perturbation threshold, convex u disk and image; univalence and full radius budget are separate results |
| S,calligraphic C_gamma | Before eq:b:cone | Complex distance R_theta-x and its two-distance cone with principal arguments. Normalized distances remain 1-y/S and 1+y/S; delta is not reused |
| sigma,S_sigma | lmm:b:cone-transport | Real nonnegative characteristic parameter and moving distance, with separately stated small-sigma/full-sigma scopes |
| u_0,r,beta,theta_0 | lmm:b:regular-disk | Complex center, positive radius/derivative scale and real base parameter. beta is a local scalar, not beta_g |
| s | Proof of lmm:b:regular-disk | Positive local abbreviation beta+theta-theta_0 |
| Fraktur T_theta^Omega | eq:b:tube | Open inverse-radius tube in complex (x,y), distinct from the transport integral |
| nu,a,c | B.3 endpoint class | Fixed 1/2<nu<1 and nonnegative real scale exponents; shift c in B.1 has a separate bound scope |
| Calligraphic H,J,Q; H_0^pm,H_1^pm,E^pm | eq:b:endpoint-class, eq:b:quadratic-input | Generic holomorphic inputs, quadratic expression, analytic endpoint coefficients and remainder, with full stated hypotheses. These are not actual P_h |
| Calligraphic T,N | lmm:b:local-transport | Truncated characteristic integral and its integer vanishing order N>a+1/2 |
| H,theta_H,r_H,gamma_H | prp:b:common-domains | Fixed maximum defect and resulting thresholds; r_H controls the normalized disk enlargement and small negative interval; no growing-defect uniformity |
| r | Before eq:b:dented-disk | Positive normalized geometric disk enlargement; local to B.4, separately from the regular-disk radius r in B.2 |
| r_0,u_{r_0} | Proof of prp:b:primitive-bound | Fixed positive negative-axis interval size and its corresponding positive parameter w(-u_{r_0})=-r_0; confined to that proof |
| I_k | eq:b:modified-bessel | Modified Bessel function, integer k>=0, real argument 2 sqrt(u), u>0; distinct from shifted calligraphic I_d |
| N | prp:b:primitive-bound | Coefficient degree 2g+h-2, local to this estimate; g_2 is not renamed |

Geometric sizes use r,r_H,r_0; the formal Hodge parameter epsilon
retains its Section 7 meaning.

Other derivative orders, integration variables and compact intervals are
bound in their statements. No new macro or package is required.

## Exported analytic results

1. lmm:b:angular, eq:b:angular, eq:b:derivative-signs: direct angular
   inequalities for |u|<=x_*, x_*<1.446, and derivative-series bounds
   through 1.447. The monotone angular polynomial has minimum 937/2880;
   its absolute series tail is <0.049.
2. lmm:b:convex-domain, eq:b:omega: the positive center repairs the
   theta>0 derivative-real-part degeneration. All shifted maps
   w_{theta+sigma}, sigma>=0, are univalent on the same closed disk.
3. prp:b:inverse-budget, eq:b:inverse-budget, eq:b:morse-inverse:
   full image radius R_theta-x with unique contact at R_theta, also
   on a fixed small negative interval; inverse continuation elsewhere
   and a uniform slit-sector Morse inverse.
4. lmm:b:cone-transport, eq:b:transport-distances,
   eq:b:transport-distance-identity: shift preservation and local
   characteristic scales |S|+sigma sqrt(|S|)+sigma^2. Full convex-image
   distance never decreases, including at interior complex centers.
5. lmm:b:negative-disks, eq:b:negative-radius: inverse radius >R at
   w(-u), u>0, uniformly on compact u intervals.
6. lmm:b:regular-disk, eq:b:regular-hypothesis, eq:b:regular-disk,
   eq:b:regular-derivatives, eq:b:regular-integral: actual normal Borel
   convergence, norm O((beta+theta-theta_0)^(h-1)), all fixed derivatives
   and an integrable full-sigma bound. Constants are independent of
   genus and the local derivative scale.
7. prp:b:tube, eq:b:tube: actual tube holomorphy, normal kernel sums
   and all-sigma integrals, plus joint continuation on noncritical
   boundary arcs. Convergence of the formal series is proved, not assumed.
8. crl:b:remote: remote characteristics are holomorphic in (v,y), have
   y-order at least 3h-2 and are analytic at both endpoint values for
   compact real center intervals; no large-theta critical branch is assumed.
9. lmm:b:linear-endpoint, eq:b:linear-endpoint: for the scale-a input
   class the sole square-root term is the corresponding m=1 branch.
   Other branches have bounded first normalized derivative. The m>=2
   cubic difference stays intact with a summable m^-2 majorant;
   isolated infinite linear-subtraction terms are never summed.
10. lmm:b:quadratic-endpoint, eq:b:quadratic-input: endpoint corners
    cannot be reached simultaneously; first normalized derivative is
    bounded and second is at most inverse-square-root. There is no
    square-root endpoint term.
11. lmm:b:local-transport, eq:b:local-transport,
    eq:b:transport-endpoint-coefficient: local transport gains half a
    scale, with integer N>a+1/2. Its proof controls the frozen model,
    the intermediate range and the vanishing-order tail. Additive
    numerator bounds remain valid at zero coefficients.
12. prp:b:common-domains, eq:b:dented-disk, eq:b:common-bounds:
    actual fields have common dented regions for finite 1<=h<=H,
    small theta>=0 and -r_H<=x<R_theta, with joint complex-center
    neighborhoods and endpoint scale (h-1)/2. The conditional class,
    normal convergence and domain patching are verified inductively.
13. lmm:b:growing-disks, eq:b:modified-bounds, eq:b:growing-radius:
    negative-infinity radius c_h sqrt(u) I_0(2 sqrt(u)) and norm
    C_h I_0(2 sqrt(u))^(h-1), from an explicit relative-variation bound.
14. lmm:b:primitive, eq:b:primitive: G_{g,h}(0;0) is the negative-axis
    integral of L_{g,h} for g>=h>=1, g>=2. The geometric zero limit and
    fixed-genus absolute convergence are proved. G_{1,1} is excluded.
15. lmm:b:coefficient-bound, eq:b:coefficient-bound: two-endpoint
    O(N^-3/2) from first/second derivative bounds, with an elementary
    Fourier proof; this is a bound, not asymptotic transfer.
16. prp:b:primitive-bound, eq:b:primitive-bound: for fixed h>=1,
    g>=max(2,h), N=2g+h-2,
    |G_{g,h}(0;0)| <= C_h (2pi)^(-2g) N! R^(-N) N^(-5/2).
    All three negative-axis intervals are controlled uniformly in genus.

## Derivatives, sources and remaining work

The conditional endpoint class is defined on larger complex cones and
parameter neighborhoods. Its value remainder gives every fixed
Cauchy derivative on smaller cones. Thus the third derivative needed
by the next Euler/transport step is regenerated even when an application
records only two output orders. Only finitely many reductions are used
for fixed H. Constants can depend on that cap, nu, derivative orders,
angular margins and the stated compact parameter ranges, but not genus.
Regular-disk constants have their stronger scale-independent scope.
Normal convergence precedes coefficient extraction and integral exchanges.

The Bessel product/critical data and exact ILW identities come through
s06/s07. Primary DLMF (10.25.2), (10.32.3) supplies the modified-Bessel
series/integral; every inequality used is proved in B.5. The lecture
notes supply a route only. No new source entry, FO90 theorem, nefness
or positivity theorem is an input to this appendix.

Section 8 retains the actual P_h coefficients, their recurrence and
iterated-integral factorial, the Bessel transport constant, sine
inversion, asymptotic transfer with both dominant points and the
kappa/Hodge comparison. B gives their analytic domains and error
calculus; it does not claim Theorem 1.4.

No analytic gap is known in this author draft, subject to independent
review. Builds and formal review await the coordinator's shared refresh.
