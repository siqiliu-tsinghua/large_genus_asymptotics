# Appendix C r001 mathematical handoff

Reviewer: `/root/s02_math`. Verdict: **pass**.
Snapshot: `13570207b4cdb59aee7e4720a5ac1b2cc51f89ec8b10d68fcf3e64a03e7659ab`.
`issues=[]`; `resolved_issue_ids=[]`.

This is the first complete scientific review of Appendix C. Read both
new subsections, entry, interface, handoff, all checker code, README and
computation record. Checked the exact frozen s06 vertex/tree formulas
and s02 Chern relation against their use here; the old asymptotic proofs
and long A/S4 calculations were not rerun.

## Independent mathematical reconstruction

For an unmarked stable tree, the exact relation
`sum m_v=g_2-E`, with every `m_v>=0`, gives `E<=1` for g=2 and `E<=3`
for g=3. Stability excludes rational leaves and rational bivalent
vertices. Thus genus two has exactly the one-vertex tree and elliptic
pair. Genus three has the one-vertex tree, genus-(1,2) edge and the
three-elliptic chain; at E=3, all orders are zero, excluding bivalent
vertices and forcing the rational center with three elliptic leaves.
There is no omitted tree type; cyclic graphs are absent by the inherited
exact top-Hodge tree identity.

Finite coefficient extraction gives the six stated polynomials. In
particular `[x^3]Phi^-4=61/36`, so multiplication by 3! gives
`W_(3,0)=61 beta_3/6`. For the genus-two one-leg vertex,
`[x^2]Phi^-3 J_0(2sqrt(sx))=5/4-3s/2+s^2/4`, and its 2! gives
the stated `5/2-3s+s^2/2`. The two-leg elliptic vertex is
`beta_1(1-s-t)`. The zero-order vertices are exactly beta_1 and 1.
The one-point coefficients are independently recovered as
`beta_1=1/24`, `beta_2=7/5760`, `beta_3=31/967680`.

The genus-two pair has Aut=2. In the manuscript's genus-three order,
the automorphism orders are 1,1,2,6. Using one common variable at each
edge's two ends, the mixed edge integrates to `7 beta_1 beta_2/6`;
the chain integrates to zero because `1-1/2-1/2=0`; the star contributes
`beta_1^3/6`. The chain remains in both the proof and actual enumeration.

The full tree sums are `1/480` and `1/2520`. Restoring the exact
exponential-to-power factors gives

`b_2=(1!/12)(1/480)=1/5760`,
`b_3=(3!/12^3)(1/2520)=1/725760`.

The coefficient of t^2 in `c_t c_-t=1` gives `lambda_1^2=2lambda_2`.
In rank three, the coefficient of t^4 gives
`lambda_2^2=2lambda_1 lambda_3`. Substituting the first relation and
then multiplying by `lambda_1^2` yields the top-degree identity giving
`a_3=8b_3`; no division by lambda_1 is used. Likewise `a_2=2b_2`.
This gives exactly `a_2=1/2880`, `a_3=1/90720`, the defect ratios
`(2,2)` and `(4,8,8)`, and `<lambda_3>_3=b_3/a_3=1/8`.

All dimensions, stable zero-order cases, beta_0 convention and shared
edge parameters match the accepted exact inputs. Definitions and dummy
ranges are available before use or directly inherited. The proposition
has an adjacent proof, and all three numbered formulas agree with the
actual full native pages 98-99.

## Actual checker execution and separate implementation

Ran the exact frozen checker bytes under a private root:

    python -B build/closing-writing/math-c-r001/isolated/sections/c_exact_checks/checks/run.py

This preserves the source-relative location and algorithm while keeping
the author's existing output untouched. The source hash is
`d80607341d6d81db41376fea2386bb7528590361d6c9929c8b4c3ae349909b5b`.
The actual JSON hash is
`0f6655b1cb27ef66190ab96f2440a8d40a1e057bdbcfd8539f03da9411a1669d`,
identical to the tracked computation record, using Python 3.14.10.
Every final post-comparison passed.

Inspected the full implementation: finite sinc inversion, Phi inverse
powers, J_0 coefficients and every polynomial operation use Fraction;
Pruefer trees and weak genus compositions cover the exact degree bound;
stability is enforced; shared edge powers are added before integration.
The number of vertex labelings is V!/Aut for these simple trees, so the
division by V! gives the exact graph factor. The separate permutation
calculation checks stabilizers. Targets and proposed class counts appear
only after the complete reconstruction returns; no preparation data is
read. The computation-only flags accurately distinguish author execution
from this review.

Also wrote and actually ran:

    python -B build/closing-writing/math-c-r001/independent_exact.py

This implementation uses connected subsets of complete-graph edges,
Bernoulli-derived beta coefficients and a direct negative-binomial Phi
expansion. It independently reconstructs all outputs before reading
the other result. Every class, Aut, labeled multiplicity, edge integral,
weighted contribution, vertex polynomial and final rational value agrees.
The labeled counts are 2 and 10 and the unlabelled counts 2 and 4.
Both programs' generated results remain in this ignored private tree.

The finite Taylor orders suffice because Phi has constant term one and
all requested coefficient degrees are at most three. All integrations
and sums here are finite; there is no unproved analytic interchange or
numerical precision issue. The appendix and its documentation correctly
make no inference of an asymptotic rate. The existing A/S4 entrypoints
are documented as resources, not used as inputs to these finite values;
supplementary higher coefficients remain outside Theorem 1.1's proof.

## Frozen identity and build checks

Verified all 117 frozen/live entries, archive artifacts, canonical
snapshot and actual `/root/s02_math` binding. All ten approved dependency
units are fresh. Actual mathematical inputs here are s01 definitions
and exact s02/s06 results; the formal closure adds no circular premise.

- Render source: `27f0f5e339e10c06fa5b216cccefd2d0828c4fa9d45a106c69d632e3171fb6cc`.
- Standard 101-page PDF: `9c17a93cbd69454a6fdb399801f3b985f0c82d5b2d6e77db30690acbf2146609`.
- Standard entry/helper: `7d40710c82bfb9a16df8accd4acacc0dda12906724897d15a1046191e6e5ea1a` / `83e54aba6b9d59878fefe7c120f9385cfefa2fdc21f5347dacdcbb387bb052db`.
- Full 101-page manuscript PDF: `c31f2039fcf9fa30da3d5a96e10fe8ee8e936e3193e973d1fcd6e9c21bebd585`.
- Full entry/helper: `8a8f67b49b9ef17daf20e077a76a80bb261200d8a850fe86f88c119c2782e6d4` / `ebed6268396249456c961fa8831fa42b12f8ae9fcc5a48762b5b896a7f295ee3`.

Both receipts match actual files, this snapshot and the common source
hash, with strict native 10pt builds and empty standard/layout diagnostics.
The full entry retains title/abstract and differs from frozen main.tex
only by the explicit complete section assembly. Inspected C on full
manuscript pp.98-99. `python -B scripts/validate.py --unit c` passes.
Private artifact audit: `build/closing-writing/math-c-r001/audit.json`.

Only these reports and authorized ignored private checks/renderings were
written. No scientific/shared source, state, other report, old record,
author-generated output or frozen PDF/receipt was changed. Stop for
coordinator collection and registration.
