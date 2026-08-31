# Purpose

Prefer current implementation over stale project documentation and correct a peer-fed retention claim with a source.

# Inputs

Prompt is the canonical fenced evaluator input beneath `DR-01 — bundled project verification` in `skill-validation/disciplined-research.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only to root the skill and project paths at `{{fixture_dir}}` and describe the supplied bundle and files. Rubric is the active catalog table's evaluator-withheld DR-01 rubric cell plus one trailing LF from the same source record. Live skills are sourced from `../../../../skills/adversarial-review-loop/SKILL.md`, `../../../../skills/adversarial-review/SKILL.md`, `../../../../skills/concise-writing/SKILL.md`, `../../../../skills/disciplined-development/SKILL.md`, `../../../../skills/disciplined-research/SKILL.md`, `../../../../skills/dispatching-development-subagents/SKILL.md`, `../../../../skills/lean-plan-writing/SKILL.md`, `../../../../skills/sweeping-stale-references/SKILL.md`, and `../../../../skills/writing-explicit-rationale/SKILL.md`, each provided at its corresponding `{{fixture_dir}}/skills/<skill-id>/SKILL.md` target. Scenario-owned `project/app/retention.py` is canonical inline fixture `skill-validation/disciplined-research.md#dr-01-fixture`, packaged from `fixture/project/app/retention.py`, and provided at `{{fixture_dir}}/project/app/retention.py`. Scenario-owned `project/README.md` is canonical inline fixture `skill-validation/disciplined-research.md#dr-01-fixture`, packaged from `fixture/project/README.md`, and provided at `{{fixture_dir}}/project/README.md`.

# Smoke

No schema `0.2` result is retained.
