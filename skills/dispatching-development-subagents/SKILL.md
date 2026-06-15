---
name: dispatching-development-subagents
description: 'Use when dispatching a development subagent whose code changes you will integrate — an implementation task, a fix for a review finding, or a parallel batch of changes. Triggers: "dispatch a subagent", "spawn an agent", delegating a fix, fanning a change out across files, or before trusting a subagent''s commits or diff.'
---

# Dispatching Development Subagents

**Role:** Companion — discipline overlay on `superpowers:subagent-driven-development` and `superpowers:dispatching-parallel-agents`. Invoke when you dispatch a development subagent — one that changes code and commits — including ad-hoc fixers those skills don't model. Research/review subagents (findings, not commits) are out of scope — verify their claims per `disciplined-research`.
**Owns:** the scope contract, the out-of-scope gradient, the report extension, and the verify-every-commit duty.
**Does not own:** plan-task execution + two-stage review (`superpowers:subagent-driven-development`); parallel fan-out mechanics (`superpowers:dispatching-parallel-agents`); the orchestrator's own gates (`disciplined-development`).
**Audience:** the orchestrator. If you are the dispatched subagent, this is not your manual — your doctrine is `disciplined-development` plus your dispatch prompt (see the subagent red flag below).

## Overview

**A subagent's output is a claim, not a result.** Scope the dispatch crisply; verify the diff against it. Reports omit and mislabel their own over-reach — long runs especially drift into "while I'm here" changes — so the diff is the only ground truth.

**Exceeding your scope to be helpful is the over-reach, not the spirit.** The spirit is a minimal, verifiable change plus an honest list of what you left for the orchestrator.

## When you dispatch

- **Write a scope contract:** name the in-scope files (and shape of change), the governing files, and locked constraints in that area. Explicitly tell the subagent to not dispatch its own subagents and to ignore hook nudges (review / checkpoint / PR). Both of those are orchestrator responsibilities.
- **One finding per dispatch by default.** Batch only same-kind, non-overlapping, behavior-free changes; split out anything coupled or behavior-changing. Mixed batches are where drift hides.
- **Require the report** (`superpowers:subagent-driven-development` Report Format + a "changes beyond the dispatched scope" line, each with a one-line rationale).
- **State the out-of-scope rule in the prompt:** the subagent acts only on small, safe, obviously-correct fixes, each in its own commit; anything risky, large, design-level, or uncertain — including deleting or overwriting a tracked file — it surfaces, doesn't act.

## Verify — orchestrator, non-negotiable

The report is a claim, not the diff. For every commit a subagent lands: `git show --stat` then the diff → reconcile against the scope contract → keep out-of-scope changes on merit, or revert. A clean test run is not verification — tests pass over silent out-of-scope edits.

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "I found a real bug — I'll just fix it too." | Small+safe → own commit, disclosed. Else surface. |
| "The report says it's in scope." | A claim, not the diff. Diff it — reports mislabel their over-reach. |
| "Tests pass, so the change is fine." | Tests pass over out-of-scope edits; scope ≠ correctness. |
| "It's a long task; a little cleanup won't hurt." | Drift lives in long runs. Surface, don't tidy. |
| "It looked like junk." | Tracked ≠ junk. Surface it; the orchestrator decides. |

## Red Flags — STOP

**As the orchestrator:**

- "The report says DONE — I'll trust it." (diff it; the report isn't the diff)
- "I'll batch these unrelated findings into one dispatch." (mixed batches hide drift)
- "Tests pass, so the diff is fine." (tests pass over out-of-scope edits)

**As the dispatched subagent** — first: are you reading this orchestrator playbook at all? It isn't your manual. Your doctrine is `disciplined-development` plus your dispatch prompt, which carry the review / checkpoint / PR / nested-dispatch limits. Beyond that, you over-reach if you think:

- "While I'm here, I'll also fix / tidy this."
- "This tracked file looks like junk — I'll delete it."
- "I'll fold this into the same commit."
- "It's a real improvement, so it's fine."
- "The dispatch didn't say I *couldn't*."

All mean: stop. Out of scope — disclose; act only if small, safe, obvious, in its own commit; else surface and move on.

## Composition

- `superpowers:subagent-driven-development` — plan-task execution + two-stage review; this skill extends its Report Format with the out-of-scope line.
- `superpowers:dispatching-parallel-agents` — parallel fan-out; the same overlay applies per agent.
- `disciplined-development` Principle 4 points here.
