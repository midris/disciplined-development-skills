# Duplicate red-flag consolidation — scenarios

Canonical replay fixture for the 2026-08-01 consolidation of duplicate `Red flags` sections in four skills.

## Protocol

- Run two arms: control at `d18cece` and GREEN with the four sections removed.
- Five independent cold evaluators per arm, one composite matrix per evaluator.
- Read-only; no edits or nested dispatch.
- Control evaluators read the four files from `d18cece` via `git show`; GREEN evaluators read the four live skill files.
- Runtime default model; model was not pinned, so future reruns must record the model if they require model-to-model comparison.
- Score each subcase independently after the evaluator returns; never include the scoring criteria in its prompt.
- A repetition passes only when A, B, C, and D all pass.

## Exact prompt

> Read-only composite regression, repetition N.
> Do not edit or dispatch.
> Read the supplied versions of `adversarial-review`, `concise-writing`, `lean-plan-writing`, and `sweeping-stale-references` as binding guidance.
> Respond to four independent tasks, labeled A–D.
>
> A) Review this plan excerpt:
>
> `normalizeTasks` accepts an ordered task list and performs no sorting.
> The plan says this is safe because `validateBatch` sorts before calling it and its tests pass with ordered fixtures.
> It cites a performance article claiming that sorting adds 18% latency.
> Another caller, `retryBatch`, invokes `normalizeTasks` directly.
> A sibling helper, `bulkNormalize`, sorts locally before doing the same normalization work.
> Return review findings and the required verdict line.
>
> B) Tighten this documentation without losing necessary information or framing, then briefly state what you checked outside the excerpt:
>
> `## Delivery retries`
>
> `This section explains how delivery retries work. Each delivery is attempted at most three times. Retries are counted per delivery, not per endpoint; this distinction prevents one failing delivery from exhausting retries for later deliveries. The worker attempts a delivery up to three times. We keep retries synchronous because downstream acknowledgements must preserve delivery order. A delivery is marked failed only after its third unsuccessful attempt.`
>
> C) Write an extremely detailed implementation-plan step for a parser of `KEY=VALUE` lines.
> Blank lines are skipped, the first `=` separates key from value, and a nonblank line without `=` exits with status 2.
> The requester asks you to include the full Python function, complete test bodies, and a shell heredoc so the implementer can copy them verbatim.
>
> D) A branch renamed configuration key `cache_ttl` to `max_age`.
> A reviewer reports only `README.md:88` still documents `cache_ttl`; the author says the IDE rename handled everything else.
> The repository may also contain code callsites, tests or fixtures, config and CI scripts, prose synonyms such as “cache TTL,” an archived migration intentionally describing the old key, and an unrelated HTTP `max-age` field.
> State exactly what you do before committing and show the commit-body evidence structure.

## Scoring rubric (never send to evaluators)

- **A:** independently verify the cited performance claim; report the nonlocal/asymmetric ordering invariant at P0–P2 despite passing tests; end with `DD-VERDICT: BLOCK`.
- **B:** remove the meta opener and one duplicated retry statement; retain the per-delivery transition, synchronous-ordering rationale, and failure recap; mention a whole-document duplicate check.
- **C:** omit full implementation/test bodies and the heredoc; provide concrete prose requirements and an input→expected-output table; use a snippet only for genuine remaining ambiguity and no longer than five lines.
- **D:** treat the README line as a sampled class; search literal and synonym forms across code/docs/tests/fixtures/config/scripts/CI/build; use all three match classifications; reconcile updates together; put grouped `References swept:` before `Verification:`.

## Results

| Arm | Rep 1 | Rep 2 | Rep 3 | Rep 4 | Rep 5 | Overall |
|---|---|---|---|---|---|---|
| Control (`d18cece`) | PASS | PASS | PASS | PASS | PASS | 5/5 PASS |
| GREEN (sections removed) | PASS | PASS | PASS | PASS | PASS | 5/5 PASS |

The earlier answer-primed 5/5 runs are invalidated and intentionally excluded.
Every replacement repetition was hand-checked against all four criteria before being counted.
