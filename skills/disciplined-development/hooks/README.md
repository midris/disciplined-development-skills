# disciplined-development hook stack — design

The durable "why" for the hook layer that scaffolds the
`disciplined-development` skill.

## What this is

A minimal set of Claude Code hooks + a model-callable review engine that keep
the model on-track without continuous human steering. The hooks are
**model-facing**: the consumer of every signal is Claude, not the user. The
user is the architect; the discipline layer keeps the model honest during long
autonomous stretches.

Design ethos — **dumb triggers, smart model.** A hook fires on a concrete
boundary (a tool call, a commit, a PR open, a session resume) and emits a
fixed, actionable nudge. It does **not** inspect the model's work to decide
*what* to say — that "scan output to classify a smart agent's work" pattern
has unbounded edge cases and trains tune-out (see the spec's "nudge, never
police"). The intelligence stays in the model; the hook just marks the moment.

## Hook table

Eight hook scripts (one event entry each) plus one model-callable engine.
**Three hard blocks, zero kicks** — everything except the edit-count ceiling,
the commit ceiling, and the pre-PR gate is an advisory nudge.

| Hook | Event | Matcher | Behavior | Bypass |
|---|---|---|---|---|
| `inject_plan_state.py` | UserPromptSubmit | — | Surface the active plan + checkbox progress + next pending task; reset the per-turn discipline counter; run throttled housekeeping. | `DD_SKIP_INJECT_PLAN_STATE` |
| `discipline_nudge.py` | PreToolUse | `*` (all) | Count tool-calls since the last re-ground; at the threshold emit a "re-read CLAUDE.md + the plan, re-check the skills" nudge and reset. | `DD_SKIP_DISCIPLINE_NUDGE` |
| `edit_block.py` | PreToolUse | `Edit\|Write` | **Hard block.** Deny when stored `edits.count` ≥ 60 (i.e. the 61st edit). Reads only; never increments. | `DD_SKIP_EDIT_BLOCK` |
| `commit_block.py` | PreToolUse | `Bash` (`is_git_commit`) | **Hard block.** Deny a `git commit` (incl. `--amend`) when commits-since-last-cold-read ≥ 5 — allows 5, denies the 6th. | `DD_SKIP_COMMIT_BLOCK` |
| `pre_pr_review.py` | PreToolUse | `Bash` (`gh pr create`) | **Hard block.** Detect → extract base/cwd → delegate to `dd_review_runner.py pre-pr` with `DD_HARD_BLOCK=1`. Blocks the PR on findings. | `DD_SKIP_PR_REVIEW` |
| `edit_counter.py` | PostToolUse | `Edit\|Write` | Increment `edits.count`; emit a T0 nudge on each edit once the stored count reaches 30, continuing until a clean review resets the counter. Advisory only — PostToolUse runs after the edit. | `DD_SKIP_EDIT_COUNTER` |
| `review_nudge.py` | PostToolUse | `Bash` | On a landed commit: always emit a Gate-3 **verify** reminder; also T1 nudge when `edits.count` ≥ 30; also T2 nudge when commits-since-cold-read ≥ 3. | `DD_SKIP_REVIEW_NUDGE` |
| `session_reground.py` | SessionStart | — | On every session (re)start, emit a source-specific preamble + shared re-ground instructions. Fires on all sources (startup/resume/clear/compact); unknown source fires with a generic preamble. | `DD_SKIP_SESSION_REGROUND` |

Gate 3 (verify before "done") rides the **post-commit verify nudge**, not a
Stop kick: the commit is where an edit becomes an assertion that owes
verification, and PostToolUse reaches the model without a Stop hook's
block-or-be-silent constraint.

**Boundary note (PreToolUse reads / PostToolUse writes).** `edit_counter.py`
increments `edits.count` after each edit (PostToolUse). `edit_block.py` reads
the stored value before the next edit (PreToolUse). A stored count of 60 means
60 edits have already landed — the block fires on the next (61st) edit attempt.
Thresholds are stated against the **stored** count to avoid this off-by-one.

## Four-tier review

Reviews run at four tiers — T0 through T3. The model invokes all tiers through
the single **`/dd-review <tier>`** command.

| Tier | Fires on | Reviewer | Diff scope | Hard block |
|---|---|---|---|---|
| **T0 fast** | edit counter ≥ 30 (nudge) or ≥ 60 (block) | 1 holistic subagent | working-tree vs HEAD | at 60 edits (`edit_block.py`) |
| **T1 regular** | landed commit when `edits.count` ≥ 30 (nudge) | holistic + correctness + rationale subagents | fork-base..HEAD | — nudge only |
| **T2 cold-read** | 3 commits since checkpoint (nudge) or 5 (block) | holistic + correctness + rationale + cross-file + security + necessity *(doc-dominant cold-read swaps two — see the `/dd-review` command)* | fork-base..HEAD | at 5 commits (`commit_block.py`) |
| **T3 pre-pr** | `gh pr create` | `codex review` (subprocess) | fork-base..HEAD | always (`pre_pr_review.py`) |

**T0–T2 reviewer:** the `/dd-review` command dispatches fresh adversarial-review
subagents in parallel (Task tool — runs in-session on the subscription). A
**holistic** subagent covers the whole scope; higher tiers add focused **angle**
subagents (correctness, rationale, cross-file, security, necessity — the same
`adversarial-review` posture + one appended focus line). The angle set is not
config-driven; a doc-dominant cold-read substitutes two angles by model judgment
(see the `/dd-review` command). Angles are monotonic — each tier is a superset
of the one below.

**T3 reviewer:** `dd_review_runner.py` runs `codex review` as a subprocess
(codex is OpenAI tooling — unaffected by Anthropic billing). Severity-scanned
and hard-blocks `gh pr create` on any P0/P1/P2.

**`dd_review_runner.py` CLI modes:**

| Mode | When to use |
|---|---|
| `dd_review_runner.py pre-pr [--base <ref>] [--cwd <path>]` | T3 codex review (invoked by `pre_pr_review.py`) |
| `dd_review_runner.py --write-checkpoint <tier>` | Write post-clean-review state after a T0/T1/T2 clean pass (`fast`/`regular`/`cold-read`) |
| `dd_review_runner.py --resolve-scope <tier>` | Resolve the git diff argument for a tier (`HEAD` for fast; `<fork-base>..HEAD` for the others) |
| `dd_review_runner.py --log-review --tier <t> --source <s> [--round <n>] [--reviewer <id>] [--cwd <path>]` | Append one model-layer review row to `reviews.jsonl` from findings on stdin (derives severity/decision/git fields). Logged per round by the `/dd-review` command (`--source command`). |

## State model

Two per-branch state files under `<repo>/.claude/.dd-state/<branch-slug>/`
(gitignored). Writes are atomic (temp file + `os.replace`); last-write-wins.
The layer is advisory — a read or write failure degrades to a safe default.

- **`edits.count`** — unreviewed edits on this branch since the last clean
  review of any tier. Incremented by `edit_counter.py` on every Edit/Write
  (PostToolUse). Read by `edit_block.py` (PreToolUse) and `review_nudge.py`.
  Reset on any clean review — T0/T1/T2 resets are command-driven (the `/dd-review`
  command runs `--write-checkpoint <tier>`; advisory, not mechanically enforced);
  T3 (pre-pr) resets deterministically inside `dd_review_runner.py` on a clean
  codex pass.

- **`review.checkpoint`** — SHA of HEAD at the last clean cold-read (T2) or
  pre-PR (T3). `commit_block.py` and the T2 segment of `review_nudge.py`
  count commits since this SHA. When absent (fresh branch or no cold-read yet),
  both fall back to counting from the **fork base** at the same thresholds —
  so the T2 block fires even on a branch that has never been cold-read.

**Reset rule:**
- A clean **T0** or **T1** review resets `edits.count` only
  (`--write-checkpoint fast` or `--write-checkpoint regular`).
- A clean **T2** review sets `review.checkpoint` = HEAD **and** resets
  `edits.count` (`--write-checkpoint cold-read`).
- A clean **T3** review sets `review.checkpoint` = HEAD **and** resets
  `edits.count` (done inside `dd_review_runner.py` on a clean codex pass).

See the Boundary note under the hook table for the PreToolUse/PostToolUse off-by-one.

## Observability

Every hook emits structured traces — comprehensive, on by default, tuned by
retention/cleanup.

- **Rolling log:** `.claude/.dd-state/.logs/dd-hooks-YYYYMMDD.jsonl` (append;
  all hooks interleave, keyed by `hook`/`pid`). Dir resolution: `DD_LOG_DIR`
  env → `logging.dir` config → consumer `<project-root>/.claude/.dd-state/.logs`
  (project root from `CLAUDE_PROJECT_DIR` or cwd) → `__file__` walk-up to
  `.claude` → `/tmp/dd-hooks`.
- **Curated review trace:** `.claude/.dd-state/.logs/reviews.jsonl` — one record
  per review round, **multi-source**: `source: engine` rows from the T3 codex
  path (add model, effort, strategy, diff_bytes, duration_s) and `source: command`
  rows the `/dd-review` tiers log via `--log-review` (add round). Both share tier,
  reviewer, decision, P0–P3 counts, branch/head_sha/base, ts, and full reviewer
  output. Never aged out.
- **Cleanup:** a throttled sweep (from `inject_plan_state`) prunes day-logs
  past `logging.retention_days` and removes orphaned per-branch state dirs.

## Configuration

- **Shipped defaults:** `lib/dd-defaults.json` (read-only; the schema).
- **Single override surface:** `.claude/dd-config.json` — all behavior
  tunables (thresholds, review_tiers, strategy_selector, logging,
  trunk_branches, codex timeout). Edit a value to override; delete a key to
  fall back to the default.
- **Escape hatches:** `DD_SKIP_<HOOK>=1` env vars (in
  `.claude/settings.local.json`) silence a hook. Env, not config — a human
  escape the model can't set by editing a tracked file. Override knobs
  (`DD_ACTIVE_PLAN`, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`, `DD_REVIEW_PROMPT_PATH`)
  live there too. Full reference: `dd-config.md`.

## Companion skills

- **`disciplined-development`** — the doctrine: the Iron Law, five gates,
  principles, rationalization tables. Principle 8 is the source of the review
  cadence.
- **`adversarial-review`** / **`adversarial-review-loop`** — reviewer posture +
  the severity contract (P0/P1/P2 block, P3 advisory) and the
  review-fix-review iteration cap + cold-read escape. Loaded by every T0–T2
  subagent.
- **`dispatching-development-subagents`** — scope-contract + verify-every-commit
  overlay for development subagents whose diffs the orchestrator integrates.
- **`lean-plan-writing`**, **`writing-explicit-rationale`**,
  **`sweeping-stale-references`**, **`disciplined-research`**,
  **`concise-writing`** — the plan-density, rationale-on-page, stale-reference,
  verify-before-claiming, and prose-tightening companions.

## Two classes of discipline (why the hooks are dumb)

Every rule enforces one of two things, and the split bounds what a hook can do:

- **Class A — boundary-observable** (a commit, a PR open, a tool call, a turn
  end). A hook can see the moment and fire. This is what the hooks cover.
- **Class B — in-the-head** (did you re-read the schema, write the test first,
  sweep references, put rationale on-page). No event fires; a hook that tries
  to *detect* these is a dumb process classifying smart work — rejected. The
  re-ground nudges re-seed the whole class at once; **adversarial review is
  the net** that catches Class-B failures once they land in an artifact.

## Extending the system

Before adding a hook: (1) name the signal the model loses without it; (2) pick
the tier — nudge (default) vs a hard block (only for an irreversible boundary);
(3) keep the trigger dumb (no output-classification); (4) every hook gets a
`DD_SKIP_<HOOK>` bypass; (5) test-first; (6) update this README + the spec.
If the surface is for the human, not the model — don't build it.
