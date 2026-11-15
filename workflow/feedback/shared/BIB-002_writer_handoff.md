# BIB-002 original-writer handoff

Original writer: `/root/s02_writer`.
Audit time: `2026-11-15T01:45:11+00:00`.
Feedback: `workflow/feedback/shared/BIB-002.json`, SHA256
`09548a242320ba01a622fb8643b292a6e82d4a8f4a752185eaf2943dc916c759`.

This is a compatibility-only follow-up to the unchanged BIB-001 audit:
`workflow/feedback/shared/BIB-001_writer_handoff.md`, SHA256
`fab11a0e02489f0d192a765a906328e46ad3d30e0a59bbd5ce372cdbc6f424de`.
The original scientific baseline remains
`build/s06-preparation/bibliography-refresh/baseline.json`, SHA256
`0333d304931078fe84bdd00e6a36688e067ea7491620bb471bd032d123e0b71c`.

## Actual scientific-input comparison

For each original accepted submission I again compared its baseline
`files` to `Engine().fingerprint(uid, sub.get("response_path"))`.
There are no added or removed inputs; only `references.bib` differs.
Every other actual archived input was also compared byte for byte with
the live file. This includes all scientific TeX, interfaces, original
handoffs, macros, existing calculation sources and old author responses.
The outline/unit aliases remain unchanged.

| Unit | Original baseline round | Fingerprint entries | Other archived files unchanged | Only changed input |
| --- | --- | --- | --- | --- |
| s02 | r006 | 23 | 20 | references.bib |
| s03 | r003 | 30 | 27 | references.bib |
| a | r002 | 48 | 45 | references.bib |
| s04 | r003 | 71 | 68 | references.bib |
| s05 | r002 | 78 | 75 | references.bib |

The BIB-001 conclusion that the old TeX cites none of the three new keys
is preserved by this exact byte equality; no scientific reread or new
calculation is needed.

## Exact bibliography delta

The BIB-001 reference copy was read from
`workflow/reviews/s02/r007/source/references.bib`.
Its SHA256 is
`64ce27872d52b51ad18fa76900b991159e034c9219ffb79fd5ab41083ec3e940`.
The current SHA256 is
`33f3b50ab92ad38e93e03b1c0c6cae0230f4f557ba8a133241df2f6a84ba2aa4`.

Applying just `key={\relax DLMF}` -> `key={{\relax DLMF}}` to that
copy gives the current file exactly: 7476 bytes become 7478 bytes.
Only one pair of outer braces is added. All author/title/version/date,
DOI/URL and other publication metadata are byte-identical. The original
6058-byte bibliography is still an exact prefix; the entry-key sequence
is unchanged from BIB-001, with exactly FP03, MaZ00 and DLMF added to the
original 15 entries. No old entry, macro or package is modified.

## Existing compatibility evidence

I inspected the coordinator's existing fresh-job smoke receipt, without
rerunning its build:
`build/s06-preparation/bib-smoke/protected-receipt.json`, SHA256
`3c72643386864a3d5188ed7d21bd0a6af99a4fccc4d39f7fcfb1fa94e48bf210`.
It records passed=true, strict=true, diagnostics=[] and
layout_diagnostics=[], bound to the current bibliography hash.

I verified the actual PDF digest, inspected the matching source citations
of all three new entries and the generated protected bibliography label,
and checked that the saved final log has no strict/font/overfull warning.
The smoke bibliography copy is byte-identical to current references.bib.
The output is `build/s06-preparation/bib-smoke/bib-protected-key.pdf`, SHA256
`79e76e4b414d6536266110f92ac97d3dee69d3b48c3f2e57abb7769996f94bc3`.
The generated entry retains `\bibitem[{\relax DLMF}]{DLMF}` and contains
no truncated `\re` control sequence. This is reused evidence of the
coordinator's actual test, not a build performed by the writer.

## Reuse and workflow boundary

This extra handoff is the only writer output. No section directory,
prior handoff, shared file, workflow state, old review or old build
artifact was edited. BIB-001 accepted rounds remain historical records.

Later s03, a, s04 and s05 metadata refreshes can reuse their unchanged
scientific drafts and this single audit while the delta remains exactly
BIB-001/BIB-002. No new scientific writing is required. Existing interface
snapshot identifiers remain historical scientific provenance; current
approval and freshness are recorded in workflow/state.json.

s02 was the sole active unit during the audit. Each unit still requires
its own coordinator-controlled submission, fresh signatures by the three
original reviewers and actual acceptance in dependency order. This
handoff replaces none of those steps. No new computation or build was run.
The writer stops and retains the original context for eventual s06 work.
