# Purpose

Treat producer ordering as an unresolved blocking invariant.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-07.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and review-series paths; retained SHA-256 `7023f5a2cdb2aadc443477d2c934e8ef584cf1e3539b602db607465caad2833f`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-07.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `a9f2bb2083974a0e6e793e26e0a3ced34dd4f5260b6d1359bb5e33dbc418f003` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario file: canonical `skill-validation/fixtures/adversarial-review/ar-07/review-series.patch` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/subject/review-series.patch`, supplied as `subject/review-series.patch`, SHA-256 `948088882749126f0e351155b6cdf505b530250b88504c0bb4421dcaf21dcdcf`.

# Smoke

No schema `0.2` result is retained.
