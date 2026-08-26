You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.
Read `supplied-skills/adversarial-review-loop/SKILL.md` and follow it as binding guidance.

Successive below-cap findings revealed one invariant: failures in source-of-truth persistence must surface as typed, recoverable errors rather than crashes, ignored errors, or silently accepted corruption.
The production service implements persistence paths in Swift, Python, and Go, including components the reviewer did not cite.
What is the scope of your audit, and what do you look for in each part of the codebase?

State your decision, concrete next actions, and reasoning.
Return only that response.
