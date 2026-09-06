# Controlled-Input Skill Testing: Pilot-First Design Amendment

**Status:** Live design discussion, not an approved implementation specification.
The owner accepted the scoped feasibility findings on 2026-09-06 and requested review of the next steps one at a time.
The owner selected the pilot-first scope below; broader methodology decisions remain constraints for later expansion, not prerequisites to design every future workflow now.
This draft does not change scoring rules or authorize runner implementation, provider calls, or effectiveness testing.
It is a reviewed decision record in progress, not an executable implementation contract; the exact invocation changes and unresolved decisions below still require approval.

## Overall goal

Rewrite the organically grown, mostly agent-authored and partly hand-tuned DD skills into a cleaner, lighter and more effective system.
Preserve charter-defined behavior while reducing unnecessary prose, repetition and procedural burden; shorter text alone is not evidence of improvement.

Follow **dumb tools for smart agents**: skills guide judgment, sequencing and decisions; targeted tools perform specific mechanical, repeatable operations deterministically; hooks surface checks at observable boundaries.
When exact parsing, rendering, validation or evidence recording is necessary, use a small mechanical tool rather than asking the model to reproduce deterministic work from prose.
Do not make hooks or deterministic checkers responsible for deciding whether the agent exercised sound semantic judgment.

Use a fixed, repeatable testing workflow to establish RED before authoring, verify GREEN, detect regressions and support simplification.
The earlier rewrite attempts lacked a sufficiently repeatable testing foundation; the mechanical runner and accepted current-skill observations now provide that foundation, with controlled-input integration still to design and implement.
The testing system is supporting infrastructure for evidence-led skill edits, not a separate goal or a reason to restart the charter and baseline work.
This section is the durable home of the overall goal; repository entry points link here instead of maintaining parallel explanations.

## Accepted immediate scope: one usable pilot

Build and exercise one small testing path before deciding the final testing organization; practical use should expose missing capabilities and unnecessary procedure.
The first path uses Codex / gpt-5.6-sol / low with a few representative scenarios, current-DD and no-DD conditions, fixed declared Superpowers and no DD hooks.
Select the exact scenarios, counts and order in the pilot runbook before execution; this provider/model/effort choice is not approval of a provider command.

The deliverables are one short provisional agent runbook, existing-format configs and fixture inputs, the necessary Codex invocation/setup/validation changes, and the CLI-version worksheet field with its 105-record historical backfill.
Reuse the existing directory layout, runner, worksheets and evidence bundles, with one plain Markdown pilot summary linking the conditions, attempts, judgments and deviations.
No campaign engine, new result or manifest schema, generic status framework, or per-catalog/per-scenario runbook hierarchy is required.
Use existing commands and recoverable source files for input preparation and provenance; add code only for a demonstrated required mechanical gap.

Qualify the selected discovery, composition, task-tool and evidence-write paths, then exercise preparation, execution, scoring and owner handoff end to end under exact-command approval.
Use the pilot to assess the procedure, not to claim skill effectiveness or full-suite coverage; do not label procedure success as skill GREEN.
Produce complete run records and scored worksheets to exercise the whole process; a judgeable skill FAIL can still demonstrate that the testing procedure works.
Start at low because this is process qualification and no need for higher effort has been demonstrated.
If a concrete workflow problem warrants a medium-effort diagnostic, record the reason, retain the low-effort attempt and obtain the required exact-command approval; do not automatically increase effort to obtain a passing skill result.
Keep medium diagnostics separately identified, not replacements for low observations or unchanged-command infrastructure retries.
Walk through interruption/failure handling and the later edit workflow using retained or synthetic evidence where useful, without authoring candidate DD skills or claiming RED/GREEN validation from a dry run.
Stop for owner review of the pilot and adjust the procedure before scaling.

Defer Claude runner integration, the Sol high/medium/low effectiveness matrix and possible Terra comparison, full controlled-baseline collection, campaign-wide sampling rules, detailed edit/regression runbooks and directory reorganization.
After owner acceptance of the process, freeze the agreed inputs and procedure and collect fresh effectiveness results; do not promote pilot observations into that campaign.
The accepted Claude feasibility evidence remains available for later work; it is not a dependency of this Codex pilot.
Retain the RED/GREEN, validity and evidence requirements below, but settle only the concrete choices needed for the pilot now.
This scope does not authorize implementation or provider calls; the exact Codex change map and a separate test-driven implementation plan still require approval.

## Accepted starting constraints

The [charter](../../skill-validation/charter/core-contracts.md#skill-contracts-and-proposed-core-portfolios) already defines each skill's intended behavior through named invariants.
Use those contracts and the existing audited scenario rubrics; do not redefine success as part of harness design.
The charter also specifies evaluation ledgers, judgment ownership and executed-work evidence requirements.
Its proposed suite changes and historical repetition schedule retain their stated activation conditions; this amendment does not silently activate them.

The goal is to compare current and candidate skill compositions under a recorded harness where the declared DD skill or skill-plus-tool changes are the only intended differences between those arms, apart from recorded incidental variation.
Known provider inputs may be common to both arms because the intended claim is conditional on that harness, not provider-independent effectiveness or universal filesystem isolation.
The [Codex finding](../2026-09-05-skilltest-provider-input-isolation.md#accepted-result-controlled-input-harness-is-feasible) and [Claude finding](../2026-09-06-skilltest-claude-controlled-inputs.md#accepted-scope-and-next-checkpoint) supply the evidence and provider-specific limits; spike scripts remain throwaway.

Preserve all 105 owner-accepted baseline observations without rescoring or replacing them.
The CLI-provenance decision below permits a metadata-only addition to their worksheets when the template is updated.
They establish historical methodology evidence, not an arm of a new controlled comparison.
Do not inspect or compare the unrelated rewritten-skills worktree.
Qualify the no-DD and current-DD environments, their declared Superpowers composition and representative scenario tools before controlled baseline collection; the synthetic spikes did not establish those production conditions.
Qualify the candidate's actual inputs and any changed discovery/tool requirements before its comparison runs, after RED and candidate authoring; do not require a rewrite as a prerequisite for collecting RED.
Harness qualification may use synthetic A/B variants to test switching and loading, but those variants are not skill candidates or effectiveness observations.
The runner remains responsible for mechanical evidence; the orchestrator owns semantic/protocol judgment and the owner retains acceptance authority.

## RED/GREEN authoring requirement

The owner uses `superpowers:writing-skills` and requires repeatable testing before skill creation or edits, independently of that superpower's mandate.
The methodology must support its RED-GREEN-REFACTOR workflow: observe the targeted failure before authoring, test the candidate against the same scenario and criteria, then rerun relevant tests while simplifying or correcting the skill.
Freeze each comparison's scenario, rubric and surrounding conditions; an intentional test-contract change requires fresh comparable observations rather than moving the criteria to make the candidate pass.

The installed writing-skills superpower requires a no-skill baseline and, for behavior-shaping wording micro-tests, a no-guidance control with at least five repetitions per variant and manual review of flagged matches.
It treats those micro-tests as supplementary to full pressure scenarios, not a replacement.
These are authoring requirements, not authorization to invoke providers or a complete effectiveness-campaign sampling policy.

Distinguish the no-DD control defined below, current DD composition and candidate DD composition.
The control tests the need for DD guidance on top of Superpowers; current-versus-candidate comparisons assess improvements and regressions.
The 105 accepted current-skill observations are not no-skill RED controls and must not be relabeled as such.
Reconcile repetition and acceptance rules before the later effectiveness campaign, not as a prerequisite to this procedure pilot; do not invent replacement behavioral criteria.
Fixed execution and scoring procedures do not make model behavior deterministic.

## Accepted methodology decision: RED control

The owner selected a control that excludes all DD skills while retaining Superpowers.
DD skills are intended to compose with one another and with Superpowers, so removing only the target DD skill is not the standard RED control.
Removing Superpowers as well would answer a different question about the combined stack and is not required by this design.
Keep the declared Superpowers version and configuration fixed across control, current and candidate conditions.
Current and candidate conditions supply the intended DD composition, not an isolated skill stripped of its dependencies.
The comparison measures DD's contribution on that substrate, not its independent effect outside it.
An observed, judgeable failure establishes RED; merely running without DD does not guarantee RED.
Assess charter behavior, not the expected absence of a DD file or command.
Some existing prompts explicitly require reading a DD skill, such as [DR-02](../../skill-validation/scenarios/disciplined-research/dr-02/prompt.md); deleting that fixture alone would leave a broken instruction, not a valid control.
Prepare fresh comparison inputs with a common task and rubric and explicitly declared condition-specific skill-loading instructions, where needed; audit them before freezing or collecting runs.
This does not authorize editing the accepted scenario packages or rewriting their historical results.

## Accepted baseline decision: current DD and no-DD, with CLI provenance

Fresh controlled baseline collection includes both the current-DD composition and the no-DD control, recorded and reported separately.
Retain the no-DD observations for later comparisons even when they pass; they become RED evidence only when they demonstrate a judgeable targeted failure.
Both conditions retain the declared Superpowers substrate and exclude DD hooks as specified here; the pilot starts with Codex / gpt-5.6-sol / low, while its scenarios and repetition counts still require agreement.

Record the actual subject-provider CLI version alongside provider, model and effort for every baseline observation and subsequent edit-test observation.
Its durable scoring home is the completed worksheet: add a blank `Provider CLI version` field to the run-identity table for the orchestrator to fill while scoring.
Capture version evidence from the same executable immediately before each run, including repetitions and retries, and link it to that run ID; a batch-start check, expected dependency pin or later lookup is not per-run provenance.
The orchestrator fills the new field with the captured version and a reference to its retained evidence in the same value cell; ordinary version evidence does not belong in the worksheet's ambiguity, defect or proposed-change fields.
Worksheet generation remains offline and leaves the field blank; it must not query the then-installed CLI and present it as the version used earlier.
If version evidence is missing, unusable or contradicted by detected drift, state that uncertainty in the field rather than guessing and apply the failure/drift policy below; this is not an automatic skill FAIL.
Record detected CLI changes rather than silently treating different versions as the same harness; a pre-run version check is diagnostic provenance, not proof against an update during execution.
This provenance helps investigate changed results with unchanged skills; a version difference is diagnostic context, not proof of the cause.
Use version commands for capture and the existing worksheet generator for the added blank field; this is a targeted template addition, not a new metadata framework or result-schema change.
The current worksheet template does not contain this field; implement and document it with a focused test in the separately approved implementation work, rather than hand-changing the fixed worksheet structure or mechanical result files now.
When adding the template field, audit all 105 accepted baseline runs and add CLI-version provenance to their existing worksheets so later harness comparisons can also use the historical observations.
This is a metadata-only exception to baseline preservation: leave verdicts, assessments, run identities, result.json, final.txt and judged evidence unchanged; do not regenerate completed worksheets or rerun baselines.
Use contemporaneous evidence tied to the accepted run, retaining a credential-free evidence reference in the new field; do not substitute the currently installed version, an expected pin or a later spike's version.
Where the historical version cannot be established, record `Unknown` with the evidence limitation rather than guessing.
Check relevant scratch evidence before cleanup and preserve any version evidence needed to support the backfill; the new metadata does not make historical runs qualified controlled-comparison arms.

## Accepted methodology decision: skills without DD hooks

Exclude DD hooks from every subject-run condition: no-DD control, current DD composition and candidate DD composition.
The skills must stand on their own without hook reminders or enforcement, while retaining their intended composition with Superpowers.
Hooks are deliberately dumb support for smart models: reminders and nudges, with a few configurable hard blocks for explicitly enforced disciplines.
Their intended additional value under long-session or heavy-workload pressure is a separate evaluation question, not evidence of unaided skill effectiveness.
This exclusion concerns the tested agent's harness, not changes to the owner's installed hooks or running sessions.
Independently callable mechanical tools are not excluded by this hook decision; their comparison boundary is defined below.

The owner has a separate, deferred goal to rework the Claude-only hook system: reassess available Claude lifecycle events and extend support to other systems, including ChatGPT/Codex where supported.
Platform capabilities and suitable integration points must be verified in that work; this records intent, not a claim that equivalent hook APIs exist.
Hook redesign, portability work and hook-effectiveness testing are outside the skill-writing scope and are not prerequisites for it.

## Accepted methodology decision: model-led testing with simple tools

The testing workflow is model-driven, using the existing reusable deterministic testing tools to scaffold runs and record results.
The orchestrating model selects or prepares scenarios against the charter, audits the declared conditions, invokes tools within the owner's permissions, reads raw evidence, applies the existing rubrics and records judgments.
The tools perform mechanical preparation, execution, hashing, evidence capture and worksheet rendering; they do not choose behavioral criteria or assign semantic verdicts.
Use the existing runner and worksheet workflow first; add or extend a small deterministic tool only for a demonstrated mechanical gap, not to build a separate autonomous testing framework.
The owner retains acceptance authority, and provider-call approval requirements remain unchanged.

Distinguish the orchestrator's testing tools from tools available to the model under test.
Keep ordinary subject task tools fixed across comparison conditions.
If a DD edit adds or changes a dedicated subject tool, declare and evaluate it as a skill-plus-tool change, not a wording-only improvement.
Supply only declared scenario inputs to the subject and keep the rubric and evaluation guidance out of its prompt, supplied files and discovery sources.
Recorded common provider inputs remain subject to the accepted observability limits; withholding the rubric is not a claim of universal filesystem inaccessibility.
Model-led orchestration does not make model behavior or semantic judgment deterministic.

## Accepted workflow direction: agent runbooks, not programs

The testing deliverable is a written test script or runbook for an orchestrating agent to follow, not a shell script, Python program or new execution engine.
Start with the one provisional pilot runbook; expand it into baseline and skill-edit procedures, including RED/GREEN and regression testing, only after practical feedback.
Distinguish fresh controlled observations from the preserved historical baselines and the no-DD RED control.
Before use, a runbook and its explicitly linked inputs must together identify the scenario/config and rubric, fixture sources and target layout, skill/dependency versions, exact setup and run commands with working directories, provider/model/effort and CLI-version capture, repetition counts and ordering, validation checks, evidence/worksheet locations, failure/retry handling and approval checkpoints.
Resolve these choices before collection; an agent must not invent missing counts or change the model or conditions mid-run.
The runbook belongs to the orchestrator, not in the subject's prompt or fixtures.

Routine testing work changes runbooks, prompts and fixture/config inputs, not runner code.
Change code only when a concrete required mechanical capability is missing; the controlled-input invocation gaps already identified below still need to be addressed and qualified.
Once those capabilities exist, the work is executing the approved procedure and checking evidence that the orchestrator followed it, not building a program to replace model judgment.
Required mechanical setup validation remains the runner's responsibility; documenting a check does not replace implementing a missing control.

### Accepted sequencing: requirements before directory layout

Use the content inventory below to cover the pilot in one runbook; it is not a requirement to finish campaign-wide procedures before trying it.
The owner is open to a full reorganization of `skill-validation/` once that inventory is understood; the existing directory structure is not a design constraint.
This is permission to consider a new layout, not to move files now or modify preserved baseline evidence.
Shared procedures with catalog/scenario details remain one possible organization, not an accepted hierarchy.
Keep the existing layout for the pilot and revisit organization after practical use clarifies responsibilities and reuse.
Any later migration must explicitly preserve historical identities, evidence bytes, provenance and working references; approval of that migration is separate from approval of test-content changes.

### Working requirements inventory

This is the content checklist for one provisional runbook, not a list of new files or an approved execution schedule.
The [scenario index](../../skill-validation/scenarios/README.md), catalog summaries, [runner guide](../../skill-validation/runner/README.md) and [methodology](../completed/specs/2026-09-02-skill-testing-methodology-design.md) supply the existing material.

| Required content | Reuse | Work still to specify or assemble |
|---|---|---|
| Purpose and authority | Charter, catalog summaries, scenario rubrics and validation entry points | Name the selected scenarios and paths they exercise; distinguish procedure qualification, action-selection evidence and executed-work claims. Link governing criteria instead of duplicating them. |
| Inputs and setup | Existing configs/fixtures, Codex spike findings and fixture-root decision | Freeze and check valid no-DD/current inputs, Superpowers and ordinary tools; exclude DD hooks and evaluator guidance. Document the selected CLI version, safe authentication, required checks and cleanup. |
| Execution | One-run CLI, scratch bundles and worksheet command | Give exact working directories, setup/run/version-capture commands, counts, order and approval checkpoints for Codex / gpt-5.6-sol / low; apply the accepted stop/retry rules. |
| Judgment | Existing rubrics, blank worksheets and separate ledgers | Score all judgeable observations, fill CLI provenance and report conditions separately; disclose ambiguity and invalid attempts. No new pooled score, effectiveness estimate or skill-acceptance threshold. |
| Evidence and handoff | Existing bundles, worksheets, frozen sources and one Markdown summary | Link every planned/completed condition and repetition, evidence and deviations; identify where to resume, what needs owner review and what must survive cleanup. Keep credentials out. |

The existing methodology's single replaceable `accepted/` record cannot by itself represent a repeated multi-condition comparison.
Resolve that lifecycle explicitly while preserving the 105 historical records; a written execution record linking existing bundles and worksheets may suffice, without a database, new manifest schema or campaign engine.
The owner requires bounded retained history: keep the evidence needed to support current accepted conclusions, not an accumulating archive of every experiment, candidate revision or superseded comparison.
Bound history by retiring whole superseded sets under an agreed replacement/cleanup policy, not by retaining only favorable repetitions within a reported comparison.
The owner selected Git history for superseded accepted test results: keep the current accepted baseline/control and comparison evidence in the working tree, replacing superseded sets rather than accumulating dated archives.
The accepted replacement unit is a complete scenario test set for one scenario and provider/model/effort combination: all declared conditions and repetitions, including failures, with their worksheets, supporting evidence and a short summary.
CLI versions remain recorded provenance, not an additional permanent archive dimension.
Replace the whole set after owner acceptance and commit the replacement together; this retention unit does not require rerunning every condition for every edit or authorize combining observations that fail the agreed comparability checks.
Commit an accepted evidence set and its recoverable input provenance before a later accepted set replaces it; Git cannot recover evidence that was never committed.
Active experiments remain scratch-only pending review, and rejected/intermediate experiments need not be committed merely to create history.
This bounds checked-out history, not Git storage; do not rewrite Git history to prune evidence.
Retain experiment scratch through owner review; before cleanup, commit and verify any evidence selected for acceptance and its recoverable input provenance.
Rejected or explicitly abandoned experiments need no artificial accepted result or evidence commit; resolve any shared evidence needed by retained results or the historical CLI backfill before their cleanup.
Keep interrupted or unresolved experiments until explicitly resumed or abandoned.
This cleanup policy does not authorize committing or deleting anything now or changing the protected historical baseline records.
Procedure conformance is checked against actual commands, inputs and evidence, not an agent's claim that it followed the runbook.

Frozen-input evidence must identify recoverable versions of the prompt, rubric, config, supplied skills and supporting files before collection, not merely their current paths or hashes observed afterward.
The current runner inventories fixture contents at finalization, and worksheet generation hashes the rubric at that later invocation; neither establishes a pre-launch snapshot on its own.
Specify how prepared inputs are checked against frozen sources and how worksheet generation uses the matching frozen rubric.
For executed-work scenarios, distinguish protected guidance/test inputs from task files the subject is expected to edit; retain the initial state and judged outputs rather than treating every fixture edit as contamination.
The smallest preparation/check mechanism remains to be designed using existing tools first; this requirement does not approve another schema or a general snapshot system, nor does it reopen historical observations.

Review the pilot's preparation/qualification, no-DD/current collection, scoring, interruption/failure recovery and handoff; a paper walkthrough of a later edit may expose gaps without requiring a complete edit runbook now.
Choose exact pilot scenarios, counts and commands before execution; campaign schedules and directory moves remain deferred.

### Accepted failure and drift policy

If a required isolation check fails or cannot be completed before launch, stop without invoking the provider.
If contamination is discovered afterward, retain and explain the attempt under the scratch-review policy, but exclude it from valid comparison evidence without automatically assigning a skill FAIL.
If the CLI version changes during a comparison, pause that comparison, validate the changed harness and establish matching versions and conditions before continuing; do not automatically rerun the whole baseline suite.
For new controlled runs, unavailable or unusable version evidence also prevents establishing that match: pause and retain the affected attempt outside valid comparison evidence until resolved.
Matching versions reduce harness confounding but do not themselves prove comparable inputs.
Keep the existing `INFRA_RETRY` procedure for ordinary infrastructure failures; a changed harness is not an unchanged-command infrastructure retry.
Identify affected attempts and reasons in the comparison summary so exclusions remain visible after scratch cleanup.
Express this policy in the runbook and existing evidence records, without adding a status framework or rewriting mechanical result fields.

## Accepted design boundary: config-driven environment and isolation validation

The runner configuration declares the test inputs and provider selection; the selected provider adapter supplies the required controlled-input invocation defaults.
Use those existing mechanisms to establish the intended skill composition and environment before introducing new config fields.
The runner establishes the environment through its provider adapters; required mechanical checks and retained evidence validate the setup rather than leaving it to per-run improvisation.
Check controls available before launch before invoking the provider; retain the required observable runtime evidence for orchestrator review.
Validate only the agreed, observable controls: neither valid config syntax nor absence of a visible violation proves all hidden provider inputs are absent.
Distinguish environment setup from subject behavior: a missing declared skill is a setup defect; a model choosing not to use an available skill is evaluated under the existing rubric, not automatically excluded as an isolation failure.
A qualification probe may require exact skill reads to prove wiring, but that probe requirement must not silently become an exclusion rule for effectiveness runs.
An unproved required control cannot be treated as a validated comparison environment; apply the accepted failure and drift policy above.

Isolation retains the accepted controlled-input scope and provider observability limits; this does not reopen universal filesystem isolation as a requirement.
The current runner config declares prompt, fixtures, provider, model and effort, while provider environment controls are fixed adapter behavior.
The missing capability is the appropriate controlled-input provider invocation and its validation, not necessarily a larger configuration schema.
The current runner does not implement the accepted spike controls; those controls remain to be integrated and qualified.

### Accepted placement decision: fixture directory as project root

For the Codex pilot, use the existing `workspace/fixture/` directory as the subject's working/project root.
Declare native skills through existing fixture targets at `.agents/skills/<skill>/SKILL.md`, with required supporting files supplied alongside them.
The accepted analogous Claude target is `.claude/skills/<skill>/SKILL.md`, but its working-directory and discovery changes belong to deferred Claude integration; preserve the current Claude path in this pilot.
Keep `workspace/evidence/` as the evidence destination and explicitly grant required write access; preserve fixture hashing and the existing prompt path placeholders.
This reuses fixture copying and config declarations instead of adding destination fields, another skill installation step or links to host skills.
It deliberately changes the current provider working-directory contract; update and qualify relative-path behavior, native discovery/loading and evidence writes together before use.
No config-schema change is required for this placement decision, and it does not by itself establish the other controlled-input requirements.

## Immediate code scope: minimum provider invocation change

The owner requires the absolute minimum code change needed to invoke the CLIs with the proper options for the agreed test environment.
Start in the existing Codex provider adapter, not with a runner redesign: extend argument construction and child-process environment handling only as required by the accepted Codex evidence.
Leave Claude invocation behavior unchanged in this pilot; any shared refactor must preserve it and its tests.
Preserve the one-config, one-prompt, one-run workflow and model-led test orchestration.

- Reuse the current config schema, fixture copying, workspace allocation, output capture and worksheet interface wherever they satisfy the requirement.
- Keep invariant CLI options as fixed adapter defaults; do not expose arbitrary CLI arguments, environment maps or a generic isolation-policy language merely to pass known options.
- Add a config field only for a necessary per-test choice that the existing declarations cannot express; identify that concrete gap before proposing the field.
- Add profile files, runtime setup/cleanup or a child filesystem policy only where a required control cannot be established with CLI options and environment handling alone. Tie each addition to the provider evidence; do not import the scratch spike harness wholesale.
- Retain only the validation checks and credential-free evidence needed to establish the required controls, using existing test and artifact mechanisms where possible. No general validation framework, campaign engine, automatic scorer or new retry machinery is in scope.

The owner's CLI-provenance requirement additionally needs one blank run-identity field in the existing worksheet template, with its focused test and contract documentation updated together.
The orchestrator fills it from captured version evidence; automatic CLI-version collection and result-schema changes are not required by that addition.

Native skill discovery remains in scope; disabling all skills or replacing discovery with pasted skill text would change the tested mechanism and requires a separate decision.
The evidence identifies these gaps to resolve in the minimal change map:

| Gap | Existing evidence and constraint |
|---|---|
| Codex profile/auth setup | The accepted spike used private HOME/CODEX_HOME and a private auth cache as well as CLI flags; it did not prove flags alone sufficient. |
| Native skill placement | Use the fixture directory as the provider project root, as agreed above; changing the working directory and qualifying discovery plus sibling evidence writes remain implementation work. |
| Frozen-input provenance | `runner.py` finalizes fixture hashes after provider execution; `worksheet.py` hashes the currently supplied rubric. Specify frozen source preparation and validation without representing these records as pre-launch evidence. |

These are evidenced integration questions, not authorization to add a profile framework or copy entire host configurations.
Any necessary auth setup must keep secrets out of arguments, logs and retained evidence, remove temporary credential copies, and never log out shared accounts or alter running sessions.

Before implementation, map each required control to its exact provider option or environment setting, the existing code location to change, and the focused verification that proves it.
For any control needing more than invocation changes, state the smallest necessary addition and obtain approval for that scope before coding.
Provider-free tests must check exact invocation construction and relevant environment behavior; assertions about passed flags alone do not prove CLI enforcement.
Use the qualified spike evidence and separately approved real-provider qualification to verify effective discovery/loading, with only the necessary per-run checks retained in production.
Do not drop a required control to make the diff smaller or claim full isolation from a flag-only test.

This scope keeps testing infrastructure subordinate to skill development while preserving the accepted controlled-input claim.
It does not authorize implementation or provider calls; the exact minimal change set still requires design approval and a separate test-driven plan.

### Proposed Codex change map — pending owner agreement

The [durable Codex result](../2026-09-05-skilltest-provider-input-isolation.md#accepted-result-controlled-input-harness-is-feasible) and scratch `commands/provider-command.sh`, `auth-check.py` and `run-approved-integration.py` under `/private/tmp/skilltest-controlled-inputs.MTAyGQ/` supply the starting evidence.
Provider-free inspection on 2026-09-06 found `/opt/homebrew/bin/codex --version` reports `0.153.4`; its `exec --help` documents `--ignore-user-config`, `--ignore-rules` and `--add-dir` for additional writable directories.
Help establishes available options, not enforcement; the writable pilot combination still requires qualification.

| Surface | Proposed minimum change | Required verification |
|---|---|---|
| Codex argv/cwd in `providers.py` | Run from `workspace/fixture/`; retain model/effort, ephemeral JSONL, final output and `workspace-write`. Add `--add-dir` for `workspace/evidence/`, `--ignore-user-config`, `--ignore-rules`, and fixed config overrides for `shell_environment_policy.inherit="none"`, `cli_auth_credentials_store="file"` and `approval_policy="never"`. | Exact argv/cwd test; real qualification of native loading, relative reads and sibling evidence writes without interactive approval or broader sandbox bypass. |
| Private runtime around the Codex invocation | A small Codex-specific helper creates fresh private HOME/CODEX_HOME/TMPDIR outside the retained bundle; launch with only those values and an explicit operational PATH. Resolve the CLI executable before replacing the environment, then use that same executable for preflight and invocation. | Fake-provider tests show private directories, no inherited semantic settings/API-key variables, and fresh state on consecutive runs. Log the actual resolved argv, not a pre-setup approximation. |
| Authentication and cleanup | Copy only the existing file-backed `auth.json` from the invoking Codex profile into private CODEX_HOME with mode 0600 and private parent directories; check private login status without retaining credential-bearing output. No new login, keychain extraction, host-profile copy or shared-account logout. Remove the private runtime on success, launch failure, nonzero exit, timeout and handled interruption. | Dummy credentials only in automated tests; unavailable/invalid auth stops before the model call, partial setup is cleaned up, and cleanup failure is surfaced without masking an earlier failure. Never report successful cleanup without verifying it. |
| Fixture preparation and mechanical checks | Preserve the spike's fresh project boundary with an empty, template-free Git repository in the fixture root. Before initialization, reject a declared or existing `.git` file/tree instead of overwriting it. Check prepared prompt/fixture bytes against the declared sources and ensure the private profile contains no copied settings/instructions. Keep auth outside fixture/evidence inventories. | Provider-free tests reject setup mismatches before invocation. Separately qualify native discovery and stable common inputs using the same runtime setup; do not build a general catalog parser or claim file copying proves discovery. |
| Existing run orchestration and worksheet | Make only the necessary `runner.py` integration for preparation failure, actual invocation logging and cleanup reporting. Add the blank CLI-version worksheet field and targeted test; retain the existing result shape, output capture and manual scoring. | Preserve Claude argv/env/cwd; test new lifecycle failure reporting and verify that the historical backfill changes only authorized metadata and adds no inferred versions. |

Runtime preparation and cleanup belong to the runner because every run needs them; the runbook should not reproduce the spike's Python wrappers or provision secret files by hand for each invocation.
Use the existing invoking-profile location (CODEX_HOME, otherwise the normal `.codex` directory) only to locate the credential source, never to inherit its instructions or settings.
Support the demonstrated file-cache path first; unavailable credentials are a setup blocker, not a reason to add another authentication backend.
Bound each setup subprocess, including Git initialization and private login-status checks, to 30 seconds; keep the existing 900-second model timeout and five-second termination grace.
For Codex, start owned subprocesses in a separate process group; on timeout or handled interruption, terminate/escalate that group and reap the direct child before deleting its runtime. Never signal unrelated host sessions.
On normal return, stop any remaining owned group members before runtime cleanup as well.
Do not promise cleanup of processes that deliberately escape the owned group or survive an uncatchable runner kill; log the exact private-runtime path without contents for manual recovery, and keep such attempts outside qualified pilot evidence until resolved.
The current infrastructure-code enum lacks a runtime-cleanup failure: add only `PROVIDER_CLEANUP_FAILED` to the existing result contract, not a new schema version or status framework.
If cleanup fails after an otherwise successful call, return a nonzero runner outcome with that infrastructure error while preserving the provider's actual exit and captured output; if an earlier error exists, keep it primary and record cleanup failure additionally in the runner log.
Do not treat a retained evaluable response with a cleanup failure as an automatically retryable infrastructure-only attempt.
The runbook owns frozen source preparation, per-run CLI-version evidence, declared common-input qualification, complete worksheet scoring and the pilot summary; the runner owns the bounded pre-launch mechanical checks listed above.
Qualify catalogs and observed bootstrap/common inputs once for the pinned pilot harness and repeat qualification on relevant CLI, input, setup or tool changes; review each run's observable trace for violations. This separates effective-control validation from per-run setup checks without asserting hidden inputs are absent.
Keep shell-startup/common-input limits explicit during qualification: neither `inherit="none"` nor a private profile alone proves absence of automatic shell reads.
Use the resolved executable's directory followed by `/usr/bin:/bin:/usr/sbin:/sbin` as the explicit pilot PATH, with no inherited extra entries; qualify the selected task tools under it.
Pin recovery commands and qualification calls in the runbook before execution; this mapping approves no code, new config schema or provider call.

## Review sequence

1. **Finish the pilot design.** Select a few scenarios that exercise the required paths, their exact counts/order and frozen-input preparation; map the Codex controls to the smallest argv/env/setup changes and focused checks. Do not settle the full campaign or final directory layout.
2. **Approve the [draft test-driven implementation plan](../2026-09-06-skilltest-sol-low-pilot.md).** It covers the Codex changes, worksheet field and historical backfill, and one provisional runbook with existing-format inputs. Keep tests tied to the selected contracts.
3. **Implement and qualify — not yet authorized.** Run provider-free tests first, then representative real qualification under exact-command approval. Validate before collecting the pilot's no-DD/current observations.
4. **Exercise the runbook and stop for owner review.** Report setup, execution, scoring and handoff results, validity limitations and practical procedure changes in one Markdown summary; do not proceed automatically to a full baseline campaign or skill edits.
5. **Expand only after pilot feedback.** Separately approve detailed baseline/edit procedures, campaign metrics and sampling, additional providers/models or layout changes when needed.

Rewritten-skill comparisons remain deferred until the harness and methodology are owner-accepted.
This order prevents a feasible scratch mechanism from becoming a production contract before its evidence and scoring consequences are agreed.

## Pilot decisions still pending

Settle only the selected scenarios and their fixed inputs, exact counts/order, Codex invocation/auth/access delta and checks, and the runbook's concrete command/evidence paths before execution.
Use existing charter criteria and worksheet judgments; do not ask the owner to restate skill purpose or success criteria.
Broad sampling, detailed edit/regression coverage, Claude integration and reorganization are explicitly deferred, not missing pilot requirements.

### Proposed scenario set and run count — pending owner agreement

Use two fresh pilot variants, not replacements for their source packages or accepted results:

| Source | Pilot coverage | Required adaptation |
|---|---|---|
| [DR-02](../../skill-validation/scenarios/disciplined-research/dr-02/README.md) | Native research-skill loading, reads of three local sources, judgment from controlling evidence, and sibling evidence-directory writes | Keep the procurement task and semantic rubric; explicitly request saving the same two-line answer returned in the final response to `{{evidence_dir}}/deadline-note.md`. Replace the blanket read-only restriction in both conditions with permission to write only that file. Record the saved artifact as task fidelity, not a new skill-behavior criterion. |
| [LP-01](../../skill-validation/scenarios/lean-plan-writing/lp-01/README.md) | DD/Superpowers composition and plan-artifact scoring | Retain the JSON-report task, rubric and supplied writing-plans guidance; adapt native fixture paths and condition-specific loading instructions while keeping the response-only task boundary. |

For both variants, supply all nine current DD skills in the current-DD condition and none in no-DD; hold the explicitly inventoried Superpowers inputs and ordinary task tools fixed.
No-DD prompts must not request absent DD skills; LP-01 still invokes the supplied writing-plans guidance in both conditions.
Freeze and audit the common task/rubric and declared loading differences before collection; any adaptation creates new pilot provenance, not a historical-baseline rerun.
Do not add a separate description-routing scenario: [DISC-07](../../skill-validation/scenarios/skill-discovery/disc-07/README.md), for example, forbids file reads and supplies descriptions inline, so it would not prove native CLI discovery.
Native discovery, actual loading, composition inputs and write access still require explicit qualification; a subject choosing not to use a successfully qualified capability is scored as behavior/task fidelity, not automatically an environment failure.

Propose two repetitions per condition per scenario: eight planned scenario runs, all Codex / gpt-5.6-sol / low, with a fresh runtime each time.
Run DR-02 first, then LP-01; within each, use no-DD, current-DD, current-DD, no-DD order.
This exercises repeat setup and both order positions without claiming a useful effectiveness estimate or satisfying later skill-authoring repetition requirements.
Keep all planned judgeable results, including failures; do not add repetitions to obtain a preferred verdict.
Required pre-collection qualification calls and permitted infrastructure retries are separately counted, not included in the eight; fix qualification commands/counts with the Codex change map before requesting execution approval.

## Existing authorities to reconcile after decisions

- [Methodology](../completed/specs/2026-09-02-skill-testing-methodology-design.md): ledger/verdict separation and evidence lifecycle.
- [Core contracts](../../skill-validation/charter/core-contracts.md): invariants, orchestrator responsibility and conditional historical comparison schedule.
- [Runner contract](../../skill-validation/runner/README.md): invocation, evidence collection and infrastructure-only retry handling.

Older deferred or conditional campaign designs are context, not automatic authorization for the new comparison campaign.
