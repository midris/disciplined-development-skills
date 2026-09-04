# Sweeping Stale References Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-04. All six scenarios remain in the catalog, and no scenario contract
required repair during this audit. The accepted set contains one judgeable
high-effort run per scenario and is intended to develop the scoring method and test
process, not to measure skill effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/sweeping-stale-references/SKILL.md` had SHA-256
`d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.
All accepted runs used Codex `gpt-5.6-sol` at high effort. This is a human-authored
audit record, not a generated manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [SSR-01](ssr-01/README.md) | Keep | Tests an end-to-end symbol-and-prose rename: inspect and search the supplied project, identify every update, preserve the attached rationale, and return reconciled sweep and verification evidence. | The [accepted observation](ssr-01/accepted/worksheet.md) is a judgeable `FAIL`. SSR-I1, SSR-I2, SSR-I4, and task fidelity passed. SSR-I3 failed because the artifact's generic `prose` label did not demonstrate preservation of the partner constraint or accepted refresh cost. |
| [SSR-02](ssr-02/README.md) | Keep | Tests resistance to one-reviewer-hit and IDE-sufficiency pressure across code, comments, docs, fixtures, config, scripts, CI, build, archive, vendor, and immutable history. | The [accepted observation](ssr-02/accepted/worksheet.md) is a judgeable `PASS`. It rejected both shortcuts, classified all 13 mutable matches, excluded three immutable-history hits, and reconciled every path, location, outcome, and count. The surrounding Markdown fence is a non-blocking presentation observation. |
| [SSR-03](ssr-03/README.md) | Keep | Tests large-sweep grouping by path and outcome without sacrificing precise locations, reasons, counts, or evidence to a normal commit-body size preference. | The [accepted observation](ssr-03/accepted/worksheet.md) is a judgeable `PASS`. SSR-I2 and SSR-I4 passed: all ten groups and their line ranges reconciled to 80 updates, 40 intentionally stale matches, 6 false positives, and 126 total matches. |
| [SSR-05](ssr-05/README.md) | Keep | Tests the required negative branch after a complete search proves that a terminology correction affects only one file. | The [accepted observation](ssr-05/accepted/worksheet.md) is a judgeable `PASS`. SSR-I4 passed: the response used the truthful `References swept: n/a` form before verification and invented no sibling match or blocker. |
| [SSR-06](ssr-06/README.md) | Keep | Isolates exact replacement inventory for the SSR-01 fixture without independently grading rationale preservation. | The [accepted observation](ssr-06/accepted/worksheet.md) is a judgeable `PASS`. SSR-I2 and SSR-I4 passed: the response distinguished one symbol and two prose replacements and reported no fourth match. Workspace-prefixed paths and evaluator-status verification are non-blocking task-fidelity observations. |
| [SSR-07](ssr-07/README.md) | Keep | Isolates rationale preservation for the SSR-01 fixture without independently grading search or inventory mechanics. | The [accepted observation](ssr-07/accepted/worksheet.md) is a judgeable `PASS`. SSR-I3 passed: the new session terminology retained the partner's rejection of longer sessions and the accepted cost of more frequent refreshes for compatibility. |

## Catalog assessment

The apparent overlaps protect distinct failure boundaries:

- SSR-01 owns end-to-end composition, while SSR-06 and SSR-07 isolate its exact
  inventory and rationale-preservation components.
- SSR-02 tests reviewer and IDE pressure over a broad mixed-category inventory;
  SSR-03 separately tests grouping and evidence retention at scale.
- SSR-05 tests the mutually exclusive no-sibling output branch.

Together the catalog exercises all four charter invariants. SSR-I1 is directly
covered by SSR-01 and SSR-02. SSR-I2 is exercised by the positive inventories and
classification cases. SSR-I3's one-batch behavior passes in SSR-02, and its atomic
rationale behavior passes in SSR-07, but the combined SSR-01 artifact fails to make
that rationale preservation visible. SSR-I4 has broad positive, scaled, exact
inventory, and negative-form coverage.

The contrast between SSR-01, SSR-06, and SSR-07 is the most useful first-run
observation. The model can enumerate the exact replacements when inventory is
isolated and can preserve the complete rationale when that meaning is isolated, yet
its composite commit-body artifact does not demonstrate both at once. That is a
composition seam worth measuring with repeated runs; one observation does not show
whether the skill is ineffective or the result is ordinary model variance.

None of the scenarios has an authenticated deterministic consumer. Exact Markdown
fencing, repository-relative path style, and evaluator-status narration therefore
remain task-fidelity concerns unless they obscure or contradict the owned semantic
artifact. SSR-06 would benefit from SSR-01's explicit project-level-verification
guard in a later cleanup, but no prompt repair is necessary to preserve this
judgeable baseline.

SSR-01 also exposed an evidence-lifecycle question. Its scratch provider transcript
shows the exact file inspection and search actions, while the accepted result keeps
only the transcript hash. Before relying heavily on action-based criteria, decide
whether the final artifact must carry enough evidence for later re-adjudication or
whether selected provider transcripts can become accepted evidence. This is a
methodology decision, not a runner change required by the current catalog.

## Execution-process observation

The early runs repeatedly produced an artificial first `INFRA_RETRY`: the outer
workspace sandbox prevented the Codex CLI's in-process app-server from initializing,
while the identical host-permitted invocation succeeded. SSR-06 and SSR-07 were run
with host permission immediately after exact-command approval and completed on the
first attempt. Future approved Codex provider commands should follow that practice;
the command, fixture, model, effort, and provider-owned workspace sandbox remain
unchanged.

Provider-free catalog checks pass. The complete local suite currently reports 172
passes and two environment-version failures unrelated to these records: the tests
pin Codex CLI `0.150.1` and Claude Code `2.1.250`, while the installed versions are
`0.153.2` and `2.1.260`. No pin or runner code was changed during this audit.

## Later effectiveness campaign

Once scenario coverage and scoring methodology are stable, effectiveness testing
should use multiple independent runs for each selected model-and-effort
configuration. The intended first matrix is `gpt-5.6-sol` at high, medium, and low
effort. A later `gpt-5.6-terra` high-effort arm may help determine whether another
model is a useful baseline subject. Repetition counts, acceptance thresholds,
aggregation, and comparison rules remain deliberately undecided; these six single
runs do not answer those questions.

## Next actions

1. Select the next skill catalog for the same scenario-by-scenario current-main
   audit and single-run process-development exercise.
2. Resolve the accepted-evidence policy for action-based criteria before the later
   effectiveness campaign.
3. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently established.
