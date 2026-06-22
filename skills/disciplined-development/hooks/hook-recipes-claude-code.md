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
(exit 2) with a message to run a deep review. Never increments —
that is `edit_counter.py`'s job (PostToolUse).

**Stored-count semantics.** See the Boundary note in [`README.md`](README.md) for the PreToolUse/PostToolUse off-by-one. Clear a blocked counter by running a deep review per the adversarial-review skill and logging it via `dd-log`; for the remediation cycle itself, set `DD_SKIP_EDIT_BLOCK=1` in the launching shell.

---

## `PreToolUse` — matcher `Bash` — `commit_block.py`

**Class:** hard block (T2 ceiling). **Bypass:** `DD_SKIP_COMMIT_BLOCK=1`.

Fires only when the Bash command is `git commit` (including `--amend`, via
`command_match.is_git_commit`). If commits-since-last-deep-review ≥
`review_tiers.cold_read_escalation.hard_block_threshold` (default **5**), deny
the commit (exit 2) with a message to run a deep review.

Commit count selection: checkpoint exists → `state.commits_since_checkpoint`;
no checkpoint (fresh branch or none recorded) → `state.commits_since_fork_base`.
No fork base → degrade silent (allow). A stored count of 5 means 5 commits have
landed since the last cold-read; this hook denies the 6th.

**Note on `--amend`.** Amend is gated the same as a new commit — the gate is a
coarse "you owe a deep review" signal, not amend-specific logic. Clear it by
running a deep review per the adversarial-review skill and logging it via `dd-log`,
or set `DD_SKIP_COMMIT_BLOCK=1` for the remediation cycle.

---

## `PreToolUse` — matcher `Bash` — `pre_pr_review.py`

**Class:** hard gate (T3, the only PR gate). **Bypass:** `DD_SKIP_PR_REVIEW=1`.

Detect `gh pr create` (via `command_match.find_gh_pr_create`) and extract the
chained-`cd` target cwd, then delegate to `external_review.py --cwd <cwd>`.
No base resolution, no `DD_HARD_BLOCK`, no severity scanning — verdict is
entirely the external gate's responsibility. Any non-zero exit from the
delegate maps to exit 2 (Claude Code blocks PreToolUse only on exit 2);
delegate stdout+stderr are re-emitted so findings reach the model. An
unexpandable chained `cd` (`cd $X && gh pr create`) fails **loud** (block)
rather than letting an unreviewed PR through.

---

## `PostToolUse` — matcher `Edit|Write` — `edit_counter.py`

**Class:** counter + T0 nudge. **Bypass:** `DD_SKIP_EDIT_COUNTER=1`.

Increments `edits.count` on every Edit or Write (PostToolUse — no-op counting,
no diff inspection). When the resulting stored count reaches
`review_tiers.fast.nudge_threshold` (default **30**), emits a T0 nudge via
the PostToolUse `additionalContext` envelope and continues nudging on each
subsequent edit until the model runs a deep review and resets the counter via
`dd-log`. Advisory only — PostToolUse runs after the edit; this hook never blocks.

---

## `PostToolUse` — matcher `Bash` — `review_nudge.py`

**Class:** nudge. **Bypass:** `DD_SKIP_REVIEW_NUDGE=1`.

On a *landed* commit (`is_git_commit` + `commit_landed`), emits up to three
segments via the PostToolUse `additionalContext` envelope:

1. **Gate-3 verification (every landed commit):** verify the change against the
   running system, or state why it's not exercisable. No evidence scanning —
   the model judges.
2. **T1 nudge:** fires when `edits.count` ≥ `review_tiers.regular.commit_edit_floor`
   (default **30**). Suggests running a deep review per the adversarial-review
   skill and logging it via `dd-log` to reset the counter.
3. **T2 nudge:** fires when commits-since-last-deep-review ≥
   `review_tiers.cold_read_escalation.nudge_threshold` (default **3**).
   Checkpoint-or-fork-base selection mirrors `commit_block.py`. Suggests
   running a deep review per the adversarial-review skill and logging it via
   `dd-log` to reset the checkpoint.

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

## Model-callable tools (non-hook)

### `log_review.py` (review log writer)

Records a completed adversarial-review round: appends a `reviews.jsonl` row,
and — on a PASS result — resets `edits.count` **and** stamps
`review.checkpoint` = HEAD (both on clean, neither on BLOCK/ERROR). Reads
aggregated findings on **stdin**. Called by the `dd-log` slash command after
each clean review round.

```
python3 log_review.py \
  --source model-review|external-gate \
  --trigger <str> \
  [--round <n>] \
  [--reviewer <id>] \
  [--cwd <path>]
```

The reset-fold is decision-driven (derived from the findings on stdin), not
tier-driven. There is no `--tier` flag and no fast/regular/deep distinction
here.

### `external_review.py` (pre-PR codex gate)

Runs a whole-repo codex review anchored to the active plan. Invoked by
`pre_pr_review.py`; also runnable standalone for development/smoke testing.

```
python3 external_review.py [--cwd <path>]
```

Verdict-driven and fail-closed: reads the declared `DD-VERDICT: PASS|BLOCK`
line from codex output; exits 0 only on PASS. Every other outcome — BLOCK,
missing verdict, empty output, timeout, codex binary missing, non-zero/abnormal
codex exit — exits non-zero. No severity scanning; no `DD_HARD_BLOCK`. Reviews
the **whole repo** against the active plan (not a fork-base diff).

**Standalone note:** this tool exits 0/1 (not 2). Claude Code blocks a
PreToolUse hook only on exit 2; `pre_pr_review.py` translates any non-zero
result to exit 2. Do not wire this script directly as a PreToolUse delegate.

---

## Configuration

Schema: [`dd-config.md`](dd-config.md). Single override surface
`.claude/dd-config.json` over `lib/dd-defaults.json`. Per-hook bypass env vars
(`DD_SKIP_<HOOK>=1`, in `settings.local.json`) and the override knobs
(`DD_ACTIVE_PLAN`, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`) — full tables in
[`dd-config.md`](dd-config.md#env-vars).

---

## Testing

pytest, run from `hooks/`:

```bash
cd skills/disciplined-development/hooks
python3 -m pytest -q
```

Tests are per hook + per support module; each sets up its own sandbox tempdir
or git repo. `external_review`/`pre_pr_review` are exercised against a stubbed
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
- `log_review.py` — model-callable review log writer (resets counter/checkpoint, appends reviews.jsonl)
- `external_review.py` — model-callable pre-PR codex reviewer (invoked by pre_pr_review.py)
- `lib/config.py` — defaults + override loader (`get(dot_path)`)
- `lib/state.py` — per-branch edit counter + review checkpoint + fork-base
- `lib/cleanup.py` — age + orphaned-branch housekeeping sweep
- `lib/logging_setup.py` — rolling JSONL logging + `append_review` (reviews.jsonl)
- `lib/severity.py` — `parse_findings` (finding lines) + `parse_verdict` (declared verdict)
- `lib/command_match.py` — git-commit / gh-pr-create command matchers
- `lib/plan.py` — active-plan resolution
- `lib/reviewer_runner.py` — external-reviewer subprocess runner; `lib/envelope.py`
  — the exit-0 hook envelope
- `tests/` — pytest suite for all of the above
