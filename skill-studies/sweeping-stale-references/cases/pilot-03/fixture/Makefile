.PHONY: help test package
include ops/release/archive.mk
help:
	@echo 'test: run CLI tests; package: make a local archive; release: prepare release archive'
test:
	python3 -m unittest discover -s tests
package:
	sh scripts/package-local.sh
