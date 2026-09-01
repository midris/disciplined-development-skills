# Change request: show annual-plan price before confirmation

## Decision

For the September desktop-web annual-plan launch, show the approved monthly
equivalent in the existing change-plan sheet before **Confirm plan change**.

This release is a disclosure change only. The button's meaning, the request it
sends, the billing calculation, entitlement logic, and the post-confirmation
receipt are unchanged.

## Governing outcome

A member can see the selected annual plan's approved monthly equivalent before
the existing confirmation action. Rendering that relationship is the outcome;
conversion, click-through, and experiments are not success criteria.

## Explicit scope boundary

Included:

- The desktop-web change-plan sheet in the authenticated member portal.
- English (`en-US`) copy for the three annual plans listed in the interface
  contract.
- The existing supported desktop viewport range, 1024–1440 CSS pixels.

Excluded by the product decision:

- Native clients (scheduled separately for October) and other locales.
- Additional confirmation controls, server-side enforcement, price calculation,
  analytics, experiments, or persistent client state. They enlarge this
  display-only release without advancing its outcome.

## Acceptance criteria

1. Each listed annual ID shows its approved text above the existing button.
2. The text is static and present before that button is activated.
3. Existing focus order and accessible text relationship remain intact.
4. The request payload and billing endpoint do not change.
