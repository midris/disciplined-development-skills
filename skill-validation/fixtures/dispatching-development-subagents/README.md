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
| `DSD-02` | `aef962ad53389c9035f7d3adec5c48cedd5e820d6ae77be8b8fdf35e2eb8f948` | `5245688d8d665b6b9422acff73fcd7ad42cc3337c082dea84b772dad68dd2ba7` |
| `DSD-03` | `6e99e94ce865c2102799474225fa8ee500440d013d30b9a853951663b3ee0d70` | `c7b3fbf6eb092f8919cd8ec1eaa278af7f736f4fa1522bbb8e56bc536aab6570` |
| `DSD-04` | `31a5cbe423d9bd9531cc2706de2f9372d13af5bb142db5320e8887cb75ab2dfe` | `dc29adc91e29ca32bae2fe3a8df3ba1a7cac3293add9eec2e77b7aeecaebd25b` |

## Replay

Use the exact enforced `codex` transport in the shared protocol with one fresh process and output path per repetition, `gpt-5.6-sol`, high reasoning effort, and at most three concurrent evaluators.
Verify the mapped bundle digest, keep the bundle read-only, and pass the matching prompt bytes on standard input.
The orchestrator manually scores the last-message bytes against the separate rubric; raw transcripts remain outside the repository.
