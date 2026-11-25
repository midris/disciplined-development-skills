# Purpose

Reconcile a development handoff and landed prose while keeping a no-commit research report outside the development boundary.

# Inputs

- Prompt: canonical `skill-validation/fixtures/dispatching-development-subagents/prompts/dsd-05.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, adapted only as follows: prefixed the backticked dispatch skill and `project/dsd-05/` paths with `{{fixture_dir}}/`. The adapted prompt is retained with SHA-256 `4b0f1c15850a20e191dd060396153adf24492d791a67f2cd68aad2e29322f74a`.
- Rubric: exact canonical `skill-validation/fixtures/dispatching-development-subagents/rubrics/dsd-05.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, retained with SHA-256 `fc5d43057ffdb3055d2fbd20dba98f594ac3a654807132e5b768e8651f8b0d6b` and withheld from provider inputs.
- Live repository file: `../../../../skills/dispatching-development-subagents/SKILL.md` is provided at `{{fixture_dir}}/skills/dispatching-development-subagents/SKILL.md`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/landed-prose.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-05/landed-prose.md`, provided at `{{fixture_dir}}/project/dsd-05/landed-prose.md`, SHA-256 `dc1c4a0881580f5a883d126ddcbc00b70dfd3e226129e44aa6ed06381fbc4aae`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/research-report.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-05/research-report.md`, provided at `{{fixture_dir}}/project/dsd-05/research-report.md`, SHA-256 `0d7d31036a68767b0a586b7aad0c228999316c6463dfd39009f8d7e7131360d5`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/returned-handoff.md` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-05/returned-handoff.md`, provided at `{{fixture_dir}}/project/dsd-05/returned-handoff.md`, SHA-256 `1c9f3979e4a123c584f3ddd072f6869df6a241adca1c4da4cc484b8f6815ecab`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/src/request_config.py` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-05/src/request_config.py`, provided at `{{fixture_dir}}/project/dsd-05/src/request_config.py`, SHA-256 `f0ff7ba51f0b758aea2f9b248c754f832dd57c6d2110036a80f886690ecdee6c`.
- Scenario-owned file: canonical `skill-validation/fixtures/dispatching-development-subagents/project/dsd-05/test-output.txt` at source commit `13599fb7d3127334b0d07bfe468767e586ec5f9c`, packaged as `fixture/project/dsd-05/test-output.txt`, provided at `{{fixture_dir}}/project/dsd-05/test-output.txt`, SHA-256 `dbff34df084976e0006cd15b2bd1cf6e3b5419b626c19f0030544a1c174ec3d7`.

# Smoke

No schema `0.2` result is retained.
