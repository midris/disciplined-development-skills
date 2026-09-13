# Release process

A local packaging command is available through `make package`; `make release` prepares the release handoff.
Run these commands from the repository root. `scripts/package-local.sh` also works from another directory.
The GitHub release workflow builds the same demo project and uploads its ZIP as a workflow artifact.
Before handoff, run the CLI tests and inspect the built archive. Publishing to a package registry is not part of this tool.
