# Preserve prior quota

## Identity and purpose

Format version: `1`
Study ID: `writing-explicit-rationale`
Case ID: `quota-grace`
Definition version: `1`
Status: prepared for offline qualification
Purpose and mechanism: A maintainer might remove the grace period as a bug. Correct arithmetic alone cannot explain why an immediate reset would reject admitted work.
Development case in the [WER suite](../../../protocol.md#suite-and-evidence).

Application-only projection of the [source case card](../../../cases/quota-grace/assessment.md). Only shipped and control are scheduled.

## Inputs and setup

Supply [task](../../../cases/quota-grace/task.md) as the work request and only [fixture](../../../cases/quota-grace/fixture) as the editable project.
Use identical facts and project bytes in original, control and native conditions. The original arm explicitly receives the full skill, control has no target, and native uses ordinary catalog availability. Confirm the workspace and assigned exposure from captured inputs and traces. Missing evidence limits the affected judgment.

## Rules and evidence

Apply the [study policy](../../../protocol.md#assessment-policy) and [reader-first instructions](../../../cases/README.md#reader-first-check). In the second pass inspect the whole diff, original project and delivered response. The [worked repair](../../../cases/quota-grace/example.patch), card and controller checks stay outside subject inputs. Exact wording and line numbers are optional. Use committed or captured final project bytes; the work request does not require a commit.

## Criteria

### T1: Downgrade behavior

Basis: Task requirement.
Coverage: [Study coverage](../../../protocol.md#suite-and-evidence) for preserve prior quota.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Downgrade behavior in this execution.
Required evidence: Run fixture tests and the private [quota replay](../../../cases/quota-grace/replay.py) with the disposable project path. Inspect the diff and unchanged public contract.
Met: Old tokens use the higher limit from the change up to, but excluding, second 60. New tokens switch immediately. Upgrades, equal quotas and ordinary requests retain their behavior.
Not met: An old token loses quota early, keeps it at expiry, or a new token gets the old quota.
Insufficient evidence: Required artifact, source fact or ordered evidence is unavailable or cannot settle the distinction.
Alternatives: Accept any implementation or wording that preserves the supplied meaning and meets this evidence rule.
Consequence: A material miss leaves this part of the delivered task incomplete.
Overlap: Report a shared cause once when explaining multiple affected criteria.

### R1: Decision-site rationale

Basis: Shipped WER trigger and artifact contract.
Coverage: [Study coverage](../../../protocol.md#suite-and-evidence) for preserve prior quota.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Decision-site rationale in this execution.
Required evidence: Read the final quota decision and its surrounding source before the task or replay.
Met: From the decision site a maintainer can recover the in-flight old-token reason, what an immediate cut would reject and the accepted, bounded elevated quota. Readable code can establish the exact duration alongside the explanation.
Not met: The explanation implies all tokens or requests retain the old quota, only the duration is restated, a different risk is invented, or the reason exists solely in a response or in the subject’s commit message.
Insufficient evidence: Required artifact, source fact or ordered evidence is unavailable or cannot settle the distinction.
Alternatives: Accept any implementation or wording that preserves the supplied meaning and meets this evidence rule.
Consequence: A material miss leaves this part of the delivered task incomplete.
Overlap: Report a shared cause once when explaining multiple affected criteria.


## Limits

One exposed development fixture measures this decision in this context. Offline worked variants establish checker behavior and scoring boundaries. Provider effectiveness and selection require fresh subject evidence.
