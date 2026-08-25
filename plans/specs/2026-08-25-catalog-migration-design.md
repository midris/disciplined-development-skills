# Catalog Migration Design

**Status:** Owner-approved on 2026-08-25.

## Goal

Port every remaining active scenario into a loadable `skilltest` configuration without changing runner behavior or establishing behavioral results.

## Unit of work

Use the existing [scenario porting roadmap](../2026-08-24-scenario-porting-roadmap.md) as the program tracker. Migrate one complete catalog at a time, with one implementation plan, branch, worktree, review, and merge per catalog. Do not keep more than one catalog migration in progress.

Select the next catalog only after the current catalog merges. Do not create speculative implementation plans for later catalogs.

## Catalog-plan contract

Each catalog plan must:

- Use configuration schema `"0.1"` and one exact runner-supported root shape.
- Derive each scenario's definition, prompt, rubric, fixture, and declared skill context from source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`. Record hashes for the canonical prompt, rubric, and any fixture files.
- Materialize only the scenario-owned prompt and fixture files, and encode the canonical rubric unchanged as `expected_outcome`. Path-only adaptation for `skilltest` packaging is allowed.
- For ordinary skill-context configurations, reference the currently installed project copies of the primary skill and dependencies through explicit `source` and `include` declarations. Record hashes for the included files actually used. Version pinning and dependency sourcing remain tester-level concerns.
- For no-skill-context configurations, use explicit `skill_context: "none"` without `skill` or `dependencies`.
- Load every configuration and prepare a disposable workspace without invoking a provider.
- Verify packaged file paths and hashes, canonical prompt bytes, the runner-defined subject-input transport for the declared shape, and absence of the evaluator-withheld rubric from provider-visible input.
- Run the full runner suite, the local Markdown-link checker, and diff checks.
- Mark scenarios ported only after every configuration in the current plan passes preflight, then reconcile the affected and overall inventory totals.
- Archive the completed catalog plan and update the roadmap before review and merge.

## Boundaries

- Do not run providers or repeat runner-shape smoke tests during catalog migration.
- Do not change the runner, providers, skills, canonical scenario content, validation methodology, or testing methodology.
- Do not modify already-ported scenario packages without separate owner approval.
- Do not score scenarios, establish baselines, or commit raw output or temporary workspaces.
- If a scenario requires an unsupported runner shape, an unavailable declared dependency, an ambiguous canonical input, or content adaptation beyond paths, stop that catalog and request separate owner approval.
- Do not skip a blocked scenario and mark the rest of its catalog complete.

## Completion

Catalog packaging is ready for readiness review when every active scenario is represented by a loadable configuration, the inventory reports none remaining, and every catalog plan is archived. Readiness review remains a separate roadmap phase with its own plan and confirms whether migration is complete.
