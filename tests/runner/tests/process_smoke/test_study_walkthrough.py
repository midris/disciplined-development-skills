"""Exercise two frozen slots and assess the outputs of the installed CLI offline."""

import json

import pytest

from skilltest.cli import main
from test_documents import document_study


@pytest.mark.parametrize("document_study", ["run-cli"], indirect=True)
def test_study_walkthrough(document_study, capsys):
    root, _, _, _ = document_study
    for stage in ("collection", "assessment"):
        assert main([
            "docs", "check", str(root / "protocol.md"),
            "--ready-for", stage, "--batch", "example", "--json",
        ]) == 0
        assert json.loads(capsys.readouterr().out)["complete"]
