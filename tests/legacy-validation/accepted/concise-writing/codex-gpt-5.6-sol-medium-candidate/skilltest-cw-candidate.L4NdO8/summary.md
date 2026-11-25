# CW candidate comparison

Status: COMPLETE / AWAITING OWNER REVIEW — all 66 approved observations are scored; no further provider calls are authorized by this batch.
Frozen revision: `595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d`, pushed to `origin/feature/cw-validation-design`; branch clean and synchronized.
Working directory: `/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design`.
Provider/model/effort: codex / gpt-5.6-sol / medium.
Fixed CLI-reference directory: `/private/tmp/skilltest-cw-candidate.pITN2u/qualification`.

The owner approved the [complete exact commands](approval-commands.md); the original request document remains unchanged.
Their SHA-256 is `21b35b9dc5ea062f9f31af3fe92e0d8bc8186769f680070fb992a1fec6625c6b`; do not edit that document after approval.
[Command audit](command-audit.json) and [one-shot source](audit-commands.py) verify all 66 commands against the frozen catalog order, candidate configs, prompts, rubrics, fixture sources and provider settings.
At preparation, all 66 attempt directories and `runs/` were empty; the live ledger below records subsequent collection.
Do not rerun the directory-allocation audit or overwrite existing attempts.

[Qualification/reuse](/private/tmp/skilltest-cw-candidate.pITN2u/qualification/summary.md) supports reusing all 99 accepted no-DD/current-DD observations with original provenance.
The [accepted evidence index](/Users/simon/work/personal/disciplined-development-skills/.worktrees/cw-validation-design/skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md) and all 938 evidence files are committed in the frozen revision.
Preservation restored all 100 archives and verified every selected byte plus the readable worksheet links; original scratch remains retained.
The [preparation record](/private/tmp/skilltest-cw-candidate.pITN2u/summary.md) owns the provider-free checks, document review, packaging correction and hook verification.

Collection followed the approved serial order below, applying the frozen CW runbook's per-attempt version/input/trace/cleanup checks and full-trace scoring before each next launch.
No adaptive repeats, control recollection, effort change, new test, new wording or skill deployment is authorized.
Collection is stopped: all approved observations are scored and mechanically audited for owner review.
Worksheet cross-check corrected transposed CW-I1/CW-I2 labels in r1 CW-19 and r2 CW-01–06/CW-08: CW-I1 is preservation, CW-I2 is lossless padding removal. Criterion prose, evidence and verdicts did not change; no accepted baseline was edited.
An understood infrastructure-only retry uses the exact unchanged command and preserves excluded captures under the existing recovery policy.

## Comparison for owner review

The unchanged rewrite improved the description, ownership and response-scope diagnostics, but did not resolve complex-prose precision.
CW-19 passed 1/3 candidate observations versus 2/3 current-DD observations; this is an observed lower count, not a statistically established regression.
Do not adopt the candidate automatically or declare an overall GREEN result.

All primary cells below are PASS counts out of three, under each row's frozen purpose-specific rubric.
The last column separately reports task-fidelity FAIL counts out of three, current → candidate; a primary PASS does not erase a fidelity FAIL.
“—” means no no-DD condition was defined, not missing evidence.

| Scenario / purpose | No DD | Current DD | Candidate | Fidelity failures: current → candidate |
|---|---:|---:|---:|---:|
| CW-01 loaded prose | 3 | 3 | 3 | 1 → 0 |
| CW-01 native discovery | — | 3 | 3 | 1 → 0 |
| CW-02 loaded prose | 3 | 3 | 3 | 0 → 1 |
| CW-03 loaded prose | 3 | 3 | 3 | 0 → 0 |
| CW-04 loaded prose | 3 | 3 | 3 | 0 → 1 |
| CW-05 loaded prose | 3 | 3 | 3 | 1 → 1 |
| CW-06 loaded prose | 3 | 3 | 3 | 2 → 1 |
| CW-07 direct-load transport | 3 | 3 | 3 | 1 → 2 |
| CW-08 loaded prose | 3 | 3 | 3 | 3 → 2 |
| CW-09 description classification | — | 0 | 3 | 1 → 0 |
| CW-10 ownership contract | — | 0 | 3 | 0 → 0 |
| CW-11 description classification | — | 0 | 3 | 0 → 1 |
| CW-12 ownership contract | — | 0 | 3 | 0 → 1 |
| CW-13 loaded composition decision | 3 | 3 | 3 | 3 → 1 |
| CW-13 native authoring discovery | — | 1 | 2 | 0 → 0 |
| CW-14 loaded composition decision | 3 | 3 | 3 | 2 → 2 |
| CW-14 native authoring discovery | — | 3 | 3 | 0 → 0 |
| CW-17 response-scope contract | — | 0 | 3 | 0 → 0 |
| CW-17 native non-trigger | — | 1 | 3 | 0 → 0 |
| CW-18 file-scope contract | — | 3 | 3 | 0 → 0 |
| CW-18 native file discovery | — | 3 | 3 | 3 → 3 |
| CW-19 complex loaded prose | 0 | 2 | 1 | 2 → 0 |

No-DD task-fidelity failures were zero except CW-13 and CW-14 loaded composition, two each; their primary verdicts remain PASS.
All counts reconcile to the unchanged accepted summaries and the fresh worksheets in the [final audit](final-audit.json).
There are no candidate INCONCLUSIVE observations or excluded infrastructure-only attempts.

### Findings and limits

- **Scope and ownership:** CW-09/11 description classification, CW-10/12 ownership extraction and CW-17 response-scope contract each changed from 0/3 to 3/3 primary passes.
  These are diagnostic improvements, not proof of executed skill authoring or prose-method application.
  Native CW-17 non-trigger also changed from 1/3 to 3/3: all three candidate traces answered the detailed response-only request without invoking CW.
- **Complex prose:** [CW-19 r1](attempts/medium-r1-cw19-candidate/worksheet.md) and [r2](attempts/medium-r2-cw19-candidate/worksheet.md) replaced the inclusive mismatch stop threshold with “either metric breaches its limit.”
  The frozen criterion requires the explicit stop/escalation action at 0.1%, not merely a stricter readiness condition elsewhere.
  [r3](attempts/medium-r3-cw19-candidate/worksheet.md) preserved “reaches 0.1% or higher” and passed.
  The current-DD baseline had one failure of the same kind; the candidate had two.
- **Discovery:** [CW-13 r1](attempts/medium-r1-cw13-discovery-candidate/worksheet.md) demonstrated complete CW loading but not complete writing-skills loading before the decision.
  One read command's recorded output omitted requested skill text; later excerpts did not fill every gap.
  A sound final recommendation cannot substitute for the required exposure evidence.
  This is a failure to demonstrate full loading in the retained trace, not proof about unobservable provider context.
  The other two repetitions passed; 2/3 versus 1/3 is too small a sample for a decisive discovery claim.
- **Task fidelity:** 16 candidate observations contained unwanted model-authored narration; these remain separate FAILs despite passing primary criteria.
  All three CW-18 file-discovery runs loaded CW before creating the permitted guide, but all three added response narration.
  Full traces and all three saved guides were reviewed; final.txt alone would miss these failures.
- **Attribution:** short-prose tasks and loaded composition decisions already passed all no-DD and current-DD observations.
  Candidate passes therefore do not demonstrate incremental benefit on those tasks, and composition outcomes are not attributable solely to CW.
  The existing candidate predates this comparison, so this work does not establish RED-before-authoring chronology.

Three observations per condition are descriptive, not effectiveness estimates or a new acceptance threshold.
Reused controls are qualified as comparable but are not contemporaneous or matched pairs with equally numbered candidate repetitions; the baseline also spans the disclosed laptop-sleep interruption.
Discovery, transport, composition and contract results are not pooled into a prose-effectiveness percentage.
Prepared-input controls and trace audits do not establish absolute hermeticity: hidden provider inputs and automatic shell-startup behavior remain observability limits.

### Verification and retention

Fresh candidate collection used codex-cli 0.153.4, SHA-256 `b973d440acac501fd2594a43e7ca9ce41e0a65b9dfb28d0d7a7837c99e1261e3`, Codex / gpt-5.6-sol / medium.
The candidate body SHA-256 is `f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba`; its unchanged source is CW from `docs/comprehensive-skill-cleanup` at `13599fb7d3127334b0d07bfe468767e586ec5f9c`.
Only CW varied; surrounding skills, prompts, rubrics and native targets remained frozen.
The [approved command document](approval-commands.md), [preparation/qualification evidence](/private/tmp/skilltest-cw-candidate.pITN2u/qualification/summary.md), and ledger retain exact provenance.

The provider-free final audit rechecked all 66 complete bundles, frozen inputs, exact provider arguments, protected fixture/artifact hashes, terminal traces, per-attempt CLI captures and owned-runtime cleanup.
It reconciled every worksheet verdict with the ledger, verified 267 worksheet links, and rechecked accepted evidence checksums without rescoring or changing those records.
Command: `skill-validation/runner/.venv/bin/python /private/tmp/skilltest-cw-candidate.L4NdO8/final-audit.py`, from the frozen active worktree; [JSON result](final-audit.json), [stderr](final-audit-stderr.txt), [source](final-audit.py).
All 66 provider invocations completed with exit 0, no timeout, no provider/command stderr and no infrastructure retry.
Version checks retained the known PATH-alias warning; some internal read-only Git/search commands returned Xcode/cache, unborn-repository or absent-path diagnostics, disclosed in their worksheets.
Those internal diagnostics did not make the whole provider invocation fail; missing required read evidence was still scored as such.

Repository-required verification: `python3 -m pytest -q` from `skills/disciplined-development/hooks` in the active worktree: **263 passed, 3 skipped in 24.10s**, exit 0; [complete output](hooks-tests.txt).
No runner code/environment changed during collection; no additional runner suite was required under the runbook.
Main and the active feature worktree remain clean at their recorded revisions, matching their local origin tracking refs; no network fetch was used to claim remote freshness.
All new evidence remains in scratch; nothing was deployed, promoted into accepted/, committed or pushed, and no retained evidence was deleted.
Frozen repository documents intentionally retain their pre-approval checkboxes; this approved scratch record records collection completion without modifying the evaluated revision.

**Next checkpoint:** owner review of this comparison and its evidence, separate from approval to adopt the skill.
Recommended follow-up is a targeted discussion of CW-19 precision and the narration failures before deciding on edits; any new authoring or additional provider calls need their own agreed scope and approval.
Do not increase repetitions, broaden catalogs, change wording or package candidate evidence automatically.

## Approval

Owner approval: “approved, please continue”, recorded 2026-09-09 00:41:03 UTC (2026-09-08 local time).
Approval covers the unchanged 66-command document with SHA-256 `21b35b9dc5ea062f9f31af3fe92e0d8bc8186769f680070fb992a1fec6625c6b`, Codex / gpt-5.6-sol / medium, frozen revision `595f8e2bce0a62c5d4143ffebcdcf30cf8422b0d`, and its declared order/paths.
Repository plan checkboxes retain their frozen pre-approval state during collection; this dated scratch entry records the later approval without changing subject or evaluator inputs.
The original baseline approvals are exhausted and do not authorize this batch.

## Collection ledger

| Command | Repetition | Candidate scenario ID | Attempt | Status |
|---|---|---|---|---|
| 1 | 1 | cw-01-candidate-medium | `medium-r1-cw01-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw01-candidate/worksheet.md); exit 0 |
| 2 | 1 | cw-01-discovery-candidate-medium | `medium-r1-cw01-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw01-discovery-candidate/worksheet.md); exit 0 |
| 3 | 1 | cw-02-candidate-medium | `medium-r1-cw02-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw02-candidate/worksheet.md); exit 0 |
| 4 | 1 | cw-03-candidate-medium | `medium-r1-cw03-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw03-candidate/worksheet.md); exit 0 |
| 5 | 1 | cw-04-candidate-medium | `medium-r1-cw04-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw04-candidate/worksheet.md); exit 0 |
| 6 | 1 | cw-05-candidate-medium | `medium-r1-cw05-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw05-candidate/worksheet.md); exit 0 |
| 7 | 1 | cw-06-candidate-medium | `medium-r1-cw06-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw06-candidate/worksheet.md); exit 0 |
| 8 | 1 | cw-07-candidate-medium | `medium-r1-cw07-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r1-cw07-candidate/worksheet.md); exit 0 |
| 9 | 1 | cw-08-candidate-medium | `medium-r1-cw08-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r1-cw08-candidate/worksheet.md); exit 0 |
| 10 | 1 | cw-09-description-candidate-medium | `medium-r1-cw09-description-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw09-description-candidate/worksheet.md); exit 0 |
| 11 | 1 | cw-10-contract-candidate-medium | `medium-r1-cw10-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw10-contract-candidate/worksheet.md); exit 0 |
| 12 | 1 | cw-11-description-candidate-medium | `medium-r1-cw11-description-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw11-description-candidate/worksheet.md); exit 0 |
| 13 | 1 | cw-12-contract-candidate-medium | `medium-r1-cw12-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw12-contract-candidate/worksheet.md); exit 0 |
| 14 | 1 | cw-13-candidate-medium | `medium-r1-cw13-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r1-cw13-candidate/worksheet.md); exit 0 |
| 15 | 1 | cw-13-discovery-candidate-medium | `medium-r1-cw13-discovery-candidate` | [Primary FAIL; fidelity PASS](attempts/medium-r1-cw13-discovery-candidate/worksheet.md); exit 0 |
| 16 | 1 | cw-14-candidate-medium | `medium-r1-cw14-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw14-candidate/worksheet.md); exit 0 |
| 17 | 1 | cw-14-discovery-candidate-medium | `medium-r1-cw14-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw14-discovery-candidate/worksheet.md); exit 0 |
| 18 | 1 | cw-17-contract-candidate-medium | `medium-r1-cw17-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw17-contract-candidate/worksheet.md); exit 0 |
| 19 | 1 | cw-17-discovery-candidate-medium | `medium-r1-cw17-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw17-discovery-candidate/worksheet.md); exit 0 |
| 20 | 1 | cw-18-contract-candidate-medium | `medium-r1-cw18-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r1-cw18-contract-candidate/worksheet.md); exit 0 |
| 21 | 1 | cw-18-discovery-candidate-medium | `medium-r1-cw18-discovery-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r1-cw18-discovery-candidate/worksheet.md); exit 0 |
| 22 | 1 | cw-19-candidate-medium | `medium-r1-cw19-candidate` | [Primary FAIL; fidelity PASS](attempts/medium-r1-cw19-candidate/worksheet.md); exit 0 |
| 23 | 2 | cw-01-candidate-medium | `medium-r2-cw01-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw01-candidate/worksheet.md); exit 0 |
| 24 | 2 | cw-01-discovery-candidate-medium | `medium-r2-cw01-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw01-discovery-candidate/worksheet.md); exit 0 |
| 25 | 2 | cw-02-candidate-medium | `medium-r2-cw02-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw02-candidate/worksheet.md); exit 0 |
| 26 | 2 | cw-03-candidate-medium | `medium-r2-cw03-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw03-candidate/worksheet.md); exit 0 |
| 27 | 2 | cw-04-candidate-medium | `medium-r2-cw04-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r2-cw04-candidate/worksheet.md); exit 0 |
| 28 | 2 | cw-05-candidate-medium | `medium-r2-cw05-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r2-cw05-candidate/worksheet.md); exit 0 |
| 29 | 2 | cw-06-candidate-medium | `medium-r2-cw06-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r2-cw06-candidate/worksheet.md); exit 0 |
| 30 | 2 | cw-07-candidate-medium | `medium-r2-cw07-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r2-cw07-candidate/worksheet.md); exit 0 |
| 31 | 2 | cw-08-candidate-medium | `medium-r2-cw08-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r2-cw08-candidate/worksheet.md); exit 0 |
| 32 | 2 | cw-09-description-candidate-medium | `medium-r2-cw09-description-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw09-description-candidate/worksheet.md); exit 0 |
| 33 | 2 | cw-10-contract-candidate-medium | `medium-r2-cw10-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw10-contract-candidate/worksheet.md); exit 0 |
| 34 | 2 | cw-11-description-candidate-medium | `medium-r2-cw11-description-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw11-description-candidate/worksheet.md); exit 0 |
| 35 | 2 | cw-12-contract-candidate-medium | `medium-r2-cw12-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw12-contract-candidate/worksheet.md); exit 0 |
| 36 | 2 | cw-13-candidate-medium | `medium-r2-cw13-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw13-candidate/worksheet.md); exit 0 |
| 37 | 2 | cw-13-discovery-candidate-medium | `medium-r2-cw13-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw13-discovery-candidate/worksheet.md); exit 0 |
| 38 | 2 | cw-14-candidate-medium | `medium-r2-cw14-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r2-cw14-candidate/worksheet.md); exit 0 |
| 39 | 2 | cw-14-discovery-candidate-medium | `medium-r2-cw14-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw14-discovery-candidate/worksheet.md); exit 0 |
| 40 | 2 | cw-17-contract-candidate-medium | `medium-r2-cw17-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw17-contract-candidate/worksheet.md); exit 0 |
| 41 | 2 | cw-17-discovery-candidate-medium | `medium-r2-cw17-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw17-discovery-candidate/worksheet.md); exit 0 |
| 42 | 2 | cw-18-contract-candidate-medium | `medium-r2-cw18-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r2-cw18-contract-candidate/worksheet.md); exit 0 |
| 43 | 2 | cw-18-discovery-candidate-medium | `medium-r2-cw18-discovery-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r2-cw18-discovery-candidate/worksheet.md); exit 0 |
| 44 | 2 | cw-19-candidate-medium | `medium-r2-cw19-candidate` | [Primary FAIL; fidelity PASS](attempts/medium-r2-cw19-candidate/worksheet.md); exit 0 |
| 45 | 3 | cw-01-candidate-medium | `medium-r3-cw01-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw01-candidate/worksheet.md); exit 0 |
| 46 | 3 | cw-01-discovery-candidate-medium | `medium-r3-cw01-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw01-discovery-candidate/worksheet.md); exit 0 |
| 47 | 3 | cw-02-candidate-medium | `medium-r3-cw02-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r3-cw02-candidate/worksheet.md); exit 0 |
| 48 | 3 | cw-03-candidate-medium | `medium-r3-cw03-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw03-candidate/worksheet.md); exit 0 |
| 49 | 3 | cw-04-candidate-medium | `medium-r3-cw04-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw04-candidate/worksheet.md); exit 0 |
| 50 | 3 | cw-05-candidate-medium | `medium-r3-cw05-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw05-candidate/worksheet.md); exit 0 |
| 51 | 3 | cw-06-candidate-medium | `medium-r3-cw06-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw06-candidate/worksheet.md); exit 0 |
| 52 | 3 | cw-07-candidate-medium | `medium-r3-cw07-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw07-candidate/worksheet.md); exit 0 |
| 53 | 3 | cw-08-candidate-medium | `medium-r3-cw08-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw08-candidate/worksheet.md); exit 0 |
| 54 | 3 | cw-09-description-candidate-medium | `medium-r3-cw09-description-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw09-description-candidate/worksheet.md); exit 0 |
| 55 | 3 | cw-10-contract-candidate-medium | `medium-r3-cw10-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw10-contract-candidate/worksheet.md); exit 0 |
| 56 | 3 | cw-11-description-candidate-medium | `medium-r3-cw11-description-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r3-cw11-description-candidate/worksheet.md); exit 0 |
| 57 | 3 | cw-12-contract-candidate-medium | `medium-r3-cw12-contract-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r3-cw12-contract-candidate/worksheet.md); exit 0 |
| 58 | 3 | cw-13-candidate-medium | `medium-r3-cw13-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw13-candidate/worksheet.md); exit 0 |
| 59 | 3 | cw-13-discovery-candidate-medium | `medium-r3-cw13-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw13-discovery-candidate/worksheet.md); exit 0 |
| 60 | 3 | cw-14-candidate-medium | `medium-r3-cw14-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r3-cw14-candidate/worksheet.md); exit 0 |
| 61 | 3 | cw-14-discovery-candidate-medium | `medium-r3-cw14-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw14-discovery-candidate/worksheet.md); exit 0 |
| 62 | 3 | cw-17-contract-candidate-medium | `medium-r3-cw17-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw17-contract-candidate/worksheet.md); exit 0 |
| 63 | 3 | cw-17-discovery-candidate-medium | `medium-r3-cw17-discovery-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw17-discovery-candidate/worksheet.md); exit 0 |
| 64 | 3 | cw-18-contract-candidate-medium | `medium-r3-cw18-contract-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw18-contract-candidate/worksheet.md); exit 0 |
| 65 | 3 | cw-18-discovery-candidate-medium | `medium-r3-cw18-discovery-candidate` | [Primary PASS; fidelity FAIL](attempts/medium-r3-cw18-discovery-candidate/worksheet.md); exit 0 |
| 66 | 3 | cw-19-candidate-medium | `medium-r3-cw19-candidate` | [Primary PASS; fidelity PASS](attempts/medium-r3-cw19-candidate/worksheet.md); exit 0 |
