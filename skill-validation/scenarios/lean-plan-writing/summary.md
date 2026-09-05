# Lean Plan Writing Scenario Audit

## Status

The scenario-by-scenario audit and first current-main observations were completed
on 2026-09-04. All seven scenarios remain in the catalog, and no scenario contract
required repair during this audit. The accepted set contains one judgeable
high-effort run per scenario: six `PASS` results and one `FAIL`. These observations
are intended to develop the scoring method and test process, not to measure skill
effectiveness.

The audited subject was `main` at
`ac45ab2f3d467f5df0a49c543d8b3242423789b1`. The supplied
`skills/lean-plan-writing/SKILL.md` had SHA-256
`6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac`.
All accepted runs used Codex `gpt-5.6-sol` at high effort. The packaged
Superpowers 6.3.0 `writing-plans` dependency had SHA-256
`48508f44bbfd7d24b029fbf3a314f3cd14c9615599059366e922f47b8dc08cf2`.
This is a human-authored audit record, not a generated manifest.

## Scenario decisions

| Scenario | Decision | Coverage and rationale | Evidence disposition |
|---|---|---|---|
| [LP-01](lp-01/README.md) | Keep | Tests full-plan composition: upstream header, files, interfaces, TDD order, verification, and commit cadence must survive the lean prose-density override, while a small coupled change remains one merge unit. | The [accepted observation](lp-01/accepted/worksheet.md) is a judgeable `PASS` with a separate composition-owner `PASS`. LP-I1, LP-I2, LP-I4, and task fidelity passed; LP-I3 was not independently pressured. |
| [LP-02](lp-02/README.md) | Keep | Tests resistance to requests for full function bodies, complete test bodies, and copyable templates while requiring a complete tricky-parser behavior table. | The [accepted observation](lp-02/accepted/worksheet.md) is a judgeable `PASS` with a separate composition-owner `PASS`. LP-I1 through LP-I3 and task fidelity passed. LP-I4 was not independently pressured. |
| [LP-03](lp-03/README.md) | Keep | Tests the narrow exception permitting one short illustrative block when prose alone cannot unambiguously specify exact artifact bytes. | The [accepted observation](lp-03/accepted/worksheet.md) is a judgeable `PASS` with a separate composition-owner `PASS`. The sole four-line block mechanically matched the required 72-byte UTF-8/LF contract, and LP-I1 through LP-I3 and task fidelity passed. |
| [LP-05](lp-05/README.md) | Keep | Tests loud edge inventory for a CSV replacement: absent/empty, malformed, maximum/oversized, uniqueness, atomic visibility, and actionable errors. | The [accepted observation](lp-05/accepted/worksheet.md) is a judgeable `PASS` with a separate composition-owner `PASS`. LP-I1 through LP-I4 and task fidelity passed. Upstream TDD ordering was intentionally not rescored because the rubric reserves it for LP-01. |
| [LP-06](lp-06/README.md) | Keep | Tests quiet operational edges for a nightly digest: no events, malformed events, millions-scale pagination, shared quota, retries/overlap, per-account isolation, and local-day behavior. | The [accepted observation](lp-06/accepted/worksheet.md) is a judgeable `PASS` with a separate composition-owner `PASS`. LP-I1 through LP-I4, task fidelity, and the scenario's TDD-order requirement passed. A supplementary unnamed repository-wide test command is a non-blocking precision observation because every required verification path is concrete. |
| [LP-07](lp-07/README.md) | Keep | Tests whether an oversized four-subsystem program is split at qualitative, independently green review boundaries while resisting supplied numeric-size bait. | The [accepted observation](lp-07/accepted/worksheet.md) is a judgeable `FAIL` with a separate composition-owner `PASS`. The response correctly rejected the monolith, produced four ordered subsystem PRs, and named every green gate, but failed LP-I4's qualitative-boundary polarity by repeating “six commits and 35–45 KB” in the boundary rule. |
| [LP-08](lp-08/README.md) | Keep | Tests the opposite boundary polarity: a small schema/loader/test rename must remain one atomic PR because every per-file intermediate state is red or inconsistent. | The [accepted observation](lp-08/accepted/worksheet.md) is a judgeable `PASS` with a separate composition-owner `PASS`. All LP-I4 criteria and task fidelity passed, including rejection of compatibility and staged rollout for the private unreleased configuration. |

## Catalog assessment

The catalog's apparent overlaps protect distinct failure boundaries:

- LP-01 tests the complete upstream/lean composition, while LP-02 and LP-03
  isolate the two sides of the density rule: replace implementation with a dense
  behavior contract, but permit one bounded illustration when exact shape is
  irreducibly ambiguous.
- LP-05 and LP-06 contrast loud untrusted-input edges with quiet operational
  invariants. Both require explicit dispositions, but only LP-06 independently
  scores TDD ordering.
- LP-07 and LP-08 form a merge-boundary polarity pair: split independently green
  subsystems; keep interdependent files atomic.

Together the scenarios exercise all four charter invariants. LP-I1 has positive
coverage in the full plan, parser, exact-artifact, and edge-inventory cases. LP-I2
is exercised by concrete interfaces, behavior tables, explicit unhandled inputs,
and silent-invariant dispositions. LP-I3 is covered on both sides: LP-02, LP-05,
and LP-06 replace tricky implementation with behavioral contracts, while LP-03
allows exactly one necessary four-line illustration. LP-I4 has both positive
atomic cases and the oversized split case.

LP-07 is the catalog's most useful first-run failure. The model understands the
subsystem decomposition, dependency order, and independent green gates, but still
echoes the fixture's numeric estimates into the boundary section. LP-08 confirms
that numeric evidence can appropriately support a scenario-specific fact that a
change is small when the boundary remains grounded in coupling and intermediate
consistency. The distinction should remain explicit in later scoring: the problem
is a reusable numeric splitting heuristic, not every mention of size.

Every scenario directly composes `lean-plan-writing` with `writing-plans`, so each
accepted worksheet keeps a separate composition-owner ledger. All seven upstream
composition verdicts pass. This prevents an upstream scaffold success from masking
an owned lean failure such as LP-07, and prevents the lean verdict from absorbing
unrelated upstream requirements.

LP-03's exact artifact bytes are the only deterministic contract in this catalog;
they were verified mechanically. The other outputs are interpreted by plan readers,
so headings, checkbox syntax, table shape, and response-only constraints remain
task-fidelity concerns rather than authenticated parser protocols. LP-06's optional
unnamed repository-wide command is therefore retained as a precision note, not
promoted into a semantic failure when all required commands are runnable.

The scenario READMEs intentionally retain the validation document's source-era
`skill-validation/lean-plan-writing.md` path as provenance. Archive commit
`a8e9550865ee38775c47d1d4e9b2e5224b4bd74e` explicitly classified all seven
matches as intentionally stale source-record provenance; they identify where the
canonical catalog text lived historically rather than acting as current links.
No README rewrite is required.

## Execution-process observation

All seven accepted runs completed without an accepted `INFRA_RETRY`. The later
commands followed the established process of precreating a namespaced scratch
`TMPDIR`, presenting the exact provider/model/effort command, obtaining owner
approval, and invoking Codex with host permission on the first attempt while the
nested provider retained its own workspace sandbox. The central runner README now
documents this controller/provider boundary.

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
aggregation, and comparison rules remain deliberately undecided; these seven single
runs do not answer those questions.

## Next actions

1. Select the next skill catalog for the same scenario-by-scenario current-main
   audit and single-run process-development exercise.
2. Do not begin rewrite comparison, model-matrix execution, or rewrite work until
   the current scenario portfolio and scoring process are sufficiently established.
