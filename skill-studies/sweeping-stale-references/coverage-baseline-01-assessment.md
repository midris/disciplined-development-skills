# SSR expanded baseline: partial assessment

Format version: `2`
Assessment ID: ssr-coverage-baseline-01
Study / batch: sweeping-stale-references / coverage-baseline-01
Status: stopped after two attempts; partial assessment complete; eight slots unrun
Scope and acceptance rules: [protocol](protocol.md) at Git `2c65cdc778b1ca9a00eb95fa09876d71515427a6`, batch coverage-baseline-01; frozen SSR policy 3 and case manifests.
Attempt index: [coverage-baseline-01-run-index.json](coverage-baseline-01-run-index.json) at Git `83a581dd3b1c32e17986d55e1273df1139a5f1b6`, SHA-256 `6855aafaef0cd9c2e802ee589b859a3b03ebe781280482beee7cb39255da6f35`.
Assessor and relevant session context: Codex active session with study history and owner decisions available; not independent or blind assessment. No immutable assessor model identity recorded.

## Coverage and execution results

Ten slots were planned: two original/control repetitions on each executable case and two original-only accounting diagnostics.
Orders 1–2 completed and were retained with verified inventories; orders 3–10 were not dispatched after the control exposed outside-study material.
No retry or replacement occurred. All actual attempts are included in coverage; only the valid original enters outcome counts.
All execution-result records resolve through the pinned attempt index.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| initiating-change / original | 2 | 1 | 1 | 0 | 0 | 1 |
| initiating-change / control | 2 | 1 | 0 | 1 | 0 | 1 |
| local-change / control | 2 | 0 | 0 | 0 | 0 | 2 |
| local-change / original | 2 | 0 | 0 | 0 | 0 | 2 |
| large-sweep-account / original | 2 | 0 | 0 | 0 | 0 | 2 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | initiating-change | original | 1 | valid | met | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| 2 | initiating-change | control | 1 | invalid (excluded) | met | [coverage-baseline-01-initiating-change-control-1](results/20260921T211212148Z-ssr-initiating-change-control-b967dd0f-1583-4251-a066-0bc9d98fdd55-wnoe38hl.json) |
| 3 | local-change | control | 1 | unattempted | not assessed | none |
| 4 | local-change | original | 1 | unattempted | not assessed | none |
| 5 | initiating-change | control | 2 | unattempted | not assessed | none |
| 6 | initiating-change | original | 2 | unattempted | not assessed | none |
| 7 | local-change | original | 2 | unattempted | not assessed | none |
| 8 | local-change | control | 2 | unattempted | not assessed | none |
| 9 | large-sweep-account | original | 1 | unattempted | not assessed | none |
| 10 | large-sweep-account | original | 2 | unattempted | not assessed | none |

## Aggregate results

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| initiating-change / original / F1 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| initiating-change / original / F2 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| initiating-change / original / F3 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| initiating-change / original / P1 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| initiating-change / original / P2 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| initiating-change / original / P3 | 0 | 1 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| initiating-change / original / functional outcome | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| initiating-change / control / F1 | 0 | 0 | 0 | 0 | none |
| initiating-change / control / F2 | 0 | 0 | 0 | 0 | none |
| initiating-change / control / F3 | 0 | 0 | 0 | 0 | none |
| initiating-change / control / functional outcome | 0 | 0 | 0 | 0 | none |
| local-change / control / F1 | 0 | 0 | 0 | 0 | none |
| local-change / control / F2 | 0 | 0 | 0 | 0 | none |
| local-change / control / F3 | 0 | 0 | 0 | 0 | none |
| local-change / control / functional outcome | 0 | 0 | 0 | 0 | none |
| local-change / original / F1 | 0 | 0 | 0 | 0 | none |
| local-change / original / F2 | 0 | 0 | 0 | 0 | none |
| local-change / original / F3 | 0 | 0 | 0 | 0 | none |
| local-change / original / P1 | 0 | 0 | 0 | 0 | none |
| local-change / original / P2 | 0 | 0 | 0 | 0 | none |
| local-change / original / P3 | 0 | 0 | 0 | 0 | none |
| local-change / original / functional outcome | 0 | 0 | 0 | 0 | none |
| large-sweep-account / original / P3 | 0 | 0 | 0 | 0 | none |
| large-sweep-account / original / functional outcome | 0 | 0 | 0 | 0 | none |

Only valid setups enter the table. Zero rows mean no included observations, not failure or success.
The diagnostic remains unrun: its functional result would be not measured, but no unexecuted slot is counted as an observed not-measured outcome.
The table generator selected three outcome columns because both available records are version 1; the version-2 assessment adds the required zero Not measured column without changing counts.

The one valid original meets F1–F3 and P1–P2; P3 is not met.
Its complete sweep account correctly identifies paths, locations and dispositions, but the supplied total says 13 occurrences/9 updates while its entries sum to 14 occurrences/10 updates.
That is an internal arithmetic defect under its stated unit; the criterion accepts either consistent occurrence or matching-line counts.
The defect affects the audit account and does not invalidate the committed repair.

Independent probes on disposable copies of both delivered projects pass: three unit tests, default/custom expiry calculations, rejection of zero/negative durations, and script execution from the project and an external directory.
Complete diffs preserve the partner constraint, accepted refresh trade-off, archive and vendor meanings; both correct repairs are committed after exact neutral baselines.
The control's individual functional judgments are therefore met, but its invalid setup excludes those judgments from comparison aggregates.

## Collection stop and interpretation

Control result `coverage-baseline-01-initiating-change-control-1` cites the full delivered provider response at line 62 of its retained `provider-session.jsonl`.
The preceding command changes directory to `/tmp` to test the script, then runs a broad search without returning to the fixture.
The actual response contains controller scratch matches (`round5.py` and a prior Claude review transcript) and the preceding original run's completion report.
This is observed exposure, not an inference from filesystem accessibility or merely an unattempted command.
It occurs after the task patch and before final verification/commit; the record does not claim it caused the repair or that every matched byte reached the model.
The private runtime profile and restricted PATH did not enforce a read boundary around study material.
The declared contamination stop applies; no further subject was dispatched.

Acceptance is descriptive-only. This partial batch provides one successful initiating-change original observation and one genuine reporting inconsistency, with no valid control comparison or repetition evidence.
It does not establish the full expanded baseline, local-change behavior, isolated diagnostic performance, a skill contribution, or readiness for a rewrite.
The targeted historical trace audit below found no corresponding markers in earlier retained traces; its capture and search limits apply.
The [protocol checkpoint](protocol.md#coverage-baseline-coverage-baseline-01) owns recovery: the qualified input-isolation-1 amendment governs remaining slots; retain the excluded attempt without automatic replacement.
Current spending and revised effort forecast are in [combined accounting](../concise-writing/protocol.md#storage-and-accounting).

Historical isolation check: the [round-9 trace audit](../../reviews/2026-09-21-round9-review.md#historical-trace-audit) found no targeted exposure markers in the 46 earlier attempts. It records seven stdout-only capture limits and does not establish exhaustive isolation; existing setup judgments and scores are unchanged.
