# Sweeping Stale References adoption

The [806-word skill](../../../skills/sweeping-stale-references/SKILL.md) combines a revised discovery description with an instruction to read the complete claim or code block before classifying a match.
It asks for paths, changes and reasons for preserving other matches. Exact match counts are optional.
The owner adopted these bytes after the [full regression](results/complete-claim-regression-01/complete-claim-regression-01-assessment.md). The [protocol](protocol.md#full-regression-adoption) records the decision.

| Outcome on the adopted skill | Codex | Claude |
| --- | ---: | ---: |
| Complete, preserved and committed repairs | 24/24 | 24/24 |
| Read the complete wrapped troubleshooting claim before editing and corrected it | 9/9 | 9/9 |
| Loaded the skill before editing on native positive tasks | 6/6 | 5/6 |
| Avoided the sweep on tests-only and unrelated tasks | 6/6 | 5/6 |
| Commit or report met the full path-and-outcome reporting criterion | 14/21 | 11/21 |

Each provider ran three repetitions per scenario. These rows score overlapping aspects of the same 66 attempts.
Claude completed the native reviewer-correction repair even when it missed the skill load. On one tests-only task it ran the tests, then searched and classified references without making edits.
Of the 17 reporting misses, 12 came from the Shiv and initiating-rename cases. On each case, both models missed the full reporting criterion in all three repetitions.
Most misses combined paths or outcomes. Two Claude reports also claimed post-edit searches absent from the traces (slots 43 and 56). Other reports overstated the remaining matches or cited checks performed after the commit.
The owner accepted these reporting limits because direct inspection of the projects and commits verified the repairs.
Ten read-only Opus reviews covered all 48 repaired projects and agreed on all 144 functional judgments. The active assessor judged discovery, search timing and reporting from the traces. [Review packets and reconciliation](results/complete-claim-regression-01/evaluation/README.md)

The [earlier regression](results/count-free-regression-01/count-free-regression-01-assessment.md) and [focused paragraph comparison](results/complete-claim-01/complete-claim-01-assessment.md) explain the revision.
Both the skill and the Claude CLI changed between the full regressions. The observed load rates come from two exposed positive triggers and three repetitions each.

## Run the suite from a clean checkout

From the repository root on macOS with Git and uv:

```sh
cd tests/runner
uv sync --locked
uv run --locked --offline python ../skills/sweeping-stale-references/verify.py
uv run --locked --offline pytest -q ../skills/sweeping-stale-references
```

The verifier loads all 22 runner configurations, matches their prompts and fixture bytes to the manifests, compares the tested snapshot with the shipped skill, and checks the case cards, grading policy, 66 scheduled subject records and ten review audits.
It recomputes each provider’s functional, selection and reporting totals, checks the 18 indexed complete-claim observations, and reconciles the 144 first-pass review judgments with the scored repairs.
The offline tests exercise reference repairs and deliberately incomplete alternatives in disposable projects. Use the runner environment for pytest so the Shiv fixture’s shell commands also find its Python interpreter.

The six explicit repair cases cover a pressured correction, Shiv command consumers, a moved guide, semantic delivery-policy drift, an initiating rename, and a local correction.
A large-inventory reporting task and four native tasks complete the suite. The native tasks cover an ordinary rename, a reviewer correction, running tests, and an unrelated explanation.
The [schedule](results/complete-claim-regression-01/preparation/schedule.json), [case cards](results/complete-claim-regression-01/preparation/criteria/), [count-free policy](results/complete-claim-regression-01/preparation/policy.txt) and [interpretation](results/complete-claim-regression-01/preparation/interpretation.md) define what each run measures.
Case cards retain their frozen bytes. Their historical framework links refer to the [archived study framework](https://github.com/midris/disciplined-development-skills/blob/44766517c4550cd65c13c9fe0f489ac26efee1e0/plans/specs/2026-09-11-model-driven-skill-testing-framework.md).

For an approved live run, follow the [runner guide](../../runner/README.md) and pass one [frozen configuration](results/complete-claim-regression-01/preparation/configs/) to `skilltest run`.
The historical subjects used Codex CLI 0.166.0 with gpt-5.6-sol low and Claude Code 2.1.316 with claude-opus-5-5 low. For a discovery comparison, requalify the controlled catalog and inspect the ordered trace for actual skill delivery before the first edit.
The configs load the frozen snapshot so a later edit to the installed-source skill cannot silently change the historical arm.

## Trace the decision

Start with the [Codex](results/complete-claim-regression-01/claim-full-codex-01-run-index.json) and [Claude](results/complete-claim-regression-01/claim-full-claude-01-run-index.json) attempt indexes. Each identifies its frozen manifest, scored result, and private evidence inventory. All 66 subject attempts and ten reviews were retained, with zero retries.
The [evaluation ledger](results/complete-claim-regression-01/evaluation/evaluator-run-index.json) and packet reconciliations distinguish independent first passes from subsequent access to the active assessment.
The [archive](https://github.com/midris/disciplined-development-skills/tree/44766517c4550cd65c13c9fe0f489ac26efee1e0/skill-studies/sweeping-stale-references) preserves the previous studies and historical Git paths recorded in JSON.
Fetch the tag with `git fetch origin tag archive/study-foundation-sources` and use `git show <revision>:<path>` for revision-pinned source bytes.

For raw output, request access to the private Sweeping Stale References store from the study owner. Resolve the suffix following `skill-study-private/sweeping-stale-references/` under that store, match the inventory SHA-256 to the subject or evaluator ledger, then check the files listed in the inventory.
