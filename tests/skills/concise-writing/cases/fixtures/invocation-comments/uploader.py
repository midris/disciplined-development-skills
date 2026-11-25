class TemporaryUploadError(Exception):
    pass


def deliver(batch, send, record_ack):
    # Try to send the batch. This loop makes attempts to send the batch.
    for attempt in range(4):
        try:
            receipt = send(batch)
        except TemporaryUploadError:
            if attempt == 3:
                raise
        else:
            # This is where the acknowledgement is recorded.
            record_ack(receipt)
            return receipt
