.PHONY: help example local-test
include build-support/release/example.mk
help:
	@echo 'example: build greeting locally; release-example: build release artifact; local-test: check current CLI'
example:
	sh scripts/build-example.sh
local-test:
	python3 -m unittest discover -s tests_local
