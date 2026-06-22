# Deferred (research): uniform logging across all dd-review paths

> **SUBSUMED (2026-06-21) by `plans/completed/2026-06-21-review-tooling-overhaul-plan.md`.**
> That overhaul deletes the engine and consolidates *all* review logging into one
> tool + one schema, logging every attempt incl. failures — exactly this note's
> goal, by construction rather than by instrumenting five paths. No separate work
> remains; kept for the schema-drift context it records.

**Status:** Deferred investigation (not a committed design). Raised 2026-06-20 after PR 5.
**Question:** is there a simple way to make **every** dd-review path emit one structured log line?
**Where the fix lands:** upstream in the private dd-skills repo (the hooks/skills here are gitignored
symlinks). Resolve real files with `readlink -f .claude/skills/disciplined-development/hooks/<file>`.

## Problem

dd-review runs through several paths; only the codex **engine** path writes
`.claude/.dd-state/.logs/reviews.jsonl`. The others are invisible, so you cannot answer "did a review
run on branch X, by which path, with what verdict" from logs alone — and a silently-skipped gate looks
identical to "no review was due."

| Path | Emitter | Logs today? |
|---|---|---|
| codex engine (pre-PR, cold-read, nudge) | `hooks/dd_review_runner.py` → `reviews.jsonl` | yes |
| pre-PR hook **no-match / fail-open** | `pre_pr_review.py:97` (`return 0`, no emit) | **no** — silent skip |
| pre-PR hook **env-bypass** (`DD_SKIP_PR_REVIEW=1`) | `pre_pr_review.py:90` — `logger.emit("skip", reason="env_bypass")` → hook log | not in `reviews.jsonl` |
| subagent `adversarial-review` (SDD task + whole-branch) | none (orchestrator-driven) | **no** |
| in-conversation `adversarial-review` / `-loop` skills | none (prompt-driven) | **no** |

*Hook log* = `.claude/.dd-state/.logs/dd-hooks-YYYYMMDD.jsonl` (per-hook events); distinct from
`reviews.jsonl` (review verdicts). Only `reviews.jsonl` is the verdict telemetry this note is about.

**PR 5 evidence (2026-06-20).** The engine logged one `BLOCK` row on the first `gh pr create`. Three
substantive subagent reviews left no row. Then PR #14 opened **unreviewed** via the fail-open skip
(separate bug — `2026-06-20-pre-pr-gate-fail-open-deferred.md`), also unlogged — indistinguishable in
the logs from "no PR was created."

## `reviews.jsonl` schema (the target shape — one JSON object per line)

Recent engine rows carry: `ts, tier, source, reviewer, model, effort, strategy, diff_bytes, base,
branch, head_sha, duration_s, decision, p0, p1, p2, p3, output`. **Fields are not uniform across the
file's history:** `source` is absent from the ~38 oldest rows, and ~31 early rows use `round` in place
of `model/effort/strategy/diff_bytes/duration_s`. Design new rows against the recent shape, not by
sampling an arbitrary line. Inspect one row: `tail -1 .claude/.dd-state/.logs/reviews.jsonl | python3 -m json.tool`.

## Goal

Make every path above emit one row in this schema — **including the skip cases** (`decision=skip`/
`no_match`/`bypass` + a `reason`) so a bypassed or fail-open gate is visible.

## Candidate approaches (decide one; don't build all)

1. **Shared emitter for the code paths.** A tiny `log_review(...)` in `hooks/lib`, called at every
   decision point — crucially at `pre_pr_review.py:97` (no-match) and `:90` (env-bypass). Cheapest;
   covers engine + hook paths with one writer.
2. **Skill/orchestrator-emitted rows for the prompt-driven paths.** The subagent and in-conversation
   review paths have no Python boundary, so the skill text instructs the orchestrator to append a row
   after each review. Risk: a non-engine writer to the engine-owned log — keep **one** schema
   definition, and consider a sibling log for non-engine rows to avoid contention.

## Open questions
- One log (`reviews.jsonl`) for all paths, or engine vs. non-engine sibling logs?
- Can the prompt-driven paths log reliably without a code boundary? If not, is a thin wrapper command
  worth it, or is "best-effort, may be missing" acceptable for those rows?
- The pre-PR no-match/fail-open path currently logs nothing; this note covers **logging** it. The
  separate *fix* (fail-closed + matcher robustness) is its own bug — see the linked note above.

## Test scaffolding
(in the resolved hooks dir — `dirname $(readlink -f .claude/skills/disciplined-development/hooks/pre_pr_review.py)`)
- `tests/test_pre_pr_review.py` — assert the no-match and env-bypass branches emit a row.
- `tests/test_dd_review_runner.py` — the engine-row shape is the schema reference.

## Pointers
- Log: `.claude/.dd-state/.logs/reviews.jsonl`. Emitters: `dd_review_runner.py`, `pre_pr_review.py`.
- Skills: `adversarial-review`, `adversarial-review-loop` (symlinks → dd-skills repo; change upstream).
- `reviews.jsonl` also persists verbatim codex gate findings (recoverable when a plan only paraphrases them).
