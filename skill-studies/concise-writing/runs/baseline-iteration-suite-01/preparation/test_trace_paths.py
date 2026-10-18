"""Recognize the observed CLI path representation without changing evidence."""
import importlib.util
from pathlib import Path
import pytest

spec=importlib.util.spec_from_file_location('cw_trace_paths',Path(__file__).with_name('trace_paths.py'))
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

@pytest.mark.parametrize('value,expected',[
    ('/workspace/fixture/report.md\n',True),
    ('/workspace/fixture/report.md',True),
    ('/workspace/fixture/settings.toml',True),
    ('/workspace/fixture/uploader.py',True),
    ('/workspace/fixture/report.md.backup',False),
    ('/workspace/fixture/TASK.md',False),
])
def test_target_write_path_handles_observed_terminal_newline(value,expected):
    assert module.is_target_path(value)==expected
