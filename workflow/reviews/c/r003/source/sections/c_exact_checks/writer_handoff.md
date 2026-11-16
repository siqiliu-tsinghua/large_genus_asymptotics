# Appendix C original-writer handoff

Writer: /root/s02_writer, retained original session.
Unit: c. This is a complete first author draft, not approval.

## Delivery and scope

The section entry now assembles 01_exact_values.tex and
02_reproducibility.tex; the old content.tex placeholder is removed.
The coordinator's two-subsection manifest is used unchanged.
The directory also contains INTERFACE.md and the self-contained
checks/run.py, checks/README.md and checks/verification.json.
Only this unit was edited. No shared, approved dependency, state,
old report or frozen output was changed.

The mathematical text is intentionally short: one proposition
with a proof, three numbered equations, the two-row exact-value
table and a brief reproducibility guide. All finite data are kept
separate from the main asymptotic claims.

## Independent reconstruction at the author level

Read the actual c dispatch/task, the short outline, needed accepted
s02/s06 formulas and s04/A interfaces/source instructions. The
outline's old statement about missing programs is obsolete;
the actual tracked A/S4 bundles are documented, not rebuilt.
The ignored coordinator notes were leads and cross-checks,
not authority or manuscript citations.

The proof first classifies every allowed tree using E<=g_2 and
stability. For genus two there are the one-vertex and elliptic-pair
trees. For genus three there are the one-vertex, mixed-genus edge,
elliptic chain and rational star. It derives the six vertex
polynomials from finite Phi/J0 extraction and beta_1,beta_2,beta_3
from the reciprocal sine series.

All weights and integrals are retained. The chain's integral is
zero because integral(1-s-t)=0, rather than because the graph is
excluded. The mixed edge contributes 7 beta_1 beta_2/6 and the
star beta_1^3/6. Restoring 3! gives
12^3 b_3=61 beta_3+7 beta_1 beta_2+beta_1^3.
Mumford's degree-two/four rank relations then give a_2=2b_2,
a_3=8b_3, the defect ratios and <lambda_3>_3=1/8.

The new original-writer code implements the labeled-tree method
described in the preparation, without importing its scripts or
data. It performs actual finite sine/Phi/J0 extraction, generates
Pruefer trees and all weak genus compositions, rejects unstable
vertices, multiplies Fraction polynomials and integrates shared
edge parameters exactly. Division by the factorial of the number
of vertices gives the graph weights; a separate permutation
grouping checks the resulting automorphism factors. Proposed
values and class counts appear only after complete reconstruction.
This is not called an independent reviewer's algorithm.

## Actual execution and provenance

Ran:

    python -B sections/c_exact_checks/checks/run.py

It completed using Python 3.14.10, standard library only. The
two genera produced respectively two and four graph classes.
The exact values are a_2=1/2880, b_2=1/5760, a_3=1/90720,
b_3=1/725760; the positive-defect ratios are (2,2) and (4,8,8),
and normalized <lambda_3>_3=1/8. Every post-comparison passed.

Algorithm SHA256:
d80607341d6d81db41376fea2386bb7528590361d6c9929c8b4c3ae349909b5b.
Output build/c-exact-checks/results.json SHA256:
0f6655b1cb27ef66190ab96f2440a8d40a1e057bdbcfd8539f03da9411a1669d.
The tracked verification record binds these actual files and
marks the result computation_only, not independent acceptance.
The last paper/README wording change does not change this algorithm.

The companion README gives the actual existing A run_all.py and
standard-library core-enumerator commands, and S4 run.py plus its
verify-existing option. It preserves their SymPy 1.14.0/mpmath
1.3.0 requirements and ignored output locations. None of those
long unchanged reconstructions was rerun. The S4 bundle remains
support for supplementary reported data with omitted paper
derivations, without extending Theorem 1.1.

## Checks and handoff boundary

Final static checks cover UTF-8/LF/final newline, unexpected
controls, placeholder absence, references/citations, environment
and proof adjacency, checker syntax, source/output fingerprints,
approved dependency freshness and absence of unit bytecode or
generated data. Draft-gate/unit validation and exact scope are
checked before final source-hash reporting.

No native build is run by this author, as assigned. The coordinator
handles page layout, freezing and the actual three original
reviews. No known mathematical, source or shared-input gap remains
at the author level. STOP after the reported checks; retain this
session for revision.
