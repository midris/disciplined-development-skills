# Recognize an initiating rename

## Identity and purpose

Format version: `1`
Study ID: sweeping-stale-references
Case ID: invocation-change
Definition version: `1`
Status: accepted for comprehensive-comparison-02; collection authority and input freeze belong to the protocol.
Purpose and realistic failure opportunity: A requested setting rename should trigger SSR before reconciliation edits.
Scenario mechanism: The skill catalog provides a route to selection without a task-level cue to read SSR; retained loading events distinguish invocation from an independently correct answer.
Protocol coverage and membership/exposure: [facet map](../../protocol.md#facet-coverage-audit-2026-09-21); exposed development case in [preparation](../../invocation-pressure-preparation.md).

## Inputs and setup

Task: [task.md](task.md); [original configuration](original.json); [candidate configuration](candidate.json); [prompt](prompt.md).
The configuration supplies SSR as the only project skill for native discovery; the prompt does not name it or instruct a skill read. Original/candidate differ only in the supplied skill bytes. There is no no-target condition: an absent skill cannot answer a discovery question.
Project bytes reuse the [initiating-change fixture](../initiating-change/fixture/README.md); the parent case and expected facts are controller-only.
The neutral fixture-baseline commit is setup, not task work or an SSR trigger being scored.
A task commit is required.
Native catalog delivery, version/path identity and full action capture must meet the shared setup gate before D1 can be judged.
The comparison-02 manifest pins model/effort and source identities; the protocol owns allocation.

## Rules and evidence

Use the shared [invocation evidence rules](../../invocation-pressure-preparation.md#invocation-evidence-and-judgments). Apply [SSR policy 3](../../assessment-policies/SSR-assessment-3.txt) to task outcomes, with D1 separately recording selection and timing. D1 is procedural for schema purposes, but a correct task outcome does not count as successful invocation when D1 is not met.
Inspect complete task artifacts, Git state and delivered tool events; source-file presence and self-reported invocation are insufficient.
Reuse the [initiating-change case](../initiating-change/assessment.md) and its controller reference facts for task meaning, valid alternatives and preservation.
Controller reference facts: [expected.md](../initiating-change/expected.md); inherited criteria use these facts, not an absent local copy.
Missing evidence remains insufficient evidence; invalid availability is a setup problem, not an invocation failure.

## Criteria

Original and candidate use the same F1–F3 and D1 criteria; no control or P1–P3 judgment is defined for this discovery case.


### F1: Complete useful change

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../initiating-change/task.md); severity follows [policy 3](../initiating-change/assessment-policy.txt).
Coverage: O1, O2 plus explicit task
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Complete current project outcome
Required evidence: Final source/docs/configuration, script/runtime observations where applicable, and reference facts.
Met: The new service setting works across actual consumers; current explanations use session TTL and describe the unchanged behavior.
Not met: The requested correction remains incomplete or creates a contradictory current meaning.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Equivalent wording, organization or implementation preserving the requested outcome; follow relocated content.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F2: Preservation

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../initiating-change/task.md); severity follows [policy 3](../initiating-change/assessment-policy.txt).
Coverage: O2
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Unrelated behavior, historical meanings and useful explanation
Required evidence: Compare complete original/final artifacts, supplied constraints and relevant runtime observations.
Met: Values, units, rejection of nonpositive duration, partner constraint/trade-off, historical record and independent vendor settings retain their meaning.
Not met: The change damages one of these protected meanings or behaviors.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Semantically equivalent edits; byte differences prompt inspection rather than automatic failure.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F3: Committed completeness

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../initiating-change/task.md); severity follows [policy 3](../initiating-change/assessment-policy.txt).
Coverage: O3 and task commit requirement
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Committed result after neutral baseline
Required evidence: Retained Git history/tree and final working diff inspected against F1/F2.
Met: All required correct changes are committed.
Not met: Required work is missing/incorrect or remains uncommitted.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any complete acceptable repair; split commits do not fail this criterion.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### D1: Appropriate skill selection

Basis: SSR trigger description and owner-selected automatic-invocation question; [framework discovery requirement](../../../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#2-select-representative-tests).
Coverage: natural skill selection and timing
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Selection/read/action sequence after task delivery
Required evidence: Validated native availability and complete model-visible read/tool events, under the shared evidence rules.
Met: Selects SSR and receives its complete body before the first task reconciliation edit, without a task-level request to invoke it.
Not met: With availability and complete model-visible action evidence established, never loads SSR, receives only part before editing, or completes loading only after editing starts. Report missed, incomplete and late loading separately.
Insufficient evidence: Missing/truncated retained capture or ordering prevents determining what reached the model before editing. A complete trace showing a partial response with no remainder received before editing establishes incomplete loading, not an evidence gap.
Alternatives: Any native load/read mechanism, including multiple reads that collectively deliver the complete body before editing; relevant initial project inspection before the load is allowed. Naming SSR in the final answer is neither required nor sufficient.
Consequence: Report invocation separately; task success cannot compensate for D1 not met or unknown. No universal reliability estimate follows.
Overlap: A missed load and resulting task defect can share a cause; do not count them as independent failed executions.

## Limits

Small exposed synthetic tasks with one naturally available target skill do not establish selection among a full competing catalog, DD orchestration, provider transfer or population reliability.
The original and current comprehensive candidate have identical descriptions; any discovery difference cannot automatically be attributed to improved trigger wording.
