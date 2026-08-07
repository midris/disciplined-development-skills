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
| PreToolUse | `*` (all) | `discipline_nudge.py` |
| PreToolUse | `Edit\|Write` | `edit_block.py` |
| PreToolUse | `Bash` | `pre_pr_review.py`, `commit_block.py` |
| PostToolUse | `Edit\|Write` | `edit_counter.py` |
| PostToolUse | `Bash` | `review_nudge.py` |
| SessionStart | — | `session_reground.py` |

---

## `PreToolUse` — matcher `*` — `discipline_nudge.py`

**Class:** nudge. **Bypass:** `DD_SKIP_DISCIPLINE_NUDGE=1`.

Bump a per-branch tool-call counter (`discipline.count`) on every PreToolUse.
At `counters.discipline_threshold` emit a fixed re-ground nudge (re-read
CLAUDE.md + the active plan, re-check the governing skills) via the
PreToolUse `additionalContext` envelope, naming the resolved active-plan path;
then run the throttled cleanup sweep and reset. Otherwise silent. The text
never varies by tool — varying it would rebuild the rejected output-scanner.

---

## `PreToolUse` — matcher `Edit|Write` — `edit_block.py`

**Class:** hard block (T0 ceiling). **Bypass:** `DD_SKIP_EDIT_BLOCK=1`.

Reads the stored `edits.count` before each Edit or Write. If the count is ≥
`review_tiers.fast.hard_block_threshold` (default **60**), deny the tool call
(exit 2) with a message to run a deep review. Never increments —
that is `edit_counter.py`'s job (PostToolUse).

**Stored-count semantics.** See the Boundary note in [`README.md`](README.md)
for the PreToolUse/PostToolUse off-by-one. Run the deep-review loop and log every
round with `dd-log`; only a PASS resets the counter. For the remediation cycle,
set `DD_SKIP_EDIT_BLOCK=1` in the launching shell.

---

## `PreToolUse` — matcher `Bash` — `commit_block.py`

**Class:** hard block (T2 ceiling). **Bypass:** `DD_SKIP_COMMIT_BLOCK=1`.

Fires only when a direct Bash command segment is `git commit` (including
`--amend`, via `command_match.is_git_commit`). It does not recurse into shell
wrappers such as `bash -c 'git commit ...'`; wrapped commits bypass this block
and the post-commit nudge. The commit must be a standalone direct call in the
payload cwd, normalized to the Git top-level. A compound containing a commit,
an existing non-repository cwd, or a Git target selector blocks with guidance to
run the commit standalone from the target repository and other commands
separately. This includes `&&`, `;`, `||`, `|`, `&`, and `|&` around the
commit; unrelated compounds remain outside the gate. Repository selectors are
position-aware, so global `git -C` is unresolved while commit-local
`git commit -C HEAD` remains supported. If commits since the review checkpoint—or fork base
when no valid checkpoint exists—reach
`review_tiers.cold_read_escalation.hard_block_threshold` (default **5**), deny
the commit (exit 2) with a message to run a deep review.

Commit count selection uses shared `state.review_distance`: a valid checkpoint
wins, otherwise the fork base is used. No fork base → degrade silent (allow).
A stored count of 5 means 5 commits have
landed since `review.checkpoint`; this hook denies the 6th.

**Note on `--amend`.** Amend is gated the same as a new commit — the gate is a
coarse "you owe a deep review" signal, not amend-specific logic. Run the
deep-review loop and log every round with `dd-log`; only a PASS resets the
checkpoint. For the remediation cycle, set `DD_SKIP_COMMIT_BLOCK=1`.

---

## `PreToolUse` — matcher `Bash` — `pre_pr_review.py`

**Class:** hard gate (T3, the only PR gate). **Bypass:** `DD_SKIP_PR_REVIEW=1`.

Detect a standalone direct `gh pr create` in the payload cwd, normalize it to
the Git top-level, then delegate to `external_review.py --cwd <git-root>`.
Compounds containing the action, existing non-repository cwd values,
`gh --repo`/`-R`, `GH_REPO`, and `&&`, `;`, `||`, `|`, `&`, or `|&` compounds
are unresolved and fail **loud** with standalone-call rewrite/bypass guidance.
Selector-looking title/body values are not options, inherited `GH_REPO` key
presence is unresolved even when empty, and unrelated compounds remain outside
the gate. No base resolution, no `DD_HARD_BLOCK`, and no wrapper-level severity
policy: the reviewer declares PASS or BLOCK and the external gate trusts it.
Any non-zero delegate exit maps to exit 2. Delegate stdout+stderr are re-emitted;
full reviewer output remains available only through the best-effort trace.

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

On a *landed*, directly invoked commit (`is_git_commit` + `commit_landed`),
emits up to three segments via the PostToolUse `additionalContext` envelope.
The shell-wrapper detection boundary described under `commit_block.py` applies
here too.

1. **Gate-3 verification (every landed commit):** verify the change against the
   running system, or state why it's not exercisable. No evidence scanning —
   the model judges.
2. **T1 nudge:** fires when `edits.count` ≥ `review_tiers.regular.commit_edit_floor`
   (default **30**). Suggests running the deep-review loop and recording every
   round via `dd-log`; an explicit final PASS resets the counter.
3. **T2 nudge:** fires when commits since the review checkpoint—or fork base
   when no valid checkpoint exists—reach
   `review_tiers.cold_read_escalation.nudge_threshold` (default **3**).
   Checkpoint-or-fork-base selection mirrors `commit_block.py`. Suggests
   running the deep-review loop and recording every round via `dd-log`; an
   explicit final PASS resets the checkpoint.

The verification segment fires independent of target/repo resolution; T1 and T2
require it. An unresolved commit target therefore produces verification only
and never reads cadence state from the launching repository.

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

Processes a completed adversarial-review round: attempts a `reviews.jsonl`
append and — on a PASS result — resets `edits.count` **and** stamps
`review.checkpoint` = HEAD regardless of trace persistence. PASS attempts those
two best-effort writes independently; BLOCK/ERROR attempts neither. If only one
PASS write succeeds, the remaining edit or commit state retains conservative
review pressure; no rollback is attempted. Reads
aggregated findings on **stdin**. Called by the `dd-log` slash command after
every review round; only a PASS resets cadence.

```
python3 log_review.py \
  --source model-review|external-gate \
  --trigger <str> \
  [--round <n>] \
  [--reviewer <id>] \
  [--cwd <path>]
```

Every input ends with `DD-VERDICT: PASS|BLOCK`. The reset-fold trusts that
explicit decision; findings are telemetry-only. There is no `--tier` flag.

### `external_review.py` (pre-PR codex gate)

Runs a whole-repo codex review anchored to the active plan. Invoked by
`pre_pr_review.py`; also runnable standalone for development/smoke testing.

```
python3 external_review.py [--cwd <path>]
```

Requires a readable plan pinned by `DD_ACTIVE_PLAN` or fixed
`.claude/active-plan` before launch. It trusts the final declared
`DD-VERDICT: PASS|BLOCK`: PASS allows and BLOCK blocks. A missing/unreadable
plan, missing verdict, empty output, timeout, missing codex binary, or
non-zero/abnormal exit fails closed. Reviews cover the **whole repo** against
the pinned plan, not a fork-base diff. The subprocess uses `codex exec --cd`,
the configured model/effort, read-only sandboxing, last-message capture, and a
sanitized environment without repository selectors. No `DD_HARD_BLOCK`.

**Standalone note:** this tool exits 0/1 (not 2). Claude Code blocks a
PreToolUse hook only on exit 2; `pre_pr_review.py` translates any non-zero
result to exit 2. Do not wire this script directly as a PreToolUse delegate.

---

## Configuration

Schema: [`dd-config.md`](dd-config.md). Single override surface
`.claude/dd-config.json` over `lib/dd-defaults.json`. Per-hook bypass env vars
(`DD_SKIP_<HOOK>=1`, in `settings.local.json`) and the override knobs
(`DD_ACTIVE_PLAN`, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`, `DD_CODEX_BIN`) — full
tables in [`dd-config.md`](dd-config.md#env-vars).

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

- `discipline_nudge.py` — PreToolUse `*` (re-ground counter + plan name + cleanup on fire)
- `edit_counter.py` — PostToolUse `Edit|Write` (T0 edit counter + nudge)
- `edit_block.py` — PreToolUse `Edit|Write` (T0 hard block at 60)
- `commit_block.py` — PreToolUse `Bash` (T2 hard block at 5 commits)
- `review_nudge.py` — PostToolUse `Bash` (Gate-3 verify + T1/T2 cadence nudge)
- `session_reground.py` — SessionStart (re-ground; all sources, source-specific preamble + common body)
- `pre_pr_review.py` — PreToolUse `Bash` (T3 pre-PR hard gate)
- `log_review.py` — model-callable review logger (resets counter/checkpoint on
  PASS, attempts a reviews.jsonl append)
- `external_review.py` — model-callable pre-PR codex reviewer (invoked by pre_pr_review.py)
- `lib/config.py` — defaults + override loader (`get(dot_path)`)
- `lib/state.py` — per-branch counters + review checkpoint + fork-base
- `lib/cleanup.py` — age + orphaned-branch housekeeping sweep
- `lib/logging_setup.py` — rolling JSONL logging + `append_review` (reviews.jsonl)
- `lib/severity.py` — `parse_findings` (finding lines) + `parse_verdict` (declared verdict)
- `lib/command_match.py` — git-commit / gh-pr-create command matchers
- `lib/plan.py` — explicit active-plan resolution
- `lib/envelope.py` — the exit-0 hook envelope
- `tests/` — pytest suite for all of the above
