# adversarial-review-loop — validation

Built test-first per `superpowers:writing-skills` (no skill edit without a failing
pressure test first). This records the scenario set so the rationale is recoverable
and the set is re-runnable.

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent
rule (Claude Code: `Explore`). Test-specific: one scenario per agent, text-only.

**Re-runnable suite.** The full scenario set — exact prompts, pass criteria, reps —
is codified in [adversarial-review-loop-scenarios.md](adversarial-review-loop-scenarios.md).
Run it before and after any change.

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

**At-cap regression — caught by the 5-rep suite, fixed (2026-06-20).** The move
re-opened an at-cap leak the over-fire refactor only masked: at the cap *with a
shared root*, agents reframe "the 3rd cycle's re-run finding" as a new below-cap
round and attack the root instead of escaping. 3-rep validation hid it (the
refactor's T3 was 3/3 by luck); the codified 5-rep suite exposed it — T3 **2/5**
escape on the feature commit vs **5/5 on `main`** (unedited), confirming a
feature-introduced regression. Fixed by stating a 3rd-cycle re-run finding *is* the
cap (+ a rationalization row): T3 → **5/5 escape**; NF still **5/5 attack-root**
(below-cap unaffected); T4 **3/3**.

**Baseline (2026-06-20, post-fix) — full suite green:** NF 5/5, T3 5/5, T4 5/5;
CS, T2, T5, T6, T7, PW, XL 3/3 each.

**Trim (2026-06-20) — REFACTOR at parity.** Trimmed ~45 words of redundancy/framing
(trichotomy intro reworded + caveat moved up front, trigger example list shortened,
higher-order line's escape clause cut, over-fire tail cut, escape-recording prose
merged); load-bearing wording (one invariant, SQLi/N+1, the at-cap fix, project-wide,
the validated rationalization rows) untouched. Full suite re-run on the trimmed
skill — **all 10 cells green at parity** (NF 5/5, T3 5/5, T4 5/5;
CS/T2/T5/T6/T7/PW/XL 3/3).

**Pre-PR cold-read (2026-06-20; opus — skill-authoring + consistency + concise).**
2 P2 + 3 P3; both P2s RED-tested before acting (Iron Law):
- *Same-kind-recurring 4th case.* The 3-outcome trichotomy doesn't explicitly slot
  the "same *kind* recurring → class-sweep was incomplete" backstop (the line under
  "Iteration cap"). RED **3/3 correct** anyway — agents sweep the class branch-wide
  whatever label they use; the actions converge. No edit.
- *Same-area umbrella* → accepted limitation, below.
- P3s: corrected the trim "cut" wording (this file); kept the higher-order line
  (1-line anchor); dismissed "cap stated 3 ways" — the cap-rule / at-cap-line
  redundancy **is** the at-cap fix, so consolidating would regress it.

**Known limitation — same-area umbrella (accepted, not fixed).** The over-fire guard
rejects *cross-domain* umbrellas (T4: SQLi vs N+1, "touch the database" — **5/5
scattered**) but not *same-area* ones: a data race (missing lock) + a deadlock
(lock-order) are two different invariants → the strict "one invariant" test says
*continue*, yet agents **3/3 umbrella them as "the concurrency axis" and audit**.
Pre-existing, not a trim regression — the pre-trim skill (with the since-cut "don't
invent an umbrella axis" line) also went **3/3**, one rep working around the line
explicitly. *Accepted because* a concurrency audit after a race + a deadlock is
defensible and low-harm (it tends to find real siblings), unlike the useless
database audit. *Not fixed because* a tighter guard would over-fit this contrived
case and risk under-firing the genuine shared-root case (NF), which must keep
firing. Revisit only if a same-area over-fire causes real waste in practice — that
is the watched failure to wait for.

**On edits to this move:** re-run the shared-root RED/GREEN, **T4 over-fire**,
**T3 at-cap**, and the **project-wide / cross-language** scenarios; keep the
**"one invariant"** wording.

## Cycle-3 mandatory step-back gate (added 2026-07-03)

Makes the step-back unconditional at cycle-3 entry — STOP; re-read all rounds as one
set; **written** pattern verdict in the work artifact; attack the pattern where it
lives (artifact / your own governing text / the reviewer) — and pins the per-cycle
test's object to the **accumulated set** ("dataset, not a news feed"). The prior
trigger was conditional on already-seeing the axis — circular, and thrice failed.

**Watched failures (RED):** PR-2, 6 reactive rounds (2026-06-19); calendar PR-3, 4+
rounds with the 2026-06-20 move in force (2026-07-01); steno PR #1, 5 external-gate
rounds ending in a cold-read escape (2026-07-03) — orchestrator rationalizations
recorded verbatim ("different classes each round — scattered → continue"; ledger read
as a news feed). Key finding: the steno orchestrator held **every finding in context**
and still fixed reactively — refuting the information-delivery premise of
`plans/2026-07-01-external-gate-root-attack-forcing-function.md` ("the gate hides the
set"). Attention failure, not access failure; the fix is doctrine, not hook payloads.

**Method (quick pass — deviations from house method flagged):** single-shot sonnet
subjects, skill text embedded as binding guidance, "these look quick — PR today"
pressure; 3 scenarios × 3 reps × 2 wording versions; every transcript hand-read.
Deviations: plain subagents (text-only task, no tools), 3 reps/cell not 5, and
subjects ran inside a consumer session — ambient dd doctrine present (controls
impossible in-harness; the 2026-07-03 RED-baseline arm passed 5/5 on ambient context
alone, so single-shot scenarios cannot reproduce the watched failure — RED rests on
the incidents above).

**Fixtures:** A — shared-root failure-path set (calendar-shaped, 3 rounds);
B — intended-scattered (doc drift / off-by-one / missing flag test);
C — reviewer re-raise of an adjudicated dismissal + unrelated P3 (steno-shaped).

**Results:** v1 wording — 9/9 verdict-before-fix under pressure; A 3/3 named the
axis (2/3 also split a different-invariant finding out, citing the over-fire guard);
C 3/3 closed by written ruling, no appeasement edits. B exposed a **fixture leak**:
3/3 found the same plausible partial axis (untested boundaries), consistently —
fixture flaw, not fabrication. Concise-writing rewording pass (same day), full
re-run: 9/9 gate again; **B improved to 2/3 scattered** via the invariant-vs-topic
test (v1: 0/3); C 3/3 incl. one rep correcting the cadence-reset nuance unprompted.

**Known issues (recorded, owner-adjudicated 2026-07-03):**
- *Cycle accounting:* ~4/18 reps read the third review's arrival as "cycle 3's
  re-run = cap" rather than cycle-3 entry. Every divergence conservative (ruling or
  escape instead of a final re-run); the step-back ran in all 18. Owner: wording fine
  as-is; tighten only if a real incident shows a non-conservative miss.
- *Fixture B* leaks a defensible axis — replaced 2026-07-04 by the G3B fixture
  (unused import / doc-contract constant / unmocked network test), which ran 3/3
  clean; the original leaky fixture is retired.
- *dd-log reset claims* on non-clean rounds by some reps — mechanically harmless
  (`log_review.py` derives the decision and resets on PASS only). No skill text.

**Formal run (2026-07-04, skill @ `db26297`) — full suite green at baseline.**
Protocol-style (read-only `Explore`, sonnet, skill read from the live file): NF **5/5**,
T3 **5/5**, T4 **5/5**; CS / T2 / T5 / T6 / T7 / PW / XL **3/3** each — identical to the
2026-06-20 baseline; the cycle-3 gate introduced no regression, and several T4/T3
transcripts show the gate's written verdict composing with the legacy guards (verdict →
scattered → continue; verdict → cap → escape). New cells codified as **G3A / G3B / G3C**
(scenarios file): G3B — the rebuilt no-plausible-thread scattered fixture — ran **3/3**
(written "no shared pattern" verdict citing three distinct invariants, no fabricated
axis, normal class-sweep), closing the fixture-B issue above. G3A/G3C baseline = the
2026-07-03 quick-pass (3 reps × 2 wordings, embedded-guidance method); first
protocol-style run due at the next gate edit.

## On edits

Re-run the RED/GREEN class-sweep scenario plus the T2–T7 set (read-only) before
shipping any change to the loop skill. Any change to the cap/backstop wording must
re-pass **T3** (escape at the cap) and **T4** (no false-positive on productive
iteration). Changes to the cycle-3 gate also re-run the A/B/C set above — B is the
over-fire guard for the mandatory verdict; keep "No shared pattern is a valid
verdict" intact.
