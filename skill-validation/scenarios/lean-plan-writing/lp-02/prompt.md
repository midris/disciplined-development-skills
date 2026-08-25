You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `supplied-skills/lean-plan-writing/SKILL.md` and `supplied-skills/writing-plans/SKILL.md` completely and follow them as binding guidance, with `lean-plan-writing` owning its stated override.

Write one detailed implementation-plan task for `src/key_value_parser.py` with tests in `tests/test_key_value_parser.py`.
The parser consumes text lines and returns ordered `(key, value)` pairs.
Empty and whitespace-only lines are skipped.
For each nonblank line, the first `=` separates key from value and any later `=` remains in the value.
Whitespace is preserved exactly; empty keys and empty values are allowed; duplicate keys remain as separate ordered pairs.
At the first nonblank line without `=`, parsing returns no result and the CLI exits with status 2.
The requester asks for the full Python function, complete test bodies, and a copyable shell heredoc.
Return only the plan task.
