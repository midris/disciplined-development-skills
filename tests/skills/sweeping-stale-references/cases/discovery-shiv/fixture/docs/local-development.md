# Local input inventory

The file-list utility has its own CLI and produces JSON rather than an executable archive.
Run from the repository root:

```sh
python3 -I tools/inventory.py examples/greeting --output-file build/inventory.json
```

The report lists `greeting.py`. This utility's output option is independent of Shiv's interface.
