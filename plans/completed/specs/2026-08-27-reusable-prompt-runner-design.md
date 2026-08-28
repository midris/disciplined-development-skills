# Reusable Prompt Runner Design

## Status

Implemented and accepted by the owner on 2026-08-28 after whole-branch review
and live Codex and Claude smoke tests. This design replaces the runner's
skill-specific input contract with a small, stateless prompt-execution contract.
The completed implementation plan is archived beside this specification.

## Purpose

`skilltest` runs one supplied prompt against one configured local model CLI and
retains mechanical evidence from that invocation. It prepares an isolated input
and output area, but it does not understand the prompt, skills, dependencies, or
the meaning of the result.

The runner remains synchronous and single-run. Separate invocations may safely
use the same configuration concurrently because every invocation owns a unique
run directory and shares no mutable runner state.

## Configuration contract

The configuration is a UTF-8 RFC 8259 JSON object. Parsing rejects duplicate
object keys and the non-JSON constants `NaN`, `Infinity`, and `-Infinity`.
The object contains exactly:

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
directories, accept a source entry that is a symlink, create symlinks, merge
directories, infer includes, or interpret file contents. Parent directories
required by a target are created mechanically. Fixture targets must be pairwise
non-conflicting: no two targets may be equal, and neither target may be a
path-component ancestor of the other. A fresh run never merges or overwrites
fixture inputs.

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

No other root, fixture-entry, or execution fields are accepted. `id` is a
1–64-character string matching `[a-z0-9][a-z0-9-]{0,63}`. `prompt` and each
fixture `source` are non-empty relative paths interpreted from the configuration
directory; absolute paths are invalid. They may contain `..` and resolve outside
the configuration directory so a tester can deliberately select any locally
available regular file. The final path itself must not be a symlink; ordinary
operating-system resolution of symlinked ancestor directories is accepted.
`target` is a canonical slash-separated relative file path. Backslashes,
leading or trailing slashes, repeated slashes, and empty, `.` or `..`
components are invalid. Conflict checks compare the component tuples obtained
by splitting each accepted target on `/`. `fixtures` may be empty, but their
targets must satisfy the pairwise conflict rule above. `provider` is exactly
`codex` or `claude`; `model` is a non-empty string; `effort` matches
`[a-z0-9][a-z0-9-]*` and is passed through without semantic validation.

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
entries but performs no content, schema, outcome, or quality validation. A
tester or later reviewing tool interprets all collected evidence.

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
capture, model selection, effort selection, and fixed non-bypass
`--permission-mode acceptEdits` for the evidence-writing workspace. Remove safe
mode, Chrome suppression, structured-output options, verbosity options, and
permission-bypass options. Claude's ordinary print-mode stdout is retained as
both `stdout.txt` and, after a zero exit, `final.txt`.
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
create: strict JSON parsing, exact configuration shape, supported schema version
and provider, required scalar types, regular prompt and fixture source files,
canonical relative fixture targets, pairwise non-conflicting targets, and
filesystem failures.

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
2. a configuration-shape check for both newly created provider smoke definitions;
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
| `infrastructure_error` | `null` or the exact `code` and `message` object defined below. |

`run_id` is a non-empty string. `started_at` and `finished_at` match
`YYYY-MM-DDTHH:MM:SS.mmmZ`. `duration_seconds` is a non-negative number.

`test` contains exactly `id`, a string satisfying the same path-safe identifier
rule as the configuration.

`execution` contains exactly:

| Field | Type and value |
|---|---|
| `provider` | String enum `codex` or `claude`. |
| `model` | Non-empty string copied from the configuration. |
| `effort` | String matching `[a-z0-9][a-z0-9-]*`, copied from the configuration. |
| `executable` | String enum `codex` or `claude`; it matches `provider`. |
| `timeout_seconds` | Integer constant `900`. |
| `invocation_started` | Boolean. |
| `timed_out` | Boolean. |
| `exit_code` | Integer or `null`. |

The result schema permits exactly these execution states:

| Result state | `status` | `invocation_started` | `timed_out` | `exit_code` | `infrastructure_error` |
|---|---|---:|---:|---|---|
| Completed | `COMPLETED` | `true` | `false` | `0` | `null` |
| Preparation failed | `INFRA_ERROR` | `false` | `false` | `null` | Code `PREPARATION_FAILED` |
| Provider launch failed | `INFRA_ERROR` | `false` | `false` | `null` | Code `PROVIDER_LAUNCH_FAILED` |
| Provider timed out | `INFRA_ERROR` | `true` | `true` | Integer | Code `PROVIDER_TIMEOUT` |
| Provider exited nonzero | `INFRA_ERROR` | `true` | `false` | Any integer except `0` | Code `PROVIDER_EXIT_NONZERO` |
| Artifact write failed | `INFRA_ERROR` | `true` | `false` | `0` | Code `ARTIFACT_WRITE_FAILED` |

No other combination is valid. The error `message` remains mechanically
generated text and is not constrained beyond being a string.

Error precedence makes the table exhaustive. A provider launch failure,
timeout, or nonzero exit remains the recorded infrastructure error if a later
artifact write also fails; the execution fields preserve that provider outcome
and the affected artifact record shows that its file is absent. Code
`ARTIFACT_WRITE_FAILED` is used only when the provider completed with exit `0`
and a required post-invocation artifact write failed. An owned failure before
provider invocation is `PREPARATION_FAILED`.

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
`path` is the stable run-relative string specified above and `exists` is a
Boolean. When `exists` is true, `bytes` is a non-negative integer and `sha256`
is exactly 64 lowercase hexadecimal characters. When `exists` is false,
`bytes` and `sha256` are both `null`.

A directory artifact contains exactly `path`, `exists`, `empty`, and `entries`.
`path` is the stable run-relative string specified above and `exists` is a
Boolean. When the directory exists, `empty` is a Boolean equal to whether
`entries` has zero items, and `entries` is its lexicographically path-sorted
recursive inventory. When it does not exist, `empty` is `null` and `entries`
is empty.

Each directory entry contains exactly `path`, `type`, `bytes`, and `sha256`.
`path` is relative to its directory artifact. `type` is exactly `file`,
`directory`, `symlink`, or `other`. For `file`, `bytes` is a non-negative
integer and `sha256` is exactly 64 lowercase hexadecimal characters. Every
other type has `null` for both. Inventory does not follow symlinks. Both fixture
and evidence inventories describe their retained directories during
finalization, including after provider timeout or nonzero exit. The runner does
not compare final fixture contents with their initial copies or treat provider
changes as an error.

`infrastructure_error` is `null` exactly when `status` is `COMPLETED`. When
`status` is `INFRA_ERROR`, it is an object containing exactly `code` and
`message`. `code` is one of `PREPARATION_FAILED`, `PROVIDER_LAUNCH_FAILED`,
`PROVIDER_TIMEOUT`, `PROVIDER_EXIT_NONZERO`, or `ARTIFACT_WRITE_FAILED`;
`message` is a string.

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
- reset current Phase 3 progress in
  `plans/2026-08-24-scenario-porting-roadmap.md` to zero migrated catalogs;
- keep the completed-wave links in Phase 3 under a clearly labeled superseded
  schema `"0.1"` migration-wave history;
- retain the completed migration plans in `plans/completed/` as historical
  records;
- retain unrelated deferred plans, including the Codex-versus-Claude review
  catalog.

After the runner redesign is accepted, Phase 3 restarts from its first catalog.
Each catalog receives a fresh migration plan against schema `"0.2"`, explicit
tester-authored skill instructions, individual fixture files, and its own
end-to-end mechanical smoke run.

## Controlled provider acceptance smoke

Implementation creates one Codex smoke definition and one Claude smoke
definition under `skill-validation/runner/acceptance/fixtures/provider-smoke/`.
They share `prompt.md` and `fixture/input.txt`; `codex.json` selects
`gpt-5.6-sol` at low effort and `claude.json` selects `sonnet` at low effort.
Neither uses catalog content or asserts skill behavior.

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
