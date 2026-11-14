# Pure Hodge integrals at large genus

This repository contains the manuscript and its section-by-section writing and review workflow.

## Manuscript layout

- main.tex assembles the manuscript.
- tex/preamble.tex holds shared packages, notation and theorem environments.
- frontmatter/abstract.tex contains the abstract.
- sections/ has one directory per section and one file per subsection.
- paper_outline.md is the detailed writing and proof plan.
- workflow/sections.json defines the units, dependencies and file order.
- workflow/state.json records assignments, submissions, reviews and acceptance.
- references.bib is the bibliography. Entries must be verified before use.

Only the existing introduction is initially included in the default build. Planned sections contain explicit placeholders and are excluded until accepted. Accepted body sections enter the default build as a continuous prefix, preserving section numbers. A later accepted section can be previewed independently while earlier sections are still being completed.

Accepted appendices follow the available body prefix as soon as their prerequisites are included, without waiting for every body section. This keeps supporting appendix references available during section-by-section drafting. Appendix letters and final manuscript order remain unchanged.

## Build and checks

Use Python 3.10 or newer and TeX Live with XeLaTeX and BibTeX on PATH.

    python scripts/build.py
    python scripts/build.py --unit s02
    python scripts/validate.py
    python -m unittest discover -s tests -v

The build script runs XeLaTeX twice and runs BibTeX when citations require it. All products go to build/. A unit preview uses its intended section number and the same preamble and bibliography. References into other, excluded sections can remain unresolved in an isolated preview; acceptance also builds an integrated preview of the candidate and its prerequisites.

The abstract retains its original drafting placeholder. The Introduction's four asymptotic statements remain the targets of the later proof sections; approval of the geometric identities in Section 2 does not certify those proofs.

Writing follows the dependency graph rather than the printed order: complete Appendix A before Section 4 and Appendix B before Section 8. Integrated previews retain the intended section and appendix numbers. Strict acceptance rejects unresolved references and citations.

## Collaboration

Read AGENTS.md, workflow/PROTOCOL.md and the relevant role file before starting. A writer and the three reviewers keep their identities and original contexts through all revisions of one section. The coordinator uses the script to prepare prompts, record real agent IDs, freeze submissions and enforce review gates.

The script emits collaboration tool calls; it does not invoke a model API or manage a hidden agent service. Agent IDs belong to the actual parent conversation. Persisted files make the work inspectable and support context restoration without claiming that live agent memory survives a lost session.

Frozen rounds archive source, the relevant outline, the unit definition and revision differences. Explicit local TeX inputs are followed recursively, and recorded compilation inputs are checked against that closure. Interrupted submissions can be retried; stale review rounds can be invalidated without replacing their original agents.

## Local references and generated files

refs/ and build/ are intentionally ignored by Git. Restore the local reference PDFs separately when cloning. The reference list and source map in paper_outline.md remain versioned. Scripts do not download papers or claim a source has been checked when it is unavailable.

Text files use UTF-8 and LF, enforced by .gitattributes, .editorconfig, the VS Code workspace setting and scripts/validate.py.
