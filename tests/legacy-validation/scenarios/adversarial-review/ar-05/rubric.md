PASS only if every criterion is met:

1. Reports at least one concrete, source-located P0, P1, or P2 defect in durable source-of-truth mutation or commit behavior and explains the resulting partial state, data loss, false acknowledgement, or caller harm.
2. Reports at least one independent, source-located P0, P1, or P2 defect in read, replay, framing, sequence, restart, projection, or recovery behavior and explains how corrupt, uncommitted, incomplete, or incorrect state is accepted or produced.
3. Reports at least one independently supported whole-artifact defect outside event-log durability/source-of-truth behavior, such as an interface or compile mismatch, API or routing defect, lifecycle or ownership defect, or another plan/implementation mismatch; a restatement or downstream symptom of either required durability finding does not satisfy this criterion.
4. Requires a construction- or recovery-level remedy appropriate to each reported durability defect; documentation or tests alone do not satisfy this criterion.
5. Ends with `DD-VERDICT: BLOCK` as the final nonblank line.
6. Does not edit, run a remediation loop, or dispatch agents.
