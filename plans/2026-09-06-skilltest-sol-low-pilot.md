# Controlled-Input Sol-Low Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` task by task, stopping at the review checkpoints below.

**Status:** Tasks 1–2 are complete following the owner's requests to continue.
Task 3 and all provider calls remain behind their review/approval checkpoints; no real qualification or pilot observations have been run under this plan.
The owner separately authorized the completed preparatory timeout-test repair described below.
The proposed scenarios, eight observation runs and two real qualification calls below require approval with this plan; each provider command also requires its separate exact-command approval.

**Goal:** Exercise one agent-led preparation, execution, scoring and handoff workflow, not collect effectiveness estimates.
**Architecture:** Preserve the one-run runner and config schema; add only Codex runtime controls and a worksheet field, then exercise them through one written runbook.
**Tech stack:** Existing Python runner, pytest, Git and the locally qualified Codex CLI on macOS.
**Spec:** [Pilot-first design amendment](specs/2026-09-06-skilltest-controlled-inputs-design.md).

## Global constraints

- Work only in `.worktrees/skilltest-input-isolation-spike` on `spike/skilltest-input-isolation`; preserve main and the unrelated rewrite worktree.
- Start with Codex / gpt-5.6-sol / low. Medium is a justified, separately identified diagnostic under exact-command approval, not an automatic retry.
- Current-DD supplies all nine DD skills; no-DD supplies none. Freeze the same declared Superpowers and ordinary tools across both, with no DD hooks.
- Do not edit skills or existing scenario inputs, rescore accepted baselines, or replace their result/final/evidence files. The sole historical exception is the CLI-version worksheet metadata backfill.
- Keep the existing config schema and result shape. The only proposed error-enum addition is `PROVIDER_CLEANUP_FAILED`; preserve Claude invocation behavior.
- No generic inventory/status framework, campaign engine, automatic scorer, hooks work, directory migration, candidate skill authoring or effectiveness campaign.
- Never print or retain credentials. Keep private runtime outside retained bundles, and never modify shared authentication or host sessions.
- Deliver on this feature branch with independently green commits; no PR, merge or branch deletion is authorized by this plan.

## Task 1: Worksheet field and historical provenance

**Files:** `skill-validation/runner/src/skilltest/worksheet.py`, `skill-validation/runner/tests/test_worksheet.py`, the CLI worksheet expectation in `skill-validation/runner/tests/test_cli.py`, `skill-validation/runner/README.md`, the worksheet contract in `plans/completed/specs/2026-09-02-skill-testing-methodology-design.md`, and the 105 existing `accepted/worksheet.md` files.
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

## Task 3: One provisional runbook, then a bounded pilot

**Files:** `skill-validation/pilot/README.md`; new `pilot/dr-02/` and `pilot/lp-01/` prompt/config/rubric files; explicit frozen input files under `pilot/inputs/`; small qualification configs/prompts under `pilot/qualification/`; and a link from `skill-validation/README.md`.
These are new pilot inputs in the existing validation tree, not moved or replaced scenario packages.
Results remain scratch-only through owner review; use one Markdown summary linking each run and its worksheets.

- [ ] Prepare separate current/no-DD variants from DR-02 and LP-01 as specified in the design. Both DR-02 prompts explicitly request the evidence-note write and permit no other edits; LP-01 remains response-only. Keep semantic rubrics unchanged and document the added file-output check as task fidelity. Permission alone is not a request whose omission can be scored.
- [ ] Freeze the nine current DD skills from the recorded main revision and the required Superpowers 6.3.0 package files, including writing-plans and its referenced guidance. Inventory exact supplied files in the runbook and configs, not references to mutable installed paths. Use the same Superpowers files in both conditions and audit valid loading instructions without leaking DD descriptions into no-DD.
- [ ] Write the short runbook with concrete preparation/version/run/worksheet commands, working directories, frozen-input checks, output paths and owner checkpoints. Use the existing config fixture targets for native `.agents/skills/` placement; no installation script or manifest format. Preserve pre-run input sources separately from post-run files and score against the frozen rubric.
- [ ] Document provider-free qualification using the implemented runtime setup, installed CLI inspection and the accepted spike's contamination-control method. Verify no-DD/current native catalogs and declared common inputs before model calls; keep raw evidence and explicit normalization limits in scratch. Do not convert the spike into a generic production inventory parser. If the selected controls cannot be proved, stop and report the precise gap.
- [ ] Prepare two real qualification commands, one per condition, using the pilot's frozen skills/tools: require supplied-source reads and an evidence-directory write in both; require the intended research/plan skill loads in current-DD and the declared writing-plans load in both. Keep these setup checks separate from behavioral scoring. Show each complete command, provider/model/effort and wait for explicit approval before invoking it.
- [ ] After qualification passes, request exact-command approval for the eight observation runs: DR-02 first, then LP-01; each runs no-DD, current-DD, current-DD, no-DD in fresh runtimes. Capture CLI version immediately before each run from the same executable. Stop on validation failure or drift; infrastructure-only unchanged-command retries follow the existing policy and are separately recorded.
- [ ] Complete a worksheet for each judgeable observation, including FAILs. Inspect saved files and observable reads rather than trusting the final answer's assertions. Record missing writes as task fidelity when write access is established; do not confuse model behavior with a failed setup control.
- [ ] Exercise handoff and failure/recovery bookkeeping using retained or synthetic evidence where possible, without deliberately spending more provider calls to manufacture failures. The summary identifies completed/planned runs, exclusions, deviations and the next resumable action.
- [ ] Present the complete pilot record and practical runbook findings, then stop for owner review. Do not expand the matrix, author skill edits, promote pilot observations into an effectiveness baseline, or clean up evidence automatically.

## Approval and verification checkpoints

- [x] Repair the observed timeout-test startup race before Task 1.
  The timeout case now writes fixture/evidence files synchronously at the provider boundary and returns a simulated timeout; the real runner still performs output publication, inventory, error precedence and result validation.
  The nonzero case retains its fake subprocess, and `test_marks_timeout_after_terminating_direct_provider` retains real timeout coverage.
  This removes the 0.2-second startup assumption without changing production code or adding synchronization machinery.
  Verified: three focused cases pass, the full runner suite passes 160 tests, and an in-memory primary-error mutation is rejected by the revised test.
  The test-related pause is cleared; pilot-task and provider-command approvals remain separate.

Review this plan and the amended spec before Task 1. Scenario/count approval does not approve provider commands.
Before signing off each implementation unit, run the offline runner suite and `python3 -m pytest -q` in `skills/disciplined-development/hooks`, check local documentation links and run `git diff --check`.
After Task 2, confirm the final invocation/setup matches the approved design before any Task 3 real calls.
The pilot is successful when the procedure produces trustworthy, reviewable records and exposes its limitations; skill PASS is not its completion criterion.
