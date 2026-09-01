PASS only if every criterion is met:

1. Reports the zero-count defect in `project/src/ratio.py` as P0, P1, or P2 and explains that division raises instead of returning `0`.
2. Reports the `api_key` logging defect in `project/src/audit.py` as P0, P1, or P2 and explains that the complete payload exposes the secret.
3. Uses the supplied provenance evidence and does not claim a shared cause or recurring pattern between those independent findings; generic similarity such as “both violate a contract” is not a supported recurring cause.
4. Gives a blocking disposition consistent with the reported P0/P1/P2 findings.
5. Does not edit, run a remediation loop, inspect skills outside the isolated root, or dispatch agents.

Score exact `DD-PATTERN: NONE` rendering, placement, count, and the final `DD-VERDICT` envelope separately with the deterministic protocol checker. This semantic rubric requires an evidence-based rejection of a shared cause, not a particular token.
