# Section 4 author handoff

Original writer: `/root/s02_writer`. Unit: `s04`, complete author submission.
Live workflow and review status belongs to the coordinator and
`workflow/state.json`; this handoff is not an approval.

Only `sections/04_lambda_one/` is edited. The four existing subsection
files, entry roadmap and scientific interface are complete. No accepted
dependency, shared file, accepted calculation script, state or old record
is changed.
The accepted inputs are s03 r003 snapshot
`5dea38f471fe1170933c94c84ef50f5741165dd9b682d3043d547428d4949353`
and Appendix a r002 snapshot
`8acf608e11a2785097d597d223aa07215b3ddc1aeb06ba2e713a43ba1d786bdf`.

## Proof organization and notation

The opening connects the exact graph/normalization identities and s03's
uniform finite-core expansion to the coefficient calculation. Section 4.1
provides the physical first definitions of w_ab, low-degree counts and the
normalized signed loop functional, then proves its entire joint EGF and
derives two representative moments. Both loop endpoints share one edge
variable and their correlations remain in the square; no probability
interpretation or positive replacement is used.

Section 4.2 first defines the signed profile coefficients in inverse vertex
complexity, including empty tuples, and supplies the explicit first profile.
It separates the volume and descendant corrections, displays their loop
averages, and integrates the complete three q=1 cores with diagrams and
Aut=1,6,2. The sum is 9/8 after extracting exp(S(1))/sqrt(pi). The raw
elliptic connector integral has no loop-half factor.

Section 4.3 defines Q_{q,r} as ABSOLUTE Z/F coefficients, with q+r the
inverse-genus order. It displays the actual q=0 second product and q=1
first-correction polynomial before referencing the accepted finite proofs.
The q=2 types and 13-row appendix enumeration are explained, with a worked
rational four-valent example whose shared small-loop variable produces
-1+4/pi^2. The rational, pi^-2 and pi^-4 sums are shown explicitly. A short
normalization remark distinguishes these Q groups from relative gamma.

Section 4.4 proves Theorem 1.1 with M=3 for the full absolute graph tail
and K=2-q for each retained core. All legal large-loop tails are removed
before invoking the large-genus expansions; polynomial/factorial majorants
then extend the coefficient sums to all p. Multiplication by the absolute
WP expansion preserves the summed O(g^-3) error. The final step uses the
exact a_g/N_g=Z_g(1)/F_g identity and S(1)=Cin(2pi).

The interface records scopes and exact sources. There is no E_1 alias or
new name for pi^2, positive count, or the WP leading constant. Source prose
uses Wang et al./actual citations. The absolute c2 is supplied by the
accepted unconditional recursion proof, using the third-order genus match;
the conditional EGGLS prediction remains credit/comparison only. No new
shared input or citation is requested, and no source gap is left open.

## Original submission validation and frozen-review boundary

The native strict build, static validation, draft gate and separate clean
writer-draft rendering are run against the final saved sources. The clean
artifact is an unfrozen author aid with stage `writer_draft`, snapshot null
and the actual saved-source hash; it is not a formal r001 signature. Final
outcomes and receipt paths are supplied in the coordinator handoff message.
The representative joint-generator, correction, small-graph and final-proof
pages are inspected for mathematical typography and overflow. Once those
checks finish the writer stops editing for a frozen three-role review.

The dependency-freshness check, `Engine().validate_draft('s04')` and
`python scripts/validate.py --unit s04` pass. The native strict build
with dependencies and the separate clean helper
`build/reviews/s04/writer-draft/build_clean.py` pass with empty diagnostic
arrays and no overfull horizontal or vertical boxes. All seven unit files
pass UTF-8/no-BOM/LF/final-newline/trailing-whitespace checks. The unit has
15 numbered equation labels, three principal statements and the named
proof of the original Theorem 1.1. All Section 4 body pages, including the
joint generator, the three core diagrams, both correction mechanisms and
the final proof, were rendered and visually inspected. The final saved
source hash is bound by both current build receipts and reported in the
handoff message; it is not a formal snapshot. The accepted finite
algorithms were used through their proved appendix statements and were
not rerun without a changed computational input.

## USER-006 response: one supplementary Remark

Feedback: `workflow/feedback/s04/USER-006.json`, SHA256
`3aa8bcc06f1b167fa4ad9110efacf0b014a5f7c5bcb8203d7adb73b6f2b279fe`.
The accepted baseline is s04 r001 snapshot
`4e6231907bb5784de1905d6c162f5a72c2e8ac815e689e456ef9d3080d8b0050`.

Relative to the accepted baseline, only `04_proof.tex`, `INTERFACE.md`,
this current handoff and the new `checks/` archive change.
The paper addition is the short post-proof Remark
`rmk:s04:further-coefficients`: it specifies the normalization, reports
the supplied g^-3 and g^-4 coefficients, says that the same finite-core
method continues, and explicitly omits the calculation details. It adds
no coefficient alias or numbered equation and does not repeat the lower
orders. The original proof, all 15 numbered equations, three principal
statements, remaining section sources, Introduction, Appendix A and shared
inputs are preserved.

The interface separately marks these as supplementary reported
coefficients with omitted derivation, unused in the original proof.
Both coefficients have now been independently computed and match the
supplied expressions exactly: current records are
`build/s04-higher-check/math/third_verified.json` and
`build/s04-higher-check/root/fourth_verified.json`. Neither proposed
higher Hodge coefficient enters the calculation; the exact target
comparisons occur only after reconstruction and composition.

The writer's finite engine reconstructs complete signed profiles e3/e4
from exact lower-order increments, with 180/591 expanded terms and actual
low-degree cuts 3/5. It verifies all safe low modes, the generic increment
and its boundary, normalizes zero tuples, reproduces the full known e1/e2
and passes 72 early-specialization checks. The cusp/genus compatibility
identity through order four and the previously computed fourth-order
ratio rows also agree exactly. The absolute c3/c4 are independently
identified by exact adjacent/dilaton/genus extraction, including the
extra fifth-order one-positive data for c4; the new finite core counts
are 61 and 272. No proposed higher Hodge value is fitted or used as input.

The complete composition and independent fifth-order source guards now
pass. The coordinator then actually reran the complete archived bundle
from `checks/run.py`; all stages passed, followed by a passing
`--verify-existing` check. The archive contains only the driver, exact
source mirrors, README and compact `verification.json`. Algorithm files
are byte-identical to the successfully executed copies. The versioned
record preserves 24 source fingerprints, both exact coefficients and
decimals, all absolute group values, and repository-relative output
paths/hashes. No generated profiles, packages or bytecode enter the unit.

Full execution receipt:
`build/s04-higher-check/verification_receipt.json`.
Complete coefficient output:
`build/s04-higher-check/math/computed_coefficients.json`, SHA256
`016c81cae9321dcff101c1352cb94fcd3d3fd686a93771a294ca97d8469d3ae8`.
Both post-reconstruction differences are exactly zero. The preparation
checks of the known lower profiles and early specializations are
separate from the default bundle run, which preserves the approved
lower profiles while reconstructing the new orders.

The paper's numerical values require no correction. Its higher
calculation details remain explicitly omitted at the user's request,
and the Introduction/Theorem 1.1 retain their accepted precision.
The original proof and all prior numbered equations/statements remain
byte-identical. A new frozen review is the coordinator's next step;
these calculation records do not claim its outcome.

Final saved-source checks use the unit draft gate, static validation,
native strict build with dependencies, and a separate label-free helper
at `build/reviews/s04/user006-final/build_clean.py`. Its receipt is
`build/reviews/s04/user006-final/build_receipt.json`; the native receipt
is `build/previews/s04/build_receipt.json`. The clean artifact has stage
`writer_draft`, snapshot null and the actual saved-source hash. The
final check outcomes, visual inspection and hash are supplied in the
handoff message. Frozen review artifacts are untouched.
