# Deferred — `adversarial-review` "durability" angle (failure-path lens for source-of-truth state)

**Parked 2026-06-19**, surfaced during the **meeting-pipeline** PR-2 "event-log substrate" session.
A generalized review angle to add to the `adversarial-review` skill, with the validation protocol to
build it. The edit lands in **this repo** (`skills/adversarial-review/SKILL.md`); consumers symlink
that dir into their `.claude/skills/` via `install-skills.sh`.

**Governing:**
- Skill to edit (in THIS dd repo): `skills/adversarial-review/SKILL.md` — its **Review angles**
  table (`consistency` / `executability` / `skill-authoring`) + **When to apply** list.
- Validation method (in THIS dd repo): `skill-validation/adversarial-review.md` — the
  **angle-necessity bar** (discrimination vs holistic) every angle must pass. Read it first; its
  "small-artifact is the wrong instrument" lesson is decisive (see Validation below).
- Skill-authoring rules: `superpowers:writing-skills` — the **Iron Law** (no skill edit without a
  failing test first), **Match the Form to the Failure**, description-is-triggers-not-workflow,
  token efficiency (adversarial-review is frequently loaded — keep the addition compact).
- Real-world evidence (the watched failure): the **meeting-pipeline** PR-2 "event-log substrate"
  session — its 6-round codex pre-PR gate vs Claude's clean holistic reviews. The table below IS the
  record; you do not need that repo's session history to act on this plan.

## Why this exists (the watched failure — already real, not hypothetical)

Across PR 2, holistic adversarial reviews — three per-task reviews **and** an Opus whole-branch
review that returned "ready to merge" — all passed `EventLog` while an external gate (codex) found
**seven** defects across four rounds. Categorizing them:

| Finding | Class |
|---|---|
| open-failure leaks `CocoaError` not the documented error type | mutation failure path |
| `try!` on encode crashes the process on a pathological payload | mutation failure path |
| `replay` silently drops interior blank lines | read accepts non-committed |
| no parent-dir fsync on fresh file → dir entry not crash-durable | durability |
| parent-fsync **throws after commit** → un-advanced seq → retry duplicates | mutation not atomic |
| `replay` accepts an unterminated/torn final record | read accepts non-committed |
| content-fsync failure leaves partial bytes → retry duplicates | mutation not atomic |

Seven of seven collapse to two invariants of durable / source-of-truth state that the holistic
reviews never enumerated or tested. The reviews optimized the **happy path + spec-field fidelity**
(envelope fields, snake_case, seq contiguity when all goes well); the gate attacked the **failure /
crash / partial-state** axis — which, for a source-of-truth store (spec D2: "the log is the source
of truth; crash consistency = replay + idempotent reconciliation"), **is the primary contract, not
an edge case.** The miss was systemic (a whole unexamined axis), which is why it took four reactive
rounds instead of one audit. An angle that names this axis turns it into a checklist the reviewer
runs up front.

## The principle (generalized beyond event logs)

A review of code that **mutates or reads durable / source-of-truth state** (file writes, append-only
logs, DB transactions, a cache treated as truth, any persistence layer) must adversarially verify two
invariants — neither of which a happy-path read surfaces:

- **INV-1 — durable mutations are atomic.** The op either fully commits (written **and** durably
  flushed **and** any in-memory index/counter advanced) or leaves the store byte-for-byte as before
  and returns a typed, documented error. No partial bytes, no committed-but-unrecorded state, no
  crash on pathological input, no lower-layer error type leaking past the documented contract, and
  **retry-safe** (a retry after a failure can't duplicate / gap / reorder).
- **INV-2 — reads of durable state reject anything not fully committed.** A read/replay rejects (or
  loudly flags) torn/partial final records, interior corruption, gaps, out-of-order records, and
  unknown/forward versions — it never silently accepts or drops them. It distinguishes
  *empty/absent* from *corrupt*.

This is `disciplined-development` Principle 7 inverted: Principle 7 says don't add handling for
failures you haven't observed; this angle says for **durable source-of-truth state the failure modes
ARE the spec**, so enumerate and test them — the evidence the principle demands is the store's own
durability contract.

## Proposed skill edit (draft — final wording set by the RED/GREEN below, per the Iron Law)

Add one row to the **Review angles** table and a matching **When to apply** bullet. Draft:

- **Angle name:** `durability` (working name; the RED/GREEN may favor `crash-consistency` or
  `failure-path` — pick whichever wording actually shifts reviewer behavior in test).
- **Looks for:** "failure/crash/partial-state paths of durable or source-of-truth state — durable
  mutations that aren't atomic (partial write, committed-but-unrecorded, crash on bad input, leaked
  error type, non-retry-safe) and reads that accept non-committed data (torn/partial final record,
  interior corruption, gaps, out-of-order, unknown version silently parsed)."
- **When to apply:** the artifact creates, persists, or reads durable / source-of-truth state — a
  file write, append-only log, transaction, journal, spool, or any store another component treats as
  the source of truth. (Skip for pure in-memory / stateless code.)
- **Enumerate checklist** (the lens's concrete probes — this is what makes it operational, mirroring
  how `executability` lists "missing definitions, ambiguous contracts"):
  - *Mutation:* partial write then error → rolled back? flush/commit fails after write → acknowledged
    anyway? process killed mid-op → torn record? pathological input (non-encodable, NaN, oversized) →
    crash or typed error? failure surfaced as the documented error type or a leaked lower-layer one?
    retry after failure → duplicate / gap / reorder?
  - *Read/replay:* torn/partial final record (missing terminator) rejected? interior corruption
    (blank line, gap, out-of-order) rejected, not skipped? unknown/forward version loud, not
    mis-parsed? empty distinguished from corrupt?

**Keyword coverage** (for skill discovery — weave into the angle text / description): crash
consistency, durability, atomic, fsync, source of truth, append-only, replay, torn write, partial
write, corruption, retry, idempotent.

**Token discipline:** adversarial-review is frequently loaded; keep the addition to a table row + a
when-to-apply bullet + the compact checklist. Do not narrate. Do **not** push the checklist into the
`description` field (writing-skills: the description triggers loading and must stay
triggers-only — a workflow summary there gets followed instead of the body).

## Validation — the discrimination test (read the necessity bar FIRST)

`skill-validation/adversarial-review.md` is decisive and shapes the whole test: **per-angle
discrimination on a SMALL artifact is the wrong instrument** — a strong model following the baseline
posture catches everything when there's nothing to dilute its attention. Of seven prior candidate
angles only `skill-authoring` won a clean small-artifact discrimination; `consistency` and
`executability` were kept on **lens-not-in-posture + codex-gap** grounds, not toy discrimination. So
**do NOT** validate this with a 10-line snippet and conclude "holistic caught it, drop it." Two
things make the test representative:

1. **Use a realistically-DILUTED fixture** — a full, plausible ~190-line source-of-truth file where
   the failure-path defects are latent among correct happy-path code, so the reviewer's attention is
   diluted (the condition under which holistic actually misses them). A tight snippet is the wrong
   instrument.
2. **The load-bearing evidence is the cross-model gap**, not a single-reviewer toy result: in the
   real session, codex's blocking gate caught all seven failure-path defects across six rounds while
   Claude's holistic per-task reviews AND an Opus whole-branch "ready to merge" missed them (the
   "Why this exists" table). That gap is the justification — exactly how consistency/executability
   earned their place.

### The fixture (standalone)

The real diluted artifact: in the **meeting-pipeline** repo
(`/Users/sidris/work/coronis/code/meeting-pipeline`), the initial Task-2.2 `EventLog` (richest
co-present defect set):

```
git show b0f4511:swift/Steno/Sources/Steno/Events/EventLog.swift
```

(commit reachable from `main` via merge `c2a5403`; the `feat/rec-2-event-log` branch was deleted on
merge.) If you don't have that repo, plant the defects below into any realistic, full-length
append-only-log / file-store artifact — the point is a diluted real-looking file, not these lines in
isolation:

- **append** — `let data = try! StenoJSON.encoder().encode(envelope)` (crashes the process on a
  non-finite `Double`); `append` is non-`throws`; `writeAndSync` does **no rollback** on a failed
  write/fsync.
- **replay** — `raw.split(separator: 0x0A, omittingEmptySubsequences: true)` then decode-each:
  silently **drops interior blank lines** AND **accepts a final record with no trailing `\n`** (no
  `raw.last == 0x0A` check) — a torn/uncommitted tail is read as committed.
- **resolveSeq** — `nextSeq = raw.split(…).count + 1` (a raw **line count**; the doc-comment even
  claims "(max seq found) + 1" but counts lines) → `append` extends a gapped/torn log instead of
  refusing.

The GREEN-target (fixed) behaviour is on meeting-pipeline `main`: atomic append with truncate-
rollback, replay rejecting torn tails / blank lines, `resolveSeq` deriving from a validated replay.

### RED / GREEN

1. **RED (baseline, current skill).** Fresh reviewer with the *current* `adversarial-review`
   (posture + baseline Rules + existing angles, NO durability angle) over the diluted fixture. Expect
   happy-path / spec-fidelity findings and a **miss** on the INV-1/INV-2 violations. Record verbatim.
2. **GREEN (with the angle).** Same reviewer + fixture, skill now carrying the durability angle.
   Expect it to enumerate the mutation + read checklist and flag the violations the baseline missed.
3. **Method (writing-skills "Micro-Test Wording"):** ≥5 reps per variant; always include the no-angle
   control; read every flagged match by hand (template echoes masquerade as hits). The angle earns
   its place only if the with-angle arm catches violations the control arm consistently misses —
   weight the cross-model gap above, since small-artifact discrimination under-credits coverage value.

**Per-defect GREEN rubric** (each row: a fixture defect → the finding the angled reviewer must
produce; reusable as discrete micro-tests and as regression checks for the angle's wording):

| Defect in fixture | INV | GREEN finding the angle must elicit |
|---|---|---|
| `append` `try!`-encodes the payload | INV-1 | a pathological payload crashes the process instead of a typed error |
| open-failure path returns a raw `CocoaError` | INV-1 | failure leaks a lower-layer error past the documented contract |
| flush/parent-fsync throws after the write commits | INV-1 | committed-but-unrecorded → retry duplicates; mutation not atomic |
| write succeeds, fsync fails, no rollback | INV-1 | partial bytes left on disk → retry duplicates/corrupts |
| `replay` uses `omittingEmptySubsequences` | INV-2 | interior blank line silently dropped, masking corruption |
| `replay` accepts a final record with no terminator | INV-2 | torn/uncommitted tail accepted as committed |
| envelope decode tolerates an unknown `schema_version` | INV-2 | forward/unknown version silently mis-parsed instead of rejected |

## Execution caveats

- **This IS the dd repo.** Edit `skills/adversarial-review/SKILL.md` here. Per the repo's convention
  use a `feature/`/`docs/` branch + PR; concurrent editors — check branch/clean state before any git
  op (`skills-repo-parallel-edits`); re-run `install-skills.sh` into a consumer to exercise it after.
- **Optional parallel update:** the `dd_review_runner.py` pre-PR engine already has the instinct; if
  its review prompt is templated, fold the same angle in for consistency — secondary to the skill edit.
- **Scope check before building:** if a fresh baseline reviewer *already* reliably catches these
  without the angle (control doesn't exhibit the failure), there's nothing to add — stop (writing-
  skills: no skill without a failing control). The PR-2 evidence says it won't, but re-confirm on a
  current fixture.
