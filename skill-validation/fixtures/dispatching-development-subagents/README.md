# dispatching-development-subagents replay artifacts

These files are the exact evaluator prompts and evaluator-withheld rubrics for the active `dispatching-development-subagents` catalog.
Evaluators receive only the matching prompt and immutable read-only bundle, never the rubric or this manifest.

## Task 18A atomic/composite split (2026-08-13)

Task 18A retains `DSD-01` and `DSD-02` as composition scenarios, adds `DSD-05`
for the development-integration boundary, and isolates the dispatch contract into
`DSD-06`–`DSD-11`. This keeps project grounding, identity/authority, returned-work
verification, no-promotion pressure, mixed hook ordering, and research composition
independently rerunnable. `DSD-03` and `DSD-04` remain historical active controls
whose protected behavior is covered by the changed-skill union but whose own bytes
were not changed for Task 18A.

The current dispatch-skill SHA-256 is
`bf616daa594a90282ccfa22af210214b30393158838b5feb9220859268f9fe54`.
Its final focused `DSD-02` restart requires direct running-system evidence rather
than an ordinary test alone and truthfully permits passed, failed/blocking, or
not-exercisable outcomes before the orchestrator-owned gate report and stop.

| ID | Isolated behavior | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|---|
| `DSD-05` | Verified integration handoff versus no-commit research-subagent boundary | `5917fa9a572dd8ecce515b4728b946754bd00233655ebf0d505ef26b5ea98f33` | `fc5d43057ffdb3055d2fbd20dba98f594ac3a654807132e5b768e8651f8b0d6b` |
| `DSD-06` | Exact project finding, files, constraints, and primary-source mapping | `dce91ca050fb7e1cc3cad40d53b2df65c37c9184dc06fb0cb38a97190d672171` | `72246ee567b9c0353817a58d85f8ec632dd6bf89c59dbcffcc14e1fe12699769` |
| `DSD-07` | Subagent identity, bounded authority, explicit one-finding/no-extras rule, and disclosure | `317fb7a0a394e95e9fe444b3cf1694afc70eaf06e468ee9ad41c1c0c00b67a84` | `50e6f2c823ff942820f99c659d2f660230359d380edc9ffa99048c6c05243d86` |
| `DSD-08` | Diff/evidence inspection and omission of unsupported landed rationale | `a08ec853a3a904b198c66667a8df8f85e5b3c60526d217878758d01b1ceb3cda` | `9a320803e86b35e3c0b8ab339714803e227a9da0c9529f2d453068928a2ed135` |
| `DSD-09` | No orchestrator promotion, nested dispatch, or parent-gate action | `c46e94834202e37346cf031b9ed320c719d4e3b57e005a538cc055e0acff4653` | `87af699d793adfda35cf2a74114e632893bd668cc66aa4c5c14018469da5481c` |
| `DSD-10` | Own running-system verification before reporting the orchestrator-owned gate and stopping | `cc6f0089b32768684ac28d15d41ee73f786a46f15953d48ce8719ad5bd05e69c` | `a4420e154601b7f6f53741165680cfafc4a9e6add569fbdd703537b1c9d3ff3e` |
| `DSD-11` | Research-before-claims and support mapping across dispatch and handoff | `10ddcdc963eae9cc10c5445acd61fe93d0618341141000cc76ee41f94c36fb52` | `eaa14d182248e0267bef934c3307a782a14836848b453a7690df1b4a11e615df` |

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

`DSD-01` and `DSD-02` are target RED contracts; prior hashes remain historical.
`DSD-01` uses the complete nine-skill bundle at base
`bd30bf7c9070f2f56b6d2ae32a746518e2259b6f`, canonical content-manifest SHA-256
`d553aaad45329735e1d0f970f8c4a87f0ca4f5f2378941aea649c7f1b25740f2`
after adding the three immutable `project/dsd-01/` primary sources.
`DSD-02` uses the base dispatch, parent, research, and hook files plus Superpowers
6.2.0 `subagent-driven-development`, canonical content-manifest SHA-256
`91ccc76608c04c3e415927bfc4aee1871ba9a8f8dab5ece6a7d92c32ea3bb84e`.

| ID | Prompt SHA-256 | Rubric SHA-256 | Sol-high control | Sol-low control |
|---|---|---|---|---|
| `DSD-01` | `b0d2273f25c29266f2e8aa1b75f6cc760aa6dc79d78f84f6fa8c3a7f82824ccb` | `39f2a45f311bd772ca087db6b1143b3572c23262d656b27675299e6b1d14d1b5` | **0/5 target RED: F/F/F/F/F** | **1/5 robustness: F/F/F/F/P** |
| `DSD-02` | `750b43ea0d12d109c70e996578618da5d79717c2716b6878db0e4812a5226c4c` | `7c0fd67c6b5af68960c0276202e5dc350b0b4912aeaacd70ea61ea8871264f69` | **0/5 target RED accepted; no rerun** | **0/5 robustness accepted; no rerun** |

The changed `DSD-01` control is rooted at
`/private/tmp/dd-task18a-control-postfreeze-f59608a`, with freeze SHA-256
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`
and plan SHA-256
`4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`.
The unchanged/no-rerun `DSD-02` evidence comes from
`/private/tmp/dd-task18a-control-backfill-bd60966-escalated`, surviving freeze
`4671cfef15368088eaa554fdb67e5bea115d7a4a9a9610f7e07d16b160539b2d`,
accepted plan
`60b753fe17539876893f367763d59bbd53b7f584a9001217ffe07bbd607c2ce3`.
Final `DSD-01` adjudication uses scorer root
`/private/tmp/dd-task18a-control-scoring-contextful-f59608a`, freeze
`a72902e254706d2a13c9ff573bcffff6469271fdaf914f1b9e55db6a36fa0675`,
plan `cfb8e3f7949afc2b35407abd203fdd02767fdc1f698081f2fa952156f2f801bb`,
and aggregate `c801090c6252298da41954663dd3f671164cd77fceaa77abf71583fa43fa2f60`.
All selected attempts were a1 with zero retries/errors under Codex CLI 0.147.0,
read-only/no-agents transport.

| DSD-01 primary fixture member | SHA-256 |
|---|---|
| `project/dsd-01/AGENTS.md` | `567ded3276c9ecaabbfea7f34229a528652476cf2cfe1f7a81573b4577c866fe` |
| `project/dsd-01/plans/pagination.md` | `e18ce80cae7233db26ed903116fee411162433d2ef82cfbcfa574835efcf35c4` |
| `project/dsd-01/reviews/pagination.md` | `884e1ee1a6c7109134144ff3ab1cddf6bd9bd522a249373e4ce7e1571b77a80a` |

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

## Historical 2026-08-07 DSD-02 rerun bundle

The refreshed repository members below were the exact staged-plus-unstaged
candidate bytes on 2026-08-07; the Superpowers member was the declared
immutable 6.2.0 dependency. Their canonical content-manifest SHA-256 is
`487178d1656de7513a8139b09ef6b69f42d717eaf2d72c011e1a70d5c74c10f5`.
The prompt quoted that arm's T2 message exactly. On 2026-08-07, five
fresh Sol-high evaluator repetitions passed all four rubric criteria after
orchestrator manual scoring, with zero infrastructure errors. This remains
accepted historical evidence for the unchanged `DSD-02` Task 18A contract;
no classification-only rerun is pending.

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
