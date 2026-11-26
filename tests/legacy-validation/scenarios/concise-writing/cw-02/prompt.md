You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `{{fixture_dir}}/skills/concise-writing/SKILL.md` completely and follow it as binding guidance.

Tighten the excerpt without losing necessary information or framing. Return only the revised excerpt.

## Delivery retries

This section explains how delivery retries work. Each delivery is attempted at most three times. Retries are counted per delivery, not per endpoint; this distinction prevents one failing delivery from exhausting retries for later deliveries. The worker attempts a delivery up to three times. We keep retries synchronous because downstream acknowledgements must preserve delivery order. Before changing retry behavior, see "Delivery ordering" below. A delivery is marked failed only after its third unsuccessful attempt.
