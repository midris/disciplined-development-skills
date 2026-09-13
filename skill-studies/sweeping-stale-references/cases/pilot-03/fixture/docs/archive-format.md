# Archive format

Relaypack emits a ZIP with sorted members and a fixed timestamp for reproducible bytes.
Source files retain their contents. A generated manifest records name, normalized version and file digests.
The inspect command reads metadata and verifies each declared checksum without extracting the archive.
Release outputs go under build, which is ignored by Git. Archive contents are the deliverable, not console messages.
