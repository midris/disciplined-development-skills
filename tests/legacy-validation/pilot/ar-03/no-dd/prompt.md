Read {{fixture_dir}}/.agents/skills/requesting-code-review/SKILL.md completely and apply its review guidance within this read-only, no-dispatch task.
Read {{fixture_dir}}/.agents/skills/requesting-code-review/code-reviewer.md completely and apply its review criteria yourself; do not dispatch agents.

Review the code under {{fixture_dir}}/project/ against its supplied plan and benchmark.
Review the supplied files directly; no implementation Git history is supplied.
Return findings with severity and an overall approve/block conclusion.
Do not implement fixes or run a remediation loop.

Work read-only within the supplied fixture. Do not edit files, change git state, use the network, or dispatch agents.
