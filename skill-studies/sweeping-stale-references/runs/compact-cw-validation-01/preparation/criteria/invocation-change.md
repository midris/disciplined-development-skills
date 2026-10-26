# invocation-change: proposed CW-aligned validation

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `invocation-change`
Definition version: `3`
Status: draft; collection approval and freeze pending.
Purpose: extend the declared runtime/batch applicability while retaining the fixed case criteria.
Exposure: reconstructed development case; active author/preparer/assessor knows the evidence.

## Inputs and setup

The [proposal](../../../../../../plans/specs/2026-10-24-ssr-cw-aligned-validation.md) and [configuration index](../configuration-index.json) declare provider, mode and condition.
Controller policies/cards/expected facts remain outside subject context.
Require valid input identities, complete capture and actual availability/delivery checks; native missed loading is scored, not excluded as setup.

## Rules and evidence

Apply SSR-assessment-3 and the criterion text below, inherited from [invocation-change.md](../../../compact-regression-01/preparation/criteria/invocation-change.md).
This metadata version changes no criterion meaning, case-specific counting unit, valid alternative or failure consequence.
For local-change, finalist follows the existing Candidate P3 branch: any outside-file mutable match requires a positive inventory, including already-current or unrelated matches.
Other cases retain their own fixed accounting units; do not import semantic-delivery's four-block count.
Inspect full final projects, preserved meanings, traces and committed state; deterministic facts do not establish semantic correctness.

## Criteria

### F1: Complete useful change

Basis: Current [original skill](../../../../cases/skill-original/SKILL.md), [protocol contract](../../../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../../../../cases/initiating-change/task.md); severity follows [policy 3](../../../../cases/initiating-change/assessment-policy.txt).
Coverage: O1, O2 plus explicit task
Dimension: functional
Applies to: `finalist`
Judgment unit: Complete current project outcome
Required evidence: Final source/docs/configuration, script/runtime observations where applicable, and reference facts.
Met: The new service setting works across actual consumers; current explanations use session TTL and describe the unchanged behavior.
Not met: The requested correction remains incomplete or creates a contradictory current meaning.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Equivalent wording, organization or implementation preserving the requested outcome; follow relocated content.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F2: Preservation

Basis: Current [original skill](../../../../cases/skill-original/SKILL.md), [protocol contract](../../../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../../../../cases/initiating-change/task.md); severity follows [policy 3](../../../../cases/initiating-change/assessment-policy.txt).
Coverage: O2
Dimension: functional
Applies to: `finalist`
Judgment unit: Unrelated behavior, historical meanings and useful explanation
Required evidence: Compare complete original/final artifacts, supplied constraints and relevant runtime observations.
Met: Values, units, rejection of nonpositive duration, partner constraint/trade-off, historical record and independent vendor settings retain their meaning.
Not met: The change damages one of these protected meanings or behaviors.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Semantically equivalent edits; byte differences prompt inspection rather than automatic failure.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F3: Committed completeness

Basis: Current [original skill](../../../../cases/skill-original/SKILL.md), [protocol contract](../../../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../../../../cases/initiating-change/task.md); severity follows [policy 3](../../../../cases/initiating-change/assessment-policy.txt).
Coverage: O3 and task commit requirement
Dimension: functional
Applies to: `finalist`
Judgment unit: Committed result after neutral baseline
Required evidence: Retained Git history/tree and final working diff inspected against F1/F2.
Met: All required correct changes are committed.
Not met: Required work is missing/incorrect or remains uncommitted.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any complete acceptable repair; split commits do not fail this criterion.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### D1: Appropriate skill selection

Basis: SSR trigger description and owner-selected automatic-invocation question; [framework discovery requirement](../../../../../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#2-select-representative-tests).
Coverage: natural skill selection and timing
Dimension: procedural
Applies to: `finalist`
Judgment unit: Selection/read/action sequence after task delivery
Required evidence: Validated native availability and complete model-visible read/tool events, under the shared evidence rules.
Met: Selects SSR and receives its complete body before the first task reconciliation edit, without a task-level request to invoke it.
Not met: With availability and complete model-visible action evidence established, never loads SSR, receives only part before editing, or completes loading only after editing starts. Report missed, incomplete and late loading separately.
Insufficient evidence: Missing/truncated retained capture or ordering prevents determining what reached the model before editing. A complete trace showing a partial response with no remainder received before editing establishes incomplete loading, not an evidence gap.
Alternatives: Any native load/read mechanism, including multiple reads that collectively deliver the complete body before editing; relevant initial project inspection before the load is allowed. Naming SSR in the final answer is neither required nor sufficient.
Consequence: Report invocation separately; task success cannot compensate for D1 not met or unknown. No universal reliability estimate follows.
Overlap: A missed load and resulting task defect can share a cause; do not count them as independent failed executions.


## Limits

Declared provider strata remain separate. No contribution, held-out, full-catalog or population reliability claim.
