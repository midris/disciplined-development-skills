# adversarial-review-loop replay artifacts

These files are the exact evaluator prompts and evaluator-withheld rubrics for the active `adversarial-review-loop` catalog.
Every scenario is prompt-contained; no code fixture is supplied.
Evaluators receive a prompt file and one immutable read-only bundle, never a rubric or this manifest.

## Control bundles

All repository skills come from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2`.
Bundle digests use the canonical path-and-content algorithm in [the shared protocol](../../README.md#immutable-control-bundles).

| Bundle | Scenarios | Contents | Archive SHA-256 | Content-manifest SHA-256 |
|---|---|---|---|---|
| Loop-only control | `CS`, `T3`–`T7`, `NF`, `PW`, `XL`, `G3A`–`G3C`, `CE` | `skills/adversarial-review-loop/SKILL.md` | `17fe5aae470370b04bd607f94ed1dd9a83178be848fd710e09aecce9d3eb7c8e` | `ee55d09386f8f162e9606ac40cc7dcbfc0699ec4733fb318e5dffa91dd4f39f3` |
| Complete nine-skill control | `T2` | All nine repository `SKILL.md` files listed in the shared control manifest | `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3` | `e2249c4b24132523f1374d506957197a303314e2bfbc6e32c9c1b233909cbbff` |
| Ownership composition control | `OWN` | Loop and parent controls plus Superpowers 6.2.0 task-loop dependency | Custom bundle; use the manifest below | `8386fb9818d60c2ecdf9da95a586b5a601a678baa57c4e5268e3c987e4deb840` |

The loop control file SHA-256 is `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6`.

The ownership bundle is exactly:

| Source | Bundle path | SHA-256 |
|---|---|---|
| Repository control commit | `skills/adversarial-review-loop/SKILL.md` | `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6` |
| Repository control commit | `skills/disciplined-development/SKILL.md` | `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec` |
| Superpowers 6.2.0 | `skills/superpowers/subagent-driven-development/SKILL.md` | `349a08ad8b59b19b86c13a7d2f34a1a38719bf88257004a863eefefa8d9f9e40` |

## Prompt and rubric hashes

| ID | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|
| `CS` | `6bfbf05aa6a494295fe5e044f1ed8f45a38b0349c3fbafeeb5bc76df4877d788` | `587c543ecc82abdbde08123923e1c64aea77ca013d2a7a76ebe257f8c73989df` |
| `T2` | `157ab2e1d09d24e08c18ab4e826d847d00d96a322c4387769901480e0590a9be` | `5487fae2531b6153ee3f5d3d6fd399a5106326280f017d83accb14cd5eeaf2e9` |
| `T3` | `ef458a31071054126b7c6647a4f8859c71dc9416912c617b3f2d505fea5bea94` | `1c0f227ca974edc1a6c06e99a380f9a85c72c2b525fbb1d5c76330d23cd8a055` |
| `T4` | `d074f2aa8f0b156e0037feb5dc95e7c0b8598798fe4ec1e3fa5370c1a41808cb` | `4f329062dd03163cbbdcffc8cbf4e15fe695eceebe735183289e3609fa69cb76` |
| `T5` | `179d134c24c22bd9dc8599ade9a3e6d5a625d3177a5596a7993a0275e5f9e739` | `469171a65d370542232776bc42ded0acf10e43f26375ec677d098cc3130b6749` |
| `T6` | `59177853e8e120996001a69366f022e703e89c52c1df50f0c766f0b40d878d47` | `36f660a1320fde68110f2b6c819d0adf52b032098d6b4eb69a2a3f8b1d009d62` |
| `T7` | `3062673c9af2b2748007b44704347ff6a18058688be2f268d24cb326bb6f7179` | `21102b7487933fd8dce4a9f01579c083e38cef8cf57b0ac74749a950098420fe` |
| `NF` | `6cb872779eb18d018ae9fb8d254e96c50c51a2a2a30540a16ade6220bdd333db` | `86756fd50bf95913fcab2e6234d71ec5189f3541bc20488461c072f2e4a183c8` |
| `PW` | `088e46a7453bd054439431ab42968dde77f0b5af669a557ab46bf6cb36f4de89` | `d4a20aa222ad5ddfd171516b8212b00f2709da86420f8e217479fd2a5bb93c27` |
| `XL` | `5fae476bd5596182aaffebb5311e8f67114ad9aa888edad4e9b101b564fd8e98` | `e3ccfc978b43ae2d04cb00e00ce8da165999417465d0dfe75db732186be2a315` |
| `G3A` | `f881f1c7fba549ed96b87b6b4e8f691a5af790f590192c9e9186276bb86ee747` | `ee12c28eba3f3be9a282b3480569ce44af7e8bcc683132bf45fbc2eba5ea03e5` |
| `G3B` | `ead756c75cf32bff1ac8c5f21953649e90d9b537fe9a660364084f95f23b9190` | `3c743d848330299dec890f9230c5e86f4e107221c2494cdd146d79d01d144636` |
| `G3C` | `03207727853600c8b122843e3014ba6af563e11f65d51098b70c8cb8a0fa87ad` | `6982f364c0314610496cfbbcfaeb370166707e0da014101ff1c7f24f6efa99cc` |
| `OWN` | `d4ae4791e081658d23d37c11c7778025db95c8b0a1b329a79bbbe6fe641a77c9` | `7195792a1728cbcd27f58736489dd9b475a30712ea7be431d5e7b90a657945bb` |
| `CE` | `886d7cf352938df43e7d24d0015759835d35b1b05361790270468f9dcb0a0ffb` | `02dc65ef6bba25d9f31a51e0f02aa4dda5bb6329b40871816ac580c556aab007` |

## Task 18A OWN pre-draft freeze

The repaired `OWN` control uses the loop, parent, and research skills at base
`bd30bf7c9070f2f56b6d2ae32a746518e2259b6f` plus Superpowers 6.2.0
`subagent-driven-development`.
Its canonical content-manifest SHA-256 is
`c5bb38b5aa306fb059e12365075f8b68d238e1412450dab4cf1558efe51e259b`.
Prompt SHA-256 is `deab7d6fec9cb4654a10992d958d3d9305693b84ab8c07294d8adc34ee930f3c`;
rubric SHA-256 is `a0cb5a88011a3ea8a5be2dd5ee5bf0f627e9e540cb414d105d78d9ef4592521c`.
This is a target RED because universal acquisition, verification, and mapped
disclosure are new positive promises. Accepted controls are 0/5 at both efforts.
The unchanged prompt and bundle remain scorable and the accepted 0/5 high and low
controls remain exact evidence; classification alone triggers no rerun.
The accepted unchanged/no-rerun control comes from full-matrix root
`/private/tmp/dd-task18a-control-backfill-bd60966-escalated`, with surviving
freeze SHA-256
`4671cfef15368088eaa554fdb67e5bea115d7a4a9a9610f7e07d16b160539b2d`
and accepted plan SHA-256
`60b753fe17539876893f367763d59bbd53b7f584a9001217ffe07bbd607c2ce3`.
All selected attempts were a1 with zero retries/errors under Codex CLI 0.147.0,
read-only/no-agents transport.

The final Task 18A candidate repaired one ambiguity in the target prompt: the
whole-branch loop has **completed** its third blocking round with findings still
open. That current prompt is
`97908401be96002414033827828d8bb10def56050b10e839f600a45a5462132a`;
the rubric remains
`a0cb5a88011a3ea8a5be2dd5ee5bf0f627e9e540cb414d105d78d9ef4592521c`.
The repair starts a new target epoch and does not alter or reuse the frozen
pre-draft controls above.

## Replay

Use the exact enforced `codex` transport in the shared protocol with one fresh process and output path per repetition, `gpt-5.6-sol`, high reasoning effort, and at most three concurrent evaluators.
Materialize the mapped bundle outside the repository, verify its digest, make it read-only, and pass the matching prompt bytes on standard input.
The orchestrator scores the last-message bytes against the separate rubric; raw transcripts remain outside the repository.
