# Cache service

Example settings:

```json
{"cache_ttl": 30}
```

Run the application with `python3 src/cache.py --config config/defaults.json`.
The configured value is the maximum cache age in seconds.

Run checks with `python3 -m unittest discover -s tests`, `sh scripts/cache-smoke.sh` and `make smoke`.
