# S8 closing conjecture: original-writer handoff

Agent: /root/s02_writer. Unit: s08. Current task:
build/remarks-20261115/s08_task.txt, SHA256
293b9b67e57c985493725ecccda1b66884e08a3dea2b2b3de23389ea219998e1.
The previous approved scientific source is r003, snapshot
c601a2dae270a1a811098502cb2989753307a6f811a4328e77489fde2851cc69.
Live review and acceptance status belongs to workflow/state.json.

## Assigned change

The final Remark rmk:s08:further-asymptotics is appended after the
complete Theorem 1.4 proof. It begins by stating that the proof does
not determine higher-order terms, and labels the h=1 limit explicitly
as a conjecture. It uses only rho, z_{0,1}, J_1 and b_g(h), with no
new coefficient name or numbered equation. The old theorem remains
an asymptotic equivalence; neither the o(1) transfer error nor the
O_h(g^-1) background comparison is strengthened.

The small table displays the scaled residual at g=10,15,20 and the
intercept of its line in 1/g through consecutive genera g-1,g.
The analytic candidate 0.207760231708341177... is computed from the
Bessel values, not fitted. The Remark ends with the open problem
of proving this refinement and finding higher terms for fixed h.
No omitted high-order proof has been silently assumed.

## Actual numerical run and provenance

Executed:

    python -B sections/08_fixed_defect/checks/run.py

The program used mpmath 1.3.0 at 100 decimal digits and the archived
19 exact pairs for g=2,...,20. The table reproduced
0.136921/0.195400, 0.158393/0.203572 and 0.170045/0.205670
(raw residual/adjacent extrapolation).

The selected observations are from LiuData26, repository
https://github.com/siqiliu-tsinghua/hodge_data, fixed commit
88dd4a501ecf3fbc124a823ad1589911f86a14e5. The archive retains
the 19 source-file hashes and sizes. Its SHA256 is
9e4370649bae7db217ac41fa5197f4756dc618a7d8805688688240df3d7e825a.
The two earlier extractions agree on all 38 rationals; this checks
extraction consistency, not validity of the entire table. I read the
external AGENTS.md and README.md, including the caveat that no
additional independent validation of g>14 is claimed.
The external repository was not changed, no Sage assignment was
executed, no SQLite file was opened, and no new integral was computed.
The default checker reads only its archived snapshot.

Code SHA256:
404074e96f6299ebaf2047a963b1f8e1d24d511a8c30155ba5bd82f5c6531035.
Generated result: build/s08-higher-check/results.json, SHA256
de9e0fa164787e403842fcdbb13caa6b5da652b101e787277bed5d36094751b1.
checks/verification.json records the actual run, code/data/document
hashes and computation_only status. Finite observations do not
prove a limit, establish an error rate or validate the complete data.

## Preservation and handoff

The original 06_proof.tex is retained as a literal byte prefix.
All other old S8 TeX and the old writer_handoff.md remain unchanged.
The 33 old numbered equations, 13 principal statements, 14 proofs
and existing labels are preserved. The INTERFACE extension separates
the conjectural report from the proved exports.
No old A/S4 calculation was rerun. The inherited approved S6 higher
Remark is not a proof input for this conjecture. Shared inputs,
earlier sections, reports and workflow state were not edited here.

The new bundle and authorized prose receive UTF-8/LF, control-character,
byte-preservation and source-scope checks before handoff. Native layout,
freezing and the original three independent reviews remain with the
coordinator; this document is an author handoff, not a review pass.

Actual static checks passed: the 1,729-byte original proof is an
exact prefix, all 33 numbered equations/13 principal statements/14
proofs are byte-identical, and the old label sequence is preserved.
Only the assigned proof-file extension and INTERFACE extension
change old S8 files; the five new files are this handoff and the
four-file checks bundle. UTF-8/LF, final newlines, control characters,
absence of bytecode, archived selected-input identity, and recorded
source/output digests passed. Engine dependency freshness, original
archive integrity and the draft gate passed by read-only checks.
The detailed guard result is build/s08-higher-check/author_guards.json.
No native build or workflow transition was run by this author.
STOP for the coordinator's native build and frozen review.

Before freezing, the two column explanations were moved before the
table. The middle column now explicitly evaluates the expression
inside the limit, and the last column uses the consecutive genera
g-1,g for linear extrapolation in 1/g. The table, limit formula,
candidate value, source citation and conjectural status are unchanged.
No numerical code or output changed, and no calculation was rerun.
The source guards and final draft fingerprint are refreshed for this
prose-only clarification.
