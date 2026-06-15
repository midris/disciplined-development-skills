# Hook Recipes (Claude Code)

Reference for pairing the `disciplined-development` skill with Claude Code
hooks. The skill carries the discipline content; the hooks are dumb triggers
that surface it at concrete boundaries.
Overview: [`README.md`](README.md). Config schema: [`dd-config.md`](dd-config.md).

## Architecture overview

- **Skill enforces; hooks trigger.** `SKILL.md` gates/principles define what
  must happen; the hooks fire fixed, actionable nudges at the moments those
  gates apply. Hooks never inspect the model's work to decide *what* to say.
- **Config tunes.** `.claude/dd-config.json` (single project-override surface)
  over `lib/dd-defaults.json` (shipped defaults). Arrays replace,
  objects deep-merge.
- **Env vars bypass.** A `DD_SKIP_<HOOK>=1` env var (set in the launching shell
  or `.claude/settings.local.json`'s `env` block) silences a hook for the
  session. The model can't set these per-command — the hook reads its own
  inherited environment, not the tool's. That asymmetry is the load-bearing
  design of the hard gates.
- **No config-driven disable.** There is no enable/disable map in the config;
  the hard gates must not be model-disableable.

Live source: the Python files in this directory (what `settings.json` invokes).
Each script's header docstring shows its event + channel. Run the pytest suite
(see Testing) after changes.

The wired set (`settings.json`) — **three hard blocks, zero kicks:**

| Event | Matcher | Hook |
|---|---|---|
| UserPromptSubmit | — | `inject_plan_state.py` |
| PreToolUse | `*` (all) | `discipline_nudge.py` |
| PreToolUse | `Edit\|Write` | `edit_block.py` |
| PreToolUse | `Bash` | `pre_pr_review.py`, `commit_block.py` |
| PostToolUse | `Edit\|Write` | `edit_counter.py` |
| PostToolUse | `Bash` | `review_nudge.py` |
| SessionStart | — | `session_reground.py` |

---

## `UserPromptSubmit` — `inject_plan_state.py`

**Class:** nudge. **Bypass:** `DD_SKIP_INJECT_PLAN_STATE=1`.

At the start of each turn: resolve the active plan (`$DD_ACTIVE_PLAN` →
`.claude/active-plan` → newest `plans.fallback_glob` by mtime) and emit on
plain stdout the plan path + source, top-level checkbox progress (skipping
`plans.skip_section_headers` sections and fenced code blocks), and the next
pending task. Then reset the per-turn discipline counter and run the throttled
cleanup sweep. Resolves only inside a git repo (no cross-tree surfacing).

---

## `PreToolUse` — matcher `*` — `discipline_nudge.py`

**Class:** nudge. **Bypass:** `DD_SKIP_DISCIPLINE_NUDGE=1`.

Bump a per-branch tool-call counter (`discipline.count`) on every PreToolUse.
At `counters.discipline_threshold` emit a fixed re-ground nudge (re-read
CLAUDE.md + the active plan, re-check the governing skills) via the
PreToolUse `additionalContext` envelope, and reset. Otherwise silent. The text
never varies by tool — varying it would rebuild the rejected output-scanner.

---

## `PreToolUse` — matcher `Edit|Write` — `edit_block.py`

**Class:** hard block (T0 ceiling). **Bypass:** `DD_SKIP_EDIT_BLOCK=1`.

Reads the stored `edits.count` before each Edit or Write. If the count is ≥
`review_tiers.fast.hard_block_threshold` (default **60**), deny the tool call
(exit 2) with a message pointing at `/dd-review fast`. Never increments —
that is `edit_counter.py`'s job (PostToolUse).

**Stored-count semantics.** See the Boundary note in [`README.md`](README.md) for the PreToolUse/PostToolUse off-by-one. Clear a blocked counter by running `/dd-review fast` to a clean pass; for the remediation cycle itself, set `DD_SKIP_EDIT_BLOCK=1` in the launching shell.

---

## `PreToolUse` — matcher `Bash` — `commit_block.py`

**Class:** hard block (T2 ceiling). **Bypass:** `DD_SKIP_COMMIT_BLOCK=1`.

Fires only when the Bash command is `git commit` (including `--amend`, via
`command_match.is_git_commit`). If commits-since-last-cold-read ≥
`review_tiers.cold_read_escalation.hard_block_threshold` (default **5**), deny
the commit (exit 2) and point at `/dd-review cold-read`.

Commit count selection: checkpoint exists → `state.commits_since_checkpoint`;
no checkpoint (fresh branch or none recorded) → `state.commits_since_fork_base`.
No fork base → degrade silent (allow). A stored count of 5 means 5 commits have
landed since the last cold-read; this hook denies the 6th.

**Note on `--amend`.** Amend is gated the same as a new commit — the gate is a
coarse "you owe a cold-read" signal, not amend-specific logic. Clear it by
running `/dd-review cold-read`, or set `DD_SKIP_COMMIT_BLOCK=1` for the
remediation cycle.

---

## `PreToolUse` — matcher `Bash` — `pre_pr_review.py`

**Class:** hard gate (T3, the only PR gate). **Bypass:** `DD_SKIP_PR_REVIEW=1`.

Detect `gh pr create` (via `command_match.find_gh_pr_create`), extract the
review base (`--base`/`-B` → `branch.<cur>.gh-merge-base` git config) and a
chained-`cd` target cwd, then delegate to `dd_review_runner.py pre-pr` with
`DD_HARD_BLOCK=1`, forwarding `--base`/`--cwd` only when parsed. Detect +
extract + delegate — no review/severity logic here; `dd_review_runner` blocks the
PR (exit 2, propagated) on `[P0]`/`[P1]`/`[P2]` findings. An unexpandable
chained `cd` (`cd $X && gh pr create`) fails **loud** (block) rather than
letting an unreviewed PR through.

---

## `PostToolUse` — matcher `Edit|Write` — `edit_counter.py`

**Class:** counter + T0 nudge. **Bypass:** `DD_SKIP_EDIT_COUNTER=1`.

Increments `edits.count` on every Edit or Write (PostToolUse — no-op counting,
no diff inspection). When the resulting stored count reaches
`review_tiers.fast.nudge_threshold` (default **30**), emits a T0 nudge via
the PostToolUse `additionalContext` envelope ("run `/dd-review fast`") and
continues nudging on each subsequent edit until the model runs the review and
resets the counter. Advisory only — PostToolUse runs after the edit; this
hook never blocks.

---

## `PostToolUse` — matcher `Bash` — `review_nudge.py`

**Class:** nudge. **Bypass:** `DD_SKIP_REVIEW_NUDGE=1`.

On a *landed* commit (`is_git_commit` + `commit_landed`), emits up to three
segments via the PostToolUse `additionalContext` envelope:

1. **Gate-3 verification (every landed commit):** verify the change against the
   running system, or state why it's not exercisable. No evidence scanning —
   the model judges.
2. **T1 nudge:** fires when `edits.count` ≥ `review_tiers.regular.commit_edit_floor`
   (default **30**). Suggests `/dd-review regular`.
3. **T2 nudge:** fires when commits-since-last-cold-read ≥
   `review_tiers.cold_read_escalation.nudge_threshold` (default **3**).
   Checkpoint-or-fork-base selection mirrors `commit_block.py`. Suggests
   `/dd-review cold-read`.

The verification segment fires independent of repo/branch resolution; T1 and T2
require it. A detached HEAD or git error degrades the cadence segments silently
while keeping the verify reminder.

Both review nudges (T1/T2) carry an audience caveat (`GATE_AUDIENCE`): the review
gate is the orchestrator's, so a dispatched subagent reports it and stops rather
than acting on the nudge. The hook stays dumb — one static string for whoever is
listening; it does not detect subagent context. The verify segment carries no
such caveat (verifying its own work is the subagent's job).

---

## `SessionStart` — `session_reground.py`

**Class:** nudge. **Bypass:** `DD_SKIP_SESSION_REGROUND=1`.

On every session (re)start, re-ground (re-read CLAUDE.md + the plan; re-invoke
the governing skills). SessionStart fires the model-visible `additionalContext`
envelope on ALL sources: `startup`, `resume`, `clear`, and `compact`. Each
emits a source-specific preamble followed by a shared common body. An unknown
or missing source falls back to a generic preamble and still fires.

The `compact` source fires *after* compaction, so this is the post-compaction
reground. PreCompact is deliberately not wired — its non-blocking output can't
reach the post-compaction model, so it could never deliver the reground.

---

## `dd_review_runner.py` (model-callable engine)

Not a hook — the review engine the `/dd-review` command and the pre-PR gate
point at.

**Pre-PR gate (T3):**
```
python3 dd_review_runner.py pre-pr [--base <ref>] [--cwd <path>]
```
Runs `codex review` against the fork-base diff (pre-pr honours `--base`),
severity-scans, writes the checkpoint + resets `edits.count` on a clean pass,
and appends a rich record to `reviews.jsonl`. Returns non-zero under
`DD_HARD_BLOCK=1` (set by `pre_pr_review.py`); manual runs are advisory.

**Post-clean-review state write (T0/T1/T2):**
```
python3 dd_review_runner.py --write-checkpoint fast|regular|cold-read [--cwd <path>]
```
Writes state after a `/dd-review` clean pass — no codex dispatch.
- `fast` / `regular` → reset `edits.count` only.
- `cold-read` → set `review.checkpoint` = HEAD **and** reset `edits.count`.

**Scope resolution (all tiers):**
```
python3 dd_review_runner.py --resolve-scope fast|regular|cold-read|pre-pr [--cwd <path>]
```
Prints the git diff argument for the tier: `HEAD` for `fast`; `<fork-base>..HEAD`
for the others. No state writes, no dispatch.

---

## Configuration

Schema: [`dd-config.md`](dd-config.md). Single override surface
`.claude/dd-config.json` over `lib/dd-defaults.json`. Per-hook bypass env vars
(`DD_SKIP_<HOOK>=1`, in `settings.local.json`) and the override knobs
(`DD_ACTIVE_PLAN`, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`, `DD_REVIEW_PROMPT_PATH`) —
full tables in [`dd-config.md`](dd-config.md#env-vars).

---

## Testing

pytest, run from `hooks/`:

```bash
cd skills/disciplined-development/hooks
python3 -m pytest -q
```

Tests are per hook + per support module; each sets up its own sandbox tempdir
or git repo. `dd_review_runner`/`pre_pr_review` are exercised against a stubbed
`codex` shim so the suite runs offline. `DD_LOG_DIR` is pointed at `/tmp` for
the suite so logs never touch the real `.claude/.dd-state/`.

---

## Reference implementation files (`hooks/`)

- `inject_plan_state.py` — UserPromptSubmit (plan-state + counter reset + cleanup)
- `discipline_nudge.py` — PreToolUse `*` (re-ground counter)
- `edit_counter.py` — PostToolUse `Edit|Write` (T0 edit counter + nudge)
- `edit_block.py` — PreToolUse `Edit|Write` (T0 hard block at 60)
- `commit_block.py` — PreToolUse `Bash` (T2 hard block at 5 commits)
- `review_nudge.py` — PostToolUse `Bash` (Gate-3 verify + T1/T2 cadence nudge)
- `session_reground.py` — SessionStart (re-ground; all sources, source-specific preamble + common body)
- `pre_pr_review.py` — PreToolUse `Bash` (T3 pre-PR hard gate)
- `dd_review_runner.py` — model-callable engine (pre-pr codex / --write-checkpoint / --resolve-scope)
- `lib/config.py` — defaults + override loader (`get(dot_path)`)
- `lib/state.py` — per-branch edit counter + review checkpoint + fork-base
- `lib/cleanup.py` — age + orphaned-branch housekeeping sweep
- `lib/logging_setup.py` — rolling JSONL logging + `append_review` (reviews.jsonl)
- `lib/severity.py` — `[P0]`–`[P3]` line-anchored severity scan
- `lib/command_match.py` — git-commit / gh-pr-create command matchers
- `lib/plan.py` — active-plan resolution
- `lib/review_prompt.py`, `lib/review_invocation.py`, `lib/reviewer_runner.py`,
  `lib/envelope.py` — reviewer prompt/strategy/dispatch + the exit-0 envelope
- `tests/` — pytest suite for all of the above
