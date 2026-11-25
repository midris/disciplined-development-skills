# The root installer suite has no runner dependencies. Run the separately
# packaged runner and format checks with their locked environment (tests/README).
# The WER reader tests likewise import the installed runner. Its README gives the focused command.
collect_ignore = ["runner", "methodology", "skills/writing-explicit-rationale"]
