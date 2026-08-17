---
name: adversarial-review-loop
description: Use when an adversarial review surfaces findings — including when successive rounds keep surfacing new, surface-different findings (possible shared root), and always when a review loop enters its third cycle. Applies to both internal (self-review, mid-flight work, code review) and external (a different model, a CI reviewer bot, a required reviewer) reviews.
---

# Adversarial review loop

Apply `disciplined-research` before stating or relying on factual workflow, rule,
round, counter, owner, or next-action claims, and disclose their support
unambiguously.

## Scope and counters

This skill owns remediation for periodic and cadence-triggered reviews, Gate-5
self-review, whole-branch final review, and external review.

| Review context | Governing workflow |
|---|---|
| Individual task while `superpowers:subagent-driven-development` is reviewing it | That skill owns remediation, including its fix-round limit, reviewer selection, escalation, and breaker. Keep its completed-round record truthful. |
| Final whole-branch review from an execution workflow | The execution skill initiates the review; this skill remediates its findings with an independent three-cycle counter and cold-read escape. |
| Other owned context above | This skill governs remediation, reviewer reuse, the three-cycle counter, and the cold-read escape. |

Never combine task and whole-branch counters.
If an upstream task's next round passes, advance that task's completed-round record; a later whole-branch review still starts its own cycle 1.
When comparing the workflows, state the task loop's next fix round, scoped re-review, and breaker timing rather than only saying that its breaker does not apply to the whole-branch loop.

## State machine

A **cycle** is **review → class-sweep → re-run**.
Complete at most three cycles before the cold-read escape.
For each review result, follow these transitions in order.
Every [P3] must be acted on or deferred/dismissed with on-page rationale. At
cycle-3 entry, the written verdict precedes that disposition.

### 1. Route by cycle and severity

1. If the third cycle's re-run has any [P0]/[P1]/[P2], take the cold-read escape
   in step 6. This is the cap, not a new below-cap round: do not sweep, root-attack,
   or start a fourth ordinary cycle. Dispose any mixed [P3] before escaping.
2. If the third cycle's re-run has no [P0]/[P1]/[P2], apply the P3 rule if needed
   and stop clean.
3. If two cycles are complete and findings continue, enter step 2 before any fix,
   dismissal, or re-run.
4. Otherwise, zero [P0]/[P1]/[P2] is clean. With no findings, stop. For [P3]-only,
   apply the P3 rule above, then stop.
5. If any [P0]/[P1]/[P2] remain, apply the P3 rule to mixed findings, then go to
   step 3.

### 2. At cycle-3 entry, write the verdict first

Re-read every round's findings as one set. Before any action, write a pattern
verdict in the loop work artifact, citing every round:

| Verdict location | Action |
|---|---|
| Reviewed artifact | Fix its complete class, or use step 5 for one shared invariant. |
| Your governing text | Fix the wording; when it generated one shared invariant, continue through step 5's project-wide audit. |
| Reviewer | Record repeat themes, re-raised dismissals, or blind spots; close a re-raised dismissal with a written ruling, not an appeasement edit. |
| No shared pattern | Record that verdict, then use the ordinary class path without inventing an axis. |

After the verdict, apply the P3 rule. If blocking findings remain, complete the
resulting action and re-run; that re-run completes cycle 3. If only [P3] or no
findings remain, use step 1's clean branch.

### 3. Judge the accumulated set below the cap

Judge all rounds together, not only the newest; the history is a dataset, not a
news feed. New surface each round is necessary but not sufficient:

- **Scattered:** no shared root → use the ordinary class path.
- **Drift:** re-litigation or trivial/style nits; no additional below-cap
  transition is specified.
- **Shared root:** surface-different findings violate one invariant → use the
  root-attack path.

### 4. Sweep every blocking class, then re-run

For each [P0]/[P1]/[P2] class:

1. **Name it** — for example, "stale command," "`cd` that strands the shell," or
   "unqualified threshold claim."
2. **Enumerate it across the branch** — grep for the pattern and run each
   executable documentation claim.
3. **Fix every member before re-running.**

This applies `sweeping-stale-references` and `adversarial-review`'s "Enumerate every
class" to findings. Keep a proven one-member class bounded. A recurring class below
the cap proves the prior sweep incomplete; sweep it fully rather than fixing one
more instance. Address a different blocking class by its own class—difference is
not a dismissal or deferral lever.

Re-run the same reviewer against the new HEAD. The upstream per-task skill still
chooses its reviewer under its own rules.

### 5. Attack a visible shared root below the cap

Attack one axis visible across rounds without waiting for cycle 3; never infer an
axis from one isolated finding. When two cycles are complete, step 2's verdict
comes first.

1. **Name the axis.**
2. **Enumerate every site that could violate the invariant project-wide, across all
   code paths and languages, including uncited and unreviewed locations.** Use a
   ready checklist if one fits, such as `adversarial-review`'s `durability` angle.
3. **Fix the whole axis in one pass, then re-run.**

One invariant whose closure removes the class is a root; a shared topic is not.
SQL injection and an N+1 query both touch a database but violate different
invariants, so they remain scattered.

### 6. Take the cold-read escape

Start or dispatch a fresh review with no conversation memory, using a subagent, another model, another human, or a clean new session.

| Cold-read outcome | Transition |
|---|---|
| Confirms findings | Consider redo, not another ordinary iteration. |
| Diverges materially | Trust the cold read and stop. Remain blocked if it has any P0–P2; declare clean only if it has none. |
| Confirms fix-forward | Continue only if productive. Reset the cap for at most three more cycles, and require another escape if blocking findings persist. |

Record the escape and verdict in a work artifact—plan, spec, PR, review thread, or, for design rationale, a code comment at the decision site—so the next reader sees why iteration stopped.
No owner or criteria for `consider redo` or `productive` is specified.

## Required records

| Predicate | Record |
|---|---|
| Upstream task round completes | Truthful completed-round record in that task workflow. |
| Cycle-3 entry | All-round pattern verdict in the loop work artifact; include the written reviewer ruling when that branch applies. |
| P3 is not acted on | On-page defer/dismiss rationale. |
| Cold-read escape | Escape and verdict in a work artifact. |

This skill names no separate durable artifact for an ordinary class inventory, ordinary review result, or the independent whole-branch counter.

## Rationalizations

| Excuse | Reality |
|---|---|
| "We did a cold read, this must be drift now." | Cycle count is not the criterion. Apply scattered / drift / shared-root to the accumulated set in each cycle. |
| "The reviewer reported one finding, so there is one thing to fix." | It sampled one possible class member. Enumerate the class; keep a proven one-member class bounded. |
| "Each round found a new nit, so iteration is productive." | Recurrence of one class is drift in a productivity mask. Complete the sweep. |
| "I cannot declare clean from my fix, so I will re-run now." | Re-run only after completing the class-sweep; a one-instance fix burns the round. |
| "New surface permits one more sweep past the cap." | At the cap, escape is mandatory; sweeping and root attack are below-cap moves. |
| "Every finding is new and real, so keep going." | New, real findings can share one unexamined invariant. Audit the axis instead of fixing the next symptom. |
| "Different files and symptoms mean the findings are unrelated." | Test whether one invariant spans the artifact, your governing text, or the reviewer before calling them scattered. |
| "The reviewer will confirm green next round." | It will keep probing an open axis until the whole axis is closed. |
| "Auditing the root is slower than fixing this finding." | Once two rounds share a root, one whole-axis audit replaces many reactive rounds. |
| "Both findings touch the database, parser, or input, so that is the axis." | A shared topic is not a root. Different invariants remain scattered. |
| "I closed the axis in the reviewed file." | Audit the invariant project-wide across every path, not only the reviewed location. |
| "The third cycle's re-run found a new shared root, so I will attack it now." | That re-run is the cap. Escape; there is no fourth in-context root attack. |
| "The prior rounds are already in my context." | Context is not analysis. Write the verdict over the full set. |
| "Fix this round first and step back afterward." | Cycle-3 entry gates every fix. Write the verdict first. |
