# disciplined-research Task 18A replay artifacts

These files freeze the exact evaluator prompts, evaluator-withheld rubrics, and task fixtures for `DR-04` and `DR-05`.
Evaluators receive the matching prompt and immutable read-only bundle, never the rubric or this manifest.

## Supplied contexts

Both controls use `skills/disciplined-research/SKILL.md` from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` at SHA-256 `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`.
`DR-04` adds `project/payments/retry_policy.py`; `DR-05` adds `sources/nimbus-support-matrix.md`.
The canonical bundle-manifest hashes are recorded in the owning [validation record](../../disciplined-research.md#task-18a-contract-freeze-2026-08-09).

Task 18A accepted evidence for both unchanged/no-rerun contracts is rooted at
`/private/tmp/dd-task18a-control-backfill-bd60966-escalated`, with surviving
freeze SHA-256
`4671cfef15368088eaa554fdb67e5bea115d7a4a9a9610f7e07d16b160539b2d`
and accepted plan SHA-256
`60b753fe17539876893f367763d59bbd53b7f584a9001217ffe07bbd607c2ce3`.
`DR-04` remains a target RED at 0/5 high and 1/5 low; `DR-05` remains
preservation at 5/5 high and low. Both accepted contracts were unchanged by the
eight-scenario repaired rerun, so their prior exact artifacts remain authoritative.
All selected attempts were a1 with zero retries/errors under Codex CLI 0.147.0,
read-only/no-agents transport. High is the preservation gate; low is robustness
evidence only.

## Run policy

Each accepted control used five fresh `gpt-5.6-sol` repetitions at high effort and five at low effort under the shared read-only, no-agents transport with maximum concurrency three.
The orchestrator owns execution, scoring, and repetition-level result metadata.
