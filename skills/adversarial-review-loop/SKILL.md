---
name: adversarial-review-loop
description: Use when an adversarial review surfaces findings — including when successive rounds keep surfacing new, surface-different findings (possible shared root). Applies to both internal (self-review, mid-flight work, code review) and external (a different model, a CI reviewer bot, a required reviewer) reviews.
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

A **cycle** is **review → class-sweep → re-run**. Take at most **three**. If the third cycle still returns [P0]/[P1]/[P2], take the cold-read escape below — do not proceed to a fourth cycle.

Three outcomes per cycle:
- **Scattered** — new surface, no nameable shared root → continue (fix + re-run).
- **Drift** — re-litigation or trivial/style nits → the cap interrupts it.
- **Shared-root** — new, surface-different findings that name **one axis** → attack the root (next section). New surface alone isn't "productive"; it must also be root-scattered.

Below the cap, the same *kind* of finding recurring across cycles means step 1's class-sweep was incomplete — do it now, not another single-instance round. At the cap, any findings trigger the cold-read escape, never a sweep-and-continue.

## Find the pattern, attack the root

**Trigger:** across ≥2 cycles, new findings — each new, real, surface-different — name **one axis** (all failure-path, all concurrency, all input-validation, all error-contract, all auth-boundary, …). Then:

1. **Name the axis.**
2. **Enumerate every site that could violate the invariant — project-wide, across all code paths, not just the reviewed file(s) or cited locations.** A root closed only locally resurfaces elsewhere and restarts the loop there later. Use a ready checklist if one fits (e.g. the `durability` angle in `adversarial-review`).
3. **Fix the whole axis in one pass, then re-run.**

This is a **higher-order class-sweep**: step 1 sweeps one *named class within a round*; this sweeps a class spanning *rounds and surface-different symptoms*. Proactive, below the cap — not the cold-read escape (at-cap, fresh eyes).

**At the cap, escape — even for a shared root.** A finding on the 3rd cycle's re-run *is* the cap (3 cycles done, findings remain) — not a new below-cap round to attack the root in. Root-attack is below-cap only; at the cap a shared root still goes to the cold-read escape (which may confirm the axis and call for a redo).

**Don't over-fire.** A shared root = the findings violate **one invariant** — closing it removes the whole class. A shared *topic* is not a root: a SQL-injection and an N+1 query both "touch the database" but violate different invariants (parameterize untrusted input vs. batch related queries) → scattered, continue. Don't invent an umbrella axis.

## At the cap: cold-read escape

Start/dispatch a fresh review with no conversation memory. Use a subagent, another
model, another human, or a clean new session.

- **Confirms findings** → consider redo, not another iteration.
- **Diverges materially** → trust the cold read; stop.
- **Confirms fix-forward** → continue only if productive; the cap resets for three more cycles, gated by another escape if findings persist.

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
| "We did a cold read, this must be drift now." | Cycle count isn't the criterion. Apply the per-cycle test (scattered / drift / shared-root) to what each new cycle found. |
| "The reviewer reported one finding, so there's one thing to fix." | It sampled one instance of a class. Fix the line, siblings return next round — enumerate the class, fix all. |
| "Each round found a new nit, so iteration is productive." | One-nit-per-round on the same class is drift in a productivity mask. Sweep the class. |
| "I can't declare clean off my own fix, so re-run now." | Re-run after the class-sweep, not before. Re-running a one-instance fix burns the round. |
| "New surface, so one more sweep past the cap is fine." | At the cap the escape is mandatory — sweeping is a below-cap move, not a way to skip it. |
| "Each round found a NEW, real issue — productive, keep going." | New + real + one shared root = symptoms of an unexamined axis. Audit the axis; don't fix the Nth symptom. |
| "These findings are unrelated — different files and symptoms." | Surface-different, root-same. Test whether one axis name covers them before calling them scattered. |
| "The reviewer will confirm green next round." | It re-probes the open axis every round; new instances keep coming until you close it. |
| "Stepping back to audit is slower than fixing this finding." | Many reactive rounds vs one audit. Once ≥2 rounds share a root, the audit is faster. |
| "Both findings touch X (the DB / the parser / input) — that's the axis." | A shared topic isn't a root. An axis is one invariant whose closure removes the class; findings that violate different invariants are scattered → continue. |
| "I closed the axis in the file under review — done." | An axis left open in other files resurfaces and restarts the loop there. Audit the pattern across the whole project, not just the reviewed location. |
| "The 3rd cycle's re-run found a new shared-root issue — that's a new round, I'll attack the root." | A finding on the 3rd re-run **is** the cap: 3 cycles done, findings remain → escape. Root-attack is below-cap only; you don't get a 4th round to attack it in. |
