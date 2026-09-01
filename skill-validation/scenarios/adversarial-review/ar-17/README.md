# Purpose

Reject interior empty records as replay corruption.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-17.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and `project/` paths; retained SHA-256 `1513a66015109f998e8ca2bd5c0f92aa1b09f9791ec9b40abd87b71dc18d9c17`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-17.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `2d059422fc110f99a4e1120c48a2286f44311e610787381d998ca0eeced84844` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-17/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/EventLog.swift` — SHA-256 `f1eda7207c1241654507072d3906db8a03947ecd65e155b4ad7591968638d41a`
  - `project/contract.md` — SHA-256 `2557208d3e59c3d25e8dc914911fb73ce3b5beb7d55d43879fcc7e4ad0270a0f`

# Smoke

No schema `0.2` result is retained.
