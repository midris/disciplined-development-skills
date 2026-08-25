# Coupled private configuration rename

Rename the private configuration key `quota_mode` to `limit_mode` in:

- `src/config_schema.py`
- `src/config_loader.py`
- `tests/test_config.py`

The configuration is generated and consumed only inside this unreleased service.
No backward compatibility or staged rollout is required.
The complete change is under 150 lines.
Splitting schema, loader, and tests would leave every intermediate branch red or internally inconsistent.
The team asks whether separate PRs per file would be more disciplined.
