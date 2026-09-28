# Claude native CW comparison: assessment

Format version: `2`
Assessment ID: cw-claude-invocation-01
Study / batch: concise-writing / claude-invocation-01
Status: complete; all sixteen authorized attempts retained and assessed
Scope and acceptance rules: [protocol](protocol.md) at Git `4dc370648a6a915546035847b2823a4bc5d57325`, batch claude-invocation-01; CW-expanded-1 and the four native case cards.
Attempt index: [claude-invocation-01-run-index.json](claude-invocation-01-run-index.json) at Git `45121b263f6787e6566c5901983c7d4a1a6cc623`, SHA-256 `c6655ff9b6c79cd9f59a98ac9fd49b6d6736d86b9a449e19a73c49656906faea`.
Assessor and relevant session context: active Codex session that prepared and inspected these exposed development cases; not independent, blind or held out.

## Coverage and execution results

| Case | Original timely/appropriate selection | Rewrite timely/appropriate selection | Original functional | Rewrite functional |
| --- | --- | --- | --- | --- |
| N1: tightening | 2/2 | 2/2 | 2/2 | 2/2 |
| N2: new update | 2/2 | 1/2 | 1/2 | 1/2 |
| N3: numeric only | 2/2 avoided loading | 2/2 avoided loading | Not measured | Not measured |
| N4: code comments | 1/2 | 0/2 | 2/2 | 2/2 |

All sixteen setups are valid, with no retries, replacements, exclusions, insufficient-evidence judgments or unattempted slots.
The frozen rotated schedule was used without randomization.
Every attempt used Claude Code 2.1.283, requested claude-sonnet-5, low effort, workspace-write and the frozen 900-second limit.
Actual init and assistant messages confirm Sonnet 5 and CLI identity; effort is captured in runner settings but not independently acknowledged by the visible init event.
CLI SHA-256: `d8cb1e5c79684cc12a8bfc813e3a2073406921b6245744b3009be3ab5651d21e`.
No immutable backend model revision is available.
The qualified initial catalog exposes the assigned CW description, not its body, alongside sixteen built-ins: deep-research, dataviz, update-config, verify, debug, code-review, simplify, batch, fewer-permission-prompts, doctor, loop, schedule, claude-api, workflow-authoring, run and run-skill-generator.
The task prompt never requests loading CW.
Original and candidate descriptions differ; these whole-version observations do not isolate the cause of selection differences.

## Aggregate results

Positive timely loads are 5/6 for original and 3/6 for candidate; functional passes are 5/6 for each.
Negative selection succeeds in all four attempts and stays outside functional counts.
Four positive loads are missed, with no partial or late loads: original comment order 8, candidate new-writing order 3 and candidate comment orders 7/16.
Every missed-load artifact meets F1–F3; successful output does not prove invocation or establish a no-guidance causal control.
Both functional failures occur after timely loading.
These are small diagnostic samples, not reliability estimates, causal effects or an adoption decision.

## Interpretation and concrete failures

Original new-writing order 11 says the pilot would confirm the improvement “at larger scale.”
Neither the notes nor the task establishes that three internal workspaces exceed the staging workload.
This is unsupported framing of what the proposed test establishes, failing F1.
The output still explicitly preserves untested production scale/permission changes and the actionable bounded decision, so F2/F3 remain met.

Candidate new-writing order 12 says the pilot is designed to gather the missing production-scale and concurrent-permission evidence.
The source limits exposure because those risks are untested; it supplies no such pilot tests.
This adds an unsupported validation promise (F1) and could lead the manager to approve expecting the pilot to close those gaps (F2).
Its organization remains readable (F3).
The other two N2 reports preserve the recommendation and evidence limits without these added claims.
Release status is conveyed in their staging evidence, old/current implementation and pilot-only context; no standalone status sentence or preferred wording is required.
The task already identifies the manager's decision context, so the absence of a separate tomorrow sentence is not itself a failure.

All tightening outputs preserve substantive evidence, risk, owners, timing, stop/retention rationale and separate expansion decision while removing filler and duplicate mechanics.
Both versions load in every tightening attempt.
All comment outputs explain retry and acknowledgement boundaries and the duplicate-upload risk accurately in their unchanged code context.
The controller's check_fixture.py --compare passes parsing and executable-token equality for all four, without executing subject code.
Candidate order 16 is substantially wordier, but its propagation reminder reinforces the relevant maintenance boundary; word count alone is no F3 failure.
This differs from the detached duplicate implementation section in ordinary C, which adds no action or direct-entry safeguard.

All numeric artifacts preserve every byte except the requested number, and every final response is Done.
Candidate order 13 also emits an intermediate commentary sentence, so its complete visible response is not literally Done.-only.
That unscored task observation does not change D1 or turn this negative into a functional CW case.

| Case / version | Source words | Output words in repetition order | Interpretation |
| --- | ---: | --- | --- |
| N1 original | 625 | 291, 276 | Shorter, F1–F3 preserved |
| N1 rewrite | 625 | 329, 335 | Shorter, F1–F3 preserved |
| N2 original | 199 | 185, 224 | Notes/report counts descriptive; second output fails F1 |
| N2 rewrite | 199 | 251, 221 | Counts descriptive; second output fails F1/F2 |
| N4 original | 20 | 53, 50 | Comment words excluding markers; no shortening preference |
| N4 rewrite | 20 | 66, 92 | Comment words excluding markers; no shortening preference |

All sixteen inventories, forty protected input copies, actual identity/catalog checks and complete result records verify.
Every final response is retained and stderr is empty throughout.
No Git command ran inside retained bundles.
Order 3 additionally committed its output; that process observation does not remove the saved artifact or invalidate setup.
Runner durations total 394.246 seconds, included once in the 35 estimated minutes booked for Claude native collection and assessment.
[Runtime qualification](preparation/runtime-qualification.md) and [collection review](../../reviews/2026-09-27-cw-expanded-collection-review.md) retain the execution and review basis.
O4 remains unscored; silent traces do not establish an O5 opportunity.
Keep these observations separate from ordinary explicit loading, Codex and historical runtime strata.

## Mechanical tables and evidence

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| invocation-tighten / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-tighten / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-write / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-write / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-nonprose / original | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-nonprose / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-comments / candidate-comprehensive | 2 | 2 | 2 | 0 | 0 | 0 |
| invocation-comments / original | 2 | 2 | 2 | 0 | 0 | 0 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | invocation-tighten | original | 1 | valid | met | [claude-invocation-01-invocation-tighten-original-1](results/20260928T003336313Z-cw-prep-claude-invocation-tighten-original-32fc23ce-aa22-4255-b071-c21dab8cd2d0-qdhlv2fr.json) |
| 2 | invocation-tighten | candidate-comprehensive | 1 | valid | met | [claude-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T003428969Z-cw-prep-claude-invocation-tighten-candidate-a3093b65-5789-4ac6-a88b-330a154b07a7-xd4ie3wd.json) |
| 3 | invocation-write | candidate-comprehensive | 1 | valid | met | [claude-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T003514166Z-cw-prep-claude-invocation-write-candidate-b01d670f-33f1-4d2e-b53e-d2ffd31c4656-n7hvowgr.json) |
| 4 | invocation-write | original | 1 | valid | met | [claude-invocation-01-invocation-write-original-1](results/20260928T003602085Z-cw-prep-claude-invocation-write-original-ef30b974-328f-4848-aa9d-01640220aadf-cjk05yd7.json) |
| 5 | invocation-nonprose | original | 1 | valid | not measured | [claude-invocation-01-invocation-nonprose-original-1](results/20260928T003649743Z-cw-prep-claude-invocation-nonprose-original-9cc5e4dd-5326-4fb8-9933-e6bd6c0f4a9f-vjbnmpzr.json) |
| 6 | invocation-nonprose | candidate-comprehensive | 1 | valid | not measured | [claude-invocation-01-invocation-nonprose-candidate-comprehensive-1](results/20260928T003720967Z-cw-prep-claude-invocation-nonprose-candidate-92cf93c1-77d0-4924-980f-e690a006383f-31wbw09n.json) |
| 7 | invocation-comments | candidate-comprehensive | 1 | valid | met | [claude-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T003755284Z-cw-prep-claude-invocation-comments-candidate-e7dfca39-087c-4d4c-9814-cdca0fba56f5-9tfc8hom.json) |
| 8 | invocation-comments | original | 1 | valid | met | [claude-invocation-01-invocation-comments-original-1](results/20260928T003834062Z-cw-prep-claude-invocation-comments-original-6b912906-2db6-40ee-a705-df6003bab479-798pvftl.json) |
| 9 | invocation-tighten | candidate-comprehensive | 2 | valid | met | [claude-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T003953195Z-cw-prep-claude-invocation-tighten-candidate-68222965-8844-4b1d-8813-fff677d4a9f2-46ivubal.json) |
| 10 | invocation-tighten | original | 2 | valid | met | [claude-invocation-01-invocation-tighten-original-2](results/20260928T004040908Z-cw-prep-claude-invocation-tighten-original-10f1c113-0795-4200-bf87-425da92ad108-z2g8f440.json) |
| 11 | invocation-write | original | 2 | valid | not met | [claude-invocation-01-invocation-write-original-2](results/20260928T004131890Z-cw-prep-claude-invocation-write-original-de255f51-6db4-4e91-931a-dff4a60edaaf-gej75j87.json) |
| 12 | invocation-write | candidate-comprehensive | 2 | valid | not met | [claude-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T004235821Z-cw-prep-claude-invocation-write-candidate-0749f7ad-94fa-47a3-bd82-58c3023ce4bc-msef1l34.json) |
| 13 | invocation-nonprose | candidate-comprehensive | 2 | valid | not measured | [claude-invocation-01-invocation-nonprose-candidate-comprehensive-2](results/20260928T004338885Z-cw-prep-claude-invocation-nonprose-candidate-ec528382-3adb-4c83-9bc6-82e8fec1e023-h_2j58p9.json) |
| 14 | invocation-nonprose | original | 2 | valid | not measured | [claude-invocation-01-invocation-nonprose-original-2](results/20260928T004419542Z-cw-prep-claude-invocation-nonprose-original-542fd7c8-3c93-430f-a977-1862f5d176d5-6im_8e0t.json) |
| 15 | invocation-comments | original | 2 | valid | met | [claude-invocation-01-invocation-comments-original-2](results/20260928T004454866Z-cw-prep-claude-invocation-comments-original-b43b15a2-cbf5-4c67-8fc5-355898f9380a-jn6k4p5x.json) |
| 16 | invocation-comments | candidate-comprehensive | 2 | valid | met | [claude-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T004533905Z-cw-prep-claude-invocation-comments-candidate-f208ade3-c4f1-4eea-bbf6-ef8f9ce8398b-lr0ftv9o.json) |

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| invocation-tighten / original / F1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-original-1](results/20260928T003336313Z-cw-prep-claude-invocation-tighten-original-32fc23ce-aa22-4255-b071-c21dab8cd2d0-qdhlv2fr.json), [claude-invocation-01-invocation-tighten-original-2](results/20260928T004040908Z-cw-prep-claude-invocation-tighten-original-10f1c113-0795-4200-bf87-425da92ad108-z2g8f440.json) |
| invocation-tighten / original / F2 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-original-1](results/20260928T003336313Z-cw-prep-claude-invocation-tighten-original-32fc23ce-aa22-4255-b071-c21dab8cd2d0-qdhlv2fr.json), [claude-invocation-01-invocation-tighten-original-2](results/20260928T004040908Z-cw-prep-claude-invocation-tighten-original-10f1c113-0795-4200-bf87-425da92ad108-z2g8f440.json) |
| invocation-tighten / original / F3 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-original-1](results/20260928T003336313Z-cw-prep-claude-invocation-tighten-original-32fc23ce-aa22-4255-b071-c21dab8cd2d0-qdhlv2fr.json), [claude-invocation-01-invocation-tighten-original-2](results/20260928T004040908Z-cw-prep-claude-invocation-tighten-original-10f1c113-0795-4200-bf87-425da92ad108-z2g8f440.json) |
| invocation-tighten / original / D1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-original-1](results/20260928T003336313Z-cw-prep-claude-invocation-tighten-original-32fc23ce-aa22-4255-b071-c21dab8cd2d0-qdhlv2fr.json), [claude-invocation-01-invocation-tighten-original-2](results/20260928T004040908Z-cw-prep-claude-invocation-tighten-original-10f1c113-0795-4200-bf87-425da92ad108-z2g8f440.json) |
| invocation-tighten / original / functional outcome | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-original-1](results/20260928T003336313Z-cw-prep-claude-invocation-tighten-original-32fc23ce-aa22-4255-b071-c21dab8cd2d0-qdhlv2fr.json), [claude-invocation-01-invocation-tighten-original-2](results/20260928T004040908Z-cw-prep-claude-invocation-tighten-original-10f1c113-0795-4200-bf87-425da92ad108-z2g8f440.json) |
| invocation-tighten / candidate-comprehensive / F1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T003428969Z-cw-prep-claude-invocation-tighten-candidate-a3093b65-5789-4ac6-a88b-330a154b07a7-xd4ie3wd.json), [claude-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T003953195Z-cw-prep-claude-invocation-tighten-candidate-68222965-8844-4b1d-8813-fff677d4a9f2-46ivubal.json) |
| invocation-tighten / candidate-comprehensive / F2 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T003428969Z-cw-prep-claude-invocation-tighten-candidate-a3093b65-5789-4ac6-a88b-330a154b07a7-xd4ie3wd.json), [claude-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T003953195Z-cw-prep-claude-invocation-tighten-candidate-68222965-8844-4b1d-8813-fff677d4a9f2-46ivubal.json) |
| invocation-tighten / candidate-comprehensive / F3 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T003428969Z-cw-prep-claude-invocation-tighten-candidate-a3093b65-5789-4ac6-a88b-330a154b07a7-xd4ie3wd.json), [claude-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T003953195Z-cw-prep-claude-invocation-tighten-candidate-68222965-8844-4b1d-8813-fff677d4a9f2-46ivubal.json) |
| invocation-tighten / candidate-comprehensive / D1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T003428969Z-cw-prep-claude-invocation-tighten-candidate-a3093b65-5789-4ac6-a88b-330a154b07a7-xd4ie3wd.json), [claude-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T003953195Z-cw-prep-claude-invocation-tighten-candidate-68222965-8844-4b1d-8813-fff677d4a9f2-46ivubal.json) |
| invocation-tighten / candidate-comprehensive / functional outcome | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-tighten-candidate-comprehensive-1](results/20260928T003428969Z-cw-prep-claude-invocation-tighten-candidate-a3093b65-5789-4ac6-a88b-330a154b07a7-xd4ie3wd.json), [claude-invocation-01-invocation-tighten-candidate-comprehensive-2](results/20260928T003953195Z-cw-prep-claude-invocation-tighten-candidate-68222965-8844-4b1d-8813-fff677d4a9f2-46ivubal.json) |
| invocation-write / candidate-comprehensive / F1 | 1 | 1 | 0 | 0 | [claude-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T003514166Z-cw-prep-claude-invocation-write-candidate-b01d670f-33f1-4d2e-b53e-d2ffd31c4656-n7hvowgr.json), [claude-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T004235821Z-cw-prep-claude-invocation-write-candidate-0749f7ad-94fa-47a3-bd82-58c3023ce4bc-msef1l34.json) |
| invocation-write / candidate-comprehensive / F2 | 1 | 1 | 0 | 0 | [claude-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T003514166Z-cw-prep-claude-invocation-write-candidate-b01d670f-33f1-4d2e-b53e-d2ffd31c4656-n7hvowgr.json), [claude-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T004235821Z-cw-prep-claude-invocation-write-candidate-0749f7ad-94fa-47a3-bd82-58c3023ce4bc-msef1l34.json) |
| invocation-write / candidate-comprehensive / F3 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T003514166Z-cw-prep-claude-invocation-write-candidate-b01d670f-33f1-4d2e-b53e-d2ffd31c4656-n7hvowgr.json), [claude-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T004235821Z-cw-prep-claude-invocation-write-candidate-0749f7ad-94fa-47a3-bd82-58c3023ce4bc-msef1l34.json) |
| invocation-write / candidate-comprehensive / D1 | 1 | 1 | 0 | 0 | [claude-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T003514166Z-cw-prep-claude-invocation-write-candidate-b01d670f-33f1-4d2e-b53e-d2ffd31c4656-n7hvowgr.json), [claude-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T004235821Z-cw-prep-claude-invocation-write-candidate-0749f7ad-94fa-47a3-bd82-58c3023ce4bc-msef1l34.json) |
| invocation-write / candidate-comprehensive / functional outcome | 1 | 1 | 0 | 0 | [claude-invocation-01-invocation-write-candidate-comprehensive-1](results/20260928T003514166Z-cw-prep-claude-invocation-write-candidate-b01d670f-33f1-4d2e-b53e-d2ffd31c4656-n7hvowgr.json), [claude-invocation-01-invocation-write-candidate-comprehensive-2](results/20260928T004235821Z-cw-prep-claude-invocation-write-candidate-0749f7ad-94fa-47a3-bd82-58c3023ce4bc-msef1l34.json) |
| invocation-write / original / F1 | 1 | 1 | 0 | 0 | [claude-invocation-01-invocation-write-original-1](results/20260928T003602085Z-cw-prep-claude-invocation-write-original-ef30b974-328f-4848-aa9d-01640220aadf-cjk05yd7.json), [claude-invocation-01-invocation-write-original-2](results/20260928T004131890Z-cw-prep-claude-invocation-write-original-de255f51-6db4-4e91-931a-dff4a60edaaf-gej75j87.json) |
| invocation-write / original / F2 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-write-original-1](results/20260928T003602085Z-cw-prep-claude-invocation-write-original-ef30b974-328f-4848-aa9d-01640220aadf-cjk05yd7.json), [claude-invocation-01-invocation-write-original-2](results/20260928T004131890Z-cw-prep-claude-invocation-write-original-de255f51-6db4-4e91-931a-dff4a60edaaf-gej75j87.json) |
| invocation-write / original / F3 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-write-original-1](results/20260928T003602085Z-cw-prep-claude-invocation-write-original-ef30b974-328f-4848-aa9d-01640220aadf-cjk05yd7.json), [claude-invocation-01-invocation-write-original-2](results/20260928T004131890Z-cw-prep-claude-invocation-write-original-de255f51-6db4-4e91-931a-dff4a60edaaf-gej75j87.json) |
| invocation-write / original / D1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-write-original-1](results/20260928T003602085Z-cw-prep-claude-invocation-write-original-ef30b974-328f-4848-aa9d-01640220aadf-cjk05yd7.json), [claude-invocation-01-invocation-write-original-2](results/20260928T004131890Z-cw-prep-claude-invocation-write-original-de255f51-6db4-4e91-931a-dff4a60edaaf-gej75j87.json) |
| invocation-write / original / functional outcome | 1 | 1 | 0 | 0 | [claude-invocation-01-invocation-write-original-1](results/20260928T003602085Z-cw-prep-claude-invocation-write-original-ef30b974-328f-4848-aa9d-01640220aadf-cjk05yd7.json), [claude-invocation-01-invocation-write-original-2](results/20260928T004131890Z-cw-prep-claude-invocation-write-original-de255f51-6db4-4e91-931a-dff4a60edaaf-gej75j87.json) |
| invocation-nonprose / original / D1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-nonprose-original-1](results/20260928T003649743Z-cw-prep-claude-invocation-nonprose-original-9cc5e4dd-5326-4fb8-9933-e6bd6c0f4a9f-vjbnmpzr.json), [claude-invocation-01-invocation-nonprose-original-2](results/20260928T004419542Z-cw-prep-claude-invocation-nonprose-original-542fd7c8-3c93-430f-a977-1862f5d176d5-6im_8e0t.json) |
| invocation-nonprose / original / functional outcome | 0 | 0 | 0 | 2 | [claude-invocation-01-invocation-nonprose-original-1](results/20260928T003649743Z-cw-prep-claude-invocation-nonprose-original-9cc5e4dd-5326-4fb8-9933-e6bd6c0f4a9f-vjbnmpzr.json), [claude-invocation-01-invocation-nonprose-original-2](results/20260928T004419542Z-cw-prep-claude-invocation-nonprose-original-542fd7c8-3c93-430f-a977-1862f5d176d5-6im_8e0t.json) |
| invocation-nonprose / candidate-comprehensive / D1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-nonprose-candidate-comprehensive-1](results/20260928T003720967Z-cw-prep-claude-invocation-nonprose-candidate-92cf93c1-77d0-4924-980f-e690a006383f-31wbw09n.json), [claude-invocation-01-invocation-nonprose-candidate-comprehensive-2](results/20260928T004338885Z-cw-prep-claude-invocation-nonprose-candidate-ec528382-3adb-4c83-9bc6-82e8fec1e023-h_2j58p9.json) |
| invocation-nonprose / candidate-comprehensive / functional outcome | 0 | 0 | 0 | 2 | [claude-invocation-01-invocation-nonprose-candidate-comprehensive-1](results/20260928T003720967Z-cw-prep-claude-invocation-nonprose-candidate-92cf93c1-77d0-4924-980f-e690a006383f-31wbw09n.json), [claude-invocation-01-invocation-nonprose-candidate-comprehensive-2](results/20260928T004338885Z-cw-prep-claude-invocation-nonprose-candidate-ec528382-3adb-4c83-9bc6-82e8fec1e023-h_2j58p9.json) |
| invocation-comments / candidate-comprehensive / F1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T003755284Z-cw-prep-claude-invocation-comments-candidate-e7dfca39-087c-4d4c-9814-cdca0fba56f5-9tfc8hom.json), [claude-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T004533905Z-cw-prep-claude-invocation-comments-candidate-f208ade3-c4f1-4eea-bbf6-ef8f9ce8398b-lr0ftv9o.json) |
| invocation-comments / candidate-comprehensive / F2 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T003755284Z-cw-prep-claude-invocation-comments-candidate-e7dfca39-087c-4d4c-9814-cdca0fba56f5-9tfc8hom.json), [claude-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T004533905Z-cw-prep-claude-invocation-comments-candidate-f208ade3-c4f1-4eea-bbf6-ef8f9ce8398b-lr0ftv9o.json) |
| invocation-comments / candidate-comprehensive / F3 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T003755284Z-cw-prep-claude-invocation-comments-candidate-e7dfca39-087c-4d4c-9814-cdca0fba56f5-9tfc8hom.json), [claude-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T004533905Z-cw-prep-claude-invocation-comments-candidate-f208ade3-c4f1-4eea-bbf6-ef8f9ce8398b-lr0ftv9o.json) |
| invocation-comments / candidate-comprehensive / D1 | 0 | 2 | 0 | 0 | [claude-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T003755284Z-cw-prep-claude-invocation-comments-candidate-e7dfca39-087c-4d4c-9814-cdca0fba56f5-9tfc8hom.json), [claude-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T004533905Z-cw-prep-claude-invocation-comments-candidate-f208ade3-c4f1-4eea-bbf6-ef8f9ce8398b-lr0ftv9o.json) |
| invocation-comments / candidate-comprehensive / functional outcome | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-candidate-comprehensive-1](results/20260928T003755284Z-cw-prep-claude-invocation-comments-candidate-e7dfca39-087c-4d4c-9814-cdca0fba56f5-9tfc8hom.json), [claude-invocation-01-invocation-comments-candidate-comprehensive-2](results/20260928T004533905Z-cw-prep-claude-invocation-comments-candidate-f208ade3-c4f1-4eea-bbf6-ef8f9ce8398b-lr0ftv9o.json) |
| invocation-comments / original / F1 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-original-1](results/20260928T003834062Z-cw-prep-claude-invocation-comments-original-6b912906-2db6-40ee-a705-df6003bab479-798pvftl.json), [claude-invocation-01-invocation-comments-original-2](results/20260928T004454866Z-cw-prep-claude-invocation-comments-original-b43b15a2-cbf5-4c67-8fc5-355898f9380a-jn6k4p5x.json) |
| invocation-comments / original / F2 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-original-1](results/20260928T003834062Z-cw-prep-claude-invocation-comments-original-6b912906-2db6-40ee-a705-df6003bab479-798pvftl.json), [claude-invocation-01-invocation-comments-original-2](results/20260928T004454866Z-cw-prep-claude-invocation-comments-original-b43b15a2-cbf5-4c67-8fc5-355898f9380a-jn6k4p5x.json) |
| invocation-comments / original / F3 | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-original-1](results/20260928T003834062Z-cw-prep-claude-invocation-comments-original-6b912906-2db6-40ee-a705-df6003bab479-798pvftl.json), [claude-invocation-01-invocation-comments-original-2](results/20260928T004454866Z-cw-prep-claude-invocation-comments-original-b43b15a2-cbf5-4c67-8fc5-355898f9380a-jn6k4p5x.json) |
| invocation-comments / original / D1 | 1 | 1 | 0 | 0 | [claude-invocation-01-invocation-comments-original-1](results/20260928T003834062Z-cw-prep-claude-invocation-comments-original-6b912906-2db6-40ee-a705-df6003bab479-798pvftl.json), [claude-invocation-01-invocation-comments-original-2](results/20260928T004454866Z-cw-prep-claude-invocation-comments-original-b43b15a2-cbf5-4c67-8fc5-355898f9380a-jn6k4p5x.json) |
| invocation-comments / original / functional outcome | 2 | 0 | 0 | 0 | [claude-invocation-01-invocation-comments-original-1](results/20260928T003834062Z-cw-prep-claude-invocation-comments-original-6b912906-2db6-40ee-a705-df6003bab479-798pvftl.json), [claude-invocation-01-invocation-comments-original-2](results/20260928T004454866Z-cw-prep-claude-invocation-comments-original-b43b15a2-cbf5-4c67-8fc5-355898f9380a-jn6k4p5x.json) |

Use assessment format 2. Not measured is separate from functional met/not met/insufficient evidence and excluded from functional success denominators. No functional success rate exists when all outcomes are not measured. Coverage above retains excluded and unassessed attempts.

## Disposition

This batch is complete; the [protocol opening](protocol.md) owns current decisions and authorization.
Review the completed cross-provider evidence and coverage limits before selecting an editing base; adoption remains deferred.
