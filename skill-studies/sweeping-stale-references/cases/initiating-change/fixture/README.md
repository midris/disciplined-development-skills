# Session service

The service computes session expiry from a start time in seconds and a duration in minutes.
Set `token_ttl_minutes` in `config/defaults.json`; see [session policy](docs/session-policy.md).
Run `python3 scripts/show-session.py` from any directory to print the configured duration and example expiry.
Run `python3 -m unittest discover -s tests` from this directory to check behavior.
Archived rollout notes record past deployments; `vendor/` is an unmodified third-party package snapshot.
