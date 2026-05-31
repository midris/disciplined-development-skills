---
name: writing-explicit-rationale
description: 'Use when making a choice a future reader or review pass might re-litigate — descopes, deferrals, shortcuts, exceptions, AND design choices over a defensible alternative. Applies to plans, specs, design docs, code comments at decision sites, and commit bodies. Triggered by "make this simpler", "drop the hardening", "skip X for now", "we can cover it in the PR", "this is overkill". Also fires when a review re-litigates the same decision twice.'
---

# Writing explicit rationale

**Role:** Companion — invoke when making a choice a future reader or review pass might re-litigate.
**Owns:** the trigger test (would a future reader wonder *"did the author consider X?"*), the what / why / what's-accepted artifact pattern, the artifact-scope guidance (plans / specs / commit bodies / code comments), the active-design-choice extension.
**Does not own:** project commit-body rules; plan-density rules (lives in
`lean-plan-writing`); stale rationale sweeps (lives in
`sweeping-stale-references`).

## Overview

Choices a future reader might re-litigate — descopes, deferrals, shortcuts, exceptions, or design decisions made over a defensible alternative — must carry their rationale on the artifact where the choice is visible. The current reviewer already knows; the future reader has zero context, and can't tell *"the author considered this"* from *"the author forgot."*

## The trigger test

> Would a future reader of this artifact wonder *"did the author consider X?"* if I don't write the reasoning?

- **Yes** → write the rationale on-page, before moving on.
- **No** → no rationale needed; the choice is self-evident from the artifact.

The trigger isn't "is the descope significant." Small descopes still get flagged as oversights if their absence is unexplained. The trigger is **reader-uncertainty**.

The trigger also fires on **active design choices over alternatives** — not just descopes. Choosing approach A over approach B when both are defensible, placing a guard at site X over site Y, preserving prior state instead of resetting on a new condition, picking a default at a fork in behavior — all trigger if a future reader could reasonably ask "why this?". The implementer's awareness of the alternative is what makes the choice rationale-worthy.

**Retroactive signal:** if an automated or human review pass re-litigates the same decision twice across rounds, the on-page rationale is missing or in the wrong place. Stop fix-forwarding the specific finding; audit the change for other decision sites missing rationale and batch them.

## When NOT to apply

Not every choice needs on-page rationale. The trigger test returns "No" — skip the rationale — for choices like:

- Picking between two equivalent libraries or patterns when both meet the requirement and the codebase doesn't already prefer one.
- Naming an internal helper function, variable, or struct field by an obvious convention.
- Following the codebase's existing pattern for a standard operation (error handling, logging, transaction wrapping) where the pattern is documented or pervasive.
- Choosing a UI label, button color, or copy variant from a small set where any is acceptable.
- Routine refactors that preserve behavior (rename for clarity, extract for reuse) when the refactor's purpose is self-evident from the diff.

The skill targets choices a reader could mistake for an oversight, not every micro-decision.

## What "on-page rationale" looks like

State three things in a sentence or two:
- **What** was chosen (or descoped).
- **Why** — over what alternative, or for what reason.
- **What's accepted** — residual risk, limitation, or trade-off (when relevant).

Concrete forms:

- **Test-detail trim**: *"5 cases deferred (deleted-user, disabled-user, session-race). Add to spec if policy team confirms; currently speculative."*
- **Hardening descope**: *"Residual risk: replay attacks and source-IP spoofing not mitigated. Accepted given the trust model — internal deployment, authenticated callers only."*
- **Project-rule exception**: *"CLI parity skipped: multi-select UI operation; CLI would be ergonomically awkward. Revisit if a scripted workflow emerges."*
- **Cap-sizing**: *"Capped at 500 items per call. Larger caps would need chunked transactions; deferred until telemetry justifies the work."*
- **Code design-choice**: *"Guard at the ingest callsite, not in the shared persistence helper. Another caller uses the helper with different semantics, so centralizing the guard there would be wrong. Accepts small duplication; revisit if a 3rd caller surface needs the same protection."*

The form is flexible; the content is fixed — what / why / what's accepted.

## Scope — which artifacts

Apply rationale where the choice is visible:

- **Plans** — note beside the affected item.
- **Specs / design docs** — rationale, residual-risk, or out-of-scope note.
- **Code comments** — at the decision site; explain why, not what.
- **PR descriptions / commit bodies** — additive, never a substitute for
  the on-artifact copy.

Rationale that lives only in git history or a PR gets missed. Put it at
the artifact site.

## Rationalizations

| Excuse | Reality |
|---|---|
| "The descoping editor's job is just to trim. Rationale is the original author's job." | The descoping editor IS the author of the descope. Adding rationale is part of the descope operation, not a separate task. |
| "The user said put it in the PR description." | PR descriptions decay and aren't versioned with the artifact. PR-only is a weaker guarantee. Write it on-page AND in the PR if both are wanted. |
| "The user / current reviewer / implementer already knows the reasoning." | Current audience ≠ audience over time. User acceptance and implementer awareness don't transfer to future readers (or automated review passes) who arrive with zero context. |
| "I'll add a brief note in chat; the user can paste it in." | Chat-acknowledged rationale never lands in the artifact. If you're the one editing, you write it on-page. |
| "I'll add the rationale later." | Later = never. The artifact ships without it; the next reader re-litigates. Write it on-page now. |
| "This descope is minor — not worth a sentence." | Trigger isn't significance, it's reader-uncertainty. One sentence is cheap; the flag-as-bug round-trip isn't. |
| "The behavior is in the artifact, that's enough." | Behavior (what) is necessary but not sufficient. The *why* and *what's accepted* distinguish considered choices from oversights. |
| "Following the user's explicit instruction is the higher discipline." | User instructions are HOW to act; rationale-on-page is WHAT survives the conversation. They don't conflict — do both. |
| "Adding rationale would bloat the artifact." | One sentence per descope is not bloat. Removed content without rationale IS the bloat pattern — it produces silent gaps reviewers re-litigate. |
| "A section header or referenced external doc already covers it." | External pointers are supplementary, not substitutive. Phase plans get archived; trust chains break. Name *what* on-page even when the *why* lives downstream. A header saying "deferred to Phase 23" without listing the items is the silent-gap pattern. |
| "The rationale is in the commit body." | Commit bodies don't travel with the artifact's reading flow. Cite durable rationale from the body; don't make the body the only rationale surface. |
| "It's process metadata not design rationale" | Design choices matter. Put all rationale for the artifact on the artifact. |

## Red flags

Stop and write the rationale if you catch yourself about to:

- Remove a numbered requirement from a plan or spec without leaving a marker for what was removed and why.
- Reply "I'll cover it in the PR description" without writing the rationale on-page first.
- Cut test cases without listing which were deferred and the deferral reason.
- Follow a "make it simpler" instruction by silently removing content instead of removing-and-explaining.
- Accept an exception to a project rule (test-first, CLI parity, etc.) without explicitly noting it's a deliberate exception with reasoning.
- Mention the rationale only in your chat reply to the user, never in the artifact you just edited.
- Delete a list of items underneath a section header that names a deferral and assume the header alone satisfies the requirement — name the items on-page even when the deferral framing is in the header.
- Commit a design decision whose rationale lives in the commit body only, with no durable rationale at the artifact site.
- Fix-forward a review's design-rationale finding by adding one inline comment, without auditing the change for other missing-rationale sites.

## Pairing

Companions:
- `lean-plan-writing` — when editing plans/specs, both apply (lean-plan-writing handles content density; this skill handles why-on-page for descopes and design choices).
- `sweeping-stale-references` — when a load-bearing fact changes that has a rationale comment, the comment goes stale too. Sweep the rationale alongside the symbol.

Invoked on-demand, not gate-shaped — apply whenever the trigger test fires, regardless of which other skills are loaded.
