# Purpose

Reject a generic shared cause for two independently caused findings.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-13.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by rooting the planned `skills/` and `project/` paths at the fixture directory; retained SHA-256 `76e00b195de7e65f0a9039d7a8fbde578fea9e58ae28764fccbcfc2ffa2dcb38`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-13.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `0ea6ad7ec83921325946609145fe06ce733d6e7496bddcf13af3168082dbc1f2` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-13/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/incidents.md` — SHA-256 `5a9a9d85342ba751c28f63e297c66931c84065f080053d67699d90fbea0855a6`
  - `project/plan.md` — SHA-256 `3a500c601edc5c76c0658b89f4b36d632a416226a12e0a9c5f200dc691f5dd8c`
  - `project/src/audit.py` — SHA-256 `9188c4991ce34c96388ada0eec7a57ba966309435167ee1571819158a5c446e6`
  - `project/src/ratio.py` — SHA-256 `2ab9e87f7325f2203a79bdcc5f5d698607c52566e601b3a3db7556287c656ad3`

# Smoke

No schema `0.2` result is retained.
