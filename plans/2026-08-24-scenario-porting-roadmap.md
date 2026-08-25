# Skill Scenario Porting Roadmap

**Goal:** Port every active, replayable skill scenario into `skilltest` before designing the repository's long-term testing methodology.

**Contract:** `skill-validation/charter/core-contracts.md`

**Current phase:** Catalog migration.

## Rules

- Use `origin/docs/comprehensive-skill-cleanup` at `13599fb7d3127334b0d07bfe468767e586ec5f9c` as the canonical scenario source.
- Port only candidates in the [active scenario inventory](completed/2026-08-24-scenario-inventory.md); scenarios outside it remain out of scope unless promoted.
- Preserve prompts, rubrics, fixtures, dependencies, and declared skill context faithfully; adapt only paths required by `skilltest` packaging.
- During runner-shape coverage, run one real smoke test when first covering a shape. During catalog migration, preselect and smoke-run at least one scenario from each catalog end to end.
- Keep behavioral evaluation, baselines, and skill changes out of migration; runner changes require separate approved scope.
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

- Current phase.
- Port the remaining active scenarios catalog by catalog.
- Load every configuration, verify packaging fidelity, then run at least one preselected scenario from the catalog through the real provider and collect mechanical evidence without scoring it.
- Complete: [writing-explicit-rationale catalog migration](completed/2026-08-25-writing-explicit-rationale-catalog-migration.md).
- Complete: [sweeping-stale-references catalog migration](completed/2026-08-25-sweeping-stale-references-catalog-migration.md).

### 4. Readiness review

- Reconcile the ported scenarios with the inventory.
- Resolve or explicitly retain every blocker and ambiguity, then confirm migration is complete.

### 5. Testing methodology

- After migration, approve the testing methodology before establishing the initial baseline.

## Done when

- Every candidate in the active inventory is represented by a loadable `skilltest` configuration.
- Each distinct runner shape has completed one end-to-end smoke run.
- Each migrated catalog has at least one completed end-to-end smoke run.
- The runnable catalog is ready for testing-methodology design.
