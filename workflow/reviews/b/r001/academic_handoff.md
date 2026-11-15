# Appendix B r001 academic review

Reviewer: `/root/s02_academic`.
Snapshot: `b6e1aa092e2ee935c285035e01288f27afe0c885ce9ef9092bb35e4f90a20aff`.
Verdict: **changes_requested** for minor **ACADEMIC-008**; no prior B issues to resolve.

The complete entry, B.1--B.5, interface and writer handoff were reviewed against the frozen sources. B.2's opening calls the growing quantity an “inverse derivative.” Its hypothesis and estimates actually use the derivative scale of `w_theta`, while the inverse-function derivative is its reciprocal. Name the former explicitly in the two introductory sentences; the displayed formulas and proofs need no change for this issue.

Attribution, citation precision and claim status pass. The Section 6 critical/circle results and Section 7 finite-jet, characteristic and Borel-kernel exports are used within their verified scopes; the new domain, normal-convergence, endpoint and primitive estimates are proved in this appendix. The internal lecture notes are not substituted for primary literature. The four newly appended Section 8 sources are not inputs to B, and no new application of their theorems is approved here.

Independently read the primary [DLMF series (10.25.2)](https://dlmf.nist.gov/10.25.E2) and [integer-order integral (10.32.3)](https://dlmf.nist.gov/10.32.E3): the substitutions `order=k`, `argument=2 sqrt(u)`, integer `k>=0`, real `u>0`, match B.5 exactly. The release entry and printed DLMF label are accurate. The modified-Bessel inequalities are derived in the proof rather than assigned to an unverified locator.

The fixed-genus primitive and its uniform genus bound are distinct, with `G_(1,1)` explicitly excluded. Common analytic regions have a fixed finite layer cap, and the coefficient bound is not presented as an asymptotic-transfer theorem. The actual leading coefficients, their recurrence and constants, sine inversion and background comparison remain for Section 8; B does not claim Theorem 1.4. Necessary endpoint hypotheses precede use and all 16 principal statements have adjacent proofs. Native pages 28, 32, 34, 37, 39 and 40 were inspected: the longer proofs are dense but functionally grouped, with readable formulas and no intervening credit paragraphs.

The original reviewer binding and approved/fresh dependency chain were checked. All archived/live input and artifact hashes match the submission, the snapshot/source fingerprints recompute correctly, and the actual PDF/entry/helper hashes match the strict native receipt with empty standard/layout diagnostics. Only these two reports and private ignored page images were written; no source, shared file, state, historical record or frozen output was changed or rebuilt. Stop pending collection of all reviewers and revision by the original writer; retain this context for re-review.
