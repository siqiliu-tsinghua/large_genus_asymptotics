# s02 writer handoff - USER-004 organization and attribution

Document role: current author handoff for the reopened s02 submission. Fixed writer: `/root/s02_writer`. Live review and acceptance status are in `workflow/state.json`. The approved formal r002 record remains immutable; the present user-requested delta requires a fresh formal round 3 review by the same original agents. This handoff does not confer approval.

## Bound user feedback

- Feedback ID: USER-004.
- Feedback path: `workflow/feedback/s02/USER-004.json`.
- Feedback SHA-256: `1e03939e205eb8014e624dacf88df3cb7e964467a45a58ec97ce579df046f5f6`.
- Previous approved formal round: r002.
- Previous snapshot: `973388c748e423ce472519ec961217561b7f97769981d4d065a3d50fed8548ac`.

The feedback contains the verbatim user request and checklist. Its raw-file digest is included here so the current source snapshot binds the request. This is a response to user feedback, not a new response to past reviewer issues: both r001 readability issues were already resolved in formal r002.

## USER-004 response: addressed

1. **Classic-source recall.** The 2.3 opening now identifies Graber-Pandharipande, Appendix A.1, as the stable-graph source and says the terminology is recalled for later use. The primary v2 text was independently checked. Its `H` contains only paired half-edges and has a fixed-point-free involution; its numbered legs form a separate `L`. Our `H(Gamma)` contains both kinds of flags and represents legs by fixed points. This difference is explicit beside the definition. FP00 is retained only for the actual Hodge conventions/sequences, not credited with our identical flag presentation.
2. **Boundary statement/proof adjacency.** Proposition 2.6 is followed immediately by its proof. The source specialization and cohomology/Chow convention are in a short two-paragraph Remark after the proof, rather than between statement and proof.
3. **Purposeful intermediate modules.** A concise Example explains loop, labelled separating-edge and ordered-splitting weights. The forgetting-map paragraph explains why the maps are introduced and retains the source/base convention. A separate one-point-comparison paragraph gives the tail divisor and original equation, immediately followed by its algebraic Proof. The complete stabilization, log-dualizing line, section self-intersection, projection/base-change and binomial argument remains in the main text. Only the source citation is placed in the following short Remark. No essential definition or hypothesis is made optional.
4. **Forgetting statement/proof adjacency.** Lemma 2.8 is followed immediately by its proof. Its source credit, Arbarello-Cornalba/Faber-Zagier attribution and notation/ordered-block conversion are in a short post-proof Remark.
5. **Versioned citations.** All KMZ formula-number citations in 2.4 now use the explicit `KMZ96v1` preprint entry. No raw version identifier remains in manuscript prose. The journal `KMZ96` entry stays in the shared database but is uncited here. ABCDGLW's checked numbering version is specified by its bibliography note, with no raw identifier repeated in 2.4.
6. **Selective reading.** Short, named source remarks and the one-edge Example have one purpose each and use short paragraphs. The proof-bearing one-point material remains in the main argument. The independent `rmk`/`exm` section counters supplied by the coordinator preserve all substantive result numbers. The coordinator fixed the initially ineffective roman-body hook with explicit theorem/remark styles, retaining the substantive counter grouping. The coordinator also updated writer/reviewer duties and the shared outline; the writer read those instructions and did not edit shared files.

## Authorized current files

Only these four tracked files are edited by the writer for this request:

- `sections/02_notation/03_gluing.tex`;
- `sections/02_notation/04_boundary_and_forgetting.tex`;
- `sections/02_notation/INTERFACE.md`;
- `sections/02_notation/writer_handoff.md`.

The Introduction, 2.1, 2.2 and section roadmap are unchanged. All frozen trial/review sources, reports, author responses, build receipts and review helpers remain untouched. No commit or state-changing workflow command is made by the writer. New clean draft products and their helper use only the ignored directory `build/reviews/s02/writer-user004-draft/`.

## Mathematical preservation

All 34 numbered equation environments and their labels retain their approved mathematical payload and order. Existing theorem/lemma/proposition/corollary labels, statement hypotheses, signs, edge weights, factorials and substantive numbers are retained. The Hodge normalization/cycle-space argument, bounded defect allocation, algebraic boundary calculation, positive-new-psi tail condition, surviving negative new-psi sum, partition inversion and degree-two finite cutoff have not been changed.

The new source-convention explanation distinguishes equivalent graph encodings; it does not change our existing graph definition. The additional one-point Proof environment exposes the already present argument without introducing a numbered result. Remarks and Examples have independent counters and roman bodies. No global font or spacing change is made by the writer.

## Exact source mapping

- `GP03`: primary Appendix A.1, PDF pages 13--14 of the version fixed in its bibliography note. It defines separate paired half-edges and numbered legs, vertex stability/genus, the product of vertex moduli stacks and the gluing map. The primary HTML/PDF was checked for this request. The source graph `A`, vertex functions `g(v),n(v)` and Betti number `h^1(A)` correspond to our `Gamma,g_v,n_v,b_1(Gamma)`; the significant flag/involution difference is described above. The publisher's title uses "of moduli spaces", while the preprint title uses "on moduli spaces"; the coordinator's bibliography fixes the cited appendix version.
- `FP00`: Section 1.3 (17)--(18), retained for one-node Hodge sequences. It is not used as the source for our full stable-flag definition.
- `LX26b`: proof of Proposition 4.4 (4.2)--(4.3), retained for the partial-normalization/cycle-space argument, not its nefness conclusion.
- `ABCDGLW23`: Lemma 3.10 (3.18)--(3.22), with version in its bibliography note. The post-proof Remark identifies constant edge series `a`, linear vertex coefficient `c`, weighted one-edge class `delta` and the cohomology-to-Chow distinction. The existing algebraic proof is unchanged.
- `KMZ96v1`: Section 2 (2.4), Theorem 2.2 (2.6), Lemma 2.2.1 (2.8), comparison (2.10), and push-pull formulas (2.9)--(2.11). The explicit versioned entry replaces every section-2.4 citation to the journal key. The post-proof source Remark retains `omega_n(a)=kappa_a` and the conversion from ordered blocks with `1/k!` to unordered partitions. The original geometric attribution to Arbarello-Cornalba and earlier unpublished Faber-Zagier is retained.

No additional source uncertainty or bibliography request remains. The existing source checks for the unchanged mathematics are retained; unchanged literature was not reread for this organizational request.

## Historical continuity

Earlier scoped records under `workflow/trials/s02-01-02/` preserve USER-001's continuous-paper inheritance, USER-002's introductory convention placement, USER-003's lowercase integral/Bernoulli/Chow conventions, and the prior punctuation correction. Formal r001/r002 records under `workflow/reviews/s02/` remain immutable. The new request is bound above and is not relabelled as a past reviewer issue.

The current notation remains `a_g,b_g(h),b_g`, ordinary `B_m`, `A^a(X;Q)`, scalar `b`, and later one-point `beta_g`. Hodge indices remain `j_1,...,j_ell`, factor count `ell`, and flags use `f,f'`; `g_2` and the Bessel names are unchanged.

## Checks and handoff

The final source checks compare the numbered equations, result statements and unaffected files with approved r002, verify citation keys and absence of raw version identifiers in manuscript prose, and check proof adjacency and independent Remark/Example counters. Documents remain ASCII-safe UTF-8 with LF and final newlines, with no corrupted separators.

After all four files and the settled shared inputs are saved, the writer runs repository validation, the draft gate, native strict build and a separate label-free draft build. The clean log is required to have zero overfull horizontal/vertical boxes; selected pages are inspected visually. Actual outcomes and matching source hashes are recorded in the draft receipts and reported to the coordinator. The clean artifact records no new review signature; the coordinator freezes formal r003 and obtains all three original reviewers' fresh signatures.

The writer stops editing at handoff until the collected reviews or another explicit instruction arrive.
