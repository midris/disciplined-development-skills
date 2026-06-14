# Architecture review — disciplined-development-skills

**Date:** 2026-06-14
**Lens:** external technical-architect review against the design brief —
*achieve trust through process and rigor*, in a skill set *reusable across
models and harnesses* (low-level hooks are Claude-specific by current choice;
the doctrine should travel).
**Posture:** adversarial (`adversarial-review`). This is the settled record
after a multi-round review; it includes what was conceded, not only what stuck.

## Verdict

Against the corrected brief, the system grades **well**. Trust-through-process
is a sound, established paradigm (regulated-industry certification works this
way — you trust the output because it passed a certified process, not because
each output was measured). The doctrine layer executes that paradigm with real
rigor, and the hook/skill split is a genuine portability architecture, not just
clean code. Two structural gaps survive scrutiny; both are fixable without
touching the architecture, and both now have placeholder plans.

## What's well-engineered

- **The Class A / Class B split** (`hooks/README.md`) — boundary-observable
  rules get a hook; in-the-head rules explicitly do *not* get an
  output-classifier. This refuses an entire category of bad engineering on
  principle, and documents why. The best idea in the system.
- **"Dumb triggers, smart model" + fail-closed only on irreversible
  boundaries** — three hard blocks, everything else advisory. Correct
  blast-radius discipline for a layer that matches `*` on PreToolUse.
- **The threat model treats the model as semi-adversarial against its own
  discipline** — escape hatches are env vars the model can't set by editing a
  tracked file; the rationalization tables are pre-loaded rebuttals to the
  model's own excuse-generation.
- **Production-grade defensiveness** — advisory layer degrades to safe defaults
  on any read/write failure, atomic writes, stdlib-only, per-branch state, 23
  test files for ~2,100 lines with the highest-blast-radius hook flagged for
  mandatory testing.
- **The hook/skill layering is a portability architecture** — Class A
  enforcement lives in disposable harness-specific hooks; Class B doctrine lives
  in portable markdown. Swap the harness, rewrite the dumb triggers, the
  intelligence travels.

## Findings (surviving)

### F1 — Load-bearing constants carry no on-page rationale

**Severity: P2.** The discipline thresholds — discipline-nudge cadence (50 tool
calls), edit-counter nudge / edit-block ceiling (30 / 60), commit-block ceiling
(5), adversarial-review-loop iteration cap (3) — are gut-feel starter values
meant to be iterated. That is a perfectly good rationale; it just isn't written
down. Under trust-through-process the constants are *part of the certified
process*, so by the system's own `writing-explicit-rationale` rule they owe an
on-page "why this number." Same gap applied to the superpowers
risk-acceptance — sound call, but it lived only in conversation until this
review (now on-page in the README).

**Fix:** see [`plans/deferred/2026-06-14-threshold-rationale-and-calibration.md`](../plans/deferred/2026-06-14-threshold-rationale-and-calibration.md).
Document each as a deliberately-provisional starter value now; calibrate against
the firing telemetry from
[`plans/2026-06-14-review-logging-instrumentation.md`](../plans/2026-06-14-review-logging-instrumentation.md)
once it lands.

### F2 — No human-facing trust artifact

**Severity: P2.** The brief's goal is *the human's trust*. The rigor produces an
audit trail — `References swept:`, `Verification:`, `reviews.jsonl`, plan
checkboxes — but it is aimed at the next agent and at git history, never
synthesized into a "here is why you can trust this PR" surface delivered to the
person deciding whether to merge. Process-trust frameworks still end in a
certification a human reads and signs; this one stops at the trail. The
self-attested nature is the hard part: the same model that did the work would
write its own trust summary, so the artifact has to lean on the one independent
signal in the system (the cross-vendor T3 review) to mean anything.

**Fix:** see [`plans/deferred/2026-06-14-human-facing-trust-artifact.md`](../plans/deferred/2026-06-14-human-facing-trust-artifact.md).

## Conceded during review (honest record)

- **"No effectiveness measurement" — withdrawn.** Framed against an
  outcome-metrics model of trust; the brief is deontological (rigor *is* the
  mechanism). Demanding A/B proof to justify the system's existence was a
  category error. The open logging plan is correctly scoped as *tuning*, not as
  existential proof.
- **"Implicit superpowers coupling" — withdrawn.** The dependency is declared in
  the README Requirements section. The value-vs-risk call (superpowers covers
  all in-scope harnesses; new-harness risk accepted) is the maintainer's to make
  and is defensible. What survived is narrower: the bundle is *architecturally a
  layer over* superpowers (now stated in the README), and the cross-repo
  behavior contract is unpinned (a minor, real fragility).

## Architectural note carried into the README

dd-skills is not a bundle-with-a-dependency; it is a discipline-flavored
*extension framework* over superpowers as a platform. Most skills are deltas
over a superpowers base. This is a deliberate, defensible identity — but it was
implicit, and "portable" for this bundle means "portable wherever superpowers
runs." Now named on-page.
