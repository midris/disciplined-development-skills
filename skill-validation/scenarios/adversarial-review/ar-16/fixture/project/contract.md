# Durable append contract

This source excerpt is the append boundary for an event log that is the system of record.
Every payload accepted by the static `Codable & Sendable` constraint is valid caller input to this boundary.
An encoding failure must reach the caller as a typed failure so the caller can decide whether to retry, reject the operation, or abort a larger transition.
The process must not terminate merely because such a payload cannot be encoded at runtime.
A successful return is permitted only after the record is durably committed.
