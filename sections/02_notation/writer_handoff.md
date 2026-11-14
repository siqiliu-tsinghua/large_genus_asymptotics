# s02 writer handoff — trial of 2.1 and 2.2

Status: drafting / incomplete. This handoff covers the authorized Introduction + 2.1–2.2 trial, updated through USER-003 after trial round 4. It is not a formal submission of either whole section and does not authorize acceptance. Original writer session must be retained for revision and for eventual completion of 2.3–2.4.

## Files written

- `sections/01_introduction/section.tex`: limited clarification and relocation of global conventions at first use; stable-forgetting dimension argument; normalization ranges; current lowercase integral-family names; parenthesized Chow coefficients; requested Bessel argument and ILW wording. Main target values and error orders remain unchanged under the naming translation.
- `sections/01_introduction/INTERFACE.md`: records this limited baseline revision, global first-definition locations and unchanged theorem targets.
- `01_conventions.tex`: now starts with formal exponentials, followed by the exponential-to-power lemma and proof, exact `a_g` / `b_g(h)` factorial restoration, and fixed-parameter/error conventions. The global Chow/degree/integration/rank conventions have moved to the Introduction and are inherited directly.
- `02_tautological_classes.tex`: psi before logarithmic kappa; direct source-cotangent transition; factorial-normalized Chern characters and Chern polynomial; parenthesized Chow coefficients; total reduced boundary, chosen node and ordered branches; ordinary Bernoulli notation; fully normalized marked Mumford formula; nonlogarithmic conversion with a short section-intersection argument; divisor specialization; root-based exponential rewrite and lambda-two/lambda-three examples with proof.
- `INTERFACE.md`: exact assumptions, scopes and reasons for notation, result labels, verified primary locators, and explicit unfinished parts.
- `writer_handoff.md`: this record.
- `workflow/trials/s02-01-02/r001/author_response.json`: separate response to USER-001, with no open reviewer-issue responses and no alteration of the original pass reports.
- `workflow/trials/s02-01-02/r002/author_response.json`: separate response to USER-002; the r001 response and all previous reports remain unchanged.
- `workflow/trials/s02-01-02/r004/author_response.json`: current response to USER-003; no old response or report is modified.

For USER-003, the only chapter edits are the six assigned current Introduction and 2.1–2.2 source/interface/handoff files. No changes were made to the section-2 roadmap, 2.3, 2.4, the preamble, bibliography, abstract, other chapters or workflow state.

## USER-001 revision history

The updated writer/readability responsibilities and shared notation policy treat the paper as a continuous text. The earlier opening wrongly repeated the Introduction's basic setup; correctness of those repetitions did not justify them.

- Removed the paragraph reintroducing `g,n`, stability, the moduli stack and its base. That revision began with Chow/degree/integration conventions, subsequently relocated by USER-002.
- Removed the inventory of the Hodge bundle, Hodge indices, normalizations and `g_2`, along with the needless pointer to Theorem 1.3. Their full inherited ledger remains in `INTERFACE.md` for collaborators.
- Retained the new conventions `lambda_0=1` and vanishing above rank, the homogeneous conversion lemma, its precise local bounds, the factorial examples and the fixed-parameter/error table.
- Shortened the 2.2 opening to identify `pi=pi_{n+1,n}` with the universal stable curve. It introduces sections and the dualizing sheaf in their needed roles without retelling the already defined forgetting operation.
- Removed the routine Introduction reference before the factorial example and the redundant prose labeling the root and Chern-class dummy indices. The psi/kappa/character definitions, boundary normalization, literature conversion and proofs remain intact.

No mathematical identity or hypothesis was changed in that revision. Its placement of the new global conventions at the start of 2.1 is superseded by USER-002 below. The shared responsibility files were read but not edited by the writer. The original three reports are unchanged; all three original reviewers must sign the new snapshot.

## USER-002 revision history

Global information is now stated once at its natural first use in the Introduction:

- Moduli-stack interpretation over `\mathbb C`, rational Chow products and complex-codimension degree are stated in the first moduli paragraph.
- `lambda_0=1` and vanishing above rank accompany the first definition of the Hodge classes.
- Stack integration, stabilizer weights, top-degree selection and scalar coefficient extension appear immediately before the first pure Hodge integral.

The Introduction's forgetting argument now uses a direct dimension comparison on a stable target. It explicitly separates `g>=2,n>=1` (forget to `m=0`) and `g=1,n>=2` (forget to `m=1`), with genus zero excluded by positive-product/rank conventions and `(1,1)` retained. The unnecessary temporary target-class and tilde-alpha aliases are removed. The definitions of `b_g(h)` now specify `g>=2` and integer `0<=h<=g`; normalized homogeneous insertions specify `0<=d<=3g-3`.

The definitions of `Cin,N_g` and `b` precede their first theorem use, without changing their formulas. The fixed-index theorem's grammar and the integer nature of the fixed defect are clarified. The Introduction's organization placeholder is replaced by a description explicitly framed as the planned proof routes. No proof is claimed complete.

Section 2.1 begins directly with the local formal-exponential tool and retains its degree conversion, local hypotheses, proof, factorial examples and parameter/error discussion. At that revision, Section 2.2 was unchanged from r002; the USER-003 changes below now update its coefficient formatting, notation and transition prose.

No new global symbol or source input was needed. The coordinator approved this relocation and low-genus clarification. Both interfaces record the exact first-definition locations. The response to USER-002 is in the r002 response file; the old responses, review reports and source archives are untouched.

## USER-003 revision

- The Introduction's first-positive-zero description now says `J_0(z)`, and its last paragraph uses exactly `the ILW equation`.
- All current Chow expressions use `A^a(\MM_{g,n};\mathbb Q)` or the appropriate degree, keeping uppercase `A` for the Chow functor and placing the coefficient field inside the parentheses.
- The integral families are consistently `a_g`, `b_g(h)` and `b_g`, including the normalized-bracket denominator, theorem statements and factorial examples. Ordinary uppercase `B_m` is reserved for Bernoulli numbers, with the same generating series and signs. The scalar correction `b` and later one-point coefficient `\beta_g` are retained.
- The obsolete font explanation is removed. The descendant explanation and recipe-like reference before logarithmic kappa are replaced by a direct transition identifying `\psi_{n+1}` as the last cotangent class on the source `\MM_{g,n+1}`.
- Both interfaces and this current handoff follow the new names; frozen archives, earlier responses, review reports and addenda remain unchanged. No new source or mathematical object is introduced.

The four main target equations and all numbered identities retain their mathematical payload after the canonical notation/format translation. Hypotheses, numerical coefficients, labels, theorem order, constants and error orders are preserved.

## Mathematical decisions

1. All integrals are stack degrees. The ordered-node cover records both branch orientations, giving `delta=(1/2)xi_*1`; this is also the normalization of the GRR boundary term.
2. `kappa_a=pi_*(psi_new^(a+1))` is logarithmic. FP00 §1.1 uses the nonlogarithmic dualizing power. The local comparison is proved by identifying the universal curve with the forgetful source, writing the new cotangent class as the logarithmic dualizing class, and using disjoint sections with normal bundle `L_i^vee`. The contribution of each marking is the alternating binomial sum equal to `psi_i^a`. This supplies the negative marking term in the stated GRR formula.
3. `ch_a` includes `1/a!`. The coefficient in `log c_t` is consequently `(-1)^(a-1)(a-1)! ch_a`. Even characters vanish; odd coefficients are positive after the sign specializes to odd `a`.
4. `12lambda_1=kappa_1+delta-sum_i psi_i` follows from `B_2=1/6` and the half-boundary normalization. The unmarked specialization is explicitly restricted to `g>=2`.
5. Exponential-to-power conversions are exact finite-genus degree selections. They do not provide any uniform asymptotic estimate or interchange of graph sums.
6. `g_2`, the `j`-family Hodge indices and `ell` are retained. The WP scale is deferred, and there is no extra dimension abbreviation. Uppercase `A` is the Chow functor, ordinary uppercase `B_m` the Bernoulli family, and lowercase `a_g,b_g(h),b_g` the integral families. Scalar `b` and the later `\beta_g` retain separate roles. One local map `pi`, explicitly identified with the inherited `pi_{n+1,n}`, serves as both forgetting map and universal stable curve; no second family-map alias is introduced.

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

Current source checks compare every numbered equation with r004 after the canonical notation/format translation, including the four target equations; exactly four Introduction theorems retain their original labels and order. The handoff also checks UTF-8/LF/final newlines, response JSON, unique labels, scoped diff formatting and the absence of stale current integral names or obsolete Bernoulli formatting. No theorem proof or reviewer approval is inferred from these checks.

The coordinator is synchronizing the shared notation documents. After the coordinator's confirmation, the writer will run `python workflow/trials/s02-01-02/build_preview.py` for the Introduction followed by only 2.1–2.2; its receipt records the actual result. The coordinator must verify and freeze the next snapshot for all three original reviewers to recheck. The remaining section-2 TODO markers deliberately prevent representing the whole unit as complete. The writer will stop editing at handoff and await the coordinator's next instruction.
