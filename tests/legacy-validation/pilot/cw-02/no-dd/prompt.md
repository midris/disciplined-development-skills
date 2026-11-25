Tighten the excerpt without losing necessary information or framing. Return only the revised excerpt.

## Delivery retries

This section explains how delivery retries work. Each delivery is attempted at most three times. Retries are counted per delivery, not per endpoint; this distinction prevents one failing delivery from exhausting retries for later deliveries. The worker attempts a delivery up to three times. We keep retries synchronous because downstream acknowledgements must preserve delivery order. Before changing retry behavior, see "Delivery ordering" below. A delivery is marked failed only after its third unsuccessful attempt.

Work read-only within the supplied fixture. Do not edit files, change git state, inspect outside the supplied fixture, use the network, or dispatch agents.
