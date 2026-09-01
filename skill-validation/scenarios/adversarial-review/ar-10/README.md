# Purpose

Challenge and remove unsupported duplicate state.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-10.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and `project/` paths; retained SHA-256 `bebc32961df677d4a15b45d5d87201e43b5ae60b4a16362495a9e5de3cff9baa`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-10.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `6c161f73eab08e12f5b05bed900eb8efa08647365b064ac93417ee1a33f1b314` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-10/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/brief.md` — SHA-256 `784fef67760ffc9bca3245bffed2665f751ebeba71fa604297acebe112412c54`
  - `project/proposal.md` — SHA-256 `df3d4a609e7d879b1b0b083eb246e060b9ad4dd00d76fb3b7646885ba47dc943`

# Smoke

No schema `0.2` result is retained.
