---
name: adversarial-review-loop
description: Use when an adversarial code review surfaces findings during self-review, mid-flight work, or code review.
---

# Adversarial review loop

## The pattern

1. **Address** every [P0]/[P1]/[P2] finding in code. Decide each [P3]: act, defer with on-page rationale, or dismiss with on-page rationale.
2. **Re-run** the same reviewer against the new HEAD.
3. **Repeat** until clean (zero [P0]/[P1]/[P2]) OR you hit the iteration cap.

## Iteration cap: 3

Three review-fix cycles is the cap. After cycle 3 returns findings, the next move is the cold-review escape below, not another fix pass.

**Productive iteration** finds NEW issues on NEW surface each cycle. **Drift** re-litigates the same concerns or surfaces trivial/style findings. The cap interrupts drift before it consumes more cycles.

## At the cap: cold-review escape

Start/dispatch a fresh review with no conversation memory. Use a subagent, another
model, another human, or a clean new session.

- **Confirms findings** → consider redo, not another iteration.
- **Diverges materially** → trust the cold read; stop.
- **Confirms fix-forward** → continue only if productive; cap restarts: another escape after 3 more cycles if findings persist.

Record the escape and verdict in a work artifact so the next reader sees
why iteration stopped or continued: plan, spec, PR, review thread, or code
comment when the escape is design rationale.

A comment capturing code/design rationale at the decision site is often
the most effective way to communicate with a future reviewer or reader
when they are about to re-litigate.

## What counts as "clean"

Zero [P0]/[P1]/[P2] findings on the latest run. [P3]-only is acceptable advisory — surface rationale on-page if ignoring.

## Rationalizations

| Excuse | Reality |
|---|---|
| "we did a cold read, this must be drift now" | Cycle count isn't the criterion. Apply the productive vs drift test to what each new cycle found. |
