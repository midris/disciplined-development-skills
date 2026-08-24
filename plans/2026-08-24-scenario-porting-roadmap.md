# Skill Scenario Porting Roadmap

**Goal:** Port every active, replayable skill scenario into `skilltest` before designing the repository's long-term testing methodology.

**Approach:** Separate faithful scenario migration from behavioral evaluation. Validate every port mechanically, use real provider runs only to prove distinct runner shapes, and defer baselines, scoring, and acceptance rules until the runnable catalog is complete.

**Contract:** `skill-validation/charter/core-contracts.md`

**Current phase:** [`plans/2026-08-24-scenario-inventory.md`](2026-08-24-scenario-inventory.md)

## Constraints

- Treat `docs/comprehensive-skill-cleanup` at `13599fb7d3127334b0d07bfe468767e586ec5f9c` as the canonical scenario source and its clean `.worktrees/comprehensive-skill-cleanup/` checkout as read-only until migration is complete.
- Port active, replayable scenarios only. Record historical and retired scenarios as exclusions unless they are explicitly promoted later.
- Preserve prompts, rubrics, fixtures, dependencies, and declared skill context faithfully; adapt only paths required by `skilltest` packaging.
- Do not change skills or the runner to address behavioral fallout during migration.
- Do not treat migration smoke runs as baselines, acceptance results, or evidence for skill changes.
- Do not commit raw provider output or temporary result bundles.

## Phases

### 1. Inventory

- List every active migration candidate and its canonical source.
- Mark the scenarios already ported.
- Defer runner-shape analysis and detailed migration sequencing to the next plan.

### 2. Runner-shape coverage

- Count `WER-08` as the prompt-only runner shape.
- Count `WER-05` as the project-fixture runner shape.
- Select and port the smallest active scenarios that cover remaining shapes such as declared dependencies, multiple supplied skills, external dependencies, and larger fixtures.
- Complete one end-to-end smoke run when a runner shape is exercised for the first time.

### 3. Catalog migration

- Port the remaining active scenarios catalog-by-catalog.
- For every port, load the configuration and verify prompt, rubric, fixture, dependency, and skill-source fidelity.
- Do not require another provider run when an already-proven runner shape is reused unless packaging cannot otherwise be verified.

### 4. Readiness review

- Reconcile the ported scenario tree with the inventory.
- Resolve or explicitly retain every blocker and ambiguity.
- Confirm every active replayable scenario has a loadable configuration and every runner shape has completed one real smoke run.

### 5. Testing methodology

- After migration readiness is complete, design repetitions, model and effort coverage, controls, scoring, adjudication, concurrency, infrastructure-failure handling, and baseline rules.
- Establish the initial baseline only under that approved methodology.

## Done when

- Every active replayable scenario is represented by a loadable `skilltest` configuration.
- Every excluded scenario has an explicit historical, retired, ambiguous, or incomplete disposition.
- Each distinct runner shape has completed one end-to-end smoke run.
- No migration observation has been promoted into a baseline or skill-change decision.
- The complete runnable catalog is ready for a separate testing-methodology design.
