# Scenario Porting Roadmap

**Goal:** Package every active canonical scenario for reusable prompt runner
schema `"0.2"` before designing the repository's long-term testing methodology.

**Contract:** `skill-validation/charter/core-contracts.md`

**Design:** [schema `"0.2"` catalog migration](specs/2026-08-29-catalog-migration-design.md)

**Current phase:** Schema `"0.2"` catalog migration. See the scenario migration
index for current totals.

## Authorities

- Source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c` owns
  canonical candidate scope and scenario content.
- The migration design owns package, prompt, smoke, and completion
  rules.
- The [scenario migration index](../skill-validation/scenarios/README.md) owns
  current totals and migrated scenario links.
- This roadmap owns only phase and sequence status.

## Phases

### 1. Canonical inventory — complete

[Canonical scenario count reconciliation](completed/2026-08-24-scenario-inventory.md)
established the 105-scenario scope.

### 2. Schema 0.1 feasibility — superseded

[Runner-shape coverage](completed/2026-08-24-runner-shape-coverage.md) and the
schema `"0.1"` catalog plans are historical feasibility evidence. They do not
establish schema `"0.2"` package or catalog coverage.

### 3. Schema 0.2 catalog migration — current

Create one catalog-specific plan at a time in this order. Complete and archive
that plan and merge its catalog before creating the plan for the next catalog.
Check a catalog only after its plan is complete and archived and its catalog is
merged:

- [x] `writing-explicit-rationale`
- [x] `sweeping-stale-references`
- [ ] `lean-plan-writing`
- [ ] `disciplined-research`
- [ ] `disciplined-development`
- [ ] `adversarial-review-loop`
- [ ] `skill-discovery`
- [ ] `dispatching-development-subagents`
- [ ] `concise-writing`
- [ ] `adversarial-review`

### 4. Readiness review — pending

Reconcile all packages with the canonical inventory and resolve or explicitly
retain every blocker and ambiguity.

### 5. Testing methodology — pending

After migration, approve canonical evaluator-transport enforcement and the
testing methodology before establishing a behavioral baseline.

## Historical schema 0.1 catalog plans

- [writing-explicit-rationale](completed/2026-08-25-writing-explicit-rationale-catalog-migration.md)
- [sweeping-stale-references](completed/2026-08-25-sweeping-stale-references-catalog-migration.md)
- [lean-plan-writing](completed/2026-08-25-lean-plan-writing-catalog-migration.md)
- [disciplined-research](completed/2026-08-25-disciplined-research-catalog-migration.md)
- [disciplined-development](completed/2026-08-26-disciplined-development-catalog-migration.md)
- [adversarial-review-loop](completed/2026-08-26-adversarial-review-loop-catalog-migration.md)
- [skill-discovery](completed/2026-08-26-skill-discovery-catalog-migration.md)
- [dispatching-development-subagents](completed/2026-08-26-dispatching-development-subagents-catalog-migration.md)

## Done when

All ten catalog checkboxes are complete, the migration index reports 105/105,
and the migration design's completion contract is satisfied.
