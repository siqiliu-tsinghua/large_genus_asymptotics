# Exact low-genus values

Scientific interface for the complete Appendix C author draft.
Live review, freshness and acceptance status belongs to workflow/state.json.
No computation record here constitutes a review signature.

## Scope and assembly

The entry assembles only 01_exact_values.tex, under the title
Exact low-genus values. The engineering subsection
02_reproducibility.tex is removed from the manuscript; the
coordinator supplied the corresponding one-subsection manifest.
The complete mathematical subsection is preserved byte-for-byte.
There is one proposition with an adjacent proof and three numbered
equations. The appendix contains exact checks only; it neither fits
an asymptotic expansion nor supplies an input to a main theorem.

The formal dependency closure contains the ten approved units
s01--s08, a and b. Actual mathematical inputs to the finite
derivation are only the s01 definitions and exact s02/s06 results.
Neither supplementary higher coefficients nor the h=1 numerical
conjecture is an input to the exact values.

## Inherited notation and local scopes

| Symbols or input | Definition/source location and use here |
| --- | --- |
| a_g,b_g(h),b_g and normalized bracket | Introduction; all exact values use the existing definitions without a new normalization |
| g_2=2g-3 | Introduction; the factorial recovered from the tree sum is 1! in genus two and 3! in genus three |
| lambda_j,lambda_0 and rank conventions | Introduction and s02; provide the finite-rank Chern relations |
| c_t(EE) | eq:s02:chern-definitions and eq:s02:chern-exponential; c_t c_-t=1 is used in the proof |
| beta_G,Phi and top vertices | eq:s06:beta-series, eq:s06:phi and eq:s06:exact-vertex; all coefficients are extracted exactly |
| Stable graphs/trees, g_v,n_v,Aut | s02 and eq:s06:tree-expansion; graph weights are reciprocal automorphism orders |
| E,m_v | Local to the classification proof; E is the number of edges and m_v=2g_v-3+n_v is the inherited nonnegative vertex order |
| s,t,u | Before eq:c:vertices; real edge parameters in [0,1], shared at the two ends of an edge |
| x | Vertex-extraction paragraph; the coefficient variable of the inherited exact vertex formula |
| h in the result table | Bound integer index 1<=h<=g, only for the rows g=2,3 |

No new global symbol or family is introduced. Hodge j-indices,
ell, ordinary Bernoulli B_n, scalar b, beta_g and g_2 retain their
previous meanings. The table's finite list of defects is not a
growing-defect asymptotic statement.

## Exact exports and proof

- prp:c:low-genus gives a_2=1/2880, b_2=1/5760,
  a_3=1/90720 and b_3=1/725760.
- The same proposition gives b_2(h)/b_2=(2,2) for h=1,2 and
  b_3(h)/b_3=(4,8,8) for h=1,2,3.
- eq:c:lambda-three gives the finite value
  normalized <lambda_3>_3=1/8, distinct from the Section 5
  asymptotic example.
- eq:c:vertices lists the six required exact vertex polynomials.
- eq:c:tree-values gives
  12 b_2=beta_2+beta_1^2/2 and
  12^3 b_3=61 beta_3+7 beta_1 beta_2+beta_1^3.

The proof uses the tree-degree bound E<=g_2, leaf stability and
the zero-order condition at E=3 to prove list completeness.
The genus-two list has two types; the genus-three list has four.
The latter automorphism orders are 1,1,2,6 for the one-vertex,
mixed-genus edge, elliptic chain and rational star. The chain
integrates to zero and is explicitly retained in the classification.
The proof restores the exponential-to-power factorial before
computing b_3. Mumford's rank-two/three relations then give
a_2=2b_2 and a_3=8b_3 and all displayed normalizations.

## Sources and status

- FP03, Theorem 1, and FP00, Theorem 2/(6), enter through the
  approved s06 exact multipoint/one-point results and sine series.
  The genus-zero convention is already in that accepted theorem.
- Mum83, Section 5, enters through s02's Hodge GRR/Chern relation.
  The rank-three degree-four specialization is proved explicitly here.
- eq:s06:tree-expansion, eq:s06:tree-degree and
  eq:s06:exact-vertex are exact finite-genus identities, not
  asymptotic estimates. No volume expansion or conditional
  resurgent prediction is used.

The coordinator's ignored preparation notes provided cross-checks,
not authority, a target fit, a manuscript citation or an independent
review. The writer implemented the labeled-tree method from the
exact formulas and performed the complete reconstruction before
the target comparisons. No new reference, macro or shared input
is requested.

## Internal checks and provenance

The following records concern internal author checks only. They are
not manuscript instructions, submission attachments or premises of
the proof. The full tree classification, vertex extraction, edge
integrals, automorphism weights, factorial recovery and Chern
identities are given in the retained mathematical subsection.

- checks/run.py is self-contained and uses only the Python standard
  library, with exact Fraction arithmetic and no imported data.
  It computes sine/Phi/J0 coefficients, enumerates labeled trees
  and all genus compositions, integrates shared edge variables,
  divides by the factorial of the vertex count, and independently
  groups permutation classes to check their automorphism weights.
- Its actual completed run used Python 3.14.10 and writes only
  build/c-exact-checks/results.json plus console output. Bytecode
  is disabled. Graph counts and announced values enter only the
  final post-reconstruction assertions.
- checks/verification.json records the actual algorithm SHA256,
  command, Python version, exact results, class counts and output
  SHA256. Its stage is computation_only, not review or acceptance.
- checks/README.md gives the new standard-library command and
  the existing A/S4 commands, pinned SymPy 1.14.0/mpmath 1.3.0
  workspace-local installation, source/output locations and the
  distinction between proven finite formulas and supplementary
  coefficients whose paper derivations are omitted.

The long A and S4 calculations were not rerun for this appendix.
No released commit, public URL or external dataset is invented.
The existing three checks files and their historical outputs remain
internal and unchanged; no program is rerun for this revision.

## Remaining boundary

The mathematical finite checks and the new calculation are complete
at the author level, with no known source gap. Native pagination,
compilation and all three independent frozen reviews remain
coordinator/reviewer work. Exact low-genus identities do not prove
an asymptotic rate or strengthen any of the four main theorems.
