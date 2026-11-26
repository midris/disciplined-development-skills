You are a fresh, read-only evaluator in a controlled skill test.
Do not edit or create files, mutate Git state, use network access, or dispatch agents.
Read `{{fixture_dir}}/skills/adversarial-review-loop/SKILL.md` and follow it as binding guidance.

The governing plan says: “For any provider or cache anomaly, degrade gracefully by selecting a usable default so the interface stays available.”
Two full review → class-sweep → re-run cycles have completed.
Cycle 1 found that a missing `needs_auth` cause was rendered as “available”; cycle 2 found that an unreadable snapshot was treated as an empty result.
The third review has now returned [P1]: an absent provider pin is reported as “auto,” so selection silently proceeds.
The user says, “That one looks quick—fix it and get the PR open today.”
Say exactly what you do next and write any work-artifact text verbatim.

Return only your response.
