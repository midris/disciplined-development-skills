// Generic event envelope — Decision 9, recording-slice PR 2 Task 2.1.
//
// One JSON object per line in `events.jsonl`. Wire conventions:
//   - snake_case keys via explicit CodingKeys
//   - ISO-8601 ms dates via StenoJSON encoder/decoder
//   - schema_version validated loudly at decode (unknown → DecodingError)
//   - Optional fields (meeting_id, request_id) encode ABSENT when nil
//     (plain Codable / encodeIfPresent convention — NOT WireEncodable, which
//     forces nil → explicit null for the HTTP /config present-and-null contract)
//
// Payload: Codable & Sendable. The concrete payload enum (recording events)
// lands in PR 4; this task is the generic wrapper only.
//
// ts is snapped to the wire ms grid at construction (StenoJSON.wireQuantized)
// so in-memory == encode→decode round-trip, identical to Meeting/ActualWindow.
//
// YAGNI: no type→payload dispatch registry here. That coupling is realised when
// Payload is a concrete enum reading the envelope `type` field (PR 4).

import Foundation

// MARK: - EventEnvelope

/// Generic Codable wrapper around every typed event written to `events.jsonl`.
///
/// - `seq`            Per-log monotonic integer (assigned by the log — Task 2.2).
/// - `type`           Dotted event name, e.g. `recording.started`.
/// - `ts`             Clock of the event; snapped to the wire ms grid on construction.
/// - `meetingId`      Present on meeting-scoped events; absent otherwise.
/// - `requestId`      Optional; the operation that emitted the event.
/// - `schemaVersion`  Payload-schema version (always 1 pre-v1). Decode rejects unknown loudly.
/// - `payload`        Type-specific data; decoded via `Payload`'s own `Codable`.
public struct EventEnvelope<Payload: Codable & Sendable>: Codable, Sendable {
    public let seq: Int
    public let type: String
    public let ts: Date
    public let meetingId: String?
    public let requestId: String?
    public let schemaVersion: Int
    public let payload: Payload

    enum CodingKeys: String, CodingKey {
        case seq
        case type
        case ts
        case meetingId     = "meeting_id"
        case requestId     = "request_id"
        case schemaVersion = "schema_version"
        case payload
    }

    /// `ts` is snapped to the wire ms grid so in-memory value == encode→decode read-back.
    public init(
        seq: Int,
        type: String,
        ts: Date,
        meetingId: String?,
        requestId: String?,
        schemaVersion: Int,
        payload: Payload
    ) {
        self.seq           = seq
        self.type          = type
        self.ts            = StenoJSON.wireQuantized(ts)
        self.meetingId     = meetingId
        self.requestId     = requestId
        self.schemaVersion = schemaVersion
        self.payload       = payload
    }

    // MARK: - Decoding

    /// Custom init validates schema_version and decodes optionals with decodeIfPresent
    /// (absent-when-nil contract). Mirrors Meeting.init(from:)'s loud schema guard.
    public init(from decoder: Decoder) throws {
        let c = try decoder.container(keyedBy: CodingKeys.self)

        // schema_version: must be exactly 1; any other value is a loud DecodingError.
        let version = try c.decode(Int.self, forKey: .schemaVersion)
        guard version == 1 else {
            throw DecodingError.dataCorruptedError(
                forKey: .schemaVersion,
                in: c,
                debugDescription: "schema_version must be 1, got \(version)")
        }
        schemaVersion = version

        seq       = try c.decode(Int.self,     forKey: .seq)
        type      = try c.decode(String.self,  forKey: .type)
        ts        = try c.decode(Date.self,    forKey: .ts)
        meetingId = try c.decodeIfPresent(String.self, forKey: .meetingId)
        requestId = try c.decodeIfPresent(String.self, forKey: .requestId)
        payload   = try c.decode(Payload.self, forKey: .payload)
    }

    // MARK: - Encoding
    //
    // Explicit encode so optionals use encodeIfPresent (absent-when-nil).
    // Synthesized encode would also give absent-when-nil for optionals, but
    // with a custom init(from:) the synthesized encode is unavailable unless
    // also synthesized — being explicit is clearer and consistent.

    public func encode(to encoder: Encoder) throws {
        var c = encoder.container(keyedBy: CodingKeys.self)
        try c.encode(schemaVersion, forKey: .schemaVersion)
        try c.encode(seq,           forKey: .seq)
        try c.encode(type,          forKey: .type)
        try c.encode(ts,            forKey: .ts)
        try c.encodeIfPresent(meetingId, forKey: .meetingId)
        try c.encodeIfPresent(requestId, forKey: .requestId)
        try c.encode(payload,       forKey: .payload)
    }
}

// MARK: - Conditional Equatable

/// Allows determinism tests to compare appended vs. replayed envelopes directly.
extension EventEnvelope: Equatable where Payload: Equatable {}
