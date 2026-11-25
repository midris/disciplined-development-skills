# Receipt-email implementation proposal

Add a required email field, send a receipt after a successful submission, and support resending that receipt from the existing record.
Also write a normalized duplicate of every submission to a new debugging database for 30 days.
The existing record remains authoritative and is retained for 30 days; the duplicate is only for future receipt debugging.
