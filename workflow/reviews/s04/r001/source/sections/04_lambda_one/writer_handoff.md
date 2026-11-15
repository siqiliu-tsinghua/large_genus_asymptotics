# Section 4 author handoff

Original writer: `/root/s02_writer`. Unit: `s04`, complete author submission.
Live workflow and review status belongs to the coordinator and
`workflow/state.json`; this handoff is not an approval.

Only `sections/04_lambda_one/` is edited. The four existing subsection
files, entry roadmap and scientific interface are complete. No accepted
dependency, shared file, calculation script, state or old record is changed.
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

## Validation and frozen-review boundary

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
