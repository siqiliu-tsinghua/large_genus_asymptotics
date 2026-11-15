# s05 r001 readability handoff

- Original readability reviewer: `/root/s02_readability`.
- Snapshot: `ccc9f748fa39b46bdc2f1e300b4e57e5037b9bbf0337e0301d634725bb49e7f0`.
- Verdict: **changes_requested**.
- Open issue: **READABILITY-001**, minor. `resolved_issue_ids=[]` for this new unit's first round.

I read the complete Section 5 entry and 5.1-5.3, interface and handoff against the current role/context, target outline and retained approved interfaces. The route is understandable: labelled exact source identity and forgetting rule; whole-graph and original-core estimates; algebraic filtration; one-source free/edge calculation; finite endpoint recurrence; Theorem 1.2 and three examples. The source families and local derivative notation have useful recurring roles. Definition order, ranges, global notation consistency and symbol economy/design do not need revision. In particular `[r]` inherits the explicit `[m]={1,...,m}` convention in s02.4; no redundant new setup is needed.

READABILITY-001 is the single common-q=1 paragraph in `02_single_character.tex:49`, running through line 66 and across the foot of clean PDF p.45/top of p.46. It combines the negligible small-vertex case, the unchanged large-vertex leading factor, quotient cancellation and the remaining/new negligible terms. Add local paragraph breaks immediately before **'A free marking on the large vertex instead ...'** and **'Consequently all q=1 contributions ...'**. This makes the common factor and cancellation visible as separate steps. Preserve the complete argument and specified-edge error statement; no new environment, global spacing/font adjustment or mathematical rewrite is requested.

All six principal statements have adjacent proofs. The full source sums and all legal loop counts receive explicit controls before HMT expansion; the free-marking exponential survives forgetting, the signed profile's inverse-genus conversion is stated, the common terms cancel additively, and the specified-loop branch half is counted once. The finite degree generator and X_k recurrence/table make the coefficient substitution auditable. The Remark and three short examples have clear optional purposes.

I inspected every new body page, pp.40-49, plus the adjacent appendix continuation p.50. The source/forgetting formulas, bounds, one-source ratios, profile difference, ODE table and final theorem display are readable at normal size. No material overflow or page-break defect was found beyond the paragraph-density issue above. Entry/helper hashes match the exact strict receipt, whose standard/layout diagnostics are empty.

All 77 input hashes, three artifacts and snapshot were verified; 69 source files shared with s04 r003 are byte-identical. Source hash: `0b4d4192f1d946d3d0f0ec44916013f894e9bb0ad6c2256c4e701c4cabd459ce`. PDF hash: `b7802e15f0127f522ed589f204d280781df859b361775554624a130203675d70`. The PDF has 74 pages. Own images/text are confined to `build/reviews/s05/r001/readability-inspection/`.

Only this handoff and `readability.json` were written in the review records. No manuscript, shared input, workflow state, other report, old record or shared build was changed. Review work stops pending the original writer's response and a new frozen snapshot; this same reviewer remains available for recheck.
