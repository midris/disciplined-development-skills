# Notification delivery troubleshooting

For the current notification worker, the third consecutive failed send exhausts
automatic delivery attempts. A false result means the notification needs
operator attention.

A true result means delivery succeeded; do not resend that notification merely
because earlier attempts failed.
