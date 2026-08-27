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
| `schema_version` | Exact string `"0.1"`. |
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

## Evidence

The runner continues to retain stdout, stderr, the provider's final response,
the runner log, the configuration snapshot, and the rendered prompt. It also
adds a mechanical inventory of entries present beneath `workspace/evidence/`
when the provider finishes. Every entry records its relative path and filesystem
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

Retain noninteractive print execution, no session persistence, structured
output capture, model selection, effort selection, and normal Claude Code
permission safeguards. Remove safe mode, Chrome suppression, and permission
bypass options.

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

Existing exit-code and infrastructure-error behavior remains unless a removed
field makes a record entry obsolete.

## Migration and verification

Implementation updates the runner tests and documentation, then converts every
checked-in scenario configuration and prompt to the new contract. Skill and
dependency instructions previously assembled by the runner must become explicit
prompt text, using fixture paths where needed.

Verification consists of:

1. the runner unit and acceptance suite;
2. a configuration-shape check across all checked-in scenarios;
3. one approved end-to-end Codex invocation;
4. one approved end-to-end Claude invocation using the fixed local baseline;
5. mechanical inspection that each run produced the required stable artifacts
   and a valid evidence inventory.

The smoke runs do not judge whether the model answered correctly.

## Non-goals

- Skill or dependency discovery, installation, injection, or validation.
- Expected-outcome storage or evaluation.
- General prompt templating.
- Directory fixture copying, merging, or symlinks.
- Configurable provider flags, commands, permissions, or environment variables.
- Internal concurrency, batching, retries, campaigns, or shared run state.
- Semantic evidence validation, scoring, or behavioral pass/fail decisions.
