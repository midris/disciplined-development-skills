public final class EventLog<Payload: Codable & Sendable> {
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
}
