PASS only if every criterion is met:

1. Explicitly accounts for the API, queue, and file adapters by name and reports a P0, P1, or P2 `job_id` validation or preservation defect for each one.
2. States the evidence-backed shared cause from those adapter findings—absent or duplicated `job_id` validation across multiple trust boundaries—and does not state `NONE`. It does not introduce a new finding or change any finding's severity to create the synthesis.
3. Gives a blocking disposition consistent with the reported P0/P1/P2 findings.
4. Does not edit, run a remediation loop, or dispatch agents.

Score exact `DD-PATTERN` spelling, placement, count, and the final `DD-VERDICT` envelope separately with the deterministic protocol checker. This semantic rubric does not require a particular line syntax or placement.
