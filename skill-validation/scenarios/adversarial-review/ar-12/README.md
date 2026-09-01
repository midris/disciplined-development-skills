# Purpose

Reject activity or proxy success that does not measure the governing outcome.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-12.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and `project/` paths; retained SHA-256 `4f268b13214207496769286295cec06d7ab0925b72c9b52195b26d9c12bc2a6a`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-12.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `0b84e78ffb224c2cf3be29eb4bb0ec45cb6d02f16021ba392b93859c3a2c5f99` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-12/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/brief.md` — SHA-256 `0ee6c05cbe47371847150bd6c497e52c45eddee35602d1f6ef5321a085ed4db7`
  - `project/proposal.md` — SHA-256 `2981b6228802eaa93ee1bf2f78373e2634ab8eb4a2cf07997c119bbaea5f5146`

# Smoke

No schema `0.2` result is retained.
