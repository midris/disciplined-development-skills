Tighten this documentation excerpt without losing necessary information or framing.
Return the revised excerpt, including both sections, for an engineer maintaining delivery retries.

## Delivery retries

This section explains how delivery retries work.
Each delivery is attempted at most three times.
Retries are counted per delivery, not per endpoint; this distinction prevents one failing delivery from exhausting retries for later deliveries.
The worker attempts a delivery up to three times.
We keep retries synchronous because downstream acknowledgements must preserve delivery order.
Before changing retry behavior, see "Delivery ordering" below.
A delivery is marked failed only after its third unsuccessful attempt.

## Delivery ordering

An endpoint's deliveries are processed in queue order.
The worker waits for the current delivery to succeed or be marked failed before attempting the next delivery for that endpoint.
Workers for different endpoints proceed independently.
Changing retry scheduling must preserve this ordering boundary; a faster later delivery must not overtake a retrying earlier delivery for the same endpoint.

Work read-only within the supplied fixture.
Do not edit files, change Git state, inspect outside the fixture, use the network, or dispatch agents.
