# invocation-review: compact finalist validation

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `invocation-review`
Definition version: `2`
Status: owner-approved compact-regression-01; freeze and readiness precede dispatch.
Purpose: validate the unchanged compact finalist using the existing case and fixed outcome/procedural boundaries.
Coverage/exposure: exposed reconstructed development case; sole condition finalist, no contemporaneous comparison/control or held-out claim.

## Inputs and setup

Inherited card: [assessment.md](../../../../cases/invocation-review/assessment.md).
The unchanged task/project/prompt are supplied by [configuration](../configs/invocation-review.json); only target body and declared model/test identity substitute for the earlier configuration.
Explicit cases require complete assigned-body delivery before reconciliation; native cases receive the ordinary catalog without a named skill/read instruction.
Reuse the pinned same-runtime qualification, verify actual catalog/body/tool events and retain every stopped attempt.

## Rules and evidence

Apply SSR-assessment-3 and the inherited criteria below without changing judgment units or consequences.
This definition extends condition applicability only; preserve historical definitions/scores.
For local-change, finalist follows the existing Candidate P3 branch: any outside-file mutable match requires a positive inventory, including already-current or unrelated matches.
Other cases retain their own fixed accounting units; do not import semantic-delivery's four-block count.
Inspect complete final projects, committed state and meaningful preservation; tests/string counts alone cannot establish correctness.
The unrelated case has D1 only and functional outcome not measured; explanation accuracy/preservation are descriptive observations.

## Criteria

### F1: Complete, useful documentation

Basis: Owner-clarified changed-behavior outcome, applied to the [task](../../../../cases/semantic-delivery/task.md).
Coverage: [Protocol obligations](../../../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: functional
Applies to: `finalist`
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
Coverage: [Protocol obligations](../../../../protocol.md#behavioral-contract-and-consumers) O2.
Dimension: functional
Applies to: `finalist`
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
Coverage: [Protocol obligations](../../../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: functional
Applies to: `finalist`
Judgment unit: All required repairs in Git history after the neutral baseline.
Required evidence: Inspect retained Git history, committed tree and final working diff against F1; do not infer completeness from a message or file count.
Met: All required repairs, including consolidated explanations and their references, are committed.
Not met: A required repair is incomplete/incorrect or remains only in the working tree.
Insufficient evidence: Retained Git history or final state is unavailable and committed completeness cannot be established.
Alternatives: Any complete solution accepted by F1; multiple commits do not fail this criterion.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair can also fail F1; grouping alone belongs to P2.

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

Single-provider exposed cases and two repetitions cannot establish population reliability, full-catalog competition, DD composition or broad transfer. Native selection and functional success remain distinct.
