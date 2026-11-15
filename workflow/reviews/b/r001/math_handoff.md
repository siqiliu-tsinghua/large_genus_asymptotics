# Appendix B r001 full mathematical review

Reviewer: `/root/s02_math`. Verdict: **pass**. Issues/resolved IDs: `[]`.

Snapshot: `b6e1aa092e2ee935c285035e01288f27afe0c885ce9ef9092bb35e4f90a20aff`.
This is an independent review of the complete five-subsection implementation, all 16 statements with their adjacent proofs, all 35 numbered equations, the entry, interface, outline and handoff.

## Geometry and convergence

The angular estimates in B.1 give strict margins, including the perturbation above x_*. A positive center is essential: at the moving critical endpoint the real-part coefficient is `a_* w'''(x_{*,theta})-theta`, which is positive after choosing a_* and then shrinking theta. Closed-disk injectivity follows from the open-segment derivative integral. The full radius budget is proved separately, using the difference-quotient minimum for centers v>=a_*, the product-circle margin at zero, and affine comparison for intervening and slightly negative centers. Thus the proof does not infer a full image disk from univalence alone.

The exact two-distance identity gives the local scales `|S|+sigma sqrt(|S|)+sigma^2`; the positive-cone margin controls both endpoint distances. The full convex-image distance comparison also applies to interior complex centers and all sigma, without introducing a critical branch at large theta.

B.2 establishes actual normal Borel convergence before extracting coefficients. On a regular disk its full-sigma source is bounded by

`C_h s^(3h-2) (s+sigma)^(-2h)`,

whose integral is `C_h s^(h-1)/(2h-1)`. Finite covers and this remote majorant justify joint tube holomorphy, scalar sums, coefficient extraction and continuation across noncritical circle arcs.

## Endpoint calculus and the two potentially delicate patches

The m>=2 cubic shift difference remains intact in B.3, giving the summable m^-2 bound; the principal m=1 branch alone supplies the square-root coefficient. The other linear pieces have integrable first derivatives. In the quadratic integral, simultaneous singular corners are excluded, and the two-dimensional exponents -3/2 and -5/2 give the claimed first- and second-derivative bounds.

B.4 freezes `-S H_1/(2 sqrt(S-y+sigma d))`, with `d=x_{*,theta}-v_theta(x)`, so its lower endpoint has coefficient `S H_1/d`. The replacement errors are additive and remain valid when H_1 vanishes. The sigma=O(sqrt(|S|)) range, bounded scaled annulus and vanishing-order tail give the half-scale gain; `N>a+1/2` makes the last integral uniformly finite. Larger-domain value remainders regenerate fixed derivatives rather than consuming a finite stock of them.

The full actual-field induction is supported by two explicit portions of Proposition B.12:

- **Compact-center/critical-endpoint stitching:** `04_local_transport.tex:220-241` uses `S'=tau S+(1-tau)(S-y)`. For tau comparable to or below the normalized endpoint distance, the shifted center is in the established critical cone. Otherwise it is a relatively small perturbation of the real segment: small S' still uses the **lower-layer** critical cone, and S' bounded away from zero uses lower-layer compact neighborhoods. This covers the whole shifted segment, with no current-layer circularity; noncritical arcs and remote pieces complete the finite cover.
- **Complex theta:** the same proof's lines 243-250 explicitly use analytic Morse coordinates and critical derivatives close to positive real numbers, so the sigma sqrt(S) and sigma^2 terms retain their cone margin on a fixed small complex parameter neighborhood. Compact inverse patches and the positive-base remote bound persist there. Together with the finite successive parameter reductions at lines 206-216, this supplies the B.3 complex-parameter hypothesis and the theta Cauchy bounds, rather than establishing only real-theta estimates.

## Primitive and genus-uniform estimate

B.5 proves the fixed-genus zero limit from the finite jets on x=w(-u). Differentiated genus-one logarithms are harmless for g>=2; undifferentiated G_1,1 is correctly excluded. The modified-Bessel series and integer-order integral were checked directly against [DLMF (10.25.2)](https://dlmf.nist.gov/10.25.E2) and [DLMF (10.32.3)](https://dlmf.nist.gov/10.32.E3).

The elementary two-endpoint Fourier argument gives N^-3/2. Near zero, integration of `(R-x)^(-N)` adds N^-1. On a compact negative interval, the strict radius R_1>R gives an exponential advantage. At negative infinity, reserving h+2 radius powers leaves `u^(-(h+2)/2) I_0(2sqrt(u))^(-2)`, which is integrable; `N=2g+h-2>=h+2` holds for every stated genus. These three pieces give the absolute `(2pi)^(-2g) N! R^(-N) N^(-5/2)` estimate without positivity or an unjustified genus-integral interchange.

## Independent checks and provenance

The executed exact-rational script `build/s08-preparation/math-b-r001/exact_bounds.py` verifies the finite angular constants and regular/local/primitive exponents; its source SHA256 is `dd5f19b881a5736842a8d77be9c4e117ad63cf80334164e4f55c5161935a026f`. Output is saved beside it, together with the inspected PDF page renderings. The finite guards supplement the analytic proofs and are not numerical extrapolations.

All 45 archive/live fingerprint entries, artifacts and canonical snapshot/source match. Actual source SHA256: `7f82decb3898d10d166ef8c0d16e674e3360a0549095be7925db20f21b8dc2b4`. Actual 42-page PDF SHA256: `625520f822305c89dea820a12a12a3882b515e7bf0ecec87817d37fbe5d5c3c5`. Native entry/helper hashes match; strict/layout diagnostics are empty. The original binding, fresh accepted s02 r012/s06 r006/s07 r004 dependencies, Engine freshness gates and `python -B scripts/validate.py --unit b` were checked.

The six checks pass on this snapshot. Section 8's leading coefficient identification, asymptotic transfer and background comparison remain outside the appendix's claims. Only these reports and authorized private scratch/renderings were written; no source, state, old record, other report or frozen build output was changed or rebuilt. STOP and retain this reviewer context.
