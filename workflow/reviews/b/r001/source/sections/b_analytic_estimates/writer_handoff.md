# Appendix B original-writer handoff

Writer: /root/s02_writer.
Stage: complete mathematical first draft, not frozen or reviewed.
The coordinator will settle the Section 8 sources and refresh accepted
dependencies before returning to B. Live status is in workflow/state.json.

Only sections/b_analytic_estimates/ was edited: section.tex,
01_inverse_domains.tex, 02_regular_transport.tex, 03_endpoint_bounds.tex,
04_local_transport.tex, 05_negative_primitives.tex, INTERFACE.md and this
handoff. The coordinator has updated the five-subsection unit definition.
There are 16 principal statements with adjacent prf proofs and 35 numbered
equations. The unused legacy content.tex wrapper was removed; section.tex
directly inputs the five files, as required by the unit validator. No old
unit, shared file, state or historical record was edited.

## Proof rationale

- B.1 proves univalence and the full image-radius budget separately.
  A fixed positive center a_* repairs the theta>0 degeneration through
  the local coefficient a_*w'''(x_{*,theta})-theta. Compactness covers
  the remainder. The separate radius proof uses the difference-quotient
  angular minimum, the product margin at x=0 and an affine-distance
  argument. The same argument allows a small negative interval.
- The angular proof uses the simplified polynomial minimum 937/2880
  and explicit tail <0.049. The old even-text escape fragment is fixed;
  every current source is LF and free of abnormal control characters.
  Negative-center inverse disks have radius >R by termwise angular
  comparison and real-axis monotonicity.
- B.2 constructs actual Borel functions by normal convergence. Regular
  norms grow as derivative scale^(h-1), while the exact minimum degree
  3h-2 gives an integrable full-sigma source majorant. Tube holomorphy,
  noncritical-circle continuation and remote bounds follow by induction.
  No large-theta critical branch or assumed analytic Borel sum is used.
- B.3 specifies its conditional class on larger cones, with analytic
  endpoint coefficients, scale norms and a fixed 1/2<nu<1 value remainder.
  The m>=2 cubic difference is kept intact to avoid divergent separate
  linear sums. Quadratic singular corners cannot occur simultaneously.
- B.4 proves the local half-scale gain, controls additive frozen-model
  errors even at zero coefficients, and estimates the bounded scaled
  annulus, vanishing-order tail and regular remote part. It does not
  assume monotonicity of |S_sigma| for complex centers. The actual fields
  satisfy the class inductively: critical cones, compact center patches,
  noncritical arcs and remote parameters are all covered. Larger-angle
  value estimates regenerate any fixed derivative order, including
  the third order needed for the next layer.
- B.5 fixes the primitive at negative infinity from the finite jets.
  G_{1,1} is excluded because its undifferentiated logarithm diverges.
  For g>=max(2,h), the near-zero integral gains N^-1 on top of the
  two-endpoint N^-3/2 bound. Compact negative intervals use radius >R.
  At infinity the radius is c_h sqrt(u) I_0(2 sqrt(u)); reserving h+2
  powers makes the remaining integral finite since N=2g+h-2>=h+2.

## Main arguments retained for Section 8

The appendix uses generic endpoint coefficients. Section 8 should
identify them with the actual P_h, explain how the positive m=1 branch
and the lower end of the characteristic determine their recurrence,
and derive the iterated-integral 1/h! and the Bessel constant. It also
retains sine inversion, asymptotic transfer from both dominant points,
marked bounds and the kappa/Hodge comparison. B supplies the common
analytic domains and uniform error calculus; it does not claim that
Theorem 1.4 has been proved.

## Sources and validation

Inputs are the accepted s06/s07 results and DLMF. Primary equations
10.25.2 and 10.32.3 were read directly. No new macro, package or source
entry is needed for B. The coordinator's four Section 8 sources are a
separate shared settlement. Internal notes and arithmetic caches are
leads/checks; the finite inequalities and analytic majorants are proved
in the body, and no result here depends on running a calculation script.

Static checks cover UTF-8/LF/final newline and control characters,
assembly, labels/citations, balanced TeX and proof adjacency. Actual
outcomes are reported with the handoff. No native build or mathematical
recomputation was run while the shared refresh is being prepared.
The coordinator will build/freeze one snapshot for the original three
reviewers. No review pass is claimed by this author.

STOP after static checks; retain the original context for the restored
build and formal review revisions.

## Recovery after S08-SHARED

The shared-source refresh is complete and B has been restored to drafting
with the original writer. I read
workflow/feedback/shared/S08-SHARED_final_audit.json, SHA-256
aefd102897d2f62f7ac5326bf2d7588a7acde1cd8130a66d91c8bcdc88ca0968.
Before appending this note, comparison of the full 45-input saved B map
showed only references.bib changed. All five mathematical subsections,
the entry and interface retain their paused bytes.

Engine.assert_dependencies('b') passed with the actual accepted s06 r006
and s07 r004 approvals. The draft is ready for the coordinator's native
preflight; this writer ran no build or new mathematical computation.
Only this recovery note was appended. STOP pending actual TeX/layout
feedback and the original three reviewers' full Appendix B review.

## Pre-freeze notation and navigation cleanup

The geometric enlargement in B.4 is now r, with the common threshold
r_H; its original positive scope and both domain/interval uses are
preserved. The negative-axis proof in B.5 uses the local positive r_0
and the corresponding parameter u_{r_0}, defined by w(-u_{r_0})=-r_0.
This preserves Section 7's formal Hodge epsilon. B.3 now explicitly
points to Proposition prp:b:common-domains instead of 'the last
proposition'. The interface records all local radius scopes.

Only these naming/navigation changes were made in the mathematical
sources. The 35 equation labels and 16 statements/proofs are retained;
reversible notation translation restores the previous equations exactly.
Static/control-character checks are reported at handoff. The coordinator
will rebuild the actual new source before freezing. STOP.
