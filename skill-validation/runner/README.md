# skilltest

`skilltest` runs one supplied prompt and retains mechanical evidence, generates study-document drafts, or checks document conformance. The historical worksheet command remains available separately.
`run` is synchronous and stateless: each invocation owns a unique run directory.
It does not understand or evaluate the prompt, fixtures, evidence, or provider response.

## Testing the runner code

These tests validate the testing tool, not skill effectiveness or model latency.
Run from `skill-validation/runner/`:

```sh
.venv/bin/python -m pytest -q -m 'not process_smoke'
.venv/bin/python -m pytest -q -m process_smoke
.venv/bin/python -m pytest -q
# Equivalent full suite through uv:
uv run pytest -q
```

The first command runs unit tests; the second runs local process smoke tests; the last runs both.
Neither group invokes an installed Codex/Claude CLI or needs real credentials or network access.
Claude process smokes require macOS and exercise the real `sandbox-exec` policy against surrogate homes.
Sandbox probes resolve Python from `/opt/homebrew/bin:/usr/bin:/bin`, independently of caller PATH, so uv or another home-installed test interpreter does not require wider production reads.
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

## Study documents

Use `docs` for the [current study formats](../../skill-studies/formats/README.md). It makes no provider call and does not score model output.

```text
skilltest docs new KIND --output PATH --format-version 1
skilltest docs check PATH [--json]
skilltest docs check PROTOCOL --ready-for preparation --batch ID [--json]
skilltest docs check PROTOCOL --ready-for collection [--batch ID] [--json]
skilltest docs check PROTOCOL --ready-for assessment [--batch ID] [--json]
```

`KIND` is `protocol`, `case`, `manifest`, `index`, `result` or `assessment`. Generation defaults to the canonical version-1 draft; `result` and `assessment` additionally accept `--format-version 2`. Generation leaves the draft unfinished and refuses an existing output; its parent directory must exist.

Procedural-only execution results use version 2 and `functional_result: "not measured"`.
`docs tables` emits a Not measured column when present and requires the version-2 assessment layout; it counts only valid setups and keeps unassessed/missing coverage separate.
Exclude not measured from functional success denominators; an all-unmeasured group has no functional success rate.

Checking reads a file and its declared references. Repository identities resolve at their full Git revision or the enclosing manifest's source revision; external evidence uses absolute paths/hashes. Run from the repository when checking a document stored outside it. Referenced configurations are materialized only in disposable scratch for the existing config loader; no checker, embedded command or provider is executed.

Default checking reports structure, references and unresolved values. `complete` means no unresolved requirement among the requested mechanical checks; a default file check does not certify a batch. Stage checks require the protocol file and an unambiguous batch, follow its selected references and reconcile the declared scope. Assessment readiness validates references from both the current attempt index and the assessment's frozen index, including execution results and bundle inventories. Aggregate criteria come from each execution result’s pinned assessment manifest; collection manifests still establish the supplied inputs, which reassessment must preserve. Protocol case definitions provide coverage for groups with no recorded attempts. Collection checks also compare current dispatch inputs with their frozen bytes. A completed batch's input check does not grant authority to rerun it.

Diagnostics provide file, field/line, rule, message and severity. `--json` returns these with artifact kind, structural validity, completeness and unsupported status. Exit `0` means the requested checks passed; `1` means invalid content or unresolved stage requirements; `2` means usage or unsupported version/representation. Drafts can pass structural checking while failing readiness. Evidence absence remains explicit and is not converted into a behavioral failure.

Supported version-1 representations:

- The canonical Markdown headings/criterion cards and JSON fields; local inline links and heading anchors. External URLs are not fetched and free prose remains subject to semantic review.
- Scope in the existing `Order / Case / Condition / Repetition / CONFIG` table, or the existing explicit single-case, original-then-control, one-execution-each declaration. Stage checks support descriptive inclusion of all valid setups without retries; other inclusion or retry representations are reported unsupported.
- Aggregate tables with separate met/not-met/insufficient-evidence columns, or labelled `M/N/U` columns. Runtime strata use explicit `NAME includes orders A–B` declarations and must partition valid executions. Coverage uses the existing seven-column table; an explicit no-gap statement suffices only when every planned execution has a valid result.
- Current accounting accepts plain integers or correctly comma-grouped booked, remaining and ceiling totals in the existing paragraph, dispatched/remaining pool paragraph and `Work / Estimate / Basis` forecast table; outer ceilings may be linked from the plan. Time totals also accept `N active minutes booked; D minutes above|below the historical L-minute planning guideline`; the difference must reconcile, but the guideline does not cap the forecast. Hard-ceiling paragraphs retain their forecast limit, and call ceilings remain enforced. Only referenced attempt indexes contribute. Historical process/development-pilot indexes supply a labelled accounting-only projection, not version-1 format conformance or reassessment.

Unsupported historical documents remain unchanged. Unsupported layouts cannot silently pass stage checks; a required representation change needs explicit format review. Generation and validation share the canonical templates and structural rules, with the execution-result schema reused. Wheels package those same resource bytes; `jsonschema` is a runtime dependency.

### Mechanical study operations

```text
skilltest docs manifest MANIFEST --output DRAFT [--compare ORIGINAL CANDIDATE --allow-difference TARGET ...]
skilltest docs manifest MANIFEST --output FROZEN --revision FULL_COMMIT [--compare ORIGINAL CANDIDATE --allow-difference TARGET ...]
skilltest docs retain PROTOCOL BUNDLE --batch ID --order N --index INDEX --store DIRECTORY --revision FULL_COMMIT
skilltest docs tables PROTOCOL --batch ID --index INDEX --output FRAGMENT [--source-target TARGET --output-evidence ID]
```

Use `manifest` with the existing manifest template: supply IDs, dates, authority/controller paths, versions and condition configurations; hashes, source revision and the subject-source list are derived.
The draft checks current files, exact configured sources, criterion applicability and controller separation.
Paired checking compares execution settings and mounted bytes; declare differing target paths explicitly (`@prompt` means the prompt and is reserved as a target name during paired checking).
`preparation` checks the selected protocol scope and working manifests before freezing; complete draft cases are allowed, future index/report links are not required, and hashes are recomputed without writing the inputs.
It does not claim collection readiness or authorization.
Commit reviewed inputs, generate frozen manifests against that full commit, review and explicitly replace the committed draft at its declared path, then commit manifests and run collection readiness.
A freeze rejects working inputs that differ from the selected revision; neither command commits anything.
All generated files require an existing parent directory and a new output path.

Wait for the runner to exit before `retain`.
It selects one initial attempt from the committed protocol, verifies the frozen configuration, accepts terminal runner result version 0.5 (or a completed 0.4 result), and derives the subject charge from `invocation_started` even after failure.
The store must be outside the repository and disjoint from the source.
The command first checks the runner schema and recorded file/directory capture against the current bundle, including legitimately absent artifacts.
It then copies hidden files, directories and symlinks without following links, verifies modes/bytes/hashes/targets and source stability, and registers the verified inventory.
Declared file artifacts must be regular files; an arbitrary bundle symlink is preserved as a link.
It refuses duplicates, unknown charges, unresolved cleanup and existing destinations.
Failed 0.4 records cannot prove cleanup independently of their primary error and require manual inspection/preservation; they are not silently upgraded or automatically registered.
An exclusive index lock serializes cooperating registrations; interrupted operations can leave a lock or staging directory requiring inspection.
A publication/index-write failure can leave an unregistered bundle, which is reported and never silently adopted or overwritten.
The source remains intact; this verifies a retained copy, not a separate backup or OS-level proof against arbitrary writers.

Use `tables` after recording judgments, or to inspect partial coverage.
It validates identities and emits coverage, execution status, criterion counts and recorded functional outcomes, retaining unattempted/unassessed slots and excluded setups explicitly.
It refuses changed scopes, malformed records and incompatible scoring policies within an aggregate group.
Optional length measurement requires both the mounted source target and evidence ID; it counts complete UTF-8 files with `wc -w` and reports shorter/same/longer, with longer flagged rather than failed.
The output is a table fragment for the assessment, not a completed assessment or acceptance decision; links are relative to the fragment's location, so generate it beside the intended report.
Mechanical operations return `1` on invalid or unsupported input and `2` on argument errors.
Tools never assign judgments, retry, dispatch providers or mutate Git.

`src/skilltest/documents/` owns this functionality separately from execution. Future collection still pins the full runner Git revision and checks relevant changes, including shared CLI wiring/dependencies. Structural checks do not establish semantic correctness, causal attribution or owner consent.

## Worksheet

This command renders the historical methodology below; it is not an alternative current study assessment format. Existing CLI consumers/tests still exercise it, so retirement remains separate from adding `docs`.

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

1. Create the command's namespaced `TMPDIR` beneath the per-user temporary root (outside `/tmp` and `/var/tmp`) before presenting or invoking it; a
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
The original configuration snapshot and logged launch policy identify the selected mode; result schema `0.3` also records the resolved mode in `execution.permissions`.
Input schema remains `0.2`: this optional field preserves existing configurations and their writable default; input and result versions describe separate contracts.
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

Codex uses a fresh noninteractive session with JSON, session-rollout and last-message capture, the configured model/effort, and `workspace/fixture/` as both cwd and `--cd` root.
It retains `--skip-git-repo-check` and selects the fixed `skilltest` permission profile through command-local configuration.
The profile denies root reads and explicitly grants the fixture, sibling evidence and one invocation-owned scratch directory.
Required platform/runtime paths and `/opt/homebrew` remain readable for system tools; these are trusted installation roots, not places to store study material.
In `workspace-write` mode, fixture and evidence are writable, with `.git`, `.codex` and `.agents` protected under both workspace roots; only the fixture's `.git` receives a write exception for staging and local commits.
In `read-only` mode, fixture and evidence are readable and private scratch remains writable.
Both modes disable command network access and approvals; the exact emitted configuration is recorded in `runner.log`.
No inherited workspace or temporary-directory template is used.

Codex 0.154.0's `:minimal` macOS process defaults reopen `/tmp` and `/var/tmp` despite ordinary path denies.
Explicit deny globs block files beneath those trees and their `/private` aliases; preparation rejects fixture, evidence or scratch paths there, because the deny also applies to declared inputs.
Use an existing namespaced directory beneath macOS's per-user temporary root (`getconf DARWIN_USER_TEMP_DIR`) for the controller's `TMPDIR`.
The runner creates a separate private scratch directory per invocation and passes its path to subject shells.
An external-directory check can use that scratch; literal shared-temp reads/writes are intentionally unavailable.
Unsupported profile syntax fails without a broader-access fallback.

Run the installed-policy qualification before collection after a CLI or boundary change:

```sh
SKILLTEST_SANDBOX_EVIDENCE_DIR=/absolute/retained/scratch .venv/bin/python -m pytest acceptance/test_input_isolation.py acceptance/test_read_only_sandbox.py acceptance/test_codex_git_sandbox.py acceptance/test_codex_login_shell.py -q -s
```

The existing destination stores successful qualification copies; probes execute under the per-user temporary root, outside shared `/tmp`.
These macOS checks may require host permission to launch the inner sandbox; they make no model calls and use surrogate credentials/homes.
The [shared isolation check](acceptance/test_input_isolation.py) tests both providers and both permission modes against controller, sibling-run, home, shared-temp and symlink reads/writes, while preserving Python, Git and private scratch use.
The [read-only checks](acceptance/test_read_only_sandbox.py) additionally exercise overwrite/delete/rename/create and Git mutation denials, including scratch symlink escape.
The [login-shell check](acceptance/test_codex_login_shell.py) uses real runtime preparation and emitted policy in both modes, executes `/bin/zsh -lc`, and asserts Python and Git resolution plus Python compatibility (3.11+).
The [Codex Git check](acceptance/test_codex_git_sandbox.py) verifies source comparison, a root commit, evidence writes, protected-path write denials and network-bind denial using the adapter's emitted configuration.
These qualify the tested filesystem boundaries, not model behavior, native discovery or exhaustive host isolation.
Inspect the first authorized observation under changed conditions before continuing the batch.

The adapter fixes these additional controls:

```text
--strict-config --ignore-user-config --ignore-rules
-c shell_environment_policy.inherit="none"
-c shell_environment_policy.set={PATH="<prepared runtime PATH>",TMPDIR="<private scratch>",HOME="<private scratch>",ZDOTDIR="<private scratch>",TMPPREFIX="<private scratch>/zsh"}
-c cli_auth_credentials_store="file"
-c approval_policy="never"
```

Each invocation creates private HOME, CODEX_HOME and TMPDIR directories outside its retained bundle, with private parents mode 0700.
The CLI child receives only these three variables and PATH: the resolved Codex executable's directory followed by `/usr/bin:/bin:/usr/sbin:/sbin`. Shell tools receive that restricted PATH, private TMPDIR, HOME pointing to the same private scratch, and TMPPREFIX pointing to its `zsh` prefix while other environment inheritance stays disabled. This prevents zsh from inferring the real user home and from creating heredoc files under denied `/tmp`. The explicit PATH prevents environment stripping from selecting a different interpreter; a runner-owned `.zprofile` in private scratch restores that order after the system login profile. Explicit ZDOTDIR selects only that scratch for user startup files. [The Shiv runtime diagnosis](../../skill-studies/sweeping-stale-references/runtime-diagnosis.md) records the observed mismatch and qualification.
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
In `workspace-write` mode, Read, Skill, Glob, Grep, Write, Edit and Bash are explicitly available and allowed.
In `read-only` mode, the list is Read, Skill, Glob, Grep and Bash; dedicated Write/Edit tools are omitted, and the sandbox still denies mutations attempted through Bash.
Both modes use `--permission-mode dontAsk --permission-prompts none`; permission bypass is not used.
The sibling evidence directory remains available for reading; `--add-dir` does not override the process sandbox.

The controlled Claude runtime requires macOS `sandbox-exec` and an existing claude.ai subscription login using the standard `~/Library/Keychains/login.keychain-db` or supported file cache.
It retains normal HOME/USER for authentication and launches with an explicit operational PATH, fresh private temporary directories and the accepted memory/history/telemetry controls.
It does not inherit API keys, profile overrides, shell-startup environment variables or the old simple-system-prompt/bundled-skill suppression baseline.
A private `TMPPREFIX` keeps zsh heredoc files inside allowed scratch.
A private `ZDOTDIR` and `.zprofile` restore the prepared PATH after macOS login-zsh startup reorders it, without reading user startup files.
The whole-process Seatbelt policy denies file reads and writes by default, then grants declared fixture/evidence reads, private scratch and required system/runtime reads.
This covers native Read/Glob/Grep and Bash descendants alike.
The implementation lists the runtime exceptions: system tools/libraries (including macOS timezone data required by native ICU startup), Homebrew, Xcode, exact Claude executable paths, subscription-state files and the login keychain, plus exact macOS authentication metadata.
Filesystem metadata is readable for path traversal; contents of arbitrary home, controller and sibling-run files are not.
Selected ambient instruction/settings/skill/history paths remain explicitly denied.
In `workspace-write` mode only fixture, evidence, private scratch and `/dev/null` are writable; in `read-only` mode only scratch and `/dev/null` are writable.
HOME writes remain denied in both modes.
Scratch contains no supplied evidence, and symlinks do not extend its grants to external targets.
The controller creates the fixture Git boundary before launch and captures output outside that policy.
The emitted policy is retained in `runner.log`, since cleanup removes the runtime policy file.
Model-network connectivity remains available; this is study-input isolation, not a hostile-agent or network-exfiltration guarantee.
Runtime and fixture directories must be outside HOME.
Preparation rejects ambient instruction/configuration/skill entries in fixture ancestry.
The shared installed-policy tests above exercise the boundary; repeat affected controls when CLI/runtime assumptions change.
`SKILLTEST_SANDBOX_EVIDENCE_DIR=/absolute/new/evidence .venv/bin/python -m pytest -q acceptance/test_claude_cli.py` additionally tests the actual installed CLI in both permission modes: startup, Bash Python/Git selection, heredocs and warning-free Git ignore lookup, description delivery before Skill invocation and full body delivery afterward.
It uses surrogate authentication and a scripted localhost endpoint with external networking denied; it spends zero model calls and does not qualify production authentication or model selection.

Authentication preflight runs that same resolved Claude executable under the same child policy.
Status is inspected only in bounded memory, never logged or retained; no credentials are extracted or copied, no new login/logout occurs, and existing sessions are not manipulated.
Authentication/control failures stop preparation rather than falling back to an uncontrolled launch.
Git setup uses no templates, and inherited system/global Git settings are disabled both during setup and in the Claude environment.
A process-local `core.excludesFile=/dev/null` override also disables Git’s default host ignore-file lookup while retaining repository ignore rules; authentication keeps the real HOME without granting reads to that ignore file.
A fixture needing commits must provide its own test identity.

Prepared-input hashes, model argv, setup/model time limits and owned-process cleanup use the same mechanics as Codex.
Unresolved processes retain their runtime path for manual handling; never remove a shared profile or use logout as cleanup.
The Claude runtime contains no copied credentials.

`stdout.txt` retains the complete raw Claude trace and `stderr.txt` retains stderr.
The runner writes `final.txt` only when one unambiguous successful result supplies a text answer; trailing system events are allowed only for `background_tasks_changed`, `task_updated` and `task_notification`.
Later assistant output, unknown trailing events or multiple results prevent extraction; raw output is always retained.
An explicit empty successful answer is retained as an empty file.
Otherwise the final file is absent and `runner.log` records the extraction limitation.
Malformed, missing or provider-reported error output does not fabricate a process error or a file-write failure.
Mechanical completion and evidence validity remain distinct: inspect the raw trace before scoring or accepting the run.
Codex also captures its final answer through its last-message option. Its JSON command events may omit prefixes present in the model-facing tool response; use the retained session response entries when needed, with call-ID, content and truncation checks. See the [verified capture diagnosis](../../skill-studies/sweeping-stale-references/capture-diagnosis.md).

The earlier adapter passed offline verification and the [scoped live qualification](../pilot/qualification/README.md#claude-qualification-checkpoint) on Claude Code `2.1.266`.
Use the [Claude qualification checkpoint](../pilot/qualification/README.md#claude-qualification-checkpoint) before a real comparison, including native no-DD/A/B/composition catalogs, required reads/writes, shell/Git behavior and common-input drift.
The completed qualification adds actual companion loading, file search/write/edit and shell/Git operations to the earlier Read/Skill feasibility evidence; repeat only affected controls when that setup changes.

## Result

`result.json` now has schema version `"0.5"` and records the run identity, timestamps, duration, test id, mechanical invocation state, fixed artifacts, and an infrastructure error when one occurred.
`execution.permissions` is required and records `workspace-write` or `read-only`, including failures before provider launch; an omitted input field is recorded as its resolved `workspace-write` default.
Version 0.5 adds required `execution.cleanup_error` (null or a nonempty error string), independently of the primary infrastructure error; a timeout or nonzero exit must not hide an unresolved provider group.
The schema continues to validate historical 0.4 records without this field; their missing field is not proof of successful cleanup after failure.
Version 0.4 adds `artifacts.provider_session` for `provider-session.jsonl` and `SESSION_CAPTURE_FAILED`. Codex copies the single invocation-owned rollout before private-profile cleanup; no profile/auth files are copied. Claude records the session artifact as absent and retains its existing raw trace. Missing, ambiguous, empty, symlinked or uncopyable Codex session evidence is an explicit capture error; the private runtime is retained with a recovery path. `SESSION_CAPTURE_FAILED` takes precedence over a concurrent provider nonzero exit or timeout, and its JSON error message includes the recovery notice/path; `execution.exit_code` and `execution.timed_out` retain the actual provider outcome. A retained session may still contain truncated or incomplete tool output, so assess its actual contents.
Historical `0.2` and `0.3` results remain unchanged and must be interpreted with their version and retained configuration; a missing mode is not evidence of either permission setting.
Consumers validating new results must use the updated result schema; the worksheet reader continues to read the fields common to these versions.
`status` is `COMPLETED` only for a mechanically completed invocation; otherwise it is `INFRA_ERROR` with one of `PREPARATION_FAILED`, `PROVIDER_LAUNCH_FAILED`, `PROVIDER_TIMEOUT`, `PROVIDER_EXIT_NONZERO`, `ARTIFACT_WRITE_FAILED`, `PROVIDER_CLEANUP_FAILED`, or `SESSION_CAPTURE_FAILED`.
The cleanup code applies to either provider after an otherwise successful model call; earlier preparation/launch/timeout/provider errors stay primary, with cleanup failure logged and recorded independently.
Exit `0` means the run completed mechanically, exit `1` means an owned-run, provider, timeout, or artifact-persistence failure, and exit `2` means usage or configuration failed before a run directory was owned.

The `fixture` and `evidence` artifact records are recursive, lexicographically path-sorted inventories of retained filesystem entries.
Entries record relative path and type; regular files also record byte count and SHA-256 digest.
Inventory does not follow symlinks.
These are final-state inventories (including Codex's Git boundary), not the pre-launch input hashes recorded in `runner.log`.
Ordinary evidence may be empty.
The runner never evaluates evidence or assigns a behavioral verdict.

```json
{
  "schema_version": "0.5",
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
    "permissions": "workspace-write",
    "executable": "claude",
    "timeout_seconds": 900,
    "invocation_started": true,
    "timed_out": false,
    "cleanup_error": null,
    "exit_code": 0
  },
  "artifacts": {
    "config": {"path": "config.json", "exists": true, "bytes": 250, "sha256": "<64 lowercase hex characters>"},
    "prompt_template": {"path": "prompt-template.txt", "exists": true, "bytes": 150, "sha256": "<64 lowercase hex characters>"},
    "prompt": {"path": "prompt.txt", "exists": true, "bytes": 300, "sha256": "<64 lowercase hex characters>"},
    "stdout": {"path": "stdout.txt", "exists": true, "bytes": 40, "sha256": "<64 lowercase hex characters>"},
    "stderr": {"path": "stderr.txt", "exists": true, "bytes": 0, "sha256": "<64 lowercase hex characters>"},
    "provider_session": {"path": "provider-session.jsonl", "exists": false, "bytes": null, "sha256": null},
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
