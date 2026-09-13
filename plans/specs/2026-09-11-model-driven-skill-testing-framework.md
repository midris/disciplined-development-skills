# Model-driven skill testing and rewriting

Status: current design specification for authorized preparation, under external review.
Follow these requirements when preparing a study; authority to run providers, rewrite a skill or adopt a change comes from the recorded owner decisions in the execution plan and study protocol.
The [fresh testing plan](../2026-09-11-model-driven-skill-testing.md) owns execution order, progress and the next action.

## Goal and starting point

Build a reusable model-driven framework that understands a skill's purpose and behavior, derives representative tests, establishes measured baseline results, and supports evidence-led rewriting with Superpowers `writing-skills`.
The organizing outcome is an evidence-backed decision about improving an existing DD skill; the framework serves that outcome.
The model owns interpretation, test design, evaluation and recommendations.
Simple deterministic tools execute bounded operations and preserve evidence so the model can make those judgments reliably.
Reliability means traceable expectations, representative coverage, trustworthy execution evidence, sufficiently consistent evaluation and conclusions proportionate to the observations.
It does not mean that a model's repeated answer is necessarily correct or that a small suite proves universal effectiveness.

Design this framework from scratch using the currently checked-in skills and existing testing tooling.
Prior charters, catalogs, rubrics, ledgers, acceptance records and review procedures supply no requirements to this design.
The previous testing frameworks and their pending workflows are abandoned; historical approvals and unfinished checklists do not authorize resuming them.
Preserve prior work, but do not inherit its conclusions or treat an existing test as validated merely because it exists.
Reconsider the existing layout and framework choices on their merits; retaining a good choice is allowed, and replacing it is not an objective by itself.
The previously drafted CW review contract remains an unapproved proposal and is not an authority for this framework.

The current [runner](../../skill-validation/runner/README.md) accepts a prompt, declared fixtures and a provider/model/effort configuration, invokes one provider, and retains inputs, outputs, files, logs and mechanical status in a run bundle.
It does not evaluate skill behavior.
Those are existing mechanical capabilities to reuse; their adequacy for any proposed experiment must be checked against actual behavior before relying on them.
Specifically, verify context isolation and skill availability rather than assuming a fresh invocation excludes ambient instructions or globally installed skills.

The framework's initial scope is to design and exercise the complete process on one owner-selected skill, then check transfer to a skill with different behavior before standardizing the procedure across the bundle.
There is no requirement for equal test counts, identical fixtures or one universal quality metric across skills.

## Why this is a reset

The owner clarified the sequence on 2026-09-11: the original request was to rewrite the DD skills; that comprehensive rewrite attempt was abandoned.
The second approach sought a formal model-driven testing process supported by simple deterministic tools; that approach was also abandoned.
The current work is a third approach to the same skill-improvement objective, retaining the checked-in skills and existing tooling.
This history does not establish that every old test or tool failed.

The conversation exposed repeated confusion between intended behavior, test validity and output judgment, including settled whole-document standards being reopened and constructed calibration examples being confused with measured results.
The working diagnosis is that procedural expansion and repeated evaluation displaced progress toward a justified rewrite decision; this is an interpretation of the experience, not a measured attribution of cost to each cause.
The proposed response is one bounded, written study through a skill decision, with source-grounded expectations, a fixed evaluation procedure, durable evidence and an explicit disposition when the effort limit is reached.
The first-study plan makes that response concrete and records candidate and spending decisions; it does not itself authorize experiments.

## Architecture: seven responsibilities

Layers identify responsibility and information flow; they do not mandate seven files, seven agents or a new framework service.
Keep one authoritative home for each decision and reference it from dependent artifacts.

| Layer | Question | Required contents | Boundary |
|---|---|---|---|
| 1. Behavioral contract | What is the skill trying to accomplish? | Intended user/task, useful outcomes, applicability, exclusions, consequential constraints, dependencies, ownership and observable success. | Describe intended behavior separately from the current implementation's wording or teaching technique. |
| 2. Test suite | Which situations meaningfully exercise that behavior? | Representative tasks, source material, fixtures, ordinary uses, consequential boundaries, realistic pressures, non-applicable cases and coverage rationale. | Every scenario needs a behavioral purpose; cosmetic variations and one case per sentence do not establish coverage. |
| 3. Evaluation contract | How will evidence support a judgment? | Criteria mapped to the contract, evidence requirements, acceptable variation, consequential failure boundaries, uncertainty handling and evaluator instructions. | Criteria cannot introduce new skill obligations or make a constructed answer the only acceptable output. |
| 4. Experiment plan | What will we run and compare? | Models, versions, surrounding guidance, permissions, repetitions, controls, run ordering, budget, stopping/retry rules and participant information boundaries. | A model, fixture or context change can change the experiment; record it instead of silently pooling results. |
| 5. Execution evidence | What actually happened? | Exact supplied inputs, skill bytes, configuration, outputs, relevant files/traces, mechanical errors, duration and provenance. | Mechanical completion is not behavioral success; self-reported action is not execution evidence. |
| 6. Assessment | What does each observation demonstrate? | Evaluator judgment, cited evidence, reader or operational consequence, uncertainty and resolved or unresolved disagreements. | Apply the agreed criteria without silently changing them to fit a result. |
| 7. Comparison and decision | How effective is the skill, and is a rewrite better? | Baseline results, variation, comparisons, regressions, improvements, costs, limitations and a retain/adopt/investigate recommendation. | Conclusions are bounded by the tested tasks, models and context; aggregate success cannot conceal a consequential regression. |

The skill is the implementation under test, initially the checked-in version and later a separately versioned rewrite.
The behavioral contract remains stable during a comparison unless the owner explicitly chooses a behavior change.
Changing intended behavior creates a new comparison contract; it must not be disguised as cleanup.

## Developing each layer

### 1. Understand and agree on the behavioral contract

Read the complete skill, referenced materials used by its procedure and relevant companion skills.
Use the [skill purpose and relationship map](../../ARCHITECTURE.md#composition-boundaries) for orientation, then verify relationships against the selected skill's procedure.
Distinguish an independent procedure, an explicit adapter/base pairing, and an orchestrator invoking a sibling at a particular moment.
Default to independent evaluation unless the selected use explicitly requires composition or inter-skill interaction.
An incoming DD invocation or an ownership reference is not a reverse dependency; bundle installation requirements do not require every skill to be loaded into every subject context.
For an explicit pairing, record its direction, trigger and necessary context; evaluate broader orchestration separately when that is the question.
Establish whether it teaches a technique, supplies a reasoning pattern or reference, enforces discipline, coordinates other skills, or combines these functions.
Use that classification to guide investigation, not to force a skill into a single category.

Extract the problem it addresses, the agent decisions or outcomes it aims to improve, its applicability boundaries, important exceptions and any prescribed process that is itself consequential.
Distinguish a required behavior from one implementation technique for achieving it.
Do not discard an explicit process requirement merely because an attractive final answer is possible without it.
Conversely, do not elevate every heading, example or wording choice into a behavioral obligation.

**Required consumer check:** when defining every skill's contract, identify known consumers of its generated outputs and procedural artifacts: people, other skills/agents, commands or programs.
Record who consumes each artifact, what content or exact structure they rely on, the evidence for that dependency, and what omission or inconsistency would break.
Known consumers are the first check for output importance, not the only possible reason; document other consequences when they matter.
If no consumer is identified, record “none identified” with the scope of inspection; if the dependency is uncertain, record it as unresolved rather than inventing one or assuming format is irrelevant.
Carry these findings into procedural severity and test design: verify exact conformance where a consumer requires it, and assess usability where the consumer tolerates equivalent forms.

For each proposed obligation, record its source, intended effect and how it could be observed.
Identify conflicts, unclear intent and behavior the owner wants that the current skill does not promise.
Bring those specific choices to the owner with a recommended interpretation before using them to judge the existing skill.
Owner intent resolves the target contract; it does not retroactively prove that earlier instructions promised the resolved behavior.

Output: a compact behavioral contract with enough source grounding to distinguish preserved intent from a proposed change.
Exit condition: the owner understands and accepts what the framework will hold the skill responsible for.

### 2. Select representative tests

Derive scenarios from the contract's intended uses and meaningful failure modes.
Consider ordinary application, important variations, missing or conflicting information, scope boundaries, and interactions with required companions.
For discipline, introduce realistic opportunities to bypass a requirement; for a technique, require its useful application; for a pattern, test recognition and counterexamples; for a reference, test finding and correctly using information.
Test discovery separately from behavior after an explicit load when both matter.

For each scenario, state what it tests, why that situation is representative, what failure it could expose, what context is necessary and what evidence must be observable.
Choose the smallest initial set that spans distinct consequential behaviors and boundaries.
Record coverage gaps and why overlapping cases remain; do not use case count as a proxy for completeness.
Agree on conceptual facets and how to observe them before selecting fixtures. Where the owner permits historical reuse, then inspect earlier scenarios for fit, adapt a suitable one or create a new one for an uncovered need.
Revalidate reused inputs and expected outcomes against the current contract; previous rubrics, approvals and results do not establish validity for the new study.

The subject task should resemble actual work and permit a competent solution without access to hidden expectations.
Keep the evaluation rubric and calibration answers out of subject inputs unless the experiment explicitly measures behavior with that guidance supplied.
A promise to execute an action requires an environment where the action can be performed and inspected, rather than merely described.

Output: a reasoned scenario set and coverage map.
Exit condition: each selected scenario has a distinct purpose, sufficient inputs and a feasible evidence path.
Designate development cases and reserved transfer cases before calibration or pilot use.
The test designer may know both sets, but must not later act as a supposedly unexposed rewrite author in that same context.

### 3. Define and challenge the evaluation contract

Develop criteria alongside scenarios so tasks can actually reveal the promised behavior.
Map every criterion to an agreed obligation and every important obligation to a test or explicit coverage limitation.
Define the unit of judgment appropriate to the skill: a complete artifact, an observable action sequence, a decision with evidence, or another task-relevant outcome.
For artifact quality, local differences initiate investigation; the complete artifact and its intended use determine the final judgment.

Specify acceptable variation, consequential failure and insufficient-evidence conditions.
Distinguish behavioral failure, task-only deviation, quality differences and execution problems; define their effects explicitly rather than inheriting old labels or averaging unrelated dimensions.
Owner clarification, 2026-09-12: assess functional effectiveness and procedural/mechanical effectiveness separately, with their relative importance determined by the skill.
Functional effectiveness asks whether the skill achieves its intended useful outcomes; failure of an agreed outcome criterion is a hard failure and cannot be offset by procedural success.
Procedural/mechanical effectiveness asks whether required actions, accounting and output contracts are performed reliably.
Record procedural deviations even when the useful outcome succeeds; decide before collection which are hard failures and which are non-blocking defects, citing their consequence for that skill and its consumers.
For example, inconsistent adversarial-review output can break downstream consumption, whereas missing sweeping-stale-references accounting can leave a correct reconciliation less auditable without making the reconciliation itself incorrect.
These dimensions may overlap: a broken output contract that prevents a required downstream action also fails that functional outcome. Identify both consequences without counting them as independent failures in an aggregate.
Tests and reports must expose each dimension at the criterion level; do not force equal weighting or combine them into a score that hides a hard failure.
Use evidence-backed criterion judgments, with insufficient evidence distinct from failure; numerical summaries are optional and must retain the underlying judgments.
Use deterministic validation only for genuine mechanical requirements with a known consumer or independently checkable result.
The study protocol owns the current assessment policy, including owner clarifications and their effective identity. Before relying on a subsequent assessment, include the applicable policy and case criteria in its controller/evaluator inputs and record their exact revision/hash with the judgment; a conversation or review note alone is not an operational scoring instruction. Validate clarified boundaries with contrasting examples before using the affected evaluator. Preserve prior frozen inputs and assessments; version any reassessment instead of silently changing its rules or result.

Construct contrasting examples when a criterion is unclear, including different successful solutions and subtle consequential failures.
Label who constructed them, what guidance they used and why they exist.
They calibrate interpretation; they do not establish model performance or independently validate the contract that guided their construction.

For properties fully established by deterministic checks, validate the checker against known correct and incorrect artifacts; no model-calibration apparatus is required for an unused model judgment.
For model judgments the study uses or measures, establish source-supported reference outcomes and declare the distinctions, repeat count and allowed disagreement before calibration.
Use fresh evaluation contexts without reference answers; assess reasons as well as verdicts and investigate decision-changing errors before relying on those judgments.
Model agreement alone is not ground truth. Resolve disputed contract interpretations with the owner; repair evaluation errors or explicitly narrow the affected scope.
For blinding and every other conditional safeguard, record the mechanism or the evidence limitation and its effect on the claim before collection; an evaluator cannot silently waive the rule.

Output: criteria and checks, with model-evaluation instructions and calibration evidence where used.
Exit condition: the selected checks pass their declared validation or calibration criteria, and remaining limits are explicit.

### 4. Pilot and freeze the experiment plan

Prepare a small pilot to verify task validity, provider behavior, input isolation, evidence capture and evaluator usability before a larger baseline collection.
Before provider dispatch, record exact input paths and identities, invocation/setup instructions, expected evidence locations and checks, and the authorized scope and budget for subject and evaluator calls.
Map each case, condition and repetition to all its attempts and retained bundles so another agent can resume without duplicate runs or lost evidence.
Update this same experiment record when moving from pilot to baseline or rewrite comparison; changed inputs or scope must remain within recorded authorization or receive the needed additional authorization.
Keep infrastructure failures separate from valid behavioral failures and do not rerun selectively until a desired result appears.
Choose repetitions after considering pilot variability, the comparison question, consequential failure risk and the owner's budget.
Do not claim a universal reliability rate from an arbitrary sample count.
Agree on the sample and stopping policy before the measured collection; label pilot evidence separately when the protocol changes.

The main comparison conditions are no target skill, the original skill and, later, the rewritten skill.
Keep model settings, tasks, permissions and necessary surrounding context comparable across conditions.
Removing the target may still leave dependencies present; describe exactly what the control removes and what remains.
For an independent skill, compare the skill alone with the same task without skill guidance; preserve the ordinary task, tools and necessary neutral setup.
For an adapter or interaction test, retain the explicitly required base/context across conditions and identify the resulting attribution limit.
Keep the orchestrator's own project instructions separate from subject inputs; loading skills to conduct a study does not authorize leaking them into its control.
If the target cannot be isolated without breaking a composed workflow, narrow the attribution claim or design a different experiment.
For discovery tests, preserve natural availability and observe selection; explicit loading tests a different question.
Record available provider/CLI versions and other mutable execution dependencies in addition to requested model names, and disclose any version information the provider does not expose.
For the eventual rewrite comparison, run a contemporaneous original-skill condition alongside the candidate under the declared run-order policy.
Include a contemporaneous no-target-skill control when claiming current benefit over unguided behavior; the original/candidate comparison alone supports only their relative performance.
Use the earlier baseline to guide development and detect drift, rather than attributing a difference between an old original run and a new candidate run solely to the rewrite.
If the contemporaneous original changes materially or a relevant setting changes, investigate or report the comparison as inconclusive before attributing a gain.

Freeze the contract, scenarios, criteria, evaluator instructions, original skill bytes and execution settings for the baseline comparison.
Record permitted variation, run ordering, retry rules and the exact information available to test authors, subjects, evaluators and rewrite authors.
Keep reserved transfer cases out of calibration, pilot and rewrite development inputs, while keeping the intended contract visible to the rewrite author.
The author starts in a fresh context with an explicit input set that excludes reserved prompts, outputs, case-level findings and revealing summaries.
Keep reserved material outside the author's checkout and accessible Git history, and verify filesystem/tool restrictions; a separate branch or an instruction not to read is insufficient.
If reserved cases are measured during the original baseline, their detailed results remain separate from the author's baseline report until the candidate version is fixed for final comparison.
Record actual exposure; if separation cannot be maintained, label those cases as development evidence rather than claim held-out validation.
After a reserved result informs an edit, it becomes a development case; any renewed transfer claim requires newly reserved cases under the same contract, measured on both original and candidate versions.

Output: an executable, owner-approved collection plan.
Exit condition: the pilot demonstrates the necessary mechanical capabilities, and the run scope, budget and interpretation limits are agreed.

### 5. Collect evidence

Use the existing runner for bounded invocations and retain every attempt associated with the experiment.
Record exact supplied inputs and versions, the original output, relevant files and observable actions, and execution status.
Verify the selected inputs against the intended condition before accepting an observation for comparison.
Do not confuse final-state file inventories with a complete history of actions; require suitable traces when order or execution matters.

New tools are justified only when a specific needed operation can be made simpler and deterministic, such as input preparation, identity checks, bounded batch dispatch, evidence indexing, file comparison or aggregation of recorded judgments.
Specify inputs, outputs, failure handling and a focused verification case for each proposed tool before adding it.
Keep semantic interpretation and criterion selection in the model's procedure.
Apply the same division when improving a skill: models supply intelligence and judgment; simple programs or reusable commands can handle required mechanical consistency when observations reveal a need.
A prompt-based command can standardize an interaction, but model-generated output still requires validation where exact conformance matters; the prompt alone is not deterministic enforcement.
Distinguish tools used only to assess evidence from tools supplied to the subject to produce its output.
Adding a subject-facing helper changes the tested implementation or execution setup: version it, disclose which conditions receive it, and compare under that declared setup rather than crediting its effect to a wording-only rewrite.

Output: immutable observations with sufficient provenance to inspect and reproduce the experiment within stated limits.
Exit condition: valid observations and unusable attempts are accounted for under the agreed collection policy.

### 6. Assess observations and establish the baseline

Apply the frozen evaluation contract to raw evidence, using fresh evaluation contexts and concealed condition labels where practical.
Check important and ambiguous judgments with additional review, selected under a declared policy rather than only when the outcome is unwelcome.
Read evidence supporting passes as well as failures.
State the task-relevant consequence and distinguish missing evidence from observed failure.
Preserve disagreement and uncertainty until resolved with evidence or explicitly left unresolved.

If an assessment reveals a defective test or criterion, identify the affected observations and version the correction.
Reassess all affected comparison conditions consistently when the evidence supports doing so; recollect only when changed inputs or missing evidence require it and the owner approves.
Preserve the original record and label the revised analysis.

Summarize per-test and per-condition results, important failure patterns, variability, coverage and context limitations.
A successful control is useful evidence, even when it provides no failing case for new guidance.
Passing with the original skill establishes observed success; a comparison is required to support a contribution claim.
Cost, latency and skill size are supporting measures, not substitutes for effectiveness.

Output: a measured baseline with inspectable assessments and appropriately bounded conclusions.
Exit condition: the owner can see what works, what fails, what remains uncertain and what evidence could justify rewriting.

### 7. Rewrite, compare and decide

Identify and read the available Superpowers `writing-skills` workflow and its required testing guidance during foundation inventory, so their evidence requirements inform test design.
Re-read them before authoring and reconcile any version change with the planned experiment and edit.
Choose a specific rewrite objective from the baseline: correct a demonstrated weakness, clarify a condition, remove ineffective procedural burden or simplify successful guidance while preserving behavior.
Match the instructional change to the observed failure rather than adding generic warnings or pursuing a word-count target.
Keep the original skill and the agreed tests available throughout the work.
Original-condition configurations must source a preserved, versioned study copy of the original bytes, not the live skill path that authoring may change; retain identity checks and store candidates separately.

The current `writing-skills` workflow emphasizes failing no-guidance controls, RED–GREEN–REFACTOR, matching guidance form to failure type and repeated wording tests where applicable.
Plan for those evidence requirements in the control and experiment design.
For pure cleanup where controls already succeed and no failing case is observed, explicitly resolve how the authoring workflow applies before editing; do not manufacture a failure or call a passing control RED.
This is a concrete authoring-stage decision, not a reason to discard useful baseline results or change desired behavior silently.

Use development cases for iteration, then assess the selected rewrite against the frozen comparison suite and reserved transfer cases under comparable conditions.
Record which cases influenced authoring and which remained unexposed.
If the suite changes after a new failure is found, version it and apply the new expectations consistently to the original and rewrite.
Do not select a favorable isolated run or conceal consequential regressions inside an average score.

Recommend retaining the original, adopting the rewrite, revising it further or gathering specifically missing evidence.
The owner makes the adoption decision from that comparison.
Output: an evidence-backed rewrite recommendation with preserved history and explicit limitations.
Exit condition: the agreed acceptance question is answered sufficiently for the owner's decision, or the precise remaining uncertainty is documented.

## Roles and review

The model acting as test designer interprets sources, proposes contracts and scenarios, prepares criteria and makes supported recommendations.
The model acting as subject receives the declared task and context, without privileged evaluator material accidentally added to its inputs.
The model acting as evaluator reads the contract and evidence and owns its reasoned judgments.
The rewrite author uses the contract and permitted development evidence to improve the skill through `writing-skills`.
These are information boundaries and responsibilities; one orchestrating agent can coordinate them without giving every stage the same context.

The owner settles intended-behavior conflicts, approves experiment scope and budget, reviews consequential evaluation uncertainties and decides adoption.
The owner does not need to perform routine scoring or repeatedly approve a settled rule.
Before asking for a substantive decision, present the relevant complete context, the model's proposed judgment, its evidence and the precise unresolved choice.
Distinguish review of a recommendation from an authorization to run tests or deploy a change.
An accepted calibration example is not approval of the full evaluation contract.
Record each settled decision in its authoritative artifact and maintain artifact links, progress and the next authorized action in the testing plan.
These records must support resumption without conversation history; keep reserved-case details out of material passed to the rewrite author.

## Practical rollout and open design choices

First select one skill with a bounded purpose and observable behavior, then work through the layers in order with scenario and criterion design developed together.
Preserve known temporary historical material in durable storage; broader archival reorganization is not a prerequisite to the study.
Keep original copies until preservation is verified and record missing evidence without reconstructing it.
Use a contrasting second skill to test whether the framework generalizes to a different evidence type or dependency pattern.
Use a minimal practical organization for the first candidate, then settle reusable artifact templates and add tools for recurring mechanical work actually encountered.
This avoids building a large harness around untested assumptions about evaluation.

Before the measured baseline collection, settle the model/context, budget, evaluator review policy, repetition/stopping policy, transfer-case handling and acceptable evidence gaps using the pilot findings.
Before rewriting, settle the change objective, acceptance boundaries and any pure-cleanup conflict with the selected `writing-skills` version.
These choices depend on the candidate and pilot; they are deliberately not replaced here with universal test counts or numerical acceptance thresholds.

Track execution in the fresh testing plan rather than duplicating its checklist here.
