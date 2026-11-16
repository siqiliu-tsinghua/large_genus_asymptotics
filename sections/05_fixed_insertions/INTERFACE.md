# Fixed degree Hodge insertions

Scientific interface for Section 5 and its proof of Theorem 1.2. Live review and
acceptance status belongs to `workflow/state.json`; this document is not a
review signature.

## Dependencies and scope

These snapshot IDs record the original scientific dependency provenance.
Current approvals and dependency freshness belong to the workflow.

- Historical s03 r003 snapshot:
  `5dea38f471fe1170933c94c84ef50f5741165dd9b682d3043d547428d4949353`.
- Historical s04 r003 snapshot:
  `172195b1a31c1584895d46b98f3c7790c556bc27b4302993f8eac254d897fbb9`.

The dependencies transitively contain the geometric identities of s02 and
Appendix A. Section 5 proves `thm:fixed-insertions` / `eq:P111` with the
original fixed-index scope and O(g^-4) precision. The use of Section 4 is
its signed loop functional/moments and previously introduced profile
notation. Neither the explicit second coefficient of Theorem 1.1 nor the
supplementary third/fourth coefficients is used.

All insertion degrees, their count and the target expansion order are
fixed. The estimates do not assert uniformity for growing Hodge indices.
There is no Schubert, higher single-character coefficient or connected
correction statement in this unit.

## Inherited notation and physical first definitions

| Symbols | First definitions and present role |
| --- | --- |
| a_g, normalized Hodge bracket, P(lambda), j_1,...,j_ell, ell, F(j), G(j) | Introduction; the original insertion product, normalization, factor count, factorial product and falling-cubic sum |
| g,n, Hodge bundle/classes, lambda_0/rank conventions, g_2, Bessel data and scalar b | Introduction; inherited without a new setup or unrelated aliases |
| psi, logarithmic kappa_a, ordinary B_k, ch_a | s02.2, especially `eq:s02:chern-definitions` and `eq:s02:grr`; ch_a has the 1/a! normalization |
| Graphs, flags f,f', MM_Gamma, xi_Gamma, Aut Gamma | s02.3; vertex product is used before the quotient |
| alpha, V_{G,n}, normalized WP descendants, F_g, Z_g(u), W^{WP}_{G,n}, f(t), S(u), q,p | s03; WP scale, factorial scale, deformation, vertex/endpoint functions, original unmarked core complexity and restored loops |
| w_ab, D, m_a, signed functional L | s04.1; the two endpoints of a loop share their parameter, and L is not probability |
| e_{n,r}(d) | s04.2 body definition and Appendix A.1; signed inverse-complexity coefficient. Only e_{n,1} is numerically used here |

Hodge-class indices stay in the j-family and ell remains their product
length. The source character degrees below are a_i, and descendant degrees
are d or the entries of a bold degree tuple. No new alias for pi^2 is used.
Chow coefficients remain inside parentheses.

## New notation, definition locations and scopes

| Notation | Definition label / location | Type, scope and reason |
| --- | --- | --- |
| r,a_i,w | Opening of s05.1 | Fixed source count r>=1, fixed odd a_i>=3, and total character degree w=sum a_i; used for the filtration |
| P_a in calligraphic font, P_a(x,y) | `eq:s05:node-polynomial` | Symmetric binary polynomial of degree a-1 for odd a>=3 and formal x,y. Distinct from the inherited one-variable pairing polynomial P_m |
| epsilon_i | Before `eq:s05:source-kernel` | Commuting square-free formal labels; different labels stay distinct even when their degrees agree |
| calligraphic E(x,y), K_E(x,y) | `eq:s05:source-kernel` | Local deformed boundary series and its formally divisible edge kernel, needed for multiple labels on one edge |
| I,J,C_k,A in calligraphic font | Source/forgetting formulas in s05.1 | Local source subsets, a set partition of the vertex subset, and its ordered list of blocks; m is its number of blocks, not a new global parameter |
| s_v,m,s | Proof of `lmm:s05:character-filtration` | Number of forgetting blocks at vertex v, their total m<=r, and number s<=r at the large vertex of a fixed original core |
| H | Counting paragraph of the same proof only | H=2g-2, as in s03's counting argument; it is not the flag set H(Gamma) |
| C,B,T,C_1,A | Majorant proof | Local bound constants and fixed nonnegative integer polynomial exponent A; no global quantities are named by them |
| T_g^{free},T_g^{edge} | Before `eq:s05:single-source` | Local single-label graph sums without the Bernoulli factor, separating the two contributions needed for ch_3 |
| G=g-p,n=2p,d | Free-marking paragraph of s05.2 | Large-vertex type on the pure-loop graph and new descendant degree d>=4; D and m_0 retain their inherited degree-statistic meanings |
| varphi(z) | Before `eq:s05:averaged-increment` | Entire z^4 f^(4)(alpha z), with complex degree variable z; tracks the full new degree without dividing by a zero leg factor |
| X_k | `eq:s05:endpoint-derivatives` | (8pi^2)^k f^(k)(alpha), k>=0; local endpoint derivative family for a recurrent finite calculation |

No new global notation or bibliography entry is requested.

## Results and exported identities

| Label | Export and hypotheses |
| --- | --- |
| `lmm:s05:labelled-sources`, `eq:s05:source-graphs` | Exact finite-genus integral identity for g>=2 and labeled odd degrees; general symmetric edge kernel, ordinary graph Aut factors, product of Bernoulli factors |
| `eq:s05:tagged-edge` | A nonempty label set J on an edge gives (-1)^(|J|-1)(x+y)^(|J|-1) exp(-alpha(x+y)) times the product of node polynomials; no label factorial |
| `eq:s05:free-markings` | Partition inversion creates one marking per block with degree 1+sum a_i and its surviving exp(-alpha psi); unordered inversion has no block factorials |
| `lmm:s05:character-filtration`, `eq:s05:character-bound` | Normalized product of r fixed odd characters of total degree w is O(g^(r-w)) |
| `eq:s05:source-majorant`, `eq:s05:source-tail` | Full original unmarked-graph majorant with polynomial loss r; no-large-vertex / q>=M absolute sum is O(F_g g^(r-M)), for every fixed M>=1 |
| `eq:s05:decorated-core-bound` | Fixed original core and source pattern with s free markings on its large vertex: all legal p bounded by F_g g^(s-q) C^(p+1)(1+p)^A/p! |
| `eq:s05:character-normalization` | Exact conversion of the exponential numerator to the normalized Hodge bracket, for 3g-3>=w |
| `crl:s05:algebraic-reduction`, `eq:s05:algebraic-reduction` | F(j)<P> = 1+2G(j)<ch_3>+O(g^-4) for the original fixed product |
| `lmm:s05:single-source`, `eq:s05:free-ratio`, `eq:s05:edge-ratio` | Free and edge ratios with sufficient summable errors; q=1 common leading terms cancel graph by graph |
| `eq:s05:one-mark-volume`, `eq:s05:profile-increment` | Actual one-new-mark volume/profile increments, including the factor 1/2 in converting signed e1 from inverse complexity to inverse genus |
| `eq:s05:averaged-increment`, `eq:s05:free-moment` | Signed loop and new-degree averaging, with the S(1) terms explicitly cancelling |
| `eq:s05:specified-loop-weight` | Specifying one restored self-loop gives p/(2^p p!)=1/[2*2^(p-1)(p-1)!]; branch exchange is counted once |
| `lmm:s05:endpoint-derivatives`, `eq:s05:derivative-recurrence` | Exact ODE recurrence and finite derivative table |
| `prp:s05:third-character`, `eq:s05:third-character` | <ch_3>=(2pi^2-21)/(9g^2)+2(pi^2-10)/(3g^3)+O(g^-4) |
| `eq:s05:factorial-three`, `eq:s05:free-coefficient`, `eq:s05:loop-coefficient` | Factorial 4/g correction, free contribution 29pi^2/45-20/3, and specified-loop contribution pi^2/45 |
| `subsec:s05:03` | Proof of `thm:fixed-insertions` and three short consistency examples |

There are six principal results in the section. The theorem proved in
s05.3 retains its Introduction label and number. Optional Remark/Example
modules use their independent counters.

## Source mapping and proof boundaries

- `ABCDGLW23`, Lemma 3.10, (3.18)--(3.21), with its normal-line proof
  continuing in (3.22): the general E boundary exponential. The source is
  in cohomology; `lmm:s05:labelled-sources` supplies the algebraic
  self-intersection/projection argument for the precise integral used here.
  Its weighted one-edge pushforward equals half our ordered-branch map;
  an extra half is not inserted into K_E.
- s02 `eq:s02:grr`, `eq:s02:lambda-one-grr`,
  `eq:s02:chern-exponential`, `eq:s02:lambda-two-three`: GRR is applied
  on the original unmarked parent, not repeated in marked form at the
  vertices. The existing Mum83/FP00 attribution is inherited.
- s02 `eq:s02:partition-inversion`, `lmm:s02:rational-tail-degree`:
  exact forgetting and background pullback in Chow. The KMZ96v1 credit
  and convention conversion remain at the original proofs.
- s03 `lmm:s03:vertex-bound`, `crl:s03:marked-extension` part (ii):
  uniform all-type/Cauchy and full graph-tail majorants. Their hypotheses
  are checked explicitly on the original unmarked graphs, using
  Gamma(k_v+s_v)/Gamma(k_v) and source-edge choices absorbed into T^E.
- s03 `prp:s03:core-expansion`, `lmm:s03:degree-moments`:
  after discarding all legal p>log g, the retained genera and valences
  satisfy the HMT thresholds. The fixed derivatives only add fixed
  degree moments, hence summable remainders.
- s03 `eq:s03:c-one` and `eq:s03:fixed-n-volume`: first volume input,
  derived and originally credited to Mirzakhani--Zograf. No c2 is used.
- Appendix A `eq:a:first-profile`, `eq:a:profile-genus-conversion`:
  explicit signed first profile, originally from Wang et al. and
  identified with HMT's uniform expansion. HMT supplies remainder
  control, not the original finite first-coefficient formula.
- s04 `lmm:s04:loop-moments`, `eq:s04:representative-moments`:
  normalized absolutely convergent signed loop sum. The additional
  elementary moment L[p]=S(1) follows directly from its existing EGF.

The lecture notes and independent preparation files are calculation
leads only, not manuscript citations, proof inputs or formal reviews.
No unverified external claim or source gap is left as an input.

## Review boundary

The proof consists of the full decorated graph bound, the two-term ch_3
calculation and the fixed-product Chern reduction. The fixed-list
scope and O(g^-4) remainder are unchanged; there is no growing-index
or higher-order assertion.

Historical author handoffs and build records preserve earlier evidence.
Live review, approval and freshness are recorded by the workflow rather
than an author-stage description in this scientific interface.
