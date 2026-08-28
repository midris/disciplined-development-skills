# Scenario Porting Roadmap

**Goal:** Migrate every active, replayable scenario to the reusable prompt
runner schema `"0.2"` before designing the repository's long-term testing
methodology.

**Contract:** `skill-validation/charter/core-contracts.md`

**Current phase:** Catalog migration.

## Rules

- Use `origin/docs/comprehensive-skill-cleanup` at `13599fb7d3127334b0d07bfe468767e586ec5f9c` as the canonical scenario source.
- Migrate only candidates in the [active scenario inventory](../skill-validation/scenarios/README.md); scenarios outside it remain out of scope unless promoted.
- Author tester-authored prompts and individual fixture files faithfully from the candidate scenario; the runner neither injects nor validates skill instructions, dependencies, permissions, or behavioral expectations.
- During catalog migration, load every configuration and run at least one preselected scenario from the catalog through the real provider, collecting mechanical evidence without scoring it.
- Keep behavioral evaluation, baselines, and runner changes out of migration; runner changes require separate approved scope.
- Do not commit raw provider output or temporary result bundles.

## Phases

### 1. Inventory

- Complete: [active scenario inventory](completed/2026-08-24-scenario-inventory.md).

### 2. Runner-shape coverage

- For each uncovered shape, select a representative and agree on a faithful porting solution.
- Create a separate plan to implement, smoke-run, and complete that shape.
- Finish one shape before starting the next.
- Complete: [runner-shape coverage](completed/2026-08-24-runner-shape-coverage.md).

### 3. Catalog migration

- Current phase: 0 catalogs migrated under schema `"0.2"`.
- Create a fresh migration plan for each catalog.
- Author each catalog with tester-authored prompts and individual fixture files.
- Load every configuration and run at least one preselected scenario from each catalog through the real provider, collecting mechanical evidence without scoring it.

#### Superseded schema `"0.1"` migration wave

- [writing-explicit-rationale catalog migration](completed/2026-08-25-writing-explicit-rationale-catalog-migration.md)
- [sweeping-stale-references catalog migration](completed/2026-08-25-sweeping-stale-references-catalog-migration.md)
- [lean-plan-writing catalog migration](completed/2026-08-25-lean-plan-writing-catalog-migration.md)
- [disciplined-research catalog migration](completed/2026-08-25-disciplined-research-catalog-migration.md)
- [disciplined-development catalog migration](completed/2026-08-26-disciplined-development-catalog-migration.md)
- [adversarial-review-loop catalog migration](completed/2026-08-26-adversarial-review-loop-catalog-migration.md)
- [skill-discovery catalog migration](completed/2026-08-26-skill-discovery-catalog-migration.md)
- [dispatching-development-subagents catalog migration](completed/2026-08-26-dispatching-development-subagents-catalog-migration.md)

### 4. Readiness review

- Reconcile the migrated scenarios with the inventory.
- Resolve or explicitly retain every blocker and ambiguity, then confirm migration is complete.

### 5. Testing methodology

- After migration, approve the testing methodology before establishing the initial baseline.

## Done when

- Every candidate in the active inventory is represented by a loadable schema `"0.2"` configuration.
- Each distinct runner shape has completed one end-to-end smoke run.
- Each migrated catalog has at least one completed end-to-end smoke run.
- The runnable catalog is ready for testing-methodology design.
