# Purpose

Reach beyond a patch to absent, malformed, and out-of-scale paths.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-06.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill, patch, and project paths; retained SHA-256 `64297e2b5919d9026c259bbdde24e64e929a812e59db10d7bd5cede490afe01b`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-06.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `1fcc10f48c998b173626c37e61259ecf9bd41d2ea96b31c8b34086d14a94b924` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-06/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `context/head-change.patch` — SHA-256 `ba2d42b8dd3c3b1b04a1a81f217f4a215aeae5b68d89ae80f05a3e7c1d21a8df`
  - `project/plans/import-endpoint.md` — SHA-256 `2c38ef43ecfa7d63efcfdf079a4a81a14503e1002d27ac3f1bac95a255308c2f`
  - `project/src/api.py` — SHA-256 `43246548de85a93a0c973d9893a3d23d4493e134250d04f5a0574e7a70bfb152`
  - `project/src/importer.py` — SHA-256 `6657310fb0eb39c2cf2927be270d6c9204ff62b7743f7e39180e6356e28e1b8e`

# Smoke

No schema `0.2` result is retained.
