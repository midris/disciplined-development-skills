# Sweeping stale references: study protocol

Status: Stage 1 complete; Stage 2 conceptual coverage accepted; pilot 01 complete and externally reviewed PASS. Pilot 02's approved moved-file pair is complete; the owner accepted the results walkthrough and clarified path-count explanation, 2026-09-13.
The owner selected `sweeping-stale-references`, authorized contract/allocation preparation and clarified that this skill should be evaluated independently.
The behavioral contract and outer ceilings are agreed; both authorized pilot pairs are complete and further execution remains subject to its own recorded scope.
Progress belongs to the [plan](../../plans/2026-09-11-model-driven-skill-testing.md); general requirements belong to the [spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md).
Four subject observations are recorded across [pilot 01](pilot-results.md) and [pilot 02](pilot-02-results.md), each linking its run index and controller checks. No measured baseline or skill rewrite has been created.

## Sources and intended use

The original is [sweeping-stale-references](../../skills/sweeping-stale-references/SKILL.md) at repository revision `53a06ff4e2fcefb3c7706565bebe07d88e2782ea`, SHA-256 `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.
Original-condition runs load the [frozen study snapshot](cases/skill-original/SKILL.md), not the live skill path. Preserve these bytes for contemporaneous original-versus-candidate comparisons; candidate edits must not replace this snapshot.
[sources.json](sources.json) records inspected file paths, sizes and hashes, including all nine DD skills, installed authoring guidance and runner implementation.
This inventory identifies the initial preparation sources at the recorded revision, including the runner before its permission extension; it is not the frozen manifest of inputs supplied to subjects.
The permission qualification index below identifies the updated runner sources.

The skill combines a search-and-reconciliation technique with discipline against stopping after one cited defect.
Its intended user is a development agent changing a fact shared across project files or responding to a reviewer who found one stale reference.
The skill has its own trigger and procedure; it does not require DD or a named Superpowers base to perform a sweep.
DD invokes it at Gate 4, but that incoming invocation is not a dependency of the skill.
The [purpose and relationship map](../../ARCHITECTURE.md#composition-boundaries) records this distinction across all nine skills.
The first study measures independent application to a change and reconciliation commit; native discovery and DD orchestration are outside its claim.
[Disciplined research](../../skills/disciplined-research/SKILL.md) owns grounding the changed fact; [writing explicit rationale](../../skills/writing-explicit-rationale/SKILL.md) owns why it changed.
These ownership boundaries do not require loading either sibling into the subject context.
The task must supply a settled change and sufficient project context, rather than score this skill for inventing the desired change or resolving an unspecified business rule.

## Behavioral contract

Owner clarification, 2026-09-12: the intended outcome includes preventing documentation drift when project structure or code facts change.
When a file moves, find references to its old path and reconcile affected links, commands and other current consumers to the new location, resolving relative paths from each consumer.
When a code fact changes, find and update documentation describing that fact even when it uses different words rather than the changed identifier; search terms locate candidates, and the meaning of each reference determines the change.
The current text explicitly covers changed documented behavior, literal strings and synonyms, and doc/comment citations.
Applying that procedure to moved paths and semantically equivalent descriptions of code facts is a supported interpretation, reinforced by the owner's intended use; relative-path resolution is not an explicit instruction in the current skill.
Record those criteria as owner-clarified outcomes, not a quotation or proof that the original explicitly taught every technique needed to achieve them.
Assess those outcomes across both conditions, separately from compliance with the original's explicit procedure; a miss does not by itself establish disobedience to an explicit instruction.
Historical references and unrelated matches still receive the stated triage, rather than blanket replacement.
The broad purpose, independent evaluation direction, outcome/procedure distinction and outer limits are settled.

Judge the completed reconciliation, search evidence and commit record together.
Explicit procedural obligations remain observable requirements; an attractive final file state does not prove that the prescribed search or accounting occurred.

| Obligation and source | Intended effect | Observable evidence |
|---|---|---|
| **Explicit procedure:** search before reconciliation edits; search literal references and plausible synonyms across code, docs, tests and config/build/CI, including vendor/archive triage. Source: Quick reference, Procedure 1, What counts as a reference. **Owner-clarified outcome:** reconcile moved paths and documentation of changed code facts; relevant path variants and relative-path resolution are applications of that intent, not explicit instructions in the skill. | Find siblings of the triggering defect, including broken path references and documentation of changed code facts. | Retained search commands/results and edit ordering, checked against supplied project state. Record a path-handling miss under the clarified outcome; do not infer an explicit-instruction violation from that miss alone. |
| Classify matches as update, false positive with reason, or intentionally stale with reason. Skill: Procedure 2. | Reconcile real consumers while preserving unrelated matches and historical meaning. | Final changes, unchanged material and reasons linked to each matching location. |
| Reconcile all required updates in one commit. Skill: Procedure 3. | Avoid committing an inconsistent intermediate project state. | Git history/diff relative to the prepared original; all required changes in one reconciliation commit. |
| Account for matches in `References swept:`, grouped only by the same path and outcome, with precise locations and counts. Group before exceeding the normal commit-body preference; a broad sweep may exceed it after grouping. Skill: Output artifact. | Make coverage and deliberate preservation independently inspectable without treating necessary audit detail as verbosity. | Commit body reconciled to retained searches and final changes; after narrative and before a Verification section when present. No invented hard length cap. |
| Give the required `References swept: n/a — <reason>` in the single-file/no-sweep case. Skill: Quick reference and Output artifact. | Distinguish a justified negative finding from forgotten accounting. | Recorded search/scope basis and the negative-form commit line. |

Accept any effective search tool, sensible query order, equivalent edits and concise grouping that preserve these obligations.
Do not require a particular document structure, word count or wording from a constructed reference answer beyond the explicitly prescribed labels/header and negative form.
Useful repetition and document restructuring remain acceptable when the resulting document is at least as effective; local text differences are evidence to inspect, not automatic failures.

Owner accepted, 2026-09-12: interpret “single-file/no-sweep” as a justified outcome after checking scope, not permission to skip searching because only one file was initially named.
Owner clarification, 2026-09-12: score functional effectiveness and procedural/mechanical effectiveness separately. Outcome failures are hard failures; the consequence of procedural inconsistency depends on the skill.
The owner initially permitted either procedural severity choice; the pilot walkthrough clarified the priority: the actual committed reconciliation matters, while a fully detailed commit message is nice to have.

### Current SSR assessment policy

Policy identity: **SSR-assessment-2**, owner-confirmed 2026-09-12. This section is the authoritative assessment policy for subsequent SSR runs; the pilot report records the decision's context.
Selected policy: assess each agreed criterion as met, not met or insufficient evidence, retaining the supporting evidence and consequence. Keep the two dimensions visible instead of combining them into a single score.
Incomplete or incorrect reconciliation, including damage to material that should be preserved, is a hard functional failure.
When the task requires committing the repair, verify that every required edit is committed; a correct but uncommitted working tree does not meet that task outcome. Separately assess whether the edits were grouped into one commit.
Lead the result with whether all affected references were correctly reconciled, protected material preserved, and required edits committed. Derive these judgments from the project, checks and Git history, not the completeness or confidence of the commit message.
Purely procedural deviations are non-blocking defects for this study: report search-order, classification/accounting, commit-grouping and format failures explicitly without treating them alone as a failed functional outcome.
Detailed accounting is secondary: an omission may be recorded against the original skill's explicit instructions, but cannot turn functional success into failure, block progression by itself, or require another run merely to obtain a fuller message. This SSR policy does not weaken output contracts for other skills with downstream consumers.
This severity policy does not make the original's explicit requirements optional or establish full compliance when they are missed.
Known output consumers: people and reviewing agents inspecting the reconciliation commit use `References swept:` as an audit account; the skill's Output artifact section explains the locations, outcomes and count reconciliation they need. DD Gate 4 and this project's commit guidance require that account.
Inspection of shipped skills, hooks, commands, examples and top-level tests found no named program consuming this format, and a targeted search of hook Python sources found no `References swept` parser. This bounds the inspection, not a claim about every consumer installation.
Missing or inconsistent accounting impairs auditability; no identified program requires exact syntax to perform the reconciliation itself. That supports the selected non-blocking accounting policy while retaining the original's explicit format checks.
Complete reconciliation with correct preservation but missing `References swept:` therefore meets the functional criteria and fails the accounting criterion; a well-formatted account cannot offset unresolved current references or incorrectly changed historical references.
Where a procedural deviation also causes a functional failure, record that consequence and apply the functional hard-failure rule.
A procedural regression remains relevant to the later adoption decision even when non-blocking; agree on the rewrite's acceptance boundaries before authoring rather than treating this policy as automatic adoption approval.
Apply the useful-outcome criteria to both conditions; target-specific compliance describes the original condition and must not penalize the unguided control for undisclosed instructions.
Count and location conventions must be fixed with the eventual checkers, including repeated searches of the same location, so duplicate search hits cannot inflate claimed coverage. State which query results require accounting, including already-current references found during exploration, before assigning a defect for omitted entries. Pilot 01 surfaced competing readings of that scope; its [assessment correction](pilot-results.md#assessment-correction-2-2026-09-12) does not establish a skill defect or authorize a rewrite objective.
Missing action traces yield insufficient evidence for order/completeness claims, not an invented behavioral failure or pass.
Historical commits, PR descriptions and chat logs are not rewrite targets; vendor/archive files still require triage under the skill's stated distinctions.

For every subsequent assessment, copy this policy and the applicable case criteria into the controller/evaluator evidence package, record their policy identity and exact revision/hash alongside the assessment, and verify those inputs before relying on the judgment. Keep assessment instructions out of subject inputs.
Before another case is dispatched, map its criteria to functional or procedural outcomes and their consequences under this policy. Before using a model evaluator, qualify it on contrasting examples: complete committed reconciliation with sparse accounting must succeed functionally; incomplete reconciliation with a perfect account must fail functionally. Include correct-but-uncommitted work when committing is a task requirement.
If a judgment contradicts those boundaries, treat it as an assessment defect and resolve it before accepting the result; do not blame the subject or rerun it to repair the evaluator. The runner captures evidence and configuration identity; it does not enforce these semantic judgments automatically.
The completed pilot's frozen assessment, manifest and raw bundles retain their original identities. This clarification does not change its functional verdicts; any later reassessment must be separately identified with its applied policy, rather than overwriting the original record.

## Standalone control and attribution

Owner direction: evaluate this skill independently; do not include DD merely because it invokes the skill.
Use the same ordinary task, project files, tools, permissions, model settings and neutral execution setup across conditions.
The original condition explicitly loads only the recorded sweeping-stale-references skill; the no-target condition receives no DD, sibling or Superpowers skill guidance.
An eventual candidate condition replaces only the original target bytes.
Freeze and inspect all supplied instructions before dispatch; the task/setup must not reproduce the target's procedure, accounting format or reference answers.
For the initial contribution cases, present a realistic trigger without directing a project-wide sweep or enumerating affected consumers: for example, one reviewer-flagged reference with discoverable siblings, or a settled change with its consumers left for the agent to identify.
Keep the required change and permission to reconcile related files clear; do not impose a one-file-only constraint or make the task ambiguous to manufacture failure.
An explicit “update every reference” request may test execution quality in a separately identified case, but cannot establish that the skill caused the decision to broaden the work.
The assistant conducting this study follows project skills, but those instructions are not subject inputs.

Public-source familiarity is a separate attribution limit from in-session guidance leakage. Shiv's layout and upstream API may be familiar to either subject; we cannot establish pretraining exposure or its absence from these traces. Record explicit upstream/remembered-API statements and whether they are supported by supplied files or outside retrieval. The task explicitly settles the study rename. An edit restoring the retired option still fails the agreed functional outcome when verified against that task; investigate its evidence before claiming it demonstrates a search/triage failure or a skill-specific cause. Merely mentioning upstream is not contamination or invalid setup. Familiarity can also reduce discovery effort in both conditions, so neither project size nor a passing pair establishes difficult discovery.

This comparison asks whether the skill improves independent reconciliation over the model's ordinary task behavior, and later whether the rewrite is at least as effective as the original.
Assess useful outcomes across both conditions; separately record evidence of the target's prescribed search, triage and commit accounting.
Failure to reproduce an undisclosed target-only format is not by itself evidence that the control performed the ordinary task poorly.
Differences in the presence or spelling of `References swept:` cannot alone support a functional-effectiveness claim; report functional and procedural findings together, including observed search breadth, triage correctness, complete single-commit reconciliation and useful audit evidence.
If functional outcomes tie but useful accounting differs, report that functional tie and the procedural advantage explicitly; do not summarize the observation as “no difference.”
The control is not supplied the format, but may independently produce it; neither success nor failure is guaranteed by condition assignment.
DD handoffs, interaction with other skills and native skill discovery require separate tests if later selected; this allocation does not establish them.

The previous Gate 4 setup and missing-companion exception are superseded and must not appear in the frozen inputs.
Pilot acceptance requires evidence that the original loaded the intended target, the control received no skill guidance or instruction to retrieve a missing skill, and both could perform the same task.
Ambient guidance, inaccessible required task inputs or a setup-induced missing-skill stop invalidate that condition; repair the setup within authorization instead of scoring it as a behavioral failure.

## Conceptual coverage

Owner direction: agree on what to test and how before selecting scenarios. After that review, inspect earlier scenarios for a fit; adapt a suitable one or create a new one where coverage is missing. Old expectations and results are not inherited as authority.
The owner accepted these seven facets on 2026-09-12. They define conceptual coverage, not seven required cases or a complete scoring rubric.

**Owner priority, 2026-09-13:** establish the core value first: identify affected references beyond the cited defect, reconcile them correctly, preserve unrelated and historical meaning, and commit the completed repair. Broad searching is part of the skill's explicit procedure; finding more than the control is a diagnostic comparison, not an additional success requirement. Observe search, triage and accounting under SSR-assessment-2 without making a discovery advantage or exhaustive facet coverage a prerequisite to the first baseline. Complete repairs prompted by SSR remain useful evidence even when the control saw the same references.

**Owner coverage decision:** include three core situations in baseline design: interface rename, moved file and changed behavior described in documentation. Use Shiv and the moved-guide case as the prepared foundations, and design semantic drift before freezing collection. The earlier proposal to defer semantic drift is superseded. Specialized discovery challenges and additional boundaries can wait; trustworthy functional checks and evaluator qualification remain necessary.

| Facet | What to exercise | How to observe it |
|---|---|---|
| Broaden beyond the trigger | One cited defect has unstated siblings, including config, CI or fixtures. Distinguish discovering consumers from deciding to repair consumers already seen. | Check required consumers in final state; inspect traces separately for discovery, search breadth and search-before-edit order. The two pilots observe scope completion and broad-search behavior but do not discriminate discovery effectiveness. |
| Recognize equivalent references and changed facts | References use synonyms or describe changed code behavior without repeating its identifier. | Model judgment checks meaning against the settled fact and permitted alternatives; mechanical checks cover exact known values only. |
| Reconcile moved paths | Consumers use different relative paths, links or commands to a moved file. | Resolve each consumer's target and check it still works; assess prose context where needed. Relative-path handling is an owner-clarified outcome, not an explicit technique in the original. |
| Triage and preserve | Current consumers coexist with unrelated matches, history and vendor material. | Compare changed and preserved content; assess the correctness of each decision separately from whether its reason was recorded. |
| Complete reconciliation and commit it together | All required fixes must be complete, with no unrelated damage. | Check the final project and retained Git history. Functional completeness and the procedural single-commit requirement receive separate judgments. |
| Produce useful sweep accounting | The audit covers updates, false positives and intentional preservation, with correct locations/counts and grouping. | Mechanical checks cover syntax and count reconciliation; judgment checks whether the account and reasons match the evidence. Missing accounting is a non-blocking procedural defect under the settled policy. |
| Justify a genuinely local change | Checking scope finds no related updates. | Inspect the scope evidence and preserved project, then check the required negative-form line separately. A one-file task description alone is not justification. |

Coverage limits: both pilot controls encountered all required current consumers before choosing a narrow repair (pilot 01 control `stdout.txt:8`; pilot 02 control `stdout.txt:10`). The completed pairs therefore support a repair-scope comparison, while discovery under larger-project conditions remains unobserved. The prepared Shiv case offers that observation alongside its primary functional outcomes; no extra case or repeat is required merely to demonstrate a discovery advantage. Semantic code-to-documentation drift is now required in baseline design; justified-local-change coverage remains deferred.
Facets may share cases; this does not require seven scenarios or seven initial runs.
Start process qualification with one non-reserved case exposing scope expansion, triage, reconciliation and accounting. Paths and semantic drift can be covered in later cases if the first would become overloaded; untested facets remain explicit gaps.
The initial real-model pilot asks whether inputs/skills are loaded as intended, tasks are feasible, traces and Git changes are retained, and separate functional/procedural judgments can be supported. It can expose case defects but does not establish coverage or stable skill effectiveness.

### Discovery-case preparation

The owner approved the discovery concept on 2026-09-13: present one broken command after a settled CLI rename, with real sibling consumers in a script, nested build file and CI. Observe finding a reference separately from deciding to repair it. The owner subsequently confirmed that packaging is only the concrete project context, not a skill-testing requirement, and approved proceeding with Shiv-based preparation. No provider dispatch is authorized.
The first [pilot 03 draft](cases/pilot-03/assessment.md) remains preserved and undispatched. Its 49 files / 505,460 bytes were largely vendored packaging source; first-party/independent-tool material was only 23 files / 12,246 bytes. Four application tests and eleven checker tests establish mechanical behavior, not the required discovery setting. Do not resume that draft merely because its checks pass.

The replacement implementation base is [Shiv](https://github.com/linkedin/shiv/tree/ff542cbe75ea832df3a989d07c7fdf5214f727fa), pinned at `ff542cbe75ea832df3a989d07c7fdf5214f727fa`. The [selection record](discovery-project-selection.json) retains source identities, alternatives and offline feasibility evidence. The unmodified checkout has 40 tracked files / 100,998 bytes; source, tests, documentation and CI account for 84,665 bytes / 2,514 lines without a vendor tree. Its 12 source files implement actual archive construction, CLI behavior and runtime bootstrapping. Keep its BSD license/NOTICE with any copied source. Steno, Comics App and the current runner remain eligible alternatives. Shiv was selected for the already-verified offline path and its fit to this approved scenario, not because the testing framework requires a packager or excludes first-party tools.
In the **study-only adaptation**, rename Shiv's long option `--output-file` to `--destination` while preserving the supported short alias `-o` and archive behavior. This is an injected settled change, not a claim about upstream history. Keep the literal change unambiguous; semantic drift remains a separate gap. The earlier illustrative `--output-dir` name belonged to the rejected synthetic draft.
Provider-free scratch probes built and ran a supplied greeting package through the actual upstream CLI. A guard would fail if pip installation were attempted; none occurred. A throwaway two-file source adaptation verified that `--destination` builds/runs the archive, old `--output-file` fails without creating one, and retained `-o` still works. The selection probe used an existing local Python/Click environment solely for feasibility; the completed case below supplies and qualifies its own runtime. No user project was changed or copied into a case.

The distinct `cases/discovery-shiv/` case preserves the rejected draft's identities. It pins upstream files before study modifications and records all modifications and first-party/dependency sizes separately. Its actual offline command consumers include the cited README command plus less-obvious script/build/CI consumers, historical context and a valid independent-interface preservation case. Do not supply a consumer list, search command or prohibition against reading all files. Exclude study guidance from subject inputs and use the frozen original only in its condition. Use the existing runner and a case-specific facts-only checker; no framework feature is proposed.
Record for each required consumer whether retained output exposes stale content, whether the agent explicitly identifies a repair, and whether the correct edit is committed. Filename listings alone are not content exposure; missing/truncated output leaves awareness uncertain. Final functional completeness and preservation lead the assessment, with procedure/accounting separately governed by SSR-assessment-2. Freeze the actual reference inventory, valid aliases and accounting scope before dispatch. This case tests location diversity: one suitably broad literal search can find every required consumer. It does not require synonym or path-variant reasoning; pilot 02 separately exercised relative-path variants in a small fixture, while difficult lexical/semantic discovery remains unestablished. If both conditions discover everything, retain that result without claiming a discovery advantage or enlarging the case to manufacture a miss.
The real project supplies more meaningful first-party context, but size still does not prove discovery difficulty. Validate actual commands and damaged/correct alternatives, comparable setup, evidence capture and dependency isolation before relying on the case. Semantic drift and the justified-local-only boundary remain open. Cases are retained in the eventual active catalog for distinct coverage, not because preparation was completed.
The remaining additional-development slot is unused under the accepted phase closure; no further pre-baseline pair is planned. The 36 unused outer subject slots do not authorize transfers. Keep protected comparison capacity intact. The accepted transition below directs baseline design instead of revising the development allocation. No subject, evaluator, authoring or retry calls were spent during project selection.

The distinct [Shiv case package](cases/discovery-shiv/assessment.md) is now locally prepared. It contains 50 project files / 106,979 bytes and a separately counted 19-file / 424,152-byte Click runtime. All 40 upstream files are retained; four have recorded study adaptations and ten project files are added. The settled CLI change and stale consumers are injected study material, not upstream history. Four public CLI tests and fourteen controller tests cover runnable archive behavior, partial repairs, preserved aliases, collateral changes, rollback and script location independence. Real runner loading/copying verifies 70 control versus 71 original inputs; isolated Python uses supplied Click/Shiv and completes an offline build with pip installation guarded against. These are local mechanical observations only; the full upstream suite and hosted CI are outside their scope.
The [qualification record](cases/discovery-shiv/qualification.json), [source provenance](cases/discovery-shiv/source-provenance.json) and [manifest](cases/discovery-shiv/manifest.json) retain identities and observations. Nine old-option occurrences across eight project paths define accounting scope before collection. Only the frozen original and its read instruction differ between conditions. The case assessment specifies disposable replay, semantic review, evidence limitations and the unchanged allocation gate. The checker verifies all 69 pristine reference inputs before replay and retains unknown probe results as null. The [pilot-wide verification record](pilot-review-2026-09-13.json) rechecks both earlier pairs' retained bundles, Git changes and runtime observations without changing their assessments. No model call or skill edit occurred during case preparation.

### Transition to baseline design

**Owner approved, 2026-09-13:** pre-baseline development is closed at four completed subject calls. Its one remaining additional-development slot stays unused. Baseline design is authorized, with Shiv considered for that suite instead of another development pair. This replaces the proposal to request an extra development slot. Prior pilot observations remain pilot evidence; no baseline invocation, capacity transfer or skill rewrite is authorized.
Choose the smallest baseline case set that supports the intended comparison, freezing cases, repetitions, assessment and commands before authorization. The existing baseline arithmetic is two cases × two conditions × two repetitions (eight calls); selecting Shiv within that set need not transfer capacity. Broader case coverage requires an explicit design/allocation decision, not an assumption that all named facets fit those two slots.
New discovery, semantic-drift or justified-local-change facets are designed for the baseline/transfer set when they help the decision, or remain explicit coverage gaps. They do not each trigger a new pre-baseline pair. Functional ties, successful controls, limited novelty and sparse accounting do not reopen development. An unresolved execution/evaluation defect is a readiness blocker to resolve or a reason to close inconclusive; any additional diagnostic invocation requires a named defect and separate owner-approved exception rather than an automatic extension. Later rewrite diagnostics remain a separate, already bounded phase.


### Proposed baseline case selection

**Status: owner accepted the three core situations on 2026-09-13; detailed case design, collection freeze and dispatch remain open.** The baseline will address standalone reconciliation after an interface rename, a moved file and changed behavior described in documentation. This supersedes the earlier two-case proposal; the two-case call table remains an unrevised allocation, not authority for expanded collection.

| Core situation | Case foundation | Status and useful evidence |
|---|---|---|
| Interface rename | [Shiv](cases/discovery-shiv/assessment.md) | Locally qualified, no model run. Four executable consumers across README, script, build and CI. Check complete repair, preservation and committed edits; discovery-versus-action is supporting evidence. |
| Moved file | [Pilot 02: moved guide](cases/pilot-02/assessment.md) | One development pair complete; fresh baseline runs still needed. Resolve different relative spellings to the intended guide, execute the export script from two directories and preserve the independent same-name vendor link. |
| Changed behavior | [Semantic delivery policy](cases/semantic-delivery/assessment.md) | Locally prepared and mechanically qualified. Three current claims express the same changed fact differently; historical and independent policies must be preserved. Semantic evaluator calibration remains open. |

The owner accepted the [semantic-drift concept below](#semantic-drift-concept-delivery-retries) and authorized construction. The six earlier SSR prompts were inspected for fit; none supplied the needed changed-behavior mechanism, so the case is newly authored. No historical rubric or result was inherited.

Pilot 01's cache-setting rename adds JSON/config representations but overlaps Shiv's literal-rename problem; retain its development evidence outside the selected baseline foundations. Preserve the rejected synthetic draft without resuming it. Selection uses observed pilot behavior, so these are development cases, not reserved evidence; new runs do not erase exposure or selection bias.

| Accepted facet | Planned baseline coverage | Limit |
|---|---|---|
| Broaden beyond the trigger | Unstated current consumers in the prepared cases and planned semantic case. | Complete reconciliation leads; discovering more than the control is not required. |
| Equivalent references and changed facts | Relative spellings in the moved-guide case; meaning-based documentation repair in the semantic case. | Inputs, runtime facts and semantic reference criteria are prepared; independent evaluator qualification remains open. |
| Moved paths | Three links and an executable export consumer. | Owner-clarified outcome, not proof the original explicitly teaches path resolution. |
| Triage and preservation | Historical records, independent interfaces, a same-name vendor link and semantic distinctions to define. | Preservation is judged by meaning and behavior, not byte identity alone. |
| Complete and commit | Working consumers and all required edits in retained Git history. | One-commit grouping is assessed separately from functional completeness. |
| Useful accounting | Each case's predefined scope under SSR-assessment-2. | Secondary procedural evidence; no aggregate score hiding outcome failures. |
| Genuinely local change | Deferred. | No claim about a justified negative sweep or its required negative-form account. |

Qualify model evaluation for semantic correctness/preservation, accepted alternatives, audit usefulness and trace interpretation before relying on it. Runtime/path tools and Git supply mechanical evidence; checker tests alone do not qualify the evaluator. Use contrasting examples from the current policy and batch across cases, never conditions of one case.

Rework subject/evaluator allocation after the semantic design. Three cases × original/no-target × two repetitions would be 12 baseline subject calls, versus the previously budgeted eight; retaining all three plus one transfer case with two repetitions in final original/candidate comparison would be 16, versus 12. These are scope illustrations, not approved counts. Reconcile repetitions, diagnostic capacity, comparison coverage and evaluation batches within the owner-approved pools, or propose an explicit revision. Do not silently transfer capacity or treat the original two-case arithmetic as a reason to omit core coverage.

Existing subject configurations use Codex Sol-low and workspace-write; recommend retaining them for continuity, with identities and order settled at freeze. Preserve the original skill snapshot, pilot criteria and old observations. The baseline index and versioned evaluation package will identify current case membership, source bytes, policy and fresh run identities; historical pilot commands do not authorize baseline dispatch.

Specialized search difficulty, justified-local-change behavior, native skill discovery, composition and population reliability remain outside this baseline design. Revisit a gap when needed for a proposed rewrite or a later coverage expansion; passing the selected cases alone does not establish universal SSR effectiveness. No reserved transfer case or provider invocation is authorized here.


### Semantic-drift concept: delivery retries

**Owner accepted the concept and authorized local construction.** The [case package](cases/semantic-delivery/assessment.md) now implements a small notification worker whose settled policy allows one initial send plus up to three retries, stopping on success. Three stale current descriptions express total attempts, additional tries and exhaustion. The historical policy and independent download helper retain their former/current three-attempt meanings respectively. No identifier or file move is involved.

The [task](cases/semantic-delivery/task.md) names only the README defect, permits project edits and requests a commit. Nine project files are supplied with TASK.md in both conditions; original alone adds the frozen skill. The runner loaded and copied 10 control versus 11 original entries with identical nine-file baseline trees and one prompt-line difference. The [manifest](cases/semantic-delivery/manifest.json) identifies subject and controller bytes; this verifies local preparation, not actual provider loading or host-wide guidance isolation.

Seven public behavior tests establish delivery exhaustion/early success and the independent helper's limit. Twelve controller tests cover facts-only replay and qualification integrity: rollback, altered limits, continued sends after success, missing APIs, timeouts, malformed/incomplete output, optimized Python and inherited Git overrides. The probe does not score prose. The [qualification record](cases/semantic-delivery/qualification.json) retains nine reconstructed documentation variants and their runtime/Git facts: pristine, README-only, complete, blanket number replacement, attempts/retries confusion, always-four wording, removed explanations, equivalent consolidation and correct-but-uncommitted work. All nine retain passing code tests, demonstrating why semantic assessment must inspect the documents.

The [expected meanings and accounting scope](cases/semantic-delivery/expected.json) permit equivalent wording and effective restructuring, with history/independent meaning preserved and all required repairs committed. Reference judgments are orchestrator-constructed and locally inspected; they are not model observations or independent evaluator qualification. Keep reference judgments out of future calibration packets. Model-evaluator qualification, neutral evidence packaging, versioned baseline formats and revised call allocation remain the next preparation work. No provider call, extra development pair or skill edit occurred during construction.

## Two-run process pilot

The [pilot case](cases/pilot-01/assessment.md) adapts the earlier ssr-02 situation into real files and executable consumers; the [expected outcomes](cases/pilot-01/expected.json) and [local qualification record](cases/pilot-01/qualification.json) replace the old inventory/rubric.
The first pass covers scope expansion, preservation, complete reconciliation and accounting. Remaining facets stay unbuilt; the [plan's pilot-status table](../../plans/2026-09-11-model-driven-skill-testing.md#stage-3-qualify-and-freeze-execution) scopes partial completion.
Both configurations and all declared source files are identified in [manifest.json](cases/pilot-01/manifest.json). Configuration loading, prompt parity and byte-for-byte fixture preparation passed without provider invocation: 14 common inputs, plus only the target skill in the original condition.
The original config now sources the frozen snapshot; subject-visible skill bytes and both prompts are unchanged. The manifest records the new source path and updated config/assessment hashes. The Setup criterion records control exploration of the common `.agents/` ignore entry without treating exploration alone as contamination.
Five constructed fixture variants demonstrate task feasibility and limitations of runtime-only checks; 70 synthetic files are hash-verified in the primary and backup paths recorded by the qualification record. These are local tool observations, not model performance.

Initial order is control, then original, one attempt each, using Codex `gpt-5.6-sol`, low effort, `workspace-write`, and the runner's 900-second per-call timeout. Installed Codex 0.154.0 and its executable hash match the prior permission qualification; both real calls completed with these settings and no runner infrastructure error.
No model evaluator is dispatched in this first pair: the orchestrator inspects pilot mechanics and developmental criteria directly. Independent model judgments and calibration remain unqualified for later measured collection.

Executed commands (retained for provenance, not an instruction to repeat), run from `/Users/simon/work/personal/disciplined-development-skills`; the namespaced temporary directory already exists:

```sh
TMPDIR=/private/tmp/ssr-process-pilot-20260912 skill-validation/runner/.venv/bin/python -m skilltest run skill-studies/sweeping-stale-references/cases/pilot-01/control.json
TMPDIR=/private/tmp/ssr-process-pilot-20260912 skill-validation/runner/.venv/bin/python -m skilltest run skill-studies/sweeping-stale-references/cases/pilot-01/original.json
```

Authorization status: the owner's 2026-09-12 continuation after review of `2ca4701` requests dispatch of the reviewed pair, following presentation of these exact configurations and commands. Scope is one control and one original subject attempt, with no additional calls or retries. Host permission allows the Codex app-server to initialize; the provider's workspace sandbox remains enabled. The external provider receives the declared synthetic project/task inputs and, in the original condition, SSR.
Before each dispatch verify the manifest and CLI identity; preserve each completed attempt's entire bundle with hash-verified primary and backup copies beneath the existing development stores at `pilot-01-runs/<run-id>/` before the next dispatch. Record source/destination paths and configuration identity in the run index.
Both complete bundles are preserved and hash-verified. The run index records measured sizes and the retention decision: complete raw evidence outside Git, manifests and concise assessments in Git.
Both attempts are complete; stop for process review; a setup failure, contamination, unreadable trace or preservation failure stops progression for diagnosis. No automatic retry, case mutation or additional model call is authorized by the outer ceiling.

## Authoring guidance and allocation

### Completed moved-file development pair

The owner approved the moved-file concept and local preparation on 2026-09-13. [Pilot 02](cases/pilot-02/assessment.md) is a new fixture: none of the six inspected historical SSR prompts exercises relative-path resolution. The owner subsequently selected the simpler three-Markdown-link/export-script version, retaining historical and unrelated same-name material to preserve. The site-config consumer was removed because it had no real builder; further consumer types can be added if needed.
The task flags one broken README link after a settled move. Expected path reconciliation is an owner-clarified functional outcome; a miss is not by itself disobedience to an explicit relative-path instruction. The case fixes accounting scope before observation, prioritizes the actual committed repair, and includes a controller-only copy of `SSR-assessment-2` with source/hash provenance in its manifest.
Local qualification: eight path-observer tests and seven constructed variants distinguish incomplete repair, correct equivalent paths, a wrong existing destination, damaged historical/vendor material and restoration of the old path. The export script fails in the initial/README-only states and works after complete repair from both project and external working directories. These are constructed local observations, not model results or calibrated model judgments.
Both configurations pass the real loader and workspace-copy checks: nine common project files plus the task, with only frozen SSR added to the original. Model settings remain Codex `gpt-5.6-sol`, low, `workspace-write`; CLI version/hash are recorded and must be rechecked before dispatch.
External review of `c1ca959` returned PASS with no findings, independently confirming the fixture, checks, input boundaries and proposed allocation. The owner then approved the exact pair below; both calls are complete. Frozen case documents retain their preparation-time status; this protocol and the run index record subsequent authorization and execution.

Approved commands executed from the canonical checkout:

```sh
TMPDIR=/private/tmp/ssr-pilot-02-20260913 skill-validation/runner/.venv/bin/python -m skilltest run skill-studies/sweeping-stale-references/cases/pilot-02/control.json
TMPDIR=/private/tmp/ssr-pilot-02-20260913 skill-validation/runner/.venv/bin/python -m skilltest run skill-studies/sweeping-stale-references/cases/pilot-02/original.json
```

The owner explicitly approved these exact two calls on 2026-09-13 after their commands, provider settings and preservation sequence were presented. Host permission allowed Codex app-server initialization while retaining the provider sandbox. The provider received the synthetic project/task and, for the original only, frozen SSR. No controller criteria, checks, expected outcomes or policy copy are subject inputs.
Control then original ran once each, preserving and inspecting complete bundles between calls under `development/pilot-02-runs/<run-id>/` in the existing primary/backup stores. The pair spent two of the three additional-development subject slots, leaving one; all other pools and measured-comparison capacity remain unchanged. Execution has stopped; no evaluator call, third run or automatic retry is authorized. Read isolation remains bounded by the earlier pilot's limitations.

[Pilot 02 results](pilot-02-results.md): original repaired and committed 4/4 consumers; control repaired and committed only README (1/4). Both preserved all protected material. The original searched before editing and supplied a useful complete account, with a minor six-versus-seven-path summary error that does not affect the functional result. The [run index](pilot-02-run-index.json) and [controller checks](pilot-02-checks.json) retain identities, preservation verification, Git evidence and independent replay facts. These are development inspections, not calibrated model-evaluator judgments. The owner accepted the results walkthrough and clarified that the seven matches were real, with README counted twice in the path summary. The subsequent external review of `e5381e2` returned PASS, reproducing the retained-bundle results and identifying the discovery-coverage gap recorded above. No case or scoring-policy change is required by these observations.

### Whole-study allocation

The four completed process checks used **Codex `gpt-5.6-sol`, low effort**, following the owner's request to use Sol low or Terra medium while establishing the process.
`gpt-5.6-terra`, medium effort, remains an alternative if later evidence supports a switch; do not silently pool different models' observations.
Pre-baseline development is closed at two completed original/no-target pairs. Apply the [closure rule](#transition-to-baseline-design) to any proposed diagnostic exception; this allocation grants no additional pilot run. The five-repetition wording campaign remains conditional later work.
Choose the measured baseline model before collection freeze and keep it fixed across comparison conditions; exact commands and provider-run authorization remain Stage 3 work.

Installed Superpowers is version **6.3.0**, verified from its plugin manifest; the inspected `writing-skills`, `testing-skills-with-subagents.md` and required TDD background are hashed in the source inventory.
The guidance requires observed failure without the target before authoring, a change matched to the failure type, and five or more repetitions per variant for wording micro-tests.
It also calls for combined realistic pressures for discipline behavior and actual action rather than reciting the rule.
These inform Stage 2 design; illustrative multiple-choice prompts and historical performance claims in the guidance do not become this study's evidence or universal acceptance criteria.

The owner accepted outer ceilings of **40 subject / 12 evaluator / 4 authoring / 4 retry invocations** and **20 active hours**. The phase allocation below remains a planning envelope for at most one selected rewrite attempt, not authorization to run the whole campaign.
The table retains the original two-development-case/one-transfer-case arithmetic for comparison with the pending revision. It is superseded as a case-selection proposal by the [three accepted core situations](#proposed-baseline-case-selection); revise baseline and final-comparison counts together before freeze. Neither the table nor remaining capacity authorizes dispatch.

| Phase | Subject | Evaluator | Authoring | Retry | Allocation basis |
|---|---:|---:|---:|---:|---|
| Pilot and evaluator calibration | 2 | 2 | 0 | 0 | One non-reserved pilot slot in original/no-target conditions; two fresh calibration calls on constructed, independently checkable references. |
| Original baseline | 8 | 4 | 0 | 0 | Two development slots × two conditions × two repetitions; one evaluator batch per condition/repetition across distinct cases. |
| Rewrite and wording diagnostic | 15 | 0 | 4 | 0 | One development probe × original/no-target/candidate × five repetitions; authoring pool covers diagnosis, one candidate and inspection/selection, not four promised revisions. |
| Additional development capacity | 3 | 0 | 0 | 0 | Two used by pilot 02; the remaining one stays unused after the owner-approved pre-baseline closure. No further pre-baseline dispatch is planned. |
| Protected final comparison | 12 | 4 | 0 | 0 | Two development slots plus one transfer slot × original/candidate × two repetitions; one evaluator batch per condition/repetition across distinct cases. |
| Evaluation repair/check reserve | 0 | 2 | 0 | 0 | Additional calibrated assessment or declared disagreement checks; cannot consume subject or authoring capacity. |
| Retry reserve | 0 | 0 | 0 | 4 | Every repeated failed attempt draws here; preserve the original attempt. |
| **Total ceiling** | **40** | **12** | **4** | **4** | **60**, including reserves; unused capacity need not be spent. |

Calibration batches use distinct constructed examples, without reference answers; baseline/comparison batches never juxtapose conditions of the same case.
Model judgments used for baseline/comparison occur in the evaluator allocation; routine orchestration is not a source of unrecorded substitute scores.
Pilot mechanics use direct evidence inspection. Wording diagnostics must be checkable with validated mechanical checks plus author inspection of every flagged match; any needed independent semantic evaluation must fit the evaluator reserve or trigger an allocation revision before dispatch.
Author inspection is development evidence, not independent evaluation.

For a shaping rewrite, run the five no-target diagnostic samples first and inspect them before spending the five original and five candidate slots.
If the control supplies no observed failure supporting the proposed rewrite, retain that result and stop the diagnostic campaign; resolve the pure-cleanup/RED conflict with the owner before editing, without automatically selecting another probe to hunt for failure.
Otherwise run the five original samples before authoring and the five candidate samples afterward.
Any edit after candidate diagnostic results creates a new variant requiring its own qualifying evidence; the present allocation does not promise that second cycle.
The final comparison must use the exact selected candidate bytes.

The final comparison supports original-versus-candidate performance only; a new no-target arm is not included there, so it cannot establish contemporaneous benefit over unguided behavior.
Two repetitions per full case and one transfer slot support descriptive observations, not a stable reliability or variability estimate; report variability as **not estimable** for population-level claims.
If the allocation cannot support a decision, close inconclusive or retain the original rather than weaken the acceptance question.

### Time allocation and forecast

The original planning targets remain 240 minutes for contract/test preparation and 180 for qualification/calibration, followed by 180 baseline, 300 authoring/diagnostics, 240 comparison and 60 closure: **1,200 minutes total**. They were not separately metered. The original 220-minute booking includes mixed preparation, tooling investigation, qualification and review; its historical split is unknown. The subsequent 42 booked minutes cover preparation review, budget reconciliation, baseline case design and semantic-delivery construction/qualification/remediation and commit verification, for 262 minutes total. Reconcile that shared 420-minute envelope below without inventing phase-level actuals.

| Work category | Original estimate (minutes) | Booked use | Estimate less use | Estimated remaining work / status |
|---|---:|---:|---:|---|
| Preparation + qualification (240 + 180) | 420 | 220 historical + 42 preparation/qualification | 158 | 210–300; forecast variance of 52–142 minutes above the original estimate. |
| Baseline collection and assessment | 180 | 0 | 180 | Reforecast from frozen cases, evaluator configuration and measured latencies before dispatch; fit not yet established. |
| Authoring and diagnostics | 300 | 0 | 300 | Objective-dependent; unstarted, no fit claim. |
| Comparison | 240 | 0 | 240 | Reforecast after comparison design; preserve necessary comparison work. |
| Closure | 60 | 0 | 60 | Unstarted; retain allowance. |
| Document-tool implementation and qualification | Not in original estimate | 0 implementation | Not applicable | Preliminary 120-minute estimate after baseline assessment; refine with scoped design. This adds forecast effort, not authorized capacity. |
| Original total / overall authorization ceiling | 1,200 | 262 | 938 | See aggregate forecast below. |

Aggregate planning scenario: carry forward 180 + 300 + 240 + 60 = 780 minutes for baseline, authoring/diagnostics, comparison and closure, alongside the updated 210–300-minute preparation/qualification forecast. The later phases have not been re-estimated; this scenario assumes the full rewrite/comparison work proceeds.

| Scope | Remaining forecast (minutes) | Projected whole-study total, including 262 booked | Forecast above 1,200-minute ceiling |
|---|---:|---:|---:|
| Study excluding document-tool implementation | 990–1,080 | 1252–1342 | 52–142 |
| Study including preliminary 120-minute tool estimate | 1,110–1,200 | 1372–1462 | 172–262 |

Remaining authorized time is **938 minutes**, below both scenario ranges. Present this potential extension need now and refine it at the baseline-design walkthrough using the selected cases, evaluator work and tool scope. No extension is approved by this forecast. Continue currently authorized design within the remaining ceiling; do not remove necessary qualification merely to make the arithmetic fit.

The forward preparation/qualification estimate is a controller planning estimate, not measured effort: 60–90 minutes for baseline case selection/design, 60–90 for six concise artifact contracts and their application, and 90–120 for evaluator setup, constructed references, two calibration calls and assessment. Those estimates total 210–300 minutes; calibration is still unqualified. They predate the three-situation coverage decision and remain an illustrative planning scenario, not a forecast validated for the expanded suite. The semantic case is now constructed; replace this scenario with an updated forecast when setting the three-case allocation, evaluator work and remaining format preparation. It is not a current fit claim. Format agreement is inside preparation; implementation and its own tests belong to the separate tooling estimate. The preliminary 120-minute estimate is neither a cap nor a promise of completion.

At every active-work checkpoint, update this table with the cumulative accounting below: assign new time to its work category, preserve the mixed historical booking as such, and reconcile total use once. Include review, storage and model waits in the category they support. Revise remaining-work estimates when scope or observed effort changes. Unknown estimates remain explicit uncertainty. Compare aggregate remaining effort with remaining authorized time and update the extension forecast alongside the phase rows.

**SSR application of the [effort policy](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#4-pilot-and-freeze-the-experiment-plan):** timing variance prompts scope review, not a failure verdict or weaker qualification. The 20-hour autonomous-work ceiling remains unchanged; present forecast extension needs at the baseline-design walkthrough and obtain approval before exceeding it.

Pilot 01 model durations were 47.936 and 59.891 seconds (107.827 seconds total). Pilot 02 took 37.782 and 76.784 seconds (114.566 seconds total). At the four-call mean, 60 similar calls would take about 56 minutes; this is illustrative, not a forecast for longer subjects/evaluators. The runner's 900-second timeout is not an expected duration.
At that timeout for every call, latency alone would consume 15 hours, so the ceilings are not a promise that every call fits; substitute pilot measurements and stop under the agreed limit.
Default to sequential dispatch; no concurrency tool is proposed now.

## Runner findings and pilot requirements

Source inspection covers the [operator guide](../../skill-validation/runner/README.md), config loader, workspace preparation and both provider/runtime paths identified in the source inventory.
Existing offline configuration/workspace tests passed: **37 passed**, using `.venv/bin/python -m pytest -q tests/test_config.py tests/test_workspace.py` from `skill-validation/runner/`.
This verifies existing local mechanics, not installed-provider behavior or this study's readiness.

| Finding | Consequence for preparation |
|---|---|
| Each fixture source must be a regular file; directory entries and final symlinks are rejected. Nested target parents are created automatically. | A repository-shaped tree is supported through file-by-file declarations. Start with explicit manifests; propose a deterministic manifest generator only if actual preparation shows repeated omission/error or material effort. No new tool is needed merely to represent directories. |
| The runner creates a fresh template-free Git boundary and rejects fixture-root `.git` input. | Do not copy Git directories. Supply a test identity and arrange a verified original baseline before reconciliation; any bootstrap baseline commit is setup, followed by the one scored reconciliation commit. Pilot must demonstrate this sequence and retained history. |
| Providers capture raw streams and final filesystem inventories; inventories alone do not prove action order. | Pilot must establish readable search/edit/commit traces, prepared-input hashes, preserved original bytes and the first-bundle retention decision. |
| Codex has a private profile and explicit configuration controls; Claude has scoped HOME contamination denials. Neither inspected adapter explicitly denies reading the proposed study stores or canonical source checkout. | Do not claim hidden-case or omitted-skill isolation from directory separation. Qualify read restrictions against the stores, source skill copies and evaluator checkout before those attribution claims; the current runner alone has not established them. |
| Model calls are synchronous with a fixed 900-second timeout; provider/model/effort fields are passed through. | Verify the selected initial Sol-low configuration, executable version and permissions in Stage 3. CLI identities for the permission probes are recorded below; model availability, authentication and model latency remain unqualified. |

Reserved-case isolation remains an explicit capability gap, not authorization to expand the runner.
Owner direction: the abandoned testing effort included skill/environment isolation work. Do not investigate it now; consult that implementation or evidence if a concrete isolation issue arises, verifying applicability to the current runner and treating it as technical reference rather than authority to resume the abandoned methodology.
Keep the transfer slot only if restrictions can be established within the budget; otherwise classify it as additional development evidence and disclose the reduced claim before collection.
The no-target control separately requires demonstrating that the omitted skill is not loaded through host files or ambient instructions; if that fails, the control is invalid for contribution claims.
The owner approved exposing read-only permissions for both providers, replacing the earlier no-tools proposal.
The runner now accepts optional `execution.permissions`: `workspace-write` preserves existing behavior; `read-only` denies model writes to project files, supplied evidence and Git while retaining read/search tools.
Codex uses a read-only permission profile; Claude applies a process-tree sandbox with only private runtime scratch and `/dev/null` write exceptions.
Controller-owned preparation and output capture remain available; neither permission mode disables skills or limits reads to the supplied evidence alone.
Claude read-only runs omit dedicated Write/Edit tools while retaining sandboxed Bash and evidence reads.
New result records use schema `0.3` and include the resolved `execution.permissions`; input configurations remain schema `0.2`.
Before scoring, compare that mode and the configuration identity against the frozen condition: subjects require `workspace-write`, evaluators require `read-only`. A mismatch is an invalid setup, not a skill failure.
CLAUDE.md now explicitly accepts verified read-only permissions as an alternative to a no-write-tool agent type.

Provider-free checks against Codex **0.154.0** and Claude Code **2.1.269** passed: evidence reads and captured output, denied overwrites/deletion/renames/directory creation, denied Git mutations and outside-workspace writes, and denied symlink escapes.
Claude's private scratch allowance and Codex's existing writable Git behavior were also exercised.
The initial nested-sandbox attempts failed at host sandbox setup; rerunning the same local probes with host permission passed, without authentication or model calls.
Retained evidence, CLI identities and implementation source hashes are indexed in [permissions-qualification.json](permissions-qualification.json).
This establishes a feasible evaluator permission mechanism; Stage 3 still must qualify the actual selected model run, assessment capture and information boundaries.
Evaluator model/effort, exact evidence inputs, criteria and spending authorization remain to be fixed before dispatch; initial subjects remain Sol low.

## Storage and accounting

Canonical project checkout: `/Users/simon/work/personal/disciplined-development-skills`.
Reserved primary: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/`.
Reserved backup: `/Users/simon/work/personal/skill-study-backups/sweeping-stale-references/`.
External raw development primary: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/`; backup: `/Users/simon/work/personal/skill-study-backups/sweeping-stale-references/development/`.
These locations are resolved from the canonical checkout. The development primary and backup now contain the permission-probe bundles and all four complete pilot bundles indexed above; reserved-case access isolation remains unqualified.
An author receives only permitted copied development evidence, not access to their reserved parent directories.
Apply the plan's copy/hash/backup barrier before each later dispatch, and inspect the first pilot bundle before deciding Git retention.
Both copies remain on this host; they do not protect against host loss.

Accounting began at the first recorded clock checkpoint, **2026-09-12 04:22:19 UTC**, with a conservative **two-minute allowance** for the opening read before that checkpoint.
This preparation consumes active study time toward the accepted ceiling; recorded owner-wait intervals are excluded.
Dispatched study invocations so far: **4 subject, 0 evaluator, 0 authoring, 0 retry**. Remaining outer capacity is 36 / 12 / 4 / 4 respectively; no further call is authorized by either completed pair.
The orchestrator's preparation conversation and local tool calls consume active time, not provider-invocation slots; model assessments or authoring work must be accounted under their declared roles.

Owner walkthrough: the contract, outer limits, pilot 01 findings and pilot 02 concept are settled. Pilot 02 results and the path-count explanation have been walked through with the owner; that checkpoint was committed and pushed. Shiv case preparation is complete. Three core situations are accepted and their case foundations are prepared; exact suite freeze, evaluator qualification, revised allocation and provider dispatch remain pending.
Independent use is settled; Stage 3 has observed the declared standalone setup for this pair; broader isolation and model-evaluator qualification remain open.

Accounting updated, 2026-09-13: **book 262 active minutes through semantic-delivery review, verification and commit preparation**, leaving **15 hours 38 minutes** under the accepted 20-hour ceiling. This replaces, rather than adds to, earlier bookings.
Source: the current task's local log at `/Users/simon/.codex/sessions/2026/09/11/rollout-2026-09-11T17-59-42-01a0927b-cef5-7db0-8a30-c76c5b1ae838.jsonl`; only boundary timestamps were extracted, not conversation contents.
Reconstruction sums the union of 107 closed `task_complete` / `turn_aborted` intervals since Stage 1 began: **15,418.0 seconds (256.97 minutes)**, including model/tool waits inside turns and excluding inter-turn owner-wait.
The current turn began at 2026-09-14 00:31:31 UTC and adds 53 seconds at the 2026-09-14 00:32:24 UTC checkpoint. Retain the original two-minute opening allowance and allow two minutes for completion; round 261.85 minutes up to 262. Closing allowance and rounding are estimates, not independently measured owner/Claude effort. Provider durations are already inside active-turn time and are not added again.
At the next checkpoint, recompute cumulative closed-turn intervals plus the opening allowance and round up; do not add already counted turns or restore the superseded checkpoints. If the completed current turn exceeds the booking, correct the total before approving the remaining budget.

Relationship-correction verification: all **21** source identities match, including all nine DD skills at the recorded revision; local links resolve and `git diff --check` passes.
Hook suite: **263 passed, 3 skipped**. These documentation checks do not qualify provider execution or demonstrate skill effectiveness.
