# Deferred — `adversarial-review` "durability" angle (failure-path lens for source-of-truth state)

**Status: implemented 2026-06-19; moved to `completed/` 2026-06-20** alongside the paired
loop-pattern-attack plan, which has now landed. The angle is in `skills/adversarial-review/SKILL.md`;
validation (RED/GREEN + cross-language generalization + over-fire/skip controls) is in
`skill-validation/adversarial-review.md`.

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
**eight** failure-path defects across rounds 1–5 (six rounds total; round 6 came back clean), all on
one axis. Categorizing them:

| Finding | Class |
|---|---|
| open-failure leaks `CocoaError` not the documented error type | mutation failure path |
| `try!` on encode crashes the process on a pathological payload | mutation failure path |
| `replay` silently drops interior blank lines | read accepts non-committed |
| no parent-dir fsync on fresh file → dir entry not crash-durable | durability |
| parent-fsync **throws after commit** → un-advanced seq → retry duplicates | mutation not atomic |
| `replay` accepts an unterminated/torn final record | read accepts non-committed |
| content-fsync failure leaves partial bytes → retry duplicates | mutation not atomic |
| parent-fsync abandoned after one transient failure → fresh log's dir entry never durable | durability |

All eight collapse to two invariants of durable / source-of-truth state that the holistic
reviews never enumerated or tested. The reviews optimized the **happy path + spec-field fidelity**
(envelope fields, snake_case, seq contiguity when all goes well); the gate attacked the **failure /
crash / partial-state** axis — which, for a source-of-truth store (spec D2: "the log is the source
of truth; crash consistency = replay + idempotent reconciliation"), **is the primary contract, not
an edge case.** The miss was systemic (a whole unexamined axis), which is why it surfaced over repeated reactive
rounds instead of one upfront audit. An angle that names this axis turns it into a checklist the reviewer
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

- **Angle name:** `durability` — **locked** (the loop plan cross-references the angle by this name;
  `sweeping-stale-references`). The angle's *prose* (Looks-for + checklist wording) is still refined
  by the RED/GREEN; the name is not.
- **Looks for:** "failure/crash/partial-state paths of durable or source-of-truth state — durable
  mutations that aren't atomic (partial write, committed-but-unrecorded, crash on bad input, leaked
  error type, non-retry-safe) and reads that accept non-committed data (torn/partial final record,
  interior corruption, gaps, out-of-order, unknown version silently parsed)."
- **When to apply:** the artifact creates, persists, or reads durable / source-of-truth state — a
  file write, append-only log, transaction, journal, spool, or any store another component treats as
  the source of truth. (Skip for pure in-memory / stateless code.)
- **Enumerate checklist** (the lens's concrete probes — what makes it operational, mirroring how
  `executability` lists "missing definitions, ambiguous contracts"). **Layout:** a compact sub-list
  under this angle's **When to apply** entry, NOT in the one-line table row — the existing angles are
  single rows; this checklist is the new angle's distinguishing operational content:
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

1. **Use a realistically-DILUTED fixture** — a full, plausible ~160-line source-of-truth file where
   the failure-path defects are latent among correct happy-path code, so the reviewer's attention is
   diluted (the condition under which holistic actually misses them). A tight snippet is the wrong
   instrument.
2. **The load-bearing evidence is the cross-model gap**, not a single-reviewer toy result: in the
   real session, codex's blocking gate caught all eight failure-path defects across rounds 1–5 (round
   6 clean) while Claude's holistic per-task reviews AND an Opus whole-branch "ready to merge" missed
   them (the "Why this exists" table). That gap is the justification — exactly how consistency/
   executability earned their place.

### The fixture (standalone)

The fixture is the **initial Task-2.2 `EventLog`** — a real, ~160-line source-of-truth file the
holistic reviews passed, with the failure-path defects latent among correct happy-path code (the
dilution the necessity bar requires). It is inlined below so the test needs no other repo.
Provenance: `git show b0f4511:swift/Steno/Sources/Steno/Events/EventLog.swift` in the meeting-pipeline
repo (reachable from `main` via merge `c2a5403`; the `feat/rec-2-event-log` branch was deleted on merge).

This single commit carries a **representative subset** of the eight historical findings, not all of
them: the parent-dir-fsync and post-throw rollback findings appeared in *later* commits (after
`append` became throwing), so they are absent here and absent from the rubric below.

```swift
// Append-only typed event log — Decision 2, recording-slice PR 2 Task 2.2.
//
// `EventLog<Payload>` owns a single `events.jsonl` file:
//   - `append` stamps seq + ts, encodes via StenoJSON, fsyncs, returns the envelope.
//   - `replay` decodes all lines via StenoJSON and validates seq contiguity from 1.
//
// Wire conventions: StenoJSON.encoder() / .decoder() (ISO-8601 ms dates, sorted keys).
// No internal locking: single-writer-per-log is the owner's guarantee (Decision 2).
// The PR-4 engine actor serialises all appends; no lock is YAGNI here.

import Darwin
import Foundation

// MARK: - EventLogError

/// Errors thrown by `EventLog.replay()`.
public enum EventLogError: Error, Equatable {
    /// `seq` jumped — expected `expected`, found `found`. Indicates truncation or corruption.
    case seqGap(expected: Int, found: Int)
}

// MARK: - EventLog

/// Append-only typed event log backed by a newline-delimited JSON file.
///
/// One `EventEnvelope<Payload>` per line; no compaction (Decision 2: meetings are finite).
/// Create one `EventLog` per log file; do not share instances across writers.
public final class EventLog<Payload: Codable & Sendable> {
    private let url: URL
    private var nextSeq: Int = 0          // 0 = unresolved; resolved on first append/init
    private var fileHandle: FileHandle?
    private var seqResolved = false

    public init(url: URL) {
        self.url = url
    }

    deinit {
        fileHandle?.closeFile()
    }

    // MARK: - append

    /// Assigns the next `seq`, stamps `ts` at the wall clock, writes one line, fsyncs,
    /// and returns the durable envelope.
    ///
    /// Creates the file if it does not exist. Parent directory must already exist.
    @discardableResult
    public func append(
        type: String,
        meetingId: String?,
        requestId: String?,
        payload: Payload
    ) -> EventEnvelope<Payload> {
        // Resolve nextSeq on the first append (derive from file if it exists).
        if !seqResolved {
            resolveSeq()
        }

        let seq = nextSeq
        let envelope = EventEnvelope<Payload>(
            seq: seq,
            type: type,
            ts: StenoJSON.wireQuantized(Date()),
            meetingId: meetingId,
            requestId: requestId,
            schemaVersion: 1,
            payload: payload
        )

        // Encode; crash is intentional — encoding our own well-typed struct failing would
        // indicate a programmer error (non-Codable payload type slipping through).
        // swiftlint:disable:next force_try
        let lineData: Data = {
            let data = try! StenoJSON.encoder().encode(envelope)
            var d = data
            d.append(contentsOf: [0x0A]) // "\n"
            return d
        }()

        writeAndSync(lineData)
        nextSeq = seq + 1
        return envelope
    }

    // MARK: - replay

    /// Reads all lines in order, decodes via `StenoJSON.decoder()`, validates contiguous
    /// seq starting at 1, and returns the full envelope array.
    ///
    /// - Throws: `EventLogError.seqGap` on a missing or out-of-order seq.
    /// - Throws: `DecodingError` on malformed JSON or unknown `schema_version`.
    public func replay() throws -> [EventEnvelope<Payload>] {
        guard FileManager.default.fileExists(atPath: url.path) else {
            return []
        }

        let raw = try Data(contentsOf: url)
        guard !raw.isEmpty else { return [] }

        let decoder = StenoJSON.decoder()
        var results: [EventEnvelope<Payload>] = []
        var expectedSeq = 1

        // Split on newlines; skip trailing empty line.
        let lines = raw.split(separator: 0x0A, omittingEmptySubsequences: true)
        for lineData in lines {
            let envelope = try decoder.decode(EventEnvelope<Payload>.self, from: Data(lineData))
            guard envelope.seq == expectedSeq else {
                throw EventLogError.seqGap(expected: expectedSeq, found: envelope.seq)
            }
            results.append(envelope)
            expectedSeq += 1
        }
        return results
    }

    // MARK: - Private helpers

    /// Scans the existing file (if any) to determine `nextSeq`.
    /// Empty / missing → nextSeq = 1. Non-empty → nextSeq = (max seq found) + 1.
    /// Uses a lightweight line-count scan rather than a full decode to keep init cheap.
    private func resolveSeq() {
        seqResolved = true
        guard FileManager.default.fileExists(atPath: url.path),
              let raw = try? Data(contentsOf: url),
              !raw.isEmpty
        else {
            nextSeq = 1
            return
        }
        // Count non-empty lines; each corresponds to one event. seq starts at 1.
        let count = raw.split(separator: 0x0A, omittingEmptySubsequences: true).count
        nextSeq = count + 1
    }

    /// Appends `data` to the file (creating it if absent) and calls fsync(2).
    private func writeAndSync(_ data: Data) {
        if fileHandle == nil {
            openOrCreate()
        }
        guard let fh = fileHandle else {
            // Should not happen; openOrCreate() traps on failure.
            return
        }
        fh.seekToEndOfFile()
        fh.write(data)
        // fsync(2) via POSIX — the durable commit point (D2).
        // Failure (EIO, ENOSPC, …) is a fatal I/O error: the append is the source of truth
        // and acknowledging an un-fsync'd write would violate D2.
        if fsync(fh.fileDescriptor) == -1 {
            let savedErrno = errno
            fatalError("EventLog: fsync(2) failed with errno \(savedErrno): \(String(cString: strerror(savedErrno)))")
        }
    }

    /// Opens the file for appending, creating it atomically if it does not exist.
    private func openOrCreate() {
        if !FileManager.default.fileExists(atPath: url.path) {
            FileManager.default.createFile(atPath: url.path, contents: nil)
        }
        fileHandle = FileHandle(forUpdatingAtPath: url.path)
        // If we can't open the file, crash with a clear message — a write failure
        // here is a programmer error (wrong path, missing parent dir).
        guard fileHandle != nil else {
            fatalError("EventLog: cannot open file for writing at \(url.path)")
        }
    }
}
```

**Per-defect GREEN rubric** — each row is a defect ACTUALLY present in the file above, paired with the
finding the angled reviewer must produce (the baseline holistic review misses these on the diluted file):

| Defect (in the fixture above) | INV | GREEN finding the angle must elicit |
|---|---|---|
| `append`'s `try!` encode (the `lineData` closure) | INV-1 | a non-finite `Double` payload crashes the process instead of returning a typed error |
| `append` is non-`throws`; `writeAndSync` / `openOrCreate` `fatalError` on fsync / open failure | INV-1 | a transient I/O failure (ENOSPC / EIO / bad path) crashes the whole app instead of a recoverable typed error — no error contract |
| `resolveSeq` counts lines (its doc-comment claims "max seq found") and `try?` swallows a read error | INV-1 | `append` extends a gapped / corrupt log by miscounting; an unreadable file is treated as fresh and overwritten |
| `replay` splits with `omittingEmptySubsequences: true` | INV-2 | an interior blank line is silently dropped, masking corruption |
| `replay` has no trailing-`\n` (`raw.last == 0x0A`) check | INV-2 | a **complete-but-unterminated** final record (JSON bytes flushed, the trailing `\n` lost) is accepted as committed. Plant exactly that — a *truncated*-JSON tail is correctly rejected by the decoder, so the test must use a valid JSON line with no trailing newline |

The GREEN-target (fixed) behaviour is on meeting-pipeline `main`: `append throws` with a
truncate-to-pre-write-offset rollback, `replay` rejecting torn tails and interior blank lines, and
`resolveSeq` deriving `nextSeq` from a validated `replay`.

### RED / GREEN

**Modality:** a *paper / transcript review*, not a build — a reviewer READS the inlined fixture +
applies the skill and reports findings; nothing is compiled or run. So the fixture's undefined
external types (`EventEnvelope`, `StenoJSON` — obvious deps a reviewer reads past) don't matter, and
the loop plan's stub-reviewer is likewise canned text, not a live model.

1. **RED (baseline, current skill).** Fresh reviewer with the *current* `adversarial-review`
   (posture + baseline Rules + existing angles, NO durability angle) over the file above. Expect
   happy-path / spec-fidelity findings and a **miss** on the rubric's INV-1/INV-2 violations. Record
   verbatim.
2. **GREEN (with the angle).** Same reviewer + same file, skill now carrying the durability angle.
   Expect it to enumerate the mutation + read checklist and flag the rubric violations the baseline
   missed.
3. **Decision rule — this is NOT a holistic-vetoable gate.** Per the necessity bar, single-reviewer
   small-artifact discrimination under-credits this class (consistency/executability were kept on
   lens-not-in-posture + codex-gap grounds, not toy discrimination). So the angle **ships** on the
   cross-model gap (codex caught all eight; Claude's holistic + whole-branch missed them) plus the
   lens-not-in-posture argument; the RED/GREEN above is **corroborating**, not a pass/fail a strong
   holistic reviewer can veto by happening to catch a defect on this one file.
4. **Method (writing-skills "Micro-Test Wording"):** ≥5 reps per variant; always include the no-angle
   control; read every flagged match by hand (template echoes masquerade as hits).

## Execution caveats

- **This IS the dd repo.** Edit `skills/adversarial-review/SKILL.md` here. Per the repo's convention
  use a `feature/`/`docs/` branch + PR; with concurrent editors, check branch/clean state before any
  git op; re-run `install-skills.sh` into a consumer to exercise it after.
- **Optional parallel update:** the `dd_review_runner.py` pre-PR engine already has the instinct; if
  its review prompt is templated, fold the same angle in for consistency — secondary to the skill edit.
- **Scope check (takes precedence over the per-fixture RED/GREEN):** the angle is unjustified only if
  the **cross-model gap fails to reproduce** — i.e. an independent model (codex) ALSO misses these on
  a real diluted artifact. A strong holistic *Claude* reviewer also catching them on this single
  inlined file does **NOT** veto (necessity bar: small-artifact discrimination under-credits this
  class — see the Decision rule). Confirm the codex-gap, not just a failing Claude control.
