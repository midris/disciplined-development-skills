# disciplined-research Task 18A replay artifacts

These files freeze the exact evaluator prompts, evaluator-withheld rubrics, and task fixtures for `DR-04` through `DR-06`.
Evaluators receive the matching prompt and immutable read-only bundle, never the rubric or this manifest.

## Supplied contexts

Both controls use `skills/disciplined-research/SKILL.md` from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` at SHA-256 `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50`.
`DR-04` adds `project/payments/retry_policy.py`; `DR-05` adds `sources/nimbus-support-matrix.md`.
`DR-06` adds `project/upload-403/evidence-index.md`, a malformed `runtime-config.json`, and `worker.log`.
Its two opaque arms use the same fixture: the current control skill above and the ignored proposed research skill at frozen SHA-256 `d782407966eb0993cc16579b106994649b6c5058bffe2509af41842716bd6a91`.
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

`DR-06` is frozen but unrun.
Its fixture file SHA-256 values are `5ce87478b5f41f46f10dbba5b329f6eae004ca9b4a6895a495fa75ec292bfb46` for `evidence-index.md`, `4ec39350c64e94229c7aaa59a719afc1c18c2c673d7d5215a8be38ee5307af13` for `runtime-config.json`, and `d381395b47ed8fb03ca12fc8c1ab9a1c17299d28149d591119319705aed39eba` for `worker.log`.
The canonical fixture manifest is `c142cc3b042197f94df331d9d92967eb9fcc93d53a430fa471af7e3a99d97474`; the control and candidate bundle manifests are respectively `59663c07b2bd8b3011bd38baa36aaac3b70a6ea301a6bae3b2f84fec806e3913` and `4b6906bf1c853e5a17525935a311668d28d52f0852f20bfc341da10a7085ab7a`.

### `worker.log` generation record

A one-off Python 3 generator, not retained in the repository, emitted a 230,400-byte UTF-8 structured log from fixed start time `2026-08-09T14:20:00Z`.
It cycled ordinary heartbeat, lease-renewal, manifest-scan, part-staging, queue-poll, and temporary-cleanup traffic; inserted upload-attempt 403 records at event indices 251, 777, and 1321; filled the remaining pre-tail bytes with a deterministic hexadecimal collector-flush field; and wrote the capture-truncation record last.
Generation asserted the exact byte size, three `event=upload_attempt` occurrences, three `http_status=403` occurrences, the final truncation record, and absence of credential, token, expiry, and cause terms before writing the file.

## Run policy

Each accepted control used five fresh `gpt-5.6-sol` repetitions at high effort and five at low effort under the shared read-only, no-agents transport with maximum concurrency three.
The orchestrator owns execution, scoring, and repetition-level result metadata.
The unrun `DR-06` comparison is frozen as two opaque arms at both efforts with five repetitions per cell: 20 evaluator processes, followed by four contextful high-effort scorer processes.
