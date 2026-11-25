# Implementation proposal: approved annual-plan disclosure

## Change

In `web/member-billing/ChangePlanSheet.tsx`, add required
`detailText: string` to `PlanDisplayMetadata` and populate the existing
exhaustive `PlanId` display-metadata switch with these values:

| `PlanId` | Detail-region text |
|---|---|
| `annual_starter` | `Starter annual — $12 per month, billed annually` |
| `annual_standard` | `Standard annual — $20 per month, billed annually` |
| `annual_pro` | `Pro annual — $35 per month, billed annually` |

Render the selected value in the existing detail region above the existing
**Confirm plan change** button. The static mapping performs no fetch, storage,
price arithmetic, parsing, or request-payload change.

`PlanId` is closed over the three contract IDs. Because the new field is part of
the existing exhaustive switch, a future ID cannot compile without a text
field; Pricing Operations approval remains a release decision, not a type
guarantee. Do not change `submitPlanChange`, its payload, or endpoint.

## Why this is necessary and sufficient

The decision record identifies the missing information and decision surface.
One mapping supplies it before the existing action for all three launch plans.
Calculations, a second action, or client acknowledgement add behavior without
making the approved text more visible.

## Validation

Add one component test per `PlanId` (three total): render the shell, assert the
single existing detail region's complete text equals that selected plan's
approved text, and assert that region immediately precedes **Confirm plan
change** in the DOM. Retain the existing selector–detail–confirm–cancel
accessibility/keyboard-order test and the existing assertion that submission
sends only the selected `PlanId` to the unchanged billing endpoint.

Add one interaction test that mounts the sheet once, changes the selector
through all three `PlanId` values, and after each change asserts that the same
detail region contains only the newly selected plan's approved text.

Run the existing component tests. At 1024 px and 1440 px—the boundaries of the
contract's single layout regime—inspect each selected plan state and confirm
the text is visible above the button. No native, other-locale, analytics, or
persistence validation is needed: those paths do not run or change.
