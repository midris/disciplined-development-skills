# initiating-change: proposed CW-aligned validation

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `initiating-change`
Definition version: `4`
Status: draft; collection approval and freeze pending.
Purpose: extend the declared runtime/batch applicability while retaining the fixed case criteria.
Exposure: reconstructed development case; active author/preparer/assessor knows the evidence.

## Inputs and setup

The [proposal](../../../../../../plans/specs/2026-10-24-ssr-cw-aligned-validation.md) and [configuration index](../configuration-index.json) declare provider, mode and condition.
Controller policies/cards/expected facts remain outside subject context.
Require valid input identities, complete capture and actual availability/delivery checks; native missed loading is scored, not excluded as setup.

## Rules and evidence

Apply SSR-assessment-3 and the criterion text below, inherited from [initiating-change.md](../../../compact-regression-01/preparation/criteria/initiating-change.md).
This metadata version changes no criterion meaning, case-specific counting unit, valid alternative or failure consequence.
Finalist follows the accepted comprehensive positive-inventory branch in local-change.
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
Alternatives: Any complete acceptable repair; split commits affect P2 separately.
Consequence: A violation is a hard functional failure; unknown evidence remains insufficient evidence.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### P1: Search and triage

Basis: Current [original skill](../../../../cases/skill-original/SKILL.md), [protocol contract](../../../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../../../../cases/initiating-change/task.md); severity follows [policy 3](../../../../cases/initiating-change/assessment-policy.txt).
Coverage: O1, O2
Dimension: procedural
Applies to: `finalist`
Judgment unit: Search-before-edit sequence and justified disposition of relevant matches
Required evidence: Complete search/read/edit tool events and decisions.
Met: Search precedes task edits and establishes appropriate update/preservation scope.
Not met: Observed edits precede search or relevant matches receive incorrect/unjustified triage.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any effective search tool and sensible query order; no required command string.
Consequence: Report a non-blocking procedural defect or insufficient evidence; this cannot change a functional outcome or justify a repeat by itself.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### P2: Commit grouping

Basis: Current [original skill](../../../../cases/skill-original/SKILL.md), [protocol contract](../../../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../../../../cases/initiating-change/task.md); severity follows [policy 3](../../../../cases/initiating-change/assessment-policy.txt).
Coverage: O3
Dimension: procedural
Applies to: `finalist`
Judgment unit: Grouping of task edits
Required evidence: Git history and diffs after baseline.
Met: One reconciliation commit contains the complete task change.
Not met: Task reconciliation is split or no complete task commit exists.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Any single complete reconciliation commit; the setup baseline is excluded.
Consequence: Report a non-blocking procedural defect or insufficient evidence; this cannot change a functional outcome or justify a repeat by itself.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.

### P3: Useful account

Basis: Current [original skill](../../../../cases/skill-original/SKILL.md), [protocol contract](../../../../protocol.md#behavioral-contract-and-consumers), and explicit [task](../../../../cases/initiating-change/task.md); severity follows [policy 3](../../../../cases/initiating-change/assessment-policy.txt).
Coverage: O4
Dimension: procedural
Applies to: `finalist`
Judgment unit: Complete account using a clear, consistent occurrence or matching-line unit, deduplicated across searches
Required evidence: Commit body, expected.md, final changes and observed search scope.
Met: References swept: traces the required references with accurate locations, outcomes, same-path/outcome grouping and counts.
Not met: Required account is absent, misleading or inconsistent with its declared reference scope.
Insufficient evidence: Missing, truncated or conflicting evidence prevents deciding the required behavior; report the specific gap rather than infer a pass or failure.
Alternatives: Equivalent precise locations and grouping; redundant grand totals are not required.
Consequence: Report a non-blocking procedural defect or insufficient evidence; this cannot change a functional outcome or justify a repeat by itself.
Overlap: A shared cause can affect other criteria; do not count it as another failed execution.


## Limits

Declared provider strata remain separate. No contribution, held-out, full-catalog or population reliability claim.
