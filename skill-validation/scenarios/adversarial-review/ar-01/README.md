# Purpose

Exercise direct adversarial review, severity, output, and composition over a complete bundle.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-01.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted skill and `project/` paths; retained SHA-256 `a70567cd4c8196340d478d8738de3a244b28df00919cfb643053db4a9ac506f8`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-01.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `33c459e9042000e46c5f82488511d140b750ff53076d8ab11331cf24c91447ab` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`; `../../../../skills/adversarial-review-loop/SKILL.md` → `skills/adversarial-review-loop/SKILL.md`; `../../../../skills/concise-writing/SKILL.md` → `skills/concise-writing/SKILL.md`; `../../../../skills/disciplined-development/SKILL.md` → `skills/disciplined-development/SKILL.md`; `../../../../skills/disciplined-research/SKILL.md` → `skills/disciplined-research/SKILL.md`; `../../../../skills/dispatching-development-subagents/SKILL.md` → `skills/dispatching-development-subagents/SKILL.md`; `../../../../skills/lean-plan-writing/SKILL.md` → `skills/lean-plan-writing/SKILL.md`; `../../../../skills/sweeping-stale-references/SKILL.md` → `skills/sweeping-stale-references/SKILL.md`; `../../../../skills/writing-explicit-rationale/SKILL.md` → `skills/writing-explicit-rationale/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-01/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/CLAUDE.md` — SHA-256 `7f9a434946a09909b3d837588e5dd3f49593dc151959796132487735954f9993`
  - `project/plans/ratio.md` — SHA-256 `b42252947352d99ecc3994cf157d91746bc6c13e1dfa530d5bfe3b3750dd6424`
  - `project/src/ratio.py` — SHA-256 `2ab9e87f7325f2203a79bdcc5f5d698607c52566e601b3a3db7556287c656ad3`

# Smoke

No schema `0.2` result is retained.
