# Plan: human-facing trust artifact

**Status: placeholder.** Created from the 2026-06-14 architecture review
(Finding F2). Design-level and unsettled — run `superpowers:brainstorming` on
the surface and the anti-gaming model before any implementation. The notes below
are scope intent, not a locked design.

## Problem

The brief's goal is *the human's trust*. The system's rigor emits a real audit
trail — `References swept:`, `Verification:`, `reviews.jsonl`, plan
checkboxes — but it is aimed at the next agent and at git history, never
synthesized into a "here is why you can trust this PR" surface the deciding human
reads before merge. Process-trust frameworks still end in a certification a human
signs; this one stops at the trail.

## Scope intent

A **trust ledger**: a synthesized certification surface, emitted at a human
decision boundary (PR open, or end-of-chunk), that rolls up what the process
already produced —

- what load-bearing claims were grounded against source (`disciplined-research`),
- what was verified against the running system (Gate 3 evidence),
- what stale-reference sweeps ran (`References swept:` sections),
- what reviewed, at which tier, with what verdict (`reviews.jsonl`),
- what is explicitly accepted / deferred (on-page rationale).

Synthesis of existing artifacts, **not** new instrumentation — keep it
Principle-7 lean.

## Open questions (the hard ones)

- **Anti-gaming.** The work and the trust summary would come from the same model;
  a self-attested certificate is the "model grades its own homework" risk in a
  new wrapper. Does the ledger have to be *signed by the one independent signal*
  in the system — the cross-vendor T3 review — to mean anything? If so the ledger
  is really "render the independent review's verdict + the trail it checked,"
  not "the author summarizes itself."
- **Producer.** Hook-generated (deterministic, dumb-trigger-friendly) vs
  model-generated (richer, but self-attested and gameable)? Class A vs Class B
  tension.
- **Destination.** PR-body section, a generated file, or chat-before-merge?
  Must travel with the decision, per `writing-explicit-rationale`'s "where the
  choice is visible."
- **Failure mode to avoid.** A ledger that becomes a rubber stamp is worse than
  none — it manufactures false confidence. Better to emit nothing than to emit a
  green check the model learned to always produce.

## Rationale for placeholder

The surface and the anti-gaming model are genuinely unsettled and design-level;
scoping steps before brainstorming would be premature. Captured now so the
finding isn't lost.
