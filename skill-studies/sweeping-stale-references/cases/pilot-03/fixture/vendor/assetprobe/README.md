# Assetprobe inventory export

This independently maintained utility exports inventory metadata rather than release archives.
Run from the checkout root:

```sh
python3 vendor/assetprobe/export.py --output-dir build/inventory
```

The output is `inventory.json`. Its CLI is maintained separately from Relaypack.
