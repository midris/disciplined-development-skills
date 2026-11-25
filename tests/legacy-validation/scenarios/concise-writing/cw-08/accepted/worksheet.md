# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/concise-writing/cw-08 |
| Scenario ID | cw-08 |
| Scenario purpose | Apply concise writing to policy prose while preserving every protected eligibility, deadline, accommodation, appeal, and navigation fact. |
| Run ID | 20260906T031840280Z-cw-08-3537c587-cf02-4147-b690-72d57be62a69-exbm1m7j |
| Provider | codex |
| Provider CLI version | Unknown — no contemporaneous CLI-version evidence found in the accepted record or matching retained scratch logs. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-06T03:18:40.280Z |
| Finished | 2026-09-06T03:18:53.689Z |
| Duration seconds | 13.409 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | 389a2a40a9f06ba81f201319894f1d57172422d080ee2a475736bc55947da779 |
| Prompt template | prompt-template.txt | 91db2173ab9bb9a8251c3571fdf26bf485e4d527ce92987d89e2c369a5b3b29b |
| Rendered prompt | prompt.txt | dafe0e4260bdadb2d95e653656a8d70e837045caf262de15644d186e55024e91 |
| Concise-writing skill | workspace/fixture/skills/concise-writing/SKILL.md | 4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/concise-writing/cw-08/rubric.md | 8247b6191ecda18cbeff074b59a530552355cb5ed3096e3b5cc0f24bd431d965 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Remove meta-framing | Remove the opener that merely announces what the section explains. | PASS | final.txt:1-7 | The result starts with the section heading and eligibility rule; the original meta-opener is gone. |
| Remove duplicate deadline | State the October 15, 5:00 p.m. ET deadline once. | PASS | final.txt:5 | The deadline appears once, with the date, time, and time zone preserved. |
| Eligibility | Preserve `501(c)(3)` status and an annual budget strictly below $2 million. | PASS | final.txt:3 | Both constraints are retained; “below” preserves the strict threshold. |
| Fiscal sponsor exception | Preserve the path for organizations without `501(c)(3)` status to apply through an eligible fiscal sponsor. | PASS | final.txt:3 | The exception and sponsor eligibility requirement are explicit. |
| Sponsor navigation | Preserve navigation to `Appendix A` for sponsor requirements. | PASS | final.txt:3 | The result says “see Appendix A for requirements.” |
| Late applications | Preserve that late applications are not reviewed. | PASS | final.txt:5 | The rule is stated directly. |
| Accommodation channel and lead time | Preserve an explicit instruction to email exactly `access@communityarts.example` at least five business days before the deadline. | PASS | final.txt:5 | The action, exact destination, minimum lead time, and deadline reference are all retained. |
| Appeal window | Preserve denied applicants' ten-calendar-day appeal window. | PASS | final.txt:7 | The result retains denied applicants and “within 10 calendar days.” |
| Appeal navigation | Preserve navigation to `Appeals` for the required form. | PASS | final.txt:7 | The result directs applicants to the form specified in Appeals. |
| Appeal finality | Preserve finality after the appeal decision. | PASS | final.txt:7 | “Appeal decisions are final” preserves the rule. |
| No unsupported content | Add no software, repository, or other unsupported assumption. | PASS | final.txt:1-7 | Every statement is supported by the supplied policy. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer | N/A | rubric.md; final.txt | The scenario has no renderer, parser, schema, or production consumer whose exact output contract can be authenticated. Required content and “return only” remain semantic and task-fidelity constraints. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Return only the revised section | PASS | final.txt:1-7 | The retained final artifact contains only the revised policy section. |
| Read the directly invoked skill completely | PASS | stdout.txt | The provider used one `cat` command on the supplied skill; the captured output reaches the skill's final sentence. |
| No unnecessary blocker or procedure | PASS | final.txt:1-7 | The response completes the edit directly without blocker or procedural narration. |
| Read-only evaluator boundary | PASS | stdout.txt; result.json | The provider made one read-only command against a supplied fixture and performed no edits, Git mutations, network calls, or agent dispatches; retained evidence is empty. |
| Fixture-only execution inputs | PASS | stdout.txt; result.json | The provider read only `fixture/skills/concise-writing/SKILL.md`, the sole declared fixture. No ambient skill or repository file was accessed. |

## Readability

| Observation | Evidence |
|---|---|
| Three short paragraphs group eligibility, application timing/accommodations, and appeals while preserving the original section heading. | final.txt:1-7 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | PASS |
| Rationale | The provider removes the meta-opener and duplicate deadline while preserving every protected eligibility, fiscal-sponsor, navigation, deadline, accommodation, and appeal fact. It introduces no unsupported content and uses only the declared concise-writing fixture. |
| Disposition | Accepted by owner on 2026-09-05. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None material. “Appeal decisions are final” is equivalent to finality after the appeal decision, and “using the form specified in Appeals” preserves the required navigation. |
| Scenario defects | None observed. The fixture contains exactly the directly invoked skill, and the rubric identifies the protected facts precisely. |
| Proposed methodology changes | None. |
