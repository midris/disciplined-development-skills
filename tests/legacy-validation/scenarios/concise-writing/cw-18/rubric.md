PASS only if the response is exactly:
{"selected_skills":["concise-writing"],"apply_to_detailed_explanation":true}

The explicit detailed-explanation exemption applies only when that explanation is the agent response. Here the detailed prose is written into a Markdown file, so `concise-writing` must be selected and applied to the file prose. The brief agent completion notice does not exempt the file. Neither other supplied skill directly applies.

Any prose, malformed JSON, whitespace, wrong key order, omission or addition of a skill, or `false` application value fails.
