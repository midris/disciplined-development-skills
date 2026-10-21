# Upload maintenance notes

The limit is four send attempts in total: the initial attempt plus at most three retries.
Only TemporaryUploadError raised by send is retried.
Other send errors propagate immediately, and the fourth temporary send failure also propagates.
A successful send ends the retry sequence; unused attempts are not performed.

record_ack stores the receipt after the remote service has accepted the batch.
It runs once after a successful send and never when all sends fail.
Any record_ack error propagates without sending the batch again, even if that error is TemporaryUploadError.
This boundary matters because the remote service has already accepted the batch: another send could upload it twice.
Keep acknowledgement recording outside the send-error retry handler.

For emphasis, four is the total attempt count rather than the number of retries after the initial send.
