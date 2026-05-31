# disciplined-development hook stack — design

The durable "why" for the hook layer that scaffolds the
`disciplined-development` skill. This README is the current-state
overview; the hook source lives alongside it in this directory.

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

## The hook set

Five event hooks + one model-callable engine. **One hard block, zero kicks** —
everything except the pre-PR gate is an advisory nudge.

| Component | Event | Role |
|---|---|---|
| `inject_plan_state.py` | UserPromptSubmit | Surface the active plan + checkbox progress + next pending task; reset the per-turn discipline counter; run throttled housekeeping (cleanup). |
| `discipline_nudge.py` | PreToolUse (all tools) | Count tool-calls since the last re-ground; at the threshold emit a fixed "re-read CLAUDE.md + the plan, re-check the skills" nudge and reset. |
| `review_nudge.py` | PostToolUse (Bash) | On a landed commit: always a Gate-3 **verify** reminder; at the review-cadence threshold also a "run `/dd-review regular`" nudge. |
| `compaction_reground.py` | SessionStart + PreCompact | After a resume/compaction (context is a summary), re-ground: re-read the source of truth before acting. |
| `pre_pr_review.py` | PreToolUse (Bash, `gh pr create`) | **The only hard block.** Detect → extract base/cwd → delegate to `dd_review.py pre-pr` with `DD_HARD_BLOCK=1`. Blocks the PR on findings. |
| `dd_review.py` | model-callable CLI | The review engine: `regular` / `cold-read` / `pre-pr` tiers against the fork-base diff. |

Gate 3 (verify before "done") rides the **post-commit** verify nudge, not a
Stop kick: the commit is where an edit becomes an assertion that owes
verification, and PostToolUse reaches the model without a Stop hook's
block-or-be-silent constraint. The model decides what verification fits; the
hook never scans for or grades evidence.

## Three-tier review (`dd_review.py`)

Reviews run at three tiers, configured per project under `review_tiers`. Each
carries its own reviewer / model / effort:

| Tier | Default | When |
|---|---|---|
| `regular` | claude / opus / medium | cadence loop (the `review_nudge` threshold) |
| `cold-read` | claude / opus / high | mid-branch escalation, higher effort |
| `pre-pr` | codex / gpt-5.5 / medium | the `gh pr create` hard gate (+ manual dry-run) |

Rationale: claude credits are abundant, codex scarce — the cadence tiers
default to claude; codex is reserved for the once-per-PR independent
cross-model audit. Projects without codex override
`review_tiers.pre_pr.reviewer` in `dd-config.json` (no runtime `$PATH`
probe). Every tier resolves its diff to the **fork-base** (merge-base vs the
first trunk ref); `pre-pr` honours an explicit `--base`. A clean pass writes
the review checkpoint. `strategy_selector` decides stuffed-vs-fetched dispatch
and high-effort escalation by diff size.

## State model

Two dumb things under `.claude/.dd-state/` (gitignored), keyed by branch — no
marker subsystem:

- **Discipline counter** (`<branch>/discipline.count`) — tool-calls since the
  last re-ground. Bumped by `discipline_nudge`, reset by `inject_plan_state`
  (turn boundary) and on fire.
- **Review checkpoint** (`<branch>/review.checkpoint`) — the HEAD sha at the
  last clean review. `review_nudge` counts commits since it (`git rev-list`);
  no checkpoint → counts from fork-base, gated behind the same threshold.

## Observability (non-negotiable)

Every major hook function emits a structured trace — comprehensive, on by
default, tuned by retention/cleanup rather than by logging less. This is
*recording*, distinct from the rejected output-*policing*.

- **Rolling log:** `.claude/.dd-state/.logs/dd-hooks-YYYYMMDD.jsonl` (append;
  all hooks interleave, keyed by `hook`/`pid`). Dir resolution: `DD_LOG_DIR`
  env → `logging.dir` config → derived `.claude/.dd-state/.logs`.
- **Curated review trace:** `.claude/.dd-state/.logs/reviews.jsonl` — one rich
  record per review (tier, reviewer, model, effort, strategy, diff_bytes,
  base, branch, duration, P0–P3 counts, decision, full reviewer output) for
  offline analysis of what/how-long/is-it-working. Never aged out.
- **Cleanup:** a throttled sweep (from `inject_plan_state`) prunes day-logs
  past `logging.retention_days` and removes orphaned per-branch state dirs.

## Configuration

- **Shipped defaults:** `lib/dd-defaults.json` (read-only; the schema).
- **Single override surface:** `.claude/dd-config.json` — all behavior
  tunables (counters/thresholds, review_tiers, strategy_selector, logging,
  trunk_branches, fallback_glob, codex timeout). Edit a value to override;
  delete a key to fall back to the default.
- **Escape hatches:** `DD_SKIP_<HOOK>=1` env vars (in
  `.claude/settings.local.json`) silence a hook. Env, not config — a human
  escape the model can't set by editing a tracked file. Override knobs
  (`DD_ACTIVE_PLAN`, `DD_LOG_DIR`, `DD_REVIEW_TIMEOUT`, `DD_REVIEW_PROMPT_PATH`)
  live there too. Full reference: `dd-config.md`.

## Companion skills

- **`disciplined-development`** — the doctrine: the Iron Law, five gates,
  principles, rationalization tables. Principle 8 is the source of the review
  cadence.
- **`adversarial-review`** / **`adversarial-review-loop`** — the review prompt
  + the severity contract (P0/P1/P2 block, P3 advisory) and the
  review-fix-review iteration cap + cold-read escape.
- **`lean-plan-writing`**, **`writing-explicit-rationale`**,
  **`sweeping-stale-references`**, **`disciplined-research`** — the
  plan-density, rationale-on-page, stale-reference, and verify-before-claiming
  companions.

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
the tier — nudge (default) vs the one hard gate (only for an irreversible
boundary); (3) keep the trigger dumb (no output-classification); (4) every
gate gets a `DD_SKIP_<NAME>` bypass; (5) test-first; (6) update this README +
the spec. If the surface is for the human, not the model — don't build it.
