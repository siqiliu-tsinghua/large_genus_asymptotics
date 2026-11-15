# Section 5 author handoff

Original writer: `/root/s02_writer`. Unit: s05. This is a complete author
draft of the fixed-insertion theorem, not a reviewer signature. Only
`sections/05_fixed_insertions/` is edited. Live status is in
`workflow/state.json` and is controlled by the coordinator.

## Inputs and scope

The accepted dependencies are s03 r003 snapshot
`5dea38f471fe1170933c94c84ef50f5741165dd9b682d3043d547428d4949353`
and s04 r003 snapshot
`172195b1a31c1584895d46b98f3c7790c556bc27b4302993f8eac254d897fbb9`.
The unit uses the exact geometry, all-type graph controls, signed loop
functional and the accepted Appendix A first profile. It does not use
the explicit second coefficient of Theorem 1.1, its supplementary higher
coefficients, a general odd-character first correction, Schubert
insertions or a connected-difference result. No shared change is needed.

## Proof chain

The entry starts from lambda3=lambda1^3/6+2ch3 and explains why the
character filtration reduces the theorem to ch3. Subsection 5.1 first
proves a genuinely general labelled-source integral identity. Distinct
commuting square-free labels avoid an r! even when their character
degrees repeat. The edge kernel uses the full symmetric E and the
normal-line series, rather than the constant-edge statement alone.
The Bernoulli prefactors are written explicitly; for degree three the
prefactor is -1/720. A short post-proof Remark distinguishes the source's
cohomology formulation from the in-paper algebraic Chow calculation and
checks its weighted one-edge pushforward against half the ordered cover.

The source labels are divided between vertices and edges. Edge labels
produce a fixed polynomial times exp(-alpha(x+y)), with no residual
1/(x+y). Vertex labels are partition-inverted into forgetting blocks;
the block power is at least four and kills rational-tail pullback errors.
The background therefore retains exp(-alpha sum psi_new). The inverse
signs and lack of block factorials are explicit.

For the complete graph bound, the original unmarked graph is retained.
A vertex with s_v new markings has Gamma(k_v+s_v), whose ratio to its
original Gamma(k_v) is at most (k_v+r)^s_v. Summing assignments costs
O((2g-2)^r); specified-edge choices are polynomial in the edge count and
are absorbed into T^E, without a second loss of g^r. Cauchy on the
all-type vertex bound controls the finitely many inserted cotangent
powers uniformly in every stable type. This verifies the exact s03
majorant condition and gives the full tail O(F_g g^(r-M)).

For a fixed original core, only s free blocks on its large vertex return
powers of g: its ratio is Gamma(2g-2-q+s)/Gamma(2g-2), giving g^(s-q).
This all-type estimate is used for every legal restored loop count,
including small large-vertex genus. The factorial loop tail is discarded
before any HMT expansion is applied on p<=log g. Thus mixed character
products are O(g^(r-w)) after the exact factorial conversion. The finite
Chern-exponential expansion then leaves only 1+2G(j)<ch3> through g^-3.

Subsection 5.2 separately defines the free and edge sums for a single
source. M=2 makes the full discarded graph contribution O(F_g/g).
The q=1 large free-mark contribution is the same additive factor
8pi^2 g f^(4)(alpha) times that same core's denominator contribution,
including its Aut and all small-vertex integrals. It therefore cancels
core by core; small-vertex marks and specified edges on q=1 are already
in the error. No division by f(alpha), which is zero, is used.

The remaining free increment is actually computed: the one-new-mark
volume ratio comes from c1(n), while the signed first profile changes
by -[4Dd+2d^2+2D+(2n-3)d-n+2]/pi^2 for new degree d>=4.
The inverse-genus increment is half that expression. The new-degree
series z^4 f^(4)(alpha z), L[p]=S(1) and L[D]=-S(1) explicitly cancel
all S(1) terms. A specified self-loop has the single branch half
p/(2^p p!)=1/[2*2^(p-1)(p-1)!], giving -f'(alpha)^2/2.
After the factorial 4/g correction, the free g^-3 coefficient is
29pi^2/45-20/3 and the loop one is pi^2/45. The elementary derivative
ODE/table verifies both finite substitutions in the text. Their sum
gives <ch3>=(2pi^2-21)/(9g^2)+2(pi^2-10)/(3g^3)+O(g^-4).
The remainder includes full graph, all-legal-loop and descendant tails.

Subsection 5.3 substitutes this result into the algebraic reduction and
proves the original Theorem 1.2 formula. Three short examples check
indices at most two, a single lambda3, and two fixed classes. The six
principal statements are directly followed by their proofs. The new
symbols have local scopes and their full ledger is in INTERFACE.md.

## Sources and validation boundary

The only new direct literature application is ABCDGLW23 Lemma 3.10,
(3.18)--(3.21); its (3.22) supplies the same normal-line mechanism.
All other concrete geometry and first-order coefficients use their
accepted internal proofs and retained original source attribution.
No bibliography change is requested. The internal lecture and
preparation calculations are not cited as mathematical sources.
Independent source/math preparation corroborated the calculations but
is not a review of this manuscript and supplies no pass signature.

The coordinator requested a pause after completed drafting so that the
build and frozen snapshot can be prepared uniformly. The writer runs
only the final scope, label, UTF-8/LF, draft-gate and static validation
checks here; no build or mathematical review is claimed in this handoff.
Their actual outcomes and the saved-source hash are reported in the
handoff message. After that message the writer stops editing and remains
available for the original-role revision process.

## Preflight typography adjustment

The coordinator's first native build found legacy boldsymbol font-shape
warnings and five long paragraphs. The two occurrences of Q with a bold
cotangent argument are simplified to the already defined Q. Five local
passages in s05.1/s05.2 are reflowed; the specified-loop coefficient and
node polynomial now appear in an unnumbered display. No mathematical
content, coefficient, result, label, source locator or interface changes.
All six principal statements and all 25 numbered formulas are preserved,
with only the equivalent Q typography normalized for comparison. No
calculation is rerun. The coordinator will check the clean rendering
before freezing; the writer stops after this preflight correction.

## Formal r001 revision: READABILITY-001

Reviewed all three r001 reports for snapshot
`ccc9f748fa39b46bdc2f1e300b4e57e5037b9bbf0337e0301d634725bb49e7f0`.
Added only the two requested paragraph breaks in the common-q=1 stage:
after the small-vertex case and before the quotient-cancellation paragraph.
Every word, formula and label is preserved; whitespace-normalized s05.2
matches the frozen source. All 25 numbered formulas and six principal
statements are unchanged. No computation or build is rerun; the
coordinator will construct and freeze r002 for the original reviewers.
