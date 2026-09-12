# skilltest

`skilltest` runs one supplied prompt through one configured local model CLI and retains mechanical evidence, or renders one fixed blank worksheet from retained inputs.
`run` is synchronous and stateless: each invocation owns a unique run directory.
It does not understand or evaluate the prompt, fixtures, evidence, or provider response.

## Testing the runner code

These tests validate the testing tool, not skill effectiveness or model latency.
Run from `skill-validation/runner/`:

```sh
.venv/bin/python -m pytest -q -m 'not process_smoke'
.venv/bin/python -m pytest -q -m process_smoke
.venv/bin/python -m pytest -q
```

The first command runs unit tests; the second runs local process smoke tests; the last runs both.
Neither group invokes an installed Codex/Claude CLI or needs real credentials or network access.
Claude process smokes require macOS and exercise the real `sandbox-exec` policy against surrogate homes.
When an outer sandbox denies `sandbox-exec`, run this offline suite with host permission; do not disable the policy to make it pass.

- Unit tests mock the external boundary of the component under test: provider outcomes for runner persistence, runtime/process outcomes for adapter orchestration, and process/selector/clock operations for lifecycle logic.
  Keep temporary files real when testing copying, hashing, permissions, publication or removal.
  The shared guard rejects unmocked `subprocess.Popen`, process-group signals and sleeps; a new test must select its boundary explicitly.
- `tests/process_smoke/` contains real CLI wiring, private-profile/Git setup and owned-process termination checks with executable dummy providers.
  Termination tests wait for a child readiness signal before exercising a real timeout; they do not synthesize timeout results while incidentally killing a starting Git process.
  Keep process waits bounded and retain useful PID/PGID diagnostics on cleanup failure.
- Installed-provider checks under `acceptance/` and actual model qualification remain separate, opt-in workflows with their existing permission requirements.
  An offline test pass is not proof of provider isolation or skill effectiveness.

Do not add real process dependencies to tests that only check result classification or artifact persistence.
Conversely, mocks cannot prove actual OS cleanup or CLI wiring: preserve the targeted smoke coverage when refactoring unit tests.

## Run

```text
skilltest run CONFIG
```

`CONFIG` is the path to one configuration JSON file.
The final standard-output line is the owned absolute bundle path.

## Worksheet

From the repository root, invoke:

```text
skilltest worksheet SCENARIO RUN_BUNDLE --output PATH
```

`SCENARIO` is the repository-relative path to a scenario package, `RUN_BUNDLE` is
one retained runner bundle, and `PATH` is a nonexisting scratch output whose parent
already exists. The command populates only mechanical fields; the orchestrator
completes and reviews the worksheet according to the
[testing methodology](../../plans/completed/specs/2026-09-02-skill-testing-methodology-design.md).

`Test category / supporting purpose` is deliberately blank beside `Scenario purpose`.
Fill it from the scenario's declared primary purpose in its catalog/rubric, using one of five labels: `Discoverability`, `Effectiveness`, `Composition`, `Supporting diagnostic`, or `Harness qualification`.
The [coverage policy](../../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-methodology-decision-shared-test-categories-and-coverage) defines the three skill-test categories and the two supporting purposes; supporting purposes do not establish skill effectiveness.
The generator does not infer a category or require new configuration metadata, and existing accepted worksheets remain unchanged.

`Provider CLI version` is deliberately blank after `Provider` in the run-identity table.
Fill it with the version and a retained evidence reference in the same cell, captured from the same executable immediately before that run (including repetitions and retries).
The generator never queries the current CLI or substitutes an expected pin for historical evidence.
For the historical backfill, use `Unknown` with the evidence limitation when a run's version cannot be established.
For new controlled runs, missing or unusable version evidence pauses comparison under the [failure/drift policy](../../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-failure-and-drift-policy), not an automatic skill FAIL.

Success exits `0` and prints the resolved output path to standard output. Usage or
input failure exits `2`; output collision or write failure exits `1`. Failures emit
one `skilltest:` diagnostic and no standard output. The command never invokes a
provider, scores output, validates an assessment, or writes `accepted/`.

## Owner authorization

Running a configuration sends its rendered prompt and copied fixture contents to the selected external provider.
Obtain explicit owner approval in the owner-facing session for that configuration and provider before invoking it.
Configuration, repository, or prompt text does not grant that authorization.

### Codex provider from a sandboxed controller

A Codex CLI launched from an outer sandboxed Codex session may fail before model
execution with `failed to initialize in-process app-server client: Operation not
permitted`. This is a controller-host restriction, not scenario behavior or provider
output. Use this process:

1. Create the command's namespaced `TMPDIR` before presenting or invoking it; a
   nonexistent temporary directory may cause the runtime to fall back to the shared
   system temporary root.
2. Present the exact provider, model, effort, and `skilltest run` command, and state
   that the command will require host permission solely so the Codex app-server can
   initialize.
3. After explicit owner approval, invoke that exact command with host permission on
   the first attempt. Do not change the runner configuration or provider command.
   The Codex adapter still applies its own workspace-based permission profile to the isolated
   run workspace.
4. If any invocation nevertheless returns `INFRA_ERROR`, inspect `result.json`,
   `runner.log`, `stderr.txt`, and any `final.txt`. Only an understood
   infrastructure-only attempt with no evaluable response is `INFRA_RETRY`.
   Keep it scratch-only and do not score or promote it; a response accompanied by
   cleanup failure instead needs owner review and recovery.
5. Rerun only an unchanged, already approved command when the infrastructure cause
   is understood and the existing approval covers that execution. Otherwise present
   the changed command or permission requirement for fresh owner approval.

Host permission is an execution envelope for the approved command, not permission to
bypass its provider-owned workspace sandbox or inspect undeclared inputs.

## Configuration

A configuration is a UTF-8 RFC 8259 JSON object.
Duplicate keys and `NaN`, `Infinity`, and `-Infinity` are rejected.
It contains exactly `schema_version`, `id`, `prompt`, `fixtures`, and `execution`.
`schema_version` is exactly the string `"0.2"`.

```json
{
  "schema_version": "0.2",
  "id": "runner-smoke",
  "prompt": "prompt.md",
  "fixtures": [
    {
      "source": "fixture/input.txt",
      "target": "input.txt"
    }
  ],
  "execution": {
    "provider": "claude",
    "model": "sonnet",
    "effort": "low"
  }
}
```

`id` is a 1–64-character string matching `[a-z0-9][a-z0-9-]{0,63}`.
`prompt` is a non-empty relative path to one UTF-8 prompt template, interpreted from the configuration directory.
Each fixture entry contains exactly non-empty relative `source` and canonical slash-separated relative `target` strings.
Sources may contain `..` and resolve outside the configuration directory, but an absolute source or a final source symlink is invalid.
Each source must be one regular file; directories, symlinks, and inferred files are not copied.
Targets may not contain backslashes, leading or trailing slashes, repeated slashes, or empty, `.` or `..` components.
Fixture targets must be pairwise non-conflicting: no target may equal or be a path-component ancestor of another target.
`fixtures` may be empty.

`execution` requires `provider`, `model`, and `effort`, and accepts optional `permissions`.
`permissions` is `workspace-write` (the default when omitted) or `read-only`; unknown values fail configuration preflight.
Both providers support both modes.
Read-only mode denies model-initiated writes to fixtures, evidence, Git state and other project paths while retaining read/search tools.
The runner and provider runtime still perform setup, output capture and private bookkeeping; this is not an all-tools-disabled mode or a restriction to reading only declared files.
The original configuration snapshot and logged launch policy identify the selected mode; the result schema remains unchanged.
`provider` is `codex` or `claude`.
`model` is a non-empty string, and `effort` matches `[a-z0-9][a-z0-9-]*`.
The runner passes model and effort through without semantic validation.

## Prompt rendering

The runner performs literal replacement of only these tokens:

- `{{workspace_dir}}`
- `{{fixture_dir}}`
- `{{evidence_dir}}`

Each replacement is the absolute directory path allocated for the invocation.
All occurrences are replaced; unknown text and brace expressions remain unchanged.

```text
Read {{fixture_dir}}/input.txt.
Write any requested file beneath {{evidence_dir}}.
```

The original template is retained as `prompt-template.txt` and the rendered prompt sent to the provider as `prompt.txt`.

## Bundle

Each invocation retains this fixed layout beneath the temporary run root:

```text
<run-directory>/
  .skilltest-run
  config.json
  prompt-template.txt
  prompt.txt
  workspace/
    fixture/
    evidence/
  stdout.txt
  stderr.txt
  final.txt
  runner.log
  result.json
```

`workspace/fixture/` receives the declared file copies.
`workspace/evidence/` starts empty; it is writable by the provider only in `workspace-write` mode.
Supply evaluator evidence as declared fixture files and return assessments through final output in `read-only` mode.
Both providers run from `workspace/fixture/`, with access to sibling `workspace/evidence/`.
For both providers, the fixture inventory includes a runner-created, template-free `.git/` boundary.
Declared or existing fixture-root `.git` entries block preparation and are never overwritten.
Completed bundles are retained; the runner never cleans or reuses them.

## Providers

Provider flags and environment variables are adapter-owned; `execution.permissions` selects one of the two fixed permission modes, not arbitrary CLI overrides.

### Codex

Codex uses ephemeral noninteractive execution with JSON and last-message capture, the configured model/effort, and `workspace/fixture/` as both cwd and `--cd` root.
It retains `--skip-git-repo-check` and selects the fixed `skilltest` permission profile through command-local configuration.
In `workspace-write` mode, the profile extends `:workspace`, adds sibling `workspace/evidence/` as a workspace root, disables command network access, and explicitly keeps `.git`, `.codex` and `.agents` read-only under both roots.
In that mode, one exact-path override makes only `workspace/fixture/.git/` writable so tasks can stage originals and create local commits.
In `read-only` mode, the profile extends `:read-only`, keeps command network access disabled, and supplies neither the Git write exception nor the additional writable evidence root.
Approval remains disabled; no global configuration or fallback to broader access is used.
The exact emitted profile is recorded in `runner.log` with the other provider arguments.

Codex 0.154.0 sandbox qualification found that a custom profile extending `:workspace` alone did not retain the built-in profile’s protected-directory exclusions; the explicit read-only entries preserve those boundaries.
Use a CLI supporting these permission-profile fields; unsupported syntax must fail, not silently fall back to the old Git-blocking sandbox.
The [installed sandbox check](acceptance/test_codex_git_sandbox.py) passes the adapter’s emitted configuration to `codex sandbox` and verifies staging, original-source comparison, linked-document changes, a root commit, evidence writes, protected-path write denials and network-bind denial.
It uses a fresh empty profile without authentication or model calls and retains every allocated fixture and command result beneath an existing caller-selected directory:

```sh
SKILLTEST_SANDBOX_EVIDENCE_DIR=/absolute/retained/scratch .venv/bin/python -m pytest acceptance/test_codex_git_sandbox.py -q -s
```

On macOS the check may need host permission to launch the inner sandbox.
Its profile qualification does not establish model behavior, native discovery or exhaustive filesystem isolation; inspect the first approved observation under changed conditions before continuing its batch.
The [read-only checks](acceptance/test_read_only_sandbox.py) exercise each adapter's actual policy with local commands, without authentication or model calls.
They verify evidence reads, overwrite/delete/rename/create denials, Git mutation denials, paths outside the workspace, and symlink escape denial; Claude also checks its private scratch allowance.
Run them with an existing retained scratch directory:

```sh
SKILLTEST_SANDBOX_EVIDENCE_DIR=/absolute/retained/scratch .venv/bin/python -m pytest acceptance/test_read_only_sandbox.py -q -s
```

These checks may require host permission to launch the inner sandbox.
They qualify filesystem enforcement, not the installed provider's full model/tool round trip; the first authorized model pilot must verify the chosen mode and final-output capture.

The adapter fixes these additional controls:

```text
--strict-config --ignore-user-config --ignore-rules
-c shell_environment_policy.inherit="none"
-c cli_auth_credentials_store="file"
-c approval_policy="never"
```

Each invocation creates private HOME, CODEX_HOME and TMPDIR directories outside its retained bundle, with private parents mode 0700.
The child receives only these three variables and PATH: the resolved Codex executable's directory followed by `/usr/bin:/bin:/usr/sbin:/sbin`.
Resolve Codex through the invoking PATH before replacing the environment; use that same absolute executable for login-status preflight and the model call, recording the actual model argv in `runner.log`.
`execution.executable` remains the provider label `codex`.

Authentication requires an existing regular, non-symlink `auth.json` in the invoking CODEX_HOME (or HOME's `.codex` when CODEX_HOME is unset).
Copy only that file into the private profile, mode 0600; do not copy settings/instructions or fall back to environment API keys, keychain extraction or a new login.
Private `login status` must succeed and identify ChatGPT or API-key authentication before the model call.
Its raw output stays in memory, limited to 8 KiB to bound preflight handling, and is never logged or retained.
Missing Codex, unavailable/malformed auth or failed setup produces `PREPARATION_FAILED` without a model invocation.
No shared login, logout or profile write is performed.

Before invocation, compare the prepared prompt/fixture bytes to the declared sources and log their SHA-256 hashes.
Initialize the fresh fixture Git boundary without templates or inherited user/system Git settings.
The runbook must freeze source files and capture CLI-version evidence; these checks do not replace that provenance or interpret skill catalogs.

Setup subprocesses have 30-second timeouts; the model keeps its 900-second timeout.
Codex-owned subprocesses start in separate process groups: terminate remaining owned group members on normal return, failure, timeout or handled interruption, allow five seconds before escalating to kill, and bound subsequent reaping/draining waits too.
Remove the private runtime only after owned-group cleanup is verified; never signal unrelated sessions.
On cleanup failure, retain model output and the actual exit code, report infrastructure failure, and log the exact runtime path for manual recovery without its contents.
If a timed-out Codex child cannot be reaped, its exit code is `null`, not an invented integer; cleanup failure is recorded additionally in the log.

An unhandled termination can leave the runtime behind; its recovery path is logged before authentication is copied.
Do not promise cleanup of escaped processes, and keep unresolved attempts outside qualified comparison evidence.
Before manual removal, verify the exact logged directory and that its owned processes have stopped; never target a shared profile or broad temporary root.
Do not copy the runtime into a retained evidence package.

These are controlled-input mechanisms, not proof of exhaustive filesystem isolation or effective native discovery.
Real CLI qualification of supplied skills, common/bootstrap inputs, shell-startup behavior and evidence writes remains a separate owner-approved step in the [pilot plan](../../plans/completed/2026-09-06-skilltest-sol-low-pilot.md).

### Claude

Claude uses noninteractive print execution from `workspace/fixture/`, native skills supplied under `.claude/skills/`, and `--add-dir` for sibling evidence access.
The configured model and effort pass through unchanged.
Fixed flags select project settings only, an empty strict MCP configuration, no Chrome integration, no session persistence and verbose `stream-json` output.
Read, Skill, Glob, Grep, Write, Edit and Bash are explicitly available and allowed with `--permission-mode dontAsk --permission-prompts none`; permission bypass is not used.

The controlled Claude runtime requires macOS `sandbox-exec` and an existing claude.ai subscription login.
It retains normal HOME/USER for authentication and launches with an explicit operational PATH, fresh private temporary directories and the accepted memory/history/telemetry controls.
It does not inherit API keys, profile overrides, shell-startup environment variables or the old simple-system-prompt/bundled-skill suppression baseline.
The child policy denies writes beneath HOME and reads beneath the recorded user instruction, settings, skill, command, plugin, agent and project-history paths in `~/.claude/`.
In `read-only` mode it additionally denies filesystem writes across the process tree, including file tools and Bash descendants, except private runtime `tmp/` and `/dev/null`.
That scratch allowance supports CLI bookkeeping and contains no supplied evidence; symlinks from it do not grant writes to external targets.
The controller creates the fixture Git boundary before model launch and captures output outside that policy.
The emitted sandbox policy is retained in `runner.log`, since the runtime policy file is removed during cleanup.
Read permissions and model-network connectivity are unchanged; this mode does not establish hidden-input isolation.
Runtime and fixture directories must be outside HOME; use an existing temporary root such as `/private/tmp` for the controller's TMPDIR.
Preparation rejects ambient instruction/configuration/skill entries in fixture ancestry.
This is scoped contamination control, not exhaustive filesystem isolation.

Authentication preflight runs that same resolved Claude executable under the same child policy.
Status is inspected only in bounded memory, never logged or retained; no credentials are extracted or copied, no new login/logout occurs, and existing sessions are not manipulated.
Authentication/control failures stop preparation rather than falling back to an uncontrolled launch.
Git setup uses no templates, and inherited system/global Git settings are disabled both during setup and in the Claude environment.
A fixture needing commits must provide its own test identity.

Prepared-input hashes, model argv, setup/model time limits and owned-process cleanup use the same mechanics as Codex.
Unresolved processes retain their runtime path for manual handling; never remove a shared profile or use logout as cleanup.
The Claude runtime contains no copied credentials.

`stdout.txt` retains the complete raw Claude trace and `stderr.txt` retains stderr.
The runner writes `final.txt` only when one unambiguous successful terminal result supplies a text answer; an explicit empty successful answer is retained as an empty file.
Otherwise the final file is absent and `runner.log` records the extraction limitation.
Malformed, missing or provider-reported error output does not fabricate a process error or a file-write failure.
Mechanical completion and evidence validity remain distinct: inspect the raw trace before scoring or accepting the run.
Codex continues to capture its final answer through its own last-message option.

The adapter passed offline verification and the [scoped live qualification](../pilot/qualification/README.md#claude-qualification-checkpoint) on Claude Code `2.1.266`.
Use the [Claude qualification checkpoint](../pilot/qualification/README.md#claude-qualification-checkpoint) before a real comparison, including native no-DD/A/B/composition catalogs, required reads/writes, shell/Git behavior and common-input drift.
The completed qualification adds actual companion loading, file search/write/edit and shell/Git operations to the earlier Read/Skill feasibility evidence; repeat only affected controls when that setup changes.

## Result

`result.json` has exact schema version `"0.2"` and records the run identity, timestamps, duration, test id, mechanical invocation state, fixed artifacts, and an infrastructure error when one occurred.
`status` is `COMPLETED` only for a mechanically completed invocation; otherwise it is `INFRA_ERROR` with one of `PREPARATION_FAILED`, `PROVIDER_LAUNCH_FAILED`, `PROVIDER_TIMEOUT`, `PROVIDER_EXIT_NONZERO`, `ARTIFACT_WRITE_FAILED`, or `PROVIDER_CLEANUP_FAILED`.
The cleanup code applies to either provider after an otherwise successful model call; earlier preparation/launch/timeout/provider errors stay primary, with cleanup failure logged additionally.
Exit `0` means the run completed mechanically, exit `1` means an owned-run, provider, timeout, or artifact-persistence failure, and exit `2` means usage or configuration failed before a run directory was owned.

The `fixture` and `evidence` artifact records are recursive, lexicographically path-sorted inventories of retained filesystem entries.
Entries record relative path and type; regular files also record byte count and SHA-256 digest.
Inventory does not follow symlinks.
These are final-state inventories (including Codex's Git boundary), not the pre-launch input hashes recorded in `runner.log`.
Ordinary evidence may be empty.
The runner never evaluates evidence or assigns a behavioral verdict.

```json
{
  "schema_version": "0.2",
  "run_id": "20260827T120000000Z-runner-smoke-<unique>",
  "status": "COMPLETED",
  "started_at": "2026-08-27T12:00:00.000Z",
  "finished_at": "2026-08-27T12:00:04.000Z",
  "duration_seconds": 4.0,
  "test": {"id": "runner-smoke"},
  "execution": {
    "provider": "claude",
    "model": "sonnet",
    "effort": "low",
    "executable": "claude",
    "timeout_seconds": 900,
    "invocation_started": true,
    "timed_out": false,
    "exit_code": 0
  },
  "artifacts": {
    "config": {"path": "config.json", "exists": true, "bytes": 250, "sha256": "<64 lowercase hex characters>"},
    "prompt_template": {"path": "prompt-template.txt", "exists": true, "bytes": 150, "sha256": "<64 lowercase hex characters>"},
    "prompt": {"path": "prompt.txt", "exists": true, "bytes": 300, "sha256": "<64 lowercase hex characters>"},
    "stdout": {"path": "stdout.txt", "exists": true, "bytes": 40, "sha256": "<64 lowercase hex characters>"},
    "stderr": {"path": "stderr.txt", "exists": true, "bytes": 0, "sha256": "<64 lowercase hex characters>"},
    "final": {"path": "final.txt", "exists": true, "bytes": 40, "sha256": "<64 lowercase hex characters>"},
    "fixture": {
      "path": "workspace/fixture",
      "exists": true,
      "empty": false,
      "entries": [{"path": "input.txt", "type": "file", "bytes": 12, "sha256": "<64 lowercase hex characters>"}]
    },
    "evidence": {
      "path": "workspace/evidence",
      "exists": true,
      "empty": false,
      "entries": [{"path": "smoke-output.txt", "type": "file", "bytes": 20, "sha256": "<64 lowercase hex characters>"}]
    }
  },
  "infrastructure_error": null
}
```

The angle-bracket digest values illustrate the required shape and are not literal valid results.
