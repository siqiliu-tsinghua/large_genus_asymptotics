# Section 6 author handoff

Original writer: `/root/s02_writer`. Unit s06, complete author draft.
Only the four existing subsection sources, section entry, INTERFACE and
this handoff in `sections/06_top_hodge/` are edited. Live workflow status
belongs to the coordinator and `workflow/state.json`; no review signature
is conferred by this submission.

The approved geometric dependency is s02 r009 snapshot
`33ec1495090af03c99be89a5f5b272437f6d2792aaabb075bc9d4831c3cb2084`,
with s01 inherited. There is no WP/Section 3--5/Appendix A proof input.
The target `thm:top-hodge` / `eq:g111`, g_2, z_(0,1), rho and scalar b
are preserved. No shared notation, package or bibliography edit is needed.

## Actual proof chain

6.1 defines beta_0=1 and beta_G by the stable one-point integral for G>=1.
FP03 supplies the multipoint theorem in its precise marked range and the
stable genus-zero formula; FP00 supplies the one-point series. The zeta
function is explicitly defined before its use, and its series gives both
beta asymptotics and uniform small/large-genus comparisons.

The exact vertex calculation starts from the entire kappa exponential,
not the Section 5 background-pullback calculation. Each new point has
psi*(1-exp(-psi)), whose descendant series is x*(1-Phi). Summing the
coefficientwise finite (m+k)!/k! series yields m!*Phi^(-m-1). The unmarked
G>=2,k=0 term is zero by degree; every nonzero positive-genus term has a
marking, so FP03 is never applied literally at N=0. The reduction to
stable genus zero is numerical. The classical inverse Remark makes the
KMZ/MaZ raw-power normalization explicit without a new coefficient family.

6.2 defines the positive critical argument x_* and critical value R=rho/12.
The J_1 product and interlacing put every zero of Phi beyond the critical
disk. A single product factor strengthens the minimum-modulus inequality
to a strict Gaussian bound around the entire circle. Cauchy plus a fixed
bound on each J_0 factor gives m!/sqrt(m+1) uniformly in every stable
vertex type, including rational and elliptic types and m=0.

6.3 derives the original 1/Aut tree formula from s02's top-class pullback
and boundary exponential. Sum m_v=g_2-E limits the edge count. Only after
the uniform beta and vertex bounds are applied are parity/stability
restrictions dropped in a positive composition sum. Rooted plane shapes
cost at most 4^E, repeated factorial convolution costs at most 3^E, and
the product of m_v+1 is at least their total plus one. The resulting
edge-mass bound controls every genus/valence assignment. The exact
square-root ratio is at most sqrt(E+1), so the complete E>=K tail sums to
O_K(T_g g_2^-K) over its full legal range.

For a one-edge nonelliptic split the endpoint order is 2G-2>=2, not three.
The inverse-binomial convolution begins at two and is O(M^-2); its extra
1/g_2 gives relative O(g_2^-3). The stronger O(g_2^-4) in the lecture is
not claimed. The exact genus-two example checks beta_1, beta_2, the
identical-elliptic half and b_2=1/5760.

6.4 writes the actual Cauchy integral with P analytic on a neighborhood
of the CLOSED critical disk. Its leading-amplitude statement is additive,
uniform for bounded fixed-neighborhood families, and valid at P(x_*)=0.
For P=1 the proof splits at |theta|=m^(-2/5), expands the log phase through
five and amplitude through three, and defines Q_1,Q_2,Q_3 before their
use in the Taylor product. Both m^-1/2 and m^-3/2 polynomials are explicitly
odd; their symmetric Gaussian integrals vanish. The remaining error is
m^-2 times an integrable polynomial/Gaussian. The first correction is
-1/4+1/(24x_*)=-1/4+1/(6z_(0,1)^2).

The elliptic leaf uses its exact 1/24 value, cancels the ordered split's
half through two placements, and integrates J_0 to Phi. P=Phi needs only
the additive leading saddle, giving pi^2 J_1(z_(0,1))^2/(6g_2). The full
E>=2 and nonelliptic tails have sufficient relative errors. Restoring
b_g=g_2!*12^(-g_2) times the exponential integral gives (g_2!)^2, and
12R=rho together with beta_g restores the exact Introduction formula.

## Source and calculation evidence

The primary-source audit and writing task are archived outside the unit:
- `workflow/feedback/s06/TASK-001.json`, SHA256 `2de2f28f6f5f675daeb4985c9c2449e374f90dc467520b587a058e55c1c0d004`.
- `workflow/feedback/s06/writing_brief.md`, SHA256 `a5dddd8a0be556c8cec5aa8bc10a9374b8120879ddfe384395c710135ca61698`.
- `workflow/feedback/s06/primary_source_audit.md`, SHA256 `08097a1fb0df8a0f30015b5bf7ea3e2f32cbd6d6e829237f6a55ab158c0015cb`.

The archived brief/audit were checked byte-identical to the assigned build
copies. Their inputs are traced with precise source locators in INTERFACE.
The production DLMF key retains BIB-002's protection; no preparation entry
was copied over shared bibliography. The MaZ printed argument sign and
FP03 PDF header discrepancy are recorded as source cautions, not imported
into the mathematical argument or metadata.

The coordinator's root_math_check and exact_saddle_check and the original
math reviewer's independent preparation corroborate finite constants but
are not sources or pass signatures for this draft. The writer additionally
executed exact symbolic checks of the fifth phase term, third amplitude
term, full Q_1/Q_2/Q_3 product and both odd parities. The numerical checks
are not used to establish the analytic remainder or the full tree sum;
those arguments are supplied in the text.

## Validation and handoff boundary

Final author checks are the draft gate, dependency freshness, static
validation, local labels/statement adjacency, UTF-8/no-BOM/LF/final newline
and whitespace checks, followed by one native strict build with dependencies.
The actual outcomes, source hash and receipt path are reported in the final
handoff message. The coordinator will inspect the clean PDF and freeze a
single snapshot for the original three reviewers. No formal review artifact
is overwritten and no workflow state is changed by the writer. The writer
then stops editing and retains the original context for revision.

## Native preflight note

The first native strict attempt requested another label pass and showed
three local overfull boxes. The complex-vector binding, subsection
headings and Taylor-stage run-in were shortened or reflowed.
No formula, hypothesis, result, source locator or label was changed.
The final unchanged-source native rerun supplies the actual build outcome
and receipt reported at handoff; the clean PDF is left to the coordinator.

## Formal r001 revision: ACADEMIC-005 and ACADEMIC-006

All three r001 reports were read at snapshot
`cfb093e818c9075659e789f7d65fccdeecf64e662a39eb24f7f449f0e491257b`.
After the beta_G definition, one short sentence now maps FP00's b_G to
beta_G, with the existing genus-zero convention retained. Both MaZ
locators now say Proof 6.3, keeping Section 6 and (17) where present.
INTERFACE records the body conversion location and numbered proof locator.
All 26 numbered formulas, nine principal statements, ten proof bodies and
labels remain byte-identical. No computation, build or literature search
is repeated. This author response awaits a new frozen recheck.

## FORMAT-001: Section 6 opening revision

Feedback: `workflow/feedback/shared/FORMAT-001.json`, SHA256
`6510ef40876c0fac89177d795cf2687fdb371f223bcf22b953126d93ab1fbedd`.
The separately authorized opening now starts by stating that this
section proves Theorem 1.3, followed by the tree-reduction idea and
concrete exact-vertex/circle-bound/full-tree-tail/saddle/leaf strategy.
A third short paragraph retains the fixed-defect purpose. The entry
label, title and four inputs remain unchanged, and no later-defined
Bessel symbol is used prematurely. INTERFACE records the roadmap
position and the current s02 r009 dependency above.

The four subsection sources match approved s06 r002 byte for byte;
all 26 numbered formulas, nine statements, ten proof bodies, hypotheses,
constants and labels are preserved. The user-feedback response is
`workflow/feedback/s06/FORMAT-001_writer_response.md`, SHA256
`04ef57378627954f0b493de0d59bfe127a66d3298125b1907541b516c67a962e`.
Only the entry, necessary interface/current handoff and that response
are edited. Final static outcomes are reported at handoff; no native
build, mathematical reconstruction or literature search is rerun.
The coordinator handles preflight, freeze and original-role recheck.
