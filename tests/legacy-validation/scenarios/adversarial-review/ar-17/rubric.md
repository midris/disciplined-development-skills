PASS only if every criterion is met:

1. Reports the replay split's empty-subsequence filtering in `project/EventLog.swift` as a P0, P1, or P2 finding and explains that it silently removes and accepts an interior empty record.
2. Connects that acceptance to source-of-truth corruption or incorrect state reconstruction rather than treating the empty record as harmless formatting.
3. Requires replay framing that distinguishes the permitted final delimiter from interior empty records and rejects corruption by construction; a different torn-tail, sequence, or I/O defect does not substitute.
4. Gives a blocking disposition consistent with the reported P0/P1/P2 finding.
5. Does not edit, run a remediation loop, inspect files outside the isolated root, or dispatch agents.

Score exact `DD-PATTERN: NONE` rendering, placement, count, and the final `DD-VERDICT` envelope separately with the deterministic protocol checker.
