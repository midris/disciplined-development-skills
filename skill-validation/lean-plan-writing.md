# lean-plan-writing — validation

RED/GREEN evidence for `lean-plan-writing` rule changes. Composes with
`superpowers:writing-plans`; owns the prose-is-the-contract density rule + the
test-table substitute. Prior rules predate this record; entries below cover
validated changes.

**Dispatch protocol.** Read-only, bounded per CLAUDE.md's evaluation-subagent rule.
Plan-author subagents return a plan as text (no writes); sonnet arm — opus is the
real runtime and strictly stronger, so a non-reproducing RED on sonnet holds
*a fortiori*.

## Name the unexercised cases (added 2026-06-30)

Folded into the Per-artifact **Plans** bullet: "Before calling a plan ready, name
each task's unhandled inputs (absent, malformed, out-of-scale) and the invariants
it silently relies on — then pin the behavior or mark it an accepted edge."
Author-side mirror of `adversarial-review`'s `Generate the unexercised cases`
baseline rule (B18) — author generates the cases before review; reviewer catches
what's left. Backlog B20; source = the B18 plan's author-side-mirror follow-up
(speculative symmetry, **not** an observed failure).

**RED — premise did not reproduce.** Iron-Law control = the current skill (this is
an edit). Two scenario shapes, 5 fresh authors each (sonnet), guidance inlined:

- *Edge-loud* (bulk CSV import, untrusted upload): 5/5 enumerated all four faces
  (absent / malformed / out-of-scale / tacit-invariant) AND dispositioned each
  (pinned test/step, or Non-Goals/accepted-edge with rationale); two went
  correct-by-construction (unique index + `ON CONFLICT`).
- *Edge-quiet* (nightly digest job — silent cases are idempotency / partial-failure /
  rate-limits / timezone): 5/5 made idempotency + partial-failure isolation the
  centerpiece with explicit dispositions. The one uniformly-skipped face —
  validating a *trusted internal* service's non-throwing payload — is correct trust
  calibration (same authors validated the untrusted CSV exhaustively), not omission.

10/10 produced the discipline's substance unprompted → no RED → by the Iron Law no
edit is warranted. Shipped anyway as an **owner's-call reinforcement**.

**GREEN — a measured, placement-insensitive effect.** Tested at two placements — a
standalone `## Name the unexercised cases` heading, and the shipped form folded into
the Per-artifact Plans bullet — digest scenario, 5 reps each vs the 5 control:

| Signal | Control | GREEN-titled | GREEN-folded (shipped) |
|---|:-:|:-:|:-:|
| Dedicated edge-case section (collected + labeled, dispositioned) | 0/5 | 5/5 | 5/5 |
| Reached the malformed-payload boundary | 0/5 | 4/5 | 5/5 |
| Quiet invariants (idempotency / overlap / failure-isolation) | 5/5 | 5/5 | 5/5 |

The effect is **line-wording-driven, not heading-driven**: with the heading removed,
authors still lifted the line's own vocabulary into self-chosen section titles (one
titled its section verbatim "Unhandled inputs, invariants, and accepted edges").
Control already handled the *substance* (10/10 above); the line's delta is (a)
collecting the edges into an explicit labeled section — a modest auditability gain
over control's inline "Design decisions" dispositions — and (b) reaching the one
boundary control trusts. That malformed reach is double-edged (the internal analytics
client is a trusted boundary) but lands as cheap, sane hygiene in all 5 (drop/bucket a
bad event, don't throw; one logs it as an "unexpected API contract violation"), not
heavyweight validation. No degradation in any rep. GREEN was run on the edge-quiet
digest scenario only; the edge-loud CSV scenario was RED-only.

**Verdict.** No RED gap — the substance is already emergent from `writing-plans` +
`lean-plan-writing`. The line is a placement-insensitive **polish**: it makes the
unexercised cases explicit (labeled section, 5/5) and modestly widens boundary
coverage (5/5), harmlessly. Shipped folded into the Per-artifact Plans bullet (leanest
placement with the full effect). Kept on owner judgment.

## On edits

- Changing the line: re-run the two-scenario author RED (edge-loud + edge-quiet, ≥5
  reps, current-skill control). Ship a wording only if it beats the control; absent a
  reproducing gap, record as owner's-call with the observed GREEN effect. Placement
  (titled vs folded) did not change the effect — the line's wording carries it. Sonnet
  suffices (opus runtime is stronger).
- New density/structure rule: watched RED first, per `superpowers:writing-skills`.
