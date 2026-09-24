# Justified local terminology correction

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `local-change`
Definition version: `2`
Status: accepted for comprehensive-comparison-02; collection authority and input freeze belong to the protocol.
Purpose and realistic failure opportunity: Observe scope checking and restraint when one correction genuinely needs no sibling edits.
Scenario mechanism: This case tests a justified local outcome after checking scope. One glossary heading needs correction while related membership and shipping references remain valid. Inspect the final heading, preserved meanings and links, search-before-edit evidence and committed negative-form account. The near-matches distinguish justified restraint from blanket normalization; a one-file diff alone cannot establish that scope was checked.
Protocol coverage and membership/exposure: O1–O3 and O5; local-change boundary; exposed development evidence proposed in [coverage expansion](../../coverage-expansion.md).

## Inputs and setup

Subject task: [task.md](task.md). Configuration: [original](original.json), [candidate](candidate-comprehensive.json); working identities: [manifest](comparison-02-manifest.json).
Original and candidate receive identical project/task bytes and the full-read instruction, differing only in the supplied skill. Both first commit the supplied project as fixture baseline; that setup commit is excluded from task grouping.
Current model/effort defaults are preparation settings only; collection must declare runtime identities, scope and budget before invocation.
Only configured inputs reach subjects. This card, policy and expected facts are controller-only.
Verify actual inputs, usable tools/runtime, retained output and complete skill-read evidence for original and candidate. Missing setup evidence is unresolved setup, not an inferred skill failure; inspect traces for unintended outside guidance.

## Rules and evidence

Apply the unchanged [SSR policy 3](assessment-policy.txt) and [case-specific reference facts and boundary examples](expected.md).
Read complete delivered artifacts, diffs and available traces. Mechanical observations support human/model judgments; neither successful tests nor a self-report proves complete reconciliation.
Inspect the committed tree as well as the final workspace. F1–F3 and P1–P3 apply to original and candidate with unchanged meanings.
Counting units, relevant scope and acceptable variants are fixed in expected.md; do not inherit semantic-block or disputed-label conventions from other cases.
No fixed wording or file-change count substitutes for semantic preservation. A directly observed missing required artifact is failure; inability to inspect the artifact is insufficient evidence.
Offline qualification and commands are recorded in [qualification](../../expansion-qualification.md).

## Criteria

### F1: Complete useful change

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O1, O2 plus explicit task
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Complete current project outcome
Required evidence: Final source/docs/configuration, script/runtime observations where applicable, and reference facts.
Met: The heading is corrected and remains useful in context.
Not met: The requested correction remains incomplete or creates a contradictory current meaning.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Equivalent wording, organization or implementation preserving the requested outcome; follow relocated content.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F2: Preservation

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O2
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Unrelated behavior, historical meanings and useful explanation
Required evidence: Compare complete original/final artifacts, supplied constraints and relevant runtime observations.
Met: Membership/billing/shipping meanings, JSON values and working links remain correct.
Not met: The change damages one of these protected meanings or behaviors.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Semantically equivalent edits; byte differences prompt inspection rather than automatic failure.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F3: Committed completeness

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O3 and task commit requirement
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Committed result after neutral baseline
Required evidence: Retained Git history/tree and final working diff inspected against F1/F2.
Met: All required correct changes are committed.
Not met: Required work is missing/incorrect or remains uncommitted.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any complete acceptable repair; split commits affect P2 separately.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### P1: Search and triage

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O1, O2
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Search-before-edit sequence and justified disposition of relevant matches
Required evidence: Complete search/read/edit tool events and decisions.
Met: Search precedes task edits and establishes appropriate update/preservation scope.
Not met: Observed edits precede search or relevant matches receive incorrect/unjustified triage.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any effective search tool and sensible query order; no required command string.
Consequence: Report a non-blocking procedural defect or insufficient evidence; this cannot change a functional outcome or justify a repeat by itself.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### P2: Commit grouping

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O3
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Grouping of task edits
Required evidence: Git history and diffs after baseline.
Met: One reconciliation commit contains the complete task change.
Not met: Task reconciliation is split or no complete task commit exists.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any single complete reconciliation commit; the setup baseline is excluded.
Consequence: Report a non-blocking procedural defect or insufficient evidence; this cannot change a functional outcome or justify a repeat by itself.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### P3: Useful account

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O5
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Justified negative-form account
Required evidence: Commit body, expected.md, final changes and observed search scope.
Met: References swept: n/a with a valid locality reason is present.
Not met: Required account is absent, misleading or inconsistent with its declared reference scope.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any accurate concise rationale.
Consequence: Report a non-blocking procedural defect or insufficient evidence; this cannot change a functional outcome or justify a repeat by itself.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

## Limits

This is a small reconstructed development case, not a production incident, held-out transfer case or reliability estimate.
Native skill discovery, broader composition, hostile repositories and broad search difficulty are not established.
This controller applicability extension preserves historical cards, task/fixture bytes and criterion meanings; the protocol owns the approved comparison allocation.
