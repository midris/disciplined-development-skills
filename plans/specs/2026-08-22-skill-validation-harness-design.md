# Skill validation runner — design

## Status

Design approved by the owner on 2026-08-22.
This specification records the settled runner contract.
It does not itself authorize implementation, branch creation, worktree creation, model execution, scenario migration, or skill edits; the approved implementation plan governs local commits and publication gates.

## Purpose

Build a small, stateless command-line runner that makes skill tests predictable without trying to replace agent or human judgment.

The runner prepares a declared scenario, supplies the selected skill bytes, invokes the configured model CLI, captures what happened, runs any declared objective checks, and writes one consistent result bundle.
It then stops.

A smart agent reads the result and the evaluator-withheld expected outcomes, discusses the evidence with the owner, and decides what to do next.
The runner facilitates that loop but does not decide whether semantic skill behavior passed.

The governing principle is **dumb tools for smart agents**: deterministic mechanics belong in the tool; interpretation and adaptation remain with the agent and owner.

## Semantic foundation

The approved charter and invariant inventory at `skill-validation/charter/core-contracts.md` is the semantic foundation.
Its accepted source was the file at `/Users/simon/work/personal/disciplined-development-skills/.worktrees/comprehensive-skill-cleanup/skill-validation/core-contracts.md`, including that worktree's intentionally uncommitted cleanup edits; source and canonical copy are 16,870 bytes with SHA-256 `4d172cfbcda96883a4ebc5fec6462e81545de9b862921f39de69f18eceb74aae`.
The similarly named file in the `docs/comprehensive-skill-cleanup` branch object is not the accepted byte source and must not be substituted.
The runner branch inherits those approved bytes from `main` without reopening or rewriting them.

The charter separates five result ledgers:

- core behavior;
- deterministic protocol;
- task or fixture fidelity;
- readability;
- infrastructure.

Core-behavior failures block skill acceptance when the agent and owner adjudicate them.
Deterministic-protocol failures block only when exactness is backed by an authenticated renderer, validator, production consumer, chartered deterministic interface, or exact user-supplied literal or schema.
Task or fixture fidelity does not block unless it prevents behavioral judgment, in which case the scenario is invalid rather than a skill failure.
Readability remains a separate quality result.
Infrastructure failures remain outside the behavioral denominator.

A response can prove action selection but cannot by itself prove that searching, editing, verification, committing, delegation, or a review lifecycle occurred.
Claims about performed work require runner-observed events, state, or objective observer output.

## Responsibility boundary

The authority chain is:

```text
Charter
  -> test plan and expected outcomes
  -> runner preparation, execution, and captured facts
  -> agent review
  -> owner decision
```

The charter owns skill purpose and observable invariants.
The scenario owns neutral subject-visible setup.
The test plan owns the skill under test, expected outcomes, evidence requirements, execution configuration, and legitimate deterministic checks.
The run request supplies concrete source bytes and selects an execution profile.
The runner owns deterministic preparation, invocation, capture, logging, and result formatting.
The agent and owner own semantic interpretation and acceptance.

This specification owns externally observable runner behavior and formats: tracked definitions, source selection, subject input, provider invocation, results, logging, CLI behavior, and promotion.
The implementation plan owns sequencing and internal mechanics that do not alter those surfaces, including the run-identifier construction, child-environment allowlist, disposable Git identity, and copied-file mode normalization.
Keeping those mechanics in the plan avoids turning implementation detail into public API; any such choice that later changes subject behavior or a persisted result must first be promoted into this specification.

The runner does not:

- issue an overall semantic PASS or FAIL;
- invoke or manage an advisory judge;
- manage owner adjudication;
- maintain plan approval, calibration, or acceptance state;
- decide whether a baseline, candidate, mixed, or pinned dependency bundle is conceptually appropriate;
- diagnose a skill wording defect from a behavioral result;
- stage, commit, or publish project or evidence changes; disposable workspace initialization may create the scenario's declared initial Git commit.

## Tracked definitions

### Charter

The charter is independent of runner implementation.
It contains skill purpose and observable invariants, not fixture mechanics or runner policy.

### Scenario package

A scenario package contains neutral setup material:

- a stable scenario identifier and description;
- the subject-visible prompt;
- fixture files or initial repository state;
- required capabilities;
- optional tracked observer commands or scripts.

The scenario does not define success, blocking status, model configuration, repetition policy, or a verdict.
Observers report objective facts rather than interpreting skill behavior.

Version 1 discovers a scenario at `skill-validation/scenarios/<skill>/<scenario>/scenario.yaml`.
A selector and both of its segments match `<skill>/<scenario>` and `[a-z0-9][a-z0-9-]*` respectively.
The manifest contains exactly `schema_version: 1`, `id`, `description`, `prompt`, `workspace`, `required_capabilities`, and `observers`:

- `prompt` names one non-empty UTF-8 file contained in the scenario directory;
- `workspace.fixture` is `null` or a contained directory copied into every fresh workspace;
- `workspace.git` is a boolean requesting an initialized disposable Git repository;
- `required_capabilities` is an ordered, duplicate-free subset of `read`, `write`, `git`, and `web-search`;
- `observers` is an ordered list of direct command declarations.

### Test plan

A test plan binds a scenario to:

- the primary skill under test;
- any supplied dependency skills;
- the owning charter invariants;
- named execution profiles;
- human-readable expected outcomes;
- the evidence an agent needs to review each outcome;
- any legitimate deterministic checks or consumers.

Expected outcomes are withheld from the subject invocation.
They may distinguish behavioral, deterministic-protocol, fidelity, readability, and diagnostic observations without combining them into one score.

Each expected outcome records only what is needed to review it:

- stable identifier;
- owning skill and invariant when charter-owned;
- ledger;
- proof scope: `selection` or `executed`;
- readable expected condition;
- required evidence;
- evaluability conditions;
- exactness basis and real consumer when deterministic exactness applies.

The runner validates this structure but does not evaluate semantic conditions.

Version 1 discovers the withheld plan at `skill-validation/plans/<skill>/<scenario>.yaml`.
It contains exactly `schema_version: 1`, `id`, `skill`, `scenario`, `dependencies`, `profiles`, `expected_outcomes`, and `consumers`:

- `id` equals the selector, `scenario` equals the paired scenario identifier, and `skill` equals the selector's first segment;
- `dependencies` is an ordered, duplicate-free list of skill identifiers excluding the primary skill;
- `profiles` is a non-empty mapping;
- `expected_outcomes` contains exactly `id`, `owner`, `invariant`, `ledger`, `proof`, `condition`, `evidence`, `evaluable_when`, `exactness_basis`, and `consumer` per item;
- ledgers are `behavior`, `protocol`, `fidelity`, `readability`, or `infrastructure`, and proof is `selection` or `executed`;
- nullable outcome fields are accepted only when their ledger and outcome do not require them; a protocol outcome requires a non-empty exactness basis and a declared real consumer;
- `consumers` is an ordered list of direct command declarations.

### Execution profiles

A named profile supplies provider, model, reasoning effort, repetitions, timeout, and workspace capability policy.
Profile names have no runner-defined semantics.
The plan author chooses stable descriptive names; the CLI requires a profile when more than one exists and may select the sole profile automatically.

Every version 1 profile contains exactly `provider`, `model`, `effort`, `repetitions`, `timeout_seconds`, and `sandbox`.
Version 1 accepts provider `codex`, a non-empty model and effort, positive integer repetitions, a positive timeout, and sandbox `read-only` or `workspace-write`.
Full-access execution is excluded until an accepted scenario proves it necessary.

Capability consistency is a definition-level invariant across every declared profile, not only the selected profile.
`read` is always available; `write` requires every profile to use `workspace-write`; `git` requires `workspace.git`; and `web-search` causes every Codex invocation to include the global `--search` flag.
A plan containing any profile that cannot run its paired scenario is rejected during discovery, even if another profile would satisfy the scenario.
This keeps every tracked profile independently executable and prevents selection from hiding a defective plan.

The initial implementation uses the Codex CLI.
The runner boundary is thin and provider-neutral from the start so a later Claude Code CLI adapter can consume the same scenario, plan, source, logging, and result contracts.
No direct provider API integration is in scope.

## Source handling

Source composition is run input, not runner policy.

For the common case, the run request supplies one repository or worktree root and the runner resolves every declared skill from it.
For a mixed or pinned test bundle, the request may supply an explicit source map from skill identifiers to repository-relative files or allowed roots.

The version 1 CLI grammar is deliberately small:

- `--source PATH` supplies one common repository or worktree root; each declared skill resolves as `PATH/skills/<skill>/SKILL.md`;
- repeatable `--source SKILL=PATH` supplies explicit `SKILL.md` files for the primary and every dependency;
- common-root and explicit-map forms cannot be mixed;
- explicit-map mode requires exactly the declared skill set, with no omissions or extras;
- `run` requires a source; `inspect` may omit it to validate definitions and profile selection only.

The runner mechanically:

- resolves every declared skill and dependency;
- rejects missing inputs and path escapes;
- copies the selected bytes into the disposable scenario workspace;
- records source paths, repository state, and content digests;
- exposes the resolved source inventory in the result.

It does not judge whether the tester should have chosen a different source mixture.

## Subject input envelope

Each repetition copies the snapshotted primary and dependency skills to `supplied-skills/<skill>/SKILL.md` beneath its workspace.
That location is intentionally outside provider auto-discovery so the run does not depend on installed project skills.

The runner constructs one UTF-8 subject input from this fixed five-line preamble followed immediately by the scenario prompt bytes:

```text
For skill instructions, use only the supplied files listed below.
Primary: <primary-skill> — supplied-skills/<primary-skill>/SKILL.md
Dependencies: <dependencies>
Read those files before acting.
Scenario follows:
```

The primary identifier comes from the test plan.
`<dependencies>` is the literal `none` when the plan declares none; otherwise it is each `skill — supplied-skills/<skill>/SKILL.md` entry joined by `; ` in plan declaration order.
The preamble uses LF line endings and ends with one LF after `Scenario follows:`; the runner then appends the scenario prompt file's exact bytes without trimming, newline normalization, or an inserted separator.
Expected outcomes, consumers, profile names, and evaluator guidance never enter subject input.
The complete constructed input is captured and digested with the run so behavioral changes caused by envelope drift remain visible.

## Execution

Each `run` invocation is independent and stateless.
It creates a new run directory, performs the selected profile, writes its result, and exits.
Running the same test again means invoking `run` again; there are no retry counters, resume state, linked attempts, or automatic reruns.

For every declared repetition, the runner:

1. validates the definition and requested sources;
2. creates a fresh disposable workspace or micro-repository;
3. materializes the scenario and selected skill bundle;
4. records initial state required by the plan;
5. invokes the model CLI in a fresh ephemeral session;
6. captures raw events, final response, standard output, and standard error;
7. records final state and runs declared observers;
8. invokes declared deterministic consumers over their exact input artifacts;
9. writes the repetition facts into the run result.

The first Codex adapter invokes this ordered argument contract without a shell:

```text
codex
  --ask-for-approval never
  [--search]
  --cd <workspace>
  exec
  --strict-config
  --ignore-user-config
  --ignore-rules
  --ephemeral
  --json
  --color never
  --model <model>
  -c
  model_reasoning_effort="<effort>"
  --sandbox <sandbox>
  --output-last-message <final-message-path>
  -
```

`--ask-for-approval`, optional `--search`, and the chosen deterministic placement of `--cd` are global flags and precede `exec`.
The remaining flags are `exec` arguments.
Reasoning effort is not a first-class `exec` flag: the adapter encodes it as the documented Codex configuration key through `-c`.
The exact argv element after `-c` is `model_reasoning_effort="<effort>"`; the double quotes around the TOML string value are part of that element, and no single-quote characters are present.
`--search` appears only when the scenario declares `web-search`.
The final `-` makes the complete subject input arrive on standard input rather than in argv; JSONL events remain on stdout and the final response is also written to its separate artifact.

The runner uses argument lists without a shell, drains stdout and stderr concurrently, enforces a positive timeout, forwards interruption signals, terminates with a bounded grace period, and escalates termination if necessary.
The existing disciplined-development external-review runner is prior art for subprocess lifecycle and offline stub-CLI tests only; its prompt, verdict, severity, gate, cadence, and review-log behavior are not reused.

## Objective observers and consumers

Observers and deterministic consumers share one small subprocess primitive.
Each declaration contains exactly `id`, `command`, `argv`, `cwd`, `inputs`, `timeout_seconds`, and `json_stdout`; consumers additionally contain distinct integer `pass_exit` and `fail_exit`, normally `0` and `1`:

- `command` is one executable regular file contained beneath the declaring manifest's directory, included in the exact definition snapshot, and invoked from that snapshot;
- `argv` is an ordered list of non-empty strings passed after the snapshotted command path without a shell;
- `cwd` is contained beneath the repetition workspace, normally `.`;
- `inputs` is an ordered list of repetition-relative artifact paths appended as resolved absolute argv values after containment and existence checks;
- `timeout_seconds` is positive and `json_stdout` is boolean.

Commands are declared directly in tracked scenario or plan files; there is no discovery, registration, callback, import, or plugin mechanism.
The runner always captures exit code, stdout, stderr, timing, and digests.
When a command declares JSON output, stdout must contain exactly one UTF-8 JSON object and diagnostics go to stderr.
The runner validates only that top-level object shape and stores the stdout artifact once; it imposes no shared fact vocabulary.

An observer exits `0` after reporting its facts; any other exit is an infrastructure error.
A deterministic consumer declares pass and fail exit codes, defaulting to `0` and `1`.
Those exits produce deterministic `PASS` and `FAIL`; any other exit is an infrastructure error.
`NOT_RUN` is reserved for a consumer whose required prior artifact was unavailable.

Their semantic roles remain distinct.
An observer reports state such as files, searches, Git status, commits, diffs, or ordering visible in captured events.
A deterministic consumer authenticates an exact protocol requirement.

The runner does not provide a plugin framework, semantic observer API, workflow DSL, or comprehensive cross-provider event translation layer.
It retains raw provider events and normalizes only the small set of facts a declared observer actually emits.
The runner invokes real consumers rather than reimplementing their grammar.

Subject-authored markers, summaries, hashes, or attestations cannot independently prove that an action occurred.

## Result and logging contract

Every invocation writes beneath the consistent Git-ignored root `.skilltest/runs/`:

```text
.skilltest/runs/<run-id>/
  result.json
  runner.log
  inputs/
    definitions/
    skills/
  repetitions/
    001/
      subject-input.txt
      final.txt
      events.jsonl
      stdout.txt
      stderr.txt
      facts/
      snapshots/
      workspace/
```

At run start, `inputs/` receives the exact resolved definition and supplied skill bytes used to materialize repetitions.
This compact snapshot is separate from disposable workspaces so later inspection or promotion never rereads potentially changed source files.

The exact child artifacts are present only when applicable, but `result.json` has one stable versioned schema.
It is an index rather than a second copy of captured bytes.
Version 1 has exactly seven top-level fields:

- `schema_version`;
- `run_id`;
- overall mechanical `status`;
- `timing`;
- `test`, containing skill, scenario, and selected profile identifiers;
- `inputs`, a uniform inventory of exact definitions and supplied skills with origin, snapshot path, and digest;
- `repetitions`.

`status` is `COMPLETED` only when every requested repetition completes mechanically; otherwise it is `INFRA_ERROR`.
`timing` contains UTC `started_at`, `finished_at`, and non-negative `duration_seconds`.
`test` contains `skill`, `scenario`, and selected `profile`.
`inputs` is an ordered array whose items contain exactly `kind`, `id`, `origin`, `snapshot`, `sha256`, and nullable `repository`; repository state contains `root`, nullable `head`, and `dirty`.

Each repetition contains exactly `index`, `status`, `timing`, `execution`, nullable `infrastructure_error`, `artifacts`, `observers`, and `consumers`.
Execution contains `provider`, `model`, `effort`, `sandbox`, `timeout_seconds`, `cli_path`, and `cli_version`.
Artifacts reference the exact subject input, provider final response and streams, raw events, workspace snapshots, and declared observer or consumer outputs where applicable.
Every artifact reference is `null` or contains only run-relative `path` and `sha256`; a missing inapplicable artifact is `null` rather than omitted ambiguously.
Initial and final workspace snapshots live under `snapshots/<phase>/files/`; `snapshots/<phase>/manifest.json` records relative path, mode, and digest, and `.git/` is excluded because declared observers own Git history and state evidence.
Observer and consumer arrays contain entries with identifier, mechanical status, exit code, timing, and stdout, stderr, and fact artifact references.
Consumers may report deterministic `PASS`, `FAIL`, or `NOT_RUN`; consumer `FAIL` does not change repetition or process status.
Semantic verdict, behavioral pass, aggregate score, and adjudication fields are forbidden.

All paths to captured artifacts are relative to the run directory so a run remains movable and promotable.
The result contains no duplicated summary object.
The terminal run summary derives its counts from repetition records; `inspect` reports only the definitions, profile, capabilities, and optional sources it resolves before any run exists.

The runner writes a simple per-run log at the fixed relative path `.skilltest/runs/<run-id>/runner.log` with timestamps, levels, phases, sanitized commands, working directories, artifact paths, timings, and infrastructure outcomes.
Useful progress is mirrored to stderr while the run is active.
Stdout is reserved for the final concise summary and result path so an agent or script can consume it predictably.
Raw provider JSONL remains separate.
Secrets and credential values are never logged.
There is no global log, log rotation, external logging service, configurable logging backend, or logging plugin.

The process outcome is `COMPLETED` or `INFRA_ERROR`.
An infrastructure error records a reason such as missing executable, spawn error, timeout, interruption, nonzero model-CLI exit, malformed event stream, or missing final response.
Partial artifacts are retained and indexed when possible.

The command exits nonzero only when the runner cannot complete its mechanical contract.
A model response that semantically fails an expected outcome is still a completed run.
A deterministic consumer's ordinary validation failure is a test result; inability to invoke the declared consumer is an infrastructure error.
`run` returns `0` for `COMPLETED`, including ordinary consumer failures; `1` for recorded infrastructure failure; and `2` for CLI usage or definition errors preventing a valid run request.

Working-run directories are disposable and safe to delete.
No tracked definition or evidence artifact may contain a live dependency on a working-run path.
The first version has no cleanup, pruning, database, or retention machinery.

On completion, the terminal prints only a concise derived summary: run identifier, test selector, profile and effective model settings, completed versus infrastructure-failed repetitions, deterministic-consumer counts, an explicit reminder that semantic outcomes were not scored, and the `result.json` path.

## CLI

The initial user-facing surface is:

```text
skilltest inspect <skill>/<scenario> [--source ...] [--profile ...]
skilltest run <skill>/<scenario> --source ... [--profile ...]
skilltest promote <run-id>
```

`inspect` validates and resolves definitions and profile selection and, when supplied, sources; it does not materialize a workspace, invoke a model, or create a run directory.
`run` performs one independent test invocation and prints the result directory and concise infrastructure summary.
`promote` is a small copy/export utility, not a judgment system.

Re-running requires no special command or state: invoke `run` again with the same inputs.

## Evidence promotion

Ordinary runs remain ignored and uncommitted.
When an agent and owner decide a run contains durable value, `promote` copies a compact, self-contained record beneath `skill-validation/evidence/`.

Promotion copies the result manifest, logs, repetition outputs, raw events, observer and consumer results, definition bytes, and supplied skill bytes.
It excludes disposable workspaces and transient process files.
The agent or owner may add a separate review note to the promoted evidence.

Promotion does not choose valuable findings, issue a verdict, stage files, or commit them.
Git provides durable history after the owner reviews and commits the promoted directory.

## Model schedule and test-plan development

The adaptive schedule is operating guidance for the agent and owner, not runner state or policy.

- During scenario and plan authoring, use no model calls for fixture, observer, and consumer tests.
- When structurally ready, run one Sol-low subject invocation.
- Once the scenario and expected outcomes appear sound, collect three fresh Sol-low repetitions.
- Expand to five only when the results split or expose ambiguity.
- After stable low results, run one Sol-high confirmation.
- If high differs materially, inspect the difference and expand only when useful.

The agent and owner calibrate expected outcomes against known-positive, known-negative, and unevaluable evidence outside the runner.
Git-tracked plan review and promoted evidence record the accepted result; the runner maintains no draft, calibrated, approved, or acceptance state.

## Repository layout

```text
skill-validation/
  charter/              # approved semantic contracts
  harness/              # Python package, schema, and runner tests
  scenarios/            # neutral scenario packages
  plans/                # evaluator-withheld expected outcomes and execution profiles
  evidence/             # selected tracked evidence

.skilltest/
  runs/                  # ignored disposable results
```

Discovery follows convention rather than configurable paths.
The runner resolves the Git repository root and scans only `skill-validation/scenarios/` and `skill-validation/plans/`.
Manifests declare stable identifiers.
Discovery rejects duplicate identifiers, missing references, and path escapes.

Existing root-level validation material remains in place while it is reviewed.
New framework artifacts go only into the named directories.
Do not move obsolete material merely to classify it.

## Python packaging

The runner is a standard Python 3.11-or-newer package rooted at `skill-validation/harness/` with a `pyproject.toml`, `src/skilltest/` package, `tests/`, and a `skilltest` console entry point.
Development uses the locally available `uv` workflow and a generated lockfile; the package remains installable through standard Python packaging tools.

The implementation uses the standard library for argument parsing, subprocess supervision, files, hashing, JSON, logging, and structural validation.
PyYAML is the only runtime dependency because tracked definitions are human-authored YAML.
Pytest is a development-only dependency, consistent with existing repository tests.

The package, `inspect`, `promote`, and the self-contained offline suite do not require an installed model CLI.
`run` requires a compatible Codex CLI on `PATH`; a live invocation also requires working Codex authentication.
Acceptance therefore keeps two checks separate: the default offline pytest suite uses a controlled fake executable, while a no-model local integration check invokes the installed CLI with `--help` and `--version` to authenticate its argv grammar.
That local integration check requires no authentication or network access but is a required acceptance-environment prerequisite rather than part of the default pytest suite.

Do not add Click, Typer, Pydantic, a JSON Schema library, Rich, a database package, or a plugin framework without a demonstrated need.

## Runner tests and implementation discipline

Runner implementation follows strict test-driven development.
The implementation plan must divide work into small red-green-refactor slices: write one minimal behavioral test, run it and confirm that it fails for the expected missing behavior, add only enough production code to pass, rerun the focused and relevant broader tests, then refactor only while green.
Production behavior must not be written before its failing test.
A bug found during implementation or later use first receives a reproducing failing test.

Tests exercise real runner code, real disposable directories and Git repositories, and real subprocess boundaries.
Small fake model-CLI executables are appropriate controlled dependencies because they exercise the actual process supervisor without spending tokens; do not mock the runner's own filesystem, subprocess, or result-writing behavior merely to make tests easier.

Before migrating a real skill scenario, the self-contained offline suite must cover five synthetic mechanical families:

1. A read-only happy path with fresh repetitions, captured CLI artifacts, logs, relative paths, digests, and a completed result.
2. A writable disposable Git repository with an observed edit/commit plus passing and failing deterministic consumers, proving that consumer failure is a recorded test result rather than a runner failure.
3. Infrastructure failures covering missing executable, nonzero model-CLI exit, timeout, malformed event stream, missing final response, and pipe-sized stdout/stderr pressure without hangs or lost diagnostics.
4. Normal and mixed source resolution, exact input snapshots, missing-source and path-escape rejection, child credential sanitation, and absence of secret values from outputs and logs.
5. Two independent invocations of the same test plus promotion of one run, proving there is no shared run state and that promoted evidence remains self-contained after the disposable run is deleted.

Assertions target the versioned schema and observable relationships rather than full golden files containing timestamps, durations, or generated identifiers.

## Branch and migration sequence

After this design and its implementation plan receive owner approval, create a fresh feature branch and worktree from current `main`.
Do not build the runner on the comprehensive-cleanup branch.

The work proceeds as follows:

1. Build and verify the stateless Codex runner with synthetic mechanical cases.
2. Review every existing scenario with the owner, retiring, merging, or porting it deliberately.
3. Run accepted plans against exact `main` skill bytes to establish the Codex baseline.
4. Run the same plans against comprehensive-cleanup skill bytes and decide what work survives.
5. Clean up and sharpen skills using the accepted plans and evidence.
6. After the Codex portfolio is reliable, add the Claude Code CLI adapter and compare behavior across models.
7. Separately, modernize the unrelated dumb reminder hooks for current Claude Code and Codex behavior.
8. Remove obsolete validation machinery and results, then update `README.md`, `ARCHITECTURE.md`, applicable project instructions, and focused validation documentation.

Real Claude execution still requires fresh owner permission at that later phase.
Hook testing and hook behavior are outside this runner's scope.

## Explicit non-goals

- semantic scoring or automated prose-equivalence judgment;
- advisory-judge or owner-adjudication workflows;
- plan approval, calibration, or campaign state;
- retry, resume, or orchestration state;
- run groups, databases, dashboards, or hosted services;
- semantic ASTs, ontologies, embeddings, or gold responses;
- plugin systems or general observer frameworks;
- universal workflow or gate state machines;
- comprehensive provider-event normalization;
- exact command strings, predicted commit identifiers, or cryptographic attestation;
- automatic cleanup, evidence selection, staging, or committing;
- hook testing or hook behavior.

## Acceptance criteria

The design is complete when the owner confirms this specification matches the dumb-runner-for-smart-agents boundary and a fresh implementation agent can identify the runner's inputs, outputs, logging, error behavior, and non-goals without inventing policy.

Runner implementation is complete when:

- a clean Python environment can install and invoke the `skilltest` entry point through the documented `uv` workflow without requiring Codex for non-`run` commands;
- `inspect`, `run`, and `promote` satisfy their documented contracts;
- every production behavior was developed through a witnessed red-green-refactor cycle;
- the complete self-contained offline suite passes, including all five synthetic mechanical families, and the separate installed-Codex parser check passes in the acceptance environment;
- `.skilltest/runs/` is ignored and disposable and promoted evidence has no dependency on it;
- every `result.json` satisfies the versioned structural contract, uses run-relative artifact paths, and contains no semantic verdict;
- `runner.log`, stderr progress, raw CLI events, and captured artifacts diagnose every tested infrastructure failure;
- deterministic-consumer failure remains a completed test result while runner infrastructure failure exits nonzero;
- source snapshots, digests, credential sanitation, path containment, and secret-redaction checks pass;
- promoted evidence remains self-contained after its working run is deleted;
- after offline inputs and behavior are reviewed and frozen, one owner-announced Sol-low Codex smoke run confirms the real adapter and event/final-output capture;
- focused runner documentation explains installation, commands, definition layout, result layout, logging, and the agent/human review loop;
- runner implementation changes no skill wording, legacy validation material, hooks, or unrelated project behavior.

Only after these gates pass may migration of the first real skill scenario begin.
