# dd-config.md — Disciplined-Development Config Schema Reference

## Overview

Two layers of JSON config + env overrides:

- **Skill defaults:** `lib/dd-defaults.json` — ships with the skill, the
  schema; treat as read-only.
- **Project override (single surface):** `.claude/dd-config.json` — override
  only what you need; delete a key to fall back to the default. Resolved under
  `$CLAUDE_PROJECT_DIR` (the harness-set project root), falling back to the
  current directory when that var is unset; `DD_CONFIG` overrides the path
  outright.

### Precedence (lowest → highest)

1. `dd-defaults.json` (shipped defaults)
2. `.claude/dd-config.json` (project overrides)
3. `DD_*` override env vars (path/timeout knobs — see below)
4. `DD_SKIP_*` env vars (hook bypasses)

### Merge semantics

- **Arrays REPLACE** — to extend a default list, copy it in full and append.
- **Objects DEEP-MERGE** — `"counters": {"discipline_threshold": 30}` keeps
  other counters keys from defaults.

Regex patterns (where present) use Python `re` syntax. A malformed
`.claude/dd-config.json` (invalid JSON / non-object) is discarded silently and
defaults stand.

### No config-driven disable

`dd-config.json` has no hook enable/disable map. The only way to silence a hook
is its `DD_SKIP_*` env var — a human escape the model can't set by editing a
tracked file. The hard gates (`edit_block`, `commit_block`, `pre_pr_review`)
must not be model-disableable.

---

## `counters`

| Key | Type | Default | Description |
|---|---|---|---|
| `discipline_threshold` | int | `50` | Tool-calls since the last re-ground before `discipline_nudge` fires. |

Bool values are rejected (a config typo like `true` won't silently become 1).

---

## `review_tiers`

Four tiers, each covering one review level. **Only `pre_pr` carries reviewer
config** — `fast`, `regular`, and `cold_read_escalation` carry cadence
thresholds only; their subagent sets are fixed in the `/dd-review` command, not
config-driven.

### `review_tiers.fast` — T0 edit-counter cadence

| Key | Type | Default | Description |
|---|---|---|---|
| `nudge_threshold` | int | `30` | Stored `edits.count` at which `edit_counter.py` emits the T0 nudge (and keeps nudging). |
| `hard_block_threshold` | int | `60` | Stored `edits.count` at which `edit_block.py` denies the next edit. |

**Threshold invariant:** `hard_block_threshold` must exceed `nudge_threshold`
(60 > 30 by default). A mis-ordered override (block ≤ nudge) yields incoherent
cadence — documented expectation, not runtime-validated.

### `review_tiers.regular` — T1 commit-floor cadence

| Key | Type | Default | Description |
|---|---|---|---|
| `commit_edit_floor` | int | `30` | Stored `edits.count` floor for the T1 nudge in `review_nudge.py`. The T1 nudge fires only when a commit lands AND `edits.count` ≥ this value. |

### `review_tiers.cold_read_escalation` — T2 cold-read cadence

| Key | Type | Default | Description |
|---|---|---|---|
| `nudge_threshold` | int | `3` | Commits-since-cold-read at which `review_nudge.py` emits the T2 nudge. |
| `hard_block_threshold` | int | `5` | Commits-since-cold-read at which `commit_block.py` denies the next `git commit`. |

**Threshold invariant:** `hard_block_threshold` must exceed `nudge_threshold`
(5 > 3 by default). Same expectation as T0 — not runtime-validated.

Commits-since-cold-read uses `review.checkpoint` when present; falls back to
fork-base when absent (fresh branch) — so the T2 block fires even on a branch
that has never been cold-read.

### `review_tiers.pre_pr` — T3 pre-PR codex gate

| Key | Type | Default | Description |
|---|---|---|---|
| `reviewer` | string | `"codex"` | CLI reviewer for the T3 gate (only valid value in the current engine). |
| `model` | string | `"gpt-5.5"` | Model id passed to the reviewer. |
| `default_effort` | string | `"medium"` | Effort level; escalated to `"high"` by diff size via `strategy_selector`. |

Projects without codex on `$PATH` must override `reviewer` — there is no
runtime `$PATH` probe; the engine fails cleanly with "CLI not found" if `codex`
is absent.

---

## `strategy_selector`

Decides stuffed-vs-fetched dispatch + high-effort escalation by diff size
(used by `dd_review_runner.py` for T3).

| Key | Type | Default | Description |
|---|---|---|---|
| `pre_stuff_max_bytes` | int | `524288` | Diffs at/under this are stuffed in-prompt; larger are fetched by the reviewer. |
| `high_effort_min_bytes` | int | `51200` | Diffs at/over this escalate effort to `high`. |

---

## `logging`

Observability — comprehensive + on by default; tuned by retention/cleanup.

| Key | Type | Default | Description |
|---|---|---|---|
| `dir` | string\|null | `null` | Log directory. `null` → derived `.claude/.dd-state/.logs`. Env `DD_LOG_DIR` overrides. |
| `retention_days` | int | `14` | Rolling `dd-hooks-*.jsonl` day-files older than this are pruned. `reviews.jsonl` is exempt (never aged out). |
| `enabled` | bool | `true` | Master switch. `false` → no log writes (incl. `reviews.jsonl`). |
| `sweep_throttle_hours` | int | `24` | Minimum interval between cleanup sweeps. |

---

## `branch_convention`

| Key | Type | Default | Description |
|---|---|---|---|
| `trunk_branches` | list[string] | `["master", "main"]` | Fork-base resolution: the first that resolves is the merge-base ref for review diffs + commit counts. |

---

## `plans`

| Key | Type | Default | Description |
|---|---|---|---|
| `active_plan_pointer` | string | `".claude/active-plan"` | File holding the active plan path (one line). |
| `fallback_glob` | list[string] | `["plans/*.md"]` | mtime-fallback plan discovery (newest match wins). |
| `skip_section_headers` | list[string] | see defaults | Headers (case-insensitive) that suppress checkbox counting in `inject_plan_state` (test plan, definition of done, verification, …). |

---

## `review`

| Key | Type | Default | Description |
|---|---|---|---|
| `prompt_path` | string | `.claude/skills/adversarial-review/SKILL.md` | Prompt header for the stuffed-strategy codex review (relative → repo root). Env: `DD_REVIEW_PROMPT_PATH`. |

---

## `codex`

| Key | Type | Default | Description |
|---|---|---|---|
| `pr_review_timeout_s` | int | `600` | Wall-clock timeout for the codex reviewer in `external_review.py`. Env: `DD_REVIEW_TIMEOUT`. |

---

## Env vars

### Bypasses (`DD_SKIP_<HOOK>=1`)

Each bypass silences the named hook entirely for the session. Set in
`.claude/settings.local.json`'s `env` block (the model cannot set these at
tool-call time — hooks read their inherited environment).

| Env var | Hook silenced |
|---|---|
| `DD_SKIP_INJECT_PLAN_STATE` | `inject_plan_state.py` |
| `DD_SKIP_DISCIPLINE_NUDGE` | `discipline_nudge.py` |
| `DD_SKIP_EDIT_COUNTER` | `edit_counter.py` (T0 counter + nudge) |
| `DD_SKIP_EDIT_BLOCK` | `edit_block.py` (T0 hard block) |
| `DD_SKIP_COMMIT_BLOCK` | `commit_block.py` (T2 hard block) |
| `DD_SKIP_REVIEW_NUDGE` | `review_nudge.py` (Gate-3 verify + T1/T2 nudges) |
| `DD_SKIP_SESSION_REGROUND` | `session_reground.py` |
| `DD_SKIP_PR_REVIEW` | `pre_pr_review.py` (T3 hard gate) |

### Override knobs

| Env var | Effect |
|---|---|
| `DD_ACTIVE_PLAN` | Force the active plan path (highest-priority resolution). |
| `DD_LOG_DIR` | Override the log directory (highest-priority). |
| `DD_REVIEW_TIMEOUT` | Override `codex.pr_review_timeout_s`. |
| `DD_REVIEW_PROMPT_PATH` | Override `review.prompt_path`. |

**Set in:** the launching shell, `~/.claude/settings.json` `env`, or
`<project>/.claude/settings.local.json` `env`. (`DD_CONFIG` / `DD_DEFAULTS`
redirect the config files — for tests only; `CLAUDE_PROJECT_DIR` is harness-set
and locates `.claude/dd-config.json` (see Overview → Precedence); `DD_HARD_BLOCK`
is set internally by `pre_pr_review` and is not user-facing.)

---

## Active-plan resolution

Priority (used by `inject_plan_state`):

1. `DD_ACTIVE_PLAN` env var (explicit override — returned as-is, even if the
   path doesn't exist).
2. `.claude/active-plan` file (first non-empty line; repo-relative).
3. mtime fallback over `plans.fallback_glob` (newest match; annotated in
   output as heuristic).
