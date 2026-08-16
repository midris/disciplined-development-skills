public final class EventLog<Payload: Codable & Sendable> {
    @discardableResult
    public func append(
        type: String,
        meetingId: String?,
        requestId: String?,
        payload: Payload
    ) -> EventEnvelope<Payload> {
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
}
