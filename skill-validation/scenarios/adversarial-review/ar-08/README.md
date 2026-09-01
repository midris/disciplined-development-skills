# Purpose

Synthesize an evidence-backed pattern across API, queue, and file findings.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-08.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill, project, and plan paths; retained SHA-256 `f2b266a29190821363eb02a2535587498eea852a2cb9fa3173910bb5333be3aa`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-08.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `a974a1585bb968b072bd7d724828cd311c03f6b624a158cf70cd2972e3cb9502` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-08/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/plan.md` — SHA-256 `26c7a41a11268983452b04b43120ca7c4fd43789b2a1a5be3bbedeb247e346de`
  - `project/src/api.py` — SHA-256 `9a55bc5e939aa4b08c159afbd42222c3da4a35ae00a9fe99869dd57738da5a36`
  - `project/src/errors.py` — SHA-256 `718d317ee842c189fe538e5b86dae070f7602c1edfc62a00474854ca64344237`
  - `project/src/file.py` — SHA-256 `b7fa1e6b2ef16a1a53079cf7e4a6431ddd958721182225f6387696d46263e9d0`
  - `project/src/queue.py` — SHA-256 `36fffd19621f2bcdc471ea17fba458d88de8755e017921d4bf58f49c6df9256c`
  - `project/test_happy_path.py` — SHA-256 `c62e8137b9f5cba55feebcb22d73248c037558d5a0e971dca597bc229dcd337a`

# Smoke

No schema `0.2` result is retained.
