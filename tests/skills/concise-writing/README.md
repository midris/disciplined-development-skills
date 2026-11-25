# Concise Writing adoption

The promoted [skill](../../../skills/concise-writing/SKILL.md) pairs the original body and examples with the rewritten description.
It broadens the cue to include document additions and comment edits, and expressly excludes numeric-only changes with fixed replies.
The owner accepted more frequent surplus loading on Codex in exchange for better selection on Claude.
The [closed protocol](protocol.md#closure-and-adoption) records that decision and the limits of the evidence.

| Comparison | What was observed |
| --- | --- |
| [Body and discovery](results/revised-body-discovery-01/evaluation/assessment.md) | On the comment task, Claude loaded the fixed revised body in 0/5 runs with the old description and 5/5 with the selected description. On the numeric-only task, Codex loaded it in 1/5 and 5/5 respectively. The extra loads missed the prespecified advancement criterion. |
| [Explicit comment editing](results/final-comparison-01/screen-02/evaluation/assessment.md) | Original and revised bodies each passed 5/5 on each provider with the selected description. |
| [Explicit operational handoff](results/final-comparison-01/handoff-02/evaluation/assessment.md) | Both bodies passed 5/5 on each provider. The earlier three repetitions per cell are included in the five. |
| [Replacement examples](results/final-comparison-01/examples-screen-01/evaluation/assessment.md) | With the exact adopted skill, Codex passed 2/3 and Claude 3/3. The Codex miss made an unconditional rollback step conditional. Replacement examples passed 3/3 on each provider. The agreed rule required a repeated benefit to replace the original examples. |

Across these comparisons the indexes retain 203 subject attempts, including one expired-authentication attempt and its authorized retry, plus 20 evaluator calls.
Subjects used Codex gpt-5.6-sol or Claude Sonnet 5 at low effort.
The reports distinguish the active assessment, Opus first passes and changes after exposure to prior scores.
Native discovery of the exact adopted description/body pair across the prepared suite remains unmeasured.

## Run the suite offline

From the checkout root, run:

```sh
cd tests/runner
uv sync --locked
uv run --locked --offline python ../skills/concise-writing/verify.py
uv run --locked --offline pytest -q ../skills/concise-writing/cases/fixtures/invocation-comments/test_check_fixture.py
```

The check loads all twenty runner configurations, checks the frozen source fixtures and installed-source skill digest, and verifies the manifest and result hashes for every indexed subject attempt.
The comment checker compares syntax and executable tokens without running a subject's code.
Grade the complete artifact against its task, sources and [case criteria](cases/criteria/) using the [assessment policy](assessment-policy.txt).

The [configurations](cases/configs/) cover recommendation editing, effective briefing, document addition, long handoff, explicit comment editing and drafting, and four native selection tasks.
They reproduce the prepared original-body arm for both providers with its skill source relocated to the shipped file.
The full twenty-configuration matrix was prepared for regression testing. Only the subsets identified above were collected for the final comparison.
For a separately approved live run, follow the [runner guide](../../runner/README.md) and pass one configuration to `skilltest run` from the runner environment.
Native selection also requires the controlled catalog and trace inspection documented in the discovery assessment.

## Evidence and retrieval

Each directory under [results](results/) includes the subject attempt indexes, result records, manifests, assessments and evaluator ledger for its batch.
Two manifests changed during collection. The earlier bytes sit under the adjacent `revisions/<git_revision>/` directory so each attempt resolves to its own freeze.
Historical paths, runtime identities and hashes in JSON retain their collection-time values.
Markdown links lead to the promoted record or its source in the [immutable study archive](https://github.com/midris/disciplined-development-skills/tree/44766517c4550cd65c13c9fe0f489ac26efee1e0/skill-studies/concise-writing).
That archive also contains the earlier baselines, comparator configs, development batches and collection scripts.

For original Git bytes, fetch `archive/study-foundation-sources` from origin and use `git show <git_revision>:<path>` with the values in the record.
For raw output, ask the study owner for authorized access to the private Concise Writing store.
Locate the run in its provider index or evaluator ledger, resolve the suffix following `skill-study-private/concise-writing/` under the supplied store root, and compare the inventory file's SHA-256 with the ledger before checking its listed bundle files.
