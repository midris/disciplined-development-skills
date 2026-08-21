---
name: disciplined-development
description: 'Use when doing development work, including starting or resuming work; writing or reviewing code, plans, specs, designs, or docs; researching project or external facts; fixing bugs or findings; active-plan work; delegation; and verification, commit, review, PR, or completion boundaries.'
---

# Disciplined Development

**Role:** Orchestrator for development sessions.
**Owns:** the Iron Law; selection and acceptance of the five gates and eight principles; their artifacts, blocks, and authority; and the checkpoint ledger.
**Companions own:** discovery and procedure at their routed boundaries.
Invoke every `REQUIRED SUB-SKILL` for an active gate or principle, using a locator that resolves in the current environment, even when the child determines that no further action is due.

## The Iron Law

```
NO PROGRESS PAST A GATE WITHOUT THE ARTIFACT IT REQUIRES
```

Each gate is fail-closed: its written, conversational, or running-system artifact must exist before the blocked transition proceeds.
Size, effort, urgency, and apparent simplicity create no exemption.

## Five operational gates

### Gate 1 — Read before writing

At session start, a phase change, or a governing-artifact change, first freshly open every supplied applicable governing, task, and external source before producing or updating the next-phase artifact or taking the next-phase action.
Reading the result after writing it does not count, and memory from an earlier session is not a source.
This applies to planned work, ad-hoc changes, fixes, docs edits, and reviews given or received.
Apply Principle 6 to every factual claim or relied-on premise.
Surface unresolved source ambiguity to the governing source or decision owner; planning and later gates remain blocked until that owner resolves it.
If no source applies, say so before proceeding.

### Gate 2 — Translate to written before coding

Before implementation planning, development delegation, or coding, the governing source or decision owner must settle scope and design and sign off complete written scope.
The artifact records every applicable requirement and constraint, each accepted edge, and every intentional deferral's reason and operational consequence.
Apply Principle 7's evidence threshold; do not broaden scope beyond evidence-required consequences.
Extract visible mockup strings into the plan.
Plan review ends with the written diff signed off on the document.
Implementation planning, development delegation, and coding remain blocked while scope/design is unsettled, the artifact is incomplete, a deferral lacks either required part, or sign-off is absent.

**REQUIRED SUB-SKILL while scope or design is unsettled:** `superpowers:brainstorming`.
**REQUIRED SUB-SKILLS when the deliverable is a plan or spec:** `superpowers:writing-plans` + `lean-plan-writing`.

### Gate 3 — Verify against the running system before claiming done

Obtain fresh direct evidence appropriate to the affected interface, such as a screenshot or DOM snapshot for UI, a live HTTP response for an API, or an actual CLI invocation.
Passing tests alone is insufficient.
Paste the evidence in chat; completion remains blocked until it exists.

**REQUIRED SUB-SKILL:** `superpowers:verification-before-completion`.

### Gate 4 — Accept scope, sweep references, then commit

First inspect returned work against signed scope.
Do not provisionally verify, reconcile, accept, or commit an unauthorized returned change.
Reject and remove it, or stop for decision-owner Gate 2 resolution and signed revised scope before any remediation or positive-path action involving it.
When the checkpoint identifies a specific unauthorized change, name it and choose one disposition explicitly before checking other candidate evidence.

After the candidate conforms, complete the remaining Gate 4 steps before moving to any later gate:

1. Obtain the required Gate 3 evidence.
2. Invoke `sweeping-stale-references` and reconcile applicable references.
3. Retain its truthful child-owned `References swept:` artifact.
4. Prepare one coherent commit.

For a behavior change, that one coherent green `feat:` or `fix:` commit contains the regression test, implementation, and reconciled references.
Gate 4 remains blocked until all four steps are complete.
At a checkpoint involving unauthorized work, the checkpoint artifact must include both:

- the chosen disposition; and
- the complete conforming-candidate continuation through steps 1–4.

Stopping after rejection or remediation, or omitting the durable `References swept:` artifact, is incomplete.

**REQUIRED SUB-SKILL:** `sweeping-stale-references`.

### Gate 5 — Whole-repository review and smoke before PR

The orchestrator owns this pre-PR sequence and records one completion/acceptance path in the Gate 2 artifact:

1. Freshly reread every supplied applicable source, including the Gate 2 artifact, active plan, governing files, and linked specs.
2. Self-review the whole repository against them; remediate and re-review until PASS.
3. After self-review passes, obtain a fresh external review over the same whole-repository scope; remediate and rerun it until PASS.
4. After external review passes, smoke affected flows and record the exact successful commands and results.
5. Invoke `superpowers:finishing-a-development-branch`.
6. Only then open the PR.

For this parent gate, PR creation waits for invocation—not completion—of branch finishing.

For either review, PASS means zero `[P0]`/`[P1]`/`[P2]`; `[P3]` is advisory and nonblocking, with disposition owned by `adversarial-review-loop`.
A failed or unresolved smoke result does not pass.
Remediation invalidates affected later review or smoke evidence and restarts the sequence at the earliest affected stage.
At this checkpoint, whole-repository self-review must first discover and record an outside-diff discrepancy before scope resolution or remediation, even when the checkpoint context already flags it.
For a finding requiring code change, restart at signed Gate 2 scope when scope changes, then expected RED, code remediation, Gate 3 evidence, Gate 4 reconciliation/green commit, and Gate 5 again.
The parent coordinates the restart and retains every gate.
Every executable restart record names the applicable remediation-method owner as the fixer; reviewers emit only findings and verdicts.
A standalone or periodic whole-repository review is not Gate 5 unless it is this pre-PR checkpoint.

Only the orchestrator or user accepts gate passage, performs smoke, invokes branch finishing, or opens the PR.
A development subagent may implement bounded remediation under Principle 4, but it reports any due parent gate and stops.
`adversarial-review-loop` owns cadence and whole-repository remediation; the active execution skill owns per-task review remediation; the reviewer owns neither.

**REQUIRED SUB-SKILLS:** `superpowers:requesting-code-review` + `adversarial-review` + `adversarial-review-loop`.
**REQUIRED SUB-SKILL before opening the PR:** `superpowers:finishing-a-development-branch`.

## Eight principles

### 1. Write it down, don't remember it

Record agreed requirements, scope, design decisions, plan changes, completion, and acceptance in the durable project file.
Flip an active-plan task checkbox in the same commit that completes the task.
When the record includes an intentional descope, deferral, shortcut, exception, or choice over a defensible alternative, use `writing-explicit-rationale` to decide whether durable rationale is needed and where it belongs.

**REQUIRED SUB-SKILL:** `writing-explicit-rationale`.

### 2. Re-read, don't recall

At every Gate 1 lifecycle trigger, open the actual files relevant to the next action; the Gate 1 block applies until then.

### 3. Obey what's written; surface what isn't

Follow clear governing text.
Surface unclear or conflicting meaning to the user or decision owner; interpretation, technical evaluation, remediation, and implementation remain blocked until that owner resolves it.
Approval of one decision does not authorize adjacent changes.
For scope-ambiguous prompts such as “our X” versus “X in general,” surface the ambiguity or check both meanings; never choose silently.

### 4. Carry the discipline into development-subagent dispatches

The parent decides whether and what bounded work to delegate and selects model capability based on task complexity.
For every development-subagent dispatch, invoke `dispatching-development-subagents` through an executable locator and follow its dispatch, scope, handoff, and verification method; merely naming or summarizing the child is insufficient.
The orchestrator retains every parent gate and acceptance decision and inspects the actual returned diff against signed scope before accepting it.
A development subagent implements assigned work; when a parent gate is due, it reports that gate to the orchestrator and stops.

**REQUIRED SUB-SKILL:** `dispatching-development-subagents`.

### 5. Test first for behavior changes

Production behavior editing remains blocked until a regression test has been written, run, and observed failing for the expected missing behavior.
The test and implementation land together in the Gate 4 green `feat:` or `fix:` commit.
Only the user's explicit approval permits these exceptions: throwaway prototypes, generated code, or static configuration values—not schema or behavior changes.

**REQUIRED SUB-SKILL:** `superpowers:test-driven-development`.

### 6. Ground every factual claim and disclose its support

Before any factual claim or premise is stated, repeated, transformed, or relied on in any response, interaction, action, or task, select this principle and keep every dependent transition blocked.
Every claim must be verified from the best applicable source and support-mapped in the accompanying response or durable record.
Every checkpoint that selects Principle 6 records both ownership seams: parent—selection and dependent block; `disciplined-research`—the complete source-work bundle (source selection/ranking, acquisition, verification, support disclosure).
An omitted or partial seam is incomplete.

**REQUIRED SUB-SKILL:** `disciplined-research`.

### 7. Add complexity only when evidence demands it

Generate absent, malformed, and out-of-scale cases during analysis.
Implement only cases required by contract, reachable from accepted input, observed in use, or necessary to make an invariant robust; record the rest as accepted edges.
A fragile or unstated invariant is not a deferrable edge: fix it by construction.
Choose the smallest sufficient action, avoid speculative configuration or abstraction, and remove layers when iteration keeps surfacing findings.
The reviewer-side counterpart lives in `adversarial-review`.

### 8. Review periodically and catch problems early

Run adversarial review at chunk boundaries and after roughly 5 commits or 200 net lines since the last clean review.
Follow stricter local automation; otherwise self-trigger.
A development subagent never performs or gathers this review; it reports the due gate to the orchestrator and stops.
`adversarial-review-loop` owns cadence and whole-repository remediation, while the active execution skill owns per-task review remediation.
Prior per-task rounds do not seed the whole-repository counter; if its third completed cycle remains blocking, take its child-owned cold-read escape rather than the per-task breaker.

**REQUIRED SUB-SKILLS:** `superpowers:requesting-code-review` + `adversarial-review` + `adversarial-review-loop`.

## Route each checkpoint

Classify each independent item in this ledger:

| Independent item | Mode/checkpoint | Status | Due gates/principles | Artifact | Destination | Blocked transition | Owner |
|---|---|---|---|---|---|---|---|

Use **Selected** when due, **Blocked** when a prerequisite is missing, **Satisfied** when its artifact is accepted, and **Retained** when existing evidence still binds.
Mode cues nominate candidates; section predicates decide what is due now, and later gates are not due.
Every Selected row carries the section's artifact, destination, blocked transition, and owner.

| Observable state | Select now |
|---|---|
| Sources for the next action are unread | Gate 1; block that action. |
| Session, phase, or governing-artifact boundary | Principle 2 until relevant files are open. |
| Creating or updating a requirement, scope, decision, rationale, plan change, completion, or acceptance record | Principle 1 until recorded. |
| A factual claim or premise will be stated, repeated, transformed, or relied on | Principle 6 until the complete support-mapped outcome exists. |
| Governing meaning is unresolved | Principle 3; block interpretation, technical evaluation, remediation, and implementation through owner resolution. |
| Governing meaning is clear but a design choice is unresolved | Do not select Principle 3; surface options and keep Gate 2 Blocked. |
| An implementation item lacks settled, signed scope | Gate 2 for that item: Blocked until settled, then Selected until the signed artifact exists. |
| An established behavior change reaches its pre-edit boundary | Principle 5 until expected RED; planned, conditional, or unsettled work does not select it. |
| Deciding how an actual requirement, edge, or complexity affects work | Principle 7 until its evidence-based consequence is recorded. |
| Review cadence or the pre-PR checkpoint | Principle 8; select Gate 5 only for the pre-PR checkpoint. |

| Mode | Positive checkpoint cues |
|---|---|
| Brainstorming | Gate 1 and Principles 1/2/6/7; evidence-ground options without selecting for the owner; Gate 2 per settled item; block implementation planning and coding until owner selection and signed scope. |
| Plan writing | Gates 1–2 and Principles 1/2/6/7; reread requirements, evidence-ground scope, record accepted edges, and obtain sign-off; block implementation planning, coding, and development delegation until the complete plan diff is signed. |
| Implementation (sequential) | Gates 1–5 and Principles 1/2/5/6/7/8 at their predicates. |
| Implementation (parallel, independent only) | Sequential cues plus Principle 4 per bounded dispatch; block each item's implementation planning, dispatch, and coding until its sources are reread and its decision is settled in signed scope. |
| Debugging | Gate 1 contract reread; Gate 2 written fix scope blocks implementation planning; expected RED additionally blocks editing; Gates 3–4 follow; Principles 1/2/5/6. |
| Code review (giving) | Gate 1 and Principles 2/3/6/7; reject or remove complexity unsupported by Principle 7; Principle 8 only at its predicate; preserve reviewer, remediation, and gate-acceptance owners. |
| Code review (receiving) | Gate 1 and Principles 2/3/6; unresolved governing meaning blocks interpretation or technical action through owner resolution. |
| Documentation or specification work | Nominate lifecycle candidates in order: Gate 1; for a plan/spec deliverable, Gate 2 and the plan/spec children; Gate 4 at the pre-commit boundary. For a plain doc edit, omit Gate 2 and the plan/spec children unless implementation scope is also being created, leaving Gate 1 then Gate 4 as candidates. Select each gate and child only at its section predicate. Both branches nominate Principles 1/2/3/6/7 and limit edits to evidence-required consequences before reconciliation and commit. |

## Prose route

For reader-facing prose in project files or durable project records, invoke `concise-writing` and leave its method child-owned.
For response-only prose, invoke it unless the user explicitly requests that the response itself be a detailed explanation.

**REQUIRED SUB-SKILL at either active prose boundary:** `concise-writing`.

## Common rationalizations

| Excuse | Required response |
|---|---|
| “I read it last session.” | Freshly reopen the applicable sources at Gate 1. |
| “This is too small or urgent for the full process.” | Select every predicate that applies; size and urgency do not release a block. |
| “The requirement is clear, so it is already in scope.” | Clear governing meaning still needs decision-owner Gate 2 scope before coding when it is outside signed scope. |
| “Tests pass, so verification is done.” | Tests do not replace Gate 3 direct evidence. |
| “A separate red test commit proves test-first.” | Observe expected RED before editing, then land test and implementation together in the green behavior commit. |
| “The final external review can replace self-review.” | Gate 5 requires both reviews in order. |
| “Every edge must be implemented.” | Apply Principle 7's contract, reachability, observation, and robust-invariant threshold; record the rest as accepted edges. |
| “The input cannot happen because current callers avoid it.” | Determine whether it is reachable accepted input or exposes a demonstrably fragile invariant. Fix it by construction only in those cases; otherwise apply Principle 7's full threshold and record the accepted edge. |
| “One more layer is safer.” | Added surface needs evidence; choose the smallest sufficient action. |
