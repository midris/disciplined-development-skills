---
name: adversarial-review-loop
description: Use when an adversarial review surfaces findings — including when successive rounds keep surfacing new, surface-different findings (possible shared root), and always when a review loop enters its third cycle. Applies to both internal (self-review, mid-flight work, code review) and external (a different model, a CI reviewer bot, a required reviewer) reviews.
---

# Adversarial review loop

Apply `disciplined-research` before stating or relying on factual workflow, rule,
round, counter, owner, or next-action claims, and disclose their support
unambiguously.

## Scope and precedence

This skill governs review remediation for:

- periodic and cadence-triggered reviews;
- Gate-5 self-review;
- whole-branch final review;
- external review.

It does not govern a plan-execution skill's per-task review loop.
While `superpowers:subagent-driven-development` is reviewing an individual task, follow that skill's fix-round limit, reviewer selection, escalation, and breaker rules.
Keep that task workflow's completed-round record truthful: if its next round later
passes, advance its recorded round while keeping the whole-branch counter separate.
When comparing the two workflows, state the upstream task loop's next fix round,
scoped re-review, and breaker timing; do not merely say its breaker is inapplicable
to the whole-branch loop.

When an upstream execution skill reaches its final whole-branch review, use the upstream skill to initiate the review, then use this skill to remediate its findings.
This skill's three-cycle cap and cold-read escape govern that whole-branch remediation loop.

## The pattern

1. **Address** every [P0]/[P1]/[P2] finding by its *class*, not just the cited line — a reviewer samples one instance; fix only that line and the siblings return next round.
   - **Name the class** — e.g. "stale command", "`cd` that strands the shell", "unqualified threshold claim".
   - **Enumerate it across the branch** — grep for that pattern; run each executable doc claim.
   - **Fix every member before re-running.**

   This is `sweeping-stale-references` + `adversarial-review`'s "Enumerate every class" applied to findings. Decide each [P3]: act, or defer/dismiss with on-page rationale.
2. **Re-run** the same reviewer against the new HEAD. This applies within
   the review contexts owned above; an upstream per-task loop chooses its own
   reviewer according to its rules.
3. **Repeat** until clean (zero [P0]/[P1]/[P2]) OR you hit the iteration cap.

## Iteration cap: 3

A **cycle** is **review → class-sweep → re-run**.
Take at most **three**.
If the third cycle still returns [P0]/[P1]/[P2], take the cold-read escape below — do not proceed to a fourth cycle.

Three outcomes per cycle — new surface each round is necessary but not sufficient; the **root** decides.
Judge the accumulated set from all rounds, not the newest — the history is a dataset, not a news feed:
- **Scattered** — new surface, no shared root → continue (fix + re-run).
- **Drift** — re-litigation or trivial/style nits → the cap interrupts it.
- **Shared-root** — surface-different findings that name **one axis** → attack the root (next section).

Below the cap, the same *kind* of finding recurring across cycles means step 1's class-sweep was incomplete — do it now, not another single-instance round.
At the cap, any remaining [P0]/[P1]/[P2] findings trigger the cold-read escape, never a sweep-and-continue; P3-only is clean and does not trigger the escape.

## Find the pattern, attack the root

**Mandatory at cycle 3.** Two cycles done, findings still coming — STOP.
Before any fix, dismissal, or re-run:

1. Re-read every round's findings as one set.
2. Write the pattern verdict in the loop's work artifact. The pattern may sit in the reviewed artifact, in your own governing text (your wording keeps generating findings), or in the reviewer (repeat themes, re-raised dismissals, blind spots). "No shared pattern" is a valid verdict — only in writing, citing each round.
3. Attack the pattern where it lives: fix the class in the artifact, fix the wording in your text, or close a reviewer re-raise with a written ruling — don't just fix the latest findings.

**Don't wait for cycle 3 when the axis is already visible** (two cycles in, one theme: all failure-path, all concurrency, all auth-boundary, …).
To attack an axis in the artifact:

1. **Name the axis.**
2. **Enumerate every site that could violate the invariant — project-wide, across all code paths, not just the reviewed file(s) or cited locations.** A root closed only locally resurfaces elsewhere and restarts the loop there later. Use a ready checklist if one fits (e.g. the `durability` angle in `adversarial-review`).
3. **Fix the whole axis in one pass, then re-run.**

A **higher-order class-sweep**: step 1 sweeps one class within a round; this sweeps a class spanning rounds and surface-different symptoms.

**At the cap, escape — even for a shared root.** A [P0]/[P1]/[P2] finding on the 3rd cycle's re-run *is* the cap (3 cycles done, blocking findings remain) — not a new below-cap round to attack the root in.
Root-attack is below-cap only; at the cap a shared root still goes to the cold-read escape (which may confirm the axis and call for a redo).

**Don't over-fire.** A shared root = findings that violate **one invariant** (closing it removes the class) — not a shared *topic*.
A SQL-injection and an N+1 query both "touch the database" but violate different invariants (parameterize input vs. batch queries) → scattered, continue.

## At the cap: cold-read escape

Start/dispatch a fresh review with no conversation memory.
Use a subagent, another model, another human, or a clean new session.

- **Confirms findings** → consider redo, not another iteration.
- **Diverges materially** → trust the cold read and stop the loop. Remain blocked if
  that read has any P0–P2; declare clean only if it has none.
- **Confirms fix-forward** → continue only if productive; the cap resets for three more cycles, gated by another escape if findings persist.

Record the escape and verdict in a work artifact (plan, spec, PR, review thread, or — for design rationale — a code comment at the decision site) so the next reader sees why iteration stopped.

## What counts as "clean"

Zero [P0]/[P1]/[P2] findings on the latest run. [P3]-only is acceptable advisory — surface rationale on-page if ignoring.

## Rationalizations

| Excuse | Reality |
|---|---|
| "We did a cold read, this must be drift now." | Cycle count isn't the criterion. Apply the per-cycle test (scattered / drift / shared-root) to the accumulated set as of each cycle. |
| "The reviewer reported one finding, so there's one thing to fix." | It sampled one instance of a class. Fix the line, siblings return next round — enumerate the class, fix all. |
| "Each round found a new nit, so iteration is productive." | One-nit-per-round on the same class is drift in a productivity mask. Sweep the class. |
| "I can't declare clean off my own fix, so re-run now." | Re-run after the class-sweep, not before. Re-running a one-instance fix burns the round. |
| "New surface, so one more sweep past the cap is fine." | At the cap the escape is mandatory — sweeping is a below-cap move, not a way to skip it. |
| "Each round found a NEW, real issue — productive, keep going." | New + real + one shared root = symptoms of an unexamined axis. Audit the axis; don't fix the Nth symptom. |
| "These findings are unrelated — different files and symptoms." | Surface-different, root-same. Test for one axis — in the artifact, your governing text, or the reviewer's behaviour — before calling them scattered. |
| "The reviewer will confirm green next round." | It re-probes the open axis every round; new instances keep coming until you close it. |
| "Stepping back to audit is slower than fixing this finding." | Many reactive rounds vs one audit. Once ≥2 rounds share a root, the audit is faster. |
| "Both findings touch X (the DB / the parser / input) — that's the axis." | A shared topic isn't a root. An axis is one invariant whose closure removes the class; findings that violate different invariants are scattered → continue. |
| "I closed the axis in the file under review — done." | An axis left open in other files resurfaces and restarts the loop there. Audit the pattern across the whole project, not just the reviewed location. |
| "The 3rd cycle's re-run found a new shared-root issue — that's a new round, I'll attack the root." | A finding on the 3rd re-run **is** the cap: 3 cycles done, findings remain → escape. Root-attack is below-cap only; you don't get a 4th round to attack it in. |
| "The prior rounds are in my context — I know what they said." | Knowing ≠ analysing. Write the verdict over the full set. |
| "This round's findings are real — fix first, step back after." | The step-back gates cycle 3. Real findings every round is what an unattacked pattern looks like. Verdict first. |
