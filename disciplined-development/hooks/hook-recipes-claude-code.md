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
  design of the one hard gate.
- **No config-driven disable.** There is no enable/disable map in the config;
  the pre-PR hard gate must not be model-disableable.

Live source: the Python files in this directory (what `settings.json` invokes).
Each script's header docstring shows its event + channel. Run the pytest suite
(see Testing) after changes.

The wired set (`settings.json`) — **one hard block, zero kicks:**

| Event | Matcher | Hook |
|---|---|---|
| UserPromptSubmit | — | `inject_plan_state.py` |
| PreToolUse | `*` (all) | `discipline_nudge.py` |
| PreToolUse | `Bash` | `pre_pr_review.py` |
| PostToolUse | `Bash` | `review_nudge.py` |
| SessionStart | — | `compaction_reground.py` |
| PreCompact | — | `compaction_reground.py` |

---

## `UserPromptSubmit` — `inject_plan_state.py`

**Class:** nudge. **Bypass:** `DD_SKIP_INJECT_PLAN_STATE=1`.

At the start of each turn: resolve the active plan (`$DD_ACTIVE_PLAN` →
`.claude/active-plan` → newest `plans.fallback_glob` by mtime) and emit on
plain stdout the plan path + source, top-level checkbox progress (skipping
`plans.skip_section_headers` sections and fenced code blocks), and the next
pending task. Then reset the per-turn discipline counter and run the
throttled cleanup sweep. Resolves only inside a git repo (no cross-tree
surfacing).

---

## `PreToolUse` — matcher `*` — `discipline_nudge.py`

**Class:** nudge. **Bypass:** `DD_SKIP_DISCIPLINE_NUDGE=1`.

Bump a per-branch tool-call counter on every PreToolUse. At
`counters.discipline_threshold` emit a fixed re-ground nudge (re-read
CLAUDE.md + the active plan, re-check the governing skills) via the
PreToolUse `additionalContext` envelope, and reset. Otherwise silent. The
text never varies by tool — varying it would rebuild the rejected
output-scanner.

---

## `PreToolUse` — matcher `Bash` — `pre_pr_review.py`

**Class:** hard gate (the only one). **Bypass:** `DD_SKIP_PR_REVIEW=1`.

Detect `gh pr create` (via `command_match.find_gh_pr_create`), extract the
review base (`--base`/`-B` → `branch.<cur>.gh-merge-base` git config) and a
chained-`cd` target cwd, then delegate to `dd_review.py pre-pr` with
`DD_HARD_BLOCK=1`, forwarding `--base`/`--cwd` only when parsed. Detect +
extract + delegate — no review/severity logic here; `dd_review` blocks the PR
(exit non-zero) on `[P0]`/`[P1]`/`[P2]` findings. An unexpandable chained `cd`
(`cd $X && gh pr create`) fails **loud** (block) rather than letting an
unreviewed PR through.

---

## `PostToolUse` — matcher `Bash` — `review_nudge.py`

**Class:** nudge. **Bypass:** `DD_SKIP_REVIEW_NUDGE=1`.

On a *landed* commit (`is_git_commit` + `commit_landed`), emit up to two
segments via the PostToolUse `additionalContext` envelope:
1. **Gate-3 verification (every landed commit):** verify against the running
   system, or state why it's not exercisable. No evidence scanning — the model
   judges.
2. **Review cadence (threshold):** commits since the last review checkpoint
   (or fork-base when none) ≥ `counters.review_threshold` → "run
   `/dd-review regular`".

---

## `SessionStart` + `PreCompact` — `compaction_reground.py`

**Class:** nudge. **Bypass:** `DD_SKIP_COMPACTION_REGROUND=1`.

After context loss, re-ground (re-read CLAUDE.md + the plan; re-invoke the
governing skills). SessionStart fires the model-visible `additionalContext`
envelope on `source` ∈ {resume, compact} (silent on startup/clear). PreCompact
emits the reminder on plain stdout (its non-blocking output isn't
model-visible — the post-compaction reground is delivered by the
SessionStart(compact) path).

---

## `dd_review.py` (model-callable engine)

Not a hook — the review engine the cadence nudge + pre-PR gate point at.
`dd_review.py {regular|cold-read|pre-pr} [--base <ref>] [--cwd <path>]`. Each
tier resolves the diff to the fork-base (pre-pr honours `--base`), dispatches
the configured reviewer (`review_tiers.<tier>`), scans severities, writes a
review checkpoint on a clean pass, and appends a rich record to
`reviews.jsonl`. `pre-pr` returns non-zero only under `DD_HARD_BLOCK=1`
(set by `pre_pr_review.py`); manual runs are advisory.

---

## Configuration

Schema: [`dd-config.md`](dd-config.md). Single override surface
`.claude/dd-config.json` over `lib/dd-defaults.json`. Bypass env vars:

| Env var | Hook silenced |
|---|---|
| `DD_SKIP_INJECT_PLAN_STATE` | `inject_plan_state.py` |
| `DD_SKIP_DISCIPLINE_NUDGE` | `discipline_nudge.py` |
| `DD_SKIP_REVIEW_NUDGE` | `review_nudge.py` |
| `DD_SKIP_COMPACTION_REGROUND` | `compaction_reground.py` |
| `DD_SKIP_PR_REVIEW` | `pre_pr_review.py` (the hard gate) |

Override knobs (also env, in `settings.local.json`): `DD_ACTIVE_PLAN`,
`DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`, `DD_REVIEW_PROMPT_PATH`.

---

## Testing

pytest, run from `hooks/`:

```bash
cd .claude/skills/disciplined-development/hooks
python3 -m pytest -q
```

Tests are per hook + per support module; each sets up its own sandbox tempdir
or git repo. `dd_review`/`pre_pr_review` are exercised against stubbed
`claude`/`codex` shims so the suite runs offline. `DD_LOG_DIR` is pointed at
`/tmp` for the suite so logs never touch the real `.claude/.dd-state/`.

---

## Reference implementation files (`hooks/`)

- `inject_plan_state.py` — UserPromptSubmit (plan-state + counter reset + cleanup)
- `discipline_nudge.py` — PreToolUse `*` (re-ground counter)
- `review_nudge.py` — PostToolUse `Bash` (verify + review cadence)
- `compaction_reground.py` — SessionStart + PreCompact (re-ground)
- `pre_pr_review.py` — PreToolUse `Bash` (the pre-PR hard gate)
- `dd_review.py` — model-callable review engine (regular / cold-read / pre-pr)
- `lib/config.py` — defaults + override loader (`get(dot_path)`)
- `lib/state.py` — per-branch discipline counter + review checkpoint + fork-base
- `lib/cleanup.py` — age + orphaned-branch housekeeping sweep
- `lib/logging_setup.py` — rolling JSONL logging + `append_review` (reviews.jsonl)
- `lib/severity.py` — `[P0]`–`[P3]` line-anchored severity scan
- `lib/command_match.py` — git-commit / gh-pr-create command matchers
- `lib/plan.py` — active-plan resolution
- `lib/review_prompt.py`, `lib/review_invocation.py`, `lib/claude_runner.py`,
  `lib/envelope.py` — reviewer prompt/strategy/dispatch + the exit-0 envelope
- `tests/` — pytest suite for all of the above
