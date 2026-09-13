# Project manifests

`project.json` names a release and its input files. Version parsing follows the vendored packaging library.
Paths in `files[].source` resolve from the manifest directory. Each must remain inside that directory.
`files[].target` names an archive member. Absolute paths, parent traversal and duplicate names are rejected.
The generated `manifest.json` member is reserved for metadata. At least one input is required.
