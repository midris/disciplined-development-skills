# Skill validation protocol

This file is the single source of truth for skill-validation rules, shared infrastructure, audit status, and cross-skill score summaries.
Individual records own their active scenario catalogs, result summaries, and preserved historical evidence.

## Roles and model policy

- The orchestrator owns validation-bearing tasks, dispatch, result inspection, manual scoring, scorer and reviewer dispatch, user approval gates, commits, and Gate 5.
- Evaluators, scorers, and reviewers are fresh, bounded, read-only processes with nested-agent tools disabled.
- Skill authoring, validation design, behavioral evaluation, scoring, and cold review use `gpt-5.6-sol` at high reasoning effort.
- This cold Sol-high configuration is the non-Claude portability gate for every skill within its intended domain and with declared dependencies available.
- Sol low is limited to Tasks 11 and 27 and post-freeze control backfills.
- Sol low measures effort robustness; it is not another portability domain or model-family requirement.
- Every behavioral scenario uses five fresh evaluator processes, with at most three running concurrently.
- `research/replay_codex.py` reviews historical diffs and writes research results; it is not a skill-scenario runner.

The scope categories are:

- broad-domain companions: `concise-writing`, `disciplined-research`, and `writing-explicit-rationale`;
- development companions: `lean-plan-writing` and `sweeping-stale-references`;
- integrated development group: `disciplined-development`, `adversarial-review`, `adversarial-review-loop`, and `dispatching-development-subagents`.

Domain breadth, standalone packaging, and cross-model portability are separate axes.
Portability does not broaden a skill's authored task domain or remove a declared
dependency.

## Audit index

`Keep`, `Repair`, `Merge`, `Retire`, and `Add` are scenario counts, not file counts.
An em dash means the owning audit task has not classified the scenarios yet.

| Record | Kind | Owner | Affected skills | Audit task | Status | Keep | Repair | Merge | Retire | Add |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|
| [adversarial-review](adversarial-review.md) | Skill | `adversarial-review` | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references`, `disciplined-development` | 7 | Audit complete; 13 current Sol-high scenarios at 5/5; 4 watched target REDs GREEN; angle ablation 0/5 | 0 | 7 | 2 | 1 | 7 |
| [adversarial-review-loop](adversarial-review-loop.md) | Skill | `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development`; shared routing boundaries | 8 | Audit complete; 15 owned Sol-high controls at 5/5; complete active closure 135/135 | 0 | 14 | 3 | 3 | 1 |
| [concise-writing](concise-writing.md) | Skill | `concise-writing` | `concise-writing`, `adversarial-review-loop`; external `superpowers:writing-skills` dependency and distractor | 2, 17 | Audited; 665-word candidate `f763b43e…`; repaired-definition `CW-19` controls high 4/5 and low 2/5, candidate 5/5; complete affected candidate arm 145/145 GREEN; blind comparison found zero candidate material losses in 45 pairs; editorial review and final owner approval complete | 0 | 2 | 4 | 2 | 11 |
| [disciplined-development](disciplined-development.md) | Skill | `disciplined-development` | all nine skills through orchestration | 10, 17 | Audit complete; repaired-definition `DD-01`/`DD-02` controls are 0/5 at high and low effort; both unchanged Task 17 candidate arms passed 5/5; inherited `DSD-02` current rerun 5/5 | 0 | 2 | 0 | 1 | 1 |
| [disciplined-research](disciplined-research.md) | Skill | `disciplined-research` | `disciplined-research` | 3 | Audited; Sol-high baseline 3/3 scenarios at 5/5; `DR-02` broad-domain coverage confirmed | 0 | 1 | 0 | 1 | 2 |
| [dispatching-development-subagents](dispatching-development-subagents.md) | Skill | `dispatching-development-subagents` | `dispatching-development-subagents`, `disciplined-development`; shared routing boundaries | 9 | Audit complete; `DSD-02` current rerun 5/5; current closure 70/70 | 0 | 2 | 1 | 0 | 2 |
| [lean-plan-writing](lean-plan-writing.md) | Skill | `lean-plan-writing` | `lean-plan-writing`; external `superpowers:writing-plans` composition | 4 | Audited; 7 active owned scenarios; `LP-04` retained as historical exploratory evidence | 0 | 4 | 1 | 1 | 3 |
| [sweeping-stale-references](sweeping-stale-references.md) | Skill | `sweeping-stale-references` | `sweeping-stale-references` | 5 | Audited; 4 active owned scenarios; `SSR-04` retained as historical exploratory evidence | 0 | 2 | 0 | 1 | 2 |
| [writing-explicit-rationale](writing-explicit-rationale.md) | Skill | `writing-explicit-rationale` | `writing-explicit-rationale`, `lean-plan-writing`, `disciplined-development`; shared parent/plan composition | 6 | Audit complete; `WER-03` broad-domain coverage confirmed; current policy scope approved; final Task 10 target 5/5 | 0 | 1 | 4 | 2 | 6 |
| [adversarial-review-loop scenarios](adversarial-review-loop-scenarios.md) | Supporting | `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development`; shared routing boundaries | 8 | Audited; exact definitions for 15 loop-owned controls and links to 12 shared controls | 0 | 14 | 3 | 3 | 1 |
| [duplicate red-flags scenarios](duplicate-red-flags-scenarios.md) | Supporting history | Task 1 protocol | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references` | 1 | Audited | 0 | 0 | 0 | 4 | 0 |
| [evaluation subagents read-only](evaluation-subagents-read-only.md) | Project-rule history | Task 1 protocol | Repository evaluation rule | 1 | Audited | 0 | 0 | 0 | 1 | 0 |
| [skill discovery](skill-discovery.md) | Shared active suite | Task 1 protocol | all nine skills | 1, 17 | Audited; repaired-definition `DISC-01` original-description controls are high/low 0/5 and the candidate is 5/5; Task 17 candidate descriptions total 50/50 | 0 | 0 | 0 | 0 | 10 |

## Framework inventory

“Full” recoverability means the exact evaluator-facing prompt and an explicitly evaluator-withheld rubric are present.
“Partial” means a scenario can be reconstructed conceptually but not replayed byte-for-byte under this protocol.

| File | Purpose and owner | Affected skills | Existing IDs and repetitions | Prompt/rubric recoverability | Active disposition |
|---|---|---|---|---|---|
| `README.md` | Universal protocol and audit index; Task 1 protocol | All | Not a scenario record | Not applicable | Active source of truth |
| `adversarial-review-loop-scenarios.md` | Canonical loop decision definitions; `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development` | `CS`, `T2`–`T7`, `NF`, `PW`, `XL`, `G3A`–`G3C`, `OWN`, `CE`; five reps each | Full; exact prompts, withheld rubrics, contexts, ownership, and rerun triggers | Active definition source; complete owned control suite 75/75 |
| `adversarial-review-loop.md` | Active loop results and preserved derivation history; `adversarial-review-loop` | `adversarial-review-loop`, `disciplined-development`; shared routing boundaries | Fifteen owned IDs plus linked `DISC-01`–`DISC-10`, `CW-09`, and `CW-11`; five Sol-high repetitions each | Full for active catalog; mixed-protocol derivation retained as history | Audit complete; complete active closure 135/135 |
| `adversarial-review.md` | Active review, output, enumeration, angle, durability, whole-project, generated-case, invariant-severity, pattern, necessity, and effectiveness suite plus preserved derivation history; `adversarial-review` | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references`, `disciplined-development` | `AR-01`–`AR-10` and `AR-12`–`AR-14`, five control/current reps each; historical evidence below | Full for active catalog; historical evidence remains partial | Active suite 65/65; nine preservation controls 45/45; four watched REDs GREEN; `AR-14` holistic-only ablation 0/5 |
| `concise-writing.md` | Active verbosity, over-trim, routing, ownership, composition-pressure, response/file boundary, direct-invocation, broad-domain, and complex technical application suite; `concise-writing` | `concise-writing`, `adversarial-review-loop`; external `superpowers:writing-skills` dependency and distractor | `CW-01`–`CW-14` and `CW-17`–`CW-19`; repaired/new high/low controls complete; current candidate owned arm 85/85 | Full definitions, freeze hashes, per-repetition outcomes, repaired-definition control/candidate provenance, section necessity, blind comparison, rejected simplification arms, and superseded-arm isolation | Task 17 complete; affected candidate arm 145/145 GREEN; blind comparison 0 candidate losses/45 pairs |
| `disciplined-development.md` | Active mode routing, Gates 1–5 orchestration, Principle 7 threshold, and compact derivation history; `disciplined-development` | All through orchestration | `DD-01`–`DD-03` plus linked `DISC-01`–`DISC-10`, `DSD-01`, `DSD-02`, `OWN`, and `WER-07`; five reps each | Full for the active catalog; historical evidence remains partial | Audit complete; Task 17 repaired-definition controls high/low 0/5 and candidate `DD-01`/`DD-02` 10/10 |
| `disciplined-research.md` | Active project, procurement, and broad-domain grounding suite plus B1/B17 history; `disciplined-research` | `disciplined-research` | `DR-01`–`DR-03`, 5 reps each; historical `B1`, `B17` retained below | Full for active catalog; historical evidence remains partial | Active Sol-high baseline 15/15; `DR-02` is isolated broad-domain coverage |
| `dispatching-development-subagents.md` | Active dispatch-prompt, identity/nudge, returned-commit verification, and finding-partition suite plus preserved history; `dispatching-development-subagents` | `dispatching-development-subagents`, `disciplined-development`; shared routing boundaries | `DSD-01`–`DSD-04` and linked `DISC-01`–`DISC-10`; five Sol-high repetitions each | Full for active catalog; mixed-protocol derivation retained as history | Audit complete; `DSD-02` current rerun 5/5; current closure 70/70 |
| `duplicate-red-flags-scenarios.md` | Four-skill composite consolidation fixture; Task 1 protocol | `adversarial-review`, `concise-writing`, `lean-plan-writing`, `sweeping-stale-references` | Cells `A`–`D`; 5 per arm | Full | Retired from the active suite because it combines unrelated contracts; all retained coverage is now atomized in the owning skill catalogs |
| `evaluation-subagents-read-only.md` | Historical evidence for choosing a no-write evaluator type; Task 1 protocol | Repository evaluation rule | No stable ID; RED/GREEN counts unstated | Partial | Retired from the active suite; the enforced transport probe below replaces instruction-only evidence |
| `lean-plan-writing.md` | Active direct, prose-density, necessary-snippet, edge-inventory, and merge-boundary suite plus consolidation and exploratory cross-domain history; `lean-plan-writing` | `lean-plan-writing`; external `superpowers:writing-plans` composition | Active `LP-01`–`LP-03`, `LP-05`–`LP-08`; historical `LP-04`; five original/current repetitions preserved | Full for active catalog and retained `LP-04` definition | Seven active owned scenarios; `LP-02` and `LP-03` current GREEN; `LP-04` retired |
| `skill-discovery.md` | Atomic all-nine description routing; Task 1 protocol | All nine | `DISC-01`–`DISC-10`; five control, parent-target, Task 2A, Task 6, and Task 17 candidate-description reps complete | Full | Active; repaired-definition `DISC-01` controls high/low 0/5, candidate-description arm 50/50 |
| `sweeping-stale-references.md` | Active simple, reviewer-pressure, grouped-scale, and negative-form suite plus exploratory policy, rename, grouping, and packaging history; `sweeping-stale-references` | `sweeping-stale-references` | Active `SSR-01`–`SSR-03`, `SSR-05`; historical `SSR-04`; all recorded repetitions preserved | Full for active catalog and retained `SSR-04` definition | Four active owned scenarios; `SSR-04` retired |
| `writing-explicit-rationale.md` | Active direct, repeated-review, broad-domain, authoritative-reference, relevance-filtering, and parent/plan composition suite plus preserved history; `writing-explicit-rationale` | `writing-explicit-rationale`, `lean-plan-writing`, `disciplined-development`; shared parent/plan composition | `WER-01`–`WER-03`, `WER-05`–`WER-07`, and linked `DISC-08`–`DISC-10`; original controls classified and final Task 10 target 5/5 | Full for active catalog; historical evidence remains partial | Audit, target GREEN, and final user review complete; current policy scope approved |

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
After any approved behavior GREEN, materialize the committed skill and its declared
dependencies the same way; that bundle becomes the immediate readability control
while `4296647` remains the original-behavior control.

## Scenario taxonomy and active catalogs

Scenario type and behavior status are separate axes.

- **Discovery:** route from descriptions only.
- **Simple application:** exercise the core workflow with one uncomplicated request.
- **Non-trivial application:** exercise competing constraints, pressure, or edge conditions.
- **Direct invocation:** invoke the skill safely with the environment declared for its category.
- **Broad-domain isolated application:** run a broad-domain companion on a non-software task with only its declared dependencies.
- **Dependency-scoped development application:** run a development companion in its authored software domain with declared dependencies.
- **Focused regression:** protect a demonstrated branch, boundary, output contract, or failure mode.
- **Composition:** test cross-skill ownership or orchestration; use a composite prompt only when composition is the behavior under test.
- **Preservation:** established behavior whose `4296647` control must pass 5/5.
- **Target:** approved new behavior with a watched control RED and a 5/5 GREEN before it joins active regression coverage.

Use atomic prompts for individual promises.
A rubric evaluates the requested artifact as a whole, not isolated sentences.
Context elsewhere in the artifact satisfies a criterion when a careful reader can
take the same action in every relevant case without guessing. Require wording or
placement to survive locally only when the artifact's function depends on that
literal, placement, or explicit relationship.
A skill’s complete active suite is its owned scenarios plus every shared discovery,
direct-invocation, domain-appropriate application, dependency, and composition
scenario that lists it as affected.
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
Behavioral and readability edits land separately.
Every skill draft and final in-place edit passes the plan’s user approval gates, and any post-approval edit restarts the draft, validation, in-place review, and approval sequence.

## Cleanup Gate 5 override

The Gate 5 reviewer must use a different provider and model family from the
orchestrator. Use the Codex transport below when Claude orchestrates this
cleanup. When Codex orchestrates, run the same whole-repository, plan-anchored
review through a fresh Claude session instead and record its exact model,
effort, read-only invocation, and verdict in the Gate 2 artifact.
Gate 5 is a separate repository review boundary; it is not a second behavioral
portability provider requirement.

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

`external_review.py` appends `exec --cd <resolved-repo>`, the independently
configured model and effort, `-s read-only`, last-message output path, and the
whole-repository plan-anchored prompt after the wrapper's enforced prefix. The
plan must be explicitly pinned and readable; there is no newest-plan fallback.
The launch environment removes `GH_REPO`, `GIT_DIR`, `GIT_WORK_TREE`, and
`GIT_COMMON_DIR` so they cannot redirect the target.
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

Before accepting this boundary, also run the complete hook regression suite:

```bash
cd skills/disciplined-development/hooks
python3 -m pytest -q
```

The command-matcher and consumer cases in that suite cover standalone actions
in the payload cwd; prefix, suffix, and `cd` compounds; `&` and `|&` status
isolation; unrelated compounds; position-aware and present-empty target
selectors; unresolved post-commit verification-only
behavior; explicit `dd-log` verdicts; and
pre-launch `plan_unavailable` failure.

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

### Task 11 Sol-low control freeze and results

The frozen catalog is commit `db985d203fdbe812dc5161f63565e6e2021f0872`.
Its tracked `skill-validation/` archive SHA-256 is `7e626ccc1dd2c596e54688dfaa32a6c090e4f4c50c1ea293352669051f0b4f8b`, and its canonical 125-file manifest SHA-256 is `bbb4fdaa873aa009715bf815d18ab148eac831c92aa00fa647dfa2ca5390751d`.
The original-control archive SHA-256 is `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`; its canonical content-manifest SHA-256 is `e2249c4b24132523f1374d506957197a303314e2bfbc6e32c9c1b233909cbbff`.
`4296647f0dff48a9e77b979ef07e813bf1f66db2` remains the regression source anchor.
`WER-07` is the catalog-declared frozen mixed-control exception required for direct comparability: parent `21a46fb9…`, lean plan writing `4c659b76…`, writing explicit rationale `ec77350b…`, and Superpowers 6.2.0 writing-plans `72190c88…`; it is not a pure-`4296647` bundle.

On 2026-08-07, all 81 frozen scenarios produced five fresh `gpt-5.6-sol` low-effort responses: 405 completed responses, maximum concurrency three, zero infrastructure errors, and zero retries.
Codex CLI 0.147.0's strict/ignored-config-and-rules, ephemeral, `agents.enabled=false`, read-only transport probe passed before execution.
A separate `gpt-5.6-sol` high-effort scorer processed 81 isolated packets containing 405 response slots and no evaluator prompts, bundles, or arm mappings; it had zero infrastructure errors.
The orchestrator then manually read every raw output and exact withheld rubric and adjudicated all 81 rows; those manual verdicts are authoritative, including documented scorer false-positive and false-negative overrides.
This 81-row/405-slot aggregate is frozen historical fact and is not recomputed after
the scope repair.
Its `concise-writing` subtotal includes the now-superseded ambiguous `CW-08` arm;
that result remains historical and is not evidence for the active repaired fixture.

| Owning family | Preservation scenarios | Preservation Sol-low | Target scenarios | Target Sol-low | Combined |
|---|---:|---:|---:|---:|---:|
| Shared discovery | 6 | 30/30 | 4 | 3/20 | 33/50 |
| `concise-writing` | 8 | 37/40 | 6 | 0/30 | 37/70 |
| `disciplined-research` | 3 | 14/15 | 0 | — | 14/15 |
| `lean-plan-writing` | 5 | 11/25 | 3 | 9/15 | 20/40 |
| `sweeping-stale-references` | 5 | 11/25 | 0 | — | 11/25 |
| `writing-explicit-rationale` | 4 | 19/20 | 2 | 2/10 | 21/30 |
| `adversarial-review` | 9 | 41/45 | 4 | 1/20 | 42/65 |
| `adversarial-review-loop` | 15 | 56/75 | 0 | — | 56/75 |
| `dispatching-development-subagents` | 4 | 18/20 | 0 | — | 18/20 |
| `disciplined-development` | 1 | 0/5 | 2 | 0/10 | 0/15 |
| **Total** | **60** | **237/300** | **21** | **15/105** | **252/405** |

These observed REDs are control evidence, not fixes or authorization to alter scenario contracts or skill prose.
Any post-freeze prompt, fixture, rubric, supplied-context, or protected-promise change requires the global Sol-high and Sol-low control backfill before the scenario is used again.
Future active closure contains 82 scenarios: 60 preservation and 22 target rows, or
410 five-repetition slots. This current closure excludes historical `LP-04` and
`SSR-04` and adds Task 17's `CW-17` and `CW-19` targets plus the `CW-18`
preservation guard. `CW-19` remains a target scenario; its sentence-local 2/5 and
1/5 adjudications, actor-repetition arm, and threshold-ambiguous arm are historical
after the owner-approved whole-artifact rubric repair.
Tasks 26–27 will add final cold Sol-high domain-appropriate and composition results,
cleaned Sol-low comparisons, approved dispositions for decreases, and final
word-count deltas.

### Task 17 concise-writing current controls and candidate affected rerun

The immutable immediate readability control is the 866-word Task 2A skill at
SHA-256 `6c3a838297da8b0a17a3f3978dd6e46c7e5794f9e7e34c4e6db760e941c942aa`
under `/private/tmp/dd-task17-readability-control`. The separate pre-rewrite routing
control for `CW-17`/`CW-18` was 849 words at SHA-256
`d3a1b7ba3b384b803c22bb96c2ac03790a573c339071a031c924163459dc6504`.
The current evaluated candidate is 665 words at SHA-256
`f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba`.

Repaired `CW-08` passed current high/low controls 5/5. `CW-17` established the
required watched current RED at high 0/5 and low 0/5; `CW-18` passed both current
arms 5/5. `CW-19`'s original high 2/5 and low 1/5 sentence-local adjudications are
historical under the repaired rubric. The fresh whole-artifact arm at
`/private/tmp/dd-task17-cw19-whole-artifact-current` used the unchanged `f763b43e…`
skill, prompt `e05ab6e…`, rubric `8c7ae23f…`, and bundle `ff01764c…`; five fresh
Sol-high outputs and five fresh rubric scorers completed on attempt 1 with zero
infrastructure errors, and every score passed.

The repaired definitions now also have their protocol-required fresh high- and
low-effort controls. These target REDs are separate from, and pair with, the
candidate GREENs:

| Active repaired definition | Frozen control bytes | Sol-high control | Sol-low control | Sol-high candidate |
|---|---|---:|---:|---:|
| `CW-19` whole-artifact rubric | Skill `21e558b3…`; prompt `e05ab6e…`; rubric `8c7ae23f…`; bundle `30b02b66…` | **4/5 RED** | **2/5 RED** | **5/5 GREEN** |
| `DISC-01` supplied-source routing | Original descriptions embedded in prompt `803da9b9…`; active rubric `1fc2931e…` | **0/5 RED** | **0/5 RED** | **5/5 GREEN** |
| `DD-01` active routing matrix | Original complete control bundle `ffeeb68d…`; active prompt/rubric | **0/5 RED** | **0/5 RED** | **5/5 GREEN** |
| `DD-02` active gate ledger | Original complete control bundle `ffeeb68d…`; active prompt/rubric | **0/5 RED** | **0/5 RED** | **5/5 GREEN** |

All four backfills used five fresh `gpt-5.6-sol` processes per effort, maximum
concurrency three, read-only sandboxing, disabled agents, attempt 1, and zero
infrastructure errors. This closes the prior protocol evidence gap: every Task 17
prompt or rubric repair now has five fresh high and five fresh low controls. The
older control results remain historical under their own definitions. Full hashes,
repetition outcomes, and exact misses are in
[concise-writing](concise-writing.md#cw-19-active-whole-artifact-control-provenance-2026-08-08),
[skill discovery](skill-discovery.md#task-17-repaired-definition-control-backfill-2026-08-08),
and [disciplined development](disciplined-development.md#task-17-repaired-definition-control-backfill-2026-08-08).

Only the `CW-19` candidate arm restarted because only its rubric changed. The
fresh repaired-definition controls above backfill the separate control baseline;
they do not invalidate candidate bytes. The unchanged fresh candidate arms
for the other 28 scenarios remain valid, making the 665-word candidate affected
set GREEN:

| Owner / surface | IDs | Result |
|---|---|---:|
| `concise-writing` | `CW-01`–`CW-14`, `CW-17`–`CW-19` | **85/85 GREEN** |
| Shared discovery | `DISC-01`–`DISC-10` | **50/50 PASS** |
| `disciplined-development` | `DD-01`, `DD-02` | **10/10 PASS** |
| **Task 17 affected candidate total** | **29 scenarios** | **145/145 GREEN** |

All candidate arms used the same fresh high-effort model policy, concurrency cap,
read-only/no-agents transport, first attempts, zero infrastructure errors, and
manual orchestrator scoring. The full root, prompt/rubric, bundle, per-repetition,
design-ladder, and superseded-arm provenance is owned by
[concise-writing](concise-writing.md#task-17-current-candidate-sol-high-provenance-2026-08-08),
[skill discovery](skill-discovery.md#task-17-concise-writing-candidate-description-rerun-2026-08-08),
and [disciplined development](disciplined-development.md#task-17-concise-writing-candidate-integration-rerun-2026-08-08).

The first integrated `DISC-01` arm scored 4/5 under a stale rubric that prohibited
otherwise defensible supplied-source research; it is superseded. The prompt stayed
unchanged, the pre-approved repaired rubric made `disciplined-research` optional,
and a fresh arm passed 5/5. The owner then repaired `CW-19`'s rubric to evaluate
the complete artifact instead of requiring `or higher` in the failure sentence
when the runbook already makes readiness strictly below 0.1%. Cold semantic
classification makes the `f763b43e…` truth-ablation arm 5/5, the
rationalizations-deletion arm 4/5 because R5 leaves `BLOCKED` at equality
ambiguous, and the qualifier-rule arm 5/5 but behaviorally ineffective. Their
earlier 2/5, 1/5, and 0/5 scores remain historical superseded adjudications. The
rationalizations section remains restored, the unnecessary qualifier rule remains
reverted, and the active candidate is GREEN. Subjective comparison, editorial
review, final owner approval, and repository verification are complete. Task 17
closes in `docs(skills): clean up concise writing`; no PR was opened.

Three later post-GREEN simplification explorations did not replace that candidate.
The fresh 578-word no-rationalizations arm scored 4/5 under the repaired rubric;
R1's generic `either metric breaches its limit` left the required `BLOCKED`
action at mismatch equality ambiguous, so the section remains restored. An
approved 664-word one-line Method tightening passed `CW-02`, `CW-05`, and `CW-08`
5/5 but scored 1/5 on `CW-19`, with escalation, first-accepted-write, and
old-schema-rationale losses; it was reverted before a full rerun. A never-applied
637-word self-rewrite draft passed `CW-02`, `CW-05`, `CW-08`, `CW-17`, and
`CW-18` 5/5 but scored 4/5 on `CW-19` for the same generic equality ambiguity;
it was rejected. Full roots, hashes, bundles, results, and dispositions remain in
the owning concise-writing record. The tracked skill remains the exact 665-word
`f763b43e…` candidate and the active baseline remains 145/145 GREEN.

The required blind readability comparison then evaluated five randomized pairs
for each of `CW-01`–`CW-08` and `CW-19`: 45 pairs judged by nine fresh Sol-high
calls under read-only/no-agents transport with maximum concurrency three. The
candidate had zero material losses. `CW-01`, `CW-02`, `CW-03`, `CW-04`, `CW-06`,
and `CW-07` were equivalent in all five pairs. The control had one material loss
in `CW-05`, three in `CW-08`, and four in `CW-19`; the remaining pairs were
equivalent. The candidate was never worse, so the blind comparison gate is
complete. Full manifest and verdict hashes are in the owning record.
