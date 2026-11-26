# Decision record: annual-plan disclosure

- **Date:** 2026-08-12
- **Owner:** Member Billing product group
- **Status:** Approved for September desktop-web release

## Evidence reviewed

The complete supplied July support set in `support-evidence.md` records four
independent "price not visible before confirmation" cases. Every case is a
desktop-web contact, every charge is correct, and every member asks for the
monthly equivalent at the decision point.

The release manager scheduled native parity for October; Localization approved
an English-only September launch. Billing engineering confirmed that the
endpoint receives a plan ID, computes the price, and must not accept an amount.
The corresponding owner records are supplied in `approval-evidence.md`.

## Alternatives rejected

- **Second confirmation:** adds a step without showing the missing information.
- **Client calculation:** duplicates the billing price authority.
- **Instrumentation/A-B test:** measures a different, unapproved outcome.

## Verification record

Pricing Operations approved the exact strings in `interface-contract.md` on
2026-08-11. Design Systems confirmed `ChangePlanSheet` is the only desktop-web
surface with this selector and confirmation button.
Those approvals are included in `approval-evidence.md`.
