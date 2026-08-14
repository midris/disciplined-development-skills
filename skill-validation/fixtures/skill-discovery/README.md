# skill-discovery Task 18A replay artifacts

For every `DISC-01`–`DISC-11` scenario, the matching
`prompts/<id>-control.md` freezes the prompt with the pre-Task-18A
`disciplined-research` and dispatch descriptions. The corresponding
`prompts/<id>-target.md` carries the current complete research and dispatch
descriptions. Within each scenario, the request, the other seven descriptions,
wrapper, and evaluator-withheld rubric are byte-identical between arms.

The final union exposed one ambiguity in `DISC-02`: “help me handle” already-reported
findings allowed a new-review route even though the row protects remediation.
Both arms now say `Remediate those reported findings; do not perform a new review.`
The repaired control / prompt-ambiguity target SHA-256 values are
`3dcebec6b967ccd13e025673a4ce65f34eedbacc7bc8d74e18d4b32a363731ab`
/ `42ab326f2358b25b803d4a6f6a93a6642cbf64fc41d3c8654e5f681c21d0219b`.
Fresh high and low controls scored 0/5 for the intended missing-research reason;
that prompt-ambiguity current arm scored 5/5. All 15 responses completed on
attempt 1. The later routing repair added the explicit internal-logical-review
clause to every exact current target description; the final `DISC-02` target is
`16506525e0f9ec43e2d5099aa411564492880a9ed8c5230c1407a20be7bc7682`
and is accepted only through the final zeroed union.

`DISC-12` is the later response/interaction boundary added after the user broadened
the final description beyond project tasks. Its target prompt carries the complete
current research and dispatch descriptions and requires `disciplined-research` for
a non-development, response-only factual interaction.
Its control / target / rubric SHA-256 values are
`11e06edee0e08a07bf25e5dd71ae87cdc47f62e70f57d95acf407f1f0d8e4cd5`
/ `5a3c869dcf3307459fb548effeb4d4d015188fbd3a358a9f2fe312a800484b1c`
/ `a17e7937d27723947239247831e08f6064cfb4b7cb35159dc38bc3014c18c066`.

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

The older `DISC-02` roots above are historical for superseded wording. The repaired
high-control / low-control / prompt-ambiguity-current freeze SHA-256 values are respectively
`1e3c3afd6aa154b69ee85c7bd853f8df0cc4b5295890261d0e48b71e57eee401`,
`b34db825bb142b9e4058686c2439ddeefa2c172cc7d30a85aa600495666f6745`,
and `4a7c5097457077e70c3a8399b8a94806a155bec94abb512852f7248482a6fd01`.
