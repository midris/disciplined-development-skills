# Sweeping stale references: study protocol

Status: Stage 1 complete; Stage 2 conceptual coverage accepted and pilot case preparation active, 2026-09-12.
The owner selected `sweeping-stale-references`, authorized contract/allocation preparation and clarified that this skill should be evaluated independently.
The behavioral contract and outer ceilings are agreed; exact execution setup remains to be presented before provider dispatch.
Progress belongs to the [plan](../../plans/2026-09-11-model-driven-skill-testing.md); general requirements belong to the [spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md).
One executable pilot case and two provider configurations are prepared; no model observations or skill rewrites have been created.

## Sources and intended use

The original is [sweeping-stale-references](../../skills/sweeping-stale-references/SKILL.md) at repository revision `53a06ff4e2fcefb3c7706565bebe07d88e2782ea`, SHA-256 `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.
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
The owner considers `References swept:` important but does not require its omission to be a hard failure, and permits either procedural severity choice for this study.
Selected policy: assess each agreed criterion as met, not met or insufficient evidence, retaining the supporting evidence and consequence. Keep the two dimensions visible instead of combining them into a single score.
Incomplete or incorrect reconciliation, including damage to material that should be preserved, is a hard functional failure.
Purely procedural deviations are non-blocking defects for this study: report search-order, classification/accounting, commit-grouping and format failures explicitly without treating them alone as a failed functional outcome.
This severity policy does not make the original's explicit requirements optional or establish full compliance when they are missed.
Known output consumers: people and reviewing agents inspecting the reconciliation commit use `References swept:` as an audit account; the skill's Output artifact section explains the locations, outcomes and count reconciliation they need. DD Gate 4 and this project's commit guidance require that account.
Inspection of shipped skills, hooks, commands, examples and top-level tests found no named program consuming this format, and a targeted search of hook Python sources found no `References swept` parser. This bounds the inspection, not a claim about every consumer installation.
Missing or inconsistent accounting impairs auditability; no identified program requires exact syntax to perform the reconciliation itself. That supports the selected non-blocking accounting policy while retaining the original's explicit format checks.
Complete reconciliation with correct preservation but missing `References swept:` therefore meets the functional criteria and fails the accounting criterion; a well-formatted account cannot offset unresolved current references or incorrectly changed historical references.
Where a procedural deviation also causes a functional failure, record that consequence and apply the functional hard-failure rule.
A procedural regression remains relevant to the later adoption decision even when non-blocking; agree on the rewrite's acceptance boundaries before authoring rather than treating this policy as automatic adoption approval.
Apply the useful-outcome criteria to both conditions; target-specific compliance describes the original condition and must not penalize the unguided control for undisclosed instructions.
Count and location conventions must be fixed with the eventual checkers, including repeated searches of the same location, so duplicate search hits cannot inflate claimed coverage.
Missing action traces yield insufficient evidence for order/completeness claims, not an invented behavioral failure or pass.
Historical commits, PR descriptions and chat logs are not rewrite targets; vendor/archive files still require triage under the skill's stated distinctions.

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

| Facet | What to exercise | How to observe it |
|---|---|---|
| Broaden beyond the trigger | One cited defect has unstated siblings, including config, CI or fixtures. | Check required consumers in final state; inspect traces separately for search breadth and search-before-edit order. |
| Recognize equivalent references and changed facts | References use synonyms or describe changed code behavior without repeating its identifier. | Model judgment checks meaning against the settled fact and permitted alternatives; mechanical checks cover exact known values only. |
| Reconcile moved paths | Consumers use different relative paths, links or commands to a moved file. | Resolve each consumer's target and check it still works; assess prose context where needed. Relative-path handling is an owner-clarified outcome, not an explicit technique in the original. |
| Triage and preserve | Current consumers coexist with unrelated matches, history and vendor material. | Compare changed and preserved content; assess the correctness of each decision separately from whether its reason was recorded. |
| Complete reconciliation and commit it together | All required fixes must be complete, with no unrelated damage. | Check the final project and retained Git history. Functional completeness and the procedural single-commit requirement receive separate judgments. |
| Produce useful sweep accounting | The audit covers updates, false positives and intentional preservation, with correct locations/counts and grouping. | Mechanical checks cover syntax and count reconciliation; judgment checks whether the account and reasons match the evidence. Missing accounting is a non-blocking procedural defect under the settled policy. |
| Justify a genuinely local change | Checking scope finds no related updates. | Inspect the scope evidence and preserved project, then check the required negative-form line separately. A one-file task description alone is not justification. |

Facets may share cases; this does not require seven scenarios or seven initial runs.
Start process qualification with one non-reserved case exposing scope expansion, triage, reconciliation and accounting. Paths and semantic drift can be covered in later cases if the first would become overloaded; untested facets remain explicit gaps.
The initial real-model pilot asks whether inputs/skills are loaded as intended, tasks are feasible, traces and Git changes are retained, and separate functional/procedural judgments can be supported. It can expose case defects but does not establish coverage or stable skill effectiveness.

## Prepared two-run process pilot

The [pilot case](cases/pilot-01/assessment.md) adapts the earlier ssr-02 situation into real files and executable consumers; the [expected outcomes](cases/pilot-01/expected.json) and [local qualification record](cases/pilot-01/qualification.json) replace the old inventory/rubric.
The first pass covers scope expansion, preservation, complete reconciliation and accounting. Remaining facets stay unbuilt; the [plan's pilot-status table](../../plans/2026-09-11-model-driven-skill-testing.md#stage-3-qualify-and-freeze-execution) scopes partial completion.
Both configurations and all declared source files are identified in [manifest.json](cases/pilot-01/manifest.json). Configuration loading, prompt parity and byte-for-byte fixture preparation passed without provider invocation: 14 common inputs, plus only the target skill in the original condition.
Five constructed fixture variants demonstrate task feasibility and limitations of runtime-only checks; 70 synthetic files are hash-verified in the primary and backup paths recorded by the qualification record. These are local tool observations, not model performance.

Initial order is control, then original, one attempt each, using Codex `gpt-5.6-sol`, low effort, `workspace-write`, and the runner's 900-second per-call timeout. Installed Codex 0.154.0 and its executable hash match the prior permission qualification; no authentication or model availability check has been performed in this preparation.
No model evaluator is dispatched in this first pair: the orchestrator inspects pilot mechanics and developmental criteria directly. Independent model judgments and calibration remain unqualified for later measured collection.

Proposed exact commands, run from `/Users/simon/work/personal/disciplined-development-skills`; the namespaced temporary directory already exists:

```sh
TMPDIR=/private/tmp/ssr-process-pilot-20260912 skill-validation/runner/.venv/bin/python -m skilltest run skill-studies/sweeping-stale-references/cases/pilot-01/control.json
TMPDIR=/private/tmp/ssr-process-pilot-20260912 skill-validation/runner/.venv/bin/python -m skilltest run skill-studies/sweeping-stale-references/cases/pilot-01/original.json
```

Authorization status: awaiting approval of these exact configurations and commands under the [runner guide](../../skill-validation/runner/README.md#owner-authorization). Host permission allows the Codex app-server to initialize; the provider's workspace sandbox remains enabled. The external provider receives the declared synthetic project/task inputs and, in the original condition, SSR.
Before each dispatch verify the manifest and CLI identity; preserve each completed attempt's entire bundle with hash-verified primary and backup copies beneath the existing development stores at `pilot-01-runs/<run-id>/` before the next dispatch. Record source/destination paths and configuration identity in the run index.
Inspect the first bundle's contents and size and record retention policy before any evidence commit. No raw model trace is committed by this proposal.
Stop after the two attempts for process review; a setup failure, contamination, unreadable trace or preservation failure stops progression for diagnosis. No automatic retry, case mutation or additional model call is authorized by the outer ceiling.

## Authoring guidance and allocation

Initial process checks will use **Codex `gpt-5.6-sol`, low effort**, following the owner's request to use Sol low or Terra medium while establishing the process.
`gpt-5.6-terra`, medium effort, is the alternative if the pilot exposes a reason to switch; do not silently pool different models' observations.
The owner directed minimal real-model runs to establish the process before broader testing. Initially prepare two Sol-low subject invocations, one original and one no-target; use the pilot evidence to decide whether another run has a specific unresolved process purpose. The five-repetition wording campaign is a later conditional allocation, not part of initial process qualification.
Choose the measured baseline model after the pilot and keep it fixed across comparison conditions; exact commands and provider-run authorization remain Stage 3 work.

Installed Superpowers is version **6.3.0**, verified from its plugin manifest; the inspected `writing-skills`, `testing-skills-with-subagents.md` and required TDD background are hashed in the source inventory.
The guidance requires observed failure without the target before authoring, a change matched to the failure type, and five or more repetitions per variant for wording micro-tests.
It also calls for combined realistic pressures for discipline behavior and actual action rather than reciting the rule.
These inform Stage 2 design; illustrative multiple-choice prompts and historical performance claims in the guidance do not become this study's evidence or universal acceptance criteria.

The owner accepted outer ceilings of **40 subject / 12 evaluator / 4 authoring / 4 retry invocations** and **20 active hours**. The phase allocation below remains a planning envelope for at most one selected rewrite attempt, not authorization to run the whole campaign.
Case slots are arithmetic assumptions, not designed or approved tests: two development slots and one transfer slot, with overlapping properties allowed.

| Phase | Subject | Evaluator | Authoring | Retry | Allocation basis |
|---|---:|---:|---:|---:|---|
| Pilot and evaluator calibration | 2 | 2 | 0 | 0 | One non-reserved pilot slot in original/no-target conditions; two fresh calibration calls on constructed, independently checkable references. |
| Original baseline | 8 | 4 | 0 | 0 | Two development slots × two conditions × two repetitions; one evaluator batch per condition/repetition across distinct cases. |
| Rewrite and wording diagnostic | 15 | 0 | 4 | 0 | One development probe × original/no-target/candidate × five repetitions; authoring pool covers diagnosis, one candidate and inspection/selection, not four promised revisions. |
| Additional development capacity | 3 | 0 | 0 | 0 | Optional subject checks within the agreed development scope; not enough to qualify another five-repetition wording variant. |
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

Proposed time allocation: 4 hours for contract/test preparation, 3 for qualification/calibration, 3 for baseline, 5 for authoring/diagnostics, 4 for comparison and 1 for closure: **20 hours**, including review, storage work and model waits.
Planning assumption only: three minutes per invocation gives three hours of latency across the full 60-call ceiling; the runner's 900-second model timeout is not an expected duration.
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
Proposed external raw development primary: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/`; backup: `/Users/simon/work/personal/skill-study-backups/sweeping-stale-references/development/`.
These locations are resolved from the canonical checkout. The development primary and backup now contain the permission-probe bundles indexed above; reserved-case access isolation remains unqualified.
An author receives only permitted copied development evidence, not access to their reserved parent directories.
Apply the plan's copy/hash/backup barrier before each later dispatch, and inspect the first pilot bundle before deciding Git retention.
Both copies remain on this host; they do not protect against host loss.

Accounting began at the first recorded clock checkpoint, **2026-09-12 04:22:19 UTC**, with a conservative **two-minute allowance** for the opening read before that checkpoint.
This preparation consumes active study time toward the accepted ceiling; recorded owner-wait intervals are excluded.
Dispatched study invocations so far: **0 subject, 0 evaluator, 0 authoring, 0 retry**.
The orchestrator's preparation conversation and local tool calls consume active time, not provider-invocation slots; model assessments or authoring work must be accounted under their declared roles.

Owner walkthrough: the contract, outer limits and conceptual coverage are settled. Prepare the selected pilot case and concrete execution configurations.
Independent use is settled; Stage 3 must still qualify the exact standalone input setup and permissions.

Preparation accounting updated, 2026-09-12: **book 82 active minutes through pilot preparation**, leaving **18 hours 38 minutes** under the accepted 20-hour ceiling. This replaces, rather than adds to, earlier bookings.
Source: the current task's local log at `/Users/simon/.codex/sessions/2026/09/11/rollout-2026-09-11T17-59-42-01a0927b-cef5-7db0-8a30-c76c5b1ae838.jsonl`; only boundary timestamps were extracted, not conversation contents.
Reconstruction sums the union of `task_complete` and `turn_aborted` intervals since Stage 1 began: 38 closed intervals total **3,769 seconds (62.82 minutes)**, including local execution and model/tool waits inside turns while excluding inter-turn owner-wait.
The current turn began at 14:15:23 UTC and adds 876 seconds at the 14:29:59 checkpoint. Retain the original two-minute opening allowance, allow two minutes for completion, and round the resulting 81.42 minutes up to 82. The closing allowance and rounding are estimates; this is reconstructed orchestrator active time, not independently measured owner/Claude review effort.
At the next checkpoint, recompute cumulative closed-turn intervals plus the opening allowance and round up; do not add already counted turns or restore the superseded checkpoints. If the completed current turn exceeds the booking, correct the total before approving the remaining budget.

Relationship-correction verification: all **21** source identities match, including all nine DD skills at the recorded revision; local links resolve and `git diff --check` passes.
Hook suite: **263 passed, 3 skipped**. These documentation checks do not qualify provider execution or demonstrate skill effectiveness.
