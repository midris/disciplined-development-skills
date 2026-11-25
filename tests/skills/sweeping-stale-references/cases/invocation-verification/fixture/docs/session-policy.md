# Session policy

The session TTL is 30 minutes by default because the partner rejects longer sessions.
This trades more frequent refreshes for partner compatibility.
For a shorter session, set `session_ttl_minutes` to a positive number of minutes.
Start times and returned expiry times are measured in seconds.
