# Event-log replay contract

This source excerpt is the replay boundary for a JSON-lines event log that is the system of record.
Each nonempty record represents exactly one event, and replay must reconstruct every record in order.
One newline after the last record is the permitted file terminator.
An empty record before that final terminator is corruption and must be rejected rather than ignored.
Malformed or corrupt input must reach the caller as a typed failure.
