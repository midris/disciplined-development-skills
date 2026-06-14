# Plan: threshold rationale + calibration

**Status: placeholder.** Created from the 2026-06-14 architecture review
(Finding F1). Not yet brainstormed or decomposed — run
`superpowers:brainstorming` before implementation. The sub-tasks below are scope
intent, not a locked step list.

## Problem

The discipline layer's tuning constants are gut-feel starter values with no
on-page rationale. Under trust-through-process the constants are part of the
certified process, so by `writing-explicit-rationale` each owes a written "why
this number." Today a reader can't tell a calibrated threshold from an arbitrary
one.

The constants and their homes (verify against `lib/dd-defaults.json` and the
hook docstrings before editing — do not trust this list):

- discipline-nudge cadence — tool calls since last re-ground (~50).
- edit-counter nudge / edit-block ceiling (~30 / ~60).
- commit-block ceiling — commits since last cold-read (~5).
- adversarial-review-loop iteration cap (3).

## Scope intent

Two parts, separable by dependency:

1. **Document-as-provisional (can land now).** At each constant's single source
   of truth, add a one-line rationale: deliberately-provisional starter value,
   gut-feel, to be calibrated against firing telemetry. Single source of truth
   stays the defaults JSON; rationale lives next to it or in `dd-config.md` — do
   not duplicate the value. This alone closes F1's *rationale* gap.

2. **Calibrate (blocked on telemetry).** Depends on
   [[2026-06-14-review-logging-instrumentation]] landing. Use the hook-firing
   logs + `reviews.jsonl` to measure whether each nudge/block fires near genuine
   drift or as clock-noise, and re-set the numbers from data.

## Open questions

- What makes a threshold "right"? Candidate signal: nudge false-positive (noise)
  rate — fraction of fires not followed by a real re-ground or a real review
  finding. Target rate? (A fixed-cadence nudge uncorrelated with drift trains
  the tune-out the design doc says it avoids — this is the metric that catches
  that.)
- Are these per-consumer-tunable already (they are, via `dd-config.json`), and
  if so is the fix just better-documented defaults plus a "how to tune for your
  cadence" note rather than new machinery? Lean toward the latter —
  Principle 7.

## Rationale for placeholder

Part 1 is documentation and could start immediately, but it's bundled here with
Part 2 because the rationale text should say *how* the number will be
calibrated — so the calibration design wants at least a sketch first. Part 2
cannot start until the logging plan lands.
