---
name: dispatching-development-subagents
description: 'Use when dispatching a development subagent whose code changes you will integrate — an implementation task, a fix for a review finding, or a parallel batch of changes. Triggers: "dispatch a subagent", "spawn an agent", delegating a fix, fanning a change out across files, or before trusting a subagent''s commits or diff.'
---

# Dispatching Development Subagents

**Role:** Companion — discipline overlay on `superpowers:subagent-driven-development` and `superpowers:dispatching-parallel-agents`. Invoke when you dispatch a development subagent — one that changes code and commits — including ad-hoc fixers those skills don't model. Research/review subagents (findings, not commits) are out of scope — verify their claims per `disciplined-research`.
**Owns:** the scope contract, the out-of-scope gradient, the report extension, and the verify-every-commit duty.
**Does not own:** plan-task execution + two-stage review (`superpowers:subagent-driven-development`); parallel fan-out mechanics (`superpowers:dispatching-parallel-agents`); the orchestrator's own gates (`disciplined-development`).

## Overview

**A subagent's output is a claim, not a result.** Scope the dispatch crisply; verify the diff against it. Reports omit and mislabel their own over-reach — long runs especially drift into "while I'm here" changes — so the diff is the only ground truth.

**Exceeding your scope to be helpful is the over-reach, not the spirit.** The spirit is a minimal, verifiable change plus an honest list of what you left for the orchestrator.

## When you dispatch

- **Write a scope contract:** name the files (and the shape of the change) in scope, plus the governing files and locked constraints touching that area.
- **One finding per dispatch by default.** Batch only same-kind, non-overlapping, behavior-free changes; split out anything coupled or behavior-changing. Mixed batches are where drift hides.
- Require the report below, and state the out-of-scope rule in the prompt.

## When you ARE the dispatched subagent

- **Do the task you were given.**
- **Out-of-scope finds — disclose always.** Act only when the fix is small, safe, and obviously correct, in its own commit. Risky, large, design-level, or uncertain → surface, don't act. Deleting or overwriting a tracked file is not "small and safe" unless the dispatch asked for it — surface it.
- **Report** with the `superpowers:subagent-driven-development` Report Format plus an explicit **"changes beyond the dispatched scope"** line, each with a one-line rationale.

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

You are about to over-reach if you think:

- "While I'm here, I'll also fix / tidy this."
- "This tracked file looks like junk — I'll delete it."
- "I'll fold this into the same commit."
- "I'm a few commits in; I'll run a review / write a checkpoint." (unasked)
- "It's a real improvement, so it's fine."
- "The dispatch didn't say I *couldn't*."

All mean: out of scope. Disclose it; act only if small, safe, and obviously correct, in its own commit; else surface and move on.

## Composition

- `superpowers:subagent-driven-development` — plan-task execution + two-stage review; this skill extends its Report Format with the out-of-scope line.
- `superpowers:dispatching-parallel-agents` — parallel fan-out; the same overlay applies per agent.
- `disciplined-development` Principle 4 points here.
