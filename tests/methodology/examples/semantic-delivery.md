# Worked semantic criterion

A delivery worker now makes an initial attempt and up to three retries. The case asks whether the agent reconciles differently worded guidance across the project.

### F1: Complete, useful documentation

Basis: Owner-clarified changed-behavior outcome, applied to the [task](https://github.com/midris/disciplined-development-skills/blob/44766517c4550cd65c13c9fe0f489ac26efee1e0/skill-studies/sweeping-stale-references/cases/semantic-delivery/task.md).
Coverage: [Protocol obligations](https://github.com/midris/disciplined-development-skills/blob/44766517c4550cd65c13c9fe0f489ac26efee1e0/skill-studies/sweeping-stale-references/protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: functional
Applies to: `original`, `control`, `candidate`
Judgment unit: Current delivery documentation as a whole, serving overview, operations and troubleshooting readers.
Required evidence: Inspect all final documents against task/code behavior and expected.json current reference IDs, following moved content. Runtime observations support behavior, not prose correctness.
Met: All current descriptions agree on at most four total sends, up to three retries after initial failure, exhaustion after four consecutive failures, and immediate stopping on success; useful explanations remain.
Not met: A stale or contradictory current claim remains, attempts and retries are confused, four sends are unconditional, or useful guidance is removed without an effective replacement.
Insufficient evidence: Required final documents or their replacements cannot be inspected, or evidence cannot resolve their meaning.
Alternatives: Accurate prose, tables, reordering or consolidation with working cross-references serving all original document roles; changing all three original files is not required.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair can also fail F3; identify the shared cause, not two independent failed executions.
