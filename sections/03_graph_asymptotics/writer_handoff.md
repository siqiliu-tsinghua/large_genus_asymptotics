# s03 writer handoff

Fixed original writer: `/root/s02_writer`, reused and bound to s03 by the
coordinator. This is the complete author submission of Section 3. Live
review/acceptance status belongs to `workflow/state.json`; no approval is
claimed here. The approved s02 dependency is r005 snapshot
`5634fa68be11f0aec6929967508aa7a9cb6b4140dddeba004534a06281f68f9d`.

## Scope and method

Only `sections/03_graph_asymptotics/` was written for this assignment:
the section entry, four subsection files, scientific interface and this
handoff. No Introduction/s02 source, shared macro, bibliography, workflow
state or frozen record was edited. Earlier ignored preparation notes are
under `build/s03-preparation/`; they are leads and cross-checks, not a
source citation or review signature.

The section proves a uniform analytic framework for the full boundary
deformation. It does not input or compute the target numerical second
coefficient of the pure Hodge asymptotic theorem. The main expansion is
additive, compact-uniform in complex parameters and valid at every fixed
order. All exchanges are justified by absolute graph sums or explicit
factorial/degree moments, not by a fixed-graph limit.

## Mathematical implementation

1. WP definitions inherit the Introduction's stack/Chow/codimension
   conventions and s02's logarithmic kappa. The factorial conversion to
   actual boundary lengths and the (1,1) whole-polynomial half-factor are
   explicit. The input proposition separates fixed-n coefficients,
   all-stable bounds and HMT uniform remainders. All HMT thresholds,
   coefficient bounds and the A3 inverse-ratio orientation are retained.
2. The graph deformation is exact at finite genus. Both flags of an edge
   share one unit-interval integration variable. The link to `a_g/N_g`
   uses s02 GRR and factorial conversion. The fixed-loop calculation is
   initially motivation only; its sum is justified later. The sine identity
   has its own complex variable; the Cin identity starts with real u>=0,
   and complex continuation is through the explicitly entire S function.
3. The global ABSOLUTE graph tail is proved inside 3.3. It retains the
   valence cap, exact groupoid labelling (including repeated types),
   square-root cancellation and Gaussian density. The short factorial
   series has all three interval estimates, with constants fixed before
   shrinking the Gaussian cutoff. The large-Gaussian, no-large-vertex
   and both q-tail cases are present; no future Appendix is assumed.
4. Core means contraction of every large-vertex loop with genus increase,
   not edge deletion at unchanged genus. The genus/valence bookkeeping,
   finite core types and `2^p*p!` automorphism factor are proved. All legal
   loop counts, including small vertex genus, are controlled before HMT.
5. The core volume path starts at (g,0), makes c+p genus exchanges, then
   removes q markings at fixed genus. Every intermediate marking count is
   nonnegative, and the exact gamma scale is independent of p. A common
   sufficient threshold is checked against the actual HMT thresholds.
   Finite-product errors are polynomial in p; direct descendant moments
   preserve that dependence under summation. The final per-p error has a
   factorial denominator and no substituted logarithmic loss.
6. Entire `gamma_k(u)` functions are constructed from finitely many core
   types and normally convergent loop sums. The leading coefficient is
   `exp(S(u))`; fixed Cauchy derivatives preserve the remainder order.
7. The fixed-r external-labelled-leg extension is additive, normalized by
   `V_g,r`, with leading `e^S prod f(t_i)`. Its count differentiates the
   truncated exponential, absorbs vertex allocation into a constant per
   vertex, and loses g^r only when its factorial scale is changed to F_g.
   The marked core relation is `q=2c+r-n0`, with n0 including external
   legs, and the ratio path starts at (g,r). No division by `f(alpha)=0`
   occurs. Further contributions receive only a weighted-tail conclusion
   under the displayed uniform positive-majorant condition, with explicit
   loss `g^(r+s-M)`; arbitrary decorations are not asserted to qualify.

The independent math preparation and academic source preparation were read
before drafting. Coordinator prechecks corrected a double-marking constant,
bound-index scopes, the distinction between finite positive length sums
and infinite majorants, integral typography and explicit bound-index ranges. Real boundary
lengths were changed from the outline's L_i to y_i to preserve the
inherited cotangent line-bundle name L_i; this change is confined to s03.
These were author-side
preflight corrections, not invented formal reviewer issues.

## Source rationale

The exact source/translation ledger is in INTERFACE.md. Its key points are:

- Wol86 Section 5.1, printed p.138 / PDF p.21, gives the unmarked WP class;
  MZ15 Section 2 supplies the marked/logarithmic normalization. Mir07
  Theorem 4.4 p.14 and p.4's elliptic-involution discussion supply the
  boundary-length polynomial conventions. The isolated short-factor
  inconsistencies in the classics were not copied into the manuscript.
- MZ15 Theorem 1.2 and Remark 1.3 give the fixed-n expansion and c1(n).
  LX26 Corollary 1.2 fixes its absolute constant, with W26 Corollary 1.2
  cited as an independent determination. No unsupported higher-order
  unmarked claim is borrowed from LX26.
- SW25 Lemmas 14 and 18 and W26 Lemma 6.1 provide separate real-value,
  all-type and coefficientwise inputs. The W26 profile/bracket common
  factor is stated in the proof.
- HMT25 Theorem 4.2 really gives every fixed order. Its A1 majorant is
  rewritten by total degree, preserving the original coefficients and
  threshold; A3 retains its factor 500. The subsequent loop/graph summation
  is proved here, not credited as part of the source theorem.

All seven bibliography keys were supplied by the coordinator before this
assignment. There is no pending shared-source or macro request.

## Honest downstream boundary

Section 4 still has to reconstruct the actual second multidegree descendant
and diagonal terms, q=1 first corrections, q=2 leading contributions and the
second absolute base-volume coefficient. The old table is not a proof.
W26's fixed-marking coefficients, including low-degree exceptions, must be
identified with the unique HMT coefficients before HMT's growing-valence
uniformity is applied. This requirement is recorded in the interface.
Section 5 must check its concrete GRR edge/vertex insertions against the
stated majorant; s02's positive-new-psi hypothesis and negative new-psi
background correction remain unchanged.

## Validation and handoff

The final checks run after every assigned file is saved: repository
validation, the s03 draft gate, native strict build with dependencies,
and a separate label-free writer-draft build. The latter changes only
the generated entry's showkeys option and copies products/receipt/helper
to the new ignored directory `build/reviews/s03/writer-draft/`.
It records actual source hashes and writer-draft status, without claiming
a formal frozen-snapshot signature. Overfull horizontal/vertical boxes
are checked separately; representative dense pages are inspected visually.
Actual results and source hashes are reported to the coordinator with the
saved receipts. UTF-8/LF, final newlines, unique labels, proof adjacency,
bound-variable cleanup and protected-dependency bytes are also checked.

Preflight validation and the s03 draft gate passed. Static checks found
54 unique section labels, 37 numbered equations and 12 principal
statements immediately followed by proofs, with balanced environments
and unchanged s02 dependency TeX/interface bytes. The label-free draft
has 32 pages with dependencies and references, and its log has no
overfull horizontal or vertical boxes. Representative pages 16, 23,
27, 29 and 30 were inspected for the input bounds, graph-tail cases,
finite-product proof and marked corollary. The final strict builds
are rerun after this saved handoff and the real-length/range cleanup,
so their receipts bind the completed source.

At handoff the writer stops editing so the coordinator can freeze one
complete s03 snapshot for the original three independent reviewers.

## USER-005 opening revision

Feedback: `workflow/feedback/s03/USER-005.json`; SHA-256: `86ebc7b9672da44a277d5310ad7d44ad2684cc7d6e4490d88a173406cae5d321`. The opening now links s02's exact graph/GRR/degree identities to the uniform graph estimates, explains loop resummation, guides all four subsections, and identifies the later proofs of Theorems 1.1 and 1.2. Only the opening and this note change; subsection proofs, interface, assembly lines and protected sources remain unchanged from accepted r001. Scope and UTF-8/LF checks are performed; the coordinator handles the new builds, freeze and original-reviewer recheck.

## Shared-input refresh after s02 r006

The settled Appendix A/s04 inputs add EGGLS24, future context conventions and TikZ; s02 r006 changes only shared-input/provenance metadata, with its mathematical text unchanged. The s03 interface now records dependency snapshot `a524bfee025c0acb201e25ededbc067ee5141474253c98c2d6e5c0aeecb8df91`; its scientific exports are unchanged, and every s03 TeX file remains byte-identical to approved r002. Old records are immutable; the coordinator handles the new freeze and original-reviewer delta signatures.
