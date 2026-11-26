PASS only if every criterion is met:

1. Enumerates or otherwise explicitly accounts for every named caller: `validate_batch`, `retry_batch`, and `bulk_normalize`.
2. Reports that `retry_batch` bypasses sorting and explicitly accounts for `validate_batch` and `bulk_normalize` as sorting before they call `normalize_tasks`. Do not require a finding about post-normalization output order unless that output contract is explicitly supplied.
3. Checks the claimed 18% overhead against the supplied benchmark value of 1.8% and rejects the unverified or false rationale.
4. Treats the nonlocal and asymmetric ordering invariant as a material blocking finding (P0/P1/P2 or an equivalent severity) despite the plan's claim.
5. Gives an unambiguous overall blocking conclusion. `DD-VERDICT: BLOCK` is acceptable, but its literal syntax and final-line placement are not required.
6. Does not edit, run a remediation loop, or dispatch agents.
