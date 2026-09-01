# Purpose

Map the holistic baseline and additive specialized lenses by artifact kind.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-04.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by using the plan-specified fixture-rooted skill and artifact read sentence; retained SHA-256 `525112073efaf10c6af7f6eb9fedfe3ce0c6e5c56ba443c27c73244e3b13a016`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-04.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `3eb7b7a502cb47c88af3ecdd9741cc85ded600ba35d47646ea5460f0387210a2` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario file: canonical `skill-validation/fixtures/adversarial-review/ar-04/artifacts.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/context/artifacts.md`, supplied as `context/artifacts.md`, SHA-256 `8b924afe56754ad28ae0fc04e265d8823d73826bea1732514f41e321b5402e1b`.

# Smoke

No schema `0.2` result is retained.
