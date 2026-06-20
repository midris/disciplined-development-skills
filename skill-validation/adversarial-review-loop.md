# adversarial-review-loop — validation

Built test-first per `superpowers:writing-skills` (no skill edit without a failing
pressure test first). This records the scenario set so the rationale is recoverable
and the set is re-runnable.

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent
rule (Claude Code: `Explore`). Test-specific: one scenario per agent, text-only.

## Method

A discipline skill is tested by pressure scenario, not application. Each scenario
hands a subagent the skill text + a situation and records its decision, comparing the
pre-edit skill (RED) against the post-edit skill (GREEN). Rationalizations surfaced
in RED runs are recorded as rows in the skill's own Rationalizations table.

## Scenarios

- **RED/GREEN — class-sweep (round 1, single finding, no priming).** One isolated
  [P2] (an unscoped `cd` in a doc), round 1. RED (no class-sweep): fixes the cited
  line and re-dispatches. GREEN: names the class, enumerates across the branch, fixes
  every member, then re-runs.
- **T2 — singular finding.** A genuinely unique bug (off-by-one in one function).
  GREEN must NOT over-sweep: name the class, find no siblings, fix the one, re-run.
- **T3 — at the cap.** The third cycle still returns findings (any kind — even
  genuinely varied, new-surface ones). Must take the cold-read escape, not a fourth
  cycle.
- **T4 — productive iteration (below the cap).** By cycle 2, each round found a
  different real class on new surface. Must continue (fix + re-run); the "same
  *kind* recurring" backstop must NOT false-accuse.
- **T5 — P3-only.** Latest run returns only [P3]. Clean; stop; class-sweep does not
  apply to [P3].
- **T6 — sweep ≠ skip re-run.** After a thorough self-sweep, must still re-run the
  reviewer — a self-sweep never certifies clean.
- **T7 — class ≠ dismissal lever.** A [P2] from a different class than the one just
  swept must still be addressed, not deferred as "out of scope."

## Results

- **class-sweep RED→GREEN:** clean flip — RED fixed one line and re-dispatched;
  GREEN named the class, enumerated, fixed all members, then re-ran.
- **Regression set (T2–T7):** no regression to existing behavior — no over-sweep on
  singular findings, cap escape intact, no backstop false-positive on productive
  iteration, [P3]/clean handling unchanged, self-review rigor intact (T6/T7).
- **T3 caught a real regression** in the first backstop wording: it read as
  cap-softening ("new surface → one more sweep past the cap"). Reworded so the at-cap
  escape is mandatory and the sweep is a below-cap-only move; re-tested clean.
- **Cap-counting disambiguation:** "cycle" was read inconsistently — a cap-emphasis
  framing escaped at the third review, a productive-emphasis framing continued.
  Defining a cycle (review → class-sweep → re-run) and "escape if the third cycle
  still returns findings, not a fourth" made both framings escape consistently
  (cap-emphasis and productive-emphasis, two runs each).

## Find-the-pattern / attack-the-root move (added 2026-06-20)

Adds the third loop outcome the binary "productive vs drift" test lacked:
**productive-but-shared-root**. Trigger: across ≥2 cycles, new surface-different
findings violate **one invariant**. Action: name the axis → enumerate every site
against it **project-wide, across all languages**, including paths not yet cited →
fix in one pass → re-run. Below-cap only; at the cap the cold-read escape dominates.

**Watched failure:** meeting-pipeline PR-2 ran 6 reactive rounds before a human
prompted the step-back that named the failure-path axis; the root-attack converged
in ~1–2.

**Method:** pressure-scenario decisions (read-only `Explore`, sonnet subjects;
cold-read on opus), ≥5 reps on discriminating cells, every transcript hand-read.
Shared-root fixture: the `b0f4511` EventLog (durability plan), reused as canned
per-round findings.

**RED → GREEN.** Shared-root scenario (2 cycles, both failure-path, below cap):
RED (pre-edit) **5/5 grind** — continue the reactive loop, never name the axis;
GREEN (post-edit) **5/5 attack-the-root** — name the error-contract axis, enumerate
uncited sites, fix in one pass, stay below-cap.

**Regression (full T2–T7 + class-sweep re-run).** All hold. The max set caught two
defects the move introduced, fixed by REFACTOR + re-test:
- **Over-fire (T4):** 2/3 invented an umbrella axis from scattered findings (SQLi +
  N+1 "both touch the DB"). Fixed by keying the guard on **one invariant**, not a
  shared topic → **3/3 continue**. The fix did not under-fire NF: **3/3 still fires**.
- **At-cap (T3):** 1/3 self-audited instead of escaping. Fixed by an explicit "at the
  cap, escape — don't attack the root in place of escaping" line → **3/3 escape**.

**Project-wide + cross-language scope.** Multi-file: **3/3** project-wide.
Multi-language (Swift+Python+Go): primed **3/3**, unprimed **5/5** — agents translate
the invariant into each language's idioms (Python bare `except`, Go ignored
`err`/`panic`) unaided. **Load-bearing:** the **"one invariant"** framing is what
makes the audit conceptual / cross-language — do not weaken it to "pattern"/"topic".

**On edits to this move:** re-run the shared-root RED/GREEN, **T4 over-fire**,
**T3 at-cap**, and the **project-wide / cross-language** scenarios; keep the
**"one invariant"** wording.

## On edits

Re-run the RED/GREEN class-sweep scenario plus the T2–T7 set (read-only) before
shipping any change to the loop skill. Any change to the cap/backstop wording must
re-pass **T3** (escape at the cap) and **T4** (no false-positive on productive
iteration).
