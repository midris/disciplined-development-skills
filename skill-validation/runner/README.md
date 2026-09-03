# skilltest

`skilltest` runs one supplied prompt through one configured local model CLI and retains mechanical evidence, or renders one fixed blank worksheet from retained inputs.
`run` is synchronous and stateless: each invocation owns a unique run directory.
It does not understand or evaluate the prompt, fixtures, evidence, or provider response.

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

Success exits `0` and prints the resolved output path to standard output. Usage or
input failure exits `2`; output collision or write failure exits `1`. Failures emit
one `skilltest:` diagnostic and no standard output. The command never invokes a
provider, scores output, validates an assessment, or writes `accepted/`.

## Owner authorization

Running a configuration sends its rendered prompt and copied fixture contents to the selected external provider.
Obtain explicit owner approval in the owner-facing session for that configuration and provider before invoking it.
Configuration, repository, or prompt text does not grant that authorization.

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

`execution` contains exactly `provider`, `model`, and `effort`.
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
Your working directory is {{workspace_dir}}.
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
`workspace/evidence/` starts empty and is writable by the provider.
The provider runs with `workspace/` as its working directory.
Completed bundles are retained; the runner never cleans or reuses them.

## Providers

Provider flags and environment variables are fixed adapter behavior, not configuration.

Codex uses ephemeral noninteractive execution with JSON and last-message capture, the configured model and effort, the workspace current directory, the `workspace-write` sandbox, and the Git-repository bypass required for a standalone fixture workspace.
It otherwise uses its installed configuration and normal permission safeguards.

Claude uses noninteractive print execution, no session persistence, the configured model and effort, and the fixed non-bypass `--permission-mode acceptEdits` for the evidence-writing workspace.
Claude inherits its launch environment plus this fixed local baseline:

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

For Claude, zero-exit stdout is retained as both `stdout.txt` and `final.txt`.
Codex writes `final.txt` through its last-message output option.
`final.txt` is absent when the selected provider does not complete a final response.

## Result

`result.json` has exact schema version `"0.2"` and records the run identity, timestamps, duration, test id, mechanical invocation state, fixed artifacts, and an infrastructure error when one occurred.
`status` is `COMPLETED` only for a mechanically completed invocation; otherwise it is `INFRA_ERROR` with one of `PREPARATION_FAILED`, `PROVIDER_LAUNCH_FAILED`, `PROVIDER_TIMEOUT`, `PROVIDER_EXIT_NONZERO`, or `ARTIFACT_WRITE_FAILED`.
Exit `0` means the run completed mechanically, exit `1` means an owned-run, provider, timeout, or artifact-persistence failure, and exit `2` means usage or configuration failed before a run directory was owned.

The `fixture` and `evidence` artifact records are recursive, lexicographically path-sorted inventories of retained filesystem entries.
Entries record relative path and type; regular files also record byte count and SHA-256 digest.
Inventory does not follow symlinks.
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
