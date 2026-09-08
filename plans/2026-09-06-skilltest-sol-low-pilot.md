# Controlled-Input Sol-Low Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task by task, stopping at the review checkpoints below.

**Status:** Task 9's CW collection and review handoff are complete; owner acceptance of this batch and the earlier pilot/extension remains pending.
The initial four observations and six separately approved extension observations are scored and retained in scratch, without provider retries or unresolved cleanup.
No-DD/current-DD real qualification and the extension's affected provider-free qualification are complete; the documented reuse decision required no additional paid qualification call.
Stop for owner review: no further provider invocation, fixture revision/recollection, effectiveness campaign, discovery coverage work or skill edit is authorized by these completed calls.
The extension evidence pointers are in Task 6; Tasks 8–9 record the separately approved CW inputs and completed four-command procedure batch.

**Integration handoff:** The owner authorized merging this branch into main, removing completed local/remote branches and the completed worktree, then creating `feature/cw-validation-design` in `.worktrees/cw-validation-design`.
That next workspace is for minimal CW test-set design; this does not promote scratch observations into accepted baselines or authorize new provider calls.
Retain scratch evidence outside the removed worktree; recorded commands and frozen revisions remain historical provenance.
The [CW design and review checkpoint](specs/2026-09-07-cw-validation-design.md) now tracks the owner-approved CW-08/CW-19 behavior portfolio, retained discovery pair and draft baseline/edit runbook.
That scoped documentation/input preparation supersedes this pilot's stop boundary only for the new unit; prior results and provider approvals remain unchanged.

**Goal:** Exercise one agent-led preparation, execution, scoring and handoff workflow, not collect effectiveness estimates.
**Architecture:** Preserve the one-run runner and config schema; add only Codex runtime controls and a worksheet field, then exercise them through one written runbook.
**Tech stack:** Existing Python runner, pytest, Git and the locally qualified Codex CLI on macOS.
**Spec:** [Pilot-first design amendment](specs/2026-09-06-skilltest-controlled-inputs-design.md).

## Global constraints

- Pilot execution used `.worktrees/skilltest-input-isolation-spike` on `spike/skilltest-input-isolation`; the integration handoff above supersedes that workspace requirement. Preserve the unrelated rewrite worktree.
- Start with Codex / gpt-5.6-sol / low. Medium is a justified, separately identified diagnostic under exact-command approval, not an automatic retry.
- Current-DD supplies all nine DD skills; no-DD supplies none. Freeze the same declared Superpowers and ordinary tools across both, with no DD hooks.
- Do not edit skills or source scenario packages, rescore accepted baselines, or replace their result/final/evidence files. The sole historical exception is the CLI-version worksheet metadata backfill. Task 4 separately authorizes a future-input clarification to the two LP-01 pilot prompts, without changing completed observations.
- Keep the existing config schema and result shape. The only proposed error-enum addition is `PROVIDER_CLEANUP_FAILED`; preserve Claude invocation behavior.
- No generic inventory/status framework, campaign engine, automatic scorer, hooks work, directory migration, candidate skill authoring or effectiveness campaign.
- Never print or retain credentials. Keep private runtime outside retained bundles, and never modify shared authentication or host sessions.
- Deliver independently green commits; integration and completed-branch cleanup are now owner-authorized as recorded above. No PR or unrelated rewrite work is included.

## Task 1: Worksheet field and historical provenance

**Files:** `skill-validation/runner/src/skilltest/worksheet.py`, `skill-validation/runner/tests/test_worksheet.py`, the CLI worksheet expectation in `skill-validation/runner/tests/process_smoke/test_cli.py`, `skill-validation/runner/README.md`, the worksheet contract in `plans/completed/specs/2026-09-02-skill-testing-methodology-design.md`, and the 105 existing `accepted/worksheet.md` files.
Retain only credential-free historical version evidence needed by the new references; do not copy whole scratch bundles.
Keep the 105 metadata-only worksheet changes atomic with the template contract; the required per-file reference inventory therefore exceeds the usual commit-body length preference.

- [x] Add an exact-template test requiring a blank `Provider CLI version` row after `Provider`, with no CLI lookup during worksheet generation; run it and observe failure.
- [x] Add that row and update the worksheet contract/docs in the same change. The scorer fills version and evidence reference in the value cell.
- [x] Audit each accepted run's contemporaneous evidence before scratch cleanup; add the metadata row directly to its completed worksheet. Use `Unknown` plus the evidence limitation when no tied version evidence exists. Never regenerate a completed worksheet or infer a version from a pin/current installation.
- [x] Verify all 105 worksheets have the row; removing only that added row in memory must reproduce their pre-change bytes. Verify all other accepted files and original scenario inputs are unchanged. Check evidence references resolve.
- [x] Run `.venv/bin/python -m pytest -q` from `skill-validation/runner`, review the diff and commit the green worksheet/backfill unit. Do not delete scratch as part of this task.

Verification: the missing-row test failed before implementation; all 15 worksheet tests and the public CLI template pass, with 160 runner tests and 263 hook tests passing (three hook skips).
Every historical worksheet's pre-change bytes are reproduced by removing only its new row; other accepted files and scenario inputs are unchanged.
All historical CLI versions remain `Unknown` under the [evidence limitations in the spec](specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-baseline-decision-current-dd-and-no-dd-with-cli-provenance).

## Task 2: Controlled Codex invocation and bounded runtime lifecycle

**Files:** `skill-validation/runner/src/skilltest/providers.py`, a small `codex_runtime.py` beside it, necessary integration in `runner.py`, the error enum in `results.py` and `skill-validation/runner/result.schema.json`, and corresponding runner tests/docs.
Use existing `TestConfig`, `RunContext` and provider request/result structures; no new public CLI or config interface is required.
This task owns the internal setup-to-invocation boundary together, including logging the actual resolved command and propagating lifecycle failures.
Keep `execution.executable` as the existing provider label; record the absolute resolved invocation in runner.log instead of widening that schema field.
Keep an unknown exit code as `null` if bounded Codex timeout cleanup cannot reap the child; the Codex-only timeout schema branch must accept this existing field shape instead of requiring a fabricated integer.
The Codex-only runtime owns private directories, file-cache authentication, template-free Git initialization and owned process-group cleanup; preparation checks compare declared prompt/fixture bytes before that invocation.

- [x] Write failing contracts in `test_providers.py`, `test_run.py`, `test_results.py` and focused runtime tests for the behaviors below. Observe failures before implementing each behavior.

| Contract | Required cases |
|---|---|
| Argv and environment | Absolute resolved Codex executable; fixture cwd; sibling evidence `--add-dir`; fixed ignore/auth/approval/shell overrides from the spec; unchanged prompt bytes, configured model/effort and output flags. Only private HOME/CODEX_HOME/TMPDIR and explicit PATH reach Codex. Claude argv/env/cwd remain unchanged. |
| Preparation | Fresh private directories and project boundary; reject missing executable, mismatched prepared inputs and existing/declared `.git` before initialization or model invocation. Initialize the owned Git boundary without templates or inherited user/system Git settings. |
| Authentication | Private parents mode 0700 and auth mode 0600; copy only the invoking profile's regular auth cache, validate private login with bounded output handling, and never retain raw auth/status output. Missing, malformed or unusable credentials fail before a model call; no alternate backend is attempted. |
| Lifecycle | Setup subprocess timeout 30 seconds; model timeout 900 seconds; termination grace five seconds. Terminate/escalate only the owned Codex process group and reap its child before runtime deletion on failure/handled interruption; stop remaining owned group members after normal return too. Cover partial setup, launch failure, nonzero exit, timeout and successful completion with dummy credentials. |
| Reporting | Keep actual provider exit/output. Preflight failures use preparation reporting with no model invocation. Cleanup failure returns a nonzero outcome and `PROVIDER_CLEANUP_FAILED` if no earlier error exists; otherwise retain the earlier error and log cleanup failure additionally. Log the exact recovery path without contents. |
| Test isolation | Rework Codex fake-provider configuration so it does not rely on inherited `SKILLTEST_FAKE_*` variables; do not add a production environment bypass to keep old tests passing. Tests never read the owner's auth cache or contact a provider. |

- [x] Implement the smallest helper and adapter changes satisfying those tests. Per-run checks cover owned setup and declared copied bytes, not semantic catalog interpretation. Record safe pre-launch input hashes in the existing runner log; retain final-state inventory semantics in result.json.
- [x] Update runner documentation for the Codex-only cwd change, private-runtime requirements, added error code and manual recovery limitation after uncatchable kills. Keep raw model artifacts even when cleanup fails; do not classify an evaluable response as automatically retryable merely because cleanup failed.
- [x] Run the full offline runner suite and the hook suite; review the complete change and commit this independently green unit. No real-provider qualification yet.

Verification: 199 offline runner tests pass; the hook suite passes 263 tests with three skips.
Lifecycle review fixed deadline-edge reaping, false cleanup reporting after successful deletion, and unclosed pipes on handled interruption, with failing regression checks observed before each correction.
The schema retains its shape/version and provider labels; only the cleanup enum/state and truthful Codex timeout-with-unknown-exit case are added.
The [operator guide](../skill-validation/runner/README.md#codex) documents the implemented controls and remaining qualification limits.
Review was performed inline because this session has no no-write-tool reviewer type; no provider-backed review or real authentication was used.

## Task 2a: Consistent unit/process-smoke boundaries

Owner-approved after the Git-timeout test's intermittent cleanup failure.
Scope: runner tests, test configuration and operator documentation only; preserve production behavior and all pilot inputs.
Keep temporary filesystem operations real where they are the subject of the test; mock subprocesses, process signals and waiting in unit tests.
Real-process tests cover wiring and lifecycle behavior that mocks cannot establish, use dummy credentials, and never call an installed model CLI.

- [x] Add a unit-test guard rejecting unexpected subprocess launches/signals/sleeps; observe the mixed tests fail before restructuring them.
- [x] Separate runner persistence/provider/runtime unit tests from a small named process-smoke group; mock each unit's external boundary consistently, including both arms of failure parametrizations.
- [x] Retain real CLI wiring, Git template/profile isolation, and owned-process termination smoke coverage; use readiness signals rather than short startup deadlines and bound all waits.
- [x] Replace the ineffective provider-grace patch with checks at the actual Codex lifecycle boundary; preserve timeout, interruption, error precedence, secret handling and cleanup coverage.
- [x] Verify unit and smoke groups separately, mutation-check critical timeout/cleanup assertions, run the combined runner and hook suites, and document the two commands and remaining limits.

Verification: 224 guarded unit tests and seven local process smoke cases pass separately; the combined suite passes 231 tests, and hooks pass 263 with three skips.
In-memory mutations of the setup deadline, process shutdown and runtime removal are rejected; production files remain unchanged.
The [runner testing guide](../skill-validation/runner/README.md#testing-the-runner-code) documents selection and ownership of each boundary.

This removes incidental process scheduling from orchestration assertions; it does not establish the original failure's root cause or excuse a failing process smoke test.
No production fix, provider qualification, hooks redesign or repository-wide test rewrite is included.

## Task 3: One provisional runbook, then a bounded pilot

**Files:** `skill-validation/pilot/README.md`; new `pilot/dr-02/` and `pilot/lp-01/` prompt/config/rubric files; explicit frozen input files under `pilot/inputs/`; small qualification configs/prompts under `pilot/qualification/`; and a link from `skill-validation/README.md`.
These are new pilot inputs in the existing validation tree, not moved or replaced scenario packages.
Results remain scratch-only through owner review; use one Markdown summary linking each run and its worksheets.

- [x] Prepare separate current/no-DD variants from DR-02 and LP-01 as specified in the design. Both DR-02 prompts explicitly request the evidence-note write and permit no other edits; LP-01 remains response-only. Keep semantic rubrics unchanged and document the added file-output check as task fidelity. Permission alone is not a request whose omission can be scored.
- [x] Freeze the nine current DD skills from the recorded main revision and the required Superpowers 6.3.0 package files, including writing-plans and its referenced guidance. Use configs as the exact file/target inventory, linked from the runbook, not references to mutable installed paths. Use the same Superpowers files in both conditions and audit valid loading instructions without leaking DD descriptions into no-DD.
- [x] Write the short runbook with concrete preparation/version/run/worksheet commands, working directories, frozen-input checks, output paths and owner checkpoints. Use the existing config fixture targets for native `.agents/skills/` placement; no installation script or manifest format. Preserve pre-run input sources separately from post-run files and score against the frozen rubric.
- [x] Document provider-free qualification using the implemented runtime setup, installed CLI inspection and the accepted spike's contamination-control method. Verify no-DD/current native catalogs and declared common inputs before model calls; keep raw evidence and explicit normalization limits in scratch. Do not convert the spike into a generic production inventory parser. If the selected controls cannot be proved, stop and report the precise gap.
- [x] Prepare two real qualification commands, one per condition, using the pilot's frozen skills/tools: require supplied-source reads and an evidence-directory write in both; require the intended research/plan skill loads in current-DD and the declared writing-plans load in both. Keep these setup checks separate from behavioral scoring. Show each complete command, provider/model/effort and wait for explicit approval before invoking it.
- [x] After qualification passes, request exact-command approval for the four observation runs: DR-02 first, then LP-01; each runs no-DD once, then current-DD once, in fresh runtimes. This exercises the minimal workflow; repetitions and order balancing are deferred to later campaign design. Capture CLI version immediately before each run from the same executable. Stop on validation failure or drift; infrastructure-only unchanged-command retries follow the existing policy and are separately recorded.
- [x] Complete a worksheet for each judgeable observation, including FAILs. Inspect saved files and observable reads rather than trusting the final answer's assertions. Record missing writes as task fidelity when write access is established; do not confuse model behavior with a failed setup control.
- [x] Exercise handoff and failure/recovery bookkeeping using retained or synthetic evidence where possible, without deliberately spending more provider calls to manufacture failures. The summary identifies completed/planned runs, exclusions, deviations and the next resumable action.
- [x] Prepare the complete pilot record and practical runbook findings for owner review, then stop. Do not expand the matrix, author skill edits, promote pilot observations into an effectiveness baseline, or clean up evidence automatically.

Preparation is at [the pilot runbook](../skill-validation/pilot/README.md), with four behavioral configs and two qualification configs.
All nine DD files match main `ca14bbe24f8aea957dbcfeece3511226e929243d`; both conditions use the same frozen writing-plans and reviewer-guidance files from Superpowers 6.3.0.
The first provider-free catalog check found six common entries and exactly nine DD additions; normalized common prompt content and 60 bootstrap file hashes matched.
Provider-free gates pass: the four accepted contamination controls were reconciled to the private-profile/project-boundary setup, loopback positive/denied controls passed under host execution, and the selected shell/file tools read the qualification fixtures successfully.
Scratch `preflight/reconciliation.md` records exact evidence references, CLI version/digest, cleanup, and the limits of debug inspection and untraced login-shell startup reads.
The [qualification reference](../skill-validation/pilot/qualification/README.md) pins retained-evidence inspection and provider-free checks; the routine runbook requires version/digest comparison before each launch and owner-assisted recovery when process ownership cannot be established.
The prior mixed Git-timeout test is replaced by deterministic setup-failure checks and explicit real-process smoke coverage in Task 2a; its original OS failure cause remains unconfirmed.
Task 2a verification passes; scratch `runbook-review-verification.md` preserves the original error and retained dummy-runtime path without claiming a production fix.
The test-only review separated CLI diagnostic formatting into the guarded unit group and restored cleanup-error logging coverage at the provider adapter boundary.
The additional requested review found no new test-change findings; a fresh combined runner suite passes 231 tests.
The approved no-DD qualification passed in 42.17 seconds: all six required reads matched full supplied bytes, the correct evidence file was written and reread, declared inputs remained unchanged, and private-runtime removal was verified without a cleanup error.
The separately approved current-DD qualification passed in 40.29 seconds: all eight required full reads were observed, the evidence write was correct, all fifteen supplied files remained unchanged, and exact private-runtime removal was verified without a cleanup error.
Both calls used Codex / gpt-5.6-sol / low and CLI 0.153.4 with the same verified digest; neither required a retry or collected an effectiveness observation.
Scratch `attempts/q-no-dd/result.md` and `attempts/q-current-dd/result.md` record run IDs, tied CLI provenance, raw traces, audits and cleanup evidence beneath `/private/tmp/skilltest-sol-low-pilot.Lunoau/`.

### Pilot handoff — owner acceptance pending

All four observations used clean input revision `e537c03909eb2b4f1986e4170a3f1b662d29a719`, Codex / gpt-5.6-sol / low and CLI 0.153.4 with matching per-run executable digests.
DR-02 passed both conditions; current-DD also has a non-blocking task-fidelity failure for extra progress narration.
LP-01 failed without DD for implementation/test bodies and passed with current DD for its prose contract and single-PR boundary.
Both LP runs attempted to read application source absent from the response-only fixture, then continued; no declared input was missing and both plans remain judgeable.
The four calls completed without retries, input changes or unresolved runtime cleanup; worksheet metadata/rubric checks passed.
The [original scratch summary](/private/tmp/skilltest-sol-low-pilot.Lunoau/summary.md) links every result, worksheet and audit; `recovery-handoff-walkthrough.md` records the retained/hypothetical recovery exercise, not a live interruption test.
No runner change was needed to exercise the procedure.
Task 4 clarifies future LP-01 inputs while preserving this recorded input revision and all four observations.
These single observations are not effectiveness estimates or formal authoring RED/GREEN acceptance.
Owner acceptance remains pending; approved documentation refinement below does not authorize additional model testing or rewrite work.

## Task 4: Simplify the routine and propose a bounded extension

**Files:** the governing spec, this plan, validation/pilot READMEs, `pilot/qualification/README.md` and both `pilot/lp-01/*/prompt.md` files.
No runner, skill, source-scenario or accepted-evidence changes; preserve all existing scratch.

- [x] Separate change-triggered qualification from routine input/version checks, invocation, evidence/cleanup inspection, scoring and handoff.
- [x] Keep the ordinary record to the existing bundle, CLI/command captures, one worksheet and one summary row; extra narratives only for exceptions.
- [x] Freeze evaluator-only rubric/ledger interpretations before new collection; keep the same interpretation across conditions.
- [x] Clarify future LP-01 prompts symmetrically: task facts only, no application source or assumed implementation; do not relabel the completed runs.
- [x] Make this plan the single current project-status home; link it from the spec/README and retain attempt evidence in scratch.
- [x] Propose DR-05, LP-05 and AR-03 behavior variants and exact loading prefixes/task prompts in the [spec](specs/2026-09-06-skilltest-controlled-inputs-design.md#proposed-pilot-extension-explicitly-loaded-behavior-under-pressure), without creating executable variants or invoking providers.
- [x] Review the amended spec/runbook against the charter and source rubrics, address findings, and run provider-free verification.
- [x] Present the proposed scenarios and exact prompts for owner review, then stop before extension preparation.

The proposal is six additional observations: each scenario once without DD and once with current DD, Codex / gpt-5.6-sol / low.
It adds explicitly loaded missing-evidence/edge-case pressure and real-code review; it does not test discovery, establish effectiveness, exercise implementation or replace the original four runs.
The owner requires separate explicit discovery and behavior scenarios: the revised behavior prompts name the target/composed skills; a dedicated native-discovery scenario remains outside these six runs and needs separate prompt/count approval.
The owner also requires both coverage types for every DD skill. The [completed catalog-purpose audit and deferred plan](deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md) capture that broader work without changing historical scenarios or expanding the immediate pilot.
The new review dependency needs affected qualification; any required real qualification call is separately counted and approved.
Current execution and owner checkpoint: see Task 6 below.

Review addressed task-neutral AR verdict scoring, the new dependency's qualification boundary, scratch-directory preconditions, duplicated status and historical-prompt provenance.
Owner feedback separated explicitly loaded behavior from native discovery; the catalog audit found the concrete CW mixing and missing native discovery coverage and placed repairs in the deferred plan.
The final inline review found no remaining blocking findings; no no-write-tool reviewer type is available in this session.
Verification: 231 offline runner tests passed; hooks passed 263 with three skips; 99 local links/anchors resolved; all six existing configs loaded and the 105-scenario configuration inventory was checked.
Both LP prompt edits are exactly the same two-line insertion; skills, runner, source scenarios/accepted evidence, frozen fixtures, configs and rubrics are unchanged.
No additional provider commands ran.

## Task 5: Prepare the explicitly loaded behavior extension

**Authority:** Owner's request to continue the current pilot authorizes input preparation, not provider invocation or the deferred catalog program.
**Files:** `skill-validation/pilot/{dr-05,lp-05,ar-03}/{no-dd,current-dd}/` prompt/config/rubric files; frozen task inputs and Superpowers requesting-code-review files under `pilot/inputs/`; active spec/plan and routine runbook.

- [x] Prepare the three paired tasks with explicit DD loading only in current-DD and the same relevant Superpowers reads in both arms; supply all nine frozen DD skills versus none, no hooks.
- [x] Preserve DR-05/LP-05 source rubrics; adapt AR-03 only to a task-neutral severity/blocking conclusion. Freeze the shared scoring interpretation and record loading fidelity separately.
- [x] Verify Superpowers 6.3.0 review files and source fixture bytes; audit config targets, common-input equality, prompt differences, withheld rubric boundaries and copied bytes through the runner's provider-free preparation helpers.
- [x] Review and verify the input/documentation unit, then commit its recoverable revision before collection. Keep audit evidence in disposable scratch; preserve original pilot/scenario results.
- [x] Determine and perform affected provider-free catalog/common-input qualification; reuse unaffected controls only with evidence. Stop on drift or unproved controls.
- [x] Present all six observation commands at separate exact-command approval checkpoints before invocation. Qualification reuse required no additional paid call; approvals and commands are retained in the extension scratch summary.

Sequence remains DR-05, LP-05, AR-03, each no-DD then current-DD once on Codex / gpt-5.6-sol / low.
AR-03 supplies project files, not implementation Git history; its common prompt must explicitly apply the supplied reviewer criteria directly without dispatch or an unavailable Git-range review.
This bounds the same review task in both arms rather than introducing fake history or a new runner capability.

Input audit evidence is retained under `/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/`: `audit-inputs.py`, the exact command in `summary.md`, and `preflight/input-audit.json` with empty stderr.
All six prompts/rubrics and prepared fixture maps passed pair/source checks; ten new source copies match, and all nine DD copies retain their recorded main bytes.
The audit did not call any CLI, authenticate, prepare a private runtime or qualify a native catalog; those controls are not inferred from copying success.
Verification: 231 runner tests passed, hooks passed 263 with three skips, 108 local links/anchors resolved, and the inline input/spec review found no remaining blocking findings.
Original scenario/accepted records, runner code and DD skills are unchanged; no additional model commands ran.

Extension qualification is recorded in scratch `preflight/reconciliation.md`: CLI 0.153.4 and digest unchanged; native catalogs 7/16 with nine DD additions; common content and all 60 bootstrap hashes match; all AR fixture/guidance shell reads and private-runtime cleanup pass.
The strict historical comparison stopped on the injected September 6→7 date change, which was explicitly reviewed rather than silently normalized; both new arms share September 7 and the tasks use fixed facts.
Two earlier scratch-audit path-parser defects are retained separately; neither involved a model call or unresolved runtime.
Runtime production code and read mechanisms are unchanged from the successful real qualification, so its controls are reused without another paid qualification call.
The completed extension's exact commands and individual approvals are retained in its scratch summary; future collection uses the bounded-batch policy.

## Task 6: Execute and score the bounded behavior extension

- [x] Execute all six separately approved observations once in the frozen order and complete their worksheets.
- [x] Verify required loading, input/CLI provenance, protected files and runtime cleanup; retain every judgeable outcome and caveat.
- [x] Prepare the owner-review handoff; no further provider commands are queued.

### Extension handoff — owner acceptance pending

The [scratch summary](/private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/summary.md) owns the six attempt/approval rows and links the unchanged bundles and scored worksheets.
Do not duplicate per-run judgments here or promote these procedure observations into effectiveness estimates.
Original observations and all 105 accepted records remain unchanged; retain the evidence pending owner acceptance.

### Post-pilot workflow amendment

The owner approved applying the five process improvements in the [bounded-batch design](specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-bounded-batch-operation).
Scope: batch approvals and verification cadence, prerequisite task facts, a short criterion/evidence table, and one home per record.
This documentation unit does not authorize another batch, alter completed fixtures/rubrics/scores, or activate catalog repairs.

- [x] Update the routine runbook, design authority and deferred-plan pointers; remove duplicated per-run narratives from this plan and the extension summary while preserving approvals and evidence.
- [x] Review all five changed repository documents and the scratch summary; reconcile approval/status references and verify protected evidence/inputs. All 106 local links resolve; hooks pass 263 tests with three skips and `git diff --check` passes. Runner verification is reused from the unchanged `17f0e90` checkpoint (231 passing tests). Review was inline because no no-write-tool reviewer type is available.

The owner's subsequent review-and-continue request advances to Task 7 below.
No runner expansion, additional process spike, provider run, Claude pilot or rewritten-skill comparison is included.

## Task 7: Map catalog purposes and propose the first repair

Scope: the mapping portion of [catalog Task 1](deferred/2026-09-07-skilltest-discovery-behavior-catalog-separation.md#task-1-map-purposes-without-moving-the-catalog), using the charter, existing summaries and representative prompts/rubrics.
Keep one coverage table in `skill-validation/README.md`; retain the repair proposal in the existing deferred plan rather than creating another manifest or plan.
This authorizes documentation only, not the whole catalog program, test-contract changes, provider commands or promotion of pilot evidence into accepted results.

- [x] Re-review the five workflow documents and scratch summary; clarify retry-directory reuse and include linked evaluator guidance in the frozen-input check. Completed evidence is unchanged.
- [x] Publish the nine-skill purpose map and representative criterion/evidence boundaries; distinguish actual artifacts from hypothetical workflow answers.
- [x] Propose three separate CW purposes for owner agreement before preparing variants; keep unresolved authoring diagnostics and further catalog repairs deferred.
- [x] Verify 156 local links/anchors, the 105-config native-target inventory, protected inputs and retained evidence/commands; hooks pass 263 tests with three skips. Review completed inline with no remaining blocking findings; runner verification is reused because its code/environment are unchanged.

The owner approved preparing the three proposed CW purposes for prompt/rubric review; broader catalog implementation and effectiveness sampling stay deferred.

## Task 8: Prepare the three CW purposes for review

**Files:** new `skill-validation/pilot/cw-01/{no-dd,current-dd,discovery}/` and `pilot/cw-17/discovery/` prompt/config/rubric files; the routine runbook, this plan and the existing catalog repair plan.
Reuse frozen `pilot/inputs/dd/` and the same four Superpowers files used by the behavior extension; no skill, runner, historical scenario or existing pilot-input edits.
CW has no explicitly required upstream task workflow, so none of these prompts forces an unrelated Superpowers read; availability remains identical across conditions apart from DD.
Task facts stay inline, preserving CW-01's source paragraph and CW-17's nested natural request without another fixture-copy layer.
This is input preparation only: no provider/CLI-auth invocation, new sampling decision, accepted-evidence promotion or broader catalog activation.

- [x] Prepare the behavior pair with identical rubrics/task text and only the current-DD loading prefix plus DD availability differing.
- [x] Prepare positive/non-trigger current-DD discovery tasks without loading hints; define observable selection/loading, missing-trace handling and separate fidelity in withheld rubrics.
- [x] Audit configs and rendered fixtures using existing provider-free helpers; verify frozen dependencies, withholding and protected inputs, then review the complete change and run the required hook suite.
- [x] Prepare the [exact prompt/rubric handoff](../skill-validation/pilot/README.md#cw-purpose-separated-inputs) in the input-preparation commit; no results collected or native-discovery qualification claimed by that step.

Provider-free audit: [input-audit.json](/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/input-audit.json), produced from the feature-worktree root by `skill-validation/runner/.venv/bin/python /private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/audit-inputs.py`.
All four configs/rendered inventories match; current-DD uses the unchanged 13 guidance files and no-DD the same four common files. Prompt relationships, rubric equality and frozen source bytes pass.
The audit's pre-freeze HEAD is preparation provenance only; this committed unit makes the new inputs recoverable. Its initial whitespace-comparison defect is retained in scratch, not counted as a model attempt or INFRA_RETRY.
Verification: hooks pass 263 tests with three skips; 147 local links/anchors resolve; protected runner, skills, historical scenarios/accepted files and previous pilot inputs are unchanged.
Inline review clarified that qualification proves observation capability, not the expected discovery result; no no-write-tool reviewer type is available. The owner subsequently approved the inputs and qualification checkpoint.

## Task 9: Qualify and exercise the CW purposes

**Authority:** Owner approved the exact four-command batch at input revision `f28ea6569b7eb5b65245e77635a5ff7d12fc1082`: CW-01 no-DD behavior, current-DD loaded behavior, positive discovery, then CW-17 non-trigger discovery, once each on Codex / gpt-5.6-sol / low.
Scope remains these three purposes; no broader catalog activation, skill edit or effectiveness campaign.

- [x] Reconcile affected qualification using identical guidance targets/bytes, pinned CLI and unchanged runtime/read/trace mechanisms; no additional paid qualification.
- [x] Execute all four approved commands once in order; inspect full traces, protected inputs, CLI provenance and runtime cleanup, and complete separate worksheets.
- [x] Retain the first run's nonfatal model-catalog refresh warning under the owner's explicit non-blocking disposition; preserve its evaluable response with no retry, input change or hidden-impact claim.
- [x] Reconcile warning policy and coverage/status references; keep all judgments and attempt evidence in the [scratch summary](/private/tmp/skilltest-sol-low-pilot.Lunoau/cw-inputs.veav95/summary.md) and its worksheets.
- [x] Review and verify the documentation/evidence handoff for the bounded documentation commit; stop for owner review.

All four commands completed with runner/provider exit 0, matching CLI 0.153.4/digest and unchanged declared inputs; no retries or unresolved cleanup.
The warning-policy amendment was approved between commands 1 and 2 and retained in scratch during collection; scenario prompts, rubrics, fixture sources and commands remained frozen throughout.
Per-purpose observations stay separate; do not promote them to effectiveness estimates, authoring RED/GREEN acceptance or accepted baseline evidence.
Verification: four worksheets preserve generated mechanical fields and tied CLI captures; all 209 local links/anchors across eleven documents resolve, the four approved commands and 169 prior extension evidence files are unchanged, protected input/runner/skill/scenario diffs are empty, and hooks pass 263 tests with three skips.
Runner verification is reused from the unchanged 231-test checkpoint. Inline review retained the stop rule for actual unexpected execution failures while separating nonfatal diagnostics; no no-write-tool reviewer type is available.
Next checkpoint: owner review of this batch and the warning-policy clarification; no further provider command is queued.

## Approval and verification checkpoints

- [x] Repair the observed timeout-test startup race before Task 1.
  The timeout case now writes fixture/evidence files synchronously at the provider boundary and returns a simulated timeout; the real runner still performs output publication, inventory, error precedence and result validation.
  Task 2a subsequently applies the in-memory provider boundary to both cases and moves real timeout/termination coverage to `tests/process_smoke/test_runtime.py`.
  This removes the 0.2-second startup assumption without changing production code or adding synchronization machinery.
  Verified: three focused cases pass, the full runner suite passes 160 tests, and an in-memory primary-error mutation is rejected by the revised test.
  The test-related pause is cleared; pilot-task and provider-command approvals remain separate.

Review this plan and the amended spec before Task 1. Scenario/count approval does not approve provider commands.
Before signing off a code-changing implementation unit, run the offline runner and hook suites, check local documentation links and run `git diff --check`.
For documentation-only or collection units, use the [bounded-batch cadence](../skill-validation/pilot/README.md#bounded-batches-and-approval): retain unchanged harness verification, check affected artifacts and run the required hook suite once at handoff.
After Task 2, confirm the final invocation/setup matches the approved design before any Task 3 real calls.
The pilot is successful when the procedure produces trustworthy, reviewable records and exposes its limitations; skill PASS is not its completion criterion.
