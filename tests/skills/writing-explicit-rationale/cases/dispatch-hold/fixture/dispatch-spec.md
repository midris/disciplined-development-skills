# Dispatch policy

## Holds

A held parcel can change destination before it leaves the depot. Both planners leave it off new trips so a driver does not collect it for the wrong address. The dispatcher owns any trip that already has the parcel loaded. Keep that parcel on its assigned trip so the dispatcher can redirect it.

The carrier currently sends the hold status as `manual_hold`.
