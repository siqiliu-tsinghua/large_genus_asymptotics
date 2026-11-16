# PDF-NAVIGATION: coordinator completion

Baseline: `6156e95181cc6e244182757832bcf52881ce6506`. All 15 public GitHub topics were verified; no repository metadata was changed by this task.

The sole manuscript input change is the shared preamble: hyperref and bookmark, Unicode metadata, unobtrusive links, clickable TOC text/page numbers, numbered hierarchical bookmarks and the outline opening hint. Every section, interface, old handoff, mathematical statement, bibliography entry and production script matches the captured baseline. Both official submission artifacts were regenerated.

## Actual acceptance

| Unit | New round | Snapshot | Three original reviewers |
| --- | --- | --- | --- |
| s01 | r010 | `5421a0b4bb33358e01fe83cb441304e73143f7d042827943d3aee22239096ee6` | pass |
| s02 | r020 | `94ed540f009d7f839877da60c4d97a42058245e2b3d116513d61e9a6a04b4d67` | pass |
| s03 | r017 | `ab67843ce34958dfb7770c1b2e9d76ae612b0027ab02b35d35df944823a2c1ab` | pass |
| a | r017 | `9e445ccf72936d8307aaf912f3c768b61f7e487e680df55ef3031e454b70246f` | pass |
| s04 | r019 | `318d11027bd06658e8a92240fada062fc08e302cae82ebf74acb9d920beb8a89` | pass |
| s05 | r016 | `3d199aa4006a950a5b6529c863c127f10509b1db16c33d5626847055362fc5ea` | pass |
| s06 | r015 | `7506c5490a7f22b29aa1065ee2149b9623dc7dd9c3430c0015a49606829546ea` | pass |
| s07 | r012 | `c430fa4c38606b971f15c3de2434fb384f774fec04721930710f0c49870f3f59` | pass |
| b | r010 | `89a2023f3b49bd3dcb7b924cd895207cb418d0e5e2cf1490cdb8a666e4fd2dc1` | pass |
| s08 | r010 | `0a0453cda5b1f98844e14918c1d31d30ddb87aa429a347efe5bbfed9d94838f6` | pass |

The original writer supplied an external per-unit ACK. The original three reviewers signed each actual new snapshot, reusing unchanged complete mathematical assessments and the one independently inspected common navigation/layout review. No old pass was copied and no proof, coefficient or literature research was repeated.

## Actual output checks

- main: 102 pages, 48 outline items, 810 linked text fragments, 586 named destinations, inspected with Poppler.
- submission: 102 pages, 48 outline items, 810 linked text fragments, 586 named destinations, inspected with Poppler.
- isolated: 102 pages, 48 outline items, 810 linked text fragments, 586 named destinations, inspected with Poppler.
- Strict main build and final static validation passed. The isolated TeX-only build passed in 3 recorded passes, with no diagnostics, no project inputs, matching printed text and all 430 label numbers.
- `submission/paper.tex`: SHA256 `94147c5816c247acc4903a33866455ee2f32e773f45b46208e4872668497073e`.
- `submission/paper.pdf`: SHA256 `e1895cdc25b3af4ef1ba46c60dd51cfcdcc0e9956077b6741ba5f520938b1684`, byte-identical to the strict main PDF.
- Actual final receipt: `build/pdf-navigation-20261116/logs/ab4cf19fe6f4/final.json`; reviewed source hash `773b7ecb1646f92b4c5921d7328b07b7b42b1d7b5ede5a1b11053ad022dd29e7`.

## Comparison limits and preparation recovery

The old PDF contained no links or bookmarks. Adding PDF navigation changes some extracted whitespace/superscript ordering and tiny renderer rounding; raw old/new text and pixels are not byte-identical. Actual per-page character multisets and all 430 printed label numbers agree. Whole-page 72-dpi raster comparison records maximum changed-channel fraction 0.0005260724704682045 and maximum mean absolute channel delta 0.01680442857370594, under explicit 0.001/0.02 limits. The reviewed new companion, final main and isolated article text agree.

The first helper retained an over-strict raw-text comparison failure; its helper, pin, baseline and failed logs remain intact. A separate helper version corrected that criterion without changing inputs; a further separate version used relative Poppler output paths for this Windows Unicode workspace. No production tool, frozen snapshot, old review or baseline was rewritten. Generated build evidence remains ignored, as required.
