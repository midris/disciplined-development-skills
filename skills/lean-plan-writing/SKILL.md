---
name: lean-plan-writing
description: Use with `superpowers:writing-plans` whenever the deliverable is a plan or spec — new plans, plan edits, spec drafts, spec amendments. Triggered by "write a plan for X", "draft a spec", "update the plan", "edit the design doc", "add a task to the plan".
---

# Lean plan writing

**Role:** Refinement layer for software-development plans and specs.
**Required composition:** Always invoke `superpowers:writing-plans`.
**Owns:** the prose-density contract, the bounded illustrative-snippet exception, the test-table substitute for tricky logic, and qualitative merge boundaries.
**Does not own:** upstream headers, files-touched inventories, step decomposition, no-placeholder rules, TDD ordering, or commit cadence.
`writing-explicit-rationale` owns whether a plan or spec choice needs durable rationale.

## Prose is the contract

`superpowers:writing-plans` says to show code when a step changes code.
For software-development plans and specs, this skill overrides only that rule: **prose is the contract; code is the implementer's job**.
Keep the upstream scaffold and rigor, but write concise requirements, order of operations, and status rather than the implementation.

For every plan step:

- Describe the change, required behavior, and test behaviors in concrete prose.
- Do not embed implementation code, test bodies, or copyable templates; the single bounded illustration below is the only exception.
- Use the formats below when ordinary prose is not precise enough.

| Content | Put in the plan or spec |
|---|---|
| Change | What changes and the behavior it must produce |
| Tests | Behaviors that must pass, not test bodies |
| Fixtures | Shape and meaningful values, not literal JSON |
| Migration | Structural before/after state, not a code diff |
| API | Field names, types, and semantics, not full JSON examples |
| Commit | A concise message as text, not a shell command |

## Tricky logic and exact shapes

For gnarly logic such as a multi-arm regex, recursive CTE, or complex transform, replace embedded code with a denser test contract: an `(input → expected output)` table that pins every edge case.
The table specifies the behavior; the implementer writes the implementation against it with running tests as feedback.

If prose cannot specify an exact requirement without genuine ambiguity, include exactly one illustrative snippet of at most five lines.
Do not repeat that snippet's literal content anywhere else in the plan.

## Plans and specs

- **Specs** carry detailed requirements, design rationale, and open questions; emphasize why.
- **Plans** carry order of operations, per-step scope, dependency order, and status checkboxes; emphasize execution order.
  Before calling a plan ready, name each task's silent invariants and, when it consumes inputs, its unhandled absent, malformed, and out-of-scale cases; then pin the behavior or mark it as an accepted edge.

Both use prose as the contract.

## Merge boundaries

Declare a qualitative branch and PR sequence.
Give each independently green and reviewable unit its own branch and PR in dependency order, small enough for one review pass.
Keep a tightly coupled change in one atomic PR when no smaller boundary can remain green and internally consistent.
Do not use commit counts or diff size as the boundary rule.

## Rationalizations

| Excuse | Reality |
|---|---|
| "`writing-plans` says show the code." | This skill overrides that rule only; retain the upstream scaffold and express implementation requirements in prose. |
| "The implementer is new, or this is greenfield, so they need a code pattern." | Explain the concept and cite an existing analogue or external documentation; do not embed a template they can copy. |
| "This regex, migration, or heredoc needs exact code." | Specify logic with a complete test table. Use the bounded snippet only when an exact artifact shape remains ambiguous. |
| "Without code the plan is vague or contains TBDs." | Concrete behavior, test cases, edge dispositions, and dependencies are rigorous prose; placeholders are not. |
| "The user requested an extremely detailed plan." | Detail means complete requirements, dependencies, edge behavior, and necessary rationale—not embedded implementation. |
| "The implementer can just copy the plan code, so writing it twice is wasteful." | Plan code lacks execution feedback and turns assumptions into copyable bugs; implementation belongs with running tests. |
