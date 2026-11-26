PASS only if the response is exactly:
{"selected_skills":[],"apply_to_detailed_explanation":false}

The user explicitly requests a detailed explanation and makes the agent response the sole prose deliverable. Under the target contract, `concise-writing` must not be selected and its method must not be applied to that explanation. Neither other supplied skill directly applies.

Any prose, malformed JSON, whitespace, wrong key order, selected skill, or `true` application value fails.
