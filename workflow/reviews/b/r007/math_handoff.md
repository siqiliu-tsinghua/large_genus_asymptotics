# Appendix B r007 mathematical handoff

Reviewer: `/root/s02_math`; role: math; round: 7.
Snapshot: `dbed0d5232b62278eb66a7283588f6f691fc3702bc4fe36343eb23d2a52039ed`.
Verdict: **pass**. No open mathematical issue; `issues=[]`, `resolved_issue_ids=[]`.

I read the frozen entry, all five subsections and interface, compared the
precise B.2/B.3 changes and original-writer ACK, and checked the current
S1/S2/S6/S7 interfaces and needed exact kernel formulas. The original
independent mathematical checks remain applicable after this full reading.
The wording changes separate functional proof stages, name the local
continuations, and shorten the quadratic proof's final Cauchy sentence;
they remove no hypothesis, operator, estimate or inference.

The main points checked were:

- **Geometry:** the positive-center derivative argument and segment
  injectivity establish univalence on the closed disk, while a separate
  difference-quotient and compact-margin argument proves the full image
  radius and unique critical contact. The two-distance cones retain an
  angular margin under kernel shifts and the full characteristic-distance
  identity. Forward and reciprocal inverse derivatives remain distinct.
- **Analytic construction:** the B.2 induction first constructs normally
  convergent Borel functions, using the all-sigma integrable majorant and
  the intact cubic shift's summable m^-2 bound. Coefficient extraction
  follows that construction. The remote proof requires no large-parameter
  critical branch.
- **Endpoints and domains:** the sole principal square-root contribution
  is the correctly signed m=1 branch; the quadratic corners are separately
  integrable and give no square-root term. B.4's frozen model produces
  S H_1/(x_{*,theta}-v), with additive numerator errors, including zero
  coefficients. Its intermediate and vanishing-order ranges close the
  estimate. The final two B.4 proof paragraphs supply the compact-center/
  critical-cone patching and complex-theta parameter neighborhoods;
  larger-domain value bounds regenerate fixed mixed derivatives. All
  domain reductions are finite for fixed H.
- **Primitive:** the finite jet formula proves the zero value at negative
  infinity for g>=2; the genus-one logarithm is explicitly excluded.
  The Fourier estimate accounts for both endpoint neighborhoods. The
  near-zero integral gives N^-5/2, and the compact and growing negative
  intervals have a strict exponential radius advantage. No positivity of
  transformed coefficients or retired-C low-genus data is needed.

All 35 numbered equation blocks, 16 principal statements, 16 proof
wrappers, 30 bracket displays, 549 inline expressions, 57 labels and
one citation are preserved against r006 and fa2f374. The full analytic
arguments remain in the paper, with no program or engineering attachment
needed to fill a proof. This appendix supplies analytic tools rather than
asserting Theorem 1.4 or a stronger/growing-defect remainder.

## Current binding and artifacts

Read-only workflow status confirms the actual math binding and approved,
live-hash-fresh S1 r007, S2 r017, S6 r012 and S7 r009 dependencies. All
57 selected inputs match both archive and live hashes; the canonical
snapshot and submission artifacts match. The selected-input delta from
r006 is 21 changed entries (including the outline), five new final-polish
handoffs and no removals; inherited revisions were separately approved.

- Source SHA256: `c522640dbae94855e21e8c32623ded0cedc8769b07bf45171de88363bbbc7654`.
- Native PDF SHA256: `16ac591ac4ef002d5ab53fef23528f0252d253400445b4eb66c54a1712c5e07d`.
- Original-writer ACK SHA256: `9cb864f68d2d75bf7542c0242effe06cf2557878c1d34906411272558ef84aae`.

Current and preserved preflight receipts agree on actual source, PDF,
entry and helper hashes; strict build passed, no showkeys, and standard
and layout diagnostics are empty. The receipt transparently records
pre-submit compilation and post-submit sealing after equal fingerprints.
The native text contains the reviewed appendix results. No formal output
was rebuilt or changed.

Only this round's math.json and this handoff were written. No source,
state, historical report or other role record was edited. No unchanged
scientific program was rerun. Future full-manuscript/export/isolated-build
approval is outside this signature. STOP.
