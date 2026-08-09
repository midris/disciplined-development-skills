# Writing explicit rationale — validation

## Active catalog audit (2026-08-03)

The shared all-nine discovery suite remains owned by
[skill-discovery.md](skill-discovery.md#active-catalog-definitions).
`DISC-08` protects the routine-rename negative, `DISC-09` protects intentional
shortcut routing, and `DISC-10` protects rationale that would otherwise remain only
in a PR description.
The body-level application path protected here is `DISC-10` →
`writing-explicit-rationale` → `WER-01`, `WER-02`, `WER-03`, `WER-05`, and
`WER-06`; `WER-07` protects composition with the parent and plan-writing skills.

The historical scenarios were only partially recoverable under the common protocol:

| Historical evidence | Classification | Active disposition |
|---|---|---|
| Reviewer visibility: bare consumer | Merge | Missing-rationale placement is covered by `WER-02`, PR-only routing by `DISC-10`, and duplicate resistance by `WER-05` |
| Reviewer visibility: governing-file consumer | Retire | The governing-file distinction no longer matters after commit/PR rationale stops being part of the skill contract; replace it with existing-rationale reuse coverage in `WER-05` |
| Routing matrix: active-plan implementation with delegation | Merge | Merge into existing `DISC-04` and `DISC-06` |
| Routing matrix: padded README tightening | Merge | Merge into existing `DISC-03` |
| Routing matrix: SKILL.md shortening | Retire | The exclusion contract was superseded by the approved Task 2A authoring-boundary design |
| Routing matrix: plan deferral with PR-only rationale | Repair | Reconstruct as shared `DISC-10` |
| Routing matrix: routine convention-preserving rename | Merge | Merge into existing `DISC-08` |

No historical scenario was replayable unchanged: **Keep 0, Repair 1, Merge 4,
Retire 2**.
Existing `DISC-09` adds current shortcut-routing coverage but is not counted as a
successor to the historical five-cell matrix.
Simple direct invocation, repeated-review batch auditing, isolated broad-domain use,
existing-rationale reuse, and relevant-history filtering were missing, so
`WER-01`, `WER-02`, `WER-03`, `WER-05`, `WER-06`, and `WER-07` are **Add 6**.

The six owned scenarios are the smallest suite that keeps direct plan editing,
retroactive batch repair, broad-domain application, existing-rationale reuse, and relevance
filtering independently observable while checking parent-and-plan composition.
Scope-repair simplification changes only `WER-03`'s category and conclusion.
Its existing definition, evidence, and record structure already provide the necessary
broad-domain coverage, so no new scenario, policy rule, or duplicate section is warranted.
The section-by-section simplification questions are:

| Skill section | Would a simpler approach preserve the necessary intent and effectiveness? | Smallest evidence mapping |
|---|---|---|
| Frontmatter description | Yes; use shared routing cells rather than repeat metadata prompts here | `DISC-08`–`DISC-10` |
| Role | Yes; one sentence distinguishes rationale judgment and placement from sibling procedures | `WER-01`, `WER-03` |
| What rationale means here | Only partly; what/how, necessary why, consequence-free choices, and irrelevant history are distinct predicates but fit one paragraph | `WER-01`–`WER-03`, `WER-06` |
| Keep one authoritative home | No; repeated-review auditing, creating missing rationale, and referencing current rationale are distinct steps in one workflow | `WER-01`, `WER-02`, `WER-05` |
| Resist duplicate rationale | Yes; three observed pressure classes fit one compact table | `WER-05`, `WER-06` |
| Whole skill | No smaller structure preserves the framing, placement workflow, and tested resistance to duplicate rationale | `DISC-08`–`DISC-10`, `WER-01`–`WER-03`, `WER-05`–`WER-07` |

## Active scenario catalog

Run metadata: control commit
`4296647f0dff48a9e77b979ef07e813bf1f66db2`; Codex CLI 0.146.0;
`gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; five fresh processes per
scenario; maximum concurrency three; enforced read-only, no-agents transport;
manual scoring; rubric withheld; run date 2026-08-03; zero infrastructure errors.

The owner of every active ID is `writing-explicit-rationale`.
`WER-01`–`WER-03`, `WER-05`, and `WER-06` affect only that skill;
`WER-07` also affects `lean-plan-writing`, `disciplined-development`, and
`disciplined-research`.
`WER-01` receives the immutable complete nine-skill control.
`WER-02`, `WER-03`, and `WER-06` receive only the immutable control
`skills/writing-explicit-rationale/SKILL.md` and inline task context.
`WER-05` receives that single-skill control plus its declared existing-rationale fixture.
No external skill dependency or live web access is supplied.

| ID | Affected skills | Type / status | Protected promise and section | Supplied context | Exact prompt | Evaluator-withheld rubric | Rerun trigger |
|---|---|---|---|---|---|---|---|
| `WER-01` | `writing-explicit-rationale` | Simple application + direct invocation / preservation | Direct invocation safely applies a small descope to the adjacent plan item, preserves remaining scope, and records the selected scope, cause, and accepted impact without unrelated plan work; Role, What rationale means here, Keep one authoritative home | Complete nine-skill control + inline release-plan decision | [WER-01](#wer-01--simple-direct-descope) | Return exactly one revised plan item; retain CSV and JSON in v1; defer XML; state unstable partner schema as the cause; state that XML clients wait for schema approval as the accepted impact; keep rationale adjacent in the item; add no unrelated plan-wide work, sibling procedure, or process narration | Trigger, direct invocation, plan placement, scope preservation, rationale shape, or bundle composition changes |
| `WER-02` | `writing-explicit-rationale` | Non-trivial application + focused regression / preservation | Twice re-litigated rationale triggers a complete decision-site audit and one batched durable repair rather than another one-off reply; consequential and consequence-free sites are distinguished; What rationale means here, Keep one authoritative home, Resist duplicate rationale | Single-skill control + inline three-site change inventory | [WER-02](#wer-02--repeated-review-batch-audit) | Inventory all three supplied sites; add durable rationale at the ingest decision site or in one project document referenced from affected code, plus local quota-state rationale; for each, state the chosen behavior, causal alternative boundary, and accepted consequence; classify the consequence-free telemetry-library choice as no rationale needed; batch both triggering sites rather than fixing only the reported one; add no reviewer reply, commit-only substitute, or unsupported site | Retroactive signal, batch-audit, active-choice trigger, non-trigger, authoritative-home placement, or rationale shape changes |
| `WER-03` | `writing-explicit-rationale` | Broad-domain isolated application / preservation | Apply the approved rationale policy to a nonprofit budget exception without repository, software, hook, or sibling-skill dependencies; Role, What rationale means here, Keep one authoritative home | Single-skill control + inline nonprofit policy decision | [WER-03](#wer-03--isolated-nonprofit-policy-exception) | Return only amendment text for the Emergency grants section; state the temporary $5,000 cap through March 31, 2027; state winter-shelter demand as the cause; state the accepted $30,000 contingency exposure, monthly review, and reversion to $2,000 after March 31, 2027; keep all rationale on the policy amendment; no software, repository, Git, PR, or sibling procedure may replace a required element | Broad-domain scope, isolated application, exception trigger, policy placement, rationale shape, or supplied decision changes |
| `WER-05` | `writing-explicit-rationale` | Focused regression / watched RED → target GREEN | When authoritative project rationale already exists, new code references it instead of creating drift-prone copies; Keep one authoritative home, Resist duplicate rationale | Single-skill control + `docs/architecture/ingest.md` existing-rationale fixture | [WER-05](#wer-05--existing-rationale-reference) | Return exactly two labeled blocks; the code comment cites `docs/architecture/ingest.md#interactive-guard-placement`; the commit message identifies the change, contains no duplicated rationale, and may optionally cite the authoritative document; neither block repeats the causal explanation, accepted duplication, or revisit condition | Existing-rationale fixture, authoritative-home rule, non-duplication rule, response shape, or decision facts change |
| `WER-06` | `writing-explicit-rationale` | Focused regression / preservation | A paste-ready code comment retains history only when it constrains correctness or a future implementation decision; What rationale means here | Single-skill control + inline serializer decision | [WER-06](#wer-06--relevant-history-only) | Return only one paste-ready code comment; state that legacy leading zeroes are preserved because archived records are verified against exact serialized bytes and normalization would invalidate signatures; omit the migration year, the former importer's language, and any other backstory that does not affect correctness or future implementation | Necessity predicate, historical-context boundary, rationale content, output shape, or decision facts change |
| `WER-07` | `writing-explicit-rationale`, `lean-plan-writing`, `disciplined-development`, `disciplined-research` | Parent-and-plan composition / target RED | The parent establishes on-page placement, delegates necessity judgment without forcing rationale for every defensible alternative, and routes every factual plan claim through universal grounding; What rationale means here | Disciplined development + disciplined research + writing-plans + lean plan writing + writing explicit rationale | [prompt](fixtures/writing-explicit-rationale/prompts/wer-07.md) | [rubric](fixtures/writing-explicit-rationale/rubrics/wer-07.md) | Parent/research wording, companion delegation, necessity predicate, plan/spec pairing, supplied choices, source-disclosure mapping, or useful-versus-harmful context threshold changes |

`WER-04` is intentionally unused: its pre-freeze commit-pressure contract was merged
into `WER-02`, `DISC-10`, and `WER-05` before execution.

### 2026-08-03 bundle manifests (prior evidence)

The `WER-01` complete control uses the Task 1 nine-skill archive SHA-256
`8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`.
The `WER-02`, `WER-03`, `WER-05`, and `WER-06` single-skill controls use file SHA-256
`97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.
Their single-skill archive SHA-256 is
`d7147756bc0cf242fa63ece39ac285216e456addef5bd2c691cb9ec62c73bd0c`;
its canonical content-manifest SHA-256 is
`b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd`.

| Scenario | Source kind | Full revision or frozen content revision | Source path | Bundle-relative path | File SHA-256 |
|---|---|---|---|---|---|
| `WER-01` | Repository | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | The exact nine source paths listed in [README.md](README.md#immutable-control-bundles), incorporated here as the Task 1 manifest | Same nine repository-relative paths | Per-file hashes in that manifest |
| `WER-02`, `WER-03`, `WER-06` | Repository | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `skills/writing-explicit-rationale/SKILL.md` | `skills/writing-explicit-rationale/SKILL.md` | `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe` |
| `WER-05` | Repository | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `skills/writing-explicit-rationale/SKILL.md` | `skills/writing-explicit-rationale/SKILL.md` | `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe` |
| `WER-05` | Inline fixture | Task 6 RED candidate frozen 2026-08-03 by the content hash in this row | `skill-validation/writing-explicit-rationale.md#wer-05-fixture` | `docs/architecture/ingest.md` | `5e25960ed19f0e046ecb263282d9244b9a5026695cc16a7ddb08663f422e4f7e` |
| `WER-07` control | Prior approved working-tree candidates + declared external dependency | Frozen 2026-08-03 by the file hashes in this row | `skills/disciplined-development/SKILL.md`; `skills/lean-plan-writing/SKILL.md`; `skills/writing-explicit-rationale/SKILL.md`; Superpowers 6.2.0 `writing-plans` | Same four paths under `skills/` | `21a46fb9b80cf29862a5e8ee5953fc6a3b3271da044eca60ac75b7060f43562e`; `4c659b76d3bfbe47a6fad906987eeb2166be577613d4a4832c96b8b341039d8c`; `ec77350bf2b51ba9ccb09375234f4727a0189417e2b1a0e1814aca30dd58a62c`; `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0` |
| `WER-07` target | 2026-08-03 working-tree candidates + declared external dependency | Frozen 2026-08-03 by the file hashes in this row | Same four source paths as control | Same four bundle-relative paths | `82337abab625c40e811e274910bae654ce892004dc70210392adaa6fcc06d776`; `76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb`; `4035ecdf52cd6a9302d399440d4e93b1776fb043981558f62c584bf5aed39865`; `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0` |

The `WER-07` control and 2026-08-03 target canonical content-manifest SHA-256 values are
`8f44b0c0a7118564a696d8fa10f4b267b8741ef67181010bbb3ecd56fe7eb234`
and `add84b6a7c2d04718e6957c3672e3081dad101d65eb1dfe730d57af0efd07509`.

The fixture-expanded `WER-05` canonical content-manifest SHA-256 is
`bc170bc184b7f59a991513c331ce8e72192a683909f48abc799099824b2a0c3b`.

The 2026-08-03 complete-suite target skill file SHA-256 was
`4035ecdf52cd6a9302d399440d4e93b1776fb043981558f62c584bf5aed39865`.
Its complete nine-skill, single-skill, and fixture-expanded canonical
content-manifest SHA-256 values are respectively
`6f88fedf7f60eda822f7db106abfbabf450ce97e401cb96eb8a1729bfc905e10`,
`3792834d17f9db7344c37b161c0e680993b45a1d767fbe5b09d3b88fb58dca89`,
and `51c391083ab0958ac8671cee3be11383ce71ed077d27c1764b8f7bebeba35a56`.

The owner-approved final placement clarification adds architecture documents to
the durable document examples and names a code decision-site comment explicitly.
Its skill file SHA-256 is
`a41d59faaea4be81e6cff5b2e35154f8b4b6d077afce6c0c6cd9a3d8cb82c3e6`.
Only `WER-02` and `WER-05` met their rerun triggers; both passed 5/5 on fresh
Sol-high evaluators. Their 2026-08-03 single-skill and fixture-expanded canonical
content-manifest SHA-256 values are respectively
`7a2b47984edad87463fc9dbe7405cf5646c46cf8dde142cb30acd640b9c8d3bf`
and `5faa20d515408799218af4d110b9b1a09257ed72805560201abf6fbe62903bdb`.

The 2026-08-03 complete target retains six Task 1 control files and replaces the parent,
lean-plan, and explicit-rationale skills used by the final composition test.
Its path-sorted canonical manifest is:

| Bundle-relative path | Source | File SHA-256 |
|---|---|---|
| `skills/adversarial-review-loop/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6` |
| `skills/adversarial-review/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c` |
| `skills/concise-writing/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72` |
| `skills/disciplined-development/SKILL.md` | 2026-08-03 Task 16 target | `82337abab625c40e811e274910bae654ce892004dc70210392adaa6fcc06d776` |
| `skills/disciplined-research/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50` |
| `skills/dispatching-development-subagents/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500` |
| `skills/lean-plan-writing/SKILL.md` | 2026-08-03 Task 16 target | `76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb` |
| `skills/sweeping-stale-references/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157` |
| `skills/writing-explicit-rationale/SKILL.md` | 2026-08-03 Task 16 target | `4035ecdf52cd6a9302d399440d4e93b1776fb043981558f62c584bf5aed39865` |

#### WER-05 fixture

`docs/architecture/ingest.md`

```markdown
# Ingest architecture

## Interactive guard placement

Tenant guards stay at interactive ingest handlers because batch imports reach persistence only after approval.
This accepts duplication across two interactive handlers; extract a shared interactive guard when a third caller needs it.
```

Every prompt below is byte-for-byte evaluator input.
The catalog rubrics never enter evaluator prompts.

### WER-01 — simple direct descope

```text
You are a fresh, read-only skill evaluator.
The complete nine-skill local bundle is installed. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Directly invoke `writing-explicit-rationale`: read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

The current release-plan item says: "Ship CSV, JSON, and XML export in v1."
The team decided to keep CSV and JSON in v1 but defer XML because the partner schema is still unstable. Customers who require XML will wait until the partner approves a stable schema.

Return only one revised release-plan item. Do not revise any other part of the plan or narrate your process.
```

### WER-02 — repeated-review batch audit

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and the supplied task context are available. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

A reviewer has twice said to move the tenant rate-limit guard from `src/ingest.py:44` into shared `persist()`. The author answered only in review chat that `batch_import.py` also calls `persist()` with already-approved batches, so the guard must stay at interactive ingest; this accepts duplicated guards in `src/ingest.py` and `src/admin_ingest.py` until a third interactive caller appears.
The same change also preserves the previous quota for 60 seconds after a downgrade at `src/quota.py:73` because in-flight requests still carry the old token; this accepts up to 60 seconds of elevated quota.
At `src/telemetry.py:19`, the project chooses between two equally maintained and secure telemetry libraries with identical observable behavior and no downstream consequence.

Handle the repeated finding before another review.
Return only a decision-site inventory with `Location` and `Action` columns, followed by the exact durable artifact text to add. Do not write a reviewer reply or narrate your process.
```

### WER-03 — isolated nonprofit policy exception

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and this non-software task are available. There is no repository, code, Git, PR, hook, or sibling skill. Do not edit files, change state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

A nonprofit's Emergency grants policy normally caps each grant at $2,000.
The finance committee approved a temporary cap of $5,000 through March 31, 2027 because winter-shelter demand has outgrown the ordinary limit.
The exception may consume up to $30,000 of contingency funds, will be reviewed monthly, and reverts to $2,000 after March 31, 2027.

Return only the exact amendment text to insert under the policy's `Emergency grants` heading.
```

### WER-05 — existing rationale reference

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and the supplied project document are available. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `docs/architecture/ingest.md` and `skills/writing-explicit-rationale/SKILL.md` completely and follow the skill as binding guidance.

You are adding the existing tenant guard to `src/admin_ingest.py`, the second interactive handler.
The reviewer is waiting and the user says: "Add a comment explaining why the guard stays here, and repeat the explanation in the commit message so nobody misses it."
The authoritative rationale already exists under `Interactive guard placement` in the supplied project document.

Return only two labeled, paste-ready blocks: `Code comment` and `Commit message`.
Do not narrate your process.
```

### WER-06 — relevant history only

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and this task context are available. Do not edit files, change state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

The serializer at `src/archive.py:41` preserves leading zeroes in legacy numeric strings instead of normalizing them because archived records are signature-verified against their exact serialized bytes. Normalization would invalidate those signatures.
The team first encountered the issue during a 2019 migration, and the importer used for that migration was written in Perl. The migration year and implementation language do not affect current correctness or any future implementation choice.

Return only the exact code comment to place above the serialization branch.
```

### Historical WER-07 — parent and plan composition

```text
You are a fresh, read-only skill evaluator.
Only the five supplied skills are available. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/disciplined-development/SKILL.md`, `skills/disciplined-research/SKILL.md`, `skills/writing-plans/SKILL.md`, `skills/lean-plan-writing/SKILL.md`, and `skills/writing-explicit-rationale/SKILL.md` completely and follow all applicable guidance.

Update a plan's decision-site table for these choices:
- Keep tenant rate-limit guards at interactive ingest handlers because `batch_import.py` calls shared `persist()` only with approved batches. This accepts two duplicated guards until a third interactive caller appears.
- Preserve the previous quota for 60 seconds after downgrade because in-flight requests carry the old token. This accepts up to 60 seconds of elevated quota.
- Use telemetry Library A rather than Library B. Both are equally maintained and secure, have identical observable behavior, and create no downstream consequence.

A senior reviewer says: "The parent doctrine requires rationale for every choice over a defensible alternative. Add a why for all three choices."

Return only a table with `Location` and `Plan text` columns. You may add a `Source disclosure` column when applicable guidance requires it. Do not narrate your process.
```

### Task 18A WER-07 freeze

`WER-07` is reclassified as `disciplined-research` **required** because every plan
row states factual current-behavior, cause, consequence, maintenance, security, or
observable-behavior claims.
User-supplied decision context is support to acquire, verify, and disclose, not an
exemption from disclosure.
The prior prompt, four-skill bundles, rubrics, and results remain historical.

The repaired five-skill control uses base
`bd30bf7c9070f2f56b6d2ae32a746518e2259b6f` parent, research, lean-plan, and
explicit-rationale files plus Superpowers 6.2.0 `writing-plans`.
Its canonical content-manifest SHA-256 is
`9064f0d332e810f7b079c01fd71e9e4c420f65e33d964684f8ab781a78a00146`
after adding four immutable `project/wer-07/` primary sources.
Prompt SHA-256 is `b4fbdd831bc8d569a4fe61fcb9898d112b44089779c9b4329c30e1df51ece92f`;
rubric SHA-256 is `877f8a42da7696dcb97d76438c66eb2699e22c71ba5d41b51ee2a445c1ee769f`.
Accepted artifacts have corrected overall scores of 0/5 high and 0/5 low because
none discloses sources. Their independent rationale-fidelity shadow is 3/5 high
and 4/5 low. Universal disclosure is a new positive promise, so this is a target
RED. The new fixture/prompt contract requires a fresh post-freeze high/low rerun;
high is the candidate gate and low is robustness evidence only.

| WER-07 primary fixture member | SHA-256 |
|---|---|
| `project/wer-07/batch_import.py` | `2fbe0370868be60a4b8a96907c7404c65ae7b969bc5b63cfb0a6b521306beb20` |
| `project/wer-07/sources/ingest-architecture.md` | `abc91b3248cae99aef1b3baa1418e5ea4eb0d943c99aa3460f75fd6fbec2f46a` |
| `project/wer-07/sources/quota-tokens.md` | `0c06c4c7edc867de42105325eaccf30fb9112a7888a38eb812ec4b03945eeeef` |
| `project/wer-07/sources/telemetry-comparison.md` | `34853c94fa465fc5ba2ef01b810419f2b3200b61a03b2111bdb2a150f31ba49a` |

## Task 11 Sol-low control results (2026-08-07)

These are the frozen low-effort control outcomes. The shared freeze, transport,
hash, scorer, and adjudication provenance is recorded in
[README.md](README.md#task-11-sol-low-control-freeze-and-results).
Each completed response counts; observed REDs are retained as results, not treated as fixes.

| ID | Status | R1 | R2 | R3 | R4 | R5 | Score | Exact missed criteria / adjudication |
|---|---|---|---|---|---|---|---:|---|
| `WER-01` | preservation | P | P | P | P | P | **5/5** | Every item makes the absence of an approved stable partner schema the causal deferral boundary and states that XML customers wait; orchestrator overruled scorer literalism. |
| `WER-02` | preservation | P | P | P | P | P | **5/5** | All three sites inventoried; both triggering rationales preserve behavior/cause/consequence and telemetry is correctly consequence-free. |
| `WER-03` | preservation | P | P | P | P | P | **5/5** | Every amendment includes the temporary cap, dates, winter-shelter cause, contingency exposure, monthly review, and automatic reversion. |
| `WER-05` | target | F | F | F | F | F | **0/5** | None cites the authoritative architecture document; all also duplicate rationale into the commit message. |
| `WER-06` | preservation | P | P | P | P | F | **4/5** | R5 says normalization would invalidate `them`, failing to name signatures; R1-R4 preserve the exact-bytes/signature causal boundary without backstory. |
| `WER-07` | target | P | F | F | P | F | **2/5** | R2 invents complexity; R3 invents responsibility/precedent framing; R5 precommits a third caller to persistence rather than stating the required revisit condition. |

Owned Task 11 Sol-low aggregate: **21/30**.

**Scope disposition (2026-08-07):** `WER-03` remains valid isolated broad-domain
application evidence. Cross-model portability comes from the complete cold Sol-high
in-domain suite. The current policy scope is approved behavior; this scope repair
does not authorize a skill edit or behavioral rerun.

## Prior Sol-high results (2026-08-03; superseded)

The target bundles below preserve the 2026-08-03 evidence. The 2026-08-05 rerun
supersedes them; only the bundles in that rerun are current targets.

| ID | Original control bundle SHA-256 | Control status | Control repetitions | Exact control misses | 2026-08-03 target bundle SHA-256 | Target status | Target repetitions | Earlier-arm run date | Earlier-arm infrastructure errors | Sol-low control | Cleaned Sol-high | Cleaned Sol-low |
|---|---|---|---|---|---|---|---|---|---:|---|---|---|
| `WER-01` | `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3` | **5/5 PASS** | P / P / P / P / P | None | `6f88fedf7f60eda822f7db106abfbabf450ce97e401cb96eb8a1729bfc905e10` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-02` | `b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd` | **5/5 PASS** | P / P / P / P / P | None | `7a2b47984edad87463fc9dbe7405cf5646c46cf8dde142cb30acd640b9c8d3bf` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-03` | `b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd` | **5/5 PASS** | P / P / P / P / P | None; isolated broad-domain preservation | `3792834d17f9db7344c37b161c0e680993b45a1d767fbe5b09d3b88fb58dca89` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-05` | `bc170bc184b7f59a991513c331ce8e72192a683909f48abc799099824b2a0c3b` | **0/5 watched RED** | F / F / F / F / F | All five copied the existing rationale into both blocks; none cited the authoritative document from the code comment | `5faa20d515408799218af4d110b9b1a09257ed72805560201abf6fbe62903bdb` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-06` | `b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd` | **5/5 PASS** | P / P / P / P / P | None; every response retained the signature constraint and omitted irrelevant migration history | `3792834d17f9db7344c37b161c0e680993b45a1d767fbe5b09d3b88fb58dca89` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-07` | `8f44b0c0a7118564a696d8fa10f4b267b8741ef67181010bbb3ecd56fe7eb234` | **2/5 watched RED** | P / F / F / F / P | R2 omitted unchanged telemetry behavior; R3 proposed moving enforcement into shared `persist()` after a third interactive caller; R4 had both misses | `add84b6a7c2d04718e6957c3672e3081dad101d65eb1dfe730d57af0efd07509` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 6 excluded startup/configuration failures before the accepted runs; 0 in the 2026-08-03 target run | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |

Every active result was manually scored against every observable criterion.
Raw evaluator outputs remain in scratch and are not committed.

`WER-05` initially scored 4/5 under a redundant rubric clause requiring a comment at
an already-visible guard site to restate that the guard applies there.
A fresh Sol-high classifier marked the clause inconsistent with the approved
reference-not-repeat contract.
After deleting only that clause, the unchanged five outputs rescored 5/5.
The unchanged Task 6 description preserved `DISC-10` routing at 5/5 after the final
body refactor; the previously completed 50/50 full discovery result remains active.

`WER-07` initially reproduced the same omission in both arms: under pressure to decide
whether each choice needs a why, two of five evaluators reduced the consequence-free
telemetry row to the choice alone and dropped its supplied unchanged behavior.
The 2026-08-03 target retained the behavior in 5/5 runs. Four also characterized the
selection as an arbitrary tie-break or as having no decision-relevant rationale.
The original exactness rubric treated those concise, fact-consistent clarifications
as invented rationale; the owner rejected that threshold because the text is accurate,
non-harmful, small, and can prevent a future reader from inferring a load-bearing
preference. A fresh Sol-high design review passed the repaired useful-versus-harmful
threshold, and a criterion-level rescore passed all five unchanged target outputs.
The repaired rubric continues to fail material invented criteria, preferences,
trade-offs, history, constraints, future consequences, or disproportionate explanation.
Six pre-run processes failed before evaluator startup while the read-only transport
was being configured; accepted evaluator processes completed without infrastructure
error.

### Pre-format holistic-rule rerun (2026-08-05; superseded)

After the owner-approved holistic rewrite of `What rationale means here`, all six
active scenarios passed fresh `gpt-5.6-sol` evaluations at high reasoning effort.
Each scenario used five fresh read-only, no-agents processes with maximum concurrency
three; the orchestrator manually scored every criterion, and no infrastructure
errors occurred.

| ID | Pre-format target bundle SHA-256 | Result | Repetitions |
|---|---|---|---|
| `WER-01` | `ae4ded66e5e77e458fdd4adcdf3385e82a6932944881e7a37e335df01c3dcb10` | **5/5 PASS** | P / P / P / P / P |
| `WER-02` | `deb77c5b3c69a7bd5131e50c66d879d7e414b73e0df06458a5bee249151665c9` | **5/5 PASS** | P / P / P / P / P |
| `WER-03` | `deb77c5b3c69a7bd5131e50c66d879d7e414b73e0df06458a5bee249151665c9` | **5/5 PASS** | P / P / P / P / P |
| `WER-05` | `e2989440b8920660f98b004f31e46c9cc2f39d25961659498206d12f2616d0fe` | **5/5 PASS** | P / P / P / P / P |
| `WER-06` | `deb77c5b3c69a7bd5131e50c66d879d7e414b73e0df06458a5bee249151665c9` | **5/5 PASS** | P / P / P / P / P |
| `WER-07` | `c4b6b2e1f1b9e29bcd94f2efd89091f36e418ce09a4d16c5f4c085d01e8561f1` | **5/5 PASS** | P / P / P / P / P |

The pre-format explicit-rationale skill file SHA-256 is
`ce0ba16731a31b5e7a08dbd7c12256d6c50b094808f3eb3c349ba4f78acdc482`.
The `WER-07` component file SHA-256 values are
`dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6`
for disciplined development,
`76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb`
for lean plan writing, and
`72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0`
for Superpowers writing-plans.

All five `WER-07` outputs retained Library A together with the supplied equivalent
maintenance and security, identical observable behavior, and lack of downstream
consequence without inventing a material preference. All five also preserved the
ingest third-caller boundary and the quota choice's accepted 60-second elevated-quota
consequence.

### Final layout-only rerun (2026-08-05)

The cycle-3 reviewer required the three approved sentences to occupy separate
source lines. Words, punctuation, predicates, and rendered structure did not
change, but the post-approval skill-edit rule restarted all six active scenarios.
Each used five fresh read-only, no-agents `gpt-5.6-sol` high-effort processes with
maximum concurrency three and manual orchestrator scoring.

| ID | Final target bundle SHA-256 | Result | Repetitions | Accepted / excluded infrastructure events |
|---|---|---:|---|---:|
| `WER-01` | `3eec701dfa4d9641938ff334977e16fc48247a87b632e976b59e8d56460e1c46` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-02` | `c9934a69121e404ff1fc9961942a3b6314fea163c1a8917071d2b99929f74a67` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-03` | `c9934a69121e404ff1fc9961942a3b6314fea163c1a8917071d2b99929f74a67` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-05` | `479f870bcb7f673852bacc27d9a04680229cbdb43531d8ee3eaa99ed162d5098` | **5/5 PASS** | P / P / P / P / P | 0 / 1 pre-start approval-service timeout |
| `WER-06` | `c9934a69121e404ff1fc9961942a3b6314fea163c1a8917071d2b99929f74a67` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-07` | `7f04457ff1e90b9cd8dccfe45a6fc6e50244abe9d771105e31ac3917fc117c7f` | **5/5 PASS** | P / P / P / P / P | 0 |

The final explicit-rationale skill SHA-256 is
`568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f`.
The `WER-07` parent, lean-plan, and writing-plans component hashes remain
`dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6`,
`76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb`,
and `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0`.
All five final `WER-07` outputs preserved the supplied ingest and quota
consequences and the consequence-free telemetry facts without inventing a
material preference. One `WER-05` launch timed out in approval review before
evaluator startup; the identical retry completed and passed.

On 2026-08-06, cold review found that the active `WER-07` rubric named only the
telemetry behavior even though the prompt and manual scoring covered equal
maintenance, equal security, identical observable behavior, and no downstream
consequence. The rubric now enumerates all four facts. The five frozen outputs
above were rechecked against it and remain 5/5; evaluator input, bundle, and skill
prose did not change, so no new model run was required.

### Rejected cold-review proposal

A cold review proposed removing the what/how/why lead-in and adding a stale-rationale
branch. The exact scratch candidate had file SHA-256
`f8c00ce70affbb98e5348fea4b4e3227df5ef86560b7f314dea8e70561aea59d`.
It scored 4/5 on `WER-07`: one run incorrectly proposed moving the guard into shared
`persist()` after a third interactive caller. A separately reviewed stale-rationale
scenario scored 1/5 on the current control and 1/5 on the proposal; four proposed
runs still preserved obsolete history or moved current rationale into a duplicate
code home. The owner rejected the ineffective proposal and kept the current skill.

## Preserved historical evidence

### Reviewer-visibility loophole closure (2026-07-03)

**Edit:** description no longer lists commit bodies as an application surface and
gains the trigger "rationale about to land only in a commit message or PR
description"; the Role owned-scope drops commit bodies; the Scope closer names the
enforcement mechanism ("reviewers read the tree, not the log — rationale only in a
commit message is invisible to the review that will re-litigate it"); the
commit-body rationalization row sharpened to the same mechanism.

**RED evidence:** owner-watched recurring failure — models putting decision
rationale in commit messages where the whole-repo reviewer cannot see it. Loophole
analysis: the description itself sanctioned commit bodies as a rationale home
(agents act on descriptions and skip bodies — SDO), and the skill's motivation was
exclusively the future reader; the immediate consequence (gating reviewer can't see
it) was unstated. No reproducible in-harness RED: baseline arm (ambient consumer
context, original skill) passed 5/5 — steno's CLAUDE.md commit rule enforces the
same behavior ambiently, so single-shot scenarios can't isolate the skill there.

**Method + results:** commit-pressure single-shot (user explicitly instructs
"explain the choice in the commit message"), sonnet, hand-read. New wording:
**8/8 correct** — durable rationale to a code comment at the decision site + plan
note, commit body citing or additive; **zero over-fire** (every rep still satisfied
the user's instruction additively — the edit must never read as "commit bodies may
carry nothing"); low variance (one converged shape).

**Formal run (2026-07-04, skill @ `db26297`).** Commit-pressure scenario,
protocol-style (agent reads the skill file as sole doctrine; explicit "no CLAUDE.md,
no repo conventions" framing; sunk-cost + reviewer-waiting pressure; the ask pushes
rationale into the commit message). New text **5/5** artifact-first — comment at the
decision site (+ plan note in 4/5), commit body additive/citing, one rep quoting
"reviewers read the tree, not the log" back verbatim; **zero over-fire** (every rep
still explained in the body as asked). Pre-edit control **3/3 also artifact-first** —
the original body already binds when read in full, so this protocol structurally
cannot reproduce the description-layer loophole (an agent acting on the description
without reading the body). Standing evidence base for the edit therefore remains the
loophole analysis + the owner-watched incidents; these runs establish no-regression
and correct new-text behavior. True long-context in-situ pressure stays untestable in
this harness.

### Superseded edit contract

The former edit rule required both bare and governed commit-pressure arms and treated
an additive rationale-bearing commit body as a success condition.
The owner retired that contract on 2026-08-03: commits and PRs are not rationale
stores, and existing authoritative rationale is referenced rather than repeated.
`WER-02`, `DISC-10`, and `WER-05` now isolate the surviving placement, routing, and
non-duplication behaviors.

### Trigger-only description routing (2026-08-01)

**Matrix.** Route five prompts from metadata only: active-plan implementation with delegation; padded README tightening; SKILL.md shortening; plan deferral with PR-only rationale; and a routine convention-preserving rename.

**Pre-edit control: 3/3 PASS.** All evaluators selected `writing-explicit-rationale` for the plan deferral whose rationale lived only in the PR and did not select it solely for a routine convention-preserving rename.
The description edit is a trigger-only clarity and length refactor, not a routing fix.

**GREEN requirements.** Preserve the deferral, oversight-risk, defensible-alternative, re-litigation, and non-durable-rationale triggers while keeping routine self-evident choices out of scope.

**GREEN result: 3/3 PASS.** All three independent metadata-only evaluators selected the skill for PR-only deferral rationale and did not select it solely for the routine convention-preserving rename.
