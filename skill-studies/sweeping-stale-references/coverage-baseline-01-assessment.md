# SSR expanded baseline: completed assessment

Format version: `2`
Assessment ID: ssr-coverage-baseline-01
Study / batch: sweeping-stale-references / coverage-baseline-01
Status: complete; all ten authorized attempts accounted for; one excluded, nine included
Scope and acceptance rules: [protocol](protocol.md) at Git `2c65cdc778b1ca9a00eb95fa09876d71515427a6`, batch coverage-baseline-01; frozen SSR policy 3 and case manifests. Runtime amendments and resumption authority at `1715dca1c7887db2f0c3a6157e4ad5d521483fb4` and `780e8ae1e8491a4bba30b39c7ab80bafcf397d14` are distinguished below.
Attempt index: [coverage-baseline-01-run-index.json](coverage-baseline-01-run-index.json) at Git `b2752402eb4ae9fe7c6c7e3961ccb971f6d249e2`, SHA-256 `ca293efd65b1976472904ad206b8564931df5bb894f8c7df882d39fcdbaf628c`.
Assessor and relevant session context: Codex active session with study history and owner decisions available; not independent or blind assessment. No immutable assessor model identity recorded.

## Coverage and execution results

All ten scheduled slots completed mechanically and were retained with verified inventories before subsequent dispatch.
Order 2 remains excluded and charged for observed outside-study exposure. There were no retries, replacements or extra model calls.
Nine valid observations comprise seven executable results and two accounting-only diagnostics; the latter have no functional-success denominator.
Only valid setups enter the aggregate counts. These are descriptive counts across explicitly different runtime strata, not estimates of population reliability or a silently pooled controlled comparison.

| Case / condition | Planned | Attempted | Included | Invalid setup | Setup unresolved | Unattempted |
| --- | --- | --- | --- | --- | --- | --- |
| initiating-change / original | 2 | 2 | 2 | 0 | 0 | 0 |
| initiating-change / control | 2 | 2 | 1 | 1 | 0 | 0 |
| local-change / control | 2 | 2 | 2 | 0 | 0 | 0 |
| local-change / original | 2 | 2 | 2 | 0 | 0 | 0 |
| large-sweep-account / original | 2 | 2 | 2 | 0 | 0 | 0 |

| Order | Case | Condition | Repetition | Setup / coverage | Recorded outcome | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | initiating-change | original | 1 | valid | met | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json) |
| 2 | initiating-change | control | 1 | invalid (excluded) | met | [coverage-baseline-01-initiating-change-control-1](results/20260921T211212148Z-ssr-initiating-change-control-b967dd0f-1583-4251-a066-0bc9d98fdd55-wnoe38hl.json) |
| 3 | local-change | control | 1 | valid | met | [coverage-baseline-01-local-change-control-1](results/20260922T014406033Z-ssr-local-change-control-714a7bf0-ad41-424a-af54-aff309df4b61-w62nponi.json) |
| 4 | local-change | original | 1 | valid | met | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json) |
| 5 | initiating-change | control | 2 | valid | met | [coverage-baseline-01-initiating-change-control-2](results/20260922T015349190Z-ssr-initiating-change-control-79451cb8-8fa9-417b-b4a5-127ffa0061a2-7ka7k342.json) |
| 6 | initiating-change | original | 2 | valid | met | [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| 7 | local-change | original | 2 | valid | met | [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| 8 | local-change | control | 2 | valid | met | [coverage-baseline-01-local-change-control-2](results/20260922T020250113Z-ssr-local-change-control-847212d3-796d-4747-ba42-c088bfda667a-u1v79kp1.json) |
| 9 | large-sweep-account | original | 1 | valid | not measured | [coverage-baseline-01-large-sweep-account-original-1](results/20260922T020446278Z-ssr-large-sweep-account-original-6617d9de-206b-4e4c-b4b0-be8391645517-zq4yl2iz.json) |
| 10 | large-sweep-account | original | 2 | valid | not measured | [coverage-baseline-01-large-sweep-account-original-2](results/20260922T020644081Z-ssr-large-sweep-account-original-66a4ab6e-a486-42ac-8438-e8e3e0112623-lm2lfyxe.json) |

## Aggregate results

| Case / condition / criterion | Met | Not met | Insufficient evidence | Not measured | Evidence |
| --- | --- | --- | --- | --- | --- |
| initiating-change / original / F1 | 2 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json), [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| initiating-change / original / F2 | 2 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json), [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| initiating-change / original / F3 | 2 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json), [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| initiating-change / original / P1 | 2 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json), [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| initiating-change / original / P2 | 2 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json), [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| initiating-change / original / P3 | 1 | 1 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json), [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| initiating-change / original / functional outcome | 2 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-original-1](results/20260921T210825089Z-ssr-initiating-change-original-ae5bac03-eb81-47f6-919b-b55ea5701e8e-_8ia6w1p.json), [coverage-baseline-01-initiating-change-original-2](results/20260922T015644024Z-ssr-initiating-change-original-fed3c27c-c26c-411c-969d-249324866880-pwxa8j_z.json) |
| initiating-change / control / F1 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-control-2](results/20260922T015349190Z-ssr-initiating-change-control-79451cb8-8fa9-417b-b4a5-127ffa0061a2-7ka7k342.json) |
| initiating-change / control / F2 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-control-2](results/20260922T015349190Z-ssr-initiating-change-control-79451cb8-8fa9-417b-b4a5-127ffa0061a2-7ka7k342.json) |
| initiating-change / control / F3 | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-control-2](results/20260922T015349190Z-ssr-initiating-change-control-79451cb8-8fa9-417b-b4a5-127ffa0061a2-7ka7k342.json) |
| initiating-change / control / functional outcome | 1 | 0 | 0 | 0 | [coverage-baseline-01-initiating-change-control-2](results/20260922T015349190Z-ssr-initiating-change-control-79451cb8-8fa9-417b-b4a5-127ffa0061a2-7ka7k342.json) |
| local-change / control / F1 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-control-1](results/20260922T014406033Z-ssr-local-change-control-714a7bf0-ad41-424a-af54-aff309df4b61-w62nponi.json), [coverage-baseline-01-local-change-control-2](results/20260922T020250113Z-ssr-local-change-control-847212d3-796d-4747-ba42-c088bfda667a-u1v79kp1.json) |
| local-change / control / F2 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-control-1](results/20260922T014406033Z-ssr-local-change-control-714a7bf0-ad41-424a-af54-aff309df4b61-w62nponi.json), [coverage-baseline-01-local-change-control-2](results/20260922T020250113Z-ssr-local-change-control-847212d3-796d-4747-ba42-c088bfda667a-u1v79kp1.json) |
| local-change / control / F3 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-control-1](results/20260922T014406033Z-ssr-local-change-control-714a7bf0-ad41-424a-af54-aff309df4b61-w62nponi.json), [coverage-baseline-01-local-change-control-2](results/20260922T020250113Z-ssr-local-change-control-847212d3-796d-4747-ba42-c088bfda667a-u1v79kp1.json) |
| local-change / control / functional outcome | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-control-1](results/20260922T014406033Z-ssr-local-change-control-714a7bf0-ad41-424a-af54-aff309df4b61-w62nponi.json), [coverage-baseline-01-local-change-control-2](results/20260922T020250113Z-ssr-local-change-control-847212d3-796d-4747-ba42-c088bfda667a-u1v79kp1.json) |
| local-change / original / F1 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json), [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| local-change / original / F2 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json), [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| local-change / original / F3 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json), [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| local-change / original / P1 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json), [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| local-change / original / P2 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json), [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| local-change / original / P3 | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json), [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| local-change / original / functional outcome | 2 | 0 | 0 | 0 | [coverage-baseline-01-local-change-original-1](results/20260922T015134286Z-ssr-local-change-original-cc79b383-c81f-40a9-9f53-ef0f549fd97d-pest8ltw.json), [coverage-baseline-01-local-change-original-2](results/20260922T015941616Z-ssr-local-change-original-6c538e26-5081-49d7-83bb-c006339f0b5b-82v2j_vx.json) |
| large-sweep-account / original / P3 | 2 | 0 | 0 | 0 | [coverage-baseline-01-large-sweep-account-original-1](results/20260922T020446278Z-ssr-large-sweep-account-original-6617d9de-206b-4e4c-b4b0-be8391645517-zq4yl2iz.json), [coverage-baseline-01-large-sweep-account-original-2](results/20260922T020644081Z-ssr-large-sweep-account-original-66a4ab6e-a486-42ac-8438-e8e3e0112623-lm2lfyxe.json) |
| large-sweep-account / original / functional outcome | 0 | 0 | 0 | 2 | [coverage-baseline-01-large-sweep-account-original-1](results/20260922T020446278Z-ssr-large-sweep-account-original-6617d9de-206b-4e4c-b4b0-be8391645517-zq4yl2iz.json), [coverage-baseline-01-large-sweep-account-original-2](results/20260922T020644081Z-ssr-large-sweep-account-original-66a4ab6e-a486-42ac-8438-e8e3e0112623-lm2lfyxe.json) |


## Findings

Initiating-change: the original meets F1–F3 in both repetitions; the one valid control also meets them.
Both newly delivered projects independently pass the three unit tests, default/custom expiry and nonpositive-duration probes, and script execution from the project and an external directory.
Whole-project inspection confirms the current rename, preserved partner constraint and refresh trade-off, and unchanged historical/vendor meanings.
The complete repair is committed in every inspectable attempt, including the excluded control; that control's individual judgments do not enter aggregates.

The first original's P3 failure remains: it claims 13 occurrences/9 updates while its own entries sum to 14/10.
The second original correctly accounts for 14 occurrences across nine paths: ten updates, two historical references and two false positives.
This is variability in the audit account, not a functional failure, proof of a particular wording cause, or a reason to rescore the first observation.
Both occurrence and matching-line units remain acceptable when internally consistent.

Local-change: both original and both control repetitions correctly commit only the glossary correction, preserving the unrelated shipping near-match, billing/membership meanings, JSON values and links.
Both guided repetitions search before editing, justify locality and provide the required negative-form account; P1–P3 are met.
Controls also inspect the project and deliver correct edits. They are not penalized for omitting an undisclosed SSR account.

Large-sweep-account: both reports preserve every supplied range/count, all eleven path/outcome groups and the two distinct outcomes in docs/cache.md.
Both reconcile 80 updates, 40 historical references and six false positives to 126 matches across ten unique paths, attributing those facts to the supplied inventory without claiming performed project repairs or tests.
P3 is met in both. Reading back REPORT.md is report inspection, not verification of the described project.
These results establish successful accounting on this supplied inventory, not search/repair effectiveness or behavior under brevity pressure.

## Runtime strata and inclusion

| Orders | Runtime / invocation authority | Observed result and limitation |
|---|---|---|
| 1–2 | Pre-isolation, `2c65cdc778b1ca9a00eb95fa09876d71515427a6` | One valid original; control excluded for delivered outside text; pre-isolation startup behavior |
| 3 | input-isolation-1, `1715dca1c7887db2f0c3a6157e4ad5d521483fb4` | Correct local control recovered from blocked user Git config and zsh heredoc; included with runtime friction; isolated login-shell default resolves Apple Python 3.9.6 / system Git |
| 4–10 | input-isolation-1 plus private-shell-1, `780e8ae1e8491a4bba30b39c7ab80bafcf397d14` | Seven valid observations; required operations available; no outside study material observed; isolated login-shell default resolves Apple Python 3.9.6 / system Git |

The interpreter labels for orders 3–10 are a retrospective reconstruction of their policy under the installed login shell, not a recorded version probe from each subject command.
The earlier runtime-1 Homebrew guarantee does not survive isolation; these cases did not exercise Shiv, whose Click dependency requires a newer interpreter.
Retained artifacts and scores remain unchanged; do not treat orders 1–10 as fixed-interpreter repetitions or use them to qualify a future Shiv run.
See the [login-shell correction](runtime-diagnosis.md#isolated-login-shell-correction-2026-09-23).

The shell repair explicitly forwards HOME and TMPPREFIX to already-granted private scratch; no filesystem grant expands.
The [resumption review](../../reviews/2026-09-21-ssr-resumption.md) records the offline regression and qualification evidence.
Order 7's optional Perl helper was blocked, then both links were checked with rg/sed. Order 8's parent-directory search was denied, then task work completed inside the fixture.
These observed recoveries preserve inspectable correct outcomes; they do not establish equal effort or latency across runtimes, nor universal tool availability.
The same private-shell-1 runtime provides one valid original/control repetition per executable case; neither pair shows a functional difference.
Do not attribute a procedural difference or recovered tool friction to the skill without stronger evidence.

### Historical contamination stop

Control result `coverage-baseline-01-initiating-change-control-1` cites the full delivered provider response at line 62 of its retained `provider-session.jsonl`.
The preceding command changes directory to `/tmp` to test the script, then runs a broad search without returning to the fixture.
The actual response contains controller scratch matches (`round5.py` and a prior Claude review transcript) and the preceding original run's completion report.
This is observed exposure, not an inference from filesystem accessibility or merely an unattempted command.
It occurs after the task patch and before final verification/commit; the record does not claim it caused the repair or that every matched byte reached the model.
The private runtime profile and restricted PATH did not enforce a read boundary around study material.
The declared contamination stop was applied; orders 3–10 resumed only after the qualified amendments.


Historical isolation check: the [round-9 trace audit](../../reviews/2026-09-21-round9-review.md#historical-trace-audit) found no targeted exposure markers in the 46 earlier attempts. It records seven stdout-only capture limits and does not establish exhaustive isolation; existing setup judgments and scores are unchanged.
The eight resumed attempts have full captured sessions, matched input hashes and no observed outside guidance. Full original skill delivery is present before task work in all five resumed guided attempts. Targeted marker checks supplement direct trace inspection, not a proof against every alias or unlogged access.

## Coverage judgment and next decision

The accepted expanded baseline is complete for its bounded purpose: small explicit-load SSR tasks now include ordinary initiating changes, reviewer-triggered repairs and justified locality, plus isolated accounting.
The protocol's [facet map](protocol.md#facet-coverage-audit-2026-09-21) distinguishes this measured evidence from remaining gaps: audit detail under genuine length pressure, comprehensive placement conformance, no-op handling, autonomous discovery, composition, difficult/ambiguous repositories and held-out transfer.
There is no new functional advantage over valid controls on these additions, and no new functional defect requiring a rewrite.
The isolated diagnostic passes do not erase the observed real-task arithmetic failure or establish its cause.

Recommendation: close this collection and retain the baseline. Select a bounded, evidence-led improvement question next; more scenarios are needed only if that question touches an accepted gap.
A reporting simplification is a plausible investigation, but one failure does not establish that a proposed edit will help. Judge any edit on the fixed relevant suite, including preservation of the passing local and diagnostic behaviors.
The pre-existing comprehensive candidate has not been run on these additions; its earlier comparison does not inherit their coverage.
No skill edit or adoption is authorized by completion. A future comparison needs explicit scope and call allocation because all 56 subject slots are spent.

## Cost and preservation

Ten runner durations total **1,011.135 seconds (16.9 minutes)**; the eight resumed attempts account for **771.611 seconds (12.9 minutes)**.
All ten raw bundles total 2,708,583 file bytes excluding sibling inventories/checks; every retained inventory and every new result evidence hash was reverified after inspection.
Billed dollar cost is not established. Active-session effort and the time-guideline variance belong to [combined accounting](../concise-writing/protocol.md#storage-and-accounting); runner duration is included there, not added twice.
