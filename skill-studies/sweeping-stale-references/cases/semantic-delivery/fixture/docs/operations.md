# Operating notification delivery

This guide describes the current notification worker exposed by `deliver` in
`src/delivery.py`.

After the first failed send, the worker has two additional tries available.
Successful delivery ends processing immediately; no further copies are sent.
When the worker returns false, record the notification for operator follow-up.
Do not start a second delivery cycle automatically.
