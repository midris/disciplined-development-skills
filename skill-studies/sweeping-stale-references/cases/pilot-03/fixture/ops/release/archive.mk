.PHONY: release
release:
	python3 tools/relaypack.py build --manifest project.json --output-dir build/release
