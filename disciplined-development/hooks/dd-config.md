# dd-config.md — Disciplined-Development Config Schema Reference

## Overview

Two layers of JSON config + env overrides:

- **Skill defaults:** `lib/dd-defaults.json` — ships with the skill, the
  schema; treat as read-only.
- **Project override (single surface):** `.claude/dd-config.json` — override
  only what you need; delete a key to fall back to the default.

### Precedence (lowest → highest)

1. `dd-defaults.json` (shipped defaults)
2. `.claude/dd-config.json` (project overrides)
3. `DD_*` override env vars (path/timeout knobs — see below)
4. `DD_SKIP_*` env vars (hook bypasses)

### Merge semantics

- **Arrays REPLACE** — to extend a default list, copy it in full and append.
- **Objects DEEP-MERGE** — `"counters": {"review_threshold": 8}` keeps
  `discipline_threshold` from defaults.

Regex patterns (where present) use Python `re` syntax. A malformed
`.claude/dd-config.json` (invalid JSON / non-object) is discarded silently and
defaults stand.

### No config-driven disable

`dd-config.json` has no hook enable/disable map. The only way to silence a hook
is its `DD_SKIP_*` env var — a human escape the model can't set by editing a
tracked file. The one hard gate (`pre_pr_review`) must not be model-disableable.

---

## `counters`

| Key | Type | Default | Description |
|---|---|---|---|
| `discipline_threshold` | int | `25` | Tool-calls since the last re-ground before `discipline_nudge` fires. |
| `review_threshold` | int | `5` | Landed commits since the last review (or fork-base) before `review_nudge`'s cadence segment fires. |

Both are starting guesses — tune on observed behavior. Bool values are rejected
(a config typo like `true` won't become a threshold of 1).

---

## `review_tiers`

Per-tier reviewer config for `dd_review.py`. Each tier:

| Sub-key | Type | Description |
|---|---|---|
| `reviewer` | string | `claude` or `codex`. |
| `model` | string | Model id (e.g. `opus`, `gpt-5.5`). |
| `default_effort` | string | `low` / `medium` / `high` (escalated by diff size). |

| Tier | Default reviewer / model / effort |
|---|---|
| `regular` | claude / opus / medium |
| `cold_read_escalation` | claude / opus / high |
| `pre_pr` | codex / gpt-5.5 / medium |

Projects without codex set `review_tiers.pre_pr.reviewer = "claude"` (no
runtime `$PATH` probe).

---

## `strategy_selector`

Decides stuffed-vs-fetched dispatch + high-effort escalation by diff size.

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
| `trunk_branches` | list[string] | `["master", "main"]` | Fork-base resolution: the first that resolves is the merge-base ref for the review diff + commit counts. |

(The old chunk/phase templates + filename regex are gone — auto-detection was
removed; the pre-PR `--base` carries the chunk→phase case.)

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
| `prompt_path` | string | `.claude/skills/adversarial-review/SKILL.md` | Prompt header for `dd_review.py` **claude** mode (relative → repo root). Codex runs bare (built-in review). Env: `DD_REVIEW_PROMPT_PATH`. |

---

## `codex`

| Key | Type | Default | Description |
|---|---|---|---|
| `pr_review_timeout_s` | int | `600` | Reviewer wall-clock timeout for `dd_review.py`. Env: `DD_REVIEW_TIMEOUT`. |

---

## Env vars

### Bypasses (`DD_SKIP_<HOOK>=1`)

| Env var | Hook silenced |
|---|---|
| `DD_SKIP_INJECT_PLAN_STATE` | `inject_plan_state.py` |
| `DD_SKIP_DISCIPLINE_NUDGE` | `discipline_nudge.py` |
| `DD_SKIP_REVIEW_NUDGE` | `review_nudge.py` |
| `DD_SKIP_COMPACTION_REGROUND` | `compaction_reground.py` |
| `DD_SKIP_PR_REVIEW` | `pre_pr_review.py` (the hard gate) |

### Override knobs

| Env var | Effect |
|---|---|
| `DD_ACTIVE_PLAN` | Force the active plan path (highest-priority resolution). |
| `DD_LOG_DIR` | Override the log directory (highest-priority). |
| `DD_REVIEW_TIMEOUT` | Override `codex.pr_review_timeout_s`. |
| `DD_REVIEW_PROMPT_PATH` | Override `review.prompt_path`. |

**Set in:** the launching shell, `~/.claude/settings.json` `env`, or
`<project>/.claude/settings.local.json` `env`. The model CANNOT set these at
tool-call time — hooks read their own inherited environment. (`DD_CONFIG` /
`DD_DEFAULTS` redirect the config files, for tests; `DD_HARD_BLOCK` is set
internally by `pre_pr_review` and is not user-facing.)

---

## Active-plan resolution

Priority (used by `inject_plan_state` and `dd_review`'s claude prompt):

1. `DD_ACTIVE_PLAN` env var (explicit override — returned as-is, even if the
   path doesn't exist).
2. `.claude/active-plan` file (first non-empty line; repo-relative).
3. mtime fallback over `plans.fallback_glob` (newest match; annotated in
   output as heuristic).
