"""Exercise the collector's published metadata through its actual consumer."""
import hashlib
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from collect_one import inventory_record
from skilltest.documents import Report
from skilltest.documents.references import Context
from skilltest.documents.operations import encoded
from skilltest.documents.retention import inventory


def test_collector_inventory_is_accepted_by_study_reference_checker(tmp_path):
    bundle = tmp_path / 'bundle'
    bundle.mkdir()
    (bundle / 'output.md').write_text('Retained result.\n')
    target = tmp_path / 'bundle.inventory.json'
    target.write_bytes(encoded(inventory_record(bundle, inventory(bundle))))
    report = Report()
    owner = Path(__file__).resolve()
    Context(owner, report).inventory({
        'path': str(bundle),
        'inventory': {'path': str(target), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest(), 'version': '1'},
    }, owner)
    assert report.structurally_valid and not report.unsupported and report.complete, report.diagnostics
