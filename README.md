# On Large Genus Asymptotics of Pure Hodge Integrals

**[Download the paper (PDF)](submission/paper.pdf?raw=true)** | [Standalone LaTeX source](submission/paper.tex)

This repository contains the paper *On Large Genus Asymptotics of Pure Hodge Integrals* by Si-Qi Liu and the working record of an AI-assisted mathematical research and writing project.

The project is also a demonstration of how AI can be used to prepare a mathematical paper through explicit writing standards, coordinated subagents, incremental review and revision. Its workflow configuration, scripts, writing and review records, and complete Git history are retained alongside the paper as a reference for researchers who want to develop high-quality mathematical manuscripts with AI.

## The paper

The article studies large-genus asymptotics of pure Hodge integrals in four regimes: powers of the first Hodge class, fixed-degree Hodge insertions, the top Hodge class, and fixed defects from the top class. The proofs combine uniform stable-graph estimates, finite coefficient calculations, Bessel analysis and identities from the intermediate long-wave (ILW) equation.

The Introduction includes detailed acknowledgments and an AI disclosure describing the roles of Claude Opus 5.5, GPT-6-Astra, GPT-6.1-Sol and the human author. The results have not been formally verified in Lean.

- [submission/paper.pdf](submission/paper.pdf) is the finished paper, available directly from the repository.
- [submission/paper.tex](submission/paper.tex) is its single-file source, with the preamble, all sections, TikZ figures and bibliography inline. It can be compiled independently with XeLaTeX and standard TeX distribution packages and fonts.

## A demonstration of AI-assisted mathematical writing

The human author wrote the initial Introduction, established the writing standards, designed the multi-subagent workflow, and supervised the research and manuscript preparation. The repository makes that process inspectable through its instructions, section interfaces, frozen drafts, review reports, revision records and Git history.

The central workflow decisions are:

- Work on one section at a time, drafting each subsection in its own file.
- Give each section a writer and three reviewers with distinct responsibilities.
- Review a frozen source snapshot so that all reviewers assess the same text.
- Send revisions back to the original writer and re-review to the original reviewers, preserving their contexts.
- Require a new set of current reviews when a section or its dependencies change.
- Record actual agent identities, review issues, source fingerprints and build receipts.

Writing standards are part of the workflow: define symbols before use, inherit existing definitions without unnecessary repetition, keep notation consistent and economical, introduce a proof strategy before a long argument, split proofs into useful modules, and credit the precise literature results and versions being used.

The records show the checks and reviews actually performed. The scripts enforce workflow consistency and build requirements; they do not formally prove the mathematics.

## Roles and review cycle

| Role | Responsibility | Instructions |
| --- | --- | --- |
| Coordinator | Maintain shared conventions, check dependencies, freeze submissions, record reviews and run acceptance checks. | [Coordinator](workflow/roles/coordinator.md) |
| Writer | Draft explanations and modular proofs, maintain the section interface, and respond to review issues. | [Writer](workflow/roles/writer.md) |
| Mathematical reviewer | Check definitions, hypotheses, normalizations, proof logic and uniform estimates. | [Mathematics](workflow/roles/math.md) |
| Readability reviewer | Check notation, proof guides, structure and transitions from the reader's perspective. | [Readability](workflow/roles/readability.md) |
| Academic-writing reviewer | Check attribution, precise citations, scholarly presentation and the distinction between proved results and conjectures. | [Academic writing](workflow/roles/academic.md) |

A section passes through drafting, build and static checks, a frozen submission, three independent reviews, revision, re-review and acceptance. When a reviewer requests changes, all reports are collected before the original writer revises. All three reviewers must sign the new snapshot, including reviewers who passed the previous one.

The coordinator uses the workflow script to prepare prompts and record real agent IDs. The script emits collaboration-tool arguments; the coordinator invokes the actual tools. Agent sessions belong to their originating conversation. Archived prompts, IDs and handoffs document the process without implying that a saved ID can recreate a live session elsewhere.

## Exploring or adapting the project

| Material | Where to start |
| --- | --- |
| Collaboration and writing rules | [AGENTS.md](AGENTS.md) |
| Paper structure and proof dependencies | [paper_outline.md](paper_outline.md) |
| Shared context and notation policy | [workflow/context.md](workflow/context.md) |
| Detailed workflow protocol and report formats | [workflow/PROTOCOL.md](workflow/PROTOCOL.md) |
| Reusable workflow, build, validation and export scripts | [scripts/](scripts/) |
| Section interfaces, modular source and calculation scripts | [sections/](sections/) |
| Frozen submissions, reviewer reports and revision differences | [workflow/reviews/](workflow/reviews/) |
| Recorded feedback and project decisions | [workflow/feedback/](workflow/feedback/) |
| Workflow and export tests | [tests/](tests/) |

The full Git history is preserved. Use the repository's commit history to follow the development, or inspect it locally:

```sh
git log --oneline
git log -p -- sections/
```

Historical drafts and reports remain unchanged. Appendix C was retired and is excluded from the current paper; its source and reviews are retained as part of that history. Current acceptance and source freshness are reported by `python -B scripts/workflow.py status`.

To adapt the workflow to another manuscript, establish that manuscript's own outline, research context, role assignments and workflow state. The existing acceptance records describe this paper.

## Build and verify

For the modular project, use Python 3.10 or newer and TeX Live with XeLaTeX and BibTeX on `PATH`. The workflow scripts use the Python standard library. Isolated PDF comparison also uses `pdftotext`.

```sh
python -B scripts/workflow.py status
python -B scripts/validate.py
python -B scripts/build.py --strict
python -m unittest discover -s tests -v
```

The development PDF is generated at `build/main.pdf`. Each section has an entry file and separate subsection files under [sections/](sections/); [main.tex](main.tex) assembles the accepted manuscript, [tex/preamble.tex](tex/preamble.tex) holds shared definitions, and [references.bib](references.bib) supplies the development bibliography.

To regenerate both published paper files and check the standalone source:

```sh
python -B scripts/build.py --strict
python -B scripts/export_tex.py
python -B scripts/verify_submission.py
```

The exporter writes `submission/paper.tex` and refreshes `submission/paper.pdf` from the approved complete build. The verifier copies the TeX file alone into an isolated directory, compiles it without BibTeX or project files, and compares its PDF text and label numbers with the approved manuscript. It also checks that the published PDF is the approved compiled copy. Build products and receipts stay under `build/`.

Local reference PDFs in `refs/` and generated files in `build/` are excluded from Git. They are not needed to read or compile the standalone paper. The repository retains the bibliography, source locators, calculation scripts and collaboration records. Versioned text uses UTF-8 and LF.
