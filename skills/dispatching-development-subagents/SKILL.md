---
name: dispatching-development-subagents
description: 'Use when dispatching a development subagent whose code changes you will integrate — an implementation task, a fix for a review finding, or a parallel batch of changes. Triggers: "dispatch a subagent", "spawn an agent", delegating a fix, fanning a change out across files, or before trusting a subagent''s commits or diff. When this skill applies, `disciplined-research` also applies to factual premises in the dispatch, returned handoff, and landed prose.'
---

# Dispatching Development Subagents

**Role:** Companion — discipline overlay on `superpowers:subagent-driven-development` and `superpowers:dispatching-parallel-agents`.
Invoke when you dispatch a development subagent — one that changes code and commits — including ad-hoc fixers those skills don't model.
Research/review subagents (findings, not commits) are out of scope — verify their claims per `disciplined-research`.
**Owns:** the scope contract, the out-of-scope gradient, the report extension, and the verify-every-commit duty.
**Does not own:** plan-task execution + two-stage review (`superpowers:subagent-driven-development`); parallel fan-out mechanics (`superpowers:dispatching-parallel-agents`); the orchestrator's own gates (`disciplined-development`).
**Audience:** the orchestrator.
If you are a dispatched subagent, you are not allowed to dispatch your own subagents.
Follow `disciplined-development` + your dispatch prompt (see the subagent red flag below).

## Overview

**A subagent's output is a claim, not a result.** Scope the dispatch crisply; verify the diff against it.
Reports omit and mislabel their own over-reach — long runs especially drift into "while I'm here" changes — so the diff is the only ground truth.

**Exceeding your scope to be helpful is the over-reach, not the spirit.** The spirit is a minimal, verifiable change plus an honest list of what you left for the orchestrator.

## When you dispatch

- **Ground the dispatch contract:** the dispatch prompt must explicitly require applying `disciplined-research` before stating a factual finding, scope, file, constraint, identity, hook, counter, or ownership claim, then map the claim to the best available supplied source. Map project claims to project sources and skill-owned research, identity, authority, and boundary requirements to the applicable skill sources.
- **Write a scope contract:** name the working root, in-scope files (and shape of change), governing files, and locked constraints. Make relative paths unambiguous from that root.
- **Make skill locators executable:** when supplied skills live outside the working root, name an absolute or otherwise resolving locator; do not present `skills/...` as project-relative. Never substitute a guessed host-global path: name only a locator supplied by the task or verified to resolve in the subagent's environment.
- **Stamp the subagent's identity in the prompt:** the subagent is not the orchestrator. Review / checkpoint / PR gates and hook nudges belong to the orchestrator — a due gate does not promote the subagent. The subagent reports a due gate and stops, and dispatches no further subagents.
  The subagent may inspect its candidate and report whether it appears conforming; never instruct it to accept work or gate passage. Acceptance belongs to the orchestrator or user.
  The authority clause is incomplete unless it explicitly forbids acting on hook nudges as well as review, checkpoint, and PR gates.
  Reporting the gate and stopping applies whenever a parent gate is due, whether or not the subagent also owes verification.
  When one message carries both verification owed for the subagent's own work and an orchestrator-owned gate, the subagent completes and reports its verification first, reports the parent gate as due and explicitly names the orchestrator as its owner or recipient, then stops immediately. That gate report is the subagent's final action.
  Verification owed at that boundary means direct running-system evidence for the
  landed work; an ordinary test alone is insufficient.
  Report its outcome truthfully as passed, failed/blocking, or not exercisable;
  completing an invocation does not imply that verification passed.
  The returned report maps its counter, hook, gate, verification, and ownership
  claims to precise supplied source identifiers or directly observed invocations;
  repeating those claims without the mappings is incomplete.
- **Carry research into the handoff:** the dispatch prompt and expected returned handoff must explicitly require applying `disciplined-research` before factual identity, hook, gate, counter, verification, ownership, or completion claims and map those claims to support. Generic instructions to ground or reread sources do not replace this requirement.
  State that requirement for the returned handoff or post-hook response itself; a
  research instruction addressed only to the dispatch phase does not carry it.
- **One finding per dispatch by default.** Batch only same-kind, non-overlapping, behavior-free changes; split out anything coupled or behavior-changing. Mixed batches are where drift hides.
  Do not widen one finding into a sibling-instance or defect-class reconciliation assignment. This explicit one-finding/do-not-widen contract is a no-extras rule for the dispatch: surface every other change without acting. A reference sweep finds encodings of the assigned change; it does not authorize fixing adjacent instances.
- **Dispatch a finding verbatim.** Quote it as the reviewer first wrote it — a later re-framing or your own summary narrows scope silently.
- **Require scope disclosure in the report.** Use the execution skill's
  current report mechanism when it defines one. In addition, require
  `Changes beyond dispatched scope: none` or list each extra change with a
  one-line rationale. This disclosure requirement does not depend on an
  upstream report heading or format.
- **State the out-of-scope rule in the prompt:** the subagent acts only on small, safe, obviously-correct fixes, each in its own commit; anything risky, large, design-level, or uncertain — including deleting or overwriting a tracked file — it surfaces, doesn't act.
  Preserve that gradient unless a governing project source or an explicit dispatch instruction forbids all extras. Naming a bounded finding or in-scope files does not by itself disable the gradient. Under an explicit no-extras rule, surface every extra without acting. Do not otherwise invent a separate-authorization prerequisite that disables the small/safe/obvious branch.
  When `disciplined-development` governs, its signed scope is the governing no-extras rule: surface work outside it until Gate 2 records decision-owner approval in revised signed scope.
- **Require a verified integration handoff:** in the returned handoff, map every factual claim in the handoff or landed prose—commit messages, code comments, and documentation—to the specific support the development subagent verified, such as implementation, compiler or test output, or a primary source. Each mapping names a precise source identifier, such as a repository-relative path or exact observed invocation; naming only the evidence kind or quoting a value is insufficient. Unsupported rationale is omitted, not hedged or landed. This added contract applies only at the development integration boundary; `disciplined-research` governs other factual claims, and research/review subagents remain outside this skill.
  The handoff contract is incomplete unless it explicitly requires omission of unsupported rationale from both the handoff and landed prose.
  It also requires the exact verification commands or invocations and their directly observed results; a summary such as “tests pass” is not the evidence.
  The handoff and scope disclosure never replace the orchestrator's inspection of
  each returned commit's stat and complete diff against the dispatch contract.
  Before commit, require the applicable reference sweep and its truthful durable bookkeeping; require the returned handoff to identify that sweep evidence rather than merely claiming the commit is green.

## Verify — orchestrator, non-negotiable

The report is a claim, not the diff.
For every commit a subagent lands: `git show --stat` then the diff → reconcile against the scope contract → apply its governing disposition; absent a stricter scope rule, keep extra changes on merit or revert.
A clean test run is not verification — tests pass over silent out-of-scope edits.
Placeholders are a plan, not observed evidence: never label verification complete
until the exact invocation and result have actually been observed.

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

**As the dispatched subagent** — You are not allowed to dispatch your own subagents.
Follow `disciplined-development` + your dispatch prompt.
Beyond that, you over-reach if you think:

- "A review or another gate action is due—so I will take it." (Gate actions belong to the orchestrator; report what is due and stop.)
- "While I'm here, I'll also fix / tidy this."
- "This tracked file looks like junk — I'll delete it."
- "I'll fold this into the same commit."
- "It's a real improvement, so it's fine."
- "The dispatch didn't say I *couldn't*."

All mean: stop.
Out of scope — disclose; act only if small, safe, obvious, in its own commit; else surface and move on.

## Composition

- `superpowers:subagent-driven-development` owns plan-task execution and
  per-task review. This skill adds an upstream-format-independent scope
  disclosure requirement.
- `superpowers:dispatching-parallel-agents` — parallel fan-out; the same overlay applies per agent.
- `disciplined-development` Principle 4 points here.
