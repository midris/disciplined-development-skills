# Fixture projects contain subject tests, including deliberately stale code.
# The controller tests below replay them only in the intended project context.
collect_ignore_glob = ["cases/*/fixture"]
