# Section 4 acceptance and final handoff

Section 4 is approved on its first complete formal round, snapshot
`4e6231907bb5784de1905d6c162f5a72c2e8ac815e689e456ef9d3080d8b0050`.
The original writer and three original reviewer identities were reused.
All three reports pass with no unresolved issue, and the actual acceptance
gate completed a fresh strict integrated build. No source was changed during
review or after acceptance.

Theorem 1.1 now has a complete body proof: correlated signed-loop moments;
separate volume/profile first corrections and three complexity-one cores;
the three absolute second-order groups and a worked complexity-two core;
then the whole-graph tail with M=3, all legal loop tails, K=2-q core errors,
factorial summation and restoration of the original Hodge normalization.
The independent reviews confirm the exact coefficients and strict O(g^-3)
remainder, physical first definitions, source attribution and readable layout.

Appendix A r002 was completed and accepted first. It supplies the full finite
profile and volume reconstruction, signed moment calculations, four low
vertices, complete 1/3/13 core lists and seven reproducibility certificates.
Its first-round normalization/source presentation issues were corrected by
the original writer and explicitly closed by the same three reviewers.
EGGLS24 remains a conditional comparison, not a proof input.

The supporting bibliography, TikZ package and notation policy were settled
before the appendix review. Those shared inputs required dependency refreshes
s02 r006 and s03 r003, both formally approved by their original reviewers.
Their scientific TeX and rendered text were verified unchanged; their changed
interfaces/handoffs record the new dependency provenance only.

Frozen clean integrated preview (sections 1--4 and Appendix A):
`build/reviews/s04/r001/preview.pdf`, 65 pages. Its receipt binds source hash
`e0c123c63cdf7471e9f311c9e8943c8a310658445fc5c58e3361e1b550154332`
and PDF hash
`90f98a8f626d6f782b195f6fb9db69ba9d56c9fe18ea575e773abb24f4d38048`.
Both diagnostic arrays are empty. All new body pages and representative
reflowed appendix diagrams/tables were actually inspected; the coordinator
also inspected the final proof on page 39.

The default assembly now contains s01, s02, s03, s04 and a. An actual
`python scripts/build.py --strict` regenerated `build/main.pdf` successfully,
with no standard or overfull diagnostics. Its source/entry closure and PDF
hash were checked. Full record/freshness/LF validation and `git diff --check`
passed. Machine-readable final evidence is in `coordinator_audit.json`.

The user-requested prior Section 3 batch was committed first as `213c1ca`,
using the existing global Git identity. New Section 4/Appendix A work and
supporting review/dependency records remain uncommitted. Neither refs nor
build is tracked. Later theorems and sections are outside this completed unit.
