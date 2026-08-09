# skill-discovery Task 18A replay artifacts

For every `DISC-01`–`DISC-11` scenario, the matching
`prompts/<id>-control.md` freezes the prompt with the pre-Task-18A
`disciplined-research` description and `prompts/<id>-target.md` changes only that
line to the exact approved description `Use before stating any factual claim.`
Within each scenario, the request, all other descriptions, wrapper, and
evaluator-withheld rubric are byte-identical between arms.

The prompt, repaired-rubric, historical-rubric, and empty-manifest hashes are
recorded in [skill-discovery.md](../../skill-discovery.md#task-18a-reclassification-and-contract-freeze-2026-08-09).
No separate skill-body bundle is supplied because both prompts embed the complete description context.

The repaired `DISC-02`, `DISC-04`, and `DISC-05` controls completed at
`/private/tmp/dd-task18a-control-postfreeze-f59608a`, with freeze SHA-256
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`
and plan SHA-256
`4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`.
`DISC-02` scored 0/5 high and low; `DISC-04` scored 4/5 high and 3/5 low and is
a target RED because research changed from optional to required; `DISC-05` scored
5/5 high and low and is preservation. The other eight accepted controls remain
exact evidence from prior full-matrix root
`/private/tmp/dd-task18a-control-backfill-bd60966-escalated`, surviving freeze
SHA-256 `4671cfef15368088eaa554fdb67e5bea115d7a4a9a9610f7e07d16b160539b2d`,
accepted plan SHA-256
`60b753fe17539876893f367763d59bbd53b7f584a9001217ffe07bbd607c2ce3`.
All selected attempts were a1 with zero retries/errors under Codex CLI 0.147.0,
read-only/no-agents transport. High is the preservation gate; low is robustness
evidence only.
