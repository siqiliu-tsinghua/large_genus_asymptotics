# s02 writer handoff — trial of 2.1 and 2.2

Status: drafting / incomplete. This handoff covers the authorized trial only, now revised in response to USER-001 after trial round 1. It is not a formal submission of the whole section and does not authorize acceptance. Original writer session must be retained for revision and for eventual completion of 2.3–2.4.

## Files written

- `01_conventions.tex`: rational stack intersection convention; complex codimension; new degree-zero and out-of-rank Chern-class conventions; graded exponentials; exponential-to-power lemma and proof; exact `A_g` / `B_g(h)` factorial restoration; fixed-parameter/error conventions. The opening no longer reintroduces the inherited basic setup or inventories existing symbols.
- `02_tautological_classes.tex`: psi before logarithmic kappa; factorial-normalized Chern characters and Chern polynomial; total reduced boundary, chosen node and ordered branches; distinct-font Bernoulli numbers; fully normalized marked Mumford formula; nonlogarithmic conversion with a short section-intersection argument; divisor specialization; root-based exponential rewrite and lambda-two/lambda-three examples with proof.
- `INTERFACE.md`: exact assumptions, scopes and reasons for notation, result labels, verified primary locators, and explicit unfinished parts.
- `writer_handoff.md`: this record.
- `workflow/trials/s02-01-02/r001/author_response.json`: separate response to USER-001, with no open reviewer-issue responses and no alteration of the original pass reports.

No changes were made to `section.tex`, 2.3, 2.4, the preamble, bibliography, other sections or workflow state.

## USER-001 revision

The updated writer/readability responsibilities and shared notation policy treat the paper as a continuous text. The earlier opening wrongly repeated the Introduction's basic setup; correctness of those repetitions did not justify them.

- Removed the paragraph reintroducing `g,n`, stability, the moduli stack and its base. The opening now starts with the genuinely new rational Chow, complex-codimension and stack-integration conventions.
- Removed the inventory of the Hodge bundle, Hodge indices, normalizations and `g_2`, along with the needless pointer to Theorem 1.3. Their full inherited ledger remains in `INTERFACE.md` for collaborators.
- Retained the new conventions `lambda_0=1` and vanishing above rank, the homogeneous conversion lemma, its precise local bounds, the factorial examples and the fixed-parameter/error table.
- Shortened the 2.2 opening to identify `pi=pi_{n+1,n}` with the universal stable curve. It introduces sections and the dualizing sheaf in their needed roles without retelling the already defined forgetting operation.
- Removed the routine Introduction reference before the factorial example and the redundant prose labeling the root and Chern-class dummy indices. The psi/kappa/character definitions, boundary normalization, literature conversion and proofs remain intact.

No mathematical identity or hypothesis was changed. The shared responsibility files were read but not edited by the writer. The original three reports are unchanged; all three original reviewers must sign the new snapshot.

## Mathematical decisions

1. All integrals are stack degrees. The ordered-node cover records both branch orientations, giving `delta=(1/2)xi_*1`; this is also the normalization of the GRR boundary term.
2. `kappa_a=pi_*(psi_new^(a+1))` is logarithmic. FP00 §1.1 uses the nonlogarithmic dualizing power. The local comparison is proved by identifying the universal curve with the forgetful source, writing the new cotangent class as the logarithmic dualizing class, and using disjoint sections with normal bundle `L_i^vee`. The contribution of each marking is the alternating binomial sum equal to `psi_i^a`. This supplies the negative marking term in the stated GRR formula.
3. `ch_a` includes `1/a!`. The coefficient in `log c_t` is consequently `(-1)^(a-1)(a-1)! ch_a`. Even characters vanish; odd coefficients are positive after the sign specializes to odd `a`.
4. `12lambda_1=kappa_1+delta-sum_i psi_i` follows from `mathsf B_2=1/6` and the half-boundary normalization. The unmarked specialization is explicitly restricted to `g>=2`.
5. Exponential-to-power conversions are exact finite-genus degree selections. They do not provide any uniform asymptotic estimate or interchange of graph sums.
6. `g_2`, the `j`-family Hodge indices and `ell` are retained. The WP scale is deferred, and there is no extra dimension abbreviation. Bernoulli numbers are `\mathsf B_m` to avoid collision with the Introduction's italic integral `B_g`. One local map `pi`, explicitly identified with the inherited `pi_{n+1,n}`, serves as both forgetting map and universal stable curve; no second family-map alias is introduced.

## Literature checks

The coordinator verified and communicated the precise locators; the writer also opened and checked the primary author PDFs.

- Mumford (1983), §5, (5.2) and Corollary (5.3); primary PDF pages 34 and 36. Its original Bernoulli convention and kappa-index typo are resolved through the corrected FP00 presentation.
- Faber–Pandharipande (2000), §1.1, unnumbered Theorem (Mumford), author PDF page 6 / journal page 178. This is the intended primary clean-family statement; Proposition 1 is the stable-map virtual generalization and is not used as the locator.
- FP00 §1.3, (16), author PDF page 11 / journal page 183, for the marking correction under the forgetful convention.
- Bibliography keys `Mum83` and `FP00` were added by the coordinator. No shared bibliography change remains requested for this trial.

## Suggested section roadmap for the coordinator

When authorized to fill `section.tex`, a short roadmap could say:

> We fix the grading and factorial normalizations, then recall Mumford's formula in the logarithmic kappa convention. These identities express Hodge insertions through odd Chern characters and the boundary. We next describe their behavior under normalization at nodes and give the boundary and forgetting formulas used in the later graph expansions.

The last sentence concerns unwritten 2.3–2.4 and is a proposal, not manuscript content or a completed claim.

## Validation and next action

Author checks: all new mathematical notation has an adjacent definition and an interface entry; sums have explicit ranges; the GRR coefficient at `a=1` agrees with the stated divisor identity; Chern-log expansion gives coefficients `1/2` and `2` in the two examples. `git diff --check -- sections/02_notation` passed. A read-only Python check verified UTF-8, LF and final newline for all four authored files, unique trial labels and balanced theorem/proof/equation/tabular environments.

The revised trial must be built with `python workflow/trials/s02-01-02/build_preview.py`, then frozen by the coordinator for all three original reviewers to recheck. The section's remaining TODO markers deliberately prevent representing the whole unit as complete. The writer will stop editing after recording the new build result and await the coordinator's next instruction.
