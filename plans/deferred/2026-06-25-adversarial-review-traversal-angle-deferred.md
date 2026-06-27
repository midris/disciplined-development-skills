# Add a "traversal" (path/structure-completeness) angle to `adversarial-review` — deferred (2026-06-25)

**Status:** Parked follow-up.

**⚠ Cross-repo:** the implementation edits the **private `disciplined-development-skills` repo**, *not* this project. `adversarial-review/SKILL.md` is a gitignored **symlink** into a local clone (`github-personal:midris/disciplined-development-skills`). Edit + commit **there**, then re-run that repo's `install-skills.sh <meeting-pipeline-root>` so the symlinks resolve. **That repo has concurrent editors — check branch + clean tree before any git op; branch if unsure.**

**Goal:** Add a review **angle** to `adversarial-review` (the "Review angles" table) that catches **structure/path-completeness** failures: a new datum / message / field / contract that must propagate across many layers, sites, or tasks, but is only handled at some of them.

## Why — the baseline (RED evidence, already observed)

During step-13 design (2026-06-25), external **Codex** reviews repeatedly caught a defect class that in-session `adversarial-review` passes — using the *current* angles — **missed, one instance per round**:

- **Wire-path gap:** the step-13 plan said "worker emits `progress` / `model_load_*` / structured-error; engine consumes" but never plumbed them through the **intermediate layers** (`WorkerInboundMessage` enum → `SubprocessWorkerTransport.decode` → `StubWorkerTransport` → engine → `WorkerStatus` → wire encoder → `/status`). The decoder silently drops unknown messages, so the contract couldn't work. (Caught as a Codex P1.)
- **Cross-spec drift:** `worker.enabled` flip timing + progress cadence stated (stale) in three sibling specs while the step-13 spec refined them — leaked one-per-round (commits `1091cd2`, `b9ee1b4`).
- **Plan-as-DAG:** a task wrote a field a *later* task added (forward dep); a "deferred to plan" contract left vague.

These are three faces of **one meta-pattern: completeness/consistency across a structure** — the doc corpus, the layer stack, the task sequence. The current angles cover two faces (`consistency` = corpus drift; `executability` = DAG/contracts) but **none** says "trace a new value end-to-end through every layer it must cross." That is the gap this angle fills.

## The change — apply `superpowers:writing-skills` (this is a skill EDIT; the Iron Law applies)

**Primary — new angle.** Add one row to the "Review angles" table + a "When to apply" entry. Proposed wording (tighten via testing; keep the table's density):

> **traversal** | follow a new datum / message / field / signal through **every** layer, hop, or site it must cross (producer → transport / decoder / stub → consumer → status → wire → UI; or a fact across all its call sites). Flag any layer that silently drops, ignores, or only partially handles it. Reviewing only the source + sink is the failure.

> **When to apply** | when a change introduces or routes a value across process / module / layer boundaries — a new IPC message, event/status field, error code, or a config key consumed in several layers.

**Secondary (optional, anti-bloat permitting) — sharpen `executability`:** add "no **forward** task dependencies (each task compiles/tests given only earlier tasks); every 'deferred to plan' contract pinned to an exact shape, not relocated-but-still-vague."

**Anti-bloat (writing-skills):** `consistency` already covers cross-spec single-source duplication — do **not** duplicate it. If, under testing, `traversal` overlaps `consistency`/`executability` too much to justify its own row, fold the insight into those rows instead. One terse row; match the existing table.

## Implementation (TDD-for-skills — REQUIRED; Iron Law applies to edits)

1. **Setup (cross-repo):** open the `disciplined-development-skills` clone; confirm branch + clean tree (concurrent editors); branch.
2. **Re-read** the current `adversarial-review/SKILL.md` from disk (it may have evolved) — find the exact "Review angles" table + "When to apply" list.
3. **RED (baseline):** run a fresh-context reviewer subagent on a seeded artifact with a planted traversal gap (reduce the step-13 wire-path case: a plan that says "worker emits X, engine consumes X" with no transport/decoder/status layers). Confirm a review **without** the new angle misses it; capture the miss verbatim. Add 2-3 variant gaps (a status field never put on the wire; an error code not mapped through; a config key read in one layer only).
4. **GREEN:** add the angle. Re-run the same scenarios **with** it; confirm the reviewer now flags the missing layers.
5. **REFACTOR:** close wording loopholes; micro-test wording vs a no-guidance control (5+ reps) per writing-skills; `wc -w` to confirm no bloat.
6. **Commit in the dd-skills repo** (not this one); re-run `install-skills.sh`; verify the symlinked skill reflects the change.

## Done-when

- A reviewer subagent **without** the angle misses a planted traversal gap; **with** it, catches it (RED→GREEN demonstrated).
- The angle row + when-to-apply added — terse, non-duplicative of `consistency`/`executability`.
- Committed to the dd-skills repo + skills re-installed.

## Out of scope

- This project's specs/plans (already corrected in-session — see `codex-reviews-on-plans` memory for the meta-pattern).
- The `disciplined-development` parent skill / gates — the angle lives in `adversarial-review` only.
