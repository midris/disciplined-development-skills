---
name: disciplined-development
description: Use when starting a session, while doing development work (writing code, editing plans or specs, drafting designs, fixing documentation drift surfaced by a review), or at every boundary — before AND after dispatching subagents (carrying the discipline into their prompts), committing, opening PRs, receiving code review, and claiming work done. Especially in auto-mode, when a plan or spec is referenced, when a review flags a doc-stale claim, or when working with subagents.
---

# Disciplined Development

**Role:** Orchestrator — parent skill governing development sessions and dispatching companion skills at gate boundaries.
**Owns:** the Iron Law, the five gates, the principles, and the
mode-emphasis routing table.
**Does not own:** verification mechanics, stale-reference sweeps,
research grounding, rationale writing, plan-density rules, adversarial
review posture, or review iteration. Those live in companion skills.
Methodology skills are invoked from the gates and mode table.

## Overview

Written records govern how a project works; momentum erodes them — you
stop re-reading and start trusting memory.

**Core principle:** the file wins. Write it down before you forget;
re-read it before you act; produce evidence before you claim done.
**Gates** force specific actions at decision boundaries. **Principles** are the rules they enforce. No discipline is skippable on grounds of size, effort, or impact.

## The Iron Law

```
NO PROGRESS PAST A GATE WITHOUT THE ARTIFACT IT REQUIRES
```

Each gate is fail-closed. The artifact must exist — in writing, in
chat, or in the running system — before the next action.

## Operational gates

**Gate 1 — Read before writing.**
Re-read from disk: governing docs (CLAUDE.md / AGENTS.md /
CONTRIBUTING.md, ARCHITECTURE, project memory), task sources
(active plan, linked specs/mockups, design principles, API docs,
schemas), and external facts (library capabilities, versions, API
behavior). Applies to planned work, ad-hoc changes, bug fixes, docs
edits, AND code reviews (giving or receiving) — never review the diff
without re-reading the active plan, governing spec, and linked
guidance the change is supposed to satisfy. "Last session" doesn't
count; memory isn't a source. Cite fetched facts that drive a
decision. If nothing applies, say so before proceeding.

**Gate 2 — Translate to written before coding.**
Capture scope as written bullets before coding. Extract visible mockup
strings into the plan. Plan review ends with a written diff signed off on
the document. Use `superpowers:brainstorming` when scope/design is
unsettled. Use `superpowers:writing-plans` + `lean-plan-writing` for
plans and specs.

**Gate 3 — Verify against the running system before claiming done.**
UI: screenshot or DOM snapshot. API: live HTTP response. CLI: actual
invocation. Tests passing is necessary but not sufficient — mocks lie
about live shapes. Paste evidence in chat.
REQUIRED SUB-SKILL: `superpowers:verification-before-completion`.

**Gate 4 — Sweep stale references before commit.**
When a change touches a load-bearing fact (code symbol, doc claim,
schema, spec constraint), every place encoding it goes stale. Find
them all; reconcile in one commit; document the sweep in the commit
body's `References swept:` section.
REQUIRED SUB-SKILL: `sweeping-stale-references`.

**Gate 5 — End-of-chunk review + smoke pass before PR.**
Three steps, in order. Plan checklist does not override the gate.

1. **Self-review** `git diff <chunk-base>..HEAD`; address findings per
   `adversarial-review-loop`.
   REQUIRED SUB-SKILLS: `superpowers:requesting-code-review` + `adversarial-review` + `adversarial-review-loop`.
2. **External review** of the chunk diff. `[P0]`/`[P1]`/`[P2]` block the
   PR (resolve before merge); `[P3]` is advisory.
3. **Smoke pass** affected flows; capture evidence in the PR body.

The PR is opened by you, not by an agent.
REQUIRED SUB-SKILL before opening PR:
`superpowers:finishing-a-development-branch`.

## Principles

Each gate enforces these.

**1. Write it down, don't remember it.**
Verbal scope, design decisions, requirements, and plan changes go
into a file the moment they're agreed. Conversation is not a contract;
the file is.

Flip task checkboxes in active plans in the same commit where the
task is completed.

When the write-down includes an intentional descope, deferral,
shortcut, exception, or design choice over a defensible alternative,
the rationale belongs on-page too — not only in chat.
REQUIRED SUB-SKILL: `writing-explicit-rationale`.

**2. Re-read, don't recall.**
At session start and every major transition, open the actual files.
Plans drift; context decays.

**3. Obey what's written; surface what isn't.**
If a guideline says "do X," do X. Don't decide this case is the
exception. Violating the letter is violating the spirit. Surface
unclear or conflicting guidance to the user — do not silently resolve.
Includes scope-ambiguous prompts: "our X" vs "X in general" — flag it
or check both, don't pick silently.

**4. Carry the discipline into subagent dispatches.**
Subagents don't auto-load skills. Every dispatch prompt must tell the
implementer to load the `disciplined-development` skill before work.
If direct skill loading is unavailable, require reading
`.claude/skills/disciplined-development/SKILL.md` first and following it as
binding guidance.

Name governing files to re-read before acting. Require a re-read before
claiming done. Gate summaries do not substitute for loading the skill. Pick
the model for task complexity.

REQUIRED SUB-SKILL: `superpowers:subagent-driven-development`.

**5. Test-first for behavior changes — non-negotiable.**
- Test and impl land in the same commit (`feat:` or `fix:`).
- Editing order: write failing, watch fail, implement, refactor.
- Never `test:` then `feat:` for the same unit (the `test:` commit would land red).
- Test names state what they prove (`rejects_empty_input`), not what they do (`handles_edge_cases`).
- Fixtures match real producer output, not idealized values.
- Exceptions (need user approval): throwaway prototypes, generated code, static configuration values (not schema or behavior changes).

REQUIRED SUB-SKILL: `superpowers:test-driven-development`.

**6. Verify load-bearing claims against reality, not memory.**
Re-read schemas, handlers, fixtures, and external facts before describing them. Memory isn't a source.
REQUIRED SUB-SKILL: `disciplined-research`.

**7. Keep it simple — add complexity only when evidence demands it.**
- Build to satisfy the requirement. Don't over-engineer.
- Don't build for hypothetical futures. Don't prematurely optimize. Don't prematurely abstract (rule of three).
- Wait for the edge case to actually occur before handling it.
- When iteration keeps surfacing new findings, remove layers — don't add more.

Reviewer-side counterpart lives in `adversarial-review`.

**8. Review periodically and catch problems early.**
Run adversarial review at chunk boundaries and after roughly 5 commits or
200 net lines since the last clean review. If local automation sets a
stricter cadence, follow it; otherwise self-trigger.
REQUIRED SUB-SKILL: `adversarial-review-loop`.

## Mode emphasis

| Mode | Active gates | Methodology skill |
|------|--------------|-------------------|
| Brainstorming | Principles 1, 7 | `superpowers:brainstorming` |
| Plan writing | Principles 1, 7 + Gates 1, 2 + diff signoff | `superpowers:writing-plans` + `lean-plan-writing` |
| Implementation (sequential) | Principles 1, 2, 5, 6, 7, 8 + Gates 1, 2, 3, 4, 5 | `superpowers:executing-plans` or `superpowers:subagent-driven-development` |
| Implementation (parallel, independent only) | as above | `superpowers:dispatching-parallel-agents` |
| Debugging | Principles 1, 2, 5, 6 + Gates 1, 3, 4 | `superpowers:systematic-debugging` |
| Code review (giving) | Principles 3, 7, 8 + Gates 1, 4 + read the diff | `superpowers:requesting-code-review` + `adversarial-review` + `adversarial-review-loop` |
| Code review (receiving) | Principle 3 + Gate 1 (surface, don't interpret) | `superpowers:receiving-code-review` |
| Editing docs / specs / plans | Principles 1, 3, 6, 7 + Gates 1, 4 | `superpowers:writing-plans` + `lean-plan-writing` (for plans/specs) + `concise-writing` |

## Common rationalizations

| Excuse | Reality |
|--------|---------|
| "I read it / wrote it / searched it last session." | Cross-session memory is stale. Re-read. |
| "Last N tasks went fine." | Survivorship reasoning. Re-read anyway. |
| "I'll remember to do X later." | Write it now. Memory rationalizes. |
| "This case is different / smaller / simpler / trivial." | Apply anyway. Size doesn't exempt Gate 1. |
| "Bug fix too small for TDD." | Write the failing test first. |
| "Spirit, not letter." | There is no separate spirit. Follow the letter. |
| "User wants speed." | Discipline now. Throwaway is slower. |
| "Tests pass." | Mocks lie. Run Gate 3. |
| "Tests after = same outcome." | Not equivalent. Test first. |
| "Logically independent units → separate RED commits." | Splitting commits is fine; test-without-impl never is. |
| "`test:` commit followed by `feat:` commit = test-first." | Editing order, not commit shape. Same commit, both go in. |
| "Constraint is structural; value doesn't matter." | Constraints fire on what producers write. Use producer-shaped fixtures. |
| "It's not behavior, it's presentation." | Visual is observable. Test anyway. |
| "Build already passed; no need to re-run." | You just changed it. Re-run. |
| "Future gate will catch it." | No gate ahead does this. Run it now. |
| "Subagent reported DONE." | Read the diff. Verify before commit. |
| "The reviewer would approve it." | Don't preempt their judgment. |
| "Spec/plan locks the constraint." | Locking ≠ verifying. Grep producers. |
| "Plan says open the PR; smoke done." | Gate 5 has three steps. Plan doesn't override the gate. |
| "external code review will catch it." | That's Step 2. Skipping Step 1 = loop-of-fixes at chunk scale. |
| "I'll review at end of chunk." | Run at cadence — 5 commits or 200 lines, whichever first. |
| "Write a function for this." | Don't prematurely abstract — wait until the pattern repeats. |
| "Better safe than sorry." | Complexity has its own bug surface. Keep it simple. |
| "Just one more layer." | Layers compound. Step back at two. |
| "Defense in depth." | Only where evidence justifies it. |
| "Every case must be handled." | Handle observed cases. Document the rest as accepted edge cases. |
| "Make it configurable, just in case." | Configuration is API surface. Add for real use cases, not hypotheticals. |
| "Reviewer keeps finding issues — keep iterating." | Findings accrete because the artifact has too many surfaces. Remove layers; don't add more. |
