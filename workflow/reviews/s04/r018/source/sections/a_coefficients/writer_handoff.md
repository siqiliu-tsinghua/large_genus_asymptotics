# Appendix A author handoff

Original writer: `/root/s02_writer`. Unit: `a`, complete author submission.
Live workflow status is controlled by the coordinator; this handoff is not
an approval or a review report. No other manuscript unit, shared input,
workflow state or old record was edited for this assignment.

## Mathematical implementation

The four subsection files contain the actual finite proof chain, not a
candidate-coefficient table. A.1 gives W26's complete second profile and
four exact symbolic pivot categories, then writes the exact MZ/HMT
recursions, kernel/dilaton moment table, retained loss-2/loss-3 components,
finite third-profile extraction, three ratio rows and adjacent-genus
matching. The MZ expansion is used through order THREE; unknown c3 cancels.
A factorial-convolution argument controls the entire omitted genus sum,
and polynomial HMT errors/exponential kernel/factorial dilaton tails
justify coefficient extraction. This reconstructs c2(0) without EGGLS as
an input and gives c2(n)-c2(0).

A.2 defines the absolutely convergent, normalized signed loop functional
and joint EGF, preserving each edge's common endpoint variable. Its finite
moment/Bell rules give the full q=0 second correction and all three q=1
first corrections, including a coefficient table that exposes cancellation
of powers of S(1). These are ABSOLUTE coefficients for Z/F, not s03 gamma
coefficients for Z/V. The final remark gives the exact conversion.

A.3 derives all four low vertex polynomials from raw psi string/dilaton
integrals and s02's inversion; the negative merged kappa term and complete
stack (1,1) normalization are explicit. A.4 proves enumeration completeness
and the literal graph automorphism rule before displaying all 1/3/13 small
graphs, edge matrices, genus losses and every integral/contribution row.
The second-order finite sums give 257/128+1/(8pi^2); the Section 4 Hodge
normalization argument remains outside this assignment.

The inherited science is s02 r006 snapshot
`a524bfee025c0acb201e25ededbc067ee5141474253c98c2d6e5c0aeecb8df91`
and s03 r003 snapshot
`5dea38f471fe1170933c94c84ef50f5741165dd9b682d3043d547428d4949353`.
The scientific interface records exact symbol scopes and source locations.
Local recursion mu/nu weights, calligraphic cusp/genus ratios and adjacent
difference avoid the established loop w_ab, Bernoulli B_n and Bessel J_n.
No new raw angle bracket or positive-count alias is introduced.

## Source and executable provenance

All necessary bibliography keys were settled before this assignment.
W26 Lemma 7.2/Appendix C.1 is translated at Y=0; its fixed-marking
coefficients are identified with HMT by uniqueness before summation.
MZ/HMT exact recursions, their actual expansions and SW factorial bounds
supply the unconditional proof. EGGLS24 (6.10) is credited only as a
conditional resurgent prediction and post-computation comparison. Hua25
is neither cited nor used. Mir07 supplies the length interpretation with
the already fixed stack elliptic adjustment.

`calculations/` contains self-contained production copies of the writer's
profile/moment/q1 algorithms, the coordinator's finite absolute-volume
reconstruction and independently organized original-math algorithms for
core flag enumeration and c2. They depend on no preparation file. The
README pins SymPy 1.14.0/mpmath 1.3.0 and gives workspace-local install/run
commands. Standard-library core enumeration works without either package.
Results are console/ignored build output; bytecode generation is disabled.
The manuscript finite formulas remain the proof, rather than a CAS run.

## Validation and review handoff

All seven calculation executables passed in the pinned local runtime,
including four symbolic pivot categories, 57 independently organized literal
profile increments, all 17 literal flag automorphism counts and enumeration
counts 1/3/13. The two independent volume algorithms agree on every ratio
row and the reconstructed c2(0). The auxiliary 25-case direct kernel check
has maximum absolute discrepancy below 4.1e-44; it is not proof input.

The draft gate and `python scripts/validate.py --unit a` pass. Native
`python scripts/build.py --unit a --with-deps --strict` and the independent
label-free helper `build/reviews/a/writer-draft/build_clean.py` pass without
LaTeX/citation/reference/font diagnostics. The clean log has no overfull
horizontal or vertical boxes. Representative profile, ratio, signed-moment,
q=1, core-diagram and integral-table pages were actually rendered and
visually inspected. Header spacing was added locally to the integral tables
without changing normal font sizes or global settings. UTF-8/LF/final-newline
and absence of unit bytecode files are checked for all 17 unit files.

Exact calculation checks, static validation, strict construction and a
separate label-free writer-draft rendering are recorded in the final
coordinator handoff message and ignored build receipts. The draft PDF is
an author aid, with stage `writer_draft` and snapshot null; formal freezing
and the three independent review signatures belong to the coordinator.
No formal review of Appendix A has yet been claimed. After the final
saved-source checks the writer stops editing pending that frozen review.

## Formal r001 revision

All seven registered issues are answered separately in
`workflow/reviews/a/r001/author_response.json`. MATH-001,
READABILITY-002 and ACADEMIC-003 are addressed by explicit raw connector
generators without the loop factor 1/2: the rational degree moments are
2 M_{0,r}, and the elliptic generator integrates W_11(t) f(xt), keeping
W_11 unscaled. The two zero-indicator integrals are stated separately.
The existing raw table and every q=1 numerical coefficient are retained.

MATH-002, READABILITY-001 and ACADEMIC-002 are addressed without a new
source alias: the already defined mu generating function explains the
source half-kernel, adjacent subtraction and factors 4/8/8, including
the initial coefficient 1/2. The undefined source a_l comparison is
removed and the interface source mapping is synchronized. ACADEMIC-004
is addressed by replacing all six bare source keys in manuscript prose
with Wang et al. or actual citations, retaining the precise locators.

Only A.1, A.2, this handoff and the interface are changed in the unit.
The entry, A.3, A.4, all 44 numbered equations, all ten
principal statements and every calculation source remain byte-identical.
Checks for this saved revision and its new label-free rendering are
reported in the final handoff and the ignored r002-writer-draft receipt.
The seven unchanged algorithms need no full rerun; the corrected raw
connector generators are checked directly against their exact table.
