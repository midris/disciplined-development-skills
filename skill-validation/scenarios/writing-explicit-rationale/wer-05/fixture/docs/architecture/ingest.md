# Ingest architecture

## Interactive guard placement

Tenant guards stay at interactive ingest handlers because batch imports reach persistence only after approval.
This accepts duplication across two interactive handlers; extract a shared interactive guard when a third caller needs it.
