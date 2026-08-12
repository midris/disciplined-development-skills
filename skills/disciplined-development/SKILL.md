---
name: disciplined-development
description: 'Use when doing development work, including starting or resuming work; writing or reviewing code, plans, specs, designs, or docs; researching project or external facts; fixing bugs or findings; active-plan work; delegation; and verification, commit, review, PR, or completion boundaries.'
---

# Disciplined Development

**Role:** Orchestrator — parent skill governing development sessions and invoking companion skills at their owning gates and principles.
**Owns:** the Iron Law, the five gates, the principles, and the checkpoint-selection routing table.
**Companions own:** their discovery and procedure.
At each active gate or principle, require its artifact or outcome, preserve its owner and any blocked transition, and invoke its required skills for procedure.
Load every `REQUIRED SUB-SKILL` named by an active gate or principle, even when it has no action to take.

## Overview

Written records govern a project.
Memory of those records erodes with time and momentum.
This skill is an acknowledgement of that erosion and a guard against it.

**Core principle:** the file wins.
Write it down before you forget; re-read it before you act; produce evidence before you claim done.
**Gates** force specific actions at decision boundaries.
**Principles** are the rules they enforce.
No discipline is skippable on grounds of size, effort, or impact.

## The Iron Law

```
NO PROGRESS PAST A GATE WITHOUT THE ARTIFACT IT REQUIRES
```

Each gate is fail-closed.
The artifact must exist — in writing, in chat, or in the running system — before the next action.

## Operational gates

**Gate 1 — Read before writing.**
Re-read every applicable source.
This applies to all development work, including planned work, ad-hoc changes, bug fixes, docs edits, and code reviews (giving or receiving).
"Last session" doesn't count; memory isn't a source.

Sources may include:

- **Governing documents:** CLAUDE.md / AGENTS.md / CONTRIBUTING.md, ARCHITECTURE, and project memory.
- **Task sources:** the active plan, linked specs/mockups/designs, design principles, API docs, and schemas.
- **External sources:** library documentation, version information, and evidence of API behavior.

Apply Principle 6 before stating any factual claim.
Unresolved source ambiguity blocks planning and later gates until it is surfaced and the governing source or decision owner resolves it.
If no source applies, say so before proceeding.

**Gate 2 — Translate to written before coding.**
Before implementation planning or coding, settle scope or design through a governing source or decision owner, then capture every applicable requirement and constraint in written scope.
Extract visible mockup strings into the plan.
Plan review ends with a written diff signed off on the document.
**REQUIRED SUB-SKILL when scope or design is unsettled:** `superpowers:brainstorming`.
**REQUIRED SUB-SKILLS for plans and specs:** `superpowers:writing-plans` + `lean-plan-writing`.

**Gate 3 — Verify against the running system before claiming done.** Use direct evidence appropriate to the affected interface—for example, a screenshot or DOM snapshot for UI, a live HTTP response for an API, or an actual invocation for a CLI.
Tests passing is necessary but not sufficient — mocks lie about live shapes.
Paste evidence in chat.
REQUIRED SUB-SKILL: `superpowers:verification-before-completion`.

**Gate 4 — Accept scope, then sweep stale references before commit.**
First confirm returned work conforms to signed scope.
Reject and remove unauthorized work, or stop for decision-owner Gate 2 resolution and signed revised scope before remediation, verification, reconciliation, acceptance, or commit involving it.
For each accepted load-bearing fact (code symbol, doc claim, schema, spec constraint), run an effective reference sweep across every relevant repository surface and reconcile all encodings in one commit.
In the commit body, record a concise, truthful `References swept:` summary of the surfaces checked and their disposition.
REQUIRED SUB-SKILL: `sweeping-stale-references`.

**Gate 5 — Whole-repository review and smoke before PR.**
The orchestrator owns this fail-closed sequence.
For either review, `DD-VERDICT: PASS` means zero `[P0]`/`[P1]`/`[P2]`; `[P3]` is advisory.

1. **Self-review** — Re-read the Gate 2 artifact, active plan, governing files, and linked specs. Review the whole repository against them; remediate through `adversarial-review-loop` and re-review until PASS.
2. **External review** — After self-review passes, obtain a fresh review over the same whole-repository scope; remediate through `adversarial-review-loop` and rerun the external review until PASS.
3. **Smoke pass** — After external review passes, smoke affected flows and record the exact commands and results in the Gate 2 artifact.

All three must pass before branch finishing; PR creation then waits for the orchestrator or user to invoke `superpowers:finishing-a-development-branch`.
Reviewers emit review verdicts; only the orchestrator or user accepts gate passage, performs the smoke pass, invokes branch finishing, or opens the PR.

A development subagent may implement only bounded remediation under Principle 4.
It may not run or gather either review, accept gate passage, perform the smoke pass, invoke branch finishing, or open the PR.
It reports any due gate action and stops.

`adversarial-review-loop` owns Gate 5 remediation; the applicable execution skill owns per-task review loops.

REQUIRED SUB-SKILLS: `superpowers:requesting-code-review` + `adversarial-review` + `adversarial-review-loop`.
REQUIRED SUB-SKILL before opening PR: `superpowers:finishing-a-development-branch`.

## Principles

**1. Write it down, don't remember it.**
Verbal scope, design decisions, requirements, and plan changes go into a file the moment they're agreed.
Conversation is not a contract; the file is.

Flip task checkboxes in active plans in the same commit where the task is completed.

When the write-down includes an intentional descope, deferral, shortcut, exception, or design choice over a defensible alternative, any necessary rationale belongs on-page too — not only in chat.
Use `writing-explicit-rationale` to determine what, if anything, needs to be written down.
REQUIRED SUB-SKILL: `writing-explicit-rationale`.

**2. Re-read, don't recall.**
At session start and whenever work changes phase or governing artifact, open the actual files relevant to the next action.
Plans drift; context decays.

**3. Obey what's written; surface what isn't.**
If a guideline says "do X," do X.
Don't decide this case is the exception.
Violating the letter is violating the spirit.
Surface unclear or conflicting guidance to the user — do not silently resolve.
Approval of one decision does not authorize adjacent changes.
Includes scope-ambiguous prompts: "our X" vs "X in general" — flag it or check both, don't pick silently.

**4. Carry the discipline into subagent dispatches.**
Subagents don't auto-load skills.
Every dispatch prompt contains this reload contract:
- **Parent:** Load `disciplined-development` before work; if direct skill loading is unavailable, read `.claude/skills/disciplined-development/SKILL.md` first and follow it as binding guidance.
- **Governing sources:** Name the files and require the subagent to re-read them before acting and again before reporting completion.

Gate summaries do not substitute for loading the skill.
Pick the model based on task complexity.
Dispatch a crisp scope contract.
When work returns, inspect the actual diff against that contract — the report is not the diff.
Complete the active execution skill's task-review loop at its governing boundary before accepting the work.

Principle 8 and Gate 5 are for the orchestrator, not the subagent.
Tell the subagent not to dispatch its own subagents or act on hook nudges (review / checkpoint / PR); it reports a due gate and stops.

REQUIRED SUB-SKILL: `dispatching-development-subagents`.

**5. Test-first for behavior changes — TDD non-negotiable.**
Production behavior editing remains blocked until a test has been written, run, and observed failing for the expected missing behavior.
The test and implementation land together in one green `feat:` or `fix:` commit.
Exceptions require user approval: throwaway prototypes, generated code, and static configuration values—not schema or behavior changes.

REQUIRED SUB-SKILL: `superpowers:test-driven-development`.

**6. Ground every factual claim before stating it, and disclose its support.**
**Required artifact content:** Every factual claim is supported as written; the artifact itself maps each claim unambiguously to that support.
Apply `disciplined-research` in full; merely loading or naming it is not enough.
REQUIRED SUB-SKILL: `disciplined-research`.

**7. Keep it simple — add complexity only when evidence demands it.**
- Build to satisfy the requirement. Don't over-engineer.
- Don't build for hypothetical futures. Don't prematurely optimize. Don't prematurely abstract (rule of three).
- Generate absent, malformed, and out-of-scale cases during analysis, but implement only those required by contract, reachable from accepted input, observed in use, or necessary to make an invariant robust; record the rest as accepted edges.
- A fragile or unstated invariant is not a deferrable edge case. Fix it by construction — that's the simpler design.
- When iteration keeps surfacing new findings, remove layers — don't add more.

Reviewer-side counterpart lives in `adversarial-review`.

**8. Review periodically and catch problems early.**
Run adversarial review at chunk boundaries and after roughly 5 commits or 200 net lines since the last clean review.
If local automation sets a stricter cadence, follow it; otherwise self-trigger.
A dispatched subagent never runs this review itself — not even to gather findings.
It reports that review is due and stops; a hook nudge or a hit cadence threshold doesn't change that.
Cadence and whole-branch review remediation use `adversarial-review-loop`.
Per-task review during a plan-execution workflow uses that execution skill's own remediation loop.
REQUIRED SUB-SKILLS: `superpowers:requesting-code-review` + `adversarial-review` + `adversarial-review-loop`.

## Select gates and principles at each checkpoint

Classify each independent item in this ledger:

| Independent item | Mode/checkpoint | Status | Due gates/principles | Artifact | Destination | Blocked transition | Owner |
|---|---|---|---|---|---|---|---|

Status: **Selected** due; **Blocked** by prerequisite; **Satisfied** accepted artifact exists; **Retained** evidence binds.

Mode cues nominate candidates; select only through matching predicate/section triggers, never re-adding conditional items:

| Observable state | Classification |
|---|---|
| Sources for the next action are unread | Gate 1 is Selected; that action is Blocked. |
| Session start, phase change, or governing-artifact change | Principle 2 is Selected until files are opened. |
| Creating/updating a requirement, scope, decision, rationale, plan-change, completion, or acceptance record | Principle 1 is Selected until recorded. |
| The current artifact states a factual claim | Principle 6 is Selected for that current artifact until claims map to support. |
| Unresolved governing meaning | Principle 3 is Selected; surface the conflict; interpretation, technical evaluation, remediation, and implementation are Blocked until the decision owner resolves the meaning. |
| Clear governing meaning; unresolved design choice | Principle 3 is not Selected; surface options to owner; Gate 2 stays Blocked. |
| An independent implementation item lacks settled, signed scope | Gate 2 is classified for each independent implementation item: Selected after its choice settles, otherwise Blocked. |
| An established behavior change reaches its pre-edit boundary | Principle 5 is Selected until expected RED; planned, conditional, or unsettled work does not select it. |
| Deciding how an actual requirement, edge, or added complexity affects work | Principle 7 is Selected until its evidence-based consequence is recorded. |
| Review cadence or a Gate 5 checkpoint | Principle 8 is Selected only at that predicate. |

| Mode | Positive checkpoint cues |
|---|---|
| Brainstorming | Gate 1; Principles 1/2/6/7; evidence-grounded options; decision owner selects; Gate 2 per settled item. |
| Plan writing | Gates 1–2; Principles 1/2/6/7 through signed scope. |
| Implementation (sequential) | Gates 1–5; Principles 1/2/5/6/7/8 at predicates. |
| Implementation (parallel, independent only) | Sequential cues; Principle 4 per bounded dispatch. |
| Debugging | Gate 1 contract reread and Gate 2 written fix scope block implementation planning; observed RED additionally blocks editing; Gates 3–4 follow their sections; Principles 1/2/5/6. |
| Code review (giving) | Gate 1; Principles 2/3/6/7; Principle 8 only by its predicate. |
| Code review (receiving) | Gate 1; Principles 2/3/6; unresolved governing meaning blocks action through owner resolution. |
| Documentation or specification work | Gates 1/4; Principles 1/2/3/6 and Principle 7 for evidence-required consequences. |

Each Selected row names its section-defined artifact, destination, owner, and Blocked transition; later gates are not due.
For Principle 4, the orchestrator selects model capability, scopes each dispatch, verifies returned work, retains parent gates, and controls delegation; a bounded subagent implements assigned work, reports a due parent gate and stops.
At a Gate 5 checkpoint, select Gate 5 and Principles 1, 2, 6, and 8.
Its Gate 2 destination owns one completion/acceptance record ordered self-review → external review → smoke → branch finishing/PR.
Each review passes at zero P0/P1/P2; P3 is advisory; the remediation-method owner resolves findings.
Reviewers emit verdicts; only the orchestrator or user accepts gate passage, performs smoke, invokes branch finishing, or opens the PR; PR stays Blocked until finishing.

## Common parent rationalizations

| Excuse | Reality |
|--------|---------|
| "I read it / wrote it / searched it last session." | Cross-session memory is stale. Re-read. |
| "Last N tasks went fine." | Survivorship reasoning. Re-read anyway. |
| "I'll remember to do X later." | Write it now. Memory rationalizes. |
| "This case is different / smaller / simpler / trivial." | Every applicable gate and principle still applies; size is no exemption. |
| "Bug fix too small for TDD." | Write the failing test first. |
| "Spirit, not letter." | There is no separate spirit. Follow the letter. |
| "A governing source requires it, so it is automatically in the current scope." | A clear requirement outside signed scope needs the decision owner's Gate 2 resolution before coding. |
| "User wants speed." | Discipline now. Throwaway is slower. |
| "Tests pass." | Mocks lie. Run Gate 3. |
| "A separate RED or `test:` commit still proves test-first." | Editing order proves test-first; test and implementation still land together in one green `feat:` or `fix:` commit. |
| "It's not behavior, it's presentation." | Visual is observable. Test anyway. |
| "Future gate will catch it." | No gate ahead does this. Run it now. |
| "The reviewer would approve it." | Don't preempt their judgment. |
| "Plan says open the PR; smoke done." | Gate 5 has three steps. Plan doesn't override the gate. |
| "External code review will catch it." | That's Step 2. Skipping Step 1 = loop-of-fixes at chunk scale. |
| "I'll review at end of chunk." | Run at cadence — 5 commits or 200 lines, whichever first. |
| "Write a function for this." | Don't prematurely abstract — wait until the pattern repeats. |
| "Better safe than sorry." | Complexity has its own bug surface. Keep it simple. |
| "Just one more layer." | Layers compound. Step back at two. |
| "Defense in depth." | Only where evidence justifies it. |
| "Every case must be handled." | Implement cases that meet Principle 7's contract / reachability / observation / invariant threshold. Record the rest as accepted edges. |
| "That input can't happen — no caller passes it." | A crash or wrong output on a representable input is a defect, not an edge case. Fix by construction. |
| "Make it configurable, just in case." | Configuration is API surface. Add for real use cases, not hypotheticals. |
| "Reviewer keeps finding issues — keep iterating." | Findings accrete because the artifact has too many surfaces. Remove layers; don't add more. |
