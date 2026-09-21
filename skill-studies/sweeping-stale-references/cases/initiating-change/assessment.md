# Initiate a session setting rename

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `initiating-change`
Definition version: `1`
Status: prepared for owner review; not accepted, frozen or authorized for collection.
Purpose: Observe complete reconciliation while making the initiating change, preserving causal explanation and unrelated meanings.
Coverage and exposure: O1–O4; ordinary initiating change; exposed development evidence proposed in [coverage expansion](../../coverage-expansion.md).

Scenario mechanism and distinct purpose: This case tests propagation of an agent-initiated rename. The task names the setting and concept but not their consumers; the fixture spreads them across executable and explanatory artifacts and includes history/vendor references to preserve. Final artifacts and runtime checks expose incomplete propagation or damage; ordered tool events and Git history separately expose skipped search, grouping or accounting. This is ordinary change work, contrasting with the existing reviewer-triggered repairs.

## Inputs and setup

Subject task: [task.md](task.md). Configuration: [original](original.json), [control](control.json); working identities: [manifest](manifest.json).
The original receives the unchanged frozen original skill and a full-read instruction. Control receives identical task/project bytes and neutral bootstrap, without the skill or its read instruction. Both first commit the supplied project as fixture baseline; that setup commit is excluded from task grouping.
Current model/effort defaults are preparation settings only; collection must declare runtime identities, scope and budget before invocation.
Only configured inputs reach subjects. This card, policy and expected facts are controller-only.
Verify actual inputs, usable tools/runtime, retained output and complete skill-read evidence for original. Missing setup evidence is unresolved setup, not an inferred skill failure; inspect traces for unintended outside guidance.

## Rules and evidence

Apply the unchanged [SSR policy 3](assessment-policy.txt) and [case-specific reference facts and boundary examples](expected.md).
Read complete delivered artifacts, diffs and available traces. Mechanical observations support human/model judgments; neither successful tests nor a self-report proves complete reconciliation.
Inspect the committed tree as well as the final workspace. F1–F3 apply to both conditions; P1–P3 apply to original only, while control procedure remains descriptive.
Counting units, relevant scope and acceptable variants are fixed in expected.md; do not inherit semantic-block or disputed-label conventions from other cases.
No fixed wording or file-change count substitutes for semantic preservation. A directly observed missing required artifact is failure; inability to inspect the artifact is insufficient evidence.
Offline qualification and commands are recorded in [qualification](../../expansion-qualification.md).

## Criteria

### F1: Complete useful change

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O1, O2 plus explicit task
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Complete current project outcome
Required evidence: Final source/docs/configuration, script/runtime observations where applicable, and reference facts.
Met: The new service setting works across actual consumers; current explanations use session TTL and describe the unchanged behavior.
Not met: The requested correction remains incomplete or creates a contradictory current meaning.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Equivalent wording, organization or implementation preserving the requested outcome; follow relocated content.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F2: Preservation

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O2
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Unrelated behavior, historical meanings and useful explanation
Required evidence: Compare complete original/final artifacts, supplied constraints and relevant runtime observations.
Met: Values, units, rejection of nonpositive duration, partner constraint/trade-off, historical record and independent vendor settings retain their meaning.
Not met: The change damages one of these protected meanings or behaviors.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Semantically equivalent edits; byte differences prompt inspection rather than automatic failure.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### F3: Committed completeness

Basis: Current [original skill](../skill-original/SKILL.md), [protocol contract](../../protocol.md#behavioral-contract-and-consumers), and explicit [task](task.md); severity follows [policy 3](assessment-policy.txt).
Coverage: O3 and task commit requirement
Dimension: functional
Applies to: `original`, `control`
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
Applies to: `original`
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
Applies to: `original`
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
Coverage: O4
Dimension: procedural
Applies to: `original`
Judgment unit: Complete account using a clear, consistent occurrence or matching-line unit, deduplicated across searches
Required evidence: Commit body, expected.md, final changes and observed search scope.
Met: References swept: traces the required references with accurate locations, outcomes, same-path/outcome grouping and counts.
Not met: Required account is absent, misleading or inconsistent with its declared reference scope.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Equivalent precise locations and grouping; redundant grand totals are not required.
Consequence: Report a non-blocking procedural defect or insufficient evidence; this cannot change a functional outcome or justify a repeat by itself.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

## Limits

This is a small reconstructed development case, not a production incident, held-out transfer case or reliability estimate.
Native skill discovery, broader composition, hostile repositories and broad search difficulty are not established.
No existing case, frozen score or live skill is changed; preparation does not authorize provider calls.
