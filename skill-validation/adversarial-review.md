# adversarial-review — validation

Records how the `adversarial-review` angle set was derived and how to re-validate
it. The skill is standalone/portable: a consumer with only the skill can run a
review, name an angle, or list the angles, with no `/dd-review` dependency.
Dispatch/orchestration is validated in [dd-review-command.md](dd-review-command.md).

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent
rule (Claude Code: `Explore`). One scenario per agent, text-only.

## The angle-necessity bar

An **angle earns its place only if it catches a class of issue the baseline
holistic review reliably misses.** The baseline is the always-on posture +
Rules (find what's wrong · enumerate every class · verify rationale · challenge
necessity). The test for an angle is **discrimination vs holistic**: plant a
*subtle* instance of the angle's class, then keep the angle only if a focused
reviewer catches it AND a holistic reviewer misses it. Goal: close the lenses
that make different models (codex vs claude) catch different things, so the
reviewer is model-consistent.

## Audit (2026-06-16/17)

Ran discrimination tests (holistic RED vs angle GREEN) on subtle planted targets
for seven candidate angles.

**Holistic caught the target in 6/6 of correctness, rationale, cross-file/
consistency, security, executability, necessity — and 4/4 conformance** (incl. a
noisy multi-issue diff, two independent holistic runs). Lesson: **per-angle
discrimination on a small artifact is the wrong instrument** — a strong model
following the posture catches everything when there's nothing to dilute its
attention. It discriminates only for (a) **scope** changes to a definition, and
(b) **specialized lenses the posture lacks**.

**Decisions:**

| Angle | Verdict | Why |
|---|---|---|
| correctness | **dropped** | the posture *is* "find what's wrong" — holistic caught it |
| rationale | **dropped** | already base posture Rule "Verify every rationale claim" |
| necessity | **dropped (as angle)** | already base posture Rule "Challenge necessity"; its Principle-7 + concise-writing pointers folded into that Rule |
| conformance | **dropped** | "verify against governing rules" is posture; holistic caught 4/4 |
| security | **deferred** | claude finds low-hanging secrets via posture; real leverage is a dedicated security skillset applied explicitly, not a one-line angle |
| **consistency** | **kept** | cross-corpus drift (contract/terminology/wording/single-source) is *not* in the posture; manually prompting it reliably yields findings |
| **executability** | **kept** | the zero-context-implementer lens; surfaced by the maintainer's codex-review gap observations (not reproduced inline here) |
| **skill-authoring** | **kept** | the **only** angle that beat holistic in discrimination — see below |

`security` was broadened (+ leaked secrets/keys) and tested cleanly (old def
returned "No findings" on a hardcoded key; broadened def flagged it P0) — so the
broadening *is* load-bearing — but the angle was still dropped per the bar above:
holistic already catches secrets, and a future dedicated security skill is the
higher-leverage home.

The pre-branch command also had `cross-file` and `doctrine-consistency`; both
folded into `consistency` (their drift / single-source concerns), and the
governing-rule half of `doctrine-consistency` became `conformance`, then dropped.

## skill-authoring discrimination (the one that passed)

Planted a skill whose `description` summarized the workflow and whose rule
("Always run the tests") had no rationalization-loophole counters.

- **Holistic (RED):** flagged executability/consistency issues but **missed** the
  CSO trap (description-summarizes-workflow → agents skip the body) and framed the
  open rule as a P3 "discipline smell," not as exploitable loopholes.
- **skill-authoring (GREEN):** caught both — the CSO trap and the open
  rationalization loopholes — applying the `superpowers:writing-skills` lens.

Holistic missed what the angle caught → it earns its place.

## Standalone angle selection

- **RED — pre-edit skill, doc-dominant artifact:** with selection delegated to the
  command, a skill-only agent **guessed** and excluded the right doc angle.
- **GREEN — post-edit skill:** the **When to apply** list lets a skill-only agent
  select correctly and answer "what angles are available?" — the portability goal.

## Per-angle focus (kept angles catch their target)

Each angle's definition transmits the right focus (a reviewer applying it catches
its class):

| Angle | Target | Result |
|---|---|---|
| consistency | terminology drift across the corpus; keyword-only arg passed positionally (cross-file) | ✓ flagged |
| executability | doc step with undefined deps / no command | ✓ flagged |
| skill-authoring | CSO description trap + open rationalization loopholes | ✓ flagged (holistic missed) |
| durability | INV-2 read-side (torn tail, interior blank line) + crash-on-bad-input rationale | ✓ lifted (baseline missed); generalizes to Python/Go |

## durability angle (added 2026-06-19)

Failure-path lens for code that mutates or reads durable / source-of-truth state.
**INV-1** durable mutations are atomic (or fully roll back + typed error + retry-safe);
**INV-2** reads reject anything not fully committed (torn tail, interior corruption,
gaps, unknown/forward version) and distinguish empty from corrupt.

**Why kept (per the necessity bar).** Single-model small-artifact discrimination
under-credits this class, so the angle ships on **lens-not-in-posture + the
cross-model gap**: in the meeting-pipeline PR-2 "event-log substrate" session,
codex's blocking pre-PR gate caught **8 failure-path defects across rounds 1–5**
(round 6 clean) while Claude's three holistic per-task reviews AND an Opus
whole-branch "ready to merge" missed every one — a whole unexamined axis. The
RED/GREEN below is **corroborating**, not a vetoable gate.

**Fixtures** (read-only `Explore`, subjects on sonnet; cold-read on opus; ≥5 reps
on the primary; every flagged match read by hand). Primary: the `b0f4511`
`EventLog.swift` (inlined in the durability deferred plan — ~160-line append-only
log, failure-path defects latent among correct happy-path code). Generalization:
a Python append-only JSONL log, a Go atomic-overwrite snapshot store (different
shape), a clean Go store (over-fire control), an in-memory rate limiter (skip
control). All are paper/transcript reviews.

**Results.**
- **RED (no angle) vs GREEN (angle), b0f4511, 5 reps each.** Baseline reliably
  caught the visible logic bugs (I/O error handling, line-count seq miscount: 5/5)
  but **missed the INV-2 read-side** (interior blank line 0/5, torn final record
  0/5) and accepted the planted "crash is intentional" rationale on the encode
  crash (1/5). GREEN: blank line → 5/5, torn tail → 3–4/5, crash-on-bad-input →
  5/5, reviewers explicitly citing the read/replay checklist and the crash
  rationale-counter. No regression on the two the baseline already caught.
- **Generalization.** Python log: angle adds the same INV-2 read-side over a
  (stronger) baseline, in different idioms. Go snapshot (atomic-overwrite, not
  append-only): catches all planted defects 3/3 incl. panic-on-bad-input via the
  rationale-counter — the lens is not tied to the EventLog/Swift shape.
- **Over-fire / skip controls.** Clean Go: no false P0s (only genuine subtle
  issues). In-memory limiter: reviewers correctly did NOT apply the angle (the
  When-to-apply gate held).

**Probe-wording iterations (each re-tested).** crash-on-bad-input probe sharpened
to counter "it's a programmer error" (NaN 0/5 → 5/5); de-Swiftified
(`try!`/`Codable` → panic/abort/unchecked-unwrap; "a value that satisfies the
static type") to generalize off Swift, re-confirmed across all fixtures; two-harm
wording added (torn record AND caller-can't-recover) to close a "crash-is-pre-write"
dodge — closes it when the probe is applied. Residual 4/5 on the Swift primary is
a globally-lenient reviewer that skips the probe, not a wording gap; not chased,
to avoid tuning to one rep. Finally the crash parenthetical was trimmed ~22%
(rebuttal + static-type counter + both harms kept) and re-measured at parity
(Swift 4/5, Python 3/3, Go 3/3) — confirming the remaining words are the
load-bearing core.

**Cold-read on the final skill (opus; consistency + skill-authoring).** 4 findings,
all P2/P3 (checklist-under-bullet asymmetry, parenthetical length, run-on,
table-row breadth); all dismissed with rationale — the asymmetry and the
parenthetical are load-bearing (the rationale-counter is a rebuttal + two distinct
harms, each measured to drive a catch, not redundancy), the rest advisory/locked.

## On edits

- Adding/refining an angle: run the **discrimination test** (subtle target,
  holistic RED vs angle GREEN). Keep only if holistic misses it. Back the decision
  with cross-model (codex) gap data where available.
- Changing the **When to apply** list or a definition: re-run the standalone
  selection RED/GREEN and the affected per-angle scenario.
- Limitation: small-artifact discrimination can't validate *coverage* value (it
  appears only at scale / across models). consistency and executability are kept on
  the lens-not-in-posture + codex-gap grounds, not on demonstrated single-reviewer
  discrimination; skill-authoring is the one with a clean discrimination result.
