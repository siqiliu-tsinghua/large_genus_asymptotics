# Two higher-asymptotic Remarks: completed handoff

Completed 2026-11-16 by the coordinator, using the retained original
writer and the original math/readability/academic reviewers. This is
a completion record, not a substitute for their actual signed reports.

- Remark 6.3, main PDF p46, follows the complete Theorem 1.3 proof.
  It reports the relative g_2^-2 and g_2^-3 coefficients and explicitly
  omits the derivation. The self-contained Section 6 checks bundle
  reconstructs all seven contributing tree classes and both exact
  compact comparisons give zero. The original theorem is unchanged.
- Remark 8.2, p65, follows the complete Theorem 1.4 proof and ends the
  main body. It states the h=1 refinement as a conjecture, gives three
  transparent residual/consecutive-genus extrapolation observations,
  and ends with the open problem of proving the refinement and finding
  further terms for general fixed h. It asserts no new remainder rate.
- The 19 exact pairs for genera 2--20 are archived in the Section 8
  checks bundle, with source-file hashes and LiuData26 commit
  88dd4a501ecf3fbc124a823ad1589911f86a14e5. Independent extractions
  agree on all 38 rationals. The candidate is 0.207760231708341177...;
  the g=20 adjacent extrapolation is 0.205669656082.... Finite evidence
  supports the conjecture without proving it or validating the entire
  external dataset. The supplied external repository remained read-only.

Both new small programs were actually run by the author and coordinator,
and independently checked by the original reviewers. Their tracked
verification records distinguish calculation from mathematical proof
and formal review. Existing long A/S4 calculations were not rerun.

The actual sequential refresh and original-role reviews accepted all
eleven units: s01 r003, s02 r014, s03 r011, a r011, s04 r013,
s05 r010, s06 r008, s07 r006, b r004, s08 r004 and c r002.
All are fresh, all three registered reviews pass for every snapshot,
and no unit remains active. Historical archives and signed renderings
were preserved. The new substantive reports are under s06/r008 and
s08/r004; c/r002 also covers the actual full-manuscript companion.

The default build/main.pdf is 101 pages, SHA256
03164d5993efc876375a1a2ecfd177dbfca4630b9c11dea61a913fee248e869e.
Its extracted text exactly equals the full manuscript actually reviewed
at build/reviews/c/r002/full-manuscript/manuscript.pdf.

Actual final checks: strict XeLaTeX/BibTeX build, global validation
(5526 text files, 11 sections, 437 labels), git diff --check, and
build/remarks-20261115/final_audit.py. The audit preserves 111 prior
inputs, the user's complete Introduction, all four theorem blocks,
both original proof-file byte prefixes and all 435 old label numbers.
Only the two new Remark labels are added.

There is one explicitly retained layout exception: the LiuData26 URL
extends 3.50723pt (about 1.2 mm) beyond the right text edge. The original
readability and academic reviewers independently inspected the actual
renderings and accepted it as non-blocking: all characters and
punctuation remain visible, without clipping or overlap. The raw
diagnostic and specific exception are retained in the native receipts,
formal reports and final audit; no claim of zero overfull boxes is made.
The strict build has no LaTeX/citation diagnostics.

Current source of truth: workflow/state.json and the registered reports.
Detailed working evidence: build/remarks-20261115/final_audit.json,
the per-round summaries, and each section's new higher_remark_handoff.md.
