# Skill-testing process retrospective: SSR and CW

Status: completed active-session retrospective; recommendations for the next experiment, not new collection or authoring authorization.
Basis: [framework spec](../plans/specs/2026-09-11-model-driven-skill-testing-framework.md), [active plan](../plans/2026-09-11-model-driven-skill-testing.md), [SSR process lessons](../skill-studies/sweeping-stale-references/protocol.md#findings-and-process-lessons), [CW baseline](../skill-studies/concise-writing/contribution-baseline-01-assessment.md), [CW comparison](../skill-studies/concise-writing/comprehensive-comparison-01-assessment.md) and their linked evidence/reviews.

## What these studies established

The session workflow can handle both repository repair and prose editing: agree expectations, supply isolated inputs, retain evidence, apply the rules and compare versions.
SSR exercised mechanical outcomes and reporting; CW exercised whole-document correctness, effectiveness and readability.
Both studies reached bounded version-comparison conclusions with adoption deferred.
This demonstrates the workflow on these selected cases, not universal validity or comprehensive skill coverage.

Collaborative criteria development is part of the intended process.
The owner clarified that time spent agreeing what matters is acceptable; the useful product is a durable contract that usually survives many later comparisons.
CW's policy-4 comparison then applied the settled rules without further scoring changes or candidate-derived coverage.
The earlier sentence-level Briefing failures were assessment errors under the owner's intended whole-document standard; those errors are distinct from legitimate discussion to establish that standard.
We should reduce misapplication and repeated reopening, not suppress owner participation.

The records distinguish three different findings: a model completed the useful task, a skill contributed to that success, and a rewrite improved the result.
Passing controls and tied quality outcomes remained valid observations.
The CW candidate passes the fixed quality thresholds with a 22.7% smaller instruction, but also changes the contract: uncertainty flagging is dropped, the explicit repetition exception is narrowed, and applicability is extended.
The [comparison assessment](../skill-studies/concise-writing/comprehensive-comparison-01-assessment.md#candidate-contract-changes) records those deltas; instruction-size reduction does not establish behavior-preserving cleanup.
The candidate does not demonstrate better output quality and produces longer outputs than the original in all four pairs.
Adoption remains a separate owner decision.

## Keep and improve

| Part of the process | Evidence and consequence | Recommended practice |
|---|---|---|
| Collaborative contract design | Owner discussion resolved CW's judgment unit, outcome priorities, useful repetition and length treatment. | Keep the discussion and worked examples where they settle a real ambiguity. Once agreed, reuse the contract; distinguish assessment error from a requested behavior change. |
| Fixed baseline and matched versions | Both comparisons used preserved originals and separate candidates. CW kept its scenarios and policy fixed despite candidate differences. | Keep original/candidate inputs comparable. Candidate inspection may identify a limitation in the claim, but must not reshape the current baseline. |
| Setup and capture checks | SSR excluded two attempts because of runtime/capture problems; later runs used the repaired path. CW reused the harness successfully. | Reuse qualified mechanics and check relevant changes. Preserve every attempt, including failures; do not repeat the full qualification campaign for every skill edit. |
| Whole-artifact assessment | CW's withdrawn failures show why fragments alone were misleading. Final records explain meaning and reader consequences. | Read complete sources and outputs, inspect passes as well as failures, and justify consequences under settled rules. Keep length and process in their agreed roles. |
| Comparative reporting | CW quality thresholds tied while layout, explicitness and length differed. SSR likewise had mixed reporting outcomes. | Keep concise qualitative comparisons beside counts. Do not force a winner or invent finer numeric scores solely to break a tie. |
| Evidence records and validation | Inventories and pins establish what was supplied and assessed. The reassessment validator originally demanded superseded criteria and required repair. | Keep provenance, but validate records against their actual pinned assessment rules. Treat mechanical conformance as separate from semantic correctness. |
| Preparation and bookkeeping | CW required scope-format corrections before dispatch and separate commits for inputs, manifests, results, index and report. Temporary scripts handled repeated copying, hashing and aggregation. | Run offline format/parity checks before the input freeze where possible; freeze in dependency order once. Reuse existing commands and reviewed mechanical helpers. Propose a small helper only for a demonstrated repeated operation; do not build a new framework as a prerequisite. |
| Continuation and authorization | Current state appears in plan, protocol and handoff; explanations can drift. The latest explicit run authorization was settled by the owner. | Keep progress in the plan and decisions/accounting in the protocol; make the handoff a short route to them. Carry approved scope forward and ask only when a material decision or explicit limit remains unresolved. |

These are process observations, not measured estimates of time saved by the recommendations.
The last CW close booked 845 active minutes across the combined work, including initial infrastructure, tooling, discussions, reviews and collection; that is not the marginal cost of an ordinary future comparison.
The latest eight-call comparison spent 508.067 seconds in the runner.
The records do not provide a reliable category-by-category split of all historical effort, so they cannot support a precise percentage of avoidable overhead.

## A reusable working sequence

1. Agree the skill's intended use, criteria and selected scenarios with the owner. Resolve substantive ambiguity with examples when useful; use the accepted contract for later edits.
2. Declare the comparison question, versions, settings, repetitions and bounded run scope. Verify input parity and capture readiness using existing tooling.
3. Execute that scope and preserve each complete attempt before continuing. Separate setup problems from behavioral outcomes.
4. Assess complete evidence under fixed rules, then report counts, supported quality differences, limitations and the resulting decision.
5. Close the selected question, even when the result is a tie or adoption is deferred. Choose further work for a named unanswered question.

This summarizes the existing spec rather than adding another mandatory checklist or document layer.
The scenarios and qualification examples belong to contract development; raw subject outputs establish observed model behavior.
Neither a constructed failing example nor a successful control establishes a model failure that needs fixing.

## What remains to discover

The largest unexercised part of the intended workflow is evidence-led authoring.
Both studies reused existing comprehensive rewrites, so we have not yet established how well this process turns baseline observations into a newly authored, useful change.
The next proposed experiment should select one bounded edit objective from baseline evidence, author that edit, and compare it with the preserved original on the fixed scenarios.
A demonstrated failure is one possible objective; simplifying successful guidance is also permitted by the spec, with the writing-skills authoring requirements explicitly reconciled.
Do not invent a failure or add candidate-shaped tests to make the loop appear successful.
The particular skill, objective and execution budget remain owner decisions.

Other open questions are repeatability in a new session and transfer to another provider or effort level.
These need not become prerequisites to every study or an automatic independent-evaluator campaign.
A future study can exercise ordinary session handoff; a separately selected small reassessment can investigate a concrete disagreement without rerunning subjects.
Claude and effort-level experiments remain desired follow-ups, but they answer provider/settings questions rather than the missing authoring step.
Their order is a recommendation to discuss, not an ordering mandated by the spec.

The selected CW study is complete. More CW scenarios are not needed to close it.
Broader skill coverage, composition and discovery remain limits on adoption claims; investigate them only when the next selected question requires them, under a separately declared scope that preserves the existing baseline.

## Cross-study stocktake

The subsequent active-session review revisited the governing spec, both studies’ coverage and assessments, tooling boundaries and review resolutions.
It did not independently re-score all 46 subject executions.
Two SSR document-conformance findings were reproduced and corrected: closing balances now declare their historical ceilings instead of inheriting CW’s later increase, and first-collection provenance no longer introduces a second attempt-index link into that batch’s scope.
SSR’s runner-schema statement now explicitly describes collection-time versions.
No frozen input, result, criterion or live skill changed.

A possible authoring question is whether a targeted SSR edit can prevent the demonstrated inconsistent audit totals while preserving complete reconciliation.
The subsequent coverage review below takes priority over selecting that edit.
The comparison contains unambiguous counting errors; the disputed Shiv classification and semantic-block conventions are separate uncertainties and must not be treated as established defects.
Retain the existing three-case suite and agreed rules as regression evidence, with arithmetic consistency interpreted from the full account; settle the proposed coverage expansion below before authoring.
Choose the smallest intervention after reviewing those errors: reduce redundant accounting or derive required totals mechanically if a helper is warranted.
A subject-facing helper would be part of the tested candidate, distinct from the controller’s existing evidence tools.
This is a proposed objective, not approved authoring or collection; the subject allocation is exhausted.
It would test the missing evidence-to-edit step without manufacturing a failure or changing the baseline.

Verification after corrections: all five version-1 batches pass assessment readiness; runner unit tests pass 315 and offline process smokes pass 110; hooks pass 263 with three existing skips; formats pass nine and installer tests pass 14.
The first process-smoke invocation encountered the outer sandbox’s nested `sandbox-exec` restriction; the documented host-permission run passed without disabling the child policy or using real providers.
The final active-session review found no remaining issues in these corrections.

## Coverage review before authoring — 2026-09-19

Owner requested reconsidering coverage using historical validation and the comprehensive rewrite worktree before tailoring a skill to an observed miss.
The current studies adequately exercised the process and their declared narrow questions; their coverage is not yet a general rewrite acceptance suite.
All three SSR tasks start with a reviewer flagging a README defect after the underlying change is settled.
They vary the changed fact (CLI option, guide path, behavior), but not the initiating situation.
CW covers two short software decision updates, both editing tasks; combining many padding patterns in one constructed document does not establish breadth of use.

| Coverage question | Current evidence | Proposed treatment before the relevant edit |
|---|---|---|
| SSR: complete related repairs after one reported defect | Three executable cases with literal, path and semantic changes; preservation and committed outcomes | Retain all three unchanged as regression coverage. |
| SSR: ordinary initiating change | Not measured by the current suite; historical SSR-01 supplies a rename with causal comments | Add one executable initiating-change case with real consumers and rationale, without naming all affected files or prescribing a sweep. |
| SSR: genuinely local change | Explicitly deferred; historical SSR-05 supplies a completed negative search | Add one real searchable repository case where the agent must establish locality and avoid unrelated edits; do not supply the answer as a completed inventory. |
| SSR: accounting at scale | Current cases are small; archived grouping case has 126 matches in ten path/outcome groups | If accounting is the edit objective, adapt the grouped-inventory case as a focused diagnostic. It tests accounting, not discovery; retain complete-repair cases alongside it. |
| CW: writing as well as editing | Archived cache-eviction record contains observed drafting outputs from six facts; current cases only edit | Before a general CW rewrite, add a drafting task from fixed facts in a fresh domain, preserving audience needs without instructing padding. |
| CW: consequential procedural prose and document scale | Historical runbook/navigation examples differ from current short decision updates | Before broad CW adoption, select a complete operational document where ordering, exceptions and useful navigation matter; use whole-document policy 4 rather than inherited sentence rules. |

Sources inspected: the [archived SSR record](../skill-validation/archive/skill-records/sweeping-stale-references.md), [archived CW captured example](../skill-validation/archive/skill-records/concise-writing.md#appendix--captured-run-cache-eviction-build-domain), and historical scenario prompts [SSR-01](../skill-validation/scenarios/sweeping-stale-references/ssr-01/prompt.md), [SSR-03](../skill-validation/scenarios/sweeping-stale-references/ssr-03/prompt.md), [SSR-05](../skill-validation/scenarios/sweeping-stale-references/ssr-05/prompt.md), [SSR-06](../skill-validation/scenarios/sweeping-stale-references/ssr-06/prompt.md) and [SSR-07](../skill-validation/scenarios/sweeping-stale-references/ssr-07/prompt.md), with their fixtures.
The comprehensive worktree at commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` supplied `skill-validation/sweeping-stale-references.md` and `skill-validation/concise-writing.md`, including candidate-era coverage and the cutover-runbook example.
Those records supply candidate situations and limitations, not current requirements or transferable pass counts.
Their read-only prompts often supply inventories or request proposed artifacts; they cannot establish actual searching, editing and committing.
Some expectations belong to changed candidate contracts, including intended-new-form searches and CW authoring co-selection; do not silently import them into the original contract.

Historical provenance varies.
The [adversarial-review record](../skill-validation/archive/skill-records/adversarial-review.md) names meeting-pipeline PR 25’s pre-fix tree `66e7179` and reports that synthetic snippets exposed contracts that made the original bugs trivial.
The [review-loop record](../skill-validation/archive/skill-records/adversarial-review-loop.md) records six reactive rounds in meeting-pipeline PR-2 and the EventLog fixture `b0f4511`.
These are promising real-incident sources for later studies; this review inspected the records, not those external repository trees or their original transcripts.
The SSR inventory examples should not be described as independently verified production incidents.

Recommendation: agree the two missing SSR situations first, and include the scale diagnostic if accounting remains the proposed objective.
Recover an intact historical task/tree where available; otherwise label the adaptation as reconstructed.
Freeze any accepted additions and establish original-skill observations before editing; include a no-target control only if the new question includes skill contribution.
Then choose the edit from the combined evidence and compare versions on the declared suite.
Keep the completed baseline and its scores unchanged; new cases form an explicit expansion, not a replacement or candidate-derived baseline.
No new case, subject invocation or skill edit is authorized by this review.
