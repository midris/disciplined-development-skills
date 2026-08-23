# Single-run skill test runner implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` to implement this plan one task at a time. Use `superpowers:test-driven-development` for every task. Check boxes only after the implementation, focused tests, independent inspection, and task review are complete.

**Status:** Approved by the owner on 2026-08-23. Task 1 is authorized; pause for owner evaluation before Task 2.

**Goal:** Build a small CLI that reads one test configuration, prepares one unique local workspace, invokes the configured Codex or Claude Code CLI once, retains the raw result bundle, writes `result.json`, and exits.

**Architecture:** A linear orchestration function composes four focused mechanical units: strict configuration loading, run/workspace preparation, one built-in provider invocation, and result persistence. The public execution interface is identical for both providers: `provider`, `model`, and `effort`. Repetition and parallel sampling are achieved only by launching additional independent CLI processes.

**Tech stack:** Python 3.11+, standard-library production runtime, `pytest` and `jsonschema` as test-only dependencies, `uv` for the local development environment, and the installed Codex and Claude Code CLIs.

**Spec:** `plans/specs/2026-08-23-single-run-skill-test-runner-design.md`

## Branch and merge boundary

The implementation branch must be cut from the owner-approved `main` commit containing this plan and the governing spec, using a new worktree under `.worktrees/`. The five tasks below form one reviewable runner branch. Scenario migration, baselines, skill changes, evidence promotion, cleanup commands, orchestration, campaigns, hooks, and legacy-validation removal remain separate later branches.

Do not modify or remove `.worktrees/comprehensive-skill-cleanup`, `docs/comprehensive-skill-cleanup`, its remote branch, or its retained scenarios. They are future migration inputs after the runner is accepted.

## Global constraints

### Core guidance

> Build a simple, stateless, repeatable runner for one test scenario. One invocation accepts one configuration, creates one unique local environment, invokes the configured provider once, saves the raw results and workspace, writes one result record, and exits. Running again means starting another independent runner process. The runner contains no concurrency machinery and manages no state across invocations.

### Never do

- Never add internal concurrency: no worker threads, async tasks, pools, queues, schedulers, or multi-run coordination.
- Never add repetitions, retries, resume, campaigns, sampling, batching, or a multi-run command.
- Never add shared or lifecycle-managed state: no counters, indexes, databases, caches, locks, registries, latest pointers, retention state, or cleanup daemon. A unique disposable result bundle is output, not managed application state.
- Never add judgment: no semantic validation of test choices, scoring, grading, behavioral PASS/FAIL, adjudication, automatic comparison, calibration, or recommendations.
- Never add dynamic or test-specific selection policy: the runner does not choose or recommend skills, scenarios, dependencies, providers, models, or efforts. Each adapter applies one fixed, versioned set of permissions, tools, and isolation flags; it does not select them per test.
- Never expose provider mechanics as test configuration. The public execution declaration contains exactly `provider`, `model`, and `effort`; each built-in adapter owns its executable, permissions, tools, timeout, isolation flags, output mode, and parsing.
- Never add a generic workflow engine: no setup, observer, consumer, evaluator, validation, or post-run command framework.
- Never add project lifecycle behavior: no Git-state checks, repository policy, staging, commits, branches, pushes, approval tracking, or cleanup-project state.
- Never add hidden process machinery: one successful run starts only the configured provider CLI; no probes, helper processes, background supervisors, or descendant discovery.
- Never call provider APIs or SDKs directly; built-in providers invoke their respective fixed local CLI and leave authentication to that CLI.
- Never add speculative hardening for hostile same-user mutation, audit-synchronized races, or unsupported detached writers.
- Never turn the required provider boundary into a plugin system, dynamic registry, fallback chain, or provider lifecycle framework.

### Execution discipline

- Run every `uv` and pytest command below from `skill-validation/runner/` unless a step explicitly names another directory.
- Work test-first: add the focused failing test, run it and observe the intended failure, implement the minimum behavior, then rerun it and the accumulated offline suite.
- Use one implementation subagent at a time. Give it only the current task, the governing spec, and these global constraints. Parallel review is allowed; parallel implementation on the shared branch is not.
- Each task is an allowlist. Do not create or modify production files outside that task's file list. If a task cannot fit, stop for owner approval instead of widening it silently.
- If a subagent introduces forbidden machinery or materially exceeds the task, reject the task changes and restart from the clean task base. Do not salvage an off-target architecture incrementally.
- After each task, independently inspect the diff, run the focused and accumulated tests, perform a spec-compliance review, then a code-quality review. Commit locally only after both reviews are clean.
- Do not invoke a live model during Tasks 1–5. Fake executables and installed-CLI version/help checks must not spend tokens. A Codex live smoke requires an announcement and owner approval after the branch is otherwise complete. Any Claude model invocation requires fresh owner permission.
- The public configuration contains exactly `provider`, `model`, and `effort`; no task may add provider-specific configuration.
- Keep the production implementation within the specification's 300–500-line expectation. Stop for owner review before exceeding 600 production lines, 30 focused tests, five tasks, one working day, or one direct child process in a successful run.
- Keep the offline suite focused: target 15–25 collected pytest cases by exercising closely related validity and failure rows through compact table-driven tests instead of multiplying test machinery.

## File map

All new runner work lives under `skill-validation/runner/`:

- `pyproject.toml` and `uv.lock` — package metadata, `skilltest` entry point, test-only dependencies, and pytest discovery restricted to `tests/`.
- `README.md` — concise local usage, configuration, result-location, and no-judgment contract.
- `src/skilltest/__init__.py` and `src/skilltest/__main__.py` — package marker and module entry point.
- `src/skilltest/config.py` — strict JSON loading, immutable configuration records, path resolution, and preflight.
- `src/skilltest/workspace.py` — unique run allocation, retained input copies, workspace construction, and exact subject input.
- `src/skilltest/providers.py` — small request/result boundary, fixed Codex and Claude Code argument construction, one synchronous child lifecycle, and Claude final-result extraction.
- `src/skilltest/results.py` — mechanical log writing, input/artifact digests, exact result record, and atomic publication.
- `src/skilltest/runner.py` — the single linear `run_once` pipeline and infrastructure-error precedence.
- `src/skilltest/cli.py` — `skilltest run CONFIG`, diagnostics, stdout run path, and exit-code mapping.
- `result.schema.json` — executable Version 1 persisted-result contract used only by tests.
- `tests/conftest.py` — ordinary input builders and real fake CLI executables supplied through test-only `PATH`.
- `tests/test_config.py`, `tests/test_workspace.py`, `tests/test_providers.py`, `tests/test_run.py`, and `tests/test_cli.py` — focused offline contracts.
- `acceptance/test_provider_clis_installed.py` — opt-in version/help checks against installed CLIs without model invocation.

No generic utilities, base-class hierarchy, plugin package, process supervisor, campaign module, or shared-state module may be added.

---

### Task 1: Strict configuration and preflight

**Files:**

- Create: `skill-validation/runner/pyproject.toml`
- Create: `skill-validation/runner/uv.lock`
- Create: `skill-validation/runner/src/skilltest/__init__.py`
- Create: `skill-validation/runner/src/skilltest/config.py`
- Create: `skill-validation/runner/tests/conftest.py`
- Create: `skill-validation/runner/tests/test_config.py`

**Produces:** a minimal installable test project and `load_config(path: Path) -> TestConfig`, plus immutable records for the exact root, skill, scenario, and execution declarations. `TestConfig` retains the original configuration bytes and resolved input paths needed by later tasks.

**Unhandled inputs and invariants:** Reject all malformed or structurally invalid inputs listed by the spec before creating a run directory, including duplicate keys, non-finite JSON numbers, unknown keys, invalid identifiers, invalid provider declarations, missing or wrong-kind files, invalid UTF-8 prompt or `SKILL.md`, special files, duplicate skill identifiers, configuration containment, symlink escape to the configuration, fixture `supplied-skills` collision, and fixed-run-root overlap. Treat independent source roots and semantically odd but structurally valid combinations as valid. Accept the spec's trusted-input assumption about same-user mutation after preflight.

- [ ] Bootstrap only the package and test environment: create the listed directories, package marker, and a minimal `pyproject.toml` with Python 3.11+, no runtime dependency, `pytest` and `jsonschema` as development dependencies, and `testpaths = ["tests"]`; generate `uv.lock`; and confirm `uv sync --locked` succeeds. This scaffolding contains no runner behavior and is the explicit exception that makes the first RED test executable.
- [ ] Write focused configuration tests as a compact validity table covering every reject category and the execute-without-judgment cases. Include Codex and Claude configurations whose execution objects contain only `provider`, `model`, and `effort`.
- [ ] Run `uv run pytest tests/test_config.py -q` and confirm the new tests fail because the loader does not exist.
- [ ] Implement only the strict loader, immutable records, path resolution, and preflight required by those tests. Use the standard-library JSON parser with explicit duplicate-key and non-finite-number rejection. Configure pytest with `testpaths = ["tests"]` so the later installed-CLI acceptance directory is always opt-in. Do not allocate a run or invoke a process.
- [ ] Rerun `uv run pytest tests/test_config.py -q`, then `uv run pytest -q`; both must pass.
- [ ] Guardrail check: inspect the diff and confirm this task only turns one JSON file into validated mechanical input, performs no selection or judgment, and starts no child process. Record production and focused-test line counts.
- [ ] Run the task's spec-compliance and code-quality reviews. If clean, commit the allowlisted files in one local TDD commit.

### Task 2: Unique result directory and workspace preparation

**Files:**

- Create: `skill-validation/runner/src/skilltest/workspace.py`
- Create: `skill-validation/runner/tests/test_workspace.py`
- Modify: `skill-validation/runner/tests/conftest.py`

**Consumes:** `TestConfig` from Task 1.

**Produces:** `create_run(config: TestConfig) -> RunContext` and `prepare_workspace(context: RunContext, config: TestConfig) -> PreparedRun`. The records expose only the fixed paths and timestamps later tasks require.

**Unhandled inputs and invariants:** Use the fixed `${TMPDIR}/skilltest-runs/` parent and atomic unique-directory creation; never scan existing runs. Create the exact retained layout and marker, copy declared inputs before preparing the workspace, preserve ordinary symlinks and bytes, copy fixture contents into the workspace root, and put every supplied skill under `workspace/supplied-skills/<id>/`. Build the exact five-line preamble and append the prompt bytes without another separator. Keep the original configuration and expected outcome out of provider-visible files until after the provider attempt. Allocation failure before ownership produces no bundle; copy failure after allocation leaves the owned bundle for later error recording.

- [ ] Write focused tests for two distinct serial directories, empty and populated fixtures, ordered dependency copies, symlink preservation, the exact retained layout, exact subject-input bytes, and absence of configuration/expected-outcome bytes from runner-added provider-visible material.
- [ ] Run `uv run pytest tests/test_workspace.py -q` and confirm failure because preparation is absent.
- [ ] Implement only unique allocation, retained copies, workspace preparation, and subject-input construction. Do not invoke providers, publish results, add cleanup, or inspect Git.
- [ ] Rerun `uv run pytest tests/test_workspace.py -q`, then `uv run pytest -q`; both must pass.
- [ ] Guardrail check: confirm one call creates one unique owned directory and one workspace without counters, locks, registries, retries, rollback machinery, or concurrency. Record cumulative line counts.
- [ ] Run the task's spec-compliance and code-quality reviews. If clean, commit the allowlisted files in one local TDD commit.

### Task 3: Fixed built-in provider invocation

**Files:**

- Create: `skill-validation/runner/src/skilltest/providers.py`
- Create: `skill-validation/runner/tests/test_providers.py`
- Modify: `skill-validation/runner/tests/conftest.py`

**Consumes:** prepared workspace, subject-input bytes, the final-output path, and the exact `provider`, `model`, and `effort` values.

**Produces:** plain `ProviderRequest` and `ProviderResult` records and `invoke_provider(request: ProviderRequest) -> ProviderResult`. `ProviderResult` carries raw stdout and stderr bytes for Task 4 to persist exactly once; provider-specific final-output handling remains inside the built-in adapter.

**Unhandled inputs and invariants:** Implement exactly two built-in branches, `codex` and `claude`; unknown providers are unreachable after Task 1 validation and still fail mechanically if passed internally. Use one shell-free synchronous child process, inherited authentication environment, workspace working directory, fixed 900-second timeout, five-second terminate grace, and no probes or descendant supervision. Pin the exact argument order from the spec. Codex requires its output-last-message file after exit zero. Claude preserves raw JSONL and requires the final non-empty object to be a string-valued result event. Classify missing executable, nonzero exit, timeout, missing Codex final output, malformed Claude JSONL, missing/nonterminal Claude result, and non-string Claude result mechanically. Detached writers and external interruption remain accepted unsupported edges.

- [ ] Create real fake `codex` and `claude` executables that record argv, cwd, stdin, and selected environment facts, then write controlled stdout, stderr, final output, exit codes, and delays. Tests must cross the real subprocess boundary; do not mock it.
- [ ] Write focused provider tests for exact argv/stdin/cwd, provider/model/effort pass-through, stdout/stderr byte capture, success, launch failure, nonzero exit, timeout, Codex missing final output, and every specified Claude-output error. Timeout tests may monkeypatch the adapter's fixed timeout and grace constants; no timeout field may enter configuration or a production call signature.
- [ ] Run `uv run pytest tests/test_providers.py -q` and confirm failure because invocation is absent.
- [ ] Implement the minimum provider boundary and two fixed branches. Provider-specific executable, permissions, tools, timeout, isolation, output mode, and parsing remain constants, never configuration.
- [ ] Rerun `uv run pytest tests/test_providers.py -q`, then `uv run pytest -q`; both must pass.
- [ ] Guardrail check: confirm one successful call starts exactly one direct child, with no adapter registry, plugin discovery, APIs, SDKs, retries, helper probes, background workers, or configurable provider options. Record cumulative line counts.
- [ ] Run the task's spec-compliance and code-quality reviews. If clean, commit the allowlisted files in one local TDD commit.

### Task 4: Linear run orchestration and persisted result

**Files:**

- Create: `skill-validation/runner/result.schema.json`
- Create: `skill-validation/runner/src/skilltest/results.py`
- Create: `skill-validation/runner/src/skilltest/runner.py`
- Create: `skill-validation/runner/tests/test_run.py`
- Modify: `skill-validation/runner/tests/conftest.py`

**Consumes:** the exact Task 1–3 interfaces.

**Produces:** `run_once(config_path: Path) -> RunOutcome`, where `RunOutcome` contains the mechanical exit code, optional owned run path, and nullable mechanical diagnostic for the CLI to mirror to stderr. It performs the specification's pipeline once and never loops.

**Unhandled inputs and invariants:** Write raw stdout and stderr exactly once, preserve the live workspace, write the original configuration bytes only after the provider attempt or a preparation failure, and publish `result.json` last by atomic replacement. Implement the exact result schema, digest ordering, status vocabulary, error codes, and first-applicable error precedence. A result-write failure cannot describe itself: Task 4 records it in `runner.log` and returns it in `RunOutcome.diagnostic`; Task 5 mirrors that diagnostic to stderr without writing the log. A required-artifact write failure after launch is infrastructure failure. Never interpret provider content semantically.

- [ ] Write integration tests that drive `run_once` through real fake executables for completed Codex and Claude runs and each persisted infrastructure-error class. Validate every generated result with `result.schema.json`, verify input/artifact digests, and prove the original configuration appears only after the provider attempt. To reproduce post-allocation preparation and post-launch artifact-write failures, tests may narrowly monkeypatch the specific standard-library copy or write call; do not add a production injection seam, concurrent mutator, or filesystem framework.
- [ ] Run `uv run pytest tests/test_run.py -q` and confirm failure because orchestration and result persistence are absent.
- [ ] Implement the chronological runner log, digest/result construction, atomic publication, and a straight-line `run_once` composition of Tasks 1–3. Do not add callbacks, hooks, command lists, cleanup, comparison, or retry paths.
- [ ] Rerun `uv run pytest tests/test_run.py -q`, then `uv run pytest -q`; both must pass.
- [ ] Guardrail check: trace one successful call and prove it has one configuration load, one allocation, one preparation, one provider call, one result publication, and one return. Record cumulative line counts.
- [ ] Run the task's spec-compliance and code-quality reviews. If clean, commit the allowlisted files in one local TDD commit.

### Task 5: CLI, independence acceptance, and operator documentation

**Files:**

- Create: `skill-validation/runner/src/skilltest/cli.py`
- Create: `skill-validation/runner/src/skilltest/__main__.py`
- Create: `skill-validation/runner/tests/test_cli.py`
- Create: `skill-validation/runner/acceptance/test_provider_clis_installed.py`
- Create: `skill-validation/runner/README.md`
- Modify: `skill-validation/runner/pyproject.toml`
- Modify: `skill-validation/runner/uv.lock`
- Modify: `skill-validation/runner/tests/conftest.py`

**Consumes:** `run_once` and `RunOutcome` from Task 4.

**Produces:** the sole public command `skilltest run CONFIG` with exit codes `0`, `1`, and `2`; one final stdout run path after any normal exit that owns a directory; and concise stderr diagnostics.

**Unhandled inputs and invariants:** CLI misuse and invalid configuration exit `2` without a run. Fixed-root or unique-directory allocation failure exits `1` without stdout because no bundle exists. Normal exits after allocation print the absolute bundle path once. External interruption retains operating-system/Python defaults. Serial reruns and simultaneous external CLI processes must produce distinct independent bundles; the production runner remains unaware of either relationship.

- [ ] Write CLI tests for exact command shape, usage errors, exit mapping, stdout/stderr rules, two serial runs, and two simultaneously launched external `skilltest` processes using fake providers. Assert that production code contains no repetition or concurrency entry point.
- [ ] Run `uv run pytest tests/test_cli.py -q` and confirm failure because the CLI is absent.
- [ ] Implement only the thin argument parser and entry points around `run_once`; add the `skilltest` project script. Write the README around the exact three-field execution interface, disposable bundle location, rerun command, and human/agent judgment boundary.
- [ ] Rerun `uv run pytest tests/test_cli.py -q`, then the complete offline suite with `uv run pytest -q`; both must pass.
- [ ] Add opt-in installed-CLI checks that use only version and help commands to verify the targeted executable versions and required flag availability or placement; exact inference argv and stdin remain owned by the fake-executable tests. The checks must fail when an executable or required flag is absent and must be incapable of invoking a model. Verify `uv run pytest --collect-only -q` contains no acceptance test, then run them explicitly with `uv run pytest acceptance/test_provider_clis_installed.py -q` and record versions and results.
- [ ] Perform the final size and architecture audit: count production lines and focused tests; inspect process launch sites; search for concurrency, repetition, retry, judgment, Git-state, workflow, plugin, API, SDK, and shared-state machinery; and map every spec acceptance bullet to fresh evidence.
- [ ] Guardrail check: prove `skilltest run CONFIG` is the only production operation and each process owns exactly one scenario, workspace, provider call, result bundle, and exit.
- [ ] Run a final spec-compliance review and code-quality review over the entire branch. If clean, commit the allowlisted files in one local TDD commit.

## Final owner gates

After Task 5 is committed and all offline and installed-CLI version/help checks are fresh:

- [ ] Announce the proposed Codex Sol-low smoke, including the exact synthetic configuration and expected model cost, and obtain owner approval before invoking it.
- [ ] Run one approved Codex Sol-low smoke, inspect the bundle independently, and record the command and bundle path in an ignored local approval note. Do not promote, stage, or commit the run bundle.
- [ ] Present the implementation diff, test counts, size audit, installed-CLI checks, live-smoke result, and any accepted limitations for final owner approval.
- [ ] Only after final owner approval, push the implementation branch. Do not open a PR, merge, remove its worktree, or begin scenario migration in the same step.

## Plan acceptance check

Before implementation begins, verify that implementing only this plan yields exactly:

```text
read one test config
→ create one unique run directory
→ prepare one workspace
→ invoke Codex or Claude Code once
→ retain raw outputs and final workspace
→ write result.json
→ exit
```

If any task cannot be explained as a necessary part of that sequence, remove it or obtain an owner-approved spec amendment before implementation.
