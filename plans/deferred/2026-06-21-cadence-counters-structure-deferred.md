# Deferred: revisit the edits/commits cadence-counter structure

**Status:** Deferred. Raised 2026-06-21 during the review-tooling overhaul
(`plans/2026-06-21-review-tooling-overhaul-plan.md`), which deliberately keeps the
hook shape stable to bound blast radius.

## The question

The hooks maintain **two** per-branch cadence counters with separate triggers:

- `edits.count` — unreviewed Edit/Write count; nudge at 30, hard block at 60
  (`edit_counter.py`, `edit_block.py`).
- commits-since-`review.checkpoint` — nudge at 3, hard block at the 6th
  (`commit_block.py`, `review_nudge.py`).

The overhaul moved to a **single deep + whole-repo review mode**, so a clean review
now resets **both** counters at once. That removes the original reason the two were
distinct (light edit-review reset only edits; deep cold-read reset the checkpoint).
So: **are two counters still warranted, or should they collapse / change shape?**

Specifics to examine when resuming:

- Do "edits since review" and "commits since review" still measure meaningfully
  different drift, now that one review clears both — or is one redundant?
- Should both remain **hard** blocks, or should one soften to a nudge?
- Does the trust model still fit — both soft counters are model-self-reset via the
  log-review tool (a clean review the model self-reports)?

## Why deferred

Counter/threshold redesign is a separate concern best done **after** the new review
machinery lands and the consolidated log has accrued real data. The new
`reviews.jsonl` now carries `edits_count`, `commits_since_checkpoint`, and `trigger`
per review — use it to see how the counters actually behave before retuning, rather
than guessing.

## Scope boundary

This plan owns the **structural** question (how many counters, hard vs soft). The
**threshold-value** calibration (are 30/60 and 3/6 the right numbers, and should
"review earlier/more often" lower them) is already tracked in
`plans/deferred/2026-06-14-threshold-rationale-and-calibration.md` — resume both
together; don't duplicate the value question here.

## Pointers

- Hooks: `edit_counter.py`, `edit_block.py`, `commit_block.py`, `review_nudge.py`.
- State: `lib/state.py` (`edits.count`, `review.checkpoint`, fork-base fallback).
- Design: `plans/2026-06-21-review-tooling-overhaul.md` (State model section).
