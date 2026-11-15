# s07 r001 mathematical review

Reviewer: `/root/s02_math`. Verdict: **pass**. Issues and resolved issue IDs are both empty.

Snapshot: `aea8b2ec4386f19480f32af79e5941ae9cfe92ff9176ce8f6c129c6e2237cb46`.
This is a full review of the new section, including its entry, four subsections, seven main statements, 35 numbered equations, interface and handoff.

## Integrity and inputs

All archived/live source hashes, the two special fingerprint entries, submission artifacts and canonical snapshot were checked. The actual source hash is `0727d8104128d0e0921b54da9d716b66fd5eb3aa496105e3adc827276f25acf8`; the actual clean PDF hash is `af05ec13c85935d49706cf02d23b3c99f8e37171d418fca72ee7931056d7dfd4`. The native entry/helper hashes match the receipt, which records strict success and empty strict/layout diagnostics. No build was rerun.

The real binding remains `/root/s02_math`. `Engine.assert_fresh`, `assert_dependencies`, and `python -B scripts/validate.py --unit s07` pass. The dependency closure is s01, accepted s02 r010 (`dcb33745...0f9d8bb9`) and accepted s06 r004 (`febf9e26...eaca560d`); no WP or Appendix A input is used.

I inspected Bur15 v4 PDF pp.1–2, including the actual p.2 image, and Bur16 v2 PDF pp.1–4, including its p.1 image and Section 2. Their positive Chern weights, ILW coefficient, sine transform and inverse coefficients agree with the manuscript. The s02/s06 interfaces supply the precise forgetting, lambda_g and beta conventions used here.

## Mathematical findings

- **7.1:** Reindexing gives `h=g-j` without substituting a value for epsilon. The lambda_g formula identifies the top sector with the inverse-sine transform of genus zero; the unstable and unmarked zero coefficients are consistent. The raw string anomaly is `z/24`; the sine correction on `x^2/2` cancels it. This is derived rather than inferred from a second derivative.
- **7.2:** The retained markings are labelled, and the additional markings have exactly the exponential-forgetting weight `psi(1-exp(-psi))` and factorial `1/m!`. Dimension bounds their number. The inverse map specializes to `w+theta*u`; the unmarked degree and factorial are `g_2+h`. No equality with the lambda_1 background is asserted prematurely.
- **7.3:** String and dilaton give the stated finite sum with `sum(d_i-1)=2g-3+h`; genus one is correctly separated as `-log(W_1)/24`. All differentiated positive-defect terms are rational finite jets with negative powers of `W_1` and a higher jet in the numerator. Consequently the highest-jet argument removes every possible x-integration constant, and the zero-higher-jet evaluation sets it to zero. Keeping v fixed sends `W_1` to `W_1+sigma` and preserves the higher jets, giving the actual noncritical inverse branch, decay and the positive infinite-end integral with derivative `-script D`. Lagrange inversion gives the normalized-log coefficient with the claimed factorial, including `L_1,1=-W_2/(24W_1^2)`.
- **7.4:** The normalization is `(2pi)^(2g)/(2g+h-2)!`. Subtracting the linear odd shift makes the Dirichlet sum summable; its Beta factor first gives `(N+1)!`, corrected by `1+y partial_y`. The two quadratic integrals give `1/N!` and preserve the external half for the ordered splitting. The genus bounds, minimum degree `3h-2`, parity and first-layer weight `1/m` are correct. Derivatives are taken before characteristic composition.

The analytic claims are appropriately limited: characteristic integrals are convergent at each fixed genus, and the first Borel layer is a locally normally convergent log sum. Higher Borel layers are coefficientwise; the body does not exchange an infinite genus sum with the characteristic integral or assert the Section 8 continuation, primitive constant, singularity estimates or coefficient asymptotics. Theorem 1.4 is not used as an input or claimed proved.

## Supplementary executed checks

`build/s07-preparation/math-r001/exact_guards.py` uses exact rational arithmetic. From Bur16 (2.2), it independently forms the one-point series `beta*log(beta)`, applies the sine transform and compares the result with Bernoulli coefficients through genus 8. It also inverts the exact Bessel series for low-degree log coefficients, checks 78 linear Beta factors, 169 quadratic factors including the half, and 1092 recursive index/degree instances. Every residual is zero; the genus-one specialized value is `1/24`. These checks support the body proofs and are not a replacement for them.

Script SHA256: `7ecbc3d7664e8d17e8f8f40199969ada32a5586de408f2a6c255d350ef0d7e99`. Exact output: `build/s07-preparation/math-r001/exact_guards.json`. Primary-page and clean-PDF images used in this review are in the same ignored directory.

Only this round's two mathematical reports and authorized private scratch were written. No source, state, historical report, other role's report or shared build output was modified. STOP; retain this reviewer session for any recheck.
