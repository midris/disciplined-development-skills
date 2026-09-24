# Recognize a reviewer-triggered sweep

## Identity and purpose

Format version: `1`
Study ID: sweeping-stale-references
Case ID: invocation-review
Definition version: `1`
Status: draft for owner review; offline preparation only; no collection authorized
Purpose and realistic failure opportunity: A reviewer names one README defect while related semantic references remain stale.
Scenario mechanism: The skill catalog provides a route to selection without a task-level cue to read SSR; retained loading events distinguish invocation from an independently correct answer.
Protocol coverage and membership/exposure: [facet map](../../protocol.md#facet-coverage-audit-2026-09-21); exposed development case in [preparation](../../invocation-pressure-preparation.md).

## Inputs and setup

Task: [task.md](task.md); [original configuration](original.json); [candidate configuration](candidate.json); [prompt](prompt.md).
The configuration supplies SSR as the only project skill for native discovery; the prompt does not name it or instruct a skill read. Original/candidate differ only in the supplied skill bytes. There is no no-target condition: an absent skill cannot answer a discovery question.
Project bytes reuse the [semantic-delivery fixture](../semantic-delivery/fixture/README.md); the parent case and expected facts are controller-only.
The neutral fixture-baseline commit is setup, not task work or an SSR trigger being scored.
A task commit is required.
Native catalog delivery, version/path identity and full action capture must meet the shared setup gate before D1 can be judged.
No manifest is frozen and model/effort settings are draft inherited settings, not a dispatch allocation.

## Rules and evidence

Use the shared [invocation evidence rules](../../invocation-pressure-preparation.md#invocation-evidence-and-judgments). Apply [SSR policy 3](../../assessment-policies/SSR-assessment-3.txt) to task outcomes, with D1 separately recording selection and timing. D1 is procedural for schema purposes, but a correct task outcome does not count as successful invocation when D1 is not met.
Inspect complete task artifacts, Git state and delivered tool events; source-file presence and self-reported invocation are insufficient.
Reuse the [semantic-delivery case](../semantic-delivery/assessment.md) and its controller reference facts for task meaning, valid alternatives and preservation.
Controller reference facts: [expected.json](../semantic-delivery/expected.json); inherited criteria use these facts, not an absent local copy.
Missing evidence remains insufficient evidence; invalid availability is a setup problem, not an invocation failure.

## Criteria

Original and candidate use the same F1–F3 and D1 criteria; no control or P1–P3 judgment is defined for this discovery case.


### F1: Complete, useful documentation

Basis: Owner-clarified changed-behavior outcome, applied to the [task](../semantic-delivery/task.md).
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Current delivery documentation as a whole, serving overview, operations and troubleshooting readers.
Required evidence: Inspect all final documents against task/code behavior and expected.json current reference IDs, following moved content. Runtime observations support behavior, not prose correctness.
Met: All current descriptions agree on at most four total sends, up to three retries after initial failure, exhaustion after four consecutive failures, and immediate stopping on success; useful explanations remain.
Not met: A stale or contradictory current claim remains, attempts and retries are confused, four sends are unconditional, or useful guidance is removed without an effective replacement.
Insufficient evidence: Required final documents or their replacements cannot be inspected, or evidence cannot resolve their meaning.
Alternatives: Accurate prose, tables, reordering or consolidation with working cross-references serving all original document roles; changing all three original files is not required.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair can also fail F3; identify the shared cause, not two independent failed executions.

### F2: Preservation

Basis: Task constraints and SSR Procedure 2 triage, under the owner-clarified whole-artifact policy.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O2.
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Worker/helper behavior, historical meaning and unrelated operational guidance.
Required evidence: Inspect code, final documents and changes; compare disposable runtime observations with expected.json. Byte differences initiate semantic inspection.
Met: The worker retains settled behavior, the independent helper retains its three-attempt limit, and historical meaning and unrelated useful guidance are preserved.
Not met: Settled behavior, independent helper behavior, historical meaning or unrelated useful guidance is damaged.
Insufficient evidence: Required artifacts or runtime evidence are missing/conflicting and inspection cannot establish preservation.
Alternatives: Equivalent implementation, wording or structure that preserves the behavior and meaning; see shared replay limits.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: A harmful documentation change may also fail F1; report the shared cause.

### F3: Committed repair

Basis: Explicit task commit request and SSR Procedure 3, with owner clarification that complete committed outcome leads.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: All required repairs in Git history after the neutral baseline.
Required evidence: Inspect retained Git history, committed tree and final working diff against F1; do not infer completeness from a message or file count.
Met: All required repairs, including consolidated explanations and their references, are committed.
Not met: A required repair is incomplete/incorrect or remains only in the working tree.
Insufficient evidence: Retained Git history or final state is unavailable and committed completeness cannot be established.
Alternatives: Any complete solution accepted by F1; multiple commits do not fail this criterion.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair can also fail F1; grouping alone belongs to P2.

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
