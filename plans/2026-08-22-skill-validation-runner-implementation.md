# Skill Validation Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a small, stateless Python CLI that prepares one declared skill scenario, runs it through Codex, captures objective evidence, and stops without issuing a semantic verdict.

**Architecture:** Fixed repository conventions provide scenario and withheld-plan definitions. Focused modules resolve exact source bytes, materialize a fresh workspace, supervise one provider CLI per repetition, run declared objective commands, and write a versioned run-relative result bundle. The CLI only coordinates these mechanical parts; an agent and owner interpret behavior afterward.

**Tech Stack:** Python 3.11+, standard library, PyYAML, pytest, uv, Codex CLI subprocesses.

**Spec:** `plans/specs/2026-08-22-skill-validation-harness-design.md`

**Status:** Proposed for owner approval. This document authorizes no implementation, worktree creation, dependency installation, model call, staging, or commit.

## Global Constraints

- Read `CLAUDE.md`, `ARCHITECTURE.md`, the spec, and this plan from disk before each execution session or task handoff.
- Use `superpowers:using-git-worktrees` to create `feature/skill-validation-runner` in a fresh worktree from the `main` commit containing the approved spec and plan. Do not implement in the comprehensive-cleanup worktree.
- Use strict witnessed RED-GREEN-REFACTOR for every production behavior. A bug receives a reproducing failing test before its fix.
- Tests use real temporary files, Git repositories, and subprocesses. A fake `codex` executable is allowed; mocking runner filesystem, subprocess, or result-writing internals is not.
- Python is 3.11 or newer. PyYAML is the only runtime dependency; pytest is development-only.
- Do not add Click, Typer, Pydantic, jsonschema, Rich, a database, retries, resume state, run groups, plugins, semantic scoring, or adjudication.
- Use `apply_patch` for hand-authored edits. A generated `uv.lock` is the only planned mechanical file rewrite.
- Do not modify skill wording, hooks, existing root-level validation records, comprehensive-cleanup fixtures, or ignored Task 24–26 evidence.
- `.skilltest/runs/` is ignored and disposable. Promoted evidence must not depend on it.
- Do not invoke Claude or start a model campaign. The only live model call in this plan is one owner-announced Sol-low smoke after the offline suite and inputs are reviewed and frozen.
- Do not stage or commit at task boundaries. This deliberately overrides the normal commit-per-task workflow because owner approval is required after all hard gates. Record each task's RED and GREEN commands in this plan; stage, commit, and push only in the final owner-approved task.
- Retain partial artifacts and materially better good-enough results. Never waive an infrastructure, contract, review, or owner gate.

## Merge boundary

This plan is one branch-sized runner change. Scenario migration, main-versus-cleanup baselines, skill sharpening, Claude support, hook modernization, legacy validation removal, and top-level documentation changes are separate later branches. Keeping those changes out of this branch lets one cold review judge the runner without mixing it with the skill behavior it will eventually measure.

## Canonical implementation contract

The design specification is the sole authority for selectors, discovery paths, scenario and plan schemas, capabilities, source arguments, command declarations, subject input, Codex argv, result schema, exit behavior, run layout, and evidence promotion.
This plan intentionally does not restate those contracts; an implementation change starts by updating the owning specification section so the two documents cannot drift.

The following task-wide applications are worth making explicit:

- resolve the repository with `git rev-parse --show-toplevel` and reject execution outside a Git worktree;
- reject duplicate identifiers, selector/path disagreement, missing paired definitions, path escapes, and non-regular declared inputs;
- validate required capabilities against every profile in the tracked plan before selecting one;
- place global Codex flags before `exec`, encode effort only as `-c 'model_reasoning_effort="<effort>"'`, and never invent `--effort` or `--reasoning-effort`;
- keep selected skill bytes at `supplied-skills/<skill>/SKILL.md`, outside provider auto-discovery, and withhold expected outcomes and consumers from the subject;
- store disposable runs only beneath `.skilltest/runs/` and promote only to a new `skill-validation/evidence/<run-id>/` directory without overwrite;
- use `skills/disciplined-development/hooks/lib/reviewer_runner.py` only as subprocess-lifecycle and fake-CLI prior art; do not reuse its prompt, verdict, severity, gate, cadence, review log, or state behavior.

Official Codex behavior can still expose admin or system skills; the final live smoke must inspect for ambient-skill interference. If that gate fails, stop and amend the design with the owner instead of adding hidden isolation machinery.

## Planned file map

| File | Responsibility |
|---|---|
| `.gitignore` | Ignore `.skilltest/runs/` only; evidence stays trackable. |
| `skill-validation/charter/core-contracts.md` | Pre-existing approved design foundation inherited from `main`; verify its hash and do not edit it during runner implementation. |
| `skill-validation/harness/pyproject.toml`, `uv.lock` | Installable package, console entry point, dependency lock. |
| `skill-validation/harness/src/skilltest/contracts.py` | Small immutable dataclasses, enums, records, and user/infrastructure error types shared across modules. Later tasks add only the records their behavior requires. |
| `skill-validation/harness/src/skilltest/definitions.py` | Fixed discovery, YAML loading, structural validation, profile selection. |
| `skill-validation/harness/src/skilltest/sources.py` | Source-argument parsing, containment, repository metadata, input snapshots and digests. |
| `skill-validation/harness/src/skilltest/workspace.py` | Fresh workspace creation, fixture/Git setup, selected skill materialization, subject preamble. |
| `skill-validation/harness/src/skilltest/process.py` | One bounded, signal-aware, concurrently drained subprocess primitive and sanitized child environment. |
| `skill-validation/harness/src/skilltest/codex.py` | Codex version probe, argv construction, invocation, JSONL/final-output validation. |
| `skill-validation/harness/src/skilltest/checks.py` | Direct observer and consumer execution with artifact-input resolution. |
| `skill-validation/harness/src/skilltest/artifacts.py` | Run paths, logging, hashing, artifact references, atomic result writing, derived summary. |
| `skill-validation/harness/src/skilltest/runner.py` | Sequential inspect/run orchestration; no judgment or persistent state. |
| `skill-validation/harness/src/skilltest/promotion.py` | Refuse-overwrite copy of compact evidence; no selection or Git action. |
| `skill-validation/harness/src/skilltest/cli.py`, `__main__.py`, `__init__.py` | `inspect`, `run`, and `promote` argument surface and exit mapping. |
| `skill-validation/harness/tests/` | Offline unit, subprocess, filesystem, Git, CLI, integration, and promotion tests. |
| `skill-validation/harness/README.md` | Focused install, definition, run, logging, result, and agent/owner-loop documentation. |

---

### Task 1: Isolated worktree, package entry point, and ignored run root

**Files:**
- Read without modifying: `skill-validation/charter/core-contracts.md`
- Create: `skill-validation/harness/pyproject.toml`
- Create: `skill-validation/harness/src/skilltest/__init__.py`
- Create: `skill-validation/harness/src/skilltest/__main__.py`
- Create: `skill-validation/harness/src/skilltest/cli.py`
- Create: `skill-validation/harness/tests/test_cli.py`
- Generate: `skill-validation/harness/uv.lock`
- Modify: `.gitignore`

**Interfaces:**
- Produces: `skilltest.cli.main(argv: Sequence[str] | None = None) -> int`; console command `skilltest`; importable package version.
- Consumes: no production interface.

**Unhandled inputs and invariants:** The test entry point must work from a clean uv environment and Python 3.11. The inherited canonical charter must exist and hash to `4d172cfbcda96883a4ebc5fec6462e81545de9b862921f39de69f18eceb74aae`; any mismatch stops work. No command performs useful behavior yet.

- [ ] **Step 1: Establish the execution boundary.** Confirm the approved spec and plan are present on `main`, use `superpowers:using-git-worktrees`, create `feature/skill-validation-runner`, and re-read governing files from the new worktree.
- [ ] **Step 2: Write the failing entry-point test.** Require `uv run skilltest --help` to exit `0` and list exactly the three subcommands `inspect`, `run`, and `promote`.
- [ ] **Step 3: Witness RED.** Run `uv run pytest tests/test_cli.py::test_help_lists_only_supported_commands -q` from `skill-validation/harness`; expect failure because the package and entry point do not exist.
- [ ] **Step 4: Add the minimum package surface.** Add Python and dependency metadata, the console entry point, argparse subparsers that only display help, and `.skilltest/runs/` to `.gitignore`; generate the lockfile.
- [ ] **Step 5: Verify the inherited charter.** Hash `skill-validation/charter/core-contracts.md`, require the accepted SHA-256 above, and make no charter edit.
- [ ] **Step 6: Witness GREEN and refactor only while green.** Run the focused test, `uv run skilltest --help`, and `git check-ignore .skilltest/runs/example`; record commands and results under this task without staging.

### Task 2: Typed definition loading and fixed discovery

**Files:**
- Create: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/src/skilltest/definitions.py`
- Create: `skill-validation/harness/tests/test_definitions.py`
- Create: `skill-validation/harness/tests/conftest.py`

**Interfaces:**
- Produces: immutable `Scenario`, `WorkspaceSpec`, `CommandSpec`, `ConsumerSpec`, `TestPlan`, `Profile`, `ExpectedOutcome`, and `ResolvedTest`; `UserError(message: str)`; `InfrastructureError(code: str, message: str)`; `discover(repo_root: Path, selector: str, profile_name: str | None) -> ResolvedTest`.
- Consumes: the canonical selector and field contracts in the specification; `UserError(message: str)` for definition/usage failures.

**Unhandled inputs and invariants:** Reject absent files, invalid UTF-8, unsafe YAML tags, non-mapping documents, unknown or missing keys, wrong scalar types, duplicate identifiers/list entries, invalid selectors, path escapes, empty profiles, ambiguous profile selection, unknown or unsatisfied capabilities, bad outcome cross-references, and protocol outcomes without a real consumer. YAML aliases may be accepted because `safe_load` resolves them to ordinary data; recursive aliases and documents large enough to exhaust memory are accepted residual risks until observed.

- [ ] **Step 1: Add a temporary-repository fixture builder.** It writes the smallest valid neutral scenario and withheld plan under the fixed roots; it does not add tracked real scenarios.
- [ ] **Step 2: Write the valid-definition and sole-profile tests.** Assert exact typed values and automatic selection only when one profile exists.
- [ ] **Step 3: Witness RED.** Run the two focused tests; expect import or missing-function failure.
- [ ] **Step 4: Implement only safe loading, exact-key validation, fixed discovery, and typed construction needed by those tests.** Do not add schema libraries or a registry.
- [ ] **Step 5: Add table-driven invalid-definition tests.** Cover every rejected input named above, including two-profile ambiguity, capability/sandbox/workspace mismatch, and consumer/outcome mismatch.
- [ ] **Step 6: Witness RED, add the minimum validation, then witness GREEN.** Run `uv run pytest tests/test_definitions.py -q`, followed by the whole current harness suite; record both transitions.

### Task 3: Common and explicit source resolution with immutable snapshots

**Files:**
- Create: `skill-validation/harness/src/skilltest/sources.py`
- Create: `skill-validation/harness/src/skilltest/artifacts.py`
- Modify: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/tests/test_sources.py`

**Interfaces:**
- Produces: `SourceRequest`, `ResolvedSource`, `InputRecord`, and `ArtifactRef`; `sha256_file(path: Path) -> str`; `artifact_ref(run_dir: Path, path: Path) -> ArtifactRef`; `parse_source_args(values: Sequence[str], required_skills: Sequence[str]) -> SourceRequest`; `resolve_sources(request: SourceRequest) -> tuple[ResolvedSource, ...]`; `snapshot_inputs(run_dir: Path, resolved_test: ResolvedTest, sources: Sequence[ResolvedSource]) -> tuple[InputRecord, ...]`.
- Consumes: `ResolvedTest`, `UserError`, fixed source grammar, and SHA-256 artifact convention.

**Unhandled inputs and invariants:** Reject nonexistent, empty, non-regular, symlinked, invalid UTF-8, and escaped skill files; unkeyed/keyed mixtures; duplicate keys; and keyed sets with omissions or extras. The exact definition closure includes both manifests, prompt, fixture files, and declared observer/consumer executables. A dirty repository is valid input and must be recorded, not rejected. Git absence or a non-Git source produces nullable repository metadata rather than failure.

- [ ] **Step 1: Write common-root tests.** Resolve primary plus dependency from `skills/<id>/SKILL.md`, preserve exact bytes, order by plan declaration, and record Git HEAD/dirty state.
- [ ] **Step 2: Witness RED, implement the minimum common-root resolver, and witness GREEN.** Run only the named common-root tests around each edit.
- [ ] **Step 3: Write explicit-map and rejection tests.** Cover mixed roots, exact declared-set enforcement, missing files, symlinks, empty files, and containment escape.
- [ ] **Step 4: Witness RED, implement explicit resolution and containment, and witness GREEN.** Use resolved paths and regular-file checks; do not infer source policy.
- [ ] **Step 5: Write snapshot immutability tests.** Mutate original definitions and skill files after snapshotting and assert snapshots and digests remain unchanged under `inputs/definitions/` and `inputs/skills/`.
- [ ] **Step 6: Complete the cycle.** Implement snapshots, run `uv run pytest tests/test_sources.py -q`, then the current harness suite; record results without staging.

### Task 4: Fresh workspace, supplied skills, prompt envelope, and optional Git

**Files:**
- Create: `skill-validation/harness/src/skilltest/workspace.py`
- Modify: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/tests/test_workspace.py`

**Interfaces:**
- Produces: `MaterializedWorkspace`; `materialize_workspace(run_dir: Path, repetition: int, test: ResolvedTest, inputs: Sequence[InputRecord]) -> MaterializedWorkspace`; `snapshot_workspace(workspace: Path, destination: Path) -> ArtifactRef`.
- Consumes: snapshotted definition/skill bytes only, never live origins; `ArtifactRef`, `artifact_ref`, and `MaterializedWorkspace(root, prompt_bytes, initial_snapshot)`.

**Unhandled inputs and invariants:** Every repetition receives a new directory. Fixtures cannot overwrite runner-owned `supplied-skills/` or subject-prompt files, contain symlinks/special files, or escape through paths. Empty directories are preserved. File modes preserve executability but strip special bits. Git initialization uses local test identity and no inherited repository configuration. Initial/final snapshots copy the working tree without `.git/` and write a deterministic manifest; they do not rely on the disposable workspace remaining present.

- [ ] **Step 1: Write the read-only materialization test.** Assert fixture equality, selected skill paths, fixed preamble ordering, exact scenario-prompt suffix, no expected-outcome bytes, and distinct roots for two repetitions.
- [ ] **Step 2: Witness RED, implement minimal copy/materialization, and witness GREEN.** Do not use `.agents/skills`, plugin installation, or a provider-specific home directory.
- [ ] **Step 3: Write unsafe-fixture tests.** Cover collisions, symlinks, FIFO/special files, and executable-mode preservation.
- [ ] **Step 4: Witness RED, add the minimum safe tree copier, and witness GREEN.** Keep all destination checks beneath the repetition workspace.
- [ ] **Step 5: Write the Git-workspace test.** Require a clean initialized repository with the fixture as its initial commit and deterministic local identity, while a non-Git scenario has no `.git`.
- [ ] **Step 6: Implement Git setup and snapshot inventory, then run `uv run pytest tests/test_workspace.py -q` and the current suite.** Record RED/GREEN evidence without committing.

### Task 5: One bounded subprocess primitive and sanitized environment

**Files:**
- Create: `skill-validation/harness/src/skilltest/process.py`
- Modify: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/tests/test_process.py`

**Interfaces:**
- Produces: `ProcessResult(exit_code, exit_reason, stdout, stderr, duration_seconds)`; `run_process(argv: Sequence[str], cwd: Path, stdin_bytes: bytes, timeout_seconds: float, env: Mapping[str, str]) -> ProcessResult`; `sanitized_environment(base: Mapping[str, str]) -> dict[str, str]`.
- Consumes: no shell strings.

**Unhandled inputs and invariants:** Reject empty argv and non-positive timeout before spawn. Drain stdout and stderr concurrently in binary mode; close stdin; forward SIGINT/SIGTERM/SIGHUP when on the main thread; terminate, wait a bounded five-second grace, then kill. Preserve partial bytes. Child environment allowlists only execution, locale, temporary-directory, certificate, and Codex-auth location variables; unrelated tokens, API keys, proxy credentials, Python injection variables, and project hook variables are absent.

- [ ] **Step 1: Write success and missing-executable tests.** Use real temporary executables and assert exact stdin/stdout/stderr bytes plus structured spawn failure.
- [ ] **Step 2: Witness RED, implement the smallest Popen wrapper, and witness GREEN.** Consult `skills/disciplined-development/hooks/lib/reviewer_runner.py` only as lifecycle prior art; do not import or modify it.
- [ ] **Step 3: Write timeout and signal tests.** Assert bounded termination, reason classification, partial diagnostics, and handler restoration.
- [ ] **Step 4: Witness RED, implement timeout/signal handling, and witness GREEN.** Keep the five-second grace fixed, not configurable.
- [ ] **Step 5: Write pipe-pressure and environment-sanitation tests.** A child writes more than pipe capacity to both streams without hanging; a fake secret/token echo sees none of the forbidden variables while PATH and Codex authentication location remain usable.
- [ ] **Step 6: Complete the cycle.** Add concurrent draining and the minimal allowlist, run `uv run pytest tests/test_process.py -q`, then the current suite; record results.

### Task 6: Codex adapter and raw-output validation

**Files:**
- Create: `skill-validation/harness/src/skilltest/codex.py`
- Modify: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/tests/test_codex.py`

**Interfaces:**
- Produces: `CliIdentity` and `ProviderResult`; `probe_codex(executable: str, env: Mapping[str, str]) -> CliIdentity`; `build_codex_argv(profile: Profile, workspace: Path, final_path: Path, executable: str, web_search: bool) -> tuple[str, ...]`; `invoke_codex(profile: Profile, workspace: MaterializedWorkspace, repetition_dir: Path, env: Mapping[str, str], executable: str, web_search: bool) -> ProviderResult`.
- Consumes: `run_process`, `Profile`, the scenario-derived `web_search` boolean, subject prompt bytes, and repetition artifact paths.

**Unhandled inputs and invariants:** Resolve `codex` from sanitized PATH. A failed/empty/multiline version probe is infrastructure failure. Require CLI exit zero, a non-empty final file, and stdout consisting solely of UTF-8 JSON objects separated by newlines; preserve raw bytes before parsing. Event vocabulary is not normalized. The adapter must not place prompt or credentials in argv or logs.

- [ ] **Step 1: Write the argv/version-probe test using a fake `codex`.** Pass `web_search` directly from the resolved scenario capability and assert the spec's exact global-before-`exec` and exec-argument order, never-ask approval, explicit model/sandbox/cwd, effort encoded only as `-c 'model_reasoning_effort="<effort>"'`, stdin marker, separate final path, optional global `--search` only when that boolean is true, and no prompt text in argv.
- [ ] **Step 2: Witness RED, implement version probing and argv construction, and witness GREEN.** Use argument lists and the shared process primitive.
- [ ] **Step 3: Add a parser-only real-CLI contract test.** Locate the installed Codex CLI, derive both non-search and search argv from `build_codex_argv`, replace only the terminal stdin marker with `--help`, and require both commands to parse successfully without a model call. This check must fail if `--search` moves after `exec`. Record the CLI version. Official Codex configuration documentation must still list `model_reasoning_effort`; if the installed CLI or documented key is absent, stop as an adapter-contract failure rather than skipping the check.
- [ ] **Step 4: Write the successful invocation test.** The fake CLI emits two JSONL events, diagnostics, and a final file; assert raw artifacts and effective execution metadata.
- [ ] **Step 5: Witness RED, implement invocation/capture, and witness GREEN.** Store raw events unchanged; parsing only authenticates one object per non-empty line.
- [ ] **Step 6: Add failure-matrix tests.** Cover missing executable, failed version probe, nonzero CLI exit, timeout, invalid UTF-8/malformed JSONL, and missing or empty final response.
- [ ] **Step 7: Complete the cycle.** Implement stable infrastructure reason codes, run `uv run pytest tests/test_codex.py -q`, the parser-only real-CLI contract test, then the current suite; record results.

### Task 7: Objective observers and deterministic consumers

**Files:**
- Create: `skill-validation/harness/src/skilltest/checks.py`
- Modify: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/tests/test_checks.py`

**Interfaces:**
- Produces: `CheckContext`, `ObserverResult`, and `ConsumerResult`; `run_observers(specs: Sequence[CommandSpec], context: CheckContext) -> tuple[ObserverResult, ...]`; `run_consumers(specs: Sequence[ConsumerSpec], context: CheckContext) -> tuple[ConsumerResult, ...]`.
- Consumes: direct command declarations, `run_process`, sanitized environment, workspace and repetition roots.

**Unhandled inputs and invariants:** Execute the snapshotted declared command, resolve cwd and input artifacts beneath allowed roots, and refuse symlinks or escapes. Execute declarations sequentially in tracked order. JSON stdout accepts exactly one top-level object with surrounding whitespace only. Preserve stdout/stderr once and reference them. A missing required input yields consumer `NOT_RUN`; missing observer input is infrastructure failure because consumers may legitimately depend on an unavailable prior artifact.

- [ ] **Step 1: Write observer tests.** Cover objective JSON fact success, plain stdout success, nonzero exit, timeout, malformed JSON, and path escape.
- [ ] **Step 2: Witness RED, implement observer execution, and witness GREEN.** Do not define a shared fact vocabulary.
- [ ] **Step 3: Write consumer tests.** Cover default and custom pass/fail exits, missing input `NOT_RUN`, unexpected exit infrastructure error, and ordered artifact arguments.
- [ ] **Step 4: Witness RED, implement consumer execution, and witness GREEN.** Ensure ordinary `FAIL` is data, not an exception.
- [ ] **Step 5: Run `uv run pytest tests/test_checks.py -q` and the current suite.** Refactor duplication only while green and record results.

### Task 8: Run artifacts, logging, versioned result, and derived summary

**Files:**
- Modify: `skill-validation/harness/src/skilltest/artifacts.py`
- Modify: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/tests/test_artifacts.py`

**Interfaces:**
- Produces: `RunPaths` and `RunResult`; `create_run(repo_root: Path, selector: str) -> RunPaths`; `write_result(paths: RunPaths, result: RunResult) -> Path`; `render_summary(result: RunResult, result_path: Path) -> str`; `configure_run_logger(run_dir: Path) -> logging.Logger`.
- Consumes: the canonical result schema in the specification and mechanical records from provider/check modules.

**Unhandled inputs and invariants:** Run IDs are UTC basic timestamp plus eight random lowercase hexadecimal characters and never depend on shared counters. Creation is exclusive. Artifact refs reject paths outside the run and use POSIX run-relative paths. Result writes atomically. Logs never include stdin, environment values, expected outcomes, or raw child output; they contain timestamp, level, phase, sanitized argv, cwd, artifact path, timing, and mechanical outcome.

- [ ] **Step 1: Write run-path and artifact-reference tests.** Assert the fixed tree, unique independent IDs, digest accuracy, relative paths, and escape rejection.
- [ ] **Step 2: Witness RED, implement paths/hashing, and witness GREEN.** Do not add retention or global logs.
- [ ] **Step 3: Write exact-schema tests.** Assert the seven top-level fields, stable repetition shape, explicit nulls, no duplicated summary, and recursive absence of semantic-verdict/adjudication fields.
- [ ] **Step 4: Witness RED, implement dataclass-to-JSON serialization and atomic write, and witness GREEN.** Use sorted, indented UTF-8 JSON with one trailing newline.
- [ ] **Step 5: Write logging and summary tests.** Assert useful stderr progress, concise stdout derived from repetitions, consumer counts, semantic-not-scored reminder, result path, and absence of seeded secrets.
- [ ] **Step 6: Complete the cycle.** Implement the fixed logger and renderer, run `uv run pytest tests/test_artifacts.py -q`, then the current suite; record results.

### Task 9: Read-only end-to-end run orchestration

**Files:**
- Create: `skill-validation/harness/src/skilltest/runner.py`
- Modify: `skill-validation/harness/src/skilltest/contracts.py`
- Create: `skill-validation/harness/tests/test_runner_readonly.py`
- Modify: `skill-validation/harness/src/skilltest/cli.py`

**Interfaces:**
- Produces: `InspectRequest`, `RunRequest`, and `Inspection`; `inspect_test(request: InspectRequest) -> Inspection`; `run_test(request: RunRequest) -> RunResult`.
- Consumes: all earlier modules; `skilltest inspect` and `skilltest run` command handlers.

**Unhandled inputs and invariants:** Validate definitions and sources before any provider launch. Invalid source composition is a usage error: exit `2` and create no run. `inspect` performs no model call and creates no run directory. `run` snapshots exact inputs before repetitions, executes repetitions sequentially and independently, and attempts every declared repetition even when an earlier one has infrastructure failure. After a provider failure, it still runs observers and any consumers whose declared inputs exist; unavailable-input consumers become `NOT_RUN`. It never retries. It never reads withheld outcomes after validation except to snapshot the plan.

- [ ] **Step 1: Write the `inspect` integration test.** Invoke the real CLI subprocess against a synthetic repo and assert selected profile, capabilities, resolved sources/digests, no fake-Codex invocation, no run directory, and no semantic decision.
- [ ] **Step 2: Witness RED, implement minimum inspect orchestration/CLI mapping, and witness GREEN.** Stdout remains machine-friendly concise text; definition errors exit `2` on stderr.
- [ ] **Step 3: Write the read-only run family.** Use a fake Codex executable with two repetitions and assert fresh workspaces, exact snapshots, captured events/final/stdout/stderr, logs, relative digests, complete result, exit `0`, and no expected-outcome leakage.
- [ ] **Step 4: Witness RED, implement sequential run orchestration and result finalization, and witness GREEN.** Retain partial artifacts when a repetition fails.
- [ ] **Step 5: Run `uv run pytest tests/test_runner_readonly.py -q` and the current suite.** Record the witnessed transitions and current test count.

### Task 10: Writable Git behavior plus observers and pass/fail consumers

**Files:**
- Create: `skill-validation/harness/tests/test_runner_writable.py`
- Modify: `skill-validation/harness/src/skilltest/runner.py`

**Interfaces:**
- Produces: end-to-end composition of workspace, provider, observer, consumer, and result modules.
- Consumes: existing public interfaces only; no new abstraction unless the test exposes a real missing seam.

**Unhandled inputs and invariants:** The fake subject edits and commits in its disposable repository. Initial/final state and observer output, not final-response claims, prove the action. Both passing and failing consumers run; ordinary failure leaves repetition and process `COMPLETED`. A failed observer or unexpected consumer exit changes mechanical status to `INFRA_ERROR` while retaining earlier artifacts.

- [ ] **Step 1: Write the writable synthetic family.** Require a real edit and commit, an observer reporting Git state, one passing consumer, one failing consumer, and one consumer reading observer output.
- [ ] **Step 2: Witness RED.** Run the focused family and confirm failure at the first missing orchestration behavior.
- [ ] **Step 3: Add only the missing orchestration.** Do not reimplement Git or consumer grammar inside the runner.
- [ ] **Step 4: Witness GREEN.** Assert exit `0`, consumer `PASS`/`FAIL`, objective evidence, snapshots, and no semantic verdict.
- [ ] **Step 5: Add and complete the observer/consumer infrastructure-error cycle.** First witness the failing test, then add only necessary result propagation; run the focused file and current suite.

### Task 11: Full infrastructure, source, and secret end-to-end matrix

**Files:**
- Create: `skill-validation/harness/tests/test_runner_failures.py`
- Modify only as failures require: `skill-validation/harness/src/skilltest/process.py`
- Modify only as failures require: `skill-validation/harness/src/skilltest/codex.py`
- Modify only as failures require: `skill-validation/harness/src/skilltest/runner.py`
- Modify only as failures require: `skill-validation/harness/src/skilltest/artifacts.py`

**Interfaces:**
- Consumes and verifies existing interfaces; produces no new framework layer.

**Unhandled inputs and invariants:** The matrix covers missing executable, nonzero CLI exit, timeout, malformed event stream, missing final response, large simultaneous stdout/stderr, normal/mixed sources, missing/escaped sources, and credential/log sanitation. Every accepted run request writes a diagnosable result and partial artifacts. Definitions rejected before a valid request exit `2` without pretending a run occurred.

- [ ] **Step 1: Add one parameterized end-to-end infrastructure matrix.** Assert expected exit, overall/repetition status, stable reason code, partial-artifact presence, and a useful runner-log phase for each case.
- [ ] **Step 2: Witness RED and fix one case at a time.** For each failing row, rerun that row, make the minimal production change, rerun it green, then run the file; do not batch speculative hardening.
- [ ] **Step 3: Add the source-composition end-to-end rows.** Cover common, mixed explicit, missing, extra, symlinked, and escaped source inputs plus exact snapshot immutability.
- [ ] **Step 4: Repeat a separate RED-GREEN cycle for each new production defect.** Keep source selection policy out of the runner.
- [ ] **Step 5: Add the secret-sentinel row.** Seed representative token, key, proxy-credential, hook, and Python-injection environment variables; the fake CLI reports visible names only. Assert forbidden names/values are absent from its environment, output artifacts, terminal streams, result, and runner log.
- [ ] **Step 6: Run `uv run pytest tests/test_runner_failures.py -q` and the full current harness suite.** Record exact results and any accepted residual edges.

### Task 12: Independent reruns and self-contained evidence promotion

**Files:**
- Create: `skill-validation/harness/src/skilltest/promotion.py`
- Create: `skill-validation/harness/tests/test_promotion.py`
- Modify: `skill-validation/harness/src/skilltest/cli.py`

**Interfaces:**
- Produces: `promote_run(repo_root: Path, run_id: str) -> Path`; `skilltest promote <run-id>`.
- Consumes: fixed run layout and result artifact references.

**Unhandled inputs and invariants:** Validate run IDs before path construction. Refuse missing, incomplete, malformed, symlinked, escaped, or already-promoted runs. Copy exact inputs, result, log, outputs, raw events, snapshots, and observer/consumer artifacts; exclude every `workspace/` and transient file. Do not overwrite, judge, add review notes, stage, or commit.

- [ ] **Step 1: Write the independent-rerun test.** Run the same selector/profile/source twice and assert distinct run IDs/workspaces with no shared state or attempt links.
- [ ] **Step 2: Witness RED only if existing orchestration violates independence.** Fix the smallest defect and rerun green; do not create a rerun command.
- [ ] **Step 3: Write promotion success and refusal tests.** Assert exact compact inventory, no workspace, refuse-overwrite behavior, and preserved run-relative result references.
- [ ] **Step 4: Witness RED, implement minimum copy/export, and witness GREEN.** Use a new destination directory and atomic rename; leave Git untouched.
- [ ] **Step 5: Delete the disposable source run inside the temporary test repository.** Revalidate every promoted artifact reference and digest, then run `uv run pytest tests/test_promotion.py -q` and the current suite.

### Task 13: Focused documentation and complete offline acceptance

**Files:**
- Create: `skill-validation/harness/README.md`
- Modify: `plans/2026-08-22-skill-validation-runner-implementation.md`
- Modify only for contract defects found by acceptance: harness source/tests above

**Interfaces:**
- Documents: uv install/run commands, fixed discovery and manifests, source grammar, three CLI commands, subject input, result/log layout, exit semantics, disposable runs, promotion, and the agent/owner review loop.

**Unhandled inputs and invariants:** Root `README.md`, `ARCHITECTURE.md`, legacy validation records, scenario migration, and hook docs remain unchanged on this branch. That documentation is deferred until real scenario migration proves the framework's durable place in the repository; updating it now would describe an unaccepted system and widen review scope.

- [ ] **Step 1: Write the focused README from the tested current contract.** Include one minimal synthetic definition example, one inspect command, one run command, one promote command, and explicit “no semantic verdict” language.
- [ ] **Step 2: Run the complete offline suite from a clean uv environment.** Use `uv sync --locked --dev` and `uv run pytest -q`; record exact totals.
- [ ] **Step 3: Exercise all three real entry points without a model.** Run help, synthetic `inspect`, fake-Codex `run`, and synthetic `promote`; capture stdout/stderr/result paths.
- [ ] **Step 4: Verify repository boundaries.** Confirm `.skilltest/runs/` is ignored, evidence is not ignored, no skill/hook/legacy files changed, no ignored cleanup evidence was touched, and no model or Claude process ran.
- [ ] **Step 5: Reconcile every plan checkbox through Task 13.** Leave unchecked anything not actually witnessed and record accepted edges beside the owning task.

### Task 14: Cold review and owner-announced real Codex smoke

**Files:**
- Modify only for test-first defects: harness source/tests/docs/plan
- Create only as ignored disposable output: `.skilltest/runs/<run-id>/...`

**Interfaces:**
- Verifies the complete runner against the spec and current official Codex CLI behavior.

**Unhandled inputs and invariants:** No live call occurs until the exact synthetic scenario, withheld plan, source bytes, profile, expected command, and anticipated token scope are shown to the owner and the owner approves the call. Use one repetition of `gpt-5.6-sol` at low effort. This is a smoke, not a campaign or behavioral baseline.

- [ ] **Step 1: Run a cold whole-branch self-review against the spec and this plan.** Check simplicity, file/interface consistency, forbidden verdict logic, source and credential safety, and all five offline synthetic families; address defects test-first.
- [ ] **Step 2: Run the required focused external review only after local review is clean.** Resolve every P0–P2 finding; retain materially better good-enough results and record P3 dispositions.
- [ ] **Step 3: Freeze and present the live-smoke inputs.** Show hashes, selector, profile, source path, exact Codex argv with prompt omitted, expected artifacts, and why one low-effort call is sufficient.
- [ ] **Step 4: Inform the owner that a model call is about to begin and obtain explicit approval.** Stop here until approved.
- [ ] **Step 5: Run exactly one Sol-low repetition.** Independently inspect raw JSONL, final output, runner log, result schema, actual workspace state, source digests, model/effort/sandbox/version metadata, and any evidence of ambient user/admin/system skill interference.
- [ ] **Step 6: Apply the gate.** If the adapter, isolation, capture, or logging contract fails, write a failing offline reproduction where possible and return to the owning task. If ambient-skill behavior cannot be made deterministic within the approved simple design, stop and amend the spec with the owner rather than layering on machinery.
- [ ] **Step 7: Rerun `uv run pytest -q` and the relevant real CLI inspection after any fix.** Record final evidence and leave the live run ignored.

### Task 15: Final owner gate, stage, commit, and push

**Files:**
- Modify: `plans/2026-08-22-skill-validation-runner-implementation.md`
- Stage only the owner-reviewed files enumerated by `git status --short`

**Interfaces:**
- Produces: one green, reviewable `feature/skill-validation-runner` branch. Does not open a PR.

**Unhandled inputs and invariants:** This task is forbidden until every prior hard gate is green and the owner reviews the final diff, offline evidence, external review, and real smoke. Ignored runs remain untracked and unstaged. Existing user changes are preserved.

- [ ] **Step 1: Present the final state.** Show branch/base, complete status/diff summary, exact tests, live smoke, review findings/dispositions, ignored run location, and every intentionally deferred area.
- [ ] **Step 2: Obtain explicit final owner approval to stage, commit, and push.** Stop here until approved.
- [ ] **Step 3: Re-read status and stage only approved runner/spec/plan/charter/doc files.** Inspect `git diff --cached` and abort on any unrelated, ignored, skill, hook, or legacy validation content.
- [ ] **Step 4: Run final verification against the staged tree.** Run `uv sync --locked --dev`, `uv run pytest -q`, the three CLI smoke commands that require no model, charter hash verification, and repository-boundary checks.
- [ ] **Step 5: Commit the green change.** Use a conventional `feat:` subject, concise area bullets, `References swept:`, and exact `Verification:` commands; do not put design rationale only in the commit body.
- [ ] **Step 6: Push the current feature branch.** Do not open a PR, merge, remove either worktree, reset, force-push, or delete ignored evidence.

## Final acceptance map

| Spec acceptance | Owning task(s) |
|---|---|
| Installable Python 3.11+ package and three commands | 1, 9, 12 |
| Fixed definitions, source handling, snapshots, digests | 2, 3 |
| Fresh read/write/Git workspaces and subject-only inputs | 4, 9, 10 |
| Bounded CLI supervision, raw capture, infrastructure classification | 5, 6, 11 |
| Objective observers and deterministic consumers without semantic verdict | 7, 10 |
| Versioned relative result, fixed logging, disposable run layout | 8, 9 |
| Five offline synthetic families | 9–12 |
| Independent reruns and self-contained promotion | 12 |
| Focused documentation and unchanged unrelated surfaces | 13 |
| Owner-announced one-call Codex smoke and isolation check | 14 |
| Final review, owner approval, staging, commit, and push | 15 |
