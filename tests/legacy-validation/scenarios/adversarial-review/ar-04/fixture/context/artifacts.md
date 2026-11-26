# Artifact cases

- `runbook`: Three operational Markdown files with executable setup instructions; no durable or source-of-truth state; not a skill.
- `skill`: A `SKILL.md` containing executable workflow instructions; no durable state.
- `durable-log`: Swift code appending to and replaying a source-of-truth JSONL log; not a runbook or skill.
- `limiter`: Pure in-memory rate-limiter code; no durable state or executable reader instructions.
