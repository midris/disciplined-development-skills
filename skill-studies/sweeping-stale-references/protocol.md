# Sweeping stale references: study protocol

Status: Stage 1 complete; Stage 2 conceptual coverage accepted; pilot 01 complete and externally reviewed PASS. Pilot 02's approved moved-file pair is complete; the owner accepted the results walkthrough and clarified path-count explanation, 2026-09-13.
The owner selected `sweeping-stale-references`, authorized contract/allocation preparation and clarified that this skill should be evaluated independently.
The behavioral contract and outer ceilings are agreed; both authorized pilot pairs are complete and further execution remains subject to its own recorded scope.
Progress belongs to the [plan](../../plans/2026-09-11-model-driven-skill-testing.md); general requirements belong to the [spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md).
Four subject observations are recorded across [pilot 01](pilot-results.md) and [pilot 02](pilot-02-results.md), each linking its run index and controller checks. No measured baseline or skill rewrite has been created.

**Operating model:** the active Codex/Claude session runs scenarios, waits for evidence, applies the versioned rules and writes fixed-format score records; a human can use the same rules. The owner reaffirmed this existing intent on 2026-09-14. Separate evaluator dispatch, calibration and concealed answer-key work are not prerequisites. The two-call calibration proposal and full-campaign allocations below are superseded as an execution plan. See the [general workflow](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#default-work-session-workflow).

The owner accepted the seven-section [protocol layout](../formats/protocol.template.md): current decisions and brief rationale belong beside their subjects, with Git retaining history. Full version-1 migration remains pending.

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

A copyable snapshot of the current policy is [SSR-assessment-3.txt](assessment-policies/SSR-assessment-3.txt). It is derived verbatim from the following section; refresh unrun controller copies when changing the policy, while preserving observed-run inputs.

The owner accepted the [criterion card and completed score record](../formats/README.md): use brief entries, precise evidence citations and references to shared rules rather than repeated prose.
Scores retain assessor context, separate setup validity and functional/procedural judgments; summaries synthesize those judgments.
The policy-3 pilot-02 example is separately indexed without replacing its original assessment. Unrun Shiv and semantic-delivery controller packages carry policy-3 copies; their subject inputs remain unchanged.
Remaining companion-format agreement and version-1 migration are pending; format acceptance does not authorize runs or change scoring decisions.

### Current SSR assessment policy

Policy identity: **SSR-assessment-3**, 2026-09-14 workflow correction. The owner’s functional/procedural scoring decisions from SSR-assessment-2 remain unchanged; this version removes the unintended separate-evaluator/calibration prerequisite and makes active-session assessment the default. Observed-run case inputs, historical worked examples and prior assessments retain their policy-2 copies and identities; their preparation-time calibration requirements are superseded as workflow. Current controller inputs for unrun cases use policy 3. New assessments must identify policy 3 alongside the applicable versioned case criteria; do not overwrite historical scores or silently relabel old inputs.
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

For every subsequent assessment, the active agent or human reads this policy and the applicable case criteria, inspects the retained evidence and writes the fixed-format score record. Record policy/criteria identities, assessor context, run/configuration/skill identities, evidence citations, per-criterion judgments and consequences. Copy or identify the exact policy bytes used; keep these scoring instructions out of subject inputs. Active-session assessment is a normal scored result, not an unrecorded substitute for a separately dispatched evaluator.
Before another case is dispatched, map its criteria to functional or procedural outcomes and their consequences under this policy. Apply these settled distinctions directly: complete committed reconciliation with sparse accounting succeeds functionally; incomplete reconciliation fails despite a perfect account; correct-but-uncommitted work fails the required committed outcome. Worked examples can resolve a genuine ambiguity but do not require separate model calls or an evaluator qualification gate.
If a judgment contradicts those boundaries, correct and version the assessment; do not blame or rerun the subject to repair the scoring. The runner captures evidence and configuration identity; it does not enforce these semantic judgments automatically.
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

**Owner priority, 2026-09-13:** establish the core value first: identify affected references beyond the cited defect, reconcile them correctly, preserve unrelated and historical meaning, and commit the completed repair. Broad searching is part of the skill's explicit procedure; finding more than the control is a diagnostic comparison, not an additional success requirement. Observe search, triage and accounting under the current assessment policy without making a discovery advantage or exhaustive facet coverage a prerequisite to the first baseline. Complete repairs prompted by SSR remain useful evidence even when the control saw the same references.

**Owner coverage decision:** include three core situations in baseline design: interface rename, moved file and changed behavior described in documentation. Use Shiv and the moved-guide case as the prepared foundations, and design semantic drift before freezing collection. The earlier proposal to defer semantic drift is superseded. Specialized discovery challenges and additional boundaries can wait; trustworthy evidence and fixed interpretation rules remain necessary; the active session applies them.

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
Record for each required consumer whether retained output exposes stale content, whether the agent explicitly identifies a repair, and whether the correct edit is committed. Filename listings alone are not content exposure; missing/truncated output leaves awareness uncertain. Final functional completeness and preservation lead the assessment, with procedure/accounting separately governed by the current assessment policy. Freeze the actual reference inventory, valid aliases and accounting scope before dispatch. This case tests location diversity: one suitably broad literal search can find every required consumer. It does not require synonym or path-variant reasoning; pilot 02 separately exercised relative-path variants in a small fixture, while difficult lexical/semantic discovery remains unestablished. If both conditions discover everything, retain that result without claiming a discovery advantage or enlarging the case to manufacture a miss.
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
| Changed behavior | [Semantic delivery policy](cases/semantic-delivery/assessment.md) | Locally prepared and mechanically qualified. Three current claims express the same changed fact differently; historical and independent policies must be preserved. The active session judges semantic correctness from the documents and fixed rules. |

The owner accepted the [semantic-drift concept below](#semantic-drift-concept-delivery-retries) and authorized construction. The six earlier SSR prompts were inspected for fit; none supplied the needed changed-behavior mechanism, so the case is newly authored. No historical rubric or result was inherited.

Pilot 01's cache-setting rename adds JSON/config representations but overlaps Shiv's literal-rename problem; retain its development evidence outside the selected baseline foundations. Preserve the rejected synthetic draft without resuming it. Selection uses observed pilot behavior, so these are development cases, not reserved evidence; new runs do not erase exposure or selection bias.

| Accepted facet | Planned baseline coverage | Limit |
|---|---|---|
| Broaden beyond the trigger | Unstated current consumers in the three prepared cases. | Complete reconciliation leads; discovering more than the control is not required. |
| Equivalent references and changed facts | Relative spellings in the moved-guide case; meaning-based documentation repair in the semantic case. | Inputs, runtime facts and semantic criteria are prepared; the active session applies them and records its reasoning. |
| Moved paths | Three links and an executable export consumer. | Owner-clarified outcome, not proof the original explicitly teaches path resolution. |
| Triage and preservation | Historical records, independent interfaces, a same-name vendor link and the prepared semantic distinctions. | Preservation is judged by meaning and behavior, not byte identity alone. |
| Complete and commit | Working consumers and all required edits in retained Git history. | One-commit grouping is assessed separately from functional completeness. |
| Useful accounting | Each case’s predefined scope, with current assessments applying SSR-assessment-3. | Secondary procedural evidence; no aggregate score hiding outcome failures. |
| Genuinely local change | Deferred. | No claim about a justified negative sweep or its required negative-form account. |

The active session inspects semantic correctness/preservation, accepted alternatives, audit usefulness and trace evidence under the fixed rules. Runtime/path tools and Git supply mechanical facts. Missing or ambiguous evidence yields insufficient evidence or a versioned rule/assessment correction, not a mandatory evaluator-calibration campaign. The prior semantic-calibration fallback is superseded: semantic-delivery uses the same active-session scoring workflow as the other cases and does not depend on a new evaluator capability.

Rework the next authorized run allocation around the session workflow. The following figures describe the superseded full-campaign scenario, not a required run count: Three cases × original/no-target × two repetitions would be 12 baseline subject calls, versus the previously budgeted eight; retaining all three plus one transfer case with two repetitions in final original/candidate comparison would be 16, versus 12. These are scope illustrations, not approved counts. Reconcile repetitions, diagnostic capacity, comparison coverage and evaluation batches within the owner-approved pools, or propose an explicit revision. Do not silently transfer capacity or treat the original two-case arithmetic as a reason to omit core coverage.

Existing subject configurations use Codex Sol-low and workspace-write; recommend retaining them for continuity, with identities and order settled at freeze. Preserve the original skill snapshot, pilot criteria and old observations. The baseline index and versioned evaluation package will identify current case membership, source bytes, policy and fresh run identities; historical pilot commands do not authorize baseline dispatch.

Specialized search difficulty, justified-local-change behavior, native skill discovery, composition and population reliability remain outside this baseline design. Revisit a gap when needed for a proposed rewrite or a later coverage expansion; passing the selected cases alone does not establish universal SSR effectiveness. No reserved transfer case or provider invocation is authorized here.


### Semantic-drift concept: delivery retries

**Owner accepted the concept and authorized local construction.** The [case package](cases/semantic-delivery/assessment.md) now implements a small notification worker whose settled policy allows one initial send plus up to three retries, stopping on success. Three stale current descriptions express total attempts, additional tries and exhaustion. The historical policy and independent download helper retain their former/current three-attempt meanings respectively. No identifier or file move is involved.

The [task](cases/semantic-delivery/task.md) names only the README defect, permits project edits and requests a commit. Nine project files are supplied with TASK.md in both conditions; original alone adds the frozen skill. The runner loaded and copied 10 control versus 11 original entries with identical nine-file baseline trees and one prompt-line difference. The [manifest](cases/semantic-delivery/manifest.json) identifies subject and controller bytes; this verifies local preparation, not actual provider loading or host-wide guidance isolation.

Seven public behavior tests establish delivery exhaustion/early success and the independent helper's limit. Twelve controller tests cover facts-only replay and qualification integrity: rollback, altered limits, continued sends after success, missing APIs, timeouts, malformed/incomplete output, optimized Python and inherited Git overrides. The probe does not score prose. The [qualification record](cases/semantic-delivery/qualification.json) retains nine reconstructed documentation variants and their runtime/Git facts: pristine, README-only, complete, blanket number replacement, attempts/retries confusion, always-four wording, removed explanations, equivalent consolidation and correct-but-uncommitted work. All nine retain passing code tests, demonstrating why semantic assessment must inspect the documents.

The [expected meanings and accounting scope](cases/semantic-delivery/expected.json) permit equivalent wording and effective restructuring, with history/independent meaning preserved and all required repairs committed. Constructed references illustrate rule application; the active agent assesses real run evidence under the current policy. The [separate-evaluator proposal](../../plans/specs/2026-09-14-ssr-evaluator-calibration.md) is superseded. Its [eleven-record package](evaluation/calibration-draft/README.md) is retained as worked-example material, not a pending calibration gate. Exact reusable rule/score formats and the next run configuration remain to be settled. No provider call or skill edit followed from these constructions.

## Two-run process pilot

The [pilot case](cases/pilot-01/assessment.md) adapts the earlier ssr-02 situation into real files and executable consumers; the [expected outcomes](cases/pilot-01/expected.json) and [local qualification record](cases/pilot-01/qualification.json) replace the old inventory/rubric.
The first pass covers scope expansion, preservation, complete reconciliation and accounting. Remaining facets stay unbuilt; the [plan's pilot-status table](../../plans/2026-09-11-model-driven-skill-testing.md#stage-3-qualify-and-freeze-execution) scopes partial completion.
Both configurations and all declared source files are identified in [manifest.json](cases/pilot-01/manifest.json). Configuration loading, prompt parity and byte-for-byte fixture preparation passed without provider invocation: 14 common inputs, plus only the target skill in the original condition.
The original config now sources the frozen snapshot; subject-visible skill bytes and both prompts are unchanged. The manifest records the new source path and updated config/assessment hashes. The Setup criterion records control exploration of the common `.agents/` ignore entry without treating exploration alone as contamination.
Five constructed fixture variants demonstrate task feasibility and limitations of runtime-only checks; 70 synthetic files are hash-verified in the primary and backup paths recorded by the qualification record. These are local tool observations, not model performance.

Initial order is control, then original, one attempt each, using Codex `gpt-5.6-sol`, low effort, `workspace-write`, and the runner's 900-second per-call timeout. Installed Codex 0.154.0 and its executable hash match the prior permission qualification; both real calls completed with these settings and no runner infrastructure error.
No model evaluator is dispatched in this first pair: the orchestrator inspects pilot mechanics and developmental criteria directly. These existing direct inspections remain valid development records; later scored collection uses the same active-session assessment responsibility with the agreed fixed record format.

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

[Pilot 02 results](pilot-02-results.md): original repaired and committed 4/4 consumers; control repaired and committed only README (1/4). Both preserved all protected material. The original searched before editing and supplied a useful complete account, with a minor six-versus-seven-path summary error that does not affect the functional result. The [run index](pilot-02-run-index.json) and [controller checks](pilot-02-checks.json) retain identities, preservation verification, Git evidence and independent replay facts. These are recorded development inspections by the active agent; they do not claim independent evaluation. The owner accepted the results walkthrough and clarified that the seven matches were real, with README counted twice in the path summary. The subsequent external review of `e5381e2` returned PASS, reproducing the retained-bundle results and identifying the discovery-coverage gap recorded above. No case or scoring-policy change is required by these observations.

### Whole-study allocation

**Superseded planning scenario:** the tables and diagnostic sequence below retain the former campaign arithmetic. They are not required steps or spending authority for the session workflow. The outer ceilings remain unchanged; active-session scoring uses session effort and zero separate evaluator invocations. Choose and re-estimate the next useful run set before dispatch. No unused pool is automatically transferred.

The four completed process checks used **Codex `gpt-5.6-sol`, low effort**, following the owner's request to use Sol low or Terra medium while establishing the process.
`gpt-5.6-terra`, medium effort, remains an alternative if later evidence supports a switch; do not silently pool different models' observations.
Pre-baseline development is closed at two completed original/no-target pairs. Apply the [closure rule](#transition-to-baseline-design) to any proposed diagnostic exception; this allocation grants no additional pilot run. The five-repetition wording campaign remains conditional later work.
Choose the measured baseline model before collection freeze and keep it fixed across comparison conditions; exact commands and provider-run authorization remain Stage 3 work.

Installed Superpowers is version **6.3.0**, verified from its plugin manifest; the inspected `writing-skills`, `testing-skills-with-subagents.md` and required TDD background are hashed in the source inventory.
The guidance requires observed failure without the target before authoring, a change matched to the failure type, and five or more repetitions per variant for wording micro-tests.
It also calls for combined realistic pressures for discipline behavior and actual action rather than reciting the rule.
These inform Stage 2 design; illustrative multiple-choice prompts and historical performance claims in the guidance do not become this study's evidence or universal acceptance criteria.

The owner accepted outer ceilings of **40 subject / 12 evaluator / 4 authoring / 4 retry invocations** and **20 active hours**. The phase allocation below is retained as historical planning, not the current session execution plan.
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

**Aggregate subject-call scenario for the three accepted core situations:** retain two repetitions, the full conditional wording diagnostic and one transfer case in comparison.

| Subject pool comparison | Calls |
|---|---:|
| Accepted ceiling | 40 |
| Spent in the two development pairs | 4 |
| Remaining outer capacity | 36 |
| Remaining forecast: 12 baseline + 15 diagnostic + 16 comparison | 43 |
| Projected whole-study use: 4 + 43 | 47 |
| Forecast above the subject ceiling | 7 |

This is also eight more calls than the former 35-call remaining baseline/diagnostic/comparison schedule; the one unused development slot is not silently reassigned. The seven-call figure compares projected use with the outer ceiling, not an approved phase transfer. Evaluator, authoring and retry pools remain separate. The diagnostic campaign may stop under its existing rule, but do not count on that conditional saving to claim the full plan fits. Present this call shortfall alongside the aggregate time forecast at the baseline-design walkthrough; revise the allocation or request an explicit extension before dispatch without omitting agreed core coverage merely to fit the old table.

The active agent records baseline/comparison judgments directly; they do not require an evaluator-pool invocation. Optional separately dispatched evaluations, if later selected, retain their own budget and input/permission requirements. No such call is currently authorized.

The following wording-diagnostic sequence is an unexecuted part of the superseded proposal, not a requirement for every edit; reconcile any actual authoring workflow with the selected change and `writing-skills` before execution.
For a shaping rewrite, run the five no-target diagnostic samples first and inspect them before spending the five original and five candidate slots.
If the control supplies no observed failure supporting the proposed rewrite, retain that result and stop the diagnostic campaign; resolve the pure-cleanup/RED conflict with the owner before editing, without automatically selecting another probe to hunt for failure.
Otherwise run the five original samples before authoring and the five candidate samples afterward.
Any edit after candidate diagnostic results creates a new variant requiring its own qualifying evidence; the present allocation does not promise that second cycle.
The final comparison must use the exact selected candidate bytes.

The final comparison supports original-versus-candidate performance only; a new no-target arm is not included there, so it cannot establish contemporaneous benefit over unguided behavior.
Two repetitions per full case and one transfer slot support descriptive observations, not a stable reliability or variability estimate; report variability as **not estimable** for population-level claims.
If the allocation cannot support a decision, close inconclusive or retain the original rather than weaken the acceptance question.

### Time allocation and forecast

The [current accounting](#storage-and-accounting) owns spent effort and remaining capacity; superseded campaign estimates are available in Git, not carried as current forecasts.
Remaining work is format migration and collection preparation, authorized baseline collection/assessment, separately scoped document tooling, and any evidence-supported rewrite/comparison before closure.
Re-estimate selected work by category before collection freeze; rewrite/comparison estimates depend on the eventual objective, so no whole-study fit is claimed yet.
Document tooling retains a preliminary 120-minute implementation/qualification estimate, to be refined with its scope and CLI after baseline assessment; this is an estimate, not additional authorized capacity.
Timing variance prompts scope review under the [effort policy](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#4-pilot-and-freeze-the-experiment-plan), never weaker scoring or an automatic extension.
Pilot latency evidence is in the two result reports; use it when forecasting the selected runs, with sequential dispatch as the default.

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
If held-out transfer is explicitly selected, keep its slot only if restrictions can be established within the budget; otherwise classify it as additional development evidence and disclose the reduced claim before collection.
The no-target control separately requires demonstrating that the omitted skill is not loaded through host files or ambient instructions; if that fails, the control is invalid for contribution claims.
The owner approved exposing read-only permissions for both providers, replacing the earlier no-tools proposal.
The runner now accepts optional `execution.permissions`: `workspace-write` preserves existing behavior; `read-only` denies model writes to project files, supplied evidence and Git while retaining read/search tools.
Codex uses a read-only permission profile; Claude applies a process-tree sandbox with only private runtime scratch and `/dev/null` write exceptions.
Controller-owned preparation and output capture remain available; neither permission mode disables skills or limits reads to the supplied evidence alone.
Claude read-only runs omit dedicated Write/Edit tools while retaining sandboxed Bash and evidence reads.
New result records use schema `0.3` and include the resolved `execution.permissions`; input configurations remain schema `0.2`.
Before scoring, compare that mode and the configuration identity against the frozen condition: subjects require `workspace-write`; an optional separately dispatched evaluator uses `read-only`. The active session retains its normal permissions to write score records and make authorized skill edits. A mismatch is an invalid setup, not a skill failure.
CLAUDE.md now explicitly accepts verified read-only permissions as an alternative to a no-write-tool agent type.

Provider-free checks against Codex **0.154.0** and Claude Code **2.1.269** passed: evidence reads and captured output, denied overwrites/deletion/renames/directory creation, denied Git mutations and outside-workspace writes, and denied symlink escapes.
Claude's private scratch allowance and Codex's existing writable Git behavior were also exercised.
The initial nested-sandbox attempts failed at host sandbox setup; rerunning the same local probes with host permission passed, without authentication or model calls.
Retained evidence, CLI identities and implementation source hashes are indexed in [permissions-qualification.json](permissions-qualification.json).
This establishes an optional evaluator permission mechanism, not a requirement to dispatch an evaluator. If a separate evaluator is later chosen, verify its actual setup and authorize its call then. Initial subject settings remain Sol low.

## Storage and accounting

Canonical project checkout: `/Users/simon/work/personal/disciplined-development-skills`.
Reserved primary: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/`.
Reserved backup: `/Users/simon/work/personal/skill-study-backups/sweeping-stale-references/`.
External raw development primary: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/`; backup: `/Users/simon/work/personal/skill-study-backups/sweeping-stale-references/development/`.
These locations are resolved from the canonical checkout. The development primary and backup now contain the permission-probe bundles and all four complete pilot bundles indexed above; reserved-case access isolation remains unqualified.
For any future explicitly selected held-out claim, an unexposed author receives only permitted copied evidence. The ordinary active-session workflow uses known cases and must not claim held-out validation.
For future runs, retain one complete bundle in the existing development primary, verify it against one inventory and index it before further dispatch; include unsuccessful attempts.
The owner accepted removing the mandatory second study-managed copy; that decision did not establish an operating backup arrangement.
Backup check, 2026-09-15: `tmutil destinationinfo` reports no destinations configured, while `tmutil isexcluded /Users/simon/work/personal/skill-study-private/` reports Included.
The owner-supplied Claude review also found no common backup agents running or iCloud coverage for this location; this session independently verified the Time Machine results, not every possible backup mechanism.
Treat raw evidence retention as single-host unless another arrangement is identified. Existing same-host copies do not establish host-loss recovery, and Git cannot recover external raw bundles.
Owner decision, 2026-09-15: after the backup check and explicit host-loss explanation, the owner accepted single-host retention for this study, including possible loss of external raw bundles if the machine is lost or fails.
No backup configuration is required by this accepted scope; verify local bundle preservation before further dispatch. This storage decision does not authorize model runs.
Keep historical primary/backup copies unchanged. The small run index references runner metadata and one canonical assessment rather than duplicating settings/status/timing; Git supplies repository-record history.

Keep one canonical repository record per accepted run and commit it before correction; Git retains earlier versions.
Historical citations use commit/path/hash, including the worked example's run-index reference; no duplicate snapshots or extensive amendment ledger are required.

**Current accounting (2026-09-16): 359 active minutes booked; 841 minutes (14 hours 1 minute) remain under the 1,200-minute ceiling.**
This includes preparation, review and model/tool waits, excludes owner-wait, and retains prior conservative allowances; the current booking includes final verification and commit/push allowance through 02:32 UTC.
All booked effort to date supports preparation/qualification; its older internal category split was not measured.
Update this paragraph in place from the latest booked total plus new active intervals counted once; Git retains prior checkpoints, and their source logs are optional reconciliation evidence.
Dispatched calls are **4 subject, 0 evaluator, 0 authoring, 0 retry**; remaining outer capacity is **36 / 12 / 4 / 4**, with no additional dispatch authorized.
