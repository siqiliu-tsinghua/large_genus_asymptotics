# Section 7 final-polish original-writer handoff

Actual agent: /root/s02_writer. Unit: s07. Dispatch:
build/final-polish-20261116/rounds/s07-r009-writer-dispatch.log.
The user-designated Git baseline is fa2f374. The preceding approved
round is r008, snapshot
177e20fca56d71169c4115815153e2bcc8a53954187f725ce0144c35c96a27c9.
This is an author delivery; live review and acceptance remain workflow
matters rather than claims made by this handoff.

## Full final reading

I read the entry, all four subsections, interface, current section
outline and editorial language policy. The original writer binding and
fresh s01/s02/s06 dependencies were checked read-only, with the retained
source context and the current Section 6 exports.

- The entry already distinguishes the exact fixed-defect equations
  from the later analytic proof and gives a precise roadmap. Its whole
  source is retained.
- In 7.1, Buryak's source parameters, the genus/defect reindexing, sine
  operator, Bernoulli normalization, top-sector cancellation and raw
  string anomaly are explicit. The source locators and the entire
  subsection are retained. The string identity remains a main lemma
  immediately followed by its geometric proof.
- In 7.2, only ordinary labeled spelling changes. The formal
  specialization, its finiteness argument, forgetting identity and
  local inverse-germ scope are unchanged; no common global inverse
  domain is asserted here.
- In 7.3, the introductory finite-times statement now explicitly says
  each fixed genus and positive defect. Paragraphs distinguish the
  genus-one initial value from its dilaton resummation, the jet-kernel
  calculation from the zero integration constant, and the construction
  of a branch for all sigma from the integrable decay estimate.
  Every word and mathematical expression inside those proof paragraphs
  is unchanged. Exact transport and characteristic recovery retain
  their separate statements, adjacent proofs, fixed inverse branch,
  real parameter range and differentiate-before-evaluation rule.
- In 7.4, a paragraph break separates the coefficientwise first-layer
  identity from its local normal-convergence statement. The factorial
  normalization, removed linear shift, two Beta integrals, full
  reindexing, parity and degree statements and finite-output-coefficient
  interpretation are retained without new analytic claims.

No symbol is added or renamed. In particular x remains the zero time,
z the formal genus variable, z_{0,1} the inherited Bessel zero, and
ordinary B_n the Bernoulli family. The distinction between beta_g,
the integral b_g and scalar b is unchanged. This branch uses no WP
coefficient or retired Appendix C datum.

## Interface and source protection

INTERFACE is now phrased as a scientific interface rather than an
initial author draft. Earlier snapshot IDs remain historical provenance;
live dependency status belongs to the workflow. The analytic boundary
now identifies the subsequent work in Section 8 and Appendix B without
turning it into an input or an extra export of this unit.

All inline/displayed mathematics, principal statements, labels, citations,
derivative orders, integration ranges and proof adjacency are protected
against fa2f374. The original writer_handoff and frozen archives remain
untouched. No shared source, state or scientific program is edited or
rerun, and no new primary source or notation is requested.

## Native reading and validation boundary

Ran python -B build/layout-20261115/snapshot_pdf.py s07. The native
10pt/no-showkeys preflight has empty standard and overfull diagnostics.
Actually viewed pages 21--28, including all nine proof endings on
pages 22, 23 and 25--28. Every closing square is at the normal right
end, and the finite-jet, exact-transport, characteristic and Borel-kernel
formulas and revised paragraph transitions are clear. No global font,
spacing or diagnostic setting is changed.

The final saved-source receipt is
build/reviews/s07/format-preflight/build_receipt.json, with snapshot
null. Rendered page evidence is under
build/final-polish-20261116/s07-r009-writer/. After saving this handoff
and the external ACK, the final native build binds the saved source;
the final render is checked against the inspected pages. Static draft,
scope, formula and UTF-8/LF guards accompany delivery. This validation
does not replace the new frozen review or claim an integrated final
manuscript approval. STOP.
