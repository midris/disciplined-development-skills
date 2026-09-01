# Existing interface contract

`ChangePlanSheet` is the only desktop-web annual-plan shell. For this route,
`PlanId` is the closed union of exactly the three IDs below. The adjacent
display-metadata switch is already compile-time exhaustive over that union and
returns `PlanDisplayMetadata`. Adding a required `detailText: string` field to
that type and populating the existing switch in the same change makes every
switch branch supply the field.

The September route mounts `ChangePlanSheet` only for `en-US`; other locale
routes do not mount it. The shell renders its existing detail region, then the
existing `Confirm plan change` button. The region is ordinary visible text in
normal reading order, not an alert, tooltip, or asynchronously loaded element.

The selector can produce exactly these annual plan IDs in this release:

| Plan ID | Approved display text |
|---|---|
| `annual_starter` | `Starter annual — $12 per month, billed annually` |
| `annual_standard` | `Standard annual — $20 per month, billed annually` |
| `annual_pro` | `Pro annual — $35 per month, billed annually` |

These strings are the release-frozen September display contract. A price change
requires a new Pricing Operations decision and contract update before release;
the client must not calculate or derive a replacement value.

The shell owns 1024–1440 px layout and keeps the detail region immediately
before the button in DOM and keyboard order. That visible reading-order
relationship is the required accessible-text relationship; no ARIA linkage is
part of this contract. The existing component suite asserts the
selector–detail–confirm–cancel order and that submission sends only the selected
`PlanId` to the unchanged billing endpoint.

Changing the mounted selector updates the shell's `PlanId` and synchronously
re-renders the same detail region. The component test harness can exercise that
interaction without remounting the sheet.

There is no media query, container query, or conditional layout inside the
supported range; the same vertical stack renders from 1024 through 1440 px.
This release changes detail-region content only. Native clients do not run this
shell.
