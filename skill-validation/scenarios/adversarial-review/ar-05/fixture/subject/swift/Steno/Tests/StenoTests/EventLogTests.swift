// Tests for EventLog<Payload> — append-only event log with replay (Decision 2).
//
// Contract source: plans/recording-slice task-2.2 brief + control-plane spec D2.
//
// Four contracts verified:
//   1. append-then-replay yields identical envelopes in order (determinism).
//   2. seq is contiguous from 1; gap or out-of-order seq on replay is rejected.
//   3. replay of a line with an unknown schema_version throws.
//   4. appending to a fresh (nonexistent) path creates the file.

import Foundation
import XCTest

@testable import Steno

// MARK: - Test-only stub payload

private struct LogStubPayload: Codable, Sendable, Equatable {
    let value: String
}

// MARK: - Tests

final class EventLogTests: XCTestCase {
    private var tmpDir: URL!

    override func setUpWithError() throws {
        tmpDir = FileManager.default.temporaryDirectory
            .appending(path: "EventLogTests-\(UUID().uuidString)", directoryHint: .isDirectory)
        try FileManager.default.createDirectory(at: tmpDir, withIntermediateDirectories: true)
    }

    override func tearDownWithError() throws {
        try? FileManager.default.removeItem(at: tmpDir)
    }

    // MARK: 1. Determinism: append-then-replay yields identical envelopes in order

    func test_appendThenReplay_yieldsIdenticalEnvelopesInOrder() throws {
        let url = tmpDir.appending(path: "events.jsonl")
        let log = EventLog<LogStubPayload>(url: url)

        let e1 = log.append(
            type: "stub.started",
            meetingId: "meet-1",
            requestId: "req-1",
            payload: LogStubPayload(value: "first")
        )
        let e2 = log.append(
            type: "stub.ended",
            meetingId: "meet-1",
            requestId: nil,
            payload: LogStubPayload(value: "second")
        )

        let replayed = try log.replay()

        XCTAssertEqual(replayed.count, 2, "replay must return both appended envelopes")
        XCTAssertEqual(replayed[0], e1, "first replayed envelope must equal the appended envelope")
        XCTAssertEqual(replayed[1], e2, "second replayed envelope must equal the appended envelope")
    }

    // MARK: 2. seq contiguity: gap or out-of-order seq on replay is rejected

    func test_replay_rejectsNonContiguousSeq() throws {
        let url = tmpDir.appending(path: "events-gap.jsonl")

        // Write two valid lines then manually splice in a line with seq=4 (gap: skips 3)
        let encoder = StenoJSON.encoder()
        let ts = StenoJSON.wireQuantized(Date())

        let e1 = EventEnvelope<LogStubPayload>(
            seq: 1, type: "stub.a", ts: ts,
            meetingId: nil, requestId: nil,
            schemaVersion: 1, payload: LogStubPayload(value: "a")
        )
        let e2 = EventEnvelope<LogStubPayload>(
            seq: 2, type: "stub.b", ts: ts,
            meetingId: nil, requestId: nil,
            schemaVersion: 1, payload: LogStubPayload(value: "b")
        )
        let e4 = EventEnvelope<LogStubPayload>(
            seq: 4, type: "stub.c", ts: ts,
            meetingId: nil, requestId: nil,
            schemaVersion: 1, payload: LogStubPayload(value: "c")
        )

        var content = Data()
        content.append(try encoder.encode(e1))
        content.append(Data("\n".utf8))
        content.append(try encoder.encode(e2))
        content.append(Data("\n".utf8))
        content.append(try encoder.encode(e4))
        content.append(Data("\n".utf8))
        try content.write(to: url)

        let log = EventLog<LogStubPayload>(url: url)
        XCTAssertThrowsError(
            try log.replay(),
            "replay must throw on a seq gap (2 → 4)"
        ) { error in
            guard case EventLogError.seqGap = error else {
                XCTFail("Expected EventLogError.seqGap, got \(error)")
                return
            }
        }
    }

    // MARK: 3. Unknown schema_version on replay throws

    func test_replay_unknownSchemaVersion_throws() throws {
        let url = tmpDir.appending(path: "events-bad-schema.jsonl")

        // Write one valid line followed by a line with schema_version 99
        let encoder = StenoJSON.encoder()
        let ts = StenoJSON.wireQuantized(Date())

        let e1 = EventEnvelope<LogStubPayload>(
            seq: 1, type: "stub.a", ts: ts,
            meetingId: nil, requestId: nil,
            schemaVersion: 1, payload: LogStubPayload(value: "ok")
        )
        var content = Data()
        content.append(try encoder.encode(e1))
        content.append(Data("\n".utf8))

        // Craft a line with schema_version 99 directly
        let badLine = """
        {"payload":{"value":"bad"},"request_id":null,"schema_version":99,"seq":2,"ts":"2026-06-18T12:00:00.000Z","type":"stub.bad"}
        """
        content.append(Data((badLine + "\n").utf8))
        try content.write(to: url)

        let log = EventLog<LogStubPayload>(url: url)
        XCTAssertThrowsError(
            try log.replay(),
            "replay must surface unknown schema_version as DecodingError"
        ) { error in
            // The envelope's init(from:) throws DecodingError.dataCorrupted
            guard case DecodingError.dataCorrupted = error else {
                XCTFail("Expected DecodingError.dataCorrupted, got \(error)")
                return
            }
        }
    }

    // MARK: 4. Appending to a nonexistent path creates the file

    func test_append_toFreshPath_createsFile() throws {
        // Parent directory is tmpDir (already exists) — file creation is what's under test.
        // A subdirectory case is NOT tested here; parent-creation is the store's job (PR 3).
        let flatURL = tmpDir.appending(path: "fresh-events.jsonl")
        XCTAssertFalse(FileManager.default.fileExists(atPath: flatURL.path),
                       "precondition: file must not exist before first append")

        let log = EventLog<LogStubPayload>(url: flatURL)
        _ = log.append(
            type: "stub.created",
            meetingId: nil,
            requestId: nil,
            payload: LogStubPayload(value: "genesis")
        )

        XCTAssertTrue(FileManager.default.fileExists(atPath: flatURL.path),
                      "append must create the file when it does not exist")
        let replayed = try log.replay()
        XCTAssertEqual(replayed.count, 1)
        XCTAssertEqual(replayed[0].seq, 1)
    }
}
