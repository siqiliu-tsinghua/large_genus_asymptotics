# Standalone scholarly article: completed handoff

Completed 2026-11-16. The manuscript has been checked for internal
engineering references and the submission deliverable is now one TeX
source, submission/paper.tex. This record is internal, not part of the
article or its submission directory.

The Introduction no longer promises software/reproduction instructions.
Appendix A's calculation-directory paragraph and final engineering
Remark are removed. Appendix C is renamed Exact low-genus values;
the engineering C.2 and its input are deleted. Following the stated
default, the full mathematical C.1 is retained: its complete proposition,
table, three equations, proof and scholarly sources are byte-identical.
No engineering-absence or submission instructions replace the deletion.
The rest of the article offers no internal programs or Markdown as
reading/proof requirements. Mathematical finite recurrences and proper
literature/data credits remain. The LiuData26 URL now wraps cleanly.

Publication independence is documented in AGENTS/context and all
writer/reviewer roles. Internal checking programs and historical records
remain internal; they are neither promised nor copied into the delivery.
Old source archives, original handoffs and signed reports are preserved.

The retained original writer and three original reviewers performed the
real sequential refresh: s01 r004, s02 r015, s03 r012, a r012,
s04 r014, s05 r011, s06 r009, s07 r007, b r005, s08 r005, c r003.
All eleven units are approved and fresh with three actual registered
passes; no unit remains active. C r003 also covers the actual complete
101-page native manuscript. Those signatures cover the article content,
not the subsequent export's runtime test, which the coordinator actually
performed after acceptance.

The default strict XeLaTeX/BibTeX build passed, with no LaTeX/citation
warnings or overfull boxes. Global validation passed for 6278 text files,
11 units and 436 labels; git diff --check passed. The final source audit
preserves 108 previous inputs and 468 mathematical/statement/proof
blocks, all four theorem statements and every retained old label number.
Only the removed engineering subsection label subsec:c:02 disappears.
The default PDF text exactly matches the frozen reviewed full companion.

The new internal tools are scripts/export_tex.py and
scripts/verify_submission.py. The export inlines the preamble, abstract,
all sections, TikZ figures and the complete bibliography while retaining
TeX comment whitespace semantics. Export parser cases passed; the full
38-test suite and the later three focused cases passed. No old long
mathematical calculation was rerun.

The final delivery directory contains only paper.tex: 335610 bytes,
8079 lines, UTF-8 without BOM, LF and a final newline. Its SHA256 is
a5642b93706eb2c8532bfb5847e3448b07d51f86c07de5f6931b4dcf75a46ba7.
It was copied alone into a new temporary directory and actually compiled
with XeLaTeX and shell escape disabled. No project source, Python,
Markdown, BibTeX, bibliography file, private font or external figure was
needed. Each compiler pass's recorder was checked: all runtime inputs
belong to the temporary directory or standard TeX distribution. The
101-page result has text identical to the approved complete PDF and
exactly the same 436 label numbers, with no warnings or overfull boxes.

Current default PDF SHA256:
2772a58a1cc3d1ffb6e3dcfee8b527f7075505c9a1a62b0a2ba035aaaa060306.
Evidence is in build/export_receipt.json,
build/submission-check/verification.json and
build/standalone-20261116/final_audit.json. Repeatable internal author
commands after a future approved edit are:

    python -B scripts/build.py --strict
    python -B scripts/export_tex.py
    python -B scripts/verify_submission.py

The exported TeX itself requires only normal XeLaTeX compilation.
The exporter protects directly edited existing delivery files against
silent overwrite. No publication upload or Git commit was requested.
