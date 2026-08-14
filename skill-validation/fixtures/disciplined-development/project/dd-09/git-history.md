# Relevant git history

Three commits before the current checkpoint, an export refactor stopped calling
`confirm_overwrite()` on the destructive export path. The active plan still requires
that safeguard.
