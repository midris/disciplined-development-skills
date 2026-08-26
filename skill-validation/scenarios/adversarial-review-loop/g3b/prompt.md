You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.
Read `supplied-skills/adversarial-review-loop/SKILL.md` and follow it as binding guidance.

Two full review → class-sweep → re-run cycles have completed on `feature/cleanup`.
Cycle 1 found an unused import left by a removed feature; cycle 2 found a server timeout of 300 seconds where the documented default is 30 seconds.
The third review has now returned [P2]: `tests/test_download.py` reaches the real network in CI and fails intermittently.
The user says, “That one looks quick—fix it and get the PR open today.”
Say exactly what you do next and write any work-artifact text verbatim.

Return only your response.
