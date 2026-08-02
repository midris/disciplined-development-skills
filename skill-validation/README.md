# Skill validation protocol

This file is the single source of truth for skill-validation rules, shared infrastructure, audit status, and cross-skill score summaries.
Individual records own their active scenario catalogs, result summaries, and preserved historical evidence.

## Roles and model policy

- The orchestrator owns validation-bearing tasks, dispatch, result inspection, manual scoring, scorer and reviewer dispatch, user approval gates, commits, and Gate 5.
- Evaluators, scorers, and reviewers are fresh, bounded, read-only processes with nested-agent tools disabled.
- Skill authoring, validation design, behavioral evaluation, scoring, and cold review use `gpt-5.6-sol` at high reasoning effort.
- Sol low is limited to Tasks 11 and 27 and post-freeze control backfills.
- Every behavioral scenario uses five fresh evaluator processes, with at most three running concurrently.
- `research/replay_codex.py` reviews historical diffs and writes research results; it is not a skill-scenario runner.

## Audit index

`Keep`, `Repair`, `Merge`, `Retire`, and `Add` are scenario counts, not file counts.
An em dash means the owning audit task has not classified the scenarios yet.

| Record | Kind | Owner | Affected skills | Audit task | Status | Keep | Repair | Merge | Retire | Add |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|
| [adversarial-review](adversarial-review.md) | Skill | `adversarial-review` | `adversarial-review`; mapped composition skills pending audit | 7 | Unaudited | — | — | — | — | — |
| [adversarial-review-loop](adversarial-review-loop.md) | Skill | `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development` | 8 | Unaudited | — | — | — | — | — |
| [concise-writing](concise-writing.md) | Skill | `concise-writing` | `concise-writing`, `adversarial-review-loop`; external authoring dependencies | 2 | Audited; Task 2A verified | 0 | 2 | 4 | 2 | 8 |
| [disciplined-development](disciplined-development.md) | Skill | `disciplined-development` | all nine skills through orchestration | 10 | Unaudited | — | — | — | — | — |
| [disciplined-research](disciplined-research.md) | Skill | `disciplined-research` | `disciplined-research`; mapped composition skills pending audit | 3 | Unaudited | — | — | — | — | — |
| [dispatching-development-subagents](dispatching-development-subagents.md) | Skill | `dispatching-development-subagents` | `dispatching-development-subagents`, `disciplined-development` | 9 | Unaudited | — | — | — | — | — |
| [lean-plan-writing](lean-plan-writing.md) | Skill | `lean-plan-writing` | `lean-plan-writing`; mapped composition skills pending audit | 4 | Unaudited | — | — | — | — | — |
| [sweeping-stale-references](sweeping-stale-references.md) | Skill | `sweeping-stale-references` | `sweeping-stale-references`; mapped composition skills pending audit | 5 | Unaudited | — | — | — | — | — |
| [writing-explicit-rationale](writing-explicit-rationale.md) | Skill | `writing-explicit-rationale` | `writing-explicit-rationale`; mapped composition skills pending audit | 6 | Unaudited | — | — | — | — | — |
| [adversarial-review-loop scenarios](adversarial-review-loop-scenarios.md) | Supporting | `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development` | 8 | Unaudited | — | — | — | — | — |
| [duplicate red-flags scenarios](duplicate-red-flags-scenarios.md) | Supporting history | Task 1 protocol | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references` | 1 | Audited | 0 | 0 | 0 | 4 | 0 |
| [evaluation subagents read-only](evaluation-subagents-read-only.md) | Project-rule history | Task 1 protocol | Repository evaluation rule | 1 | Audited | 0 | 0 | 0 | 1 | 0 |
| [skill discovery](skill-discovery.md) | Shared active suite | Task 1 protocol | all nine skills | 1 | Audited | 0 | 0 | 0 | 0 | 9 |

## Framework inventory

“Full” recoverability means the exact evaluator-facing prompt and an explicitly evaluator-withheld rubric are present.
“Partial” means a scenario can be reconstructed conceptually but not replayed byte-for-byte under this protocol.

| File | Purpose and owner | Affected skills | Existing IDs and repetitions | Prompt/rubric recoverability | Active disposition |
|---|---|---|---|---|---|
| `README.md` | Universal protocol and audit index; Task 1 protocol | All | Not a scenario record | Not applicable | Active source of truth |
| `adversarial-review-loop-scenarios.md` | Canonical loop decision suite; `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development` | `CS`, `T2`–`T7`, `NF`, `PW`, `XL`, `G3A`–`G3C`; 5 reps for `NF`/`T3`/`T4`, 3 for the other 10 | Full, but model/context metadata and 5-rep normalization remain | Audit in Task 8 |
| `adversarial-review-loop.md` | Narrative history and result ledger; `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development` | Canonical IDs by link; later ownership scenarios lack IDs; mixed 1–5 reps | Partial | Audit in Task 8 |
| `adversarial-review.md` | Historical derivation of angles, verdict, scope, unexercised-case, and invariant-severity contracts; `adversarial-review` | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references`, `disciplined-development` | No stable active IDs; heterogeneous 1–8 reps, plus one 5-per-arm shared cell | Partial; several fixtures are only narrative or scratch-referenced | Audit in Task 7 |
| `concise-writing.md` | Active verbosity, over-trim, routing, ownership, composition-pressure, direct-invocation, and extraction suite; `concise-writing` | `concise-writing`, `adversarial-review-loop`; external authoring dependencies | `CW-01`–`CW-14`; five control and Task 2A target repetitions complete | Full | Baseline and Task 2A GREEN, cold review, approval, and repository verification complete |
| `disciplined-development.md` | Parent scope, Principle 7, and routing evidence; `disciplined-development` | All through orchestration | Linked `DISC-01`–`DISC-09`, 5 control and 5 target reps each; older scope 4 RED/3 GREEN, threshold 1 control/3 GREEN, routing 3 per arm | Full for the linked discovery suite; partial for older evidence | Linked suite active; audit older evidence in Task 10 |
| `disciplined-research.md` | B1/B17 grounding experiments; `disciplined-research` | `disciplined-research` | Historical `B1`, `B17`; mixed 2–6 reps | Partial; exact prompts absent and one run leaked an answer key | Audit in Task 3 |
| `dispatching-development-subagents.md` | Nudge, prompt-contract, identity, and audience evidence; `dispatching-development-subagents` | `dispatching-development-subagents`, `disciplined-development` | Named Tests 1–3; mixed 1–5 reps | Partial | Audit in Task 9 |
| `duplicate-red-flags-scenarios.md` | Four-skill composite consolidation fixture; Task 1 protocol | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references` | Cells `A`–`D`; 5 per arm | Full | Retired from the active suite because it combines unrelated contracts; preserved as history until Tasks 2, 4, 5, and 7 atomize retained coverage |
| `evaluation-subagents-read-only.md` | Historical evidence for choosing a no-write evaluator type; Task 1 protocol | Repository evaluation rule | No stable ID; RED/GREEN counts unstated | Partial | Retired from the active suite; the enforced transport probe below replaces instruction-only evidence |
| `lean-plan-writing.md` | Consolidation and unexercised-case evidence; `lean-plan-writing` | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references` | No stable IDs; shared cell 5 per arm; edge scenarios 5 per condition | Partial except the linked shared cell | Audit in Task 4 |
| `skill-discovery.md` | Atomic all-nine description routing; Task 1 protocol | All nine | `DISC-01`–`DISC-09`; 5 each | Full | Active |
| `sweeping-stale-references.md` | Rename, grouping, and packaging evidence; `sweeping-stale-references` | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references` | No stable IDs; shared cell 5 per arm, rename 1 per arm, grouping 1 RED/3 GREEN | Partial except the linked shared cell | Audit in Task 5 |
| `writing-explicit-rationale.md` | Reviewer-visible rationale and routing evidence; `writing-explicit-rationale` | `writing-explicit-rationale` | No stable IDs; formal control 3/GREEN 5, routing 3 per arm, earlier 8 GREEN | Partial | Audit in Task 6 |

## Enforced evaluator transport

Codex CLI 0.146.0 is the selected fresh-context transport.
`--sandbox read-only` enforces no repository writes, and `agents.enabled=false` removes nested-agent tools.
`--disable multi_agent` is insufficient in this CLI and must not substitute for `agents.enabled=false`.

Use one new process and one new output path per repetition:

```bash
codex --ask-for-approval never exec \
  --strict-config \
  --ignore-user-config \
  --ignore-rules \
  --ephemeral \
  -c 'agents.enabled=false' \
  --sandbox read-only \
  --skip-git-repo-check \
  --model gpt-5.6-sol \
  -c 'model_reasoning_effort="high"' \
  -C "$EVAL_ROOT" \
  --output-last-message "$RUN_OUTPUT" \
  - < "$EVALUATOR_PROMPT"
```

`EVAL_ROOT` contains only the immutable material and task context declared by the scenario.
`RUN_OUTPUT` and prompts live in scratch space outside the repository.
Replace `high` with `low` only for an authorized comparative arm.

### Transport probe evidence

The selected command was probed on 2026-08-01 with `gpt-5.6-sol` at high effort.
An `apply_patch` attempt to create `evaluator-write-probe.txt` was rejected, the file remained absent, `git status` and both tracked diffs remained clean, and no nested-agent tool was exposed.
One provider 503 produced no final response and was recorded as infrastructure error 1/3 before the identical retry passed.
A discarded preliminary probe proved that feature-flag-only disabling still exposed `spawn_agent`; it is not an approved transport configuration.

## Immutable control bundles

Every regression control, target control, and immediate readability control is materialized outside the repository before use.
The bundle contains all scenario-supplied skill files and declared dependencies, is identified by commit plus hashes, and is made read-only after creation.
Never use a mutable working tree as a control arm.

Task 1 materialized the nine-skill regression source bundle from full commit `4296647f0dff48a9e77b979ef07e813bf1f66db2`.
The deterministic `git archive` SHA-256 is `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`.
Its dependency manifest is exactly the following repository-relative path list, all at that commit; Task 1 discovery supplied only descriptions extracted from these files and had no external dependency:

```text
skills/adversarial-review-loop/SKILL.md
skills/adversarial-review/SKILL.md
skills/concise-writing/SKILL.md
skills/disciplined-development/SKILL.md
skills/disciplined-research/SKILL.md
skills/dispatching-development-subagents/SKILL.md
skills/lean-plan-writing/SKILL.md
skills/sweeping-stale-references/SKILL.md
skills/writing-explicit-rationale/SKILL.md
```

Materialize that exact bundle with the paths above appended after `--` in the same order:

```bash
CONTROL_COMMIT=4296647f0dff48a9e77b979ef07e813bf1f66db2
CONTROL_ROOT=/absolute/scratch/path/control-4296647
CONTROL_TAR=/absolute/scratch/path/control-4296647.tar
git archive "$CONTROL_COMMIT" -- \
  skills/adversarial-review-loop/SKILL.md \
  skills/adversarial-review/SKILL.md \
  skills/concise-writing/SKILL.md \
  skills/disciplined-development/SKILL.md \
  skills/disciplined-research/SKILL.md \
  skills/dispatching-development-subagents/SKILL.md \
  skills/lean-plan-writing/SKILL.md \
  skills/sweeping-stale-references/SKILL.md \
  skills/writing-explicit-rationale/SKILL.md \
  > "$CONTROL_TAR"
mkdir "$CONTROL_ROOT"
tar -xf "$CONTROL_TAR" -C "$CONTROL_ROOT"
chmod -R a-w "$CONTROL_ROOT" "$CONTROL_TAR"
shasum -a 256 "$CONTROL_TAR"
```

For a later scenario, record a manifest entry for every supplied file as `<source kind> <full revision or package version> <source path> <bundle-relative path>`.
Archive same-repository entries as above; copy declared external dependencies into their manifest paths from the recorded immutable package version.
After making the bundle read-only, generate a canonical content manifest and its aggregate hash:

```bash
(cd "$CONTROL_ROOT" && find . -type f -print0 | LC_ALL=C sort -z | xargs -0 shasum -a 256) > "$CONTROL_ROOT.sha256"
shasum -a 256 "$CONTROL_ROOT.sha256"
```

Verify every same-repository entry before use by comparing its recorded file hash with `git show "$CONTROL_COMMIT:$REPO_PATH" | shasum -a 256`; verify external entries against their recorded source hashes.
Before baseline testing, every live skill file matched its control hash:

| Skill | SHA-256 |
|---|---|
| `adversarial-review-loop` | `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6` |
| `adversarial-review` | `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c` |
| `concise-writing` | `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72` |
| `disciplined-development` | `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec` |
| `disciplined-research` | `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50` |
| `dispatching-development-subagents` | `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500` |
| `lean-plan-writing` | `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac` |
| `sweeping-stale-references` | `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157` |
| `writing-explicit-rationale` | `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe` |

Each scenario catalog declares any additional dependency or fixture before dispatch.
Materialize that dependency from its recorded version into the same read-only bundle and update the aggregate hash.
After a portability GREEN, materialize the committed post-portability skill and its declared dependencies the same way; that bundle becomes the immediate readability control while `4296647` remains the original-behavior control.

## Scenario taxonomy and active catalogs

Scenario type and behavior status are separate axes.

- **Discovery:** route from descriptions only.
- **Simple application:** exercise the core workflow with one uncomplicated request.
- **Non-trivial application:** exercise competing constraints, pressure, or edge conditions.
- **Direct invocation:** invoke the skill safely with the environment declared for its category.
- **Portability/extraction:** run a portable skill with only declared external dependencies and a non-software task.
- **Focused regression:** protect a demonstrated branch, boundary, output contract, or failure mode.
- **Composition:** test cross-skill ownership or orchestration; use a composite prompt only when composition is the behavior under test.
- **Preservation:** established behavior whose `4296647` control must pass 5/5.
- **Target:** approved new behavior with a watched control RED and a 5/5 GREEN before it joins active regression coverage.

Use atomic prompts for individual promises.
A skill’s complete active suite is its owned scenarios plus every shared discovery, direct-invocation, portability, and composition scenario that lists it as affected.
Every shared or supporting record has exactly one owner and lists every affected skill.

Each active catalog has a definition table and a results table.
The definition table contains scenario ID, owner, affected skills, type and preservation/target status, protected promise, protected skill section, supplied skill context, exact prompt or fixture link, evaluator-withheld rubric, and rerun triggers.
The results table contains scenario ID, control bundle commit and hash, Sol-high control result, target GREEN when applicable, cleaned Sol-high result, Sol-low control and cleaned scores, run date, and infrastructure-error count.
Metadata identical for every scenario in one shared record may be stated once directly
above its table instead of repeated as columns. Scenario-varying fields, aggregate
outcomes, and all per-repetition outcomes remain in the tables.

Preserve superseded, invalidated, retired, and historical evidence below the active catalog rather than rewriting history.

## Run and scoring protocol

Record the scenario ID, run date, exact prompt and fixture, bundle commit and hash, model and reasoning effort, Codex CLI version, Superpowers version, sibling skills supplied, five per-repetition outcomes, exact missed criteria, and infrastructure errors.
Evaluator prompts never contain or point to the rubric.
The orchestrator manually scores every completed behavioral response against every observable criterion.
One missed criterion fails that response; do not average, discard, or replace behavioral failures.
A scenario passes only at 5/5.
Changing prompt wording after a failure restarts that scenario at zero.
Do not commit raw evaluator or scorer transcripts.

An infrastructure error produces no evaluable response.
Record it separately and retry without changing the behavioral denominator.
After three consecutive infrastructure errors for one scenario and configuration, stop and surface the blocker.

### Subjective comparisons

Generate five fresh immutable-control outputs and five fresh draft outputs with identical prompts, rubrics, supplied context, model, and effort.
Replace arm labels with opaque IDs before scoring.
A separate fresh scorer receives only the withheld rubric and opaque outputs, never the control/draft mapping.
Hash the scorer’s record before revealing the mapping, then record the scored summary and mapping; keep outputs and mapping scratch outside the repository.

Task 1’s replayable isolation check ran on 2026-08-01 with a fresh `gpt-5.6-sol` high-effort scorer through the enforced transport above and no sibling skills.
The scorer received this exact evaluator-withheld rubric: PASS only if an output states the selected decision, a causal reason, and an explicit accepted tradeoff.
Its opaque fixtures were exactly:

```text
X7: We chose SQLite for the offline-first client because it removes a network dependency during field use. We accept lower write concurrency than a client-server database.
Q2: We chose SQLite for the offline-first client.
```

The scorer received this exact prompt:

```text
You are a fresh, read-only scorer.
Do not inspect files, use tools, edit anything, or dispatch agents.
Score each opaque output independently against this evaluator-withheld rubric:

PASS only if the output states all three observable elements:
1. the selected decision;
2. a causal reason for that decision;
3. an explicit accepted tradeoff.

Opaque output X7:
We chose SQLite for the offline-first client because it removes a network dependency during field use. We accept lower write concurrency than a client-server database.

Opaque output Q2:
We chose SQLite for the offline-first client.

Return exactly three lines in this order:
X7: PASS or X7: FAIL — <missed criteria>
Q2: PASS or Q2: FAIL — <missed criteria>
Frozen-score summary: <pass count> PASS, <fail count> FAIL
```

The prompt did not contain the arm mapping.
The scorer returned `X7: PASS`, `Q2: FAIL — missing causal reason and explicit accepted tradeoff`, and `Frozen-score summary: 1 PASS, 1 FAIL`.
The canonical bytes were the UTF-8 bytes written by `--output-last-message`; the
three-line file had no final newline. They were frozen with
`shasum -a 256 "$RUN_OUTPUT"` at SHA-256
`b54f38b0901c4cbc2eda6fa3bc745a2499d2978880c953dd61f307ec04ee2c96`.
Only after that hash was recorded was the mapping revealed: `X7` was the complete control output and `Q2` was the incomplete draft output.

## Failure and invalidation rules

A preservation result below 5/5 stops the owning task before skill edits or rubric weakening.
Classify it as a flawed scenario/rubric, genuine skill inconsistency requiring user-approved RED/GREEN work, or inherent variance requiring an explicit observable contract and redesigned scenario.

After Task 11 freezes the suite, any change to a prompt, fixture, rubric, supplied context, or protected promise invalidates that scenario’s comparison baseline.
Before using the changed scenario, rerun five Sol-high and five Sol-low control arms and update every owning and shared record.
A new target also requires its watched control RED before the GREEN arm.

No skill prose may change before Tasks 1–11 establish and score the control suite, except a user-approved RED/GREEN slice required to resolve a genuine baseline inconsistency.
Portable behavior and readability edits land separately.
Every skill draft and final in-place edit passes the plan’s user approval gates, and any post-approval edit restarts the draft, validation, in-place review, and approval sequence.

## Cleanup Gate 5 override

Materialize this cleanup-only config in scratch outside the repository as `$CLEANUP_GATE5_ROOT/dd-config.json`:

```json
{
  "review": {
    "prompt_path": "skills/adversarial-review/SKILL.md",
    "reviewer": "codex",
    "model": "gpt-5.6-sol",
    "effort": "high"
  }
}
```

Materialize the following cleanup-only executable as `$CLEANUP_GATE5_ROOT/codex-read-only-no-agents`, then run `chmod 500 "$CLEANUP_GATE5_ROOT/codex-read-only-no-agents"`:

```sh
#!/bin/sh
if [ "$1" != "exec" ]; then
  echo "expected codex exec invocation" >&2
  exit 64
fi
shift
exec codex --ask-for-approval never exec \
  --strict-config \
  --ignore-user-config \
  --ignore-rules \
  --ephemeral \
  -c 'agents.enabled=false' \
  "$@"
```

`external_review.py` appends the configured model, effort, repository root, read-only sandbox, output path, and prompt after the wrapper’s enforced prefix.
Task 1 probed this exact wrapper before use: a repository write attempt was denied, the probe file remained absent, and no nested-agent tool was exposed.

Run the boundary review from the repository root with:

```bash
DD_CONFIG="$CLEANUP_GATE5_ROOT/dd-config.json" \
DD_LOG_DIR="$CLEANUP_GATE5_ROOT/logs" \
DD_ACTIVE_PLAN="plans/2026-08-01-comprehensive-skill-cleanup.md" \
DD_CODEX_BIN="$CLEANUP_GATE5_ROOT/codex-read-only-no-agents" \
python3 skills/disciplined-development/hooks/external_review.py \
  --cwd "$(git rev-parse --show-toplevel)"
```

Then verify the newest scratch `reviews.jsonl` row before the boundary passes:

```bash
python3 - "$CLEANUP_GATE5_ROOT/logs/reviews.jsonl" "$(git rev-parse HEAD)" <<'PY'
import json
import sys

rows = [json.loads(line) for line in open(sys.argv[1], encoding="utf-8") if line.strip()]
row = rows[-1]
expected = {
    "source": "external-gate",
    "decision": "PASS",
    "head_sha": sys.argv[2],
    "reviewer": "codex",
    "model": "gpt-5.6-sol",
    "effort": "high",
}
for key, value in expected.items():
    assert row.get(key) == value, (key, row.get(key), value)
print("Cleanup Gate 5 requested-model metadata OK.")
PY
```

The log records the configured/requested model and effort; this check is not independent attestation of the provider-served model.
A mismatch or non-PASS decision fails the boundary.

## Verification commands

Run this exact read-only local Markdown-link command before every commit after Task 1.
It preflights changed and untracked working-tree Markdown against the filesystem, then
checks every staged Markdown source against the resulting index snapshot. A staged
local target must already exist in that snapshot as a tracked file or directory; an
unstaged or untracked target cannot satisfy the commit check.

```bash
python3 - <<'PY'
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

def names(argv):
    return [Path(os.fsdecode(item)) for item in subprocess.check_output(argv).split(b"\0") if item]

working_docs = set(names(["git", "diff", "--name-only", "-z", "--diff-filter=ACMR", "HEAD", "--", "*.md"]))
working_docs.update(names(["git", "ls-files", "-z", "--others", "--exclude-standard", "--", "*.md"]))
staged_docs = set(names(["git", "diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR", "--", "*.md"]))
index_paths = {path.as_posix() for path in names(["git", "ls-tree", "-r", "--name-only", "-z", "HEAD"])}
index_paths.difference_update(path.as_posix() for path in names(["git", "diff", "--cached", "--no-renames", "--name-only", "-z", "--diff-filter=D"]))
index_paths.update(path.as_posix() for path in names(["git", "diff", "--cached", "--no-renames", "--name-only", "-z", "--diff-filter=ACMR"]))
patterns = (
    re.compile(r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))"),
    re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]+)>|([^\s]+))", re.M),
)
missing = []

def check(source, text, exists, label):
    for pattern in patterns:
        for match in pattern.finditer(text):
            target = next(value for value in match.groups() if value is not None)
            if target.startswith(("#", "//")) or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            resolved = Path(target) if Path(target).is_absolute() else Path(os.path.normpath(source.parent / target))
            if not exists(resolved):
                missing.append(f"{label} {source}: {target} -> {resolved}")

def in_index(path):
    value = path.as_posix().rstrip("/")
    return value in index_paths or any(item.startswith(value + "/") for item in index_paths)

for source in sorted(working_docs):
    check(source, source.read_text(encoding="utf-8"), lambda path: path.exists(), "working")

for source in sorted(staged_docs):
    text = subprocess.check_output(["git", "show", f":{source.as_posix()}"]).decode("utf-8")
    check(source, text, in_index, "staged")

if missing:
    raise SystemExit("\n".join(missing))
print(f"Local Markdown links OK: {len(working_docs)} working, {len(staged_docs)} staged document(s).")
PY
```

Use `<destination with spaces>` Markdown syntax for destinations containing whitespace or parentheses.
Before every commit also run `git diff --check` and `git diff --cached --check`.
Before every skill commit run the hook, installer, and research pytest suites listed in `CLAUDE.md`.

## Cross-skill score summaries

Task 11 will add the frozen Sol-low control table here.
Tasks 26–27 will add final Sol-high composition results, cleaned Sol-low comparisons, approved dispositions for decreases, and final word-count deltas.
