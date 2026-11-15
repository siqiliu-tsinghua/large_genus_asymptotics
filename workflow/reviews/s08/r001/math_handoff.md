# s08 r001 mathematical handoff

Reviewer: `/root/s02_math`. Verdict: **changes_requested**.
Snapshot: `376e26aba67c4b70f8ca635464c6b17beb4fd20806344c41da8fde23c9c8a9cd`.
This is a full review of the frozen Section 8 implementation, not a signature
inherited from source preparation or Appendix B. There are no earlier s08
MATH issues; `resolved_issue_ids=[]`.

## MATH-001: initial shifted segment in Proposition 8.8

Location: `sections/08_fixed_defect/04_coefficient_transfer.tex:100-104`,
native PDF p.32. The issue is a local proof gap in the asserted complex
domain, not evidence that the intended asymptotic constant is wrong.

For clarity in this handoff, write `t=S-y` for the endpoint distance.
The principal branch has shifted center `s=x+y-u`, distance `S'=t+u`
and normalized Borel argument `u/(t+u)`. The claim that this argument
stays in a compact subregion of the inverse disk on the initial segment
is false. For any allowed `gamma_H<pi/4`, choose
`3pi/4<phi<pi-gamma_H`, put `t=epsilon exp(i phi)`, `y=S-t`, and
`u=tau y`, where `tau=-epsilon cos(phi)/S`. This is a point of the
integration segment with `|u|=O(|t|)`, while

`|u/(t+u)| -> |cot(phi)| > 1`.

The original dented-domain conditions hold for small epsilon. Thus a
real-axis inverse-disk argument cannot justify the complex coefficient
transfer. The private exact rational example uses `S=1`,
`t=10^-4(-4/5+3i/5)` and `tau=1/12500`; its squared normalized modulus
is `100016001/56241001>1`, within `|u|<2|t|`.

The needed repair is already supported by the approved B r002. Apply
Lemma B.4's kernel-shift preservation and Proposition B.12's
near-critical-cone extension and final patching paragraph. For the
initial `|u|<=C|t|` segment, verify the fixed angular margins and

`|S'| asymp |t|`, `S'-u=t`, `|S'+u|=|t+2u| asymp |t|`.

Both normalized endpoint distances then stay bounded away from zero
on a strictly smaller critical cone, although the normalized argument
may be outside the unit disk. Formula (B.28), with total derivative
order one, gives

`|partial_s L_h(theta;s,u)| <= C |t|^((h-1)/2-1)`.

Multiplication by the `O(|t|)` path length yields the claimed
`O(|t|^((h-1)/2))`, bounded for all `h>=1`. If higher fixed mixed
derivatives are invoked, their corresponding exponent is
`(h-1)/2-a-k`. State the actual domain and scale before proceeding to
the remaining segment. Retain the complex neighborhood and additive
error of Proposition 8.8. A name distinct from the inherited descendant
`t_0` would also remove the notation collision in this passage.

## Complete mathematical review retained for recheck

- Read all six subsections, entry, outline, interface and writer handoff,
  together with the necessary s02/s06/s07 and B r002 proofs. The critical
  inverse and theta branch, logarithmic seed, positive principal linear
  branch and lower characteristic endpoint give the stated recurrence
  for the actual `P_h`. The quadratic term has no square-root coefficient;
  its two endpoint corners cannot coincide. The order `3h-2` is sufficient
  for the local characteristic integral. The ordered recurrence gives
  `P_h=B^(h-1)/((h-1)!(x_*-v_0))` and `integral P_h=B(0)^h/h!`.
- Independently checked the harmonic-number integral and Bessel
  Wronskian signs. They give `B(0)=1/(z_{0,1}J_1(z_{0,1}))=1/(2R)`.
  The inverse-sine kernel has alternating outer weight, a plus between
  shifts, the correct two-shift factor and Beta factorial. The two
  endpoint contributions add at the actual parity `D=g_2+h`; neither
  may be discarded. The untransformed primitive is smaller by `O(1/g)`.
- Apart from MATH-001, checked the recovered-singularity path estimates,
  including the full path rather than a fixed-center substitution,
  the remote negative-center patches, and the integrable remaining
  error with exponent `(h-1)/2-nu>-1`. The two-indent coefficient proof
  gives an additive `O(N^-nu)` uniformly even for zero amplitudes.
  Fixed markings use genus-scaled Cauchy radii. The genus-one logarithm
  is excluded from the large-genus primitive argument and handled among
  the finite stable cases; h=0 uses the exact s06 top-Hodge input.
- The exact boundary decomposition has `1/2` for ordered branches and
  ordered component pairs. Its nonseparating term loses one factorial
  degree. For every separating genus and allowed component defect,
  `a+c=D-1`, and the normalized product is bounded by
  `C_h/(D binom(D-1,a))`. Summing the full inverse-binomial sequence
  proves the entire genus convolution, not just each fixed split.
- Checked full Hodge-bundle nefness on boundary curves by finite graph
  labeling and partial normalization, determinant nefness, the ample
  criterion for `kappa_1=12 lambda_1-delta`, and the positive-degree
  smooth projective cover. On the quotient bundle, Mumford's relation
  gives `p_*xi^(g-1+j)=lambda_j`. All mixed intersection degrees match.
  Ample approximation upstairs and Hodge index on the resulting surface
  give log concavity. Monotonicity from the effective boundary and the
  first increment squeeze the whole polynomial through `C_D/C_0`, not
  just the single boundary term. No generically finite pullback is
  incorrectly assumed ample.
- In the final proof both factorial ratios are retained. Their limits,
  `B(0)=1/(2R)`, `rho=12R` and `g_2/g->2` give the constant `24`.
  The conclusion is asymptotic equivalence; the transfer error does not
  supply a relative `O(1/g)` theorem. The proof does not use Theorem 1.4
  as an input, nor any WP result from Sections 3--5 or Appendix A.

## Primary inputs and executed checks

Directly checked the local primary PDFs for Fuj78 Main Theorem (0.6),
printed pp.779-780; Kaw81 Theorem 5, printed p.254; CH88 Theorem (1.3),
printed pp.457-458; LX26b Proposition 4.4 and its boundary proof, and
Proposition 6.1 at m=0. Fujita's curve statement and Kawamata's
normal-crossing/unipotent hypotheses are used with the stated reduction
and descent; the full ample-cone assertion is distinguished from CH88's
weaker outside-boundary slope assertion. Viewed FO90 printed p.4 and
checked the manuscript's own two-point specialization of its Section 2
contour method. The exact Bessel formulas were checked on the official
[DLMF 10.8.2](https://dlmf.nist.gov/10.8.E2) and
[DLMF 10.5.2](https://dlmf.nist.gov/10.5.E2) pages.

Executed `python -B build/s08-preparation/math-s08-r001/exact_guards.py`.
It passes eight inverse-sine/Bernoulli comparisons, 180 kernel
degree/factorial/parity cases, 52 projective-dimension cases, the
genus-two stack check and final normalization. The resulting JSON also
records the exact complex counterexample above. These finite guards
supplement, and do not replace, the uniform analytic arguments.
`python -B scripts/validate.py --unit s08` passes.

## Frozen identity and permissions

All 54 fingerprint entries, archived/live bytes, artifact hashes,
canonical snapshot and actual role binding were independently checked.
The accepted dependencies s02 r012, s06 r006, s07 r004 and B r002 are
fresh. The actual 53-page native PDF was inspected at the issue page.

- Source SHA256: `d85268f907c49a3f7f8da0b2df68407a2a7da826fddf4493524d7533bd4b2a7f`.
- PDF SHA256: `916aeb78405e3889fe64227bc9c3046509ae465a334f7c44316d3153fa6b3ba5`.
- Entry SHA256: `57af60d7779769461349c8232cb82bad5492665599f5c1efc0e72a3e4afebe4c`.
- Helper SHA256: `83e54aba6b9d59878fefe7c120f9385cfefa2fdc21f5347dacdcbb387bb052db`.

The receipt binds this snapshot, records a strict successful native
10pt build without showkeys, and has empty standard/layout diagnostics.
No manuscript/shared/state/old record/other-role report or frozen build
output was edited. Only this round's two mathematical reports and the
authorized private scratch directory were written. Stop pending the
coordinator's collection of all reports and the original author's revision.
