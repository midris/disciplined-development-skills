# Full SSR regression with the revised complete-claim instruction

All 66 subjects and ten complete-output reviews are assessed. The reviewers agreed on all 48 repairs.

All 48 repairs are complete in the retained Git trees.
Codex and Claude each passed all 24 repair tasks.
In all 18 notification-policy repairs, the trace contains the complete wrapped troubleshooting sentence before the first edit, and the committed documentation says the fourth failed send exhausts delivery.
The [claim inspection record](claim-inspection.json) identifies the corresponding response in each trace.

| Full-suite outcome | Codex | Claude |
| --- | ---: | ---: |
| Complete, preserved and committed repair | 24/24 | 24/24 |
| Timely full skill load on a native rename | 3/3 | 3/3 |
| Timely full skill load on a native reviewer correction | 3/3 | 2/3 |
| Appropriate non-use on a tests-only task | 3/3 | 2/3 |
| Appropriate non-use on an unrelated explanation | 3/3 | 3/3 |
| Useful large-inventory reports | 3/3 | 3/3 |
| Commit/report account meets the full P3 criterion | 14/21 | 11/21 |

Each provider ran three fresh repetitions of all eleven scenarios.
Six reporting-only outputs and twelve negative-selection observations have their own denominators.
All 36 explicit repair runs met both search/triage and commit-grouping criteria.
The [design](../../../../plans/specs/2026-11-07-ssr-complete-claim-regression.md), [schedule](preparation/schedule.json) and [frozen skill](preparation/skill/SKILL.md) identify the tested scope and version.
The candidate SHA-256 is `9bdd02d316c57fd320fe25feddbe30d08af57ffc541742b40b1d08ec3e68c224`, identical to the candidate in complete-claim-01, including its description.

## Discovery and task boundaries

Claude loaded the skill before editing on five of six native positive tasks, compared with three of six in the previous full regression.
Codex loaded it on six of six in both regressions.
The historical comparison used the earlier description and paragraph, and Claude Code changed from 2.1.312 to 2.1.316.
The samples cover two exposed triggers with three repetitions each. They cannot isolate how much of the difference comes from wording, runtime or run-to-run variation.
The [previous full regression](../count-free-regression-01/count-free-regression-01-assessment.md) and [focused paragraph comparison](../complete-claim-01/complete-claim-01-assessment.md) retain their own evidence.

In slot 62, Claude's catalog listed SSR. The ordered trace contains a repository search and a full read of the three current documents, with no Skill invocation or targeted skill read.
Claude still corrected and committed all three claims and explained why it preserved the historical policy and download helper.
The commit lacks a sweep inventory.

In slot 64, Claude ran the requested tests once, then searched the old setting and classified three archive/vendor matches.
The files were preserved and the tests passed. The extra sweep fails the tests-only D1 rule even though Claude never opened the skill.
All twelve negative tasks avoided loading the skill. Eleven also avoided applying its sweep procedure.
All six explanation runs calculated the expected expiry of 1900.

## Repair completeness

- **Delivery policy** — all three current documents agree on at most four attempts and stopping on success. Historical and independent download policies retain their meaning. All seven disposable behavior tests pass for each of the 18 repair projects.
- **Session setting** — all twelve explicit/native renames update the six current consumers and preserve the 30-minute default, positive-value validation, partner constraint, refresh-cost trade-off and independent vendor settings. Scripts report the new key and expiry 1900 from both working directories.
- **Shiv** — all six repairs restore the four executable consumers. Each consumer produces the correct runnable greeting archive. The script works outside the project, the short alias works, the retired flag is rejected, and the independent inventory utility works. CI commands were replayed locally. Claude’s provider-specific ignore file matches the configured fixture.
- **Moved guide** — all six repairs resolve each document-relative link and emit the complete moved guide from both working directories. The service guide, historical record and vendor guide survive intact.
- **Local correction** — all six repairs change only the malformed glossary heading. The definition, related terms, shipping phrase, configuration and README links are preserved.

## Reporting

Seventeen of 42 P3 observations missed at least one reporting requirement. Most combined required paths or outcomes into one inventory row.
All six large-inventory outputs kept the eleven supplied groups, including both dispositions for the same document, and attributed the records to the supplied inventory.
Exact reference counts were optional throughout.

In slot 18, Claude repaired the wrapped troubleshooting claim, then classified its second line as generic attempt wording in the commit message.
In slots 43 and 56, Claude claimed post-edit searches absent from the complete traces. The retained files and independent replay establish the correct repairs.
Some other reports overstated which matches remained or cited checks performed only after the commit.
These issues affect the accuracy of the account. Direct project and commit inspection supplied the evidence for the functional judgments.

## Execution and review

The first 24 subjects and four audited reviews passed the [checkpoint](focused-gate.json).
All remaining 42 subjects then completed. There were zero replacements or retries.
The two provider assessments link each execution to its canonical score: [Codex](claim-full-codex-01-assessment.md) and [Claude](claim-full-claude-01-assessment.md).

Codex CLI 0.166.0 ran gpt-5.6-sol at low effort. Claude Code 2.1.316 ran claude-opus-5-5 at low effort.
Eleven installed-runtime checks passed before dispatch. Each subject’s complete retained inventory, provider identity and score hash was verified.
Review packets use Git inspection with index-cache refresh disabled and retain immutable review-time index snapshots. All 66 subject inventories matched after building the packets.
The hook suite passed 263 tests with three environment skips.

The active assessor prepared the inputs and saw the condition and prior results.
Separate Opus-medium reviewers received complete original and final projects, delivered responses and neutral execution evidence under a read-only tool boundary.
Native discovery, claim delivery and actual search order were judged from the subject traces in the active session.
See [review reconciliation](evaluation/README.md) and [verification](verification.json).

The study used 66 subject calls, ten evaluator calls and zero retries. The runners recorded 2,711.992 subject seconds and 1,775.081 review seconds. The estimated 105 active minutes include that time once, plus qualification, assessment and closure. The original forecast was 180–260 minutes. Production adoption remains an owner decision.
