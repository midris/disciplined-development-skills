# Defer XML export

## Identity and purpose

Format version: `1`
Study ID: `writing-explicit-rationale`
Case ID: `export-deferral`
Definition version: `2`
Status: prepared for offline qualification
Purpose and mechanism: The PR summary offers an easy place to put a correct explanation that will be missing from the release plan.
Development case in the [WER suite](../../../protocol.md#suite-and-evidence).

Application-only projection of the [source case card](../../../cases/export-deferral/assessment.md). Only shipped and control are scheduled.

## Inputs and setup

Supply [task](../../../cases/export-deferral/task.md) as the work request and only [fixture](../../../cases/export-deferral/fixture) as the editable project.
Use identical facts and project bytes in original, control and native conditions. The original arm explicitly receives the full skill, control has no target, and native uses ordinary catalog availability. Confirm the workspace and assigned exposure from captured inputs and traces. Missing evidence limits the affected judgment.

## Rules and evidence

Apply the [study policy](../../../protocol.md#assessment-policy) and [reader-first instructions](../../../cases/README.md#reader-first-check). In the second pass inspect the whole diff, original project and delivered response. The [worked repair](../../../cases/export-deferral/example.patch), card and controller checks stay outside subject inputs. Exact wording and line numbers are optional. Use committed or captured final project bytes; the work request does not require a commit.

## Criteria

### T1: Release scope and handoff

Basis: Task requirement.
Coverage: [Study coverage](../../../protocol.md#suite-and-evidence) for defer xml export.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Release scope and handoff in this execution.
Required evidence: Compare the entire release plan and delivered PR summary with the supplied decision and original plan.
Met: CSV and JSON still ship in v1, XML is deferred, other milestones retain their meaning and a short accurate PR summary is supplied.
Not met: The final plan still promises XML in v1, a retained format or milestone is removed, a new deadline is promised, or the requested summary is missing.
Insufficient evidence: Required artifact, source fact or ordered evidence is unavailable or cannot settle the distinction.
Alternatives: Accept any implementation or wording that preserves the supplied meaning and meets this evidence rule.
Consequence: A material miss leaves this part of the delivered task incomplete.
Overlap: Report a shared cause once when explaining multiple affected criteria.

### R1: Reason at the release item

Basis: Shipped WER trigger and artifact contract.
Coverage: [Study coverage](../../../protocol.md#suite-and-evidence) for defer xml export.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Reason at the release item in this execution.
Required evidence: Read the final release plan before the team message or PR summary.
Met: At the affected item a reader can identify the retained v1 scope, XML deferral pending partner approval of a stable schema, and the resulting wait for XML customers. When these are clear, leaving ongoing schema churn implicit is a precision observation. A clearly connected Later item can carry the deferral if a reader of the v1 scope can find it. Equivalent concise wording passes.
Not met: The item silently drops XML, leaves its return date unexplained, assigns approval to the wrong party, or the reason appears only in the PR or in the subject’s commit message.
Insufficient evidence: Required artifact, source fact or ordered evidence is unavailable or cannot settle the distinction.
Alternatives: Accept any implementation or wording that preserves the supplied meaning and meets this evidence rule.
Consequence: A material miss leaves this part of the delivered task incomplete.
Overlap: Report a shared cause once when explaining multiple affected criteria.


## Limits

One exposed development fixture measures this decision in this context. Offline worked variants establish checker behavior and scoring boundaries. Provider effectiveness and selection require fresh subject evidence.
