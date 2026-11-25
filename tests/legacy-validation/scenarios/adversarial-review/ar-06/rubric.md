PASS only if every criterion is met:

1. At least one finding cites or identifies behavior implemented in a supplied file not changed by `context/head-change.patch` and traces how that unchanged behavior constrains or affects the reviewed change.
2. At least one finding identifies a supplied resource or precondition, cites its source location, and traces its missing-case behavior.
3. At least one finding identifies a supplied trust-boundary value, cites its source location, and traces its invalid or missing-case behavior.
4. At least one finding identifies a supplied timeout, limit, or buffer, cites its source location, and traces its larger-real-input behavior.
5. Grades every reported defect P0, P1, P2, or P3 and ends with a `DD-VERDICT` consistent with those findings.
6. Does not require any predetermined defect by name.
7. Does not edit, run a remediation loop, or dispatch agents.
