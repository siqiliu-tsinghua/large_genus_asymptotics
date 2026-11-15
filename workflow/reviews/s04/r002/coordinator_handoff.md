# Section 4 supplementary coefficients: final handoff

USER-006 requested a short post-proof Remark giving two further coefficients,
with the printed calculation details omitted and the Introduction unchanged.
Both coefficients were independently reconstructed from exact recursion
inputs, signed moments and complete rooted-core sums before comparison with
the targets. Both exact differences are zero; the user's fourth coefficient
and the old note's third coefficient contain no detected transcription error.

The full reproducible calculation is preserved under
`sections/04_lambda_one/checks/`. Its driver was actually run to completion;
the subsequent `--verify-existing` checks validate the saved evidence without
rerunning the long reconstruction. The verification binds 24 source files,
the computed groups, both coefficient expressions and execution/output
fingerprints. The targets enter only after reconstruction, never as fitted
data. This was independent reconstruction, not a blind calculation after
the feedback had been read.

The manuscript adds only Remark 4.4 after the original proof. It states the
normalization explicitly and introduces no new coefficient symbols. The
Introduction, theorem statement, original proof, preceding numbered
equations and principal statements are unchanged. All 45 protected inputs
are byte-identical to r001; the original proof is an exact byte prefix of
the new proof file. Supplementary calculations are not inputs to that proof.

The original writer and all three original reviewers were reused. Each
reviewer issued a fresh r002 pass on snapshot
`49709716eb7727c33aef75f4e58308d545d5fab65362602733660224dd29abc1`,
with no unresolved issue. The actual acceptance command completed its
strict integrated build and set s04 to approved. No unit source changed
after freezing or acceptance.

The clean review PDF is `build/reviews/s04/r002/preview.pdf` (65 pages),
with Remark 4.4 on page 40. Its strict receipt has no standard or layout
diagnostics; the coordinator also inspected the rendered page. The default
`build/main.pdf` was then actually rebuilt in strict mode, with no standard
or overfull diagnostics. Final source/PDF fingerprints, fresh dependency
records, LF validation, `git diff --check` and ignored refs/build checks are
recorded in `coordinator_audit.json`.

No new commit was requested. The prior Section 3 commit remains `213c1ca`;
Section 4, Appendix A and their supporting records remain uncommitted.
