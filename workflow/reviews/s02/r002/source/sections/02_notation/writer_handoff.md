# s02 writer handoff - formal r001 layout revision

Status: **revised complete draft, awaiting formal r002 recheck**. Fixed writer: `/root/s02_writer`. Formal r001 math and academic reports passed; readability requested two local layout repairs. Both are addressed in the original writer session. No old report is edited, and no r001 signature is treated as a signature of r002. No acceptance or proof of an asymptotic target is claimed.

## Complete-draft work and files

This extension writes only:

- `sections/02_notation/03_gluing.tex`;
- `sections/02_notation/04_boundary_and_forgetting.tex`;
- `sections/02_notation/section.tex`;
- `sections/02_notation/INTERFACE.md`;
- `sections/02_notation/writer_handoff.md`.

The Introduction and 2.1--2.2 stay unchanged from the committed trial batch. Shared bibliography entries and primary copies were supplied by the coordinator; the writer did not edit shared files, workflow state, historical responses/reports, or any later chapter. The complete section is ready for the next frozen snapshot after the coordinator's checks.

## Formal r001 revision

The collected formal reports are under `workflow/reviews/s02/r001/`. The author response is `workflow/reviews/s02/r001/author_response.json`, using the generated template and both stable issue IDs.

- READABILITY-001: the boundary-exponential identity now places its left side and graph-sum right side on separate aligned lines. Its font size, single label, factors, graph weights and hypotheses are unchanged.
- READABILITY-002: the KMZ version locator is a short separate sentence with a local break opportunity after its slash; attribution and notation translation are separate paragraphs. The complete checked version, theorem/formula locators, source translation and attribution are retained.
- Adjacent cleanup: short local rephrasing of the gluing transition, rational-tail degree paragraph and final application paragraph removes the three small additional overfull lines, without changing their mathematical content or proof steps.

This revision changes only `03_gluing.tex`, `04_boundary_and_forgetting.tex`, this handoff, the designated author response and the coordinator-requested interface status metadata. The interface's scientific ledger and exports, section roadmap, all other manuscript files and all earlier records remain unchanged. Interface metadata now identifies an author submission and defers live review/acceptance status to `workflow/state.json`. No literature was reopened and no new source is introduced. The coordinator separately synchronized actual statement numbers and the already-stated tail/cutoff distinctions in the shared outline before the final checks.

## Mathematical organization

The roadmap now connects factorial restoration, GRR, normalization at nodes, graph exponentials and forgetting. The new material is split into reusable units:

1. Stable graphs are defined by vertices, flags, an involution, labelled legs and stable vertex genera. The labelled product and gluing map precede every graph formula; automorphisms preserve every leg label.
2. The Hodge-normalization lemma has quotient `H_1(Gamma;C) tensor O`. The cycle space is defined before the statement as the incidence-map kernel. Partial normalization, prescribed residues and relative duality give a bundle sequence over the full labelled product, including deeper degenerations of the vertex curves.
3. The quotient is constant on that product; it is not asserted equivariantly trivial. A loop reversal changes residue sign. Chern factorization then proves the full defect allocation with integers `0<=h<=g`, `0<=h_v<=g_v`, `sum h_v=h-b_1`. For `h=0`, only trees survive.
4. Logarithmic kappa is additive under gluing because each normalized branch becomes a marking of its vertex factor. Leg cotangent lines are preserved.
5. The boundary proposition is the constant-edge, linear-kappa specialization of Andersen et al. Its kernel is a divisible formal series, not an inverse cotangent class. The normal-line self-intersection gives the sign, and labelled multiplicities give `1/Aut`. The `(1,1)` self-loop has weight `1/2`; a `(0,4)` separating edge with a fixed labelled split has weight one. The unmarked equal-genus separating exchange is also explained.
6. The one-point logarithmic-kappa comparison is proved algebraically. On the universal source curve, stabilization identifies the old log-dualizing line with the line with only old markings; the new log line adds the new section. Its self-intersection and the alternating binomial sum give the extra `psi_new^a`; projection/flat base change supplies the pulled-back base term. This is a distinct comparison from the nonlogarithmic marking conversion in 2.2.
7. The rational-tail lemma requires a positive psi power at EVERY forgotten marking. A tail with `k` new points has dimension `k-1` when it contains one old point and `k-2` when it contains none. The new factors have degree at least `k`, annihilating the comparison-divisor ideal. The old psi corrections disappear, while `pi_m^*kappa_1` becomes `kappa_1-sum_new psi`, retaining the latter sum. Arbitrary polynomials and graded-truncated series in the stated old classes inherit these replacements.
8. KMZ's forward permutation sum has cycle factors `(block size-1)!`. Its inverse unordered partition coefficient is just `(-1)^(m-number of blocks)`. The proof uses the one-point algebraic comparisons and a signed exponential-series inversion. The two-kappa example explicitly retains the negative merged-block term.
9. The exponential specialization is derived by counting labelled block sizes. For `m` blocks of sizes `r_i>=1`, the coefficient is `1/m! prod_i((-1)^(r_i-1) s^(r_i)/r_i!)`, yielding one factor `psi(1-exp(-s psi))` at each new marking. The minimum degree after forgetting is `m`, so only `m<=3g-3+n` can contribute at fixed genus.

No local tool is presented as a uniform asymptotic estimate. In particular, neither a per-graph identity nor degree truncation justifies exchanging a growing graph/marking sum with a genus limit; later sections must supply that control.

## Checked primary sources and shared requests

No further bibliography or source request remains outstanding.

- `FP00` Section 1.3 (17)--(18), already in the trial bibliography: one-node Hodge sequences.
- `LX26b` arXiv:2610.39462v1, proof of Proposition 4.4 (4.2)--(4.3): partial normalization and the cycle-space quotient. No positivity input is imported here.
- `ABCDGLW23` arXiv:1905.10352v3, Section 3.6, weighted one-edge `jmath` before Proposition 3.9 and Lemma 3.10 (3.18)--(3.22): edge-exponential/graph identity. Primary HTML was checked by the writer; the coordinator also supplied the primary PDF and journal metadata. Set their edge series equal to constant `a` and their vertex series to linear coefficient `c`.
- `KMZ96` alg-geom/9604001v1, Section 2, (2.4), Theorem 2.2 (2.6), Lemma 2.2.1 (2.8), Lemma 2.2.2 (2.13), and geometric formulas (2.9)--(2.11): forward cycles and inverse partitions. Their cohomological `omega_n(a)` is the logarithmic `kappa_a` here, with degree `2a` converted to complex codimension `a`. Their credit to Arbarello-Cornalba and earlier unpublished Faber-Zagier is retained.

The ABCDGLW and KMZ primary statements are in cohomology. The manuscript does not infer Chow equalities from equality of cycle classes: it supplies the same algebraic normal-bundle/push-pull argument, with the local kappa comparison proved via universal curves. Existing Mumford/FP00 GRR attribution and normalization are unchanged.

## Canonical notation and historical continuity

The user-revised lowercase families `a_g,b_g(h),b_g`, ordinary Bernoulli `B_m`, and `A^a(X;Q)` coefficient format remain in force. Scalar `b` and later `beta_g` are separate. New flag labels are `f,f'`; `h` stays the Hodge defect and `ell` stays the Hodge-product length. No aliases for `g_2`, the Bessel zero, or `3g-3` are introduced; `alpha` remains deferred until WP formulas.

Historical scope and feedback are preserved under `workflow/trials/s02-01-02/`:

- USER-001 established continuous-paper inheritance of definitions.
- USER-002 placed global intersection/degree conventions at first introductory use and clarified stable forgetting targets and normalization domains.
- ACADEMIC-001 corrected only theorem-final punctuation.
- USER-003 established the current notation, Chow formatting and concise 2.2 transition.

Those scoped passes are not substituted for a full-section review. The same writer and reviewers must review the whole new snapshot and any later revision.

## Validation and handoff

Author checks passed:

- `python scripts/build.py --unit s02 --with-deps --strict`: XeLaTeX, BibTeX and final reruns succeeded with no diagnostics.
- `python scripts/validate.py`: repository validation passed.
- `git diff --check -- sections/02_notation`: no whitespace errors.
- Read-only source checks confirmed that the Introduction and 2.1--2.2 are unchanged from the committed batch; all section files use UTF-8, LF and final newlines; labels are unique, environments balanced, citation keys present and notation canonical. The adjusted display retains the same mathematical payload after removing alignment whitespace.
- A separate clean rendering disables showkeys locally in its preview entry. Its final log is required to have no overfull horizontal or vertical boxes; the native strict builder's warning check alone does not establish this. Draft artifacts stay under `build/reviews/s02/writer-r002-draft/`; the frozen r001 artifacts are untouched.

The native and clean draft receipts are regenerated after saving this handoff and the response, so their source hash records the current files and synchronized outline. The clean artifact is a writer draft with the prior snapshot recorded only as its base; it is not an r002 review signature. The coordinator will independently verify and freeze r002. Source checks and compilation do not replace mathematical review.

No known source or mathematical gap is intentionally left unresolved. The coordinator should freeze the full s02 snapshot only after its checks, then dispatch all three original reviewers. The writer stops editing at handoff until the collected reviews are returned.
