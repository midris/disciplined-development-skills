---
name: adversarial-review-loop
description: Use when an adversarial review surfaces findings. This applies to both internal (self-review, mid-flight work, code review) and external (a different model, a CI reviewer bot, a required reviewer) reviews.
---

# Adversarial review loop

## The pattern

1. **Address** every [P0]/[P1]/[P2] finding by its *class*, not just the cited line — a reviewer samples one instance; fix only that line and the siblings return next round.
   - **Name the class** — e.g. "stale command", "`cd` that strands the shell", "unqualified threshold claim".
   - **Enumerate it across the branch** — grep for that pattern; run each executable doc claim.
   - **Fix every member before re-running.**

   This is `sweeping-stale-references` + `adversarial-review`'s "Enumerate every class" applied to findings. Decide each [P3]: act, or defer/dismiss with on-page rationale.
2. **Re-run** the same reviewer against the new HEAD.
3. **Repeat** until clean (zero [P0]/[P1]/[P2]) OR you hit the iteration cap.

## Iteration cap: 3

Three review-fix cycles is the cap. After cycle 3 returns findings, the next move is the cold-read escape below, not another fix pass.

**Productive iteration** finds NEW issues on NEW surface each cycle. **Drift** re-litigates the same concerns or surfaces trivial/style findings. The cap interrupts drift before it consumes more cycles. Below the cap, the same *kind* of finding recurring across rounds means step 1's class-sweep was incomplete — do it now, not another single-instance round. At the cap, any findings trigger the cold-read escape, never a sweep-and-continue.

## At the cap: cold-read escape

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
| "We did a cold read, this must be drift now." | Cycle count isn't the criterion. Apply the productive vs drift test to what each new cycle found. |
| "The reviewer reported one finding, so there's one thing to fix." | It sampled one instance of a class. Fix the line, siblings return next round — enumerate the class, fix all. |
| "Each round found a new nit, so iteration is productive." | One-nit-per-round on the same class is drift in a productivity mask. Sweep the class. |
| "I can't declare clean off my own fix, so re-run now." | Re-run after the class-sweep, not before. Re-running a one-instance fix burns the round. |
| "New surface, so one more sweep past the cap is fine." | At the cap the escape is mandatory — sweeping is a below-cap move, not a way to skip it. |
