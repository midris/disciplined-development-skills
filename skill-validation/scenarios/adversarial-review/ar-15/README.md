# Purpose

Avoid inventing a blocking defect or shared cause in a supported bounded proposal.

# Inputs

- Prompt: canonical `skill-validation/fixtures/adversarial-review/prompts/ar-15.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only by adding the planned fixture-rooted base-skill and `project/` paths; retained SHA-256 `7864f44d15beef43df08bea1fab53586ea634a9c5eda2576c06453a539accc28`.
- Rubric: exact canonical `skill-validation/fixtures/adversarial-review/rubrics/ar-15.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `67ac9d18db0aab32349752b26e25c21e89a8c5e94f675366fefaef7a2c869cc8` and withheld from provider inputs.
- Live skills: `../../../../skills/adversarial-review/SKILL.md` → `skills/adversarial-review/SKILL.md`.
- Pinned Superpowers dependencies: exact files from tag `v6.2.0`; each source `skills/<path>` is packaged as `fixture/skills/superpowers/<path>` and supplied as `skills/superpowers/<path>`:
  - `skills/requesting-code-review/SKILL.md` — SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`
  - `skills/requesting-code-review/code-reviewer.md` — SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`
- Scenario files: exact canonical files from `skill-validation/fixtures/adversarial-review/ar-15/` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged beneath `fixture/` and supplied at the matching path:
  - `project/approval-evidence.md` — SHA-256 `4e0b97116bb4dcd2e0f406e8bd43da561b267de29ebfe5adb5d252fd42c540b2`
  - `project/change-request.md` — SHA-256 `40ec5077bd654fdae4d82fe5321ce157d23da86228f2eb186d813fd8a83266e4`
  - `project/decision-record.md` — SHA-256 `b26aef2a0076d52c7578ae442a0afa5d863b20ffae5371fa7d87f6c487e630d6`
  - `project/interface-contract.md` — SHA-256 `9996f1267cd295f7331866bfb03461bbe8a73b35b13405476154f9410e5857f1`
  - `project/proposal.md` — SHA-256 `bf8b784fdf97b333d976872b134f3881b527f706b4efc7f75f66742538ea9698`
  - `project/support-evidence.md` — SHA-256 `504c72f8798cf1957fe98e442aa197599ca46f9702f44f2fd04c82d1faedf626`

# Smoke

No schema `0.2` result is retained.
