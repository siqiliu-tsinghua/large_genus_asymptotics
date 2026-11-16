# Final integrated reading request

This is a coordination request, not a review signature. The existing
author-name-only signature and generic article format are retained at
the user's explicit request.

After the final Section 8 submission is frozen, the coordinator builds
one complete-manuscript companion in that actual round's native-review
directory. It includes the title, abstract, Sections 1--8, Appendices A--B
and bibliography. Retired Appendix C is excluded. All three original
reviewers must inspect this same companion and verify its receipt,
source fingerprint, unit snapshots and PDF hash before signing.

The ordinary Section 8 reports remain mandatory. In addition, each
original reviewer writes one independent integrated-review JSON file:

- `workflow/feedback/shared/FINAL-POLISH/final_math.json`
- `workflow/feedback/shared/FINAL-POLISH/final_readability.json`
- `workflow/feedback/shared/FINAL-POLISH/final_academic.json`

Each file records `role`, actual `agent_id`, `verdict`, Section 8
`snapshot`, complete `source_hash`, complete `snapshots` map, companion
`pdf` path and `pdf_sha256`, substantive `checks`, and `issues`. Copy
identifying fields from the verified actual receipt; reach the review
conclusion independently. A pass requires no unresolved issue. Describe
the actual full-manuscript reading and visual inspection in `checks`;
do not infer an inspection from a successful compiler exit.

Math reviews the four theorem statements against their full dependency
chains, both independent proof routes, hypotheses and parameter scopes,
normalization and whole-sum estimates, and the distinction between
proved conclusions, supplementary reported coefficients and the closing
fixed-defect-one conjecture. Earlier final-round reviews can support this
integrated assessment; unchanged technical calculations need not be
repeated.

Readability reviews the complete article's narrative and first-use
definitions in physical reading order, inherited notation without
redundant introductions, letter roles, forward references, subsection
and appendix transitions, proof endings, optional modules and figures,
tables and bibliography. Inspect the complete PDF/text and the relevant
actual pages, documenting the extent of visual inspection accurately.

Academic reviews full-article credit and versioned locators, source
convention translations and publication metadata, distinctions between
technical W26 v4 and broader W26v5 background, claim status and article
independence. Public data support only the explicitly identified
numerical evidence; no program or collaboration file completes a proof.

Reviewers may edit only their own current reports and handoffs and their
designated integrated-review file. The manuscript remains frozen. A new
issue in an earlier section returns through its original writer and
reviewers; it is not silently fixed during this reading. These signatures
approve the identified complete companion, not a future export. The
coordinator subsequently checks the standard build and isolated single
TeX against that approved companion, including exact PDF text and label
numbers.
