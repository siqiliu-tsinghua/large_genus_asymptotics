# Pure Hodge integrals at large genus

This repository contains the manuscript and its section-by-section writing and review workflow.

## Manuscript layout

- main.tex assembles the manuscript.
- tex/preamble.tex holds shared packages, notation and theorem environments.
- frontmatter/abstract.tex contains the abstract.
- sections/ has one directory per section and one file per subsection.
- paper_outline.md maps the completed proof structure and current finalization scope.
- workflow/sections.json defines the units, dependencies and file order.
- workflow/state.json records assignments, submissions, reviews and acceptance.
- references.bib is the bibliography. Entries must be verified before use.

The abstract, Introduction, Sections 2--8 and Appendices A/B are complete and have passed the section review workflow. Current acceptance and freshness are reported by `python scripts/workflow.py status`. Reopening a section or changing a shared input requires a new review of the affected snapshots; existing approval does not cover later changes.

The generated assembly includes the continuous approved body prefix and available supporting appendices. Appendix C is retired and is excluded from the manuscript and export. Its sources and frozen reviews remain internal history; see workflow/RETIREMENT.md.

## Build and checks

Use Python 3.10 or newer and TeX Live with XeLaTeX and BibTeX on PATH.

    python scripts/build.py --strict
    python scripts/build.py --unit s02
    python scripts/validate.py
    python -m unittest discover -s tests -v

The build script runs at least two XeLaTeX passes; when citations require BibTeX, it also runs BibTeX and an additional XeLaTeX pass. All products go to build/. A unit preview uses its intended section number and the same preamble and bibliography. References into other, excluded sections can remain unresolved in an isolated preview; acceptance also builds an integrated preview of the candidate and its prerequisites.

Read the current PDF at build/main.pdf. Root-level compilation products are not manuscript inputs or submission files.

Writing follows the dependency graph rather than the printed order: complete Appendix A before Section 4 and Appendix B before Section 8. Integrated previews retain the intended section and appendix numbers. Strict acceptance rejects unresolved references and citations.

## Single-file submission

After all published units have passed their current reviews, build and export the complete article:

    python -B scripts/validate.py
    python -B scripts/build.py --strict
    python -B scripts/export_tex.py
    python -B scripts/verify_submission.py

submission/paper.tex is the sole submission source. Its preamble, all sections, TikZ figures and bibliography are inline. The verification command copies that file alone into a new temporary directory, compiles it with XeLaTeX without BibTeX or project files, and compares its text and label numbers with the current manuscript. Receipts and the preview PDF stay under build/. The internal programs, data-check instructions and workflow records are not article attachments.

## Collaboration

Read AGENTS.md, workflow/PROTOCOL.md and the relevant role file before starting. A writer and the three reviewers keep their identities and original contexts through all revisions of one section. The coordinator uses the script to prepare prompts, record real agent IDs, freeze submissions and enforce review gates.

The script emits collaboration tool calls; it does not invoke a model API or manage a hidden agent service. Agent IDs belong to the actual parent conversation. Persisted files make the work inspectable and support context restoration without claiming that live agent memory survives a lost session.

Frozen rounds archive source, the relevant outline, the unit definition and revision differences. Explicit local TeX inputs are followed recursively, and recorded compilation inputs are checked against that closure. Interrupted submissions can be retried; stale review rounds can be invalidated without replacing their original agents.

## Local references and generated files

refs/ and build/ are intentionally ignored by Git. Local reference PDFs are optional author materials, not compilation inputs or article attachments. The bibliography, structure map and source locators in the section interfaces remain versioned. Scripts do not download papers or claim a source has been checked when it is unavailable. Root-level main.aux, main.log, main.pdf and main.synctex.gz are also ignored; use build/main.pdf as the development preview.

Text files use UTF-8 and LF, enforced by .gitattributes, .editorconfig, the VS Code workspace setting and scripts/validate.py.
