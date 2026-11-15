# FORMAT-001 implementation note

The user's live document class is now a4paper,10pt. The showkeys package is removed entirely from the live preamble; historical frozen sources/helpers are preserved. The local TeX Live article.cls bibliography hook (thebibliography, lines 565-585) supports setting itemindent to the original label margin and then leftmargin to zero before list setup. This retains alpha labels on the first line while continuation lines use the full width, without a new package or a copied bibliography environment.

The 10pt article default also reduces textwidth from the previous 390pt to 345pt. The final preamble explicitly sets 390pt and centers it on paperwidth, retaining the prior physical horizontal text block. Emergency stretch of 3em gives long inline-mathematics paragraphs a fallback in line breaking; it does not enlarge the text block or suppress overfull diagnostics. No formula, source entry, mathematical macro or theorem hypothesis is changed.

A full-layout preflight compiled the captured prior accepted assembly in an ignored temporary entry, without modifying the generated sections/included.tex or pretending stale units were approved. Its receipt is build/layout-20261115/preflight/build_receipt.json. It records actual font size 10, no loaded showkeys.sty, empty standard/layout diagnostics, and all rendered inputs fingerprinted before/after. This is an unapproved layout check, not new role signatures. The original-role refreshes and separate Section 6 roadmap revision follow.

Final shared hashes:

- main.tex: `aaadac5ce1fc36a5194727abc1bf779a6289826b6f0c7eb7babf8ff5a549a76f`
- tex/preamble.tex: `79f6624fd2f06162a58aecd319d824f6d59d1cdb4e06c66cccff17a80fe87c28`
