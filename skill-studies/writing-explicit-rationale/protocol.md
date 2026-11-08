# Writing explicit rationale — study protocol

Format version: `1`
Study ID: `writing-explicit-rationale`
Status: draft. The owner selected WER, added the repeated-review case and accepted the reader-first output check. Case packages and frozen dispatch inputs are pending.
Plan: [current milestone](../../plans/2026-09-11-model-driven-skill-testing.md#wer-milestones)
General spec: [testing framework](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md)

## Sources and intended use

A future maintainer encounters a choice in a plan or in code without the original conversation. The study asks whether that person can recover the reason and accepted consequence from the edited tree. The [shipped WER skill](../../skills/writing-explicit-rationale/SKILL.md) was inspected at main revision `2a0e2499a39c2000fa2bab3152e12f41f26f038a`, SHA-256 `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`. Earlier scenarios supply fixture facts. All baseline results will come from fresh runs.

## Behavioral contract and consumers

WER should make consequential choices understandable at the decision site, preserve the supplied facts, and leave self-evident edits concise. Repeated review of the same decision should prompt an audit of related choices in the change. The subjects edit project artifacts. A fresh reviewer reads those artifacts as a maintainer would.

## Assessment policy

Separate task correctness, rationale placement, factual accuracy and timely native loading. Record what the reviewer could recover from the final tree before releasing the source facts, conversation, diff and final response. Use code replays to check behavior and human or agent judgment to evaluate meaning. Freeze criterion-level evidence rules and ambiguous examples before collection. [Reader-first procedure](../../plans/specs/2026-11-08-wer-focused-baseline.md#reader-first-output-check)

## Suite and evidence

| Proposed case | Behavior under test | Distinguishing evidence |
| --- | --- | --- |
| Defer XML export | A deliberate omission remains intelligible in the plan. | A reader recovers the retained scope, deferral reason and customer impact from the affected item. |
| Preserve prior quota | A surprising code choice carries the reason and trade-off. | Timing tests verify the policy. The code explains what immediate reset would break and the bounded exposure it accepts. |
| Rename a private helper | Routine work preserves existing rationale and avoids invented justification. | The rename works, the nearby quota explanation survives, and the diff adds no misleading rationale. |
| Address repeated review | The editor examines the change for other unexplained decisions. | The tree explains both the flagged guard and a second consequential choice. The routine edit stays concise. |

These are designed cases with zero collected observations. They cover plans and code, explicit application, native selection and a near-boundary routine edit. Standalone spec writing and transfer to unfamiliar tasks remain outside this focused screen. The [case design](../../plans/specs/2026-11-08-wer-focused-baseline.md#cases-and-acceptance) supplies the task details for packaging.

## Execution scope and authorization

Proposed: 16 application subjects (four cases × two providers × two conditions), followed on a passing checkpoint by eight native subjects and two read-only output reviews. One run per cell supports diagnosis. The selected providers are Codex and Claude. Runtime qualification, case cards, configs, manifests, exact schedule and frozen approval remain pending. [Run sequence](../../plans/specs/2026-11-08-wer-focused-baseline.md#proposed-run-sequence)

## Storage and accounting

WER has spent zero calls. Proposed ceilings are 24 subjects, two evaluators, zero authoring calls and zero retries. The estimate is 120–200 active minutes. Select the durable external store, verify retention and establish the batch index before collection. The settled CW/SSR budgets belong to their original studies.

## Results and decision

Baseline preparation is open. No model runs, scores or rewrite decision have been recorded.
