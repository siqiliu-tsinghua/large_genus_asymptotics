# s02 writer handoff — trial of 2.1 and 2.2

Status: drafting / incomplete. This handoff covers the authorized trial, now coordinated with a limited Introduction revision for USER-002 after trial round 2. It is not a formal submission of either whole section and does not authorize acceptance. Original writer session must be retained for revision and for eventual completion of 2.3–2.4.

## Files written

- `sections/01_introduction/section.tex`: limited USER-002 clarification and relocation of global conventions at first use; stable-forgetting dimension argument; normalization ranges; definition order and grammar; planned-organization paragraph. The four main target displays remain verbatim.
- `sections/01_introduction/INTERFACE.md`: records this limited baseline revision, global first-definition locations and unchanged theorem targets.
- `01_conventions.tex`: now starts with formal exponentials, followed by the exponential-to-power lemma and proof, exact `A_g` / `B_g(h)` factorial restoration, and fixed-parameter/error conventions. The global Chow/degree/integration/rank conventions have moved to the Introduction and are inherited directly.
- `02_tautological_classes.tex`: psi before logarithmic kappa; factorial-normalized Chern characters and Chern polynomial; total reduced boundary, chosen node and ordered branches; distinct-font Bernoulli numbers; fully normalized marked Mumford formula; nonlogarithmic conversion with a short section-intersection argument; divisor specialization; root-based exponential rewrite and lambda-two/lambda-three examples with proof.
- `INTERFACE.md`: exact assumptions, scopes and reasons for notation, result labels, verified primary locators, and explicit unfinished parts.
- `writer_handoff.md`: this record.
- `workflow/trials/s02-01-02/r001/author_response.json`: separate response to USER-001, with no open reviewer-issue responses and no alteration of the original pass reports.
- `workflow/trials/s02-01-02/r002/author_response.json`: separate response to USER-002; the r001 response and all previous reports remain unchanged.

For USER-002, the only chapter edits are the authorized Introduction files and the assigned 2.1/interface/handoff files. Subsection 2.2 is unchanged from r002. No changes were made to the section-2 roadmap, 2.3, 2.4, the preamble, bibliography, abstract, other chapters or workflow state.

## USER-001 revision history

The updated writer/readability responsibilities and shared notation policy treat the paper as a continuous text. The earlier opening wrongly repeated the Introduction's basic setup; correctness of those repetitions did not justify them.

- Removed the paragraph reintroducing `g,n`, stability, the moduli stack and its base. The opening now starts with the genuinely new rational Chow, complex-codimension and stack-integration conventions.
- Removed the inventory of the Hodge bundle, Hodge indices, normalizations and `g_2`, along with the needless pointer to Theorem 1.3. Their full inherited ledger remains in `INTERFACE.md` for collaborators.
- Retained the new conventions `lambda_0=1` and vanishing above rank, the homogeneous conversion lemma, its precise local bounds, the factorial examples and the fixed-parameter/error table.
- Shortened the 2.2 opening to identify `pi=pi_{n+1,n}` with the universal stable curve. It introduces sections and the dualizing sheaf in their needed roles without retelling the already defined forgetting operation.
- Removed the routine Introduction reference before the factorial example and the redundant prose labeling the root and Chern-class dummy indices. The psi/kappa/character definitions, boundary normalization, literature conversion and proofs remain intact.

No mathematical identity or hypothesis was changed in that revision. Its placement of the new global conventions at the start of 2.1 is superseded by USER-002 below. The shared responsibility files were read but not edited by the writer. The original three reports are unchanged; all three original reviewers must sign the new snapshot.

## USER-002 revision

Global information is now stated once at its natural first use in the Introduction:

- Moduli-stack interpretation over `\mathbb C`, rational Chow products and complex-codimension degree are stated in the first moduli paragraph.
- `lambda_0=1` and vanishing above rank accompany the first definition of the Hodge classes.
- Stack integration, stabilizer weights, top-degree selection and scalar coefficient extension appear immediately before the first pure Hodge integral.

The Introduction's forgetting argument now uses a direct dimension comparison on a stable target. It explicitly separates `g>=2,n>=1` (forget to `m=0`) and `g=1,n>=2` (forget to `m=1`), with genus zero excluded by positive-product/rank conventions and `(1,1)` retained. The unnecessary temporary target-class and tilde-alpha aliases are removed. The definitions of `B_g(h)` now specify `g>=2` and integer `0<=h<=g`; normalized homogeneous insertions specify `0<=d<=3g-3`.

The definitions of `Cin,N_g` and `b` precede their first theorem use, without changing their formulas. The fixed-index theorem's grammar and the integer nature of the fixed defect are clarified. The Introduction's organization placeholder is replaced by a description explicitly framed as the planned proof routes. No proof is claimed complete.

Section 2.1 now begins directly with the local formal-exponential tool and retains its degree conversion, local hypotheses, proof, factorial examples and parameter/error discussion. Section 2.2, including all first psi/kappa/character definitions and GRR normalization explanations, is byte-for-byte unchanged from r002.

No new global symbol or source input was needed. The coordinator approved this relocation and low-genus clarification. Both interfaces record the exact first-definition locations. The response to USER-002 is in the r002 response file; the old responses, review reports and source archives are untouched.

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

## Earlier unimplemented roadmap proposal

When authorized to fill `section.tex`, a short roadmap could say:

> We fix the grading and factorial normalizations, then recall Mumford's formula in the logarithmic kappa convention. These identities express Hodge insertions through odd Chern characters and the boundary. We next describe their behavior under normalization at nodes and give the boundary and forgetting formulas used in the later graph expansions.

This quotation predates USER-002 and is retained only as handoff history. It was never inserted into the manuscript; no section-2 roadmap is drafted or updated in this revision.

## Validation and next action

Author source checks for USER-002 confirmed that `eq:111`, `eq:P111`, `eq:g111` and `eq:gh11` are byte-for-byte identical to the r002 archive, that exactly four Introduction theorems retain their original label order, and that 2.2 is unchanged. The final handoff also checks UTF-8/LF/final newlines, response JSON, unique labels and scoped diff formatting. No theorem proof or reviewer approval is inferred from these checks.

The coordinator has updated `python workflow/trials/s02-01-02/build_preview.py` to typeset the revised Introduction followed by only 2.1–2.2. The writer may run that updated driver before handoff; its receipt records the actual result. The coordinator must verify and freeze r003 for all three original reviewers to recheck. The remaining section-2 TODO markers deliberately prevent representing the whole unit as complete. The writer will stop editing at handoff and await the coordinator's next instruction.
