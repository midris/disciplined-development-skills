# Skill Test Worksheet Generator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the approved `skilltest worksheet` command that renders one fixed, unscored Markdown worksheet from one scenario package and one retained runner bundle.

**Architecture:** A new focused module reads only the scenario rubric and the existing `result.json` fields needed by the worksheet, renders the fixed Markdown in memory, and writes one caller-selected scratch file without overwriting. The existing CLI dispatches the new command and maps its input and output failures to the specified exit codes; `skilltest run` and every provider path remain unchanged.

**Tech Stack:** Python 3.11+ standard library, pytest, and the existing `uv` runner environment. Add no dependency or schema.

**Spec:** [Skill Testing Methodology Design](specs/2026-09-02-skill-testing-methodology-design.md)

## Global Constraints

- Implement only `skilltest worksheet SCENARIO RUN_BUNDLE --output PATH`.
- Invoke the command from the repository root and pass `SCENARIO` as a repository-relative path. Record that argument as supplied; do not discover or validate the repository root.
- Read only `SCENARIO/rubric.md` and `RUN_BUNDLE/result.json`. Parse only the existing result fields required by the fixed worksheet; do not validate the result schema or compare scenario and run identities.
- Populate only the mechanical worksheet fields. Leave purpose, ledger rows, readability, verdict, disposition, and methodology notes blank.
- Preserve the spec's exact UTF-8 Markdown headings, tables, row order, escaping, LF endings, and one trailing LF.
- Refuse an existing output path. Do not create its parent, choose an `accepted/` path, copy an accepted record, or add cleanup or lifecycle behavior.
- Preserve `skilltest run`, provider adapters, configuration and result schemas, scenario packages, skills, dependencies, and lockfile bytes.
- Add no assessment parsing, scoring, verdict calculation, evidence inspection, post-edit validation, model invocation, retry, repetition, comparison, or suite orchestration.
- Run all Python tests from `skill-validation/runner/`. Existing offline tests may invoke their fake provider executables; no step invokes an installed/live provider or model.
- Implement on a new `feature/skill-test-worksheet` branch in `.worktrees/skill-test-worksheet/`, based on the owner-approved commit containing this plan and its governing spec.

## File Map

- Create `skill-validation/runner/src/skilltest/worksheet.py` for input loading, fixed rendering, rubric hashing, table-cell escaping, exclusive output writing, and the two mechanical exception types.
- Create `skill-validation/runner/tests/test_worksheet.py` for exact-byte rendering and focused input/output failure contracts.
- Modify `skill-validation/runner/src/skilltest/cli.py` only to register and dispatch `worksheet` while preserving `run` behavior.
- Modify `skill-validation/runner/tests/test_cli.py` to cover the public worksheet command and retain the complete run-command contract.
- Modify `skill-validation/runner/README.md` to document the command, inputs, output, exit codes, and no-assessment boundary.

No other file is in implementation scope.

---

### Task 1: Render and write one blank worksheet

**Files:**

- Create: `skill-validation/runner/src/skilltest/worksheet.py`
- Create: `skill-validation/runner/tests/test_worksheet.py`

**Interfaces:**

- Produces: `WorksheetInputError`, raised only for unreadable, malformed, or incomplete scenario/run inputs.
- Produces: `WorksheetOutputError`, raised only for output collision or write failure.
- Produces: `write_worksheet(scenario_argument: str, run_bundle: Path, output_path: Path) -> Path`, returning the resolved written path.

- [ ] **Step 1: Write exact-output and failure tests**

Create a local test builder that writes `rubric.md` and the smallest `result.json` containing every field the renderer consumes:

Use `tmp_path / "repo"` as a temporary repository root, change into it with
`monkeypatch.chdir`, and pass a stable relative argument such as
`skill-validation/scenarios/example/worksheet-case` while creating the scenario
at that relative path.

```python
record = {
    "run_id": "20260902T120000000Z-worksheet-case-unique",
    "status": "COMPLETED",
    "started_at": "2026-09-02T12:00:00.000Z",
    "finished_at": "2026-09-02T12:00:01.000Z",
    "duration_seconds": 1.0,
    "test": {"id": "worksheet-case"},
    "execution": {
        "provider": "codex",
        "model": "gpt-5.6-sol",
        "effort": "high",
    },
    "artifacts": {
        "config": {"path": "config.json", "sha256": "a" * 64},
        "prompt_template": {
            "path": "prompt-template.txt",
            "sha256": "b" * 64,
        },
        "prompt": {"path": "prompt.txt", "sha256": "c" * 64},
        "fixture": {
            "entries": [
                {
                    "path": "skills/example/SKILL.md",
                    "type": "file",
                    "sha256": "d" * 64,
                },
                {
                    "path": "sources/input.md",
                    "type": "file",
                    "sha256": "e" * 64,
                },
            ]
        },
    },
    "infrastructure_error": None,
}
```

Cover these behavioral rows without introducing a schema-test matrix:

- completed result with two fixture files produces the spec's complete literal worksheet, exact rubric SHA-256, empty assessment cells, LF endings, and one trailing LF;
- a directory or symlink fixture entry emits no row, while regular-file rows retain recorded order;
- no regular fixture files emits no Fixture row;
- `null` artifact digests and `null` infrastructure error values render as empty cells;
- infrastructure error text and scenario/path values exercise the exact backslash, pipe, CRLF, carriage-return, and line-feed escaping order;
- `duration_seconds` renders with `str()`;
- missing scenario directory, rubric, run bundle, result file, malformed JSON, or one required result field raises `WorksheetInputError` before the output path exists;
- an existing output remains byte-for-byte unchanged and raises `WorksheetOutputError`;
- a missing output parent raises `WorksheetOutputError`;
- a narrowly monkeypatched `Path.open` that raises `OSError` only for the selected
  output path produces `WorksheetOutputError` without affecting input reads.

Assert the renderer does not require unused result-schema fields and does not inspect `final.txt`, evidence files, scenario `test.json`, or the run marker.

- [ ] **Step 2: Run the focused test and observe RED**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_worksheet.py
```

Expected: collection fails because `skilltest.worksheet` does not exist.

- [ ] **Step 3: Implement the minimal worksheet module**

Define only the public boundary needed by Task 2:

```python
class WorksheetInputError(Exception):
    """The declared worksheet inputs cannot produce the fixed sheet."""


class WorksheetOutputError(Exception):
    """The completed worksheet text cannot be written as requested."""


def write_worksheet(
    scenario_argument: str,
    run_bundle: Path,
    output_path: Path,
) -> Path:
    """Render one blank worksheet, write it exclusively, and return its resolved path."""
```

Keep all helpers private and local to `worksheet.py`:

- read and hash `Path(scenario_argument) / "rubric.md"` as bytes;
- read `run_bundle / "result.json"` as UTF-8 and decode it with `json.loads`;
- extract only the exact scalar, artifact, infrastructure-error, and fixture-entry fields shown in the spec;
- render the rubric display path by adding `/rubric.md` to the supplied scenario text, avoiding a doubled slash when it already ends in `/`;
- include only fixture entries whose `type` equals `"file"`, in recorded order;
- convert `None` to an empty cell and `duration_seconds` with `str()`;
- apply the spec's cell escaping in its exact order;
- assemble the entire worksheet in memory before opening the output;
- write with exclusive creation, UTF-8, LF newlines, and the already-rendered trailing LF;
- translate only input read/decode/required-field failures to `WorksheetInputError` and output collision/write failures to `WorksheetOutputError`.

Do not import `jsonschema`, the runner, provider modules, or scenario configuration code. Do not add a generalized renderer, template file, result model, validation helper, or output publication framework.

- [ ] **Step 4: Run focused tests and verify GREEN**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_worksheet.py
git diff --check
```

Expected: every worksheet test passes and the diff check reports no errors.

- [ ] **Step 5: Inspect and commit the renderer**

Confirm the diff contains only `worksheet.py` and `test_worksheet.py`, the test uses no provider, and production code contains no scoring or schema validation. Then commit:

```bash
cd "$(git rev-parse --show-toplevel)"
git add skill-validation/runner/src/skilltest/worksheet.py skill-validation/runner/tests/test_worksheet.py
git commit -m "feat(validation): render skill test worksheets"
```

---

### Task 2: Expose the worksheet command and document it

**Files:**

- Modify: `skill-validation/runner/src/skilltest/cli.py`
- Modify: `skill-validation/runner/tests/test_cli.py`
- Modify: `skill-validation/runner/README.md`

**Interfaces:**

- Consumes: `write_worksheet`, `WorksheetInputError`, and `WorksheetOutputError` from Task 1.
- Produces: `skilltest worksheet SCENARIO RUN_BUNDLE --output PATH` with the exact exit and output-channel contract from the spec.
- Preserves: `skilltest run CONFIG` argument parsing, diagnostics, stdout bundle path, and exit codes.

- [ ] **Step 1: Write failing public-command tests**

Extend the existing black-box CLI coverage with:

```text
skilltest worksheet SCENARIO RUN_BUNDLE --output PATH
```

Let the test's local subprocess helper accept an optional `cwd` and invoke successful
worksheet cases from a temporary repository root with a repository-relative
`SCENARIO` argument. Keep existing run-command invocations on their current path.

Cover only these public rows:

- missing or extra arguments exit `2`, write argparse usage to stderr, and write no stdout;
- valid inputs exit `0`, write no stderr, print the resolved output path plus one LF, and create the exact worksheet;
- malformed or incomplete input exits `2`, prints one `skilltest:` diagnostic, emits no stdout, and creates no output;
- an existing output or missing output parent exits `1`, prints one `skilltest:` diagnostic, emits no stdout, and preserves any existing bytes;
- `skilltest --help` lists both `run` and `worksheet` and still lists no lifecycle command;
- every existing `skilltest run` assertion remains unchanged and green.

- [ ] **Step 2: Run the CLI test and observe RED**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_cli.py
```

Expected: worksheet invocations fail because the parser does not recognize the command.

- [ ] **Step 3: Add the thin CLI dispatch**

Register exactly two positional arguments and one required option:

```python
worksheet = commands.add_parser("worksheet")
worksheet.add_argument("scenario", metavar="SCENARIO")
worksheet.add_argument("run_bundle", metavar="RUN_BUNDLE")
worksheet.add_argument("--output", required=True, metavar="PATH")
```

Dispatch `run` through the existing path without changing its behavior. For `worksheet`, call `write_worksheet(parsed.scenario, Path(parsed.run_bundle), Path(parsed.output))`; print the returned resolved path on success, map `WorksheetInputError` to exit `2`, map `WorksheetOutputError` to exit `1`, prefix both diagnostics with `skilltest:`, and emit no stdout on failure.

Update only the stale `cli.py` module/function wording that describes `run` as the
sole command; do not restructure its existing run dispatch beyond the branch needed
for the new subcommand.

Do not add shared outcome types, callback dispatch, a command registry, or changes to `runner.py`.

- [ ] **Step 4: Document the public command**

Adjust the README's opening sentence so it covers both mechanical operations, then
add one concise `Worksheet` section after the existing `Run` section. Document:

- the exact command and repository-root invocation requirement;
- scenario, run-bundle, and nonexisting scratch-output inputs;
- that only mechanical fields are populated;
- that the orchestrator completes and reviews the worksheet;
- exit codes `0`, `1`, and `2` and the successful stdout path;
- that the command never invokes a provider, scores output, validates an assessment, or writes `accepted/`.

Do not duplicate the full worksheet template or methodology verdict rules in the
runner README; link to
`../../plans/specs/2026-09-02-skill-testing-methodology-design.md` instead.

- [ ] **Step 5: Run focused and full offline verification**

```bash
cd "$(git rev-parse --show-toplevel)/skill-validation/runner"
uv run pytest -q tests/test_worksheet.py tests/test_cli.py
uv run pytest -q
git diff --check
```

Expected: focused worksheet/CLI tests and the complete default offline runner suite pass; no acceptance test, installed/live provider, or model is invoked; the diff check reports no errors. Existing fake-provider subprocess tests remain ordinary offline coverage.

- [ ] **Step 6: Inspect and commit the public command**

Confirm the complete implementation changes exactly the five files in this plan, `skilltest run` retains its prior tests and behavior, and no dependency, schema, provider, scenario, skill, or lifecycle file changed. Then commit:

```bash
cd "$(git rev-parse --show-toplevel)"
git add skill-validation/runner/src/skilltest/cli.py skill-validation/runner/tests/test_cli.py skill-validation/runner/README.md
git commit -m "feat(validation): expose worksheet generation"
```

## Final Gate

After both commits, rerun the Task 2 focused and full offline verification commands from a clean worktree and report the two commit hashes and exact results to the owner.

Stop there. Do not invoke a provider, run `DR-02`, create or replace an `accepted/` record, edit a scenario or skill, push, merge, archive this plan, or remove the branch/worktree without new explicit approval.
