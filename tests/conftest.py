# The root installer suite has no runner dependencies. Run the separately
# packaged runner and format checks with their locked environment (tests/README).
# The WER reader tests likewise import the installed runner. Its README gives the focused command.
# Legacy bundles contain subject projects; the runner acceptance suite prepares their catalogs.
collect_ignore = ["legacy-validation", "runner", "methodology", "skills/writing-explicit-rationale"]
