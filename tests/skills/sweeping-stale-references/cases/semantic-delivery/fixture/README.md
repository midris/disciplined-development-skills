# Notification worker

The worker sends a notification through a caller-provided transport.
A transport returns true on success and false when that attempt fails.

## Delivery limit

The worker makes at most three delivery attempts for a notification.
It stops as soon as delivery succeeds and reports failure if delivery is exhausted.

For operational handling, see [the operations guide](docs/operations.md) and
[troubleshooting](docs/troubleshooting.md).
The independent [download helper](docs/download-helper.md) is a separate operation.

## Local verification

No network service or third-party package is required:

```sh
python3 -m unittest discover -s tests
```
