---
name: lean-plan-writing
description: Use with `superpowers:writing-plans` whenever the deliverable is a plan or spec — new plans, plan edits, spec drafts, spec amendments. Triggered by "write a plan for X", "draft a spec", "update the plan", "edit the design doc", "add a task to the plan".
---

# Lean plan writing

**Role:** Refinement layer.
**Composes with:** `superpowers:writing-plans` — always invoke both.
**Owns:** the per-step content-density rule ("prose is the contract; code is the implementer's job"), the illustrative-snippet operational test, the test-table substitute for tricky logic.
**Does not own:** upstream plan scaffolding (header, files-touched, step decomposition, no-placeholders, TDD ordering, commit cadence) — that stays with `superpowers:writing-plans`.

`superpowers:writing-plans` says "if a step changes code, show the code." This skill flips that one rule: **prose is the contract; the code is the implementer's job**. Plans and specs carry requirements + order-of-operations + status — not the implementation written out.

## The rule

For every step, ask: *can a reader infer the shape from prose alone, given the linked spec and the codebase's existing patterns?*

- **Yes** → no code. Prose only.
- **No** → a short illustrative snippet (≤5 lines) anchoring the ambiguity. Not the implementation.

A snippet is *illustrative* when removing it makes the requirement genuinely ambiguous. It is *bloat* when removing it leaves prose that still specifies the requirement.

## What goes in prose, not code

- Per-step "What" — describe the change in prose.
- Tests required — list behaviors that must pass ("rejects empty input"), not test bodies.
- Fixtures — describe shape ("user row with non-null email, null deleted_at"), not literal JSON.
- BEFORE/AFTER migrations — structural description, not code diffs.
- API request/response — field names + types + semantics, not full JSON examples.
- Commit message templates — text, not code-fenced.

## When the implementation is genuinely tricky

The substitute for embedded code is a **denser test contract**, not vaguer prose. When the logic is gnarly (a multi-arm regex, a recursive CTE, a complex transform), give a table of `(input → expected output)` rows pinning every edge case. The implementer writes the implementation against the table with running tests as feedback. The table is the precise spec; the regex/CTE is one valid implementation of it.

## Per-artifact

- **Specs** (design docs — typically in a `specs/` directory): detailed requirements + design rationale + open questions. Heavier on the why.
- **Plans** (implementation plans — typically in a `plans/` directory): order-of-operations + per-step scope + dependency chain + status checkboxes. Heavier on the order.

Both bound by prose-is-the-contract.

## Rationalizations

| Excuse | Reality |
|---|---|
| "writing-plans says show the code" | This skill is the override layer. Compose with the upstream's scaffolding but ignore its "show code in every step" rule for plans and specs. |
| "the implementer needs the code to follow the pattern" | The implementer writes the code with running tests as feedback. Patterns live in the codebase, not the plan. |
| "this is a tricky migration / regex / heredoc — I need the exact code" | A ≤5-line snippet anchoring the shape is fine. For gnarly logic, use a test table instead of embedded code. |
| "TBD is forbidden so I have to write the code" | The prose alternative is concrete requirements ("Tests required: A, B, C"), not TBD. A list of behaviors is rigorous. |
| "I'm not writing it twice — the implementer just copies it" | They cannot — plan code has no execution feedback. It's a source of bugs that surface only at runtime. |
| "leaving it as prose is hand-waving" | "TODO add tests" is hand-waving. "Tests required: rejects empty input, returns exit 2 on missing prefix" is not. |
| "the user said make it extremely detailed" | Detail = requirements coverage + dependency clarity + explicit shortcuts with rationale. Detail ≠ embedded code. |
| "this is greenfield, no patterns to reference" | The spec carries the design; the plan carries the order. Code-embedding does not become correct because the context is greenfield. |
| "the implementer is new — I'll add a teaching snippet showing the concept" | Teaching snippets that show implementation shape ARE implementation — the implementer copy-pastes them. Explain the concept in prose; cite an existing codebase analogue or external doc. Do not embed the template they will copy. |

## Red flags

Stop and re-read this skill if you catch yourself:

- Pasting a function body, struct definition, or test body into a plan step.
- Writing a heredoc inside a plan code block.
- Drafting a JSON example longer than ~5 lines.
- Writing "the implementer should write:" followed by a code block.
- Defaulting to a code block as the first move when writing a step.

## Pairing

Always invoked with `superpowers:writing-plans`. Companion: `writing-explicit-rationale` (when descoping or making a design choice that could be re-litigated, write the rationale into the artifact).
