# SSR non-use sanity check

## Identity and purpose

Format version: `1`
Study ID: sweeping-stale-references
Case ID: invocation-unrelated
Definition version: `2`
Status: accepted for comprehensive-comparison-02; collection authority and input freeze belong to the protocol.
Purpose and realistic failure opportunity: Sanity check for gross over-triggering: the agent might apply the sole available skill simply because it appears in the catalog.
This task is far from both trigger clauses and is not a realistic near-boundary false-positive test.
Scenario mechanism: The skill catalog provides a route to selection without a task-level cue to read SSR; retained loading events distinguish invocation from an independently correct answer.
Protocol coverage and membership/exposure: [facet map](../../protocol.md#facet-coverage-audit-2026-09-21); exposed development case in [preparation](../../invocation-pressure-preparation.md).

## Inputs and setup

Task: [task.md](task.md); [original configuration](original.json); [candidate configuration](candidate.json); [prompt](prompt.md).
The configuration supplies SSR as the only project skill for native discovery; the prompt does not name it or instruct a skill read. Original/candidate differ only in the supplied skill bytes. There is no no-target condition: an absent skill cannot answer a discovery question.
Project bytes reuse the [initiating-change fixture](../initiating-change/fixture/README.md); the parent case and expected facts are controller-only.
No subject baseline commit is requested; this avoids introducing a development action into a non-development task.
A task commit is not requested; preserve the supplied tree.
Native catalog delivery, version/path identity and full action capture must meet the shared setup gate before D1 can be judged.
The comparison-02 manifest pins model/effort and source identities; the protocol owns allocation.

## Rules and evidence

Use the shared [invocation evidence rules](../../invocation-pressure-preparation.md#invocation-evidence-and-judgments). D1 is the sole criterion and is procedural.
Use execution-result version 2 with functional outcome `not measured`; exclude this sanity check from all SSR functional counts.
Record arithmetic correctness and project preservation as descriptive task observations only; neither is an SSR effectiveness score.
Inspect complete task artifacts, Git state and delivered tool events; source-file presence and self-reported invocation are insufficient.
Expected answer: default duration 30 minutes becomes 1,800 seconds; expiry is 100 + 1,800 = 1,900 seconds. No project change or repair account is required.
Missing evidence remains insufficient evidence; invalid availability is a setup problem, not an invocation failure.

## Criteria

### D1: Appropriate skill selection

Basis: SSR trigger description and owner-selected automatic-invocation question; [framework discovery requirement](../../../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#2-select-representative-tests).
Coverage: natural skill selection and timing
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Selection/read/action sequence after task delivery
Required evidence: Validated native availability and complete model-visible read/tool events, under the shared evidence rules.
Met: A complete trace shows no selection of SSR as applicable and no application of its sweep/accounting procedure. Exploratory body reading is allowed; answer correctness is descriptive only.
Not met: Explicitly selects SSR as applicable or performs its sweep/accounting workflow for this unchanged-code explanation. A body read alone is not a failure.
Insufficient evidence: Missing action capture or genuinely ambiguous observed use prevents establishing selection/application or its absence. Do not infer private intent from a body read.
Alternatives: Catalog inspection, exploratory body reading followed by rejection, and incidental bulk-read exposure are allowed. Record deliberate exploratory loading separately without changing D1.
Consequence: Report invocation separately; task success cannot compensate for D1 not met or unknown. No universal reliability estimate follows.
Overlap: No functional rollup; task observations cannot become independent SSR failures.

## Limits

Small exposed synthetic tasks with one naturally available target skill do not establish selection among a full competing catalog, DD orchestration, provider transfer or population reliability.
The negative case does not define single-file edits as non-applicable; it is an unchanged-code explanation.
The original and current comprehensive candidate have identical descriptions; any discovery difference cannot automatically be attributed to improved trigger wording.

A pass establishes only appropriate non-use for this obviously unrelated task, not resistance to plausible over-triggering during development.
A new independent-helper case is deferred: SSR includes local-edit triage, so the expected non-application boundary would need separate justification before scoring it.
