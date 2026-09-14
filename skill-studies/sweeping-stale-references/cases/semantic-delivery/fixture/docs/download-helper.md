# Download helper

`fetch` in `src/download.py` is independent of notification delivery.
It makes at most three attempts to obtain an artifact, stopping after success.
The caller receives false if all attempts fail. This helper does not call the
notification worker or share its retry policy.
