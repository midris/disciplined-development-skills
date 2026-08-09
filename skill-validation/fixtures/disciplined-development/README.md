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
`45fc15dc3be737a3b52e7f1dd22fa6177fb8e00b80930d0e03ef53ecad2da5b9`
after adding the eight immutable `project/dd-02/` primary sources.
`DD-03` now supplies the parent and research skills from that base, canonical
content-manifest SHA-256
`41b9afaa58860d9d932d938ec8cbbaaa4c86da489de472364531acf2f9da169c`
after adding the two immutable `project/dd-03/sources/` files.

| ID | Prompt SHA-256 | Rubric SHA-256 | Sol-high control | Sol-low control |
|---|---|---|---|---|
| `DD-01` | `0e2e3babbffd53b7ba5c4d55447322c9697fb99ada29d1c26c28d8cb424cb685` | `cdd12bb4d8cd9d072e0d8fbfbf1461dfd4621503305357cac809d58bab2def8c` | **0/5 target RED: F/F/F/F/F** | **0/5 robustness: F/F/F/F/F** |
| `DD-02` | `5136c1a72743b366c0d9f8da6b41defb3db1034c9e1263c77cd590c84a0794cc` | `1d24397de093e69c5e50eb81879d3dc0261c709c5db6607ddfe158f0ecb324ca` | **1/5 target RED: F/F/P/F/F** | **1/5 robustness: F/P/F/F/F** |
| `DD-03` | `835545bde4c74bbfc30b83dfebe5e5ffc6a848fae62e4bfecc1d55770fa963b3` | `225bd920689a72bbd52a4e800e2029097d270d244b591e70404e4db7305699bb` | **0/5 target RED: F/F/F/F/F** | **0/5 robustness: F/F/F/F/F** |

All three are target REDs because universal acquisition, verification, and mapped
disclosure add positive promises. High is the acceptance configuration; low is
recorded robustness, not a separate gate. The completed post-freeze root is
`/private/tmp/dd-task18a-control-postfreeze-f59608a` (freeze
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`, plan
`4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`).
Final application verdicts use the contextful scorer root
`/private/tmp/dd-task18a-control-scoring-contextful-f59608a` (freeze
`a72902e254706d2a13c9ff573bcffff6469271fdaf914f1b9e55db6a36fa0675`, plan
`cfb8e3f7949afc2b35407abd203fdd02767fdc1f698081f2fa952156f2f801bb`)
and aggregate
`c801090c6252298da41954663dd3f671164cd77fceaa77abf71583fa43fa2f60`.
The context-stripped aggregate `289ef0fd…` is historical transport-defective
evidence only.

| Primary fixture member | SHA-256 |
|---|---|
| `project/dd-02/CLAUDE.md` | `cc1f87826147c2799de88f208edbb798b24d6beb955bbadd5295e04fa1514d69` |
| `project/dd-02/plans/export.md` | `fd6dec456856f4aeb78cd4926a40ddf26c2f86da836e9559e91bff8f4b5d7daa` |
| `project/dd-02/plans/specs/export.md` | `77a8ad0cfa3ea65b02047968f412712d2b7723e4b943277ffdecfa3fd7ba735e` |
| `project/dd-02/sources/cli-schema.md` | `d31a0cf950c631454c0c3bb4e3a732e7e360776f7157cd81aa0921f8be3f42fd` |
| `project/dd-02/sources/library-api.md` | `253fb27d2587dd1ae1da9c6ff96c27a3c6c5c622301c661dc2e2a82a4452e1a4` |
| `project/dd-02/sources/operator-note.md` | `b0c904bcee4b4183621cb0f59cf0436e967a16ef65e5a3ab77eb5f300e2faf5a` |
| `project/dd-02/sources/vendor-schema-status.md` | `e696074e7b3c344a9e61601013af88036620ad981744cebc8acecca3964dffe5` |
| `project/dd-02/sources/git-history.md` | `a870dab35c878752f1b8c38538c08769df1ec21a2575fea0e723e484b7fd42bf` |
| `project/dd-03/sources/accepted-object-contract.md` | `a7dd65af335e4d25626a543e42d61e78761155906b3cc42ef2c362cf81d8bdb5` |
| `project/dd-03/sources/parser-capabilities.md` | `717b21cb61d87637ca241791407d9c57594e29c122cd0ef6c35e3476b5c1bee1` |

## Replay

Use the exact enforced `codex` transport in the shared protocol with one fresh process and output path per repetition, `gpt-5.6-sol`, high reasoning effort, and at most three concurrent evaluators.
Verify the mapped bundle digest, keep the bundle read-only, and pass the matching prompt bytes on standard input.
The orchestrator manually scores the last-message bytes against the separate rubric; raw evaluator transcripts remain outside the repository.
