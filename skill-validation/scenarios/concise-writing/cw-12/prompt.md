You are a fresh, read-only skill-contract evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `{{fixture_dir}}/skills/concise-writing/SKILL.md` completely and follow it as binding guidance.

A user is authoring a reference file shipped as part of a skill and asks which skill owns the authoring decisions and validation.
Extract only ownership stated explicitly in the supplied contract; do not infer an owner from prior knowledge or from a skill name.
Return only a compact JSON object with keys `authoring_owner`, `validation_owner`, and `evidence`, in that order and no whitespace. Use the explicitly named owner's canonical skill name for each owner. Quote the complete ownership sentence from the supplied contract verbatim as `evidence`. Use `null` for all three values if that sentence is absent.
