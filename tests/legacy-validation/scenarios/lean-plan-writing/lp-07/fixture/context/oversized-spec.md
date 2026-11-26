# Oversized reporting program

The program contains four independently deployable subsystems in dependency order:

1. A storage schema and migration with its own compatibility tests.
2. An ingestion worker with unit and live queue smoke tests.
3. A query API with contract and live HTTP tests.
4. An operator dashboard with browser verification and documentation.

Each subsystem is expected to take roughly six commits and 35–45 KB of reviewable diff.
After its predecessor is available, each subsystem can be green, deployed, and reviewed independently.
The requester initially proposes one branch and one PR for the whole program.
