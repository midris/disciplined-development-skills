.PHONY: release-example
release-example:
	mkdir -p build
	python3 -I tools/shiv-local.py --site-packages examples/greeting -e greeting:main --output-file build/release.pyz
