# dispatching-development-subagents replay artifacts

These files are the exact evaluator prompts and evaluator-withheld rubrics for the active `dispatching-development-subagents` catalog.
Evaluators receive only the matching prompt and immutable read-only bundle, never the rubric or this manifest.

## Control bundles

Repository files come from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2`.
Bundle digests use the canonical path-and-content algorithm in [the shared protocol](../../README.md#immutable-control-bundles).

| Bundle | Scenarios | Contents | Repository archive SHA-256 | Content-manifest SHA-256 |
|---|---|---|---|---|
| Dispatch-only control | `DSD-03`, `DSD-04` | `skills/dispatching-development-subagents/SKILL.md` | `46b5fc86b9b3ea895f5bdbd760edb74c4ed9bff7ee47a88928fb8dcffbc9896d` | `824bb24d7c59e307f72607688df2410366d77600a4bd49d3931bd01511a6deff` |
| Complete nine-skill control | `DSD-01` | All nine repository `SKILL.md` files listed in the shared control manifest | `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3` | `e2249c4b24132523f1374d506957197a303314e2bfbc6e32c9c1b233909cbbff` |
| Identity/nudge composition control | `DSD-02` | Dispatch skill, parent skill, exact hook, and Superpowers 6.2.0 execution dependency | `e53574d8f507f43ac2a0d413159fa28a71f2d43ce5d386e62b01f86eb437b2ec` for repository members | `957816e0a88621d8650f541249e1797200d14a0ccfa16e9de8b25e89e9af07c9` |

The composition bundle is exactly:

| Source | Bundle path | SHA-256 |
|---|---|---|
| Repository control commit | `skills/dispatching-development-subagents/SKILL.md` | `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500` |
| Repository control commit | `skills/disciplined-development/SKILL.md` | `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec` |
| Repository control commit | `skills/disciplined-development/hooks/review_nudge.py` | `4c7fc6940939c0e7a148b339ac7862a0ad0980a8f8f153d0ab640dc8271363b0` |
| Superpowers 6.2.0 | `skills/superpowers/subagent-driven-development/SKILL.md` | `349a08ad8b59b19b86c13a7d2f34a1a38719bf88257004a863eefefa8d9f9e40` |

The dispatch control skill SHA-256 is `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500`.

## Prompt and rubric hashes

| ID | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|
| `DSD-01` | `d365c6a2f8979519f31d3d9ea9b969f23f96956bb722a02b0fb0baf178f8aecf` | `c00fc4d4ea8d875c25b9cd0c7c2a50f99d325f0f7799264c412572754f85a7f1` |
| `DSD-02` | `5dd3edc6600ac1288cf26fb4c3f5fdd3c66dbb62da6decc5bc6470649e4ee416` | `5245688d8d665b6b9422acff73fcd7ad42cc3337c082dea84b772dad68dd2ba7` |
| `DSD-03` | `6e99e94ce865c2102799474225fa8ee500440d013d30b9a853951663b3ee0d70` | `c7b3fbf6eb092f8919cd8ec1eaa278af7f736f4fa1522bbb8e56bc536aab6570` |
| `DSD-04` | `31a5cbe423d9bd9531cc2706de2f9372d13af5bb142db5320e8887cb75ab2dfe` | `dc29adc91e29ca32bae2fe3a8df3ba1a7cac3293add9eec2e77b7aeecaebd25b` |

## Task 18A pre-draft freeze

`DSD-01` and `DSD-02` are repaired preservation contracts; the prior hashes and results
remain historical.
`DSD-01` uses the complete nine-skill bundle at base
`bd30bf7c9070f2f56b6d2ae32a746518e2259b6f`, canonical content-manifest SHA-256
`0a98f98107a9fc409c91d2197927298e531dccd678c7226f5561424ab747ced3`.
`DSD-02` uses the base dispatch, parent, research, and hook files plus Superpowers
6.2.0 `subagent-driven-development`, canonical content-manifest SHA-256
`713930e51e1a2ebecec52d2a15ed249210c34ada20945f58c09f0f07627cf5eb`.

| ID | Prompt SHA-256 | Rubric SHA-256 | Sol-high control | Sol-low control |
|---|---|---|---|---|
| `DSD-01` | `be49d7269965b2b1b2fe3446b6137b82f20ec7f308e3927b79e8e37a177a8f5f` | `0cf272a54a21bb50d77bedef6907e245b8d74a67a11719bac6d358b0889ddf07` | Pending orchestrator backfill | Pending orchestrator backfill |
| `DSD-02` | `750b43ea0d12d109c70e996578618da5d79717c2716b6878db0e4812a5226c4c` | `7c0fd67c6b5af68960c0276202e5dc350b0b4912aeaacd70ea61ea8871264f69` | Pending orchestrator backfill | Pending orchestrator backfill |

## Historical 2026-08-06 DSD-02 rerun bundle

The repository members below were the supplied bytes on 2026-08-06; the
Superpowers member was the declared immutable 6.2.0 dependency. Their
canonical content-manifest SHA-256 is
`8217d48556c879f55c63d268c211282a8dc1f4095003e2558b494404e3b8523d`.
The prompt hash listed above quoted that bundle's T2 message exactly. On 2026-08-06,
five fresh Sol-high evaluator repetitions passed after orchestrator manual
scoring, with zero infrastructure errors. This is preserved historical evidence,
not the current arm.

| Source | Bundle path | SHA-256 |
|---|---|---|
| Staged candidate | `skills/dispatching-development-subagents/SKILL.md` | `93a13cd44ddd350b00477db6cb9e285d16816c20edf7c9be52931f608df4cc6a` |
| Staged candidate | `skills/disciplined-development/SKILL.md` | `dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6` |
| Staged candidate | `skills/disciplined-development/hooks/review_nudge.py` | `e43784e0e850facdaf0bb2fd9e67ba8ef642f07ce7416f43609cbef6d11a90bb` |
| Superpowers 6.2.0 | `skills/superpowers/subagent-driven-development/SKILL.md` | `349a08ad8b59b19b86c13a7d2f34a1a38719bf88257004a863eefefa8d9f9e40` |

## Current DSD-02 rerun bundle

The refreshed repository members below are the exact staged-plus-unstaged
candidate bytes on 2026-08-07; the Superpowers member remains the declared
immutable 6.2.0 dependency. Their canonical content-manifest SHA-256 is
`487178d1656de7513a8139b09ef6b69f42d717eaf2d72c011e1a70d5c74c10f5`.
The prompt still quotes the current T2 message exactly. On 2026-08-07, five
fresh Sol-high evaluator repetitions passed all four rubric criteria after
orchestrator manual scoring, with zero infrastructure errors.

| Source | Bundle path | SHA-256 |
|---|---|---|
| Staged candidate | `skills/dispatching-development-subagents/SKILL.md` | `93a13cd44ddd350b00477db6cb9e285d16816c20edf7c9be52931f608df4cc6a` |
| Staged candidate | `skills/disciplined-development/SKILL.md` | `dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6` |
| Candidate hook | `skills/disciplined-development/hooks/review_nudge.py` | `61f0603da0b6ced00ca1bf0be7042f745daf199e68ba700e574018f4fad00da3` |
| Superpowers 6.2.0 | `skills/superpowers/subagent-driven-development/SKILL.md` | `349a08ad8b59b19b86c13a7d2f34a1a38719bf88257004a863eefefa8d9f9e40` |

## Replay

Use the exact enforced `codex` transport in the shared protocol with one fresh process and output path per repetition, `gpt-5.6-sol`, high reasoning effort, and at most three concurrent evaluators.
Verify the mapped bundle digest, keep the bundle read-only, and pass the matching prompt bytes on standard input.
The orchestrator manually scores the last-message bytes against the separate rubric; raw transcripts remain outside the repository.
