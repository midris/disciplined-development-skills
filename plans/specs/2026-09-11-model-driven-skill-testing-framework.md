# Model-driven skill testing and rewriting

Status: current design specification for authorized preparation, under external review.
Follow these requirements when preparing a study; authority to run providers, rewrite a skill or adopt a change comes from the recorded owner decisions in the execution plan and study protocol.
The [fresh testing plan](../2026-09-11-model-driven-skill-testing.md) owns execution order, progress and the next action.

## Goal and starting point

Build a reusable model-driven framework that understands a skill's purpose and behavior, derives representative tests, establishes measured baseline results, and supports evidence-led rewriting with Superpowers `writing-skills`.
The organizing workflow is skill development inside a Codex or Claude work session: edit a skill, ask the active agent to run the agreed scenarios, inspect and score the evidence, and record the result. The framework serves that workflow.
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

## Default work-session workflow

The active session is the assessor by default; a human can apply the same written rules.
The owner reaffirmed this existing intent on 2026-09-14 after mandatory separate-evaluator steps had contradicted it.
Responsibilities below are not a pipeline of separately dispatched agents.

1. Read the selected suite, versioned scoring rules and fixed execution configuration; identify the skill version being tested.
2. Run the authorized scenarios through the existing deterministic harness and wait for completion.
3. Preserve and verify the evidence bundles; distinguish execution/setup errors from observed skill failures.
4. Run applicable deterministic checks, inspect the actual outputs/files/traces, and apply the scoring rules in the active session.
5. Record each execution’s criterion outcomes with reasons and evidence, then write the batch assessment with aggregate results, failure patterns and limitations; report it to the owner.
6. After an authorized edit, repeat the relevant fixed scenarios and compare their aggregate assessments under the same rules, recording any changed conditions.

No separate evaluator service, fresh scoring context, blind answer-key test or calibration campaign is a prerequisite to this loop.
Worked examples help explain rules and settle actual ambiguities; they are not a mandatory exam for the active agent.
Additional independent review or evaluator automation is optional when explicitly chosen for a concrete need; it must not silently become the normal workflow.
Direct-session judgments are first-class assessments, labelled as such, not downgraded to development-only evidence because the same agent edited the skill.
Record that shared context and bound claims accordingly; do not claim independent or blind validation.

The runner owns predictable execution and evidence structure. The scoring contract owns what facts matter and their weight. The active agent or human owns interpretation. Deterministic generation/validation supports the record structure and mechanical checks, not semantic verdicts.

## Why this is a reset

The owner clarified the sequence on 2026-09-11: the original request was to rewrite the DD skills; that comprehensive rewrite attempt was abandoned.
The second approach sought a formal model-driven testing process supported by simple deterministic tools; that approach was also abandoned.
The current work is a third approach to the same skill-improvement objective, retaining the checked-in skills and existing tooling.
This history does not establish that every old test or tool failed.

The conversation exposed repeated confusion between intended behavior, test validity and output judgment, including settled whole-document standards being reopened and constructed calibration examples being confused with measured results.
The working diagnosis is that procedural expansion and repeated evaluation displaced progress toward a justified rewrite decision; this is an interpretation of the experience, not a measured attribution of cost to each cause.
The response is a documented session workflow with source-grounded scenarios, fixed scoring rules, durable evidence and bounded conclusions. A formal comparison study is available when needed; it is not the only way to test an edit.
The first-study plan makes that response concrete and records candidate and spending decisions; it does not itself authorize experiments.

## Architecture: seven responsibilities

Layers identify responsibility and information flow; they do not mandate seven files, seven agents or a new framework service.
Keep one authoritative home for each decision and reference it from dependent artifacts.

An **execution** is one model invocation; an **attempt** also includes a launch/preparation failure and is always accounted for.
A **case** defines a task and criteria; a **batch** is the declared set of cases, conditions and repetitions being assessed.
An **execution result** records criterion outcomes and evidence for one execution. A **batch assessment** summarizes those results across repetitions and conditions, including observed frequency, failure patterns and uncertainty.
Use these units explicitly rather than the ambiguous word “run” in study instructions; the runner's existing command and emitted run_id remain unchanged.
Mechanical runner completion is not criterion success; categorical criterion judgments do not imply a second, unregistered quality scale.

| Layer | Question | Required contents | Boundary |
|---|---|---|---|
| 1. Behavioral contract | What is the skill trying to accomplish? | Intended user/task, useful outcomes, applicability, exclusions, consequential constraints, dependencies, ownership and observable success. | Describe intended behavior separately from the current implementation's wording or teaching technique. |
| 2. Test suite | Which situations meaningfully exercise that behavior? | Representative tasks, source material, fixtures, ordinary uses, consequential boundaries, realistic pressures, non-applicable cases and coverage rationale. | Every scenario needs a behavioral purpose; cosmetic variations and one case per sentence do not establish coverage. |
| 3. Evaluation contract | How will evidence support a judgment? | Criteria mapped to the contract, evidence requirements, acceptable variation, consequential failure boundaries, uncertainty handling and evaluator instructions. | Criteria cannot introduce new skill obligations or make a constructed answer the only acceptable output. |
| 4. Experiment plan | What will we run and compare? | Models, versions, surrounding guidance, permissions, repetitions, controls, run ordering, budget, stopping/retry rules and participant information boundaries. | A model, fixture or context change can change the experiment; record it instead of silently pooling results. |
| 5. Execution evidence | What actually happened? | Exact supplied inputs, skill bytes, configuration, outputs, relevant files/traces, mechanical errors, duration and provenance. | Mechanical completion is not behavioral success; self-reported action is not execution evidence. |
| 6. Assessment | What do the executions collectively demonstrate? | Detailed execution outcomes/evidence and batch aggregates, failure patterns, consequences, uncertainty and disagreements. | Apply the agreed criteria and declared inclusion/acceptance rules without changing them to fit results. |
| 7. Comparison and decision | How effective is the skill, and is a rewrite better? | Versioned scores, baseline/comparison results when used, regressions, improvements, costs, limitations and a retain/adopt/investigate recommendation. | Conclusions are bounded by the tested tasks, models and context; aggregate success cannot conceal a consequential regression. |

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
Choose the smallest initial set that spans distinct consequential behaviors and boundaries. Prioritize the skill’s core useful outcomes and the evaluation needed to establish them before expanding edge coverage. Distinguish an obligation from a diagnostic comparison of how the skill contributed; do not require an advantage on every observed mechanism. Deferred coverage remains part of the contract where applicable and must be reconsidered when a proposed rewrite depends on it.
Record coverage gaps and why overlapping cases remain; do not use case count as a proxy for completeness.
Agree on conceptual facets and how to observe them before selecting fixtures. Where the owner permits historical reuse, then inspect earlier scenarios for fit, adapt a suitable one or create a new one for an uncovered need.
Revalidate reused inputs and expected outcomes against the current contract; previous rubrics, approvals and results do not establish validity for the new study.

The subject task should resemble actual work and permit a competent solution without access to hidden expectations.
Keep the evaluation rubric and calibration answers out of subject inputs unless the experiment explicitly measures behavior with that guidance supplied.
A promise to execute an action requires an environment where the action can be performed and inspected, rather than merely described.

Output: a reasoned scenario set and coverage map.
Exit condition: each selected scenario has a distinct purpose, sufficient inputs and a feasible evidence path.
Ordinary development uses known scenarios and records that exposure. If a separate held-out transfer claim is explicitly selected, designate those cases before exposure and do not present an exposed author as unexposed.

### 3. Define and challenge the evaluation contract

Develop criteria alongside scenarios so tasks can actually reveal the promised behavior.
Map every criterion to an agreed obligation and every important obligation to a test or explicit coverage limitation.
Define the unit of judgment appropriate to the skill: a complete artifact, an observable action sequence, a decision with evidence, or another task-relevant outcome.
For artifact quality, local differences initiate investigation; the complete artifact and its intended use determine the final judgment.

Specify acceptable variation, consequential failure and insufficient-evidence conditions.
Distinguish behavioral failure, task-only deviation, quality differences and execution problems; define their effects explicitly rather than inheriting old labels or averaging unrelated dimensions.
Owner clarification, 2026-09-12: assess functional effectiveness and procedural/mechanical effectiveness separately, with their relative importance determined by the skill.
Functional effectiveness asks whether the skill achieves its intended useful outcomes; failure of an agreed outcome criterion makes that execution a functional failure and cannot be offset by procedural success. Batch acceptance is a separate declared rule; it never relabels individual failures.
Procedural/mechanical effectiveness asks whether required actions, accounting and output contracts are performed reliably.
Record procedural deviations even when the useful outcome succeeds; decide before collection which are hard failures and which are non-blocking defects, citing their consequence for that skill and its consumers.
For example, inconsistent adversarial-review output can break downstream consumption, whereas missing sweeping-stale-references accounting can leave a correct reconciliation less auditable without making the reconciliation itself incorrect.
These dimensions may overlap: a broken output contract that prevents a required downstream action also fails that functional outcome. Identify both consequences without counting them as independent failures in an aggregate.
Tests and reports must expose each dimension at the criterion level; do not force equal weighting or combine them into a score that hides a hard failure.
Use evidence-backed criterion judgments, with insufficient evidence distinct from failure; numerical summaries are optional and must retain the underlying judgments.
Use deterministic validation only for genuine mechanical requirements with a known consumer or independently checkable result.
The study protocol owns the current assessment policy, including owner clarifications and their effective identity. Before relying on a subsequent assessment, include the applicable policy and case criteria in its controller/evaluator inputs and record their exact revision/hash with the judgment; a conversation or review note alone is not an operational scoring instruction. Use contrasting examples to resolve an unclear boundary before scoring affected evidence; this does not require separate model calls. Preserve prior frozen inputs and assessments; version any reassessment instead of silently changing its rules or result.

Construct contrasting examples when a criterion is unclear, including different successful solutions and subtle consequential failures.
Label who constructed them, what guidance they used and why they exist.
They calibrate interpretation; they do not establish model performance or independently validate the contract that guided their construction.

For mechanically checkable properties, validate the checker against known correct and incorrect artifacts.
For semantic properties, the active agent or human inspects the evidence and applies the fixed rules, citing reasons and uncertainty.
Disagreement can reveal an ambiguous rule, an evidence gap or a mistaken assessment; resolve the actual issue rather than automatically dispatching another model or rerunning the subject.
If an independent evaluator or blind comparison is explicitly commissioned, define its inputs, acceptance checks and information boundaries for that optional use. Do not claim safeguards that were not established.

Output: versioned scoring rules usable by the active agent or a human, plus validated mechanical checks and useful worked examples.
Exit condition: each judgment has a usable rule and evidence path, mechanical checks work as declared, and genuine ambiguities are resolved or explicitly unknown.

### 4. Pilot and freeze the experiment plan

Use a small pilot when necessary to verify task validity, provider behavior, input isolation, evidence capture and the ability to record execution outcomes and assess a batch. Reuse already established mechanics rather than repeating a pilot for every edit.
Track time and invocations against the experiment plan. At work checkpoints, reconcile actual or explicitly estimated time, remaining work and forecast variance by category and in total, including tooling. Compare the total remaining forecast with remaining authorized time; distinguish updated estimates from carried-forward planning assumptions. Count review, storage and model waits once, preserving any unknown historical split. Time variance prompts scope and effort review, not failure scoring, automatic cuts or a phase gate. Preserve necessary work and evidence standards. An owner-set autonomous-work ceiling remains an authorization boundary: present a forecast extension need to the owner, and obtain approval before exceeding that ceiling. If work stops, report incomplete evidence as a limitation.
Before provider dispatch, record exact input paths and identities, invocation/setup instructions, expected evidence locations and checks, and the authorized scope and budget for subject and evaluator calls.
Map each case, condition and repetition to all its attempts and retained bundles so another agent can resume without duplicate runs or lost evidence.
Update this same experiment record when moving from pilot to baseline or rewrite comparison; changed inputs or scope must remain within recorded authorization or receive the needed additional authorization.
Keep infrastructure failures separate from valid behavioral failures and do not rerun selectively until a desired result appears.
Choose repetitions after considering pilot variability, the comparison question, consequential failure risk and the owner's budget.
Do not claim a universal reliability rate from an arbitrary sample count.
Agree on the sample and stopping policy before the measured collection; label pilot evidence separately when the protocol changes.

Choose conditions for the question: a regression check runs the edited skill against fixed expectations; a version comparison uses original and edited skills; an added no-target condition supports a skill-contribution question. No universal three-arm campaign is required.
Keep model settings, tasks, permissions and necessary surrounding context comparable across conditions.
Removing the target may still leave dependencies present; describe exactly what the control removes and what remains.
For an independent skill, compare the skill alone with the same task without skill guidance; preserve the ordinary task, tools and necessary neutral setup.
For an adapter or interaction test, retain the explicitly required base/context across conditions and identify the resulting attribution limit.
Keep the orchestrator's own project instructions separate from subject inputs; loading skills to conduct a study does not authorize leaking them into its control.
If the target cannot be isolated without breaking a composed workflow, narrow the attribution claim or design a different experiment.
For discovery tests, preserve natural availability and observe selection; explicit loading tests a different question.
Record available provider/CLI versions and other mutable execution dependencies in addition to requested model names, and disclose any version information the provider does not expose.
For public-source fixtures, distinguish in-session input isolation from possible prior model familiarity with the source, layout or upstream API. Record source provenance, study-specific changes, explicit upstream-knowledge claims in traces and the resulting attribution limits. Absence of such claims does not establish non-exposure, and familiarity itself does not invalidate a run. Judge the stated task outcome separately from claims about why the model succeeded or failed; equal public-source exposure across conditions does not prove a measured difference was caused by the skill.
For a public-source rename case, consider inventing both the old and new names when remembered upstream behavior would otherwise conflict with the settled task. Record the choice and its realism/attribution trade-off before freezing inputs. This can reduce a specific API-name conflict; it cannot establish absence of prior familiarity and is not mandatory for realistic upstream migrations.
For the eventual rewrite comparison, run a contemporaneous original-skill condition alongside the candidate under the declared run-order policy.
Include a contemporaneous no-target-skill control when claiming current benefit over unguided behavior; the original/candidate comparison alone supports only their relative performance.
Use the earlier baseline to guide development and detect drift, rather than attributing a difference between an old original run and a new candidate run solely to the rewrite.
If the contemporaneous original changes materially or a relevant setting changes, investigate or report the comparison as inconclusive before attributing a gain.

Freeze the contract, scenarios, criteria, evaluator instructions, original skill bytes and execution settings for the baseline comparison.
Record permitted variation, run ordering, retry rules and the exact information available to test authors, subjects, evaluators and rewrite authors.
Only for an explicitly selected held-out transfer study, keep reserved cases out of authoring inputs and use an unexposed author context. The ordinary session may design tests, inspect results and edit the skill; its evidence is development/regression evidence, not held-out transfer validation.
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

The active session applies the versioned scoring contract to the retained evidence and writes the assessment. A human uses the same rules and format. Additional review is optional for a named ambiguity or consequential judgment, not a prerequisite for reporting each run.
Read evidence supporting passes as well as failures.
State the task-relevant consequence and distinguish missing evidence from observed failure.
Preserve disagreement and uncertainty until resolved with evidence or explicitly left unresolved.

If an assessment reveals a defective test or criterion, identify the affected observations and version the correction.
Reassess all affected comparison conditions consistently when the evidence supports doing so; recollect only when changed inputs or missing evidence require it and the owner approves.
Preserve the original record and label the revised analysis.

The batch assessment summarizes per-case/per-condition results, important failure patterns, variability, coverage and context limitations.
Identify the declared batch scope and the accepted attempt-index version supplying its execution results.
Count met, not met and insufficient evidence separately for each applicable criterion and for the execution-level functional outcome. Show unusable attempts and uncompleted repetitions separately, reconciling them to the planned scope.
For a reported success fraction, use met / (met + not met + insufficient evidence) among the declared included executions with valid setup, showing unknowns explicitly. Never silently drop invalid, missing or unfavorable observations: explain coverage separately and apply the declared inclusion/retry rule consistently.
A retry, reassessment or worked example must not silently replace a failed repetition or inflate the sample. Reassessments replace the interpretation of the same execution; worked examples are not measured executions.
Do not sum overlapping criterion failures as independent failed executions or pool different cases/settings into a single success rate that conceals weaknesses.
Record batch acceptance against the rule selected before collection, or report descriptive results without inventing a threshold. An agreed 4/5 rule can accept a batch containing one recorded failure; it does not make that execution pass. This illustration establishes no default threshold or claim of population reliability.
Evidence pointers and concise reasons in the execution results support pattern investigation without copying model output into each summary. Inspect passes too; a repeated explanation of the criterion is not additional evidence.
A successful control is useful evidence, even when it provides no failing case for new guidance.
Passing with the original skill establishes observed success; a comparison is required to support a contribution claim.
Cost, latency and skill size are supporting measures, not substitutes for effectiveness.
Use whitespace-delimited word count (`wc -w`) over the complete supplied skill text, including frontmatter and Markdown, to compare skill size; exact token counts are unnecessary for this comparison.
A smaller skill with preserved observed effectiveness is a simplification benefit; report behavioral uncertainty and regressions alongside it, without a word-count target.

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

Use the fixed scenarios for in-session iteration and compare skill versions under recorded conditions. Include reserved transfer cases only when that separate claim has been selected and its access boundary is feasible.
Record which cases influenced authoring and which remained unexposed.
If the suite changes after a new failure is found, version it and apply the new expectations consistently to the original and rewrite.
Do not select a favorable isolated run or conceal consequential regressions inside an average score.

Recommend retaining the original, adopting the rewrite, revising it further or gathering specifically missing evidence.
The owner makes the adoption decision from that comparison and may defer it while further studies proceed.
A study can close with its findings, limitations and deferred adoption recorded; choosing a version is required before rollout, not before studying another skill.
Output: an evidence-backed rewrite recommendation with preserved history and explicit limitations.
Exit condition: the agreed acceptance question is answered sufficiently for the owner's decision, or the precise remaining uncertainty is documented.

## Roles and review

The active agent can design scenarios, edit the skill, dispatch subject runs, inspect their evidence, score them and explain the results in one work session.
The subject is the model invocation under test and receives only its fixed task, skill and declared context.
Scoring rules and reference facts belong to the assessing session, not the subject inputs.
A human can replace the active agent as assessor without changing the rule or record format.
A separately dispatched reviewer/evaluator is optional; when used, identify it and apply the relevant read-only and information-boundary requirements. Those dispatch restrictions do not prevent the active agent from recording execution results and batch assessments or making authorized edits.

The owner settles intended-behavior conflicts, approves experiment scope and budget, reviews consequential evaluation uncertainties and decides adoption.
The owner does not need to perform routine scoring or repeatedly approve a settled rule.
Before asking for a substantive decision, present the relevant complete context, the model's proposed judgment, its evidence and the precise unresolved choice.
Distinguish review of a recommendation from an authorization to run tests or deploy a change.
A worked example illustrates a rule; accepting it neither authorizes a run nor silently changes other rules.
Record each settled decision in its authoritative artifact and maintain artifact links, progress and the next authorized action in the testing plan.
These records must support resumption without conversation history; keep reserved-case details out of material passed to the rewrite author.

## Working artifact organization

Owner clarification, 2026-09-15: keep canonical accepted records and use Git for earlier versions. Each execution has one current result; each declared batch has one aggregate assessment, referencing those results.
Commit accepted records before replacing them; cite a full commit ID and path when an assessment needs older file bytes.
Preservation requirements below do not require duplicate historical files, snapshot directories or an extensive amendment ledger; a concise correction reason and Git history suffice.
Distinct actual attempts still require accounting, and Git preserves only committed artifacts; full raw bundles remain in the existing external stores under the separately documented retention policy.

The SSR study supplies the current working layout below. Reuse its ownership and information boundaries; universal case counts are not prescribed.
Owner direction: settle a versioned protocol template at the end of baseline design, before freezing collection. Define stable section names/order, required fields, optional sections and their applicability, artifact links, and decision/amendment conventions. Apply the agreed version 1 to SSR and subsequent skills. Agree on the related artifact contracts below at the same checkpoint. A contrasting skill tests their generality; any needed structural change receives an explicit new version rather than silently changing the format.
The active plan owns the checklist, this spec owns general requirements, and `skill-studies/<skill>/protocol.md` owns the skill-specific contract, coverage map, assessment policy, execution decisions and artifact index.
A suite is the explicitly selected set of cases under that protocol, not every case directory or historical run present on disk.

| Artifact, relative to a study directory | Purpose |
|---|---|
| `sources.json`; `cases/skill-original/SKILL.md` | Source identities and preserved original skill bytes. Candidates remain separate. |
| `cases/<case>/task.md`, prompts and `fixture/` | Realistic subject task, condition-specific setup and supplied source material. A fixture can be documents or other task inputs; it need not be a software repository. |
| `cases/<case>/control.json`, `original.json` | Existing runner configurations declaring every supplied regular file and execution settings. Candidate configuration is added when needed. |
| `cases/<case>/assessment.md`, `expected.json`, `assessment-policy.txt` | Pre-run criteria, valid alternatives, known facts, uncertainty boundaries and the exact applicable policy. These are controller inputs, not completed-run judgments or subject guidance. |
| `cases/<case>/check_*.py`, checker tests, `qualification.json` | Optional deterministic observations and evidence that the chosen checks work on known outcomes. The active agent or human applies the rules where semantics require judgment; no separate evaluator qualification gate. |
| `cases/<case>/manifest.json`; source provenance where needed | Exact input and controller identities, including versions and hashes. |
| `<batch>-run-index.json` | Actual attempts, scope/authorization references, input manifests, call charge, retained bundles and execution-result links; runner metadata is referenced rather than copied. |
| `results/<run-id>.json`; `<batch>-assessment.md` | Detailed execution outcomes/evidence and the aggregate batch assessment, including comparison when needed. Existing pilot reports/checks and historical `assessments/` examples retain their locations and identities. |

Retain one complete bundle per actual run in the durable external store recorded by the protocol, with one inventory verifying completeness; keep unsuccessful attempts too.
The owner accepted a small index referencing the manifest, authorization, bundle and canonical assessment, with call accounting; derive execution metadata from runner artifacts rather than duplicating it.
Use ordinary backup arrangements when configured, without requiring a second study-managed copy or per-run backup verification. Record the actual arrangement, unverified coverage or explicitly accepted single-host retention; existing historical evidence is not deleted by this simplification.
Git holds permitted case materials, policies, manifests and reports. Reserved cases and revealing results stay outside the rewrite author's accessible checkout/history. Verify that access boundary before claiming reserved transfer evidence.
Case files may be reused in a later authorized phase without relabeling prior pilot observations. Once assessed, preserve their identities; version changed cases or assessments explicitly. Redundant and rejected cases can remain as history without belonging to the active suite.

### Execution results and batch assessments

Settle the reusable formats before the next assessed collection. Rules identify each criterion, evidence, dimension, consequence, valid alternatives and missing-evidence treatment; known consumers determine consequential format requirements.
The active agent or human records one execution result with schema/result/run identity, condition, manifest reference, assessor context, evidence pointers, setup validity, criterion outcomes/reasons/consequences and uncertainty.
Resolve study/case, skill/configuration and criteria/policy identities through the manifest instead of copying them into every result. A reassessment may identify changed rules, but must verify unchanged subject inputs against the actual attempt and explain the correction.
For SSR, retain met / not met / insufficient evidence per criterion. Derive that execution's functional result: any functional failure gives not met, otherwise any functional unknown gives insufficient evidence, otherwise met. Procedure and setup remain separately visible.
The [execution-result schema/template](../../skill-studies/formats/README.md#execution-results) implements this per-execution contract, not batch acceptance or graded quality. Optional graded scoring for another skill requires a declared mapping; observed success counts are not a new grading scale.
The [batch-assessment template](../../skill-studies/formats/assessment.template.md) implements section 6's aggregate requirement and can compare those same results across conditions or batches. Do not require an additional comparison record.
The protocol owns study decisions and authorizations, citing the relevant assessment. Input identity belongs in manifests, attempt/bundle identity in indexes, detailed outcomes in execution results, aggregates in batch assessments and costs in accounting.
Schema validity alone cannot establish a complete assessment. Validate identities, criterion coverage and declared batch coverage as well; explicit checks suffice until the planned tooling exists.

### Format decisions and document tooling

Owner requested a template generator and conformance validator after the formats are settled. Agree on a small version 1 contract set at the design checkpoint; the following are the proposed companion boundaries to the protocol template, not finalized schemas:

Existing example: [`skilltest worksheet`](../../skill-validation/runner/README.md#worksheet), implemented in `skill-validation/runner/src/skilltest/worksheet.py`, renders a fixed blank assessment from a run's `result.json` and a scenario's `rubric.md`. Inspection confirmed that it fills mechanical identity fields, leaves judgments blank, writes exclusively and makes no provider call. It does not validate completed assessments or arbitrary study documents. This is evidence of the recurring generation/validation pattern, not a required implementation base or scoring authority.
Owner clarification: choose the best deterministic tool design from the agreed requirements. Reusing, adapting, replacing or retiring the existing worksheet are all available choices. Its command shape, document layout, rubric dependency and code structure impose no requirement on the new design. Update scoring/assessment formats and tooling as needed under the settled functional/procedural policy, while preserving versioned historical evidence. Evaluate the runner interfaces as integration constraints and version any necessary changes explicitly.

| Contract to settle | Stable contents and relationships |
|---|---|
| Case and evaluation definition | Case/criterion identifiers, purpose and coverage references, subject inputs, functional/procedural classification, consequences, acceptable alternatives, evidence requirements and uncertainty. Skill-specific payload and judgment remain flexible. |
| Execution and evidence index | Batch, case, condition, repetition and attempt identity; authorization, call charge and references to configurations/manifests, results and evidence. Define the interface to runner configuration/result records; explicitly version any necessary changes and preserve historical record identities. |
| Source and freeze manifest | Artifact identities, spec/template/policy versions, source revisions, hashes and the relationships between subject and controller inputs. |
| Execution results and batch assessment | Detailed outcomes/evidence, aggregate counts and patterns, explicit coverage/denominators, uncertainty and optional comparisons of the same aggregates; no universal grade or fixed acceptance threshold. |
| Layout and lifecycle | Canonical locations and artifact roles, active-suite membership, reserved/development boundaries, status meanings, and how frozen material is superseded or reassessed without overwriting history. |

For SSR, build the document tool after baseline collection and assessment, with contracts agreed before collection. Its implementation is not a collection-freeze prerequisite: explicit structural and identity checks suffice in the meantime. Estimate implementation and its own qualification separately before starting; do not hide their effort in case preparation. Review scope and the overall authorization boundary if the forecast grows. Later studies may use the completed tool at preparation time.
Generation and validation should consume the same versioned structural definitions so they cannot drift independently. Generation creates the selected artifact or study skeleton with declared version and clearly unfinished content; it does not invent behavioral contracts, findings or approvals. Validation checks required sections/fields, types and allowed values, identifiers, links, cross-artifact references, declared versions, applicable hashes and deterministic allocation arithmetic. Distinguish a structurally valid draft from a complete artifact eligible for a declared stage; unresolved placeholders must not pass readiness checks.
The validator reports file/field or line locations and specific failed rules, with human-readable output and a machine-readable form/exit status for automation. Unknown versions are reported as unsupported; do not silently reinterpret or migrate existing documents. Validation is read-only and generation must not overwrite existing work. Historical artifacts retain their declared versions and statuses; migration is an explicit, separate operation.
Document validation does not establish semantic coverage, realistic scenarios, correct causal attribution, evaluator reliability or actual owner consent. It can check that required evidence/approval references are recorded, not substitute for judging their meaning. Models remain responsible for those judgments.
Qualify the tool using generated valid drafts, representative complete documents and deliberately invalid examples, including missing requirements, unresolved references, wrong versions/hashes and inconsistent run counts. Agree on its concrete CLI, supported document representations and integration point with the existing runner before implementation; no provider dispatch or new testing service is implied.

### Document conformance

The spec governs the document set, not just its starting design. Format walkthroughs settle representations; they do not reopen the workflow or criterion policy.
Before accepting a document change, trace its fields/sections to the responsibilities above, identify the authoritative home of each fact, and check the whole set for omissions, duplication and conflicting current instructions.
In particular, follow one declared batch from case/configuration through manifest, attempts and execution results to aggregate assessment and decision; check failed, unknown, unusable and unfinished observations as well as passes. Use existing evidence or clearly labelled structural examples, without requiring new model calls.
Schema tests establish structural rules only. Review whether the artifacts collectively answer the spec's questions; accepting one template does not establish that the complete set conforms.
If the representation cannot express an existing requirement, correct the representation. Change the spec only for a genuine requirement clarification, with the reason at that rule; do not invent new workflow steps to accommodate a template.
Keep this check within the existing review and plan. It requires no separate traceability ledger, review service or additional owner approval. Git preserves superseded instructions; current documents describe the selected work.

## Practical rollout and open design choices

First select one skill with a bounded purpose and observable behavior, then work through the layers in order with scenario and criterion design developed together.
Preserve known temporary historical material in durable storage; broader archival reorganization is not a prerequisite to the study.
Keep original copies until preservation is verified and record missing evidence without reconstructing it.
Use a contrasting second skill to test whether the framework generalizes to a different evidence type or dependency pattern.
Use a minimal practical organization for the first candidate, then settle reusable artifact templates and add tools for recurring mechanical work actually encountered.
This avoids building a large harness around untested assumptions about evaluation.

Before the next scored collection, settle the fixed rule/record formats, selected scenarios and skill versions, execution settings, authorized run count and handling of evidence gaps. Decide independent review or held-out transfer only if the question needs it.
Before rewriting, settle the change objective, acceptance boundaries and any pure-cleanup conflict with the selected `writing-skills` version.
These choices depend on the candidate and pilot; they are deliberately not replaced here with universal test counts or numerical acceptance thresholds.

Track execution in the fresh testing plan rather than duplicating its checklist here.
