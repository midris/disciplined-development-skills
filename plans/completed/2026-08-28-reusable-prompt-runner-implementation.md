# Reusable Prompt Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the skill-aware runner with the approved schema `"0.2"` stateless prompt runner, verify both providers end to end, and reset Phase 3 catalog migration.

**Architecture:** Preserve the existing straight-line modules: configuration loads one closed JSON object, workspace preparation copies declared files and renders one prompt, a fixed provider adapter invokes one CLI, and result construction inventories retained artifacts. Do not add orchestration, compatibility, provider configuration, or behavioral evaluation machinery.

**Tech Stack:** Python 3.11+, standard library, pytest, jsonschema, local Codex and Claude Code CLIs.

**Spec:** [Reusable Prompt Runner Design](specs/2026-08-27-reusable-prompt-runner-design.md)

## Global Constraints

- Configuration and result schema versions are exactly the string `"0.2"`; schema `"0.1"` configurations and numeric result schema `1` are not supported.
- One invocation loads one prompt configuration, atomically creates one unique run directory, invokes one provider once, writes one result, and exits synchronously.
- Production runner code contains no concurrency, retries, repetitions, batching, campaigns, shared state, compatibility layer, or behavioral judgment.
- Configuration contains exactly `schema_version`, `id`, `prompt`, `fixtures`, and `execution`; execution contains exactly `provider`, `model`, and `effort`.
- Fixtures copy individual regular files only. Do not add directory copying, symlink copying, merging, inferred includes, or content inspection.
- Prompt rendering performs literal replacement only for `{{workspace_dir}}`, `{{fixture_dir}}`, and `{{evidence_dir}}`.
- Preserve the existing provider/model/effort selection. Provider flags and environment variables remain adapter constants, not public configuration.
- Claude inherits the launch environment plus only the eight approved `CLAUDE_CODE_*` baseline variables from the spec.
- Evidence collection inventories filesystem entries mechanically and never validates their meaning or contents.
- Do not migrate a behavioral catalog in this plan. Delete the old packaged migrations, reset current Phase 3 progress, and preserve the completed schema `"0.1"` plan links as superseded history.
- Live provider runs require owner-facing execution and validate runner mechanics only. Do not commit temporary run bundles.
- Commit this implementation plan before creating the implementation worktree; final archival uses `git mv` on the tracked plan.

---

### Task 1: Replace the configuration contract

**Files:**
- Modify: `skill-validation/runner/src/skilltest/config.py`
- Modify: `skill-validation/runner/tests/conftest.py`
- Rewrite: `skill-validation/runner/tests/test_config.py`

**Interfaces:**
- Produces: `FixtureDeclaration(source: Path, target: Path)`, unchanged `ExecutionDeclaration`, and `TestConfig(schema_version, id, prompt, fixtures, execution, config_path, config_bytes)`.
- Produces: `load_config(path: Path) -> TestConfig` with the exact schema `"0.2"` contract.

- [x] **Step 1: Rewrite configuration tests for the accepted shape**

Cover one valid empty-fixture configuration, one valid multi-file configuration with `..` sources, strict JSON rejection, exact keys, UTF-8 prompt loading, final-entry symlink rejection, canonical targets, target conflicts, and execution scalars. Write invalid UTF-8 bytes to the prompt file and assert `load_config()` raises `ConfigError` before any run allocation. Use direct cases such as:

```python
value = {
    "schema_version": "0.2",
    "id": "config-case",
    "prompt": "prompt.md",
    "fixtures": [
        {"source": "source/a.txt", "target": "docs/a.txt"},
        {"source": "../shared/b.txt", "target": "b.txt"},
    ],
    "execution": {"provider": "codex", "model": "gpt-5.6-sol", "effort": "low"},
}
```

Parameterize invalid targets with `"/a"`, `"a/"`, `"a//b"`, `"a\\b"`, `"."`, `".."`, `"a/./b"`, and `"a/../b"`. Test conflicts `("a", "a")`, `("a", "a/b")`, and `("a/b", "a")`. Retain explicit duplicate-key and non-finite JSON tests.

- [x] **Step 2: Run the configuration tests and verify they fail against schema `"0.1"`**

Run:

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_config.py
```

Expected: failures reference missing schema `"0.2"` fields or retained skill/scenario fields.

- [x] **Step 3: Implement the minimal configuration dataclasses and loader**

Remove `SkillDeclaration`, `ScenarioDeclaration`, skill/dependency parsing, directory-tree checks, reserved-directory checks, and overlap policy. Add only:

```python
@dataclass(frozen=True, slots=True)
class FixtureDeclaration:
    source: Path
    target: Path

@dataclass(frozen=True, slots=True)
class TestConfig:
    schema_version: str
    id: str
    prompt: Path
    fixtures: tuple[FixtureDeclaration, ...]
    execution: ExecutionDeclaration
    config_path: Path
    config_bytes: bytes
```

Parse targets by splitting the JSON string on `/`, reject the exact invalid forms from the spec, construct `Path(*parts)`, and compare component tuples for equality or prefix conflicts. Reject absolute prompt/source strings and allow `..`. For each prompt/source candidate, use `lstat()` on the final entry before `resolve()`: reject a final symlink or non-regular entry, while allowing normal resolution through symlinked ancestors. Call `_read_utf8(prompt, "prompt")` inside `load_config()` before returning so invalid prompt bytes are configuration failure, not preparation failure. Preserve `_parse_config`, `_unique_object`, `_reject_nonfinite`, `_identifier`, `_execution`, `_read_utf8`, and `_exact_keys` only as needed by schema `"0.2"`.

- [x] **Step 4: Replace the shared test builder with schema `"0.2"` fixtures**

Make `build_config_case` write `prompt.md`, optional individual source files, and:

```python
{
    "schema_version": "0.2",
    "id": f"{name}-run",
    "prompt": "prompt.md",
    "fixtures": fixture_entries,
    "execution": {"provider": provider, "model": model, "effort": effort},
}
```

Remove expected-outcome, skill, dependency, and no-skill-context helpers.

- [x] **Step 5: Run focused tests and commit**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_config.py
git diff --check
git add src/skilltest/config.py tests/conftest.py tests/test_config.py
git commit -m "refactor(validation): adopt prompt runner config schema 0.2"
```

Expected: configuration tests pass; no production code references skill declarations.

---

### Task 2: Build the isolated prompt workspace

**Files:**
- Modify: `skill-validation/runner/src/skilltest/workspace.py`
- Rewrite: `skill-validation/runner/tests/test_workspace.py`

**Interfaces:**
- Consumes: `TestConfig.prompt` and `TestConfig.fixtures` from Task 1.
- Produces: `RunContext` paths for `prompt-template.txt`, `prompt.txt`, `workspace/fixture`, `workspace/evidence`, and existing runner-owned outputs.
- Produces: `PreparedRun(workspace_dir: Path, prompt_bytes: bytes, final_output_path: Path)`.

- [x] **Step 1: Write failing layout, rendering, copying, and isolation tests**

Assert the exact prepared tree:

```text
.skilltest-run
prompt-template.txt
prompt.txt
workspace/
  fixture/
  evidence/
```

Assert configured bytes land only at their declared fixture targets, both runtime directories exist, evidence starts empty, unknown brace expressions remain unchanged, and every occurrence of the three supported tokens becomes the current absolute path. Remove every assertion about `inputs/`, `subject-input.txt`, and `supplied-skills/`.

Add a caller-side concurrency test—without production concurrency machinery—that invokes `create_run(config)` twice concurrently and asserts distinct directories beneath the same run root:

```python
with ThreadPoolExecutor(max_workers=2) as pool:
    first, second = pool.map(lambda _: create_run(case.config), range(2))
assert first.run_dir != second.run_dir
```

- [x] **Step 2: Run workspace tests and verify the old layout fails**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_workspace.py
```

- [x] **Step 3: Implement the exact runtime paths and literal renderer**

Remove retained input/skill paths and `_subject_input_bytes`. Create fixture and evidence directories before copying files. Retain the original template, render only:

```python
rendered = template
for token, path in (
    ("{{workspace_dir}}", context.workspace_dir),
    ("{{fixture_dir}}", context.fixture_dir),
    ("{{evidence_dir}}", context.evidence_dir),
):
    rendered = rendered.replace(token, str(path.resolve()))
```

Write rendered UTF-8 bytes to `prompt.txt` and return those exact bytes for provider stdin.

- [x] **Step 4: Run focused tests and commit**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_config.py tests/test_workspace.py
git diff --check
git add src/skilltest/workspace.py tests/test_workspace.py
git commit -m "refactor(validation): prepare isolated prompt workspaces"
```

---

### Task 3: Simplify fixed provider invocation

**Files:**
- Modify: `skill-validation/runner/src/skilltest/providers.py`
- Modify: `skill-validation/runner/tests/conftest.py`
- Rewrite: `skill-validation/runner/tests/test_providers.py`

**Interfaces:**
- Renames: `ProviderRequest.subject_input_bytes` to `prompt_bytes`.
- Preserves: `invoke_provider(request: ProviderRequest) -> ProviderResult` and timeout behavior.
- Produces: Claude launch environment equal to the inherited environment plus the eight fixed baseline variables.

- [x] **Step 1: Write failing exact-argument and environment tests**

Assert Codex arguments are exactly:

```python
[
    "codex", "--cd", str(workspace), "exec", "--ephemeral",
    "--skip-git-repo-check", "--json", "--color", "never",
    "--model", model, "-c", f'model_reasoning_effort="{effort}"',
    "--sandbox", "workspace-write", "--output-last-message", str(final_path), "-",
]
```

Assert Claude arguments are exactly:

```python
[
    "claude", "--print", "--no-session-persistence",
    "--model", model, "--effort", effort,
    "--permission-mode", "acceptEdits",
]
```

Have the fake provider record the eight approved Claude variables and one unrelated inherited marker. Assert all nine are present for Claude and the inherited marker remains present for Codex. Retain launch-failure, timeout, nonzero, and raw stdout/stderr tests.

- [x] **Step 2: Run provider tests and verify old flags fail**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_providers.py
```

- [x] **Step 3: Implement only the accepted argument and environment changes**

Add one constant mapping:

```python
CLAUDE_BASELINE_ENV = {
    "CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT": "1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    "CLAUDE_CODE_DISABLE_BUNDLED_SKILLS": "1",
    "CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS": "1",
    "CLAUDE_CODE_DISABLE_WORKFLOWS": "1",
    "CLAUDE_CODE_DISABLE_ARTIFACT": "1",
    "CLAUDE_CODE_DISABLE_CRON": "1",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
}
```

For Claude, pass `env=os.environ | CLAUDE_BASELINE_ENV` to `Popen` and include
the fixed non-bypass `--permission-mode acceptEdits` argument; for Codex,
preserve the inherited environment. Do not add provider configuration or output
parsing.

- [x] **Step 4: Run focused tests and commit**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_providers.py
git diff --check
git add src/skilltest/providers.py tests/conftest.py tests/test_providers.py
git commit -m "refactor(validation): simplify provider launch defaults"
```

---

### Task 4: Replace the result contract and inventory retained directories

**Files:**
- Rewrite: `skill-validation/runner/result.schema.json`
- Modify: `skill-validation/runner/src/skilltest/results.py`
- Create: `skill-validation/runner/tests/test_results.py`

**Interfaces:**
- Produces: `result_record(context, config, provider_result, error, finished_at, duration_seconds) -> dict[str, Any]` with schema `"0.2"`.
- Produces: `_directory_artifact(path: Path, run_dir: Path) -> dict[str, Any]` and lexicographically sorted, non-following entry inventory.
- Preserves: atomic `publish_result` and streaming `_sha256`.

- [x] **Step 1: Write failing result-shape and inventory tests**

Construct completed and each infrastructure-error record directly. Validate them against `result.schema.json`; mutate every execution-state row into an invalid combination and require `jsonschema.ValidationError`.

Add explicit parameterized invalid records for each independent schema invariant:

```python
mutations = (
    ("schema_version", "0.1"),
    ("run_id", ""),
    ("started_at", "2026-08-28"),
    ("finished_at", "not-a-timestamp"),
    ("duration_seconds", -1),
    ("test.id", "INVALID"),
    ("execution.model", ""),
    ("execution.effort", "HIGH"),
    ("execution.executable", "other-provider"),
    ("execution.timeout_seconds", 901),
)
```

Separately mutate a Codex record to `execution.executable: "claude"`. For every file artifact, reject `exists: true` with null metadata and `exists: false` with non-null metadata. For both directory artifacts, reject `exists: false` with non-null `empty` or non-empty `entries`, and reject either mismatch between `empty` and whether `entries` has zero items. For directory entries, reject negative/fractional bytes, malformed digests, file entries with null metadata, and non-file entries with non-null metadata. Remove one required field and add one unknown field at each closed object level.

Create an evidence tree containing a regular file, empty directory, and symlink. Assert entries have exactly `path`, `type`, `bytes`, and `sha256`; only regular files have non-null metadata; symlinks are not followed. Validate one manually constructed `type: "other"` entry against the JSON Schema without creating a device or socket. Assert fixture inventory reflects final retained state after a test mutation.

- [x] **Step 2: Run result tests and verify schema `1` fails**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_results.py
```

- [x] **Step 3: Implement schema `"0.2"` and mechanical directory inventory**

Build exactly:

```python
{
    "schema_version": "0.2",
    "run_id": context.run_id,
    "status": "COMPLETED" if error is None else "INFRA_ERROR",
    "started_at": context.started_at,
    "finished_at": finished_at,
    "duration_seconds": duration_seconds,
    "test": {"id": config.id},
    "execution": execution_record,
    "artifacts": {
        "config": _file_artifact(context.config_path, context.run_dir),
        "prompt_template": _file_artifact(context.prompt_template_path, context.run_dir),
        "prompt": _file_artifact(context.prompt_path, context.run_dir),
        "stdout": _file_artifact(context.stdout_path, context.run_dir),
        "stderr": _file_artifact(context.stderr_path, context.run_dir),
        "final": _file_artifact(context.final_output_path, context.run_dir),
        "fixture": _directory_artifact(context.fixture_dir, context.run_dir),
        "evidence": _directory_artifact(context.evidence_dir, context.run_dir),
    },
    "infrastructure_error": None if error is None else {"code": error[0], "message": error[1]},
}
```

Encode the six valid state rows and every closed object directly in the JSON Schema. Do not retain `inputs`, skill metadata, scenario metadata, or the generic workspace artifact.

- [x] **Step 4: Run focused tests and commit**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_results.py
git diff --check
git add result.schema.json src/skilltest/results.py tests/test_results.py
git commit -m "refactor(validation): publish result schema 0.2"
```

---

### Task 5: Reconnect the straight-line runner

**Files:**
- Modify: `skill-validation/runner/src/skilltest/runner.py`
- Modify: `skill-validation/runner/tests/conftest.py`
- Rewrite: `skill-validation/runner/tests/test_run.py`
- Modify: `skill-validation/runner/tests/test_cli.py`

**Interfaces:**
- Consumes: `PreparedRun.prompt_bytes`, schema `"0.2"` result construction, and unchanged `ProviderResult`.
- Preserves: `run_once(config_path: Path) -> RunOutcome` and CLI exit behavior.

- [x] **Step 1: Write failing end-to-end fake-provider tests**

For both providers, assert one invocation receives the rendered prompt with the workspace as CWD; fixture and evidence directories are isolated; config/template/prompt/stdout/stderr/final/result occupy exact stable paths; Claude zero-exit stdout is copied byte-for-byte to `final.txt`; Codex uses its CLI-written final file.

Retain one case for every error-state row. Extend `FakeProvider.configure()` with `fixture_bytes: bytes | None = None`, `evidence_name: str | None = None`, and `evidence_bytes: bytes = b""`; have the fake executable apply those actions before its delay or exit. In both the timeout and nonzero-exit cases, overwrite `workspace/fixture/input.txt`, create `workspace/evidence/provider-output.txt`, and assert both final inventories contain the changed retained state. Assert provider errors take precedence over later artifact errors, pre-invocation owned failures use `PREPARATION_FAILED`, invalid JSON and invalid UTF-8 prompts exit `2` with no run directory, and every emitted result validates.

- [x] **Step 2: Run runner and CLI tests and verify stale transport fails**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_run.py tests/test_cli.py
```

- [x] **Step 3: Update orchestration with no new layer**

Pass `prepared.prompt_bytes` to `ProviderRequest`. Continue writing raw stdout and stderr. After a successful Claude invocation, write the same stdout bytes to `final.txt`; do not parse them. Preserve existing error precedence, logging, atomic result publication, and exit codes. Remove all subject-input and input-snapshot handling.

- [x] **Step 4: Run the complete offline runner suite and commit**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q
uv run pytest -q acceptance/test_provider_clis_installed.py
git diff --check
git add src/skilltest/runner.py tests/conftest.py tests/test_run.py tests/test_cli.py
git commit -m "refactor(validation): run opaque prompts through schema 0.2"
```

---

### Task 6: Add controlled provider smoke definitions

**Files:**
- Create: `skill-validation/runner/acceptance/fixtures/provider-smoke/prompt.md`
- Create: `skill-validation/runner/acceptance/fixtures/provider-smoke/fixture/input.txt`
- Create: `skill-validation/runner/acceptance/fixtures/provider-smoke/codex.json`
- Create: `skill-validation/runner/acceptance/fixtures/provider-smoke/claude.json`
- Create: `skill-validation/runner/acceptance/test_provider_smoke_definitions.py`

**Interfaces:**
- Produces: two checked-in schema `"0.2"` configurations sharing one controlled prompt and fixture.

- [x] **Step 1: Add a failing provider-free acceptance test**

Load both real smoke configurations and prepare them beneath a monkeypatched temporary root. Assert provider/model/effort, fixture bytes, empty evidence, and exact rendering of all three absolute runtime paths. The test must not invoke a provider.

- [x] **Step 2: Create the exact controlled prompt and configurations**

Use this prompt:

```text
This is an explicitly authorized runner acceptance smoke.
Read {{fixture_dir}}/input.txt.
Write one regular UTF-8 file at {{evidence_dir}}/smoke-output.txt.
Return a short final response.
Do not modify anything outside {{workspace_dir}}.
```

Write `fixture/input.txt` as the exact bytes `runner smoke fixture\n`. Use these exact configurations:

```json
{
  "schema_version": "0.2",
  "id": "codex-runner-smoke",
  "prompt": "prompt.md",
  "fixtures": [{"source": "fixture/input.txt", "target": "input.txt"}],
  "execution": {"provider": "codex", "model": "gpt-5.6-sol", "effort": "low"}
}
```

```json
{
  "schema_version": "0.2",
  "id": "claude-runner-smoke",
  "prompt": "prompt.md",
  "fixtures": [{"source": "fixture/input.txt", "target": "input.txt"}],
  "execution": {"provider": "claude", "model": "sonnet", "effort": "low"}
}
```

- [x] **Step 3: Run provider-free acceptance and commit**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q acceptance/test_provider_clis_installed.py acceptance/test_provider_smoke_definitions.py
git diff --check
git add acceptance/fixtures/provider-smoke acceptance/test_provider_smoke_definitions.py
git commit -m "test(validation): add controlled provider smokes"
```

---

### Task 7: Reset Phase 3 to a clean schema `"0.2"` migration

**Files:**
- Delete tracked packages under: `skill-validation/scenarios/adversarial-review-loop/`
- Delete tracked packages under: `skill-validation/scenarios/concise-writing/`
- Delete tracked packages under: `skill-validation/scenarios/disciplined-development/`
- Delete tracked packages under: `skill-validation/scenarios/disciplined-research/`
- Delete tracked packages under: `skill-validation/scenarios/dispatching-development-subagents/`
- Delete tracked packages under: `skill-validation/scenarios/lean-plan-writing/`
- Delete tracked packages under: `skill-validation/scenarios/skill-discovery/`
- Delete tracked packages under: `skill-validation/scenarios/sweeping-stale-references/`
- Delete tracked packages under: `skill-validation/scenarios/writing-explicit-rationale/`
- Rewrite: `skill-validation/scenarios/README.md`
- Modify: `plans/2026-08-24-scenario-porting-roadmap.md`

**Interfaces:**
- Produces: zero active migrated catalogs and preserved links to the superseded schema `"0.1"` completed plans.

- [x] **Step 1: Remove only the nine listed packaged-scenario directories**

Use tracked-file deletion for those exact directories. Do not delete `skill-validation/scenarios/README.md`, canonical source catalogs, charter files, or any plan under `plans/completed/`.

```bash
cd "$(git rev-parse --show-toplevel)"
git rm -r skill-validation/scenarios/adversarial-review-loop
git rm -r skill-validation/scenarios/concise-writing
git rm -r skill-validation/scenarios/disciplined-development
git rm -r skill-validation/scenarios/disciplined-research
git rm -r skill-validation/scenarios/dispatching-development-subagents
git rm -r skill-validation/scenarios/lean-plan-writing
git rm -r skill-validation/scenarios/skill-discovery
git rm -r skill-validation/scenarios/sweeping-stale-references
git rm -r skill-validation/scenarios/writing-explicit-rationale
```

- [x] **Step 2: Rewrite the active inventory for the restart**

Retain canonical source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, state active packaging schema `"0.2"`, and mark these exact totals as zero migrated: adversarial-review 15, adversarial-review-loop 15, concise-writing 17, disciplined-development 9, disciplined-research 7, dispatching-development-subagents 11, lean-plan-writing 7, skill-discovery 12, sweeping-stale-references 6, and writing-explicit-rationale 6. Overall state is `105 total, 0 migrated, 105 not migrated`.

- [x] **Step 3: Reset roadmap Phase 3 without losing history**

Replace skill/dependency packaging language with tester-authored prompt and individual-file fixture language. Mark current Phase 3 at zero catalogs. Move the eight completed plan links beneath `Superseded schema "0.1" migration wave`; do not mark them as current completions.

- [x] **Step 4: Remove the aborted active draft and verify the reset**

The draft is currently untracked in the original workspace, so the owner-facing controller removes that exact file after branch integration if it is not present in the implementation worktree. Verify:

```bash
cd "$(git rev-parse --show-toplevel)"
test "$(find skill-validation/scenarios -mindepth 1 -type f ! -name README.md | wc -l | tr -d ' ')" = "0"
test "$(find skill-validation/scenarios -mindepth 1 -type d | wc -l | tr -d ' ')" = "0"
rg -n 'Superseded schema `"0.1"` migration wave|0 migrated|schema `"0.2"`' plans/2026-08-24-scenario-porting-roadmap.md skill-validation/scenarios/README.md
git diff --check
```

- [x] **Step 5: Commit the tracked reset**

```bash
cd "$(git rev-parse --show-toplevel)"
git add -A skill-validation/scenarios plans/2026-08-24-scenario-porting-roadmap.md
git commit -m "docs(validation): restart catalog migration for schema 0.2"
```

---

### Task 8: Run both live smokes, publish documentation, and verify

**Files:**
- Rewrite: `skill-validation/runner/README.md`
- Move after Steps 1–5 are complete: `plans/2026-08-28-reusable-prompt-runner-implementation.md` to `plans/completed/2026-08-28-reusable-prompt-runner-implementation.md`

**Interfaces:**
- Consumes: the complete runner and both controlled smoke definitions.
- Produces: mechanically inspected Codex and Claude bundles plus documentation matching the accepted contract.

- [x] **Step 1: Run the Codex smoke from the owner-facing session** — bundle: `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260828T174827646Z-codex-runner-smoke-80920b0b-3b6a-4649-be3e-3026ac97a520-i5u89o7s`

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
CODEX_RUN_DIR="$(uv run skilltest run acceptance/fixtures/provider-smoke/codex.json)"
```

The assignment preserves `skilltest`'s exit status because it contains no
pipeline. Stop unless it exits `0`. Record the printed bundle path in the plan
checkbox note, but do not commit the bundle.

- [x] **Step 2: Mechanically inspect the Codex bundle**

Run this mechanical inspection; it does not read response or generated-file contents:

```bash
uv run python - "$CODEX_RUN_DIR" result.schema.json acceptance/fixtures/provider-smoke/fixture/input.txt <<'PY'
import json, sys
from pathlib import Path
import jsonschema

run = Path(sys.argv[1])
schema = json.loads(Path(sys.argv[2]).read_text())
result = json.loads((run / "result.json").read_text())
jsonschema.validate(result, schema)
assert result["status"] == "COMPLETED"
assert result["infrastructure_error"] is None
assert result["execution"]["invocation_started"] is True
assert result["execution"]["timed_out"] is False
assert result["execution"]["exit_code"] == 0
for name in ("config.json", "prompt-template.txt", "prompt.txt", "stdout.txt", "stderr.txt", "final.txt"):
    assert (run / name).is_file(), name
assert (run / "workspace/fixture/input.txt").read_bytes() == Path(sys.argv[3]).read_bytes()
rendered = (run / "prompt.txt").read_text()
assert all(token not in rendered for token in ("{{workspace_dir}}", "{{fixture_dir}}", "{{evidence_dir}}"))
matches = [entry for entry in result["artifacts"]["evidence"]["entries"] if entry["path"] == "smoke-output.txt"]
assert len(matches) == 1
assert matches[0]["type"] == "file"
assert isinstance(matches[0]["bytes"], int) and matches[0]["bytes"] >= 0
assert len(matches[0]["sha256"]) == 64
assert result["artifacts"]["evidence"]["empty"] is False
PY
```

- [x] **Step 3: Run and inspect the Claude smoke from the owner-facing session** — passing bundle: `/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/skilltest-runs/20260828T182851670Z-claude-runner-smoke-4d4db6eb-6d1a-4236-965a-0b3fae567dc3-pdw723xp`

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
CLAUDE_RUN_DIR="$(uv run skilltest run acceptance/fixtures/provider-smoke/claude.json)"
```

The assignment must exit `0`. Repeat the Step 2 inspection with
`CLAUDE_RUN_DIR` in place of `CODEX_RUN_DIR`, then run:

```bash
cmp "$CLAUDE_RUN_DIR/stdout.txt" "$CLAUDE_RUN_DIR/final.txt"
```

Do not score either provider response.

- [x] **Step 4: Rewrite runner documentation after both smokes pass mechanically**

Document only `skilltest run CONFIG`, owner authorization, exact schema `"0.2"`, fixture source/target rules, three literal tokens, fixed bundle layout, result meaning, provider/model/effort selection, fixed provider behavior, and the configuration/prompt/result examples from the spec. State that ordinary evidence may be empty and that the runner never evaluates it.

- [x] **Step 5: Run final verification**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv sync --locked
uv run pytest -q
uv run pytest -q acceptance/test_provider_clis_installed.py acceptance/test_provider_smoke_definitions.py
cd "$(git rev-parse --show-toplevel)"
git diff --check
git status --short
```

Expected: all offline and provider-free acceptance tests pass; only intended implementation, reset, documentation, and plan-state changes remain.

- [x] **Step 6: Archive the completed plan and commit documentation**

```bash
cd "$(git rev-parse --show-toplevel)"
git mv plans/2026-08-28-reusable-prompt-runner-implementation.md plans/completed/2026-08-28-reusable-prompt-runner-implementation.md
git add skill-validation/runner/README.md plans/completed/2026-08-28-reusable-prompt-runner-implementation.md
git commit -m "docs(validation): document reusable prompt runner"
```
