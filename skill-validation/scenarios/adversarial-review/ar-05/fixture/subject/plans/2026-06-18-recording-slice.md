# Recording-slice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: use `superpowers:subagent-driven-development`
> (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Each
> task is one `- [ ]` checkbox: write the listed tests first, watch them fail, implement,
> go green, commit. One PR per `## PR` section (the merge boundary).

**Goal:** Re-introduce the recording lifecycle scrapped in the clean-slate reset, rebuilt
as an event-sourced recording engine + bundle store on disk, exposed over HTTP / CLI / menu.

**Architecture:** Three separated state engines (app / recording / ML); this slice builds
the recording engine and the cross-engine skeleton it needs (event-log substrate,
per-meeting bundle dirs as the filesystem handoff queue, dual-sink logging). The event log
is the source of truth; state is a pure synchronous projection; the bundle dir is a derived
projection that moves between stage dirs by atomic `rename(2)`. The ML engine is a later
slice and is not built here.

**Tech Stack:** Swift 6 / SwiftPM (`swift/Steno`, library `Steno` + executable `StenoApp`),
Hummingbird HTTP, ServiceLifecycle; Python 3.12 / Typer + Rich (`python/`, `stenoctl`).

## Governing docs (re-read before each PR — Gate 1)

- Spec: `plans/specs/2026-06-18-control-plane-design.md` (D1–D12 + build order). Authoritative
  for this slice.
- Master spec: `plans/specs/2026-06-04-meeting-pipeline-design.md` (everything else; reconciled
  *after* this slice — see the closing section).
- `CLAUDE.md` (test-first, commit, dual-sink-config-example rules).
- Prior state: `plans/completed/2026-06-17-clean-slate-reset.md` (what the slate kept/scrapped).

## Global Constraints

- **Test-first, commits land green** (`CLAUDE.md` Test-Driven Changes). Swift tests under
  `swift/Steno/Tests/StenoTests/`; Python under `python/tests/`.
- **Pre-v1: no migrations, no back-compat shims.** Breaking changes are direct. `schema_version`
  bumps abandon old data rather than migrating.
- **ML processing stays local; no audio leaves the device.** This slice touches no remote service.
- **Never commit** audio, real transcripts, `config.toml`, recordings, tokens.
- **`config.toml.example` topology:** the canonical file is `python/src/steno/config.toml.example`;
  the repo-root file is a symlink to it; `swift/Steno/Sources/Steno/Resources/config.toml.example`
  is a real committed copy kept byte-identical (re-`cp` after editing canonical, or
  `test_config_example_parity.py` fails).
- **Commands:** Swift `(cd swift/Steno && swift test)` and `make -C swift/Steno app`; Python
  `uv run --directory python pytest` / `ruff check .` / `ruff format --check .` (shell stays at
  repo root).
- **Glossary (D12), applied codebase-wide:** *Engine* = state-aware lifecycle driver (reducer +
  projection, no `await` mid-transition); *Worker* = doer with no coordination state; *Service* =
  long-running resource with no domain state machine; *Orchestrator* = the app engine.

## Merge boundaries

Seven PRs, in order; each a single small PR off its predecessor. PR 0–4 are buildable without
exposing Start; PR 5 installs the recover-before-bind gate; PR 6 turns recording on.

| PR | Branch | Deliverable |
|----|--------|-------------|
| 0 | `feat/rec-0-capture-worker-rename` | `CaptureEngine` → `CaptureWorker` rename |
| 1 | `feat/rec-1-logging-dual-sink` | Swift logger → OSLog + rotating `steno-app.log` (Swift-owned) |
| 2 | `feat/rec-2-event-log` | Event envelope + append/replay log; clock lifted out of the reducer |
| 3 | `feat/rec-3-bundle-store` | `MeetingStore` → bundle store (stage dirs, atomic moves, reconcile) |
| 4 | `feat/rec-4-recording-engine` | Recording engine: events, projection, hashing, classification, recovery |
| 5 | `feat/rec-5-app-wiring` | Recover-before-bind + drain-on-shutdown in the app engine |
| 6 | `feat/rec-6-exposure` | HTTP routes + `stenoctl record` + menu Start/Stop + StatusStore |

---

## PR 0: Rename `CaptureEngine` → `CaptureWorker`

**Goal:** Mechanical glossary-consistency rename. A worker by D12; no functional change.
One observable change, by design: the capture log event IDs are renamed to match
(`capture_engine_started`/`stopped` → `capture_worker_*`). Leaving them `engine_*` would
re-introduce the half-rename this cleanup removes; there is no consumer yet (Swift logs go to
OSLog; the greppable file sink lands in PR 1), so nothing breaks. Any future log-grep tooling
uses the new IDs.

**Files:**
- Rename: `swift/Steno/Sources/Steno/Capture/CaptureEngine.swift` → `CaptureWorker.swift`
- Rename: `swift/Steno/Tests/StenoTests/CaptureEngineTests.swift` → `CaptureWorkerTests.swift`
- Modify (references): `swift/Steno/Tests/StenoTests/{M4AFixture,AudioIntegrityTests,SilenceMeterTests}.swift`
- Modify (comment refs only — Gate 4): `Capture/{CaptureSource,SilenceMeter}.swift`,
  `Permissions/PermissionCoordinator.swift`, `StenoApp/SCKCaptureSource.swift`, `Config/Config.swift`
  all name `CaptureEngine` in comments.
- Keep (not engine-named): `CaptureSource` (the type), `CaptureStopOutcome`, `CaptureChannel`,
  `CaptureBufferHandler`, `UnexpectedStopReporting`.

- [x] **Task 0.1 — Rename the type and its symbols, keep tests green.**
  - Rename class `CaptureEngine` → `CaptureWorker` and error enum `CaptureEngineError` →
    `CaptureWorkerError` (the only two `Engine`-named symbols; `CaptureStopOutcome` /
    `CaptureChannel` stay). Rename both files. Update all references in the three test files +
    `M4AFixture`, and sweep the comment refs in the five sources listed above.
  - This is a pure rename — no behavior change, so the existing `CaptureWorkerTests` (renamed)
    are the test coverage; they must stay green unchanged except for the type name.
  - Done when: `(cd swift/Steno && swift test)` green; `grep -rn CaptureEngine swift/Steno`
    returns nothing (code **and** comments).
  - **`References swept:`** `CaptureEngine` in CaptureSource, SilenceMeter, PermissionCoordinator,
    SCKCaptureSource, Config (comments).
  - Commit: `refactor(capture): rename CaptureEngine → CaptureWorker (glossary D12)`.

---

## PR 1: Logging dual-sink (OSLog + rotating file)

**Goal (D8):** `StenoLog` writes every event to OSLog **and** appends the same greppable line to
Swift's own rotating `~/Library/Logs/steno/steno-app.log` (Python writes a sibling `steno.log` —
each process owns its file, no cross-process sharing), so host-smokes can grep Swift events via
`~/Library/Logs/steno/*.log`. Observability only — not the typed event store.

**Files:**
- Create: `swift/Steno/Sources/Steno/Logging/RotatingFileSink.swift`
- Modify: `swift/Steno/Sources/Steno/Logging/Logger.swift` (add a file sink alongside OSLog)
- Modify: `swift/Steno/Sources/StenoApp/StenoApp.swift` (configure the sink at launch with
  `ResolvedPaths.logsRoot / "steno-app.log"`)
- Test: `swift/Steno/Tests/StenoTests/RotatingFileSinkTests.swift`,
  `swift/Steno/Tests/StenoTests/LoggerFormatTests.swift` (extend)

**Interfaces:**
- Consumes: `StenoLog.formatEvent(_:requestId:fields:)` (existing — the greppable line format
  stays the canonical Swift log line); `ResolvedPaths.logsRoot` (URL).
- Produces: `StenoLog.configure(logFile: URL)` — installs the sink (idempotent); until called,
  `StenoLog` is OSLog-only (so tests that don't configure write no file). Matches Python's rotation
  defaults (10 MB, 5 backups).

- [x] **Task 1.1 — Rotating file sink.**
  - A thread-safe append-only file sink: opens/creates the file, appends a line per call under a
    serial lock (callers are off many isolation domains), rotates by size (rename `steno-app.log` →
    `steno-app.log.1`, shift backups, cap at 5) when the next write would exceed 10 MB. Creates the
    parent dir if missing (0700).
  - Tests required: appends a line and reads it back; concurrent appends from many tasks all land
    (no interleaved/truncated lines); rotation fires after the byte cap and caps backup count;
    missing parent dir is created.
  - **Rationale (`writing-explicit-rationale`):** Swift owns `steno-app.log` exclusively; Python's
    `structlog` writes a sibling `steno.log`. **Separate files, not one shared `steno.log`** — two
    processes independently writing *and* size-rotating one file is irreducibly racy (atomic append,
    stale handle on external rotation, rotation ownership — four pre-PR review findings). Separate
    files give the same greppable outcome (grep `~/Library/Logs/steno/*.log`) with none of the
    cross-process hazards. Settled 2026-06-18; spec D8 amended (was a shared `steno.log`). The sink's
    `NSLock` is intra-process only (callers span many isolation domains). Document in the header comment.
  - Commit: `feat(logging): rotating file sink for the Swift log`.

- [x] **Task 1.2 — Dual-sink wiring in `StenoLog`.**
  - `StenoLog.event(...)` keeps the OSLog call and, when configured, also writes
    `formatEvent(...)` + newline to the sink. Add `StenoLog.configure(logFile:)`; unconfigured =
    OSLog-only.
  - Tests required: after `configure`, an event lands in the file as the exact `formatEvent` line (+
    newline); without `configure`, no file is written; `configure` is idempotent (second call is a
    no-op, does not duplicate lines); a `requestId` flows through to the file line; the OSLog line
    format is unchanged (existing `LoggerFormatTests` stay green).
  - Commit: `feat(logging): dual-sink StenoLog (OSLog + file)`.

- [x] **Task 1.3 — Configure at launch + host-smoke.**
  - In `StenoApp` startup call (before other services start):
    ```swift
    try? StenoLog.configure(logFile: paths.logsRoot.appendingPathComponent("steno-app.log"))
    ```
    Use `try?`: a failure to open the log file (rare, e.g. permission denial on the logs dir) is
    non-fatal — the app continues OSLog-only, and `StenoLog.configure` is idempotent so retry is
    safe on a later launch.
  - No new unit test (composition wiring); covered by host-smoke.
  - Host-smoke (record in commit `Verification:`): `make -C swift/Steno app` → `stenoctl app start`
    → `grep event=app_launched ~/Library/Logs/steno/steno-app.log` (expect one line in logfmt format,
    e.g. `event=app_launched`) → `stenoctl app stop`. Confirms Swift events reach the file.
  - Commit: `feat(logging): configure dual-sink at app launch`.

---

## PR 2: Event-log substrate

**Goal (D2/D9):** A generic durable append-only typed log (`events.jsonl`) and the reducer reshaped
into a pure fold by lifting the clock out. The log is the source of truth; replay rebuilds state.
No recording-specific events yet — those land in PR 4.

**Files:**
- Create: `swift/Steno/Sources/Steno/Events/EventEnvelope.swift`
- Create: `swift/Steno/Sources/Steno/Events/EventLog.swift`
- Modify: `swift/Steno/Sources/Steno/Meetings/MeetingTransition.swift` (lift `Date()` → param)
- Test: `swift/Steno/Tests/StenoTests/EventEnvelopeTests.swift`,
  `EventLogTests.swift`, and extend `MeetingTransitionTests.swift`

**Interfaces:**
- Produces:
  - `EventEnvelope<Payload>` — fields per D9: `seq: Int`, `type: String`, `ts: Date`,
    `meetingId: String?`, `requestId: String?`, `schemaVersion: Int`, `payload: Payload`. One JSON
    object per line; wire conventions match existing `WireEncodable`/`StenoJSON` (snake_case keys,
    ISO-8601 `ts`). `Payload: Codable & Sendable` carrying its own `type` tag for decode dispatch.
  - `EventLog<Payload>` over a file URL: `append(type:meetingId:requestId:payload:) -> EventEnvelope`
    (assigns the next `seq`, writes one line, **fsyncs**, returns the stamped envelope) and
    `replay() throws -> [EventEnvelope<Payload>]`.
  - `MeetingTransition.transition(_:to:applying:at: Date)` — the existing reducer with an explicit
    `Date` parameter replacing the internal `Date()` at `MeetingTransition.swift:154`
    (`let nowMs = StenoJSON.wireQuantized(Date())`). The caller passes `event.ts`; quantize it with
    the same `StenoJSON.wireQuantized` so `updatedAt` keeps its existing wire precision.
- Note: `seq` is per-log monotonic starting at 1; single writer per log, so no event UUID (D9).

- [x] **Task 2.1 — Event envelope.**
  - Codable envelope with the D9 fields; one compact JSON line; `ts` ISO-8601; snake_case keys.
    Decode dispatches the payload by `type`.
  - Tests required: round-trips all fields including optional `meeting_id`/`request_id` absent vs
    present; `ts` round-trips exactly under the quantization the codebase already uses; an unknown
    `schema_version` is surfaced as a decode error (loud), not silently parsed.
  - Commit: `feat(events): typed event envelope (D9)`.

- [x] **Task 2.2 — Append-only log with replay.**
  - `append` assigns the next `seq`, writes the envelope as one line, fsyncs, returns it. `replay`
    reads all lines in order and decodes them.
  - Tests required: append-then-replay yields identical envelopes in order (determinism);
    `seq` is contiguous from 1 and a gap/out-of-order `seq` on replay is rejected (truncation
    detection); replay of a line with an unknown `schema_version` throws; appending to a fresh
    (nonexistent) path creates it.
  - Commit: `feat(events): append-only event log with replay (D2)`.

- [ ] **Task 2.3 — Lift the clock out of the reducer.**
  - Add an explicit timestamp parameter to `transition(...)`; remove the internal `Date()`. The
    event will supply `ts` (PR 4). Legal-moves table + required-fields map + states all unchanged.
  - Tests required: a determinism test — identical `(meeting, target, update, at:)` produces a
    byte-identical result on repeat. Update the two existing time-dependent tests
    (`test_updatedAt_refreshed_isLaterThanInput`, `test_updatedAt_roundTripsExactlyAfterEncodeDecode`)
    to pass an explicit time; all other `MeetingTransitionTests` stay green.
  - Commit: `refactor(meetings): lift clock out of the reducer for replay determinism (D2)`.

---

## PR 3: Bundle store

**Goal (D4/D5/D6):** Reshape `MeetingStore` from flat `<id>.meta.json` to a per-meeting **bundle
dir** under `~/Documents/steno-recordings/<stage>/<id>/`, where the stage dir name *is* the status.
A status change is an atomic `rename(2)` of the dir; reconciliation converges the filesystem to the
log idempotently.

**Files:**
- Modify (largely rewrite): `swift/Steno/Sources/Steno/Meetings/MeetingStore.swift` — including its
  header docstring (Gate 4: it still describes the flat `<id>.meta.json` model + cites the completed
  step-9 spec; rewrite to the bundle-dir model).
- Delete: `swift/Steno/Sources/Steno/Recording/FilenameTemplate.swift` +
  `swift/Steno/Tests/StenoTests/FilenameTemplateTests.swift` (dead — no caller in `Sources`;
  bundle audio is the fixed `audio.m4a`)
- Test (rewrite against the bundle contract): `swift/Steno/Tests/StenoTests/MeetingStoreTests.swift`

**Interfaces:**
- Consumes: `ResolvedPaths.documentsRoot` (the recordings root); `MeetingID` (the dir name is the
  validated id); the `Meeting` projection + `StenoJSON` writer.
- Produces (bundle store API; supersedes the flat-path methods):
  - `init(root: URL)` — `root` is `documentsRoot`; stage parents are `root/<status>/`.
  - `createBundle(id:status:) async throws -> URL` — make `root/<status>/<id>/` (the bundle is
    created **directly in its stage**, normally `recording/`) and return it. The engine then commits
    `recording.started` into it; the append+fsync is the commit point (ARCHITECTURE.md:48), not the
    `mkdir`. A crash between `mkdir` and that commit leaves an empty scaffold recovery removes
    (Task 4.8) — no staging indirection.
  - `bundleURL(id:status:) -> URL` and `audioURL(id:status:) -> URL` (the fixed `<bundle>/audio.m4a`).
  - `writeMeeting(_ meeting: Meeting) async throws` — rewrite `meeting.json` **in place** in the
    bundle's current-status dir (step 2 of the D6 ordering; no move).
  - `moveBundle(id:from:to:) async throws` — atomic `rename(2)` of the dir to the new-status parent
    (step 3 of the D6 ordering — stage→stage transitions of an already-live bundle).
  - `read(id:) async throws -> Meeting` — locate the bundle across stage dirs, decode `meeting.json`.
  - `list(status:) async throws -> [Meeting]` — meetings under one stage parent.
  - `findActiveRecording() async throws -> Meeting?` — single dir under `recording/` (D10 invariant).
  - `reconcile(id:to:) async throws` — idempotently converge: ensure `meeting.json` is current and
    the dir sits under the `to` stage parent, wherever it currently is.
  - `removeEmptyScaffold(id:) async throws` — remove a `recording/<id>/` whose `events.jsonl` is
    empty/missing **and** which has no `audio.m4a` (a pre-commit crash scaffold). The only removal the
    store performs: not a bundle (no committed event), no audio — so it is **not** the deletion the
    audio-preservation rule governs. Refuses to remove a dir that has any committed event or an audio
    file.
  - `StoreError` keeps `alreadyExists` / `notFound` / `invalidId`.

- [ ] **Task 3.1 — Bundle layout: create-in-place + read.**
  - `createBundle(id, status)` makes `root/<status>/<id>/` directly and returns it. `writeMeeting`
    writes `meeting.json` atomically (keep the existing temp-write-then-rename file atomicity) into
    the bundle's current dir. `read` finds the bundle by scanning stage parents for `<id>/`.
    Path-guard the id (reuse the existing `invalidId` checks — no `/`, no `..`, non-empty) so the dir
    name can't escape the root.
  - Tests required: `createBundle(id, status: recording)` makes `root/recording/<id>/`; read
    round-trips a fully and a minimally populated meeting; create collision (dir exists) throws
    `alreadyExists`; an id with `/` or `..` throws `invalidId`; read of a missing id throws
    `notFound`.
  - Commit: `feat(meetings): create-in-place bundle layout (D5)`.

- [ ] **Task 3.2 — In-place write + atomic stage move + list/findActiveRecording.**
  - `writeMeeting` rewrites `meeting.json` in the current dir; `moveBundle` is a single dir
    `rename(2)` to the new stage parent (creating the parent if absent). `list(status:)` enumerates a
    stage parent; `findActiveRecording` returns the single `recording/` bundle.
  - Tests required: move relocates the whole dir (audio + meeting.json + events.jsonl travel
    together) and is observable as atomic (no half-moved state); `list` returns only the requested
    stage; `findActiveRecording` returns nil on empty, the one bundle when present; an
    unparseable `meeting.json` is skipped by `list` and left on disk.
  - Commit: `feat(meetings): in-place write + atomic stage move (D6)`.

- [ ] **Task 3.3 — Idempotent reconciliation + empty-scaffold removal.**
  - `reconcile(id:to:)` converges the filesystem to an intended status: rewrite `meeting.json`, then
    move the dir to the `to` parent if it isn't already there. Running it twice is a no-op.
    `removeEmptyScaffold(id)` removes a `recording/<id>/` with an empty/missing `events.jsonl` and no
    `audio.m4a`; it refuses (throws) if any committed event or an audio file is present.
  - Tests required: a bundle stranded in the old-status dir (simulating a crash between event-append
    and dir-move, D6 window) is moved to the logged stage; reconcile is idempotent (second call
    changes nothing); reconcile of a bundle already in the right place is a no-op;
    `removeEmptyScaffold` removes an empty no-audio scaffold and **refuses** one that has a committed
    `events.jsonl` or an `audio.m4a` (guard against deleting a real bundle).
  - Commit: `feat(meetings): idempotent reconciliation + empty-scaffold removal (D2/D6)`.

- [ ] **Task 3.4 — Retire `FilenameTemplate`.**
  - Confirm no caller in `Sources` (only the unrelated `validateFilenameTemplate` config check
    remains — leave it; see rationale). Delete `FilenameTemplate.swift` + its tests.
  - **Rationale (on-page, `writing-explicit-rationale`):** the bundle's audio path is a fixed
    `audio.m4a`, so the template type is dead. The `audio.filename_template` *config key* and its
    Swift↔Python lockstep validator (`ConfigLoader.validateFilenameTemplate`) are now unused too,
    but removing them is a cross-language change deferred to the master-spec reconciliation — out of
    scope for this slice to keep the PR small.
  - Done when: `grep -rn FilenameTemplate swift/Steno/Sources` returns only the
    `validateFilenameTemplate` config lines; `swift test` green.
  - Commit: `refactor(recording): retire dead FilenameTemplate (fixed audio.m4a) (D5)`.

---

## PR 4: Recording engine

**Goal (D7/D10):** The recording engine — single-active state, drives the capture worker, the stop
join point, event emission + projection + side-effects + hashing + outcome classification, **and**
the startup recovery-reconcile routine. Engine tests stub the capture worker at its `CaptureSource`
seam.

**Files:**
- Modify: `swift/Steno/Sources/Steno/Meetings/Meeting.swift` (`MeetingStatus` += `partial`,
  `discarded`) + `swift/Steno/Sources/Steno/Meetings/MeetingTransition.swift` (legal-moves +
  required-fields); see Task 4.2.
- Create: `swift/Steno/Sources/Steno/Recording/RecordingEvent.swift` (the 7-event enum + payloads + fold)
- Create: `swift/Steno/Sources/Steno/Recording/RecordingClassification.swift` (pure outcome fn)
- Create: `swift/Steno/Sources/Steno/Recording/RecordingHash.swift` (SHA-256 + size)
- Create: `swift/Steno/Sources/Steno/Recording/RecordingEngine.swift` (the engine + recovery)
- Modify: Swift `Config.RecordingConfig` + `ConfigLoader`; Python `RecordingConfig`;
  `config.toml.example` (+ swift resource copy); see Task 4.1.
- Test: extend `MeetingTransitionTests.swift`; `RecordingEventTests.swift`,
  `RecordingClassificationTests.swift`, `RecordingHashTests.swift`, `RecordingEngineTests.swift`,
  `RecordingRecoveryTests.swift`; Python `test_config_loader.py` (extend)

**Interfaces:**
- Consumes: `CaptureWorker` (PR 0) built on an injected `CaptureSource` (the stub seam);
  `EventLog` (PR 2); bundle store (PR 3); `AudioIntegrity.assessAudioIntegrity(at:)`;
  the extended `MeetingStatus` + legal-moves table (Task 4.2); `MeetingTransition.transition(...,at:)`;
  `recording.min_duration_seconds` (Task 4.1).
- Produces:
  - `RecordingEvent` — enum of the 7 D7 types with payloads:
    `started(meetingId, kind, title?, actualStart, audioPath)`, `stopped(actualEnd, cause)`,
    `hashed(sha256, byteSize)`, `completed`, `partial`, `failed(ErrorInstance)`, `discarded`.
    Conforms to the PR-2 payload protocol (`type` tag + `schemaVersion`). `cause` ∈
    `clean | writer_error | source_died | crash_recovered`. **`started` carries `audioPath`** so the
    fold can populate `Meeting.audioPath` — `recorded`/`partial` require it, and the pure fold sees
    only the event.
  - **Projection = seed the first event, then fold the rest — purely from `events.jsonl`, no
    unlogged Meeting.** A meeting log's first event is always `recording.started`.
    - `seed(from started: RecordingEvent, at ts: Date) -> Meeting` — the **bootstrap**: constructs
      the initial `Meeting` directly at status `recording` from the `started` payload (meetingId,
      kind, title?, `actual.start` → open `actual`, `audioPath`), `createdAt = updatedAt = ts`,
      empty attendees / nil organizer. There is **no** pre-record `pending` Meeting in the
      recording-first build, so `started` does **not** go through `transition` (it has no
      from-state) — it seeds. This is what keeps replay purely log-derived: no constructor conjures
      an unlogged Meeting just to fold into.
    - `apply(_ event: RecordingEvent, to: Meeting) -> Meeting` — folds every **subsequent** event,
      two paths:
      - **Status-changing** (`completed`→`recorded`, `partial`→`partial`, `failed`→`failed` (sets
        `errors: [errorInstance]`), `discarded`→`discarded`): call `transition(meeting, to: target,
        applying: update, at: event.ts)`.
      - **Non-status-changing** (`stopped`, `hashed`): the reducer has **no self-loops**
        (`recording→recording` is illegal), so these do **not** call `transition` — direct field
        merge: `stopped` closes `actual` (sets `actual.end`); `hashed` touches no `Meeting` field
        (digest is log-only); both refresh `updatedAt = event.ts`.
    - `project(events)` = `seed(events[0])` then `apply`-fold `events[1...]`. Replay rebuilds state
      purely from the log; a log whose first event isn't `recording.started` is invalid (reject loud).
  - `classifyOutcome(integrity:durationSeconds:minDurationSeconds:cause:) -> RecordingOutcome`
    where `RecordingOutcome ∈ {recorded, partial, discarded, failed}` (pure). `durationSeconds` is the
    audio's **measured** duration (the value `AudioIntegrity` reads from the asset), used consistently
    by both the live stop and recovery.
  - `RecordingEngine` (actor): `start(title:requestId:) async throws -> Meeting`,
    `stop(requestId:) async throws -> Meeting`, `drain() async`, `recover() async`.

- [ ] **Task 4.1 — `recording.min_duration_seconds` config key.**
  - Add `min_duration_seconds: float = 30.0` to Python `RecordingConfig`; `minDurationSeconds:
    Double = 30` to Swift `RecordingConfig` + parse it in `ConfigLoader`. Add `min_duration_seconds = 30`
    under `[recording]` in the canonical `config.toml.example`; re-`cp` to the swift resource copy.
    Add a commented `# junk_age_days` placeholder under `[retention]` (reserved — see rationale).
  - **Rationale (on-page):** `junk_age_days` is reserved by D7 but its purge mechanism is the later
    retention step; ship it as a commented example line for discoverability, *not* a live schema
    field, to avoid dead config nothing reads.
  - Tests required (Python): loads the default 30.0 and a file override. Update Swift
    `test_config_wire_carries_audio_and_recording_sections` and `test_config_example_parity` for the
    new key.
  - **Gate 4 — `References swept:`** the key in: Python `RecordingConfig`, Swift `RecordingConfig`,
    Swift `ConfigLoader`, canonical example, swift resource copy, parity test.
  - Commit: `feat(config): recording.min_duration_seconds (default 30) (D7)`.

- [ ] **Task 4.2 — Extend the state machine with `partial` + `discarded`.**
  - Add `partial` + `discarded` to `MeetingStatus` (Meeting.swift). Extend the legal-moves table
    (MeetingTransition.swift) with `recording → partial`, `recording → discarded`, and
    `partial → recorded` (the promote path; `discarded` is terminal). Add required-fields
    `partial → [audio_path, actual]` and `discarded → [audio_path, actual]` (both are usable audio
    with a closed window) — the existing key-handler `switch` already covers `audio_path`/`actual`,
    so no new key case is needed.
  - Audit for exhaustive `switch`es over `MeetingStatus` that the two new cases would break (the wire
    encode is `rawValue`-based, not a switch; confirm none elsewhere).
  - Tests required: the three new moves are accepted; `recording → discarded`/`partial` reject when
    `audio_path` or `actual` is missing; the existing illegal-pairs test is regenerated for the now
    13-value enum (full complement); `discarded` has no outgoing legal move.
  - Commit: `feat(meetings): add partial + discarded statuses + moves (D7)`.

- [ ] **Task 4.3 — Recording events + projection (seed + fold).**
  - The 7-event enum + payloads (Interfaces above); the `seed(from started, at ts)` bootstrap
    constructor (builds the initial `Meeting` at `recording` from the `started` payload — no prior
    Meeting); the **two-path** `apply` fold for subsequent events (status-changing via
    `transition(...,at: event.ts)`; `stopped`/`hashed` via direct field merge); and
    `project(events) = seed(events[0]) + apply-fold(events[1...])`.
  - Tests required: `seed` builds a `recording` Meeting from `started` with `audioPath` + open
    `actual` + `createdAt == updatedAt == started.ts`, **without** any pre-existing Meeting;
    `project` over a full event sequence rebuilds the expected Meeting purely from the log
    (replay determinism: same events → identical Meeting); a log whose first event isn't
    `recording.started` is rejected; `completed`→`recorded`, `partial`→`partial`, `failed`→`failed`
    (with `errors`), `discarded`→`discarded`; `stopped` closes `actual` **without** a status change;
    `hashed` changes only `updatedAt`; `completed` after `started`+`stopped` satisfies the `recorded`
    required-fields; an illegal implied transition is rejected by the reducer.
  - Commit: `feat(recording): event set + seed/fold projection (D7)`.

- [ ] **Task 4.4 — Outcome classification (pure).**
  - `classifyOutcome` per the D7 order. Below-min beats clean; unusable wins outright.
  - Test table (every row a test case):

    | integrity | duration vs min | cause | → outcome |
    |---|---|---|---|
    | unparseable | any | any | `failed` |
    | intact | `< min` | clean | `discarded` |
    | intact | `< min` | writer_error | `discarded` |
    | intact | `≥ min` | clean | `recorded` |
    | intact | `≥ min` | writer_error | `partial` |
    | intact | `≥ min` | source_died | `partial` |
    | intact | `≥ min` | crash_recovered | `partial` |
    | intact | `≥ min`, min = 0 (disabled) | clean | `recorded` |

  - Commit: `feat(recording): outcome classification (D7)`.

- [ ] **Task 4.5 — Integrity hash event.**
  - `RecordingHash`: SHA-256 hex digest + byte size of a file → a `hashed` payload.
  - Tests required: known bytes → known digest + size; a missing file surfaces an error (caller
    decides — hashing only runs on retained paths).
  - Commit: `feat(recording): SHA-256 integrity hash (D4)`.

- [ ] **Task 4.6 — Engine start (single-active, create-in-place).**
  - `start`, in the universal commit order (ARCHITECTURE.md:48): enforce single-active → mint an
    `adhoc-` id → `createBundle(id, status: .recording)` (makes `recording/<id>/` directly) → append
    `recording.started` to `recording/<id>/events.jsonl` and **fsync — this is the commit**, carrying
    the `recording/<id>/audio.m4a` path → **seed** the projection from that event (the bootstrap,
    Task 4.3) → `writeMeeting` → start the capture worker writing that `audio.m4a`.
  - **Crash-safety (rationale, `writing-explicit-rationale`):** the `mkdir` is not the commit; the
    `recording.started` fsync is (D2/ARCH:48). A crash between `mkdir` and that fsync leaves an empty
    `recording/<id>/` scaffold — no committed event, no audio (capture starts only after the commit) —
    which recovery removes (Task 4.8). A crash after the fsync leaves a committed bundle recovery
    classifies. So `recording/` never holds an *un-handled* orphan, and a committed event is never
    deleted. (We rejected a `.staging/`+publish layer: it added a window where a committed event sat
    unpublished and a blind staging-sweep could delete it — removing the layer is the fix, not adding
    triage to it.)
  - **Single-active mechanism:** the engine (an `actor`, so calls serialize) holds the active
    recording in its in-memory projection; `start` rejects when one is already active. Recovery
    (PR 5) runs before the engine goes live and clears every `recording/` orphan (classify or remove
    the empty scaffold), and Start isn't exposed until PR 6 — so no `start` ever races recovery or a
    second `start`.
  - Tests required (stub `CaptureSource`): a successful `start` leaves `recording/<id>/` with
    `events.jsonl` (started, carrying `audioPath`) + `meeting.json`, projection `recording`; the
    `recording.started` fsync happens before capture starts (assert the committed event exists at the
    moment the worker is handed its URL); a second start while active is rejected (single-active); the
    worker is handed the `recording/<id>/audio.m4a` path.
  - Commit: `feat(recording): engine start + single-active + create-in-place (D2/D7/D10)`.

- [ ] **Task 4.7 — Engine stop join point (the four outcomes).**
  - `stop`: stop the worker (the single join point all triggers funnel through), append
    `recording.stopped` with the cause derived from `CaptureStopOutcome`/the failure callback
    (`clean`→clean, `writerError`→writer_error, unexpected-stop→source_died), assess integrity +
    measured duration, `classifyOutcome`, append `recording.hashed` on the retained paths
    (`recorded`/`partial`) only, append the terminal event, then per D6 ordering rewrite
    `meeting.json` and `moveBundle` to the outcome stage.
  - Tests required (stub worker driven to each end-state): clean ≥min → `recorded` with a `hashed`
    event present; interrupted ≥min → `partial` with `hashed`; usable <min → `discarded` with **no**
    `hashed`; unusable → `failed` with **no** `hashed` and an `ErrorInstance` appended; the bundle
    ends under the matching stage dir; the `hashed` digest re-verifies against a re-hash of the file.
  - Commit: `feat(recording): stop join point + four outcomes + hashing gate (D4/D7)`.

- [ ] **Task 4.8 — Startup recovery-reconcile.**
  - `recover`: for each dir under `recording/`, replay `events.jsonl`:
    - **empty/missing log** (a pre-commit crash between `mkdir` and the `recording.started` fsync) →
      `removeEmptyScaffold(id)` (it has no audio — capture starts only after the commit). This is the
      one case that closes the Codex P2: the scaffold is removed, never published, and there is no
      committed event to lose.
    - **log reached a terminal event** → **honor it** (reconcile dir + `meeting.json`; no reclassify).
    - **otherwise** (mid-flight, ≥1 committed event) → classify by the **logged stop cause** (the
      `recording.stopped` cause, or `crash_recovered` if the last event is `started`), write the
      catch-up events (incl. `hashed` on retained paths), and move the dir. `actual.end` = the logged
      `stopped` value, else `actual.start` + measured audio duration.
  - After the scan `recording/` holds no un-reconciled orphan and no empty scaffold. Recovery
    finalizes, never resumes (one session = one bundle). `removeEmptyScaffold` refuses any dir with a
    committed event or audio, so a committed bundle can never be deleted (the P2 hazard the rejected
    staging approach reintroduced).
  - Test table (each row: a planted `recording/<id>/` → expected outcome):

    | planted state | audio | → result |
    |---|---|---|
    | empty/missing `events.jsonl` (pre-commit scaffold) | none | removed (not a bundle) |
    | empty `events.jsonl` **but** an `audio.m4a` present | present | **refused** — left in place + logged (guard: never delete audio) |
    | terminal `completed` already logged | intact | `recorded` (honored, not reclassified) |
    | terminal `failed` already logged | unparseable | `failed` (honored) |
    | `stopped(clean)`, no terminal | intact ≥min | `recorded` (clean not downgraded) |
    | `stopped(clean)`, no terminal | intact <min | `discarded` |
    | `stopped(writer_error)`, no terminal | intact ≥min | `partial` |
    | only `started` (no `stopped`) | intact ≥min | `partial` (cause `crash_recovered`) |
    | only `started` | unparseable | `failed` |

  - Also required: idempotent (re-running `recover` after it completes is a no-op); after recovery,
    `findActiveRecording` returns nil.
  - Commit: `feat(recording): startup recovery-reconcile (D10)`.

---

## PR 5: App-engine wiring (recover-before-bind + drain)

**Goal (D10/D12):** The app engine constructs the recording engine and runs `recover()` **before the
HTTP server binds**, and drains any active recording on shutdown. Lands before Start is exposed (PR 6)
so the invariant holds the moment recording becomes possible. Keep the lifecycle-attach surface
minimal — not a framework.

**Files:**
- Modify: `swift/Steno/Sources/StenoApp/StenoApp.swift` (composition root: construct engine, call
  `recover()` before `bridge.start(services: [server])`, drain on terminate)
- Modify: `swift/Steno/Sources/Steno/Lifecycle/LifecycleBridge.swift` only if a minimal drain hook is
  needed (see rationale)
- Test: `swift/Steno/Tests/StenoTests/AppWiringTests.swift` (ordering via spies),
  extend `LifecycleBridgeTests.swift` if the bridge changes

**Interfaces:**
- Consumes: `RecordingEngine.recover()` / `.drain()` (PR 4); `LifecycleBridge.start/triggerShutdown/
  waitUntilStopped` (existing).
- Produces: a composition root that (1) builds the event log + bundle store + recording engine,
  (2) `await engine.recover()`, (3) `await bridge.start(services: [server])`, (4) on terminate
  `await engine.drain()` (bounded ~10 s) then drains services.

- [ ] **Task 5.1 — Recover before bind.**
  - Wire `await engine.recover()` ahead of `bridge.start(...)` in the launch sequence. `stenoctl app
    start`'s `/health` poll absorbs the brief delay.
  - Tests required: a composition test (inject a spy engine + spy server) asserts `recover()`
    completes before the server is started/bound — ordering, not timing.
  - Commit: `feat(app): run recording recovery before the server binds (D10)`.

- [ ] **Task 5.2 — Drain on shutdown.**
  - On terminate, broadcast shutdown → `engine.drain()` runs the same stop join point on any active
    recording, bounded ~10 s: sealed in time → classified normally (D7); timed out → left in
    `recording/` for next-launch recovery. Log-don't-block.
  - **Rationale (on-page):** D12's full managed-resource hook/listener surface is design intent with
    implementation deferred; this slice adds only the single drain step the recording engine needs,
    not a general registration framework (Principle 7 — build to the requirement).
  - Tests required (spy/stub engine): on shutdown the active recording is drained to a terminal
    outcome; a drain that exceeds the bound leaves the bundle in `recording/` and shutdown still
    completes.
  - Commit: `feat(app): drain active recording on shutdown (D10)`.

- [ ] **Task 5.3 — Host-smoke the gate.**
  - Plant a `recording/<id>/` orphan, `make -C swift/Steno app` → `stenoctl app start`; confirm the
    orphan is reconciled out of `recording/` (into `partial`/`recorded`/etc.) at launch, before
    `/health` answers. Record in commit `Verification:`.
  - Commit: `test(app): host-smoke recover-before-bind`.

---

## PR 6: Exposure (HTTP + CLI + menu + StatusStore)

**Goal (D11):** Turn recording on. Re-introduce `POST /recordings` + `/recordings/<id>/stop` driving
the engine, `stenoctl record start|stop`, menu Start/Stop, and StatusStore writes — all behind the
PR-5 recovery gate, funnelling to the engine's single start/stop join point.

**Resolved spec ambiguity (Principle 3 — decided with Simon, 2026-06-18):** D11 says the menu and CLI
"call these same routes — one join point behind the HTTP layer." Read literally that's an HTTP
round-trip for the in-process menu too. **Decision: the `RecordingEngine` is the single join point;
the in-process menu calls it directly, the out-of-process CLI reaches it over HTTP.** The HTTP
handler is a thin adapter over the same engine method, so behavioral uniformity (single-active,
validation, events) is guaranteed at the engine — routing the menu through HTTP would add no
uniformity and would re-introduce a loopback-IPC hop inside the single-process app the 2026-06-04
pivot exists to avoid (plus couple the menu to server-bind ordering). No logic is duplicated.

**Files:**
- Modify: `swift/Steno/Sources/Steno/HTTP/Server.swift` (inject the engine; add the two routes),
  `swift/Steno/Sources/Steno/HTTP/WireResponses.swift` (response + `detail`-error shapes)
- Modify: `swift/Steno/Sources/Steno/Recording/RecordingEngine.swift` (write StatusStore on start/stop)
- Modify: `swift/Steno/Sources/StenoApp/StatusItemController.swift` (menu Start/Stop → engine)
- Modify: `swift/Steno/Sources/StenoApp/StenoApp.swift` (pass engine to server + menu)
- Create: `python/src/steno/cli/commands/record_cmd.py`; modify `python/src/steno/cli/main.py`,
  `python/src/steno/cli/client.py` (re-add `start_recording`/`stop_recording` on `_post`)
- Test: extend `HTTPServerTests.swift`, `RecordingEngineTests.swift` (StatusStore), add
  `StatusItemControllerTests` for the menu actions; Python `python/tests/unit/test_cli_record.py`

**Interfaces:**
- Consumes: `RecordingEngine.start/stop` (PR 4); `StatusStore.update(_:)` (existing);
  the `client._post` transport (kept through the reset).
- Produces (wire, D11):
  - `POST /recordings` body `{title?}` → `{meeting_id, status, audio_path}`; **409**
    `{detail: "already_recording", active_meeting_id}`; **400** `{detail: "invalid_request_body"}`.
  - `POST /recordings/<id>/stop` (`?force=` accepted, no-op v1) → `{meeting_id, status,
    duration_seconds, audio_path}`; **409** `{detail: "no_active_recording"}`; **404**
    `{detail: "meeting_not_found"}` when `<id>` ≠ active. (D11 also lists a `recording_busy` 409 —
    **deferred**, see Task 6.2 rationale.)
  - `stenoctl record start [--title] | stop` (CLI resolves the active id via `/status` — Task 6.5).

- [ ] **Task 6.1 — `POST /recordings` (start).**
  - Inject the engine into `StenoServer.buildRouter`/`buildApplication` (mirror the pre-reset
    `recording:` injection the reset removed). Handler decodes `{title?}`, calls `engine.start`,
    returns the success shape; maps single-active → 409, bad body → 400. Error envelope is
    `detail`-keyed (same shape as the existing `HostRejection`).
  - Tests required: 200 returns `{meeting_id, status, audio_path}`; concurrent start → 409
    `already_recording` with `active_meeting_id`; malformed body → 400 `invalid_request_body`.
  - Commit: `feat(http): POST /recordings start route (D11)`.

- [ ] **Task 6.2 — `POST /recordings/<id>/stop`.**
  - Handler calls `engine.stop`, returns `{meeting_id, status, duration_seconds, audio_path}`; maps
    no-active → 409, `<id>` ≠ active → 404. `?force=` parsed and ignored (v1).
  - **`recording_busy` deferred (rationale):** the spec lists it as a second 409, but the engine is a
    serialized `actor` with no concurrent-stop condition — there is no state in this slice that
    produces "busy." Ship without it; **flag for spec D11 reconciliation** (drop it, or define the
    state that yields it, when a trigger that can collide with a stop exists). `spec-plan-lockstep`:
    note this in the master-spec reconciliation list below.
  - Tests required: 200 returns the stop shape; no active recording → 409 `no_active_recording`;
    wrong id → 404 `meeting_not_found`.
  - Commit: `feat(http): POST /recordings/<id>/stop route (D11)`.

- [ ] **Task 6.3 — StatusStore writes.**
  - The engine calls `StatusStore.update(.recording(...))` on start and `.idle` on stop, so `/status`
    and the menu reflect live state.
  - Tests required: after `start` the store snapshot is `.recording` with the right
    `CurrentRecording`; after `stop` it's `.idle`. Extend the `/status` test to show recording after
    a start.
  - Commit: `feat(recording): write StatusStore on start/stop`.

- [ ] **Task 6.4 — Menu Start/Stop.**
  - `StatusItemController` gains Start/Stop menu actions calling the engine directly (the in-process
    join point). Re-introduces the menu recording controls dropped in the reset.
  - Tests required: the Start action invokes `engine.start`, Stop invokes `engine.stop` (spy engine);
    the menu item enable/label follows the StatusStore snapshot.
  - Commit: `feat(menu): Start/Stop recording actions (D11)`.

- [ ] **Task 6.5 — `stenoctl record start|stop`.**
  - Re-add `record_cmd.py` (`start --title`, `stop`), wire into `main.py`, re-add
    `start_recording(title)` / `stop_recording(meeting_id)` to `client.py` on the kept `_post`.
  - **`stop` resolves the active id first:** the route is `/recordings/<id>/stop`, so `record stop`
    GETs `/status`, reads `current_recording.meeting_id`, then POSTs to that id. If `/status` is
    `idle` (no `current_recording`), it errors "no active recording" (non-zero exit) **without**
    POSTing. (`/status` already carries `current_recording.meeting_id` — StatusStore.)
  - Tests required (Python, stubbing the HTTP client): `record start` POSTs to `/recordings` with the
    title; `record stop` GETs `/status` then POSTs to `/recordings/<that-id>/stop`; `record stop` when
    `/status` is idle exits non-zero without POSTing; a 409/404 from the server surfaces a clean CLI
    error (non-zero exit).
  - Commit: `feat(cli): re-add stenoctl record start|stop (D11)`.

- [ ] **Task 6.6 — End-to-end host-smoke.**
  - `make -C swift/Steno app` → `stenoctl app start` → `stenoctl record start` (or menu) →
    `/status` shows recording → `stenoctl record stop` → bundle lands in `recorded/` (≥min) with
    `events.jsonl` carrying `started`/`stopped`/`hashed`/`completed`. Then the crash path: start →
    `kill -9` the app → relaunch → orphan reconciled to `partial`. Record both in the PR `Verification:`.
  - Commit: covered by the PR body; no code commit unless smoke surfaces a fix.

---

## Self-review (spec coverage)

- D1 separated engines / watch-and-claim → recording engine (PR 4) + bundle stage dirs as the queue
  (PR 3); ML engine is a later slice (out of scope, stated).
- D2 event-log source of truth + projection + replay + reconcile → PR 2 (log) + PR 3 (reconcile) +
  PR 4 (fold/recovery). **Create-in-place:** the bundle is made directly in `recording/<id>/` and the
  `recording.started` fsync is the commit point (ARCHITECTURE.md:48) — a crash before it leaves an
  empty no-audio scaffold recovery removes, a crash after it leaves a committed bundle recovery
  classifies (PR 4.6 start + PR 4.8 recovery + PR 3 `removeEmptyScaffold`). No staging layer (it
  reintroduced a delete-a-committed-event hazard — removed, not patched). D3 granularity →
  per-meeting `events.jsonl` (PR 3/4); per-engine lifecycle log is **not** built here (no non-meeting
  events in the recording slice — deferred with the app/ML engines; flagged).
- D4 hash event + pair-travel → PR 4.5/4.7 + PR 3 (dir moves as a unit). D5 bundle dir → PR 3.
  D6 stage==status + ordering → PR 3. D7 events + four outcomes + min-duration + **the `partial`/
  `discarded` statuses + moves** → PR 4 (4.2 adds the state-machine cases). D8 dual-sink → PR 1.
  D9 envelope → PR 2. D10 recover-before-bind + drain + one-session-one-bundle → PR 4.8 + PR 5.
  D11 HTTP/CLI/menu → PR 6. D12 glossary/orchestrator + role map → PR 0 rename + PR 4/5 naming.
- Build-order PRs 0–6 map 1:1 to the spec's build order. PR 4 carries 8 tasks (4.1–4.8); all others
  unchanged — 28 tasks total.

**Deferred, with rationale (in-page above):** per-engine lifecycle log (D3) — no non-meeting events
this slice; `partial` promote/discard endpoints (D11) — stated deferred; the `recording_busy` 409
(D11) — no state produces it in a serialized engine (Task 6.2); `retention.junk_age_days` purge
mechanism (D7) — later retention step; the managed-resource hook framework (D12) — minimal drain
only (PR 5.2); multi-process log-rotation ownership (D8) — racy but low-impact this slice (PR 1.1);
`audio.filename_template` config removal — master-spec reconciliation.

## Master-spec reconciliation (after this slice — not in these PRs)

Per the spec's closing section, fold into `plans/specs/2026-06-04-meeting-pipeline-design.md` once
the slice lands: Decision 6 (bundle dir + `partial`/`discarded` statuses + no-audio-state revisit),
Decision 13 (audio in the bundle; integrity → classification), Decision 17 (`RecordController` →
recording engine; recover-before-bind; one-session-one-bundle), logging dual-sink (now **per-process
files** — Swift `steno-app.log` / Python `steno.log`; **update the future `stenoctl logs` command at
spec line ~286 to tail `~/Library/Logs/steno/*.log`**, not just `steno.log`), and the net-new
event-sourcing / watch-and-claim / glossary model. Remove `audio.filename_template` + its lockstep
validator at the same time.

**Control-plane spec refinements — DONE (`spec-plan-lockstep`, committed alongside this plan).**
`2026-06-18-control-plane-design.md` was amended: D7 create-in-place create order (the
`recording.started` fsync is the commit; recovery removes an empty pre-commit scaffold) +
`started.audio_path`; D8 separate per-process log files (Swift `steno-app.log` / Python `steno.log`,
no shared rotation — amended 2026-06-18 during PR 1); D11
`recording_busy` deferred (Task 6.2) + menu→engine-direct (PR 6 goal). Spec and plan are in lockstep.
