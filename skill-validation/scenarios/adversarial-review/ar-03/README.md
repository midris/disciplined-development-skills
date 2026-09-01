# Purpose

Require complete caller enumeration, rationale verification, and blocking treatment of a nonlocal invariant.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-03.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and `project/` paths; retained SHA-256 `a32a3269f7e89640a65b041b3f9d1ec5907f7397b032593e9473e59e42518fc8`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-03.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `31b5fab1a4a9c34a8517c51ee58aa974b309a5cecad4780caab930e7c0cf4244` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-03/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/benchmarks/sort.json` — SHA-256 `2a3c39905224a730da2182fa14aad68215caf7a536e251f818f751d4c2e4f2ae`
  - `project/plans/normalize.md` — SHA-256 `963cae0e7dbd0d03ad3dc944d53d79bf5166a029e2ee08ccc8b3e0c7c007ecd1`
  - `project/src/bulk.py` — SHA-256 `1640200ee740a66856d513fc3534ab6b62301f0838a0ebc438499620db2bbab0`
  - `project/src/normalize.py` — SHA-256 `947c4926116f228a4843a7aa213cf46c86c03553315f55735b43b5085998223d`
  - `project/src/retry.py` — SHA-256 `424d10fc3e9c4ef274312c2bffe331f60b53ad1d6ed5d873a0d13fb07aa9ff7f`
  - `project/src/validate.py` — SHA-256 `020d6e30bd07ed9d44fe122dc0772cdf7080434947be2cc2dc21a878e5dbbbb0`

# Smoke

No schema `0.2` result is retained.
