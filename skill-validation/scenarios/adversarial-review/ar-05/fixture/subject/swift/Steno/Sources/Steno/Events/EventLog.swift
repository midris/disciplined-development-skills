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
