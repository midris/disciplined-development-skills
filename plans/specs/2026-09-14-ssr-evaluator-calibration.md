# SSR evaluator calibration proposal

Status: draft for owner review; no evaluator dispatch or baseline freeze authorized.
Governed by the [framework](2026-09-11-model-driven-skill-testing-framework.md), [active plan](../2026-09-11-model-driven-skill-testing.md) and [SSR policy](../../skill-studies/sweeping-stale-references/protocol.md#current-ssr-assessment-policy).

## Decision this calibration supports

Can the selected evaluator distinguish correct, preserved and committed semantic repairs from consequential errors, while reporting accounting/grouping separately and recognizing missing evidence?
Use two fresh Codex Sol-low evaluations with runner `read-only` permissions, matching the owner's initial-model preference.
This is a proposed configuration, not evidence that Sol-low will qualify.
Repeat the same examples under neutral identifiers in different orders; neither call receives the other response or the reference judgments.
Two disjoint batches would cover more examples but would not test repeatability on the same distinctions.
A larger model or extra calls are possible later repairs, not assumed dependencies of this proposal.

## Prepared examples

The [draft package](../../skill-studies/sweeping-stale-references/evaluation/calibration-draft/README.md) contains eleven constructed document/Git examples, not eleven subject runs.
Most reuse the semantic case's retained reconstructions; additional account/grouping variants are created only for evaluator calibration.
The controller reference matrix names their provenance and expected judgments; evaluators receive neutral snapshots, task/criteria/policy and captured Git/runtime facts without that matrix.

| Contrast | Required distinction |
|---|---|
| Complete repair with sparse versus full accounting | Both succeed functionally; useful accounting differs. |
| README-only repair with a complete, truthful account | Remaining current errors still fail; the account explicitly lists unfinished repairs. |
| Blanket number replacement | Current delivery guidance can be correct while preservation fails. |
| Attempts versus retries; exactly four sends | Wrong quantity or loss of early-stop meaning fails despite passing runtime checks. |
| Removed explanations versus effective consolidation | Deletion without replacement fails; useful restructuring succeeds. |
| Correct working tree, no repair commit | Documentation succeeds; committed completeness fails. |
| Complete repair across two commits | Committed completeness succeeds; single-commit procedure fails non-blockingly. |
| Correct snapshot with Git evidence withheld | Do not infer committed work or absent accounting from missing evidence. |

No action streams are supplied in these examples: P1 must remain insufficient evidence.
This tests the missing-trace rule, not positive/negative search-order interpretation.
Before baseline use of model-scored P1, add and qualify retained-trace contrasts under an explicitly revised package/allocation; these two calls alone cannot close that item.
Likewise this semantic package does not qualify every possible Shiv/path refactor or establish population reliability.

## Evidence and response contract

The evaluator reads only the shared baseline, current policy/criteria/task and the eleven neutral records named in its batch list.
Each record supplies the final project snapshot, independently observed runtime facts and, except the deliberate missing-evidence example, actual local Git history/diffs/status.
Commit messages are evidence to check against the repair, not instructions or ground truth.
All examples share the same declared accounting expectations; they are not original/control condition comparisons.

The [draft evaluator instructions](../../skill-studies/sweeping-stale-references/evaluation/calibration-draft/instructions.md) request F1–F3 and P1–P3 judgments, evidence locations, consequences and a functional summary for each record.
Allowed judgments remain `met`, `not met`, `insufficient evidence`.
Exact prose/table spelling is not a semantic acceptance gate; omitted judgments or untraceable reasons require inspection.
This draft response contract must be reconciled with the shared assessment format before collection, not treated as a second permanent format standard.

## Proposed acceptance and two-call sequence

Before either call, freeze these bytes, the controller reference key, accepted distinctions, model/effort, permission mode and evidence-access mechanism.
Call 1 uses batch A. Inspect its setup and evidence-backed judgments against the key.
Stop if setup is invalid or a material assessment error appears; do not spend call 2 merely to see whether it gets lucky.
If call 1 meets the criteria, call 2 uses the unchanged package in fresh context with batch B's different order/identifiers.
No prompt adjustment or coaching between calls; a changed evaluator is a new version needing new qualification and authorization.

For qualification, both calls must get every supplied functional judgment and every declared procedural distinction right, including uncertainty, with supporting evidence and no contradictory functional summary.
No allowance for decision-changing errors; wording differences or accurate additional observations are acceptable.
Assess reasoning as well as labels: a correct label supported by invented evidence does not qualify.
The controller inspects reasons; deterministic checks can later validate record coverage, identifiers and allowed labels, but do not decide documentation meaning.
These two observations establish only success on the constructed distinctions, not an evaluator error rate.
If an apparent disagreement exposes ambiguity in the reference key, resolve it with the owner and version the correction rather than automatically faulting the evaluator.

Two calls fit the existing evaluator-calibration allocation: evaluator use would become 2/12 if both run; subject use remains 4/40.
Failed attempts are retained and charged under the declared role/retry policy; no automatic repair or extra invocation follows.
Apply the protocol's [semantic-calibration fallback](../../skill-studies/sweeping-stale-references/protocol.md#proposed-baseline-case-selection) if this scope cannot qualify.

## Readiness still required before requesting dispatch

The package is reviewable, not dispatch-ready.
The runner's read-only enforcement protects supplied evidence from mutation; it does not prevent reads of the canonical checkout containing the answer key.
Neutral copied inputs establish answer omission, not host-wide answer secrecy.
Settle and verify the read boundary, or present a bounded audit-based concealment limitation and its effect for owner approval before relying on calibration; do not call directory separation isolation.
Prepare exact runner configs, verify copies and full final-output capture, and record provider/CLI identity, command, primary/backup retention and authorization.
Keep controller answers, reconstruction source names and previous responses out of evaluator fixtures.
Then present the two exact calls alongside the still-pending whole-study call/time allocation.
