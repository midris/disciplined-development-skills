# adversarial-review-loop — validation

Built test-first per `superpowers:writing-skills` (no skill edit without a failing
pressure test first). This records the scenario set so the rationale is recoverable
and the set is re-runnable.

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent
rule (Claude Code: `Explore`). Test-specific: one scenario per agent, text-only.

## Method

A discipline skill is tested by pressure scenario, not application. Each scenario
hands a subagent the skill text + a situation and records its decision, comparing the
pre-edit skill (RED) against the post-edit skill (GREEN).

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
  still returns findings, not a fourth" made both framings escape consistently (4/4).

## On edits

Re-run the RED/GREEN class-sweep scenario plus the T2–T7 set (read-only) before
shipping any change to the loop skill. Any change to the cap/backstop wording must
re-pass **T3** (escape at the cap) and **T4** (no false-positive on productive
iteration).
