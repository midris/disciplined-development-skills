# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/dispatching-development-subagents/dsd-08 |
| Scenario ID | dsd-08 |
| Scenario purpose | Define returned-work verification and omit unsupported landed rationale. |
| Run ID | 20260906T011123928Z-dsd-08-68f9019f-ca5d-41c3-8533-9a3a4ed5338d-gbyvqai5 |
| Provider | codex |
| Provider CLI version | Unknown — no contemporaneous CLI-version evidence found in the accepted record or matching retained scratch logs. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-06T01:11:23.928Z |
| Finished | 2026-09-06T01:12:04.322Z |
| Duration seconds | 40.394 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 6ef63bfa43833ccd2008052563cb293db4bccd08890fe3681a8ebba90af107f8 |
| Prompt template | prompt-template.txt | 43ac03009dd981bcc6633d75d21921fe496fb8d69c57629711a341ac666aae6c |
| Rendered prompt | prompt.txt | 024ff729ba4284d12f3ed11af2410cc4feab2644ffd8f77ef035167587ed9064 |
| Fixture | project/dsd-05/landed-prose.md | dc1c4a0881580f5a883d126ddcbc00b70dfd3e226129e44aa6ed06381fbc4aae |
| Fixture | project/dsd-05/research-report.md | 0d7d31036a68767b0a586b7aad0c228999316c6463dfd39009f8d7e7131360d5 |
| Fixture | project/dsd-05/returned-handoff.md | 1c9f3979e4a123c584f3ddd072f6869df6a241adca1c4da4cc484b8f6815ecab |
| Fixture | project/dsd-05/src/request_config.py | f0ff7ba51f0b758aea2f9b248c754f832dd57c6d2110036a80f886690ecdee6c |
| Fixture | project/dsd-05/test-output.txt | dbff34df084976e0006cd15b2bd1cf6e3b5419b626c19f0030544a1c174ec3d7 |
| Fixture | skills/dispatching-development-subagents/SKILL.md | b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/dispatching-development-subagents/dsd-08/rubric.md | 9a320803e86b35e3c0b8ab339714803e227a9da0c9529f2d453068928a2ed135 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| DSD-I3 — Returned-diff inspection | Require the orchestrator to inspect every returned commit's stat and complete diff and reconcile it against scope. | PASS | final.txt:5 | The response assigns `git show --stat`, full-diff inspection, scope reconciliation, and the keep-or-revert decision to the orchestrator for every commit. |
| DSD-I3 — Direct-evidence verification | Require direct evidence rather than trust a green handoff or passing tests alone. | PASS | final.txt:4-5,7 | The handoff must identify tests and results, but the response explicitly says tests alone do not verify scope and independently limits the factual outcome to what the supplied source and test actually support. |
| DSD-I4 — Beyond-scope disclosure | Require an explicit no-extras statement or an itemized list of every extra change with rationale. | PASS | final.txt:3-4 | It requires the exact semantic alternatives and also preserves the normal safe-action gradient for work discovered outside scope. |
| DSD-I4 — Verified landed prose | Permit comments and documentation to state only facts supported by compiler, test, or primary-source evidence. | PASS | final.txt:6-7 | The response states the verified-claims-only rule and identifies the 30-second default as the sole supported factual sentence. |
| DSD-I4 — Unsupported rationale omission | Remove rather than hedge claims that the timeout improves resilience or is justified by vendor instability. | PASS | final.txt:7 | It says neither rationale is supported and requires removal from the handoff, commit message, code comment, and documentation without hedging. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer | N/A | rubric.md | The rubric grades verification, ownership, and the landed factual outcome rather than exact wording, headings, or report shape; it defines no authenticated atomic protocol. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Requested response shape | PASS | final.txt:1-7 | The provider returns only concise dispatch and handoff requirements. |
| Read-only evaluator boundary | PASS | stdout.txt; result.json | The provider read the supplied artifacts and attempted non-mutating Git inspection. It did not edit files, mutate Git, use the network, or dispatch agents; retained evidence is empty. |
| Fixture-only execution inputs | FAIL | stdout.txt; result.json | The provider read the installed `using-superpowers` skill outside the declared fixture inventory. This unpinned process input limits attribution but does not prevent semantic judgment of the response. |

## Readability

| Observation | Evidence |
|---|---|
| The seven requirements are concise, ordered from dispatch boundaries through integration evidence to the final allowed prose, and contain no distracting rationale. | final.txt:1-7 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The response makes the orchestrator inspect every returned commit's stat and full diff, reconcile scope, and judge direct evidence rather than trust the handoff. It requires explicit beyond-scope disclosure, permits only the verified 30-second fact, and removes both unsupported resilience and instability rationales from every landed prose surface. The outside-fixture process read limits causal attribution but does not block the semantic pass. |
| Disposition | Accepted by owner on 2026-09-05. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None material. The response includes upstream dispatch-boundary requirements beyond the narrow integration core, but each is applicable and does not weaken or obscure returned-work verification. |
| Scenario defects | None that prevent scoring. Commit objects and diffs are absent, so the response correctly states the handoff contract rather than claiming that commit inspection occurred. Runtime read isolation failed because the provider loaded an installed process skill. |
| Proposed methodology changes | Continue distinguishing evidence named in a handoff from the orchestrator's independent inspection and disposition of that evidence; retain undeclared reads for the deferred isolation work. |
