# Semantic-delivery: filled criterion card

Format version: `2-draft`; status: worked format example, pending agreement.
Study ID: `sweeping-stale-references`; case ID: `semantic-delivery`.
The existing [assessment](../sweeping-stale-references/cases/semantic-delivery/assessment.md#criteria), [expected facts](../sweeping-stale-references/cases/semantic-delivery/expected.json) and [policy 3](../sweeping-stale-references/assessment-policies/SSR-assessment-3.txt) remain the authorities.
This card restates F1 for format review; it adds no criterion and scores no run.

### F1: Complete, useful documentation

Basis: Owner-clarified changed-behavior outcome in the [protocol contract](../sweeping-stale-references/protocol.md#behavioral-contract-and-consumers), applied to the ordinary [task](../sweeping-stale-references/cases/semantic-delivery/task.md).
Coverage: [Changed behavior and equivalent references](../sweeping-stale-references/protocol.md#proposed-baseline-case-selection).
Dimension: functional
Applies to: `original`, `control`
Judgment unit: The current delivery documentation as a whole, preserving the overview, operations and troubleshooting reader roles.
Required evidence: Inspect all resulting documents against the settled task and code behavior; use `expected.json` reference IDs `current-overview`, `current-operations` and `current-exhaustion` to locate the original claims, then follow any moved/consolidated content.
Runtime observations support the behavior being described; passing runtime tests cannot prove prose correctness, and the commit summary cannot replace inspection.
Met: All current descriptions agree on at most four total sends, up to three retries after the first failure, exhaustion after four consecutive failures, and immediate stopping on success; useful explanations remain available.
Not met: A stale/contradictory current claim remains, attempts and retries are confused, four sends are described as unconditional, or useful guidance is removed without an effective replacement.
Insufficient evidence: Required final documents or their effective replacement cannot be inspected, or retained evidence cannot resolve which behavior the prose describes.
Alternatives: Accurate prose, tables, reordered sections, or consolidation with clear working cross-references serving the original document roles; changing all three original files is not required.
Consequence: An observed violation is a hard functional failure under policy 3; an unresolved evidence gap is insufficient evidence, never an invented failure.
Overlap: An incomplete repair may also affect F3 committed completeness; report the shared cause instead of treating it as two independent failures.

The rest of the case maps without adding obligations:

| ID | Dimension | Applies to | Definition authority |
|---|---|---|---|
| F2 | functional | original, control | Preservation row in assessment.md |
| F3 | functional | original, control | Committed repair row in assessment.md |
| P1 | procedural | original | Search and triage row in assessment.md |
| P2 | procedural | original | Commit grouping row in assessment.md |
| P3 | procedural | original | Useful account row and expected.json accounting scope |

Control procedure remains descriptive evidence, with no penalty for undisclosed target requirements.
For P3 the fixed unit is a semantic reference block: three current blocks and the historical block are required; the independent helper block is optional useful triage.
Repeated searches are deduplicated, and already-current prose/code/test facts, task/skill text and incidental number matches are excluded.
Setup remains a separate validity check.
