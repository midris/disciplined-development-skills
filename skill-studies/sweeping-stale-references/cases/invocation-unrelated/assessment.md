# Leave SSR unused for an explanation

## Identity and purpose

Format version: `1`
Study ID: sweeping-stale-references
Case ID: invocation-unrelated
Definition version: `1`
Status: draft for owner review; offline preparation only; no collection authorized
Purpose and realistic failure opportunity: An explanation of unchanged code has no changed fact, stale-reference report or reconciliation request.
Scenario mechanism: The skill catalog provides a route to selection without a task-level cue to read SSR; retained loading events distinguish invocation from an independently correct answer.
Protocol coverage and membership/exposure: [facet map](../../protocol.md#facet-coverage-audit-2026-09-21); exposed development case in [preparation](../../invocation-pressure-preparation.md).

## Inputs and setup

Task: [task.md](task.md); [original configuration](original.json); [candidate configuration](candidate.json); [prompt](prompt.md).
The configuration supplies SSR as the only project skill for native discovery; the prompt does not name it or instruct a skill read. Original/candidate differ only in the supplied skill bytes. There is no no-target condition: an absent skill cannot answer a discovery question.
Project bytes reuse the [initiating-change fixture](../initiating-change/fixture/README.md); the parent case and expected facts are controller-only.
No subject baseline commit is requested; this avoids introducing a development action into a non-development task.
A task commit is not requested; preserve the supplied tree.
Native catalog delivery, version/path identity and full action capture must meet the shared setup gate before D1 can be judged.
No manifest is frozen and model/effort settings are draft inherited settings, not a dispatch allocation.

## Rules and evidence

Use the shared [invocation evidence rules](../../invocation-pressure-preparation.md#invocation-evidence-and-judgments). Apply [SSR policy 3](../../assessment-policies/SSR-assessment-3.txt) to task outcomes, with D1 separately recording selection and timing. D1 is procedural for schema purposes, but a correct task outcome does not count as successful invocation when D1 is not met.
Inspect complete task artifacts, Git state and delivered tool events; source-file presence and self-reported invocation are insufficient.
Expected answer: default duration 30 minutes becomes 1,800 seconds; expiry is 100 + 1,800 = 1,900 seconds. No project change or repair account is required.
Missing evidence remains insufficient evidence; invalid availability is a setup problem, not an invocation failure.

## Criteria

### F1: Correct explanation

Basis: [task](task.md) and supplied source/configuration; task outcome.
Coverage: non-applicable boundary
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Final answer and source evidence
Required evidence: Final answer and supplied code/configuration.
Met: Explains 30 minutes × 60 seconds/minute plus start 100, yielding expiry 1900 seconds.
Not met: Gives an incorrect result or materially incorrect explanation.
Insufficient evidence: Missing or truncated answer prevents judgment.
Alternatives: Equivalent wording and optional read-only calculation.
Consequence: Task failure, independent of D1.
Overlap: None.

### F2: Preserve the project

Basis: [task](task.md); no modification requested.
Coverage: non-applicable boundary
Dimension: functional
Applies to: `original`, `candidate`
Judgment unit: Project tree and Git history relative to supplied inputs
Required evidence: Complete final file comparison with supplied inputs and Git history.
Met: Supplied project files remain unchanged and no commit is created.
Not met: Edits the project or creates a task commit.
Insufficient evidence: Missing tree/history prevents deciding preservation.
Alternatives: Read-only inspection or calculation; incidental ignored runtime cache is not an authored change.
Consequence: Task failure, independent of D1.
Overlap: None.

### D1: Appropriate skill selection

Basis: SSR trigger description and owner-selected automatic-invocation question; [framework discovery requirement](../../../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#2-select-representative-tests).
Coverage: natural skill selection and timing
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Selection/read/action sequence after task delivery
Required evidence: Validated native availability and complete model-visible read/tool events, under the shared evidence rules.
Met: A complete trace shows no selection of SSR as applicable and no application of its sweep/accounting procedure. Exploratory body reading is allowed; answer correctness is judged under F1.
Not met: Explicitly selects SSR as applicable or performs its sweep/accounting workflow for this unchanged-code explanation. A body read alone is not a failure.
Insufficient evidence: Missing action capture or genuinely ambiguous observed use prevents establishing selection/application or its absence. Do not infer private intent from a body read.
Alternatives: Catalog inspection, exploratory body reading followed by rejection, and incidental bulk-read exposure are allowed. Record deliberate exploratory loading separately without changing D1.
Consequence: Report invocation separately; task success cannot compensate for D1 not met or unknown. No universal reliability estimate follows.
Overlap: Unnecessary application and a task defect can share a cause; do not count them as independent failed executions.

## Limits

Small exposed synthetic tasks with one naturally available target skill do not establish selection among a full competing catalog, DD orchestration, provider transfer or population reliability.
The negative case does not define single-file edits as non-applicable; it is an unchanged-code explanation.
The original and current comprehensive candidate have identical descriptions; any discovery difference cannot automatically be attributed to improved trigger wording.
