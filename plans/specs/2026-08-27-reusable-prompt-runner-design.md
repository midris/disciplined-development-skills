# Reusable Prompt Runner Design

## Status

Approved in discussion on 2026-08-27. This design replaces the runner's
skill-specific input contract with a small, stateless prompt-execution contract.
It does not begin implementation or resume catalog migration.

## Purpose

`skilltest` runs one supplied prompt against one configured local model CLI and
retains mechanical evidence from that invocation. It prepares an isolated input
and output area, but it does not understand the prompt, skills, dependencies, or
the meaning of the result.

The runner remains synchronous and single-run. Separate invocations may safely
use the same configuration concurrently because every invocation owns a unique
run directory and shares no mutable runner state.

## Configuration contract

The JSON configuration contains exactly:

| Field | Meaning |
|---|---|
| `schema_version` | Exact string `"0.2"`. |
| `id` | Path-safe test identifier. |
| `prompt` | Path to one UTF-8 prompt template. |
| `fixtures` | Ordered list of files to copy into the run fixture directory. May be empty. |
| `execution` | Existing `provider`, `model`, and `effort` selection. |

Each fixture entry contains exactly:

| Field | Meaning |
|---|---|
| `source` | Path to one regular source file, relative to the configuration. |
| `target` | Relative file path below the runtime fixture directory. |

The runner copies individual regular files only. It does not copy whole
directories, follow or create symlinks, merge directories, infer includes, or
interpret file contents. Parent directories required by a target are created
mechanically. Duplicate targets are invalid because a fresh run never merges or
overwrites fixture inputs.

The following existing fields are removed:

- `skill`
- `dependencies`
- `skill_context`
- `scenario`
- `expected_outcome`

Skills, supporting skills, permissions, task instructions, and behavioral
expectations belong in tester-authored prompts and fixtures. The runner neither
injects nor validates them.

The complete configuration shape is:

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

No other root, fixture-entry, or execution fields are accepted. `id` retains
the current path-safe identifier rules. `prompt` and each fixture `source` are
configuration-relative paths to regular files. `target` is a non-empty relative
path without `.` or `..` components. `fixtures` may be empty, but duplicate
targets are invalid. `provider` is exactly `codex` or `claude`; `model` is a
non-empty string; `effort` retains its current path-safe string syntax and is
passed through without semantic validation.

## Runtime layout

Every invocation atomically allocates a unique directory beneath the existing
fixed temporary run root:

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

`workspace/fixture/` is populated from the configured file list.
`workspace/evidence/` starts empty and is writable by the model. Runner-owned
logs and provider output remain outside the model workspace at stable paths.

The provider process runs with `workspace/` as its current working directory.
The runner does not clean or reuse a completed run directory.

## Prompt rendering

Before provider invocation, the runner performs literal replacement of these
three tokens in the prompt template:

- `{{workspace_dir}}`
- `{{fixture_dir}}`
- `{{evidence_dir}}`

Each replacement is the absolute path created for the current invocation. No
other template syntax, escaping rules, conditionals, variables, or template
engine are supported. Unknown text, including unknown brace expressions, is
passed through unchanged.

The original template is retained as `prompt-template.txt`; the rendered prompt
sent to the provider is retained as `prompt.txt`.

For example, this template:

```text
Read {{fixture_dir}}/input.txt.
Write any requested file beneath {{evidence_dir}}.
Your working directory is {{workspace_dir}}.
```

is rendered by replacing each named token with the absolute directory allocated
for that invocation. Repeated tokens are all replaced.

## Evidence

The runner continues to retain stdout, stderr, the provider's final response,
the runner log, the configuration snapshot, and the rendered prompt. It also
adds a mechanical inventory of entries present beneath `workspace/evidence/`
during run finalization. Every entry records its relative path and filesystem
type. Regular files additionally record byte count and digest using the same
artifact conventions as other retained files. The inventory does not follow
symlinks.

An empty evidence directory is valid. The runner records whether it contains
files but performs no content, schema, outcome, or quality validation. A tester
or later reviewing tool interprets all collected evidence.

## Provider invocation

Provider selection remains part of the public contract. Each adapter owns the
provider-specific command needed to run one noninteractive prompt and collect
its output. Provider flags are not exposed as general test configuration.

### Codex

Retain the existing model and effort selection, ephemeral noninteractive
execution, JSON output capture, last-message capture, workspace current
directory, `workspace-write` sandbox, and Git-repository bypass needed for a
standalone fixture workspace.

Remove the existing flags that suppress user configuration and instructions,
force approval behavior, or enable unrelated features:

- `--ask-for-approval never`
- `--search`
- `--strict-config`
- `--ignore-user-config`
- `--ignore-rules`

Codex otherwise runs with its installed configuration and normal permission
safeguards. Prompt text may state task authorization, but it does not override
CLI or sandbox enforcement.

### Claude

Retain noninteractive print execution, no session persistence, raw output
capture, model selection, effort selection, and normal Claude Code permission
safeguards. Remove safe mode, Chrome suppression, structured-output options,
verbosity options, and permission-bypass options. Claude's ordinary print-mode
stdout is retained as both `stdout.txt` and, after a zero exit, `final.txt`.
Codex continues to write `final.txt` through its last-message output option.
`final.txt` is absent when the selected provider does not complete a final
response.

Launch Claude by adding this fixed environment to the inherited process
environment, matching the owner's current local test baseline and preserving
its normal OAuth authentication:

```text
CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=1
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
CLAUDE_CODE_DISABLE_BUNDLED_SKILLS=1
CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1
CLAUDE_CODE_DISABLE_WORKFLOWS=1
CLAUDE_CODE_DISABLE_ARTIFACT=1
CLAUDE_CODE_DISABLE_CRON=1
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

This is intentionally a local optimized baseline, not a portable environment
configuration system. Plugin, project, and user-installed skills remain
available. General provider-environment customization is deferred until a
concrete need exists.

## Errors and validation

Keep validation mechanical and limited to what the runner must safely load or
create: exact configuration shape, supported schema version and provider,
required scalar types, regular prompt and fixture source files, safe relative
fixture targets, unique targets, and filesystem failures.

Do not add semantic prompt checks, required template-token checks, skill checks,
dependency checks, evidence expectations, provider capability checks, result
judgment, retries, or compatibility abstractions.

Exit `0` means the run completed mechanically. Exit `1` means an owned-run,
provider, timeout, or artifact-persistence failure. Exit `2` means usage or
configuration failure before a run directory is owned. The infrastructure error
codes remain exactly `PREPARATION_FAILED`, `PROVIDER_LAUNCH_FAILED`,
`PROVIDER_TIMEOUT`, `PROVIDER_EXIT_NONZERO`, and `ARTIFACT_WRITE_FAILED`.

## Migration and verification

Implementation updates the runner tests and documentation, performs the catalog
migration reset defined below, and does not migrate a behavioral catalog. Fresh
catalog migration begins only after the redesigned runner is accepted. The
configuration, prompt-rendering, and result examples in this specification are
copied into the updated runner documentation after implementation is verified.

Verification consists of:

1. the runner unit and acceptance suite;
2. a configuration-shape check for both retained provider smoke definitions;
3. one approved end-to-end Codex smoke invocation;
4. one approved end-to-end Claude smoke invocation using the fixed local baseline;
5. mechanical inspection that each smoke produced the required stable artifacts
   and a valid evidence inventory.

The smoke runs do not judge whether the model answered correctly.

## Result contract

The incompatible runner redesign replaces the existing numeric result schema
version `1` with the string version `"0.2"`. A result contains exactly these
top-level fields:

| Field | Type |
|---|---|
| `schema_version` | Exact string `"0.2"`. |
| `run_id` | String allocated by the runner. |
| `status` | `COMPLETED` or `INFRA_ERROR`. |
| `started_at` | UTC timestamp string. |
| `finished_at` | UTC timestamp string. |
| `duration_seconds` | Non-negative number. |
| `test` | Object containing exactly `id`. |
| `execution` | Mechanical provider invocation record. |
| `artifacts` | Fixed artifact records described below. |
| `infrastructure_error` | `null` or the existing exact `code` and `message` object. |

`execution` contains exactly `provider`, `model`, `effort`, `executable`,
`timeout_seconds`, `invocation_started`, `timed_out`, and `exit_code`, retaining
their current meanings and types.

`artifacts` contains exactly:

| Field | Stable path | Record type |
|---|---|---|
| `config` | `config.json` | File artifact. |
| `prompt_template` | `prompt-template.txt` | File artifact. |
| `prompt` | `prompt.txt` | File artifact. |
| `stdout` | `stdout.txt` | File artifact. |
| `stderr` | `stderr.txt` | File artifact. |
| `final` | `final.txt` | File artifact. |
| `fixture` | `workspace/fixture` | Directory artifact. |
| `evidence` | `workspace/evidence` | Directory artifact. |

A file artifact contains exactly `path`, `exists`, `bytes`, and `sha256`.
`bytes` and `sha256` are non-null only when `exists` is true.

A directory artifact contains exactly `path`, `exists`, `empty`, and `entries`.
When the directory exists, `empty` is a Boolean and `entries` is its
lexicographically path-sorted recursive inventory. When it does not exist,
`empty` is `null` and `entries` is empty.

Each directory entry contains exactly `path`, `type`, `bytes`, and `sha256`.
`path` is relative to its directory artifact. `type` is exactly `file`,
`directory`, `symlink`, or `other`. Regular files have non-null `bytes` and
`sha256`; every other type has `null` for both. Inventory does not follow
symlinks. The fixture inventory describes the freshly copied fixture before
provider invocation; the evidence inventory describes evidence at finalization,
including after provider timeout or nonzero exit.

An abbreviated completed result is:

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

The angle-bracket digest values illustrate the required shape and are not
literal valid results. The implementation's JSON Schema encodes these exact
objects, required fields, closed property sets, conditional nullability, and
status/error relationship.

## Catalog migration reset

The existing packaged scenarios were produced for the retired skill-aware
contract and will not be converted in place. Implementation performs this exact
reset:

- remove every existing migrated test package beneath
  `skill-validation/scenarios/`;
- rewrite `skill-validation/scenarios/README.md` as an empty active migration
  inventory against schema `"0.2"`;
- delete the active draft
  `plans/2026-08-26-adversarial-review-catalog-migration.md`;
- reset Phase 3 of `plans/2026-08-24-scenario-porting-roadmap.md` to zero
  migrated catalogs and remove its completed-wave links;
- retain the completed migration plans in `plans/completed/` as historical
  records;
- retain unrelated deferred plans, including the Codex-versus-Claude review
  catalog.

After the runner redesign is accepted, Phase 3 restarts from its first catalog.
Each catalog receives a fresh migration plan against schema `"0.2"`, explicit
tester-authored skill instructions, individual fixture files, and its own
end-to-end mechanical smoke run.

## Controlled provider acceptance smoke

Runner acceptance includes one retained Codex smoke definition and one retained
Claude smoke definition using the same controlled prompt and fixture. Each
configuration selects its provider normally; neither uses catalog content or
asserts skill behavior.

The fixture contains one small text file. The prompt uses all three runtime
tokens, directs the provider to read the fixture, write one named regular file
beneath the evidence directory, and return a final response. Acceptance checks
only runner mechanics:

1. schema `"0.2"` loads;
2. a unique run directory and fixed workspace directories exist;
3. the fixture file was copied byte-for-byte to its declared target;
4. all three prompt tokens were replaced with the current run's absolute paths;
5. the configured provider was invoked once in the workspace directory;
6. stdout, stderr, and final-response artifacts were written at their stable
   paths;
7. the evidence directory is non-empty and its generated file appears in the
   result inventory; and
8. `result.json` validates against the result schema.

The acceptance test does not compare response wording, inspect generated-file
contents for correctness, apply a rubric, or assign a behavioral verdict. Live
provider execution remains an explicitly approved test action.

## Non-goals

- Skill or dependency discovery, installation, injection, or validation.
- Expected-outcome storage or evaluation.
- General prompt templating.
- Directory fixture copying, merging, or symlinks.
- Configurable provider flags, commands, permissions, or environment variables.
- Internal concurrency, batching, retries, campaigns, or shared run state.
- Semantic evidence validation, scoring, or behavioral pass/fail decisions.
