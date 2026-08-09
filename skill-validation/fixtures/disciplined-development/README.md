# disciplined-development replay artifacts

These files are the exact evaluator prompts and evaluator-withheld rubrics for the active parent-owned catalog.
Evaluators receive only the matching prompt and immutable read-only bundle, never the rubric or this manifest.

## Control bundles

Repository files come from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2`.
Bundle digests use the canonical path-and-content algorithm in [the shared protocol](../../README.md#immutable-control-bundles).

| Bundle | Scenarios | Contents | Repository archive SHA-256 | Content-manifest SHA-256 |
|---|---|---|---|---|
| Complete integrated control | `DD-01`, `DD-02` | All nine repository `SKILL.md` files listed in the shared control manifest plus the Superpowers 6.2.0 methodology dependencies below | `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3` for repository members | `ffeeb68d8fae44b81d4c1b57a7a92f6e5ed82fd6cc58e429cfcf4c826c8c8475` |
| Parent-only control | `DD-03` | `skills/disciplined-development/SKILL.md` | `622771912909a7fb22fd7576d17ad2cbfd2014cabdcd55324309b0a4952dd2da` | `49191f92b1cf5b2f3cfa51bc7066716c15b7671c960ded6bb1b1c7dfd8a38a76` |

The control parent skill SHA-256 is `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`.

The complete integrated control adds these immutable Superpowers 6.2.0 dependencies under `skills/superpowers/<name>/SKILL.md`:

| Dependency | SHA-256 |
|---|---|
| `brainstorming` | `4a54a4858b99807f3155ed1614b2f116e35ea5c1b788e793f565dd837fd3891f` |
| `dispatching-parallel-agents` | `1968923066f3b707eb01d1992cdf4c42284c3855f70253b9cd5000ff45fca13c` |
| `executing-plans` | `c4c3d8b628c51114cd165fb8246fe02744cd8be180032328391252e653028d9b` |
| `finishing-a-development-branch` | `d0ac8360ed9d59121776ef95c84bcb38e9747de0d7ae7e227dca81e437593b9b` |
| `receiving-code-review` | `091df1629510af1b92fc4abd6f96732ebedb4cb2c0f3457e8f2740b0504a2438` |
| `requesting-code-review` | `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8` |
| `subagent-driven-development` | `349a08ad8b59b19b86c13a7d2f34a1a38719bf88257004a863eefefa8d9f9e40` |
| `systematic-debugging` | `808fc5717aa88ad65efff312b11c186294d3e6ee301afb584e2f86599b137787` |
| `test-driven-development` | `bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54` |
| `verification-before-completion` | `2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3` |
| `writing-plans` | `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0` |

## Inherited coverage

These scenarios retain their existing owners and are linked into the parent skill's complete active closure rather than duplicated here:

| Scenario | Owner | Task 10 obligation |
|---|---|---|
| [`DISC-01`–`DISC-10`](../../skill-discovery.md#active-catalog-definitions) | Task 1 shared discovery suite | Description routing and parent-plus-applicable-companion availability |
| [`DSD-01`, `DSD-02`](../../dispatching-development-subagents.md#active-catalog-definitions) | `dispatching-development-subagents` | Principle 4 plus subagent versus orchestrator gate ownership |
| [`OWN`](../../adversarial-review-loop-scenarios.md#active-catalog) | `adversarial-review-loop` | Per-task versus whole-branch review-loop ownership and independent counters |
| [`WER-07`](../../writing-explicit-rationale.md#wer-07--parent-and-plan-composition) | `writing-explicit-rationale` | Principle 1 delegation of rationale necessity without forcing a why for every choice |

## Prompt and rubric hashes

| ID | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|
| `DD-01` | `ba51dcfa160daffdb681c3bef0b993dc36ba1091c6e789826948331ebcc39d13` | `bbd1849b0b941c63282006e019f4cc5f24ad00e85897964c3f231d6ac4c97485` |
| `DD-02` | `5da5fe92259e8a7343ebc394eba326e06fa31c65eea3ee829de0157eeac8d528` | `ab8ab55f1e58fb9c2eaa68b695e426ca6c8f85c3ec8154a64b30804aaee958f3` |
| `DD-03` | `852eb66f0c3084e4f9aff349ae3775b5c70ca5c3221d1b6538d62ca603830b80` | `ead264e837afb0fe2aa974d0a9280e3c36e23d5079968f67da21bac6902c1c06` |

## Task 18A pre-draft freeze

The table above is historical under its prior contracts.
The repaired prompts and rubrics below require universal research selection and
unambiguous source disclosure for the complete factual output.
`DD-01` and `DD-02` use the pre-Task-18A complete integrated bundle at base
`bd30bf7c9070f2f56b6d2ae32a746518e2259b6f`, canonical content-manifest SHA-256
`3fc788a23bd66ce2977a43b4a2f8d71fa6a13515a3286df1baf3089c6a4c2a53`.
`DD-03` now supplies the parent and research skills from that base, canonical
content-manifest SHA-256
`d22456d9691855f6fe271f3e52a89b1b239c6eb7f3688f88e6a1dd26224b534d`.

| ID | Prompt SHA-256 | Rubric SHA-256 | Sol-high control | Sol-low control |
|---|---|---|---|---|
| `DD-01` | `ba217bdd4254dcccdce7d5efc1914ea90863ef2c8b26995325b98c8ad9fac057` | `cdd12bb4d8cd9d072e0d8fbfbf1461dfd4621503305357cac809d58bab2def8c` | Pending orchestrator backfill | Pending orchestrator backfill |
| `DD-02` | `ec19ded3c3ad53c1dc304fe4437071654dfcb86e5ba76ab0c6da2bd981e6a669` | `2db5d91720ce463855864d28b03585f60a03340f6921bc5cb3d6ea4eb342397d` | Pending orchestrator backfill | Pending orchestrator backfill |
| `DD-03` | `ba5903ee6a599c035386117556fa9c8b318106789949744ed740520e288775ba` | `26e51c0920c0c68417d51e8e1a1a5f24f36abc041960f761819958379f4b9659` | Pending orchestrator backfill | Pending orchestrator backfill |

`DD-01` is a watched target because vignette A adds a newly universal route.
`DD-02` and `DD-03` are repaired preservation contracts because the old parent
already governs their factual checkpoint, plan, contract, and threshold claims;
their fresh Sol-high and Sol-low controls must each pass 5/5. The orchestrator
records all run and scoring metadata.

## Replay

Use the exact enforced `codex` transport in the shared protocol with one fresh process and output path per repetition, `gpt-5.6-sol`, high reasoning effort, and at most three concurrent evaluators.
Verify the mapped bundle digest, keep the bundle read-only, and pass the matching prompt bytes on standard input.
The orchestrator manually scores the last-message bytes against the separate rubric; raw evaluator transcripts remain outside the repository.
