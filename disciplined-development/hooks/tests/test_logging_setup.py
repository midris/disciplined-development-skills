"""Tests for hooks.lib.logging_setup — consolidated rolling-day JSONL logging.

Covers the Part-G relocation: one rolling ``dd-hooks-YYYYMMDD.jsonl`` per dir
(not one file per process), dir resolution (DD_LOG_DIR env > logging.dir
config > derived ``.claude/.dd-state/.logs`` > /tmp fallback), the
``logging.enabled`` master switch, and the preserved never-crash +
reserved-field guarantees.
"""

from __future__ import annotations

import datetime
import json
from pathlib import Path

import pytest

from hooks.lib import config, logging_setup


def _today() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")


def _records(log_dir: Path) -> list[dict]:
    files = list(log_dir.glob("dd-hooks-*.jsonl"))
    out: list[dict] = []
    for f in files:
        out += [json.loads(line) for line in f.read_text().splitlines() if line.strip()]
    return out


def test_records_land_in_day_stamped_file(tmp_path):
    logger = logging_setup.setup("hookA", log_dir=str(tmp_path))
    logger.emit("invoked", count=3)
    day_file = tmp_path / f"dd-hooks-{_today()}.jsonl"
    assert day_file.is_file()
    recs = _records(tmp_path)
    assert len(recs) == 1
    assert recs[0]["hook"] == "hookA" and recs[0]["event"] == "invoked"
    assert recs[0]["count"] == 3


def test_two_loggers_share_one_day_file(tmp_path):
    # The relocation's point: NOT one file per process. Two loggers in the
    # same dir append to the same day file (cross-process rows are
    # distinguished by the pid field, asserted present here).
    a = logging_setup.setup("hookA", log_dir=str(tmp_path))
    b = logging_setup.setup("hookB", log_dir=str(tmp_path))
    a.emit("x")
    b.emit("y")
    files = list(tmp_path.glob("dd-hooks-*.jsonl"))
    assert len(files) == 1
    recs = _records(tmp_path)
    assert {r["hook"] for r in recs} == {"hookA", "hookB"}
    assert all("pid" in r for r in recs)


def test_dd_log_dir_env_wins(tmp_path, monkeypatch):
    monkeypatch.setenv("DD_LOG_DIR", str(tmp_path / "envdir"))
    logger = logging_setup.setup("hookA")  # no explicit log_dir
    logger.emit("x")
    assert (tmp_path / "envdir" / f"dd-hooks-{_today()}.jsonl").is_file()


def test_config_logging_dir_honored_when_no_env(tmp_path, monkeypatch):
    monkeypatch.delenv("DD_LOG_DIR", raising=False)
    cfg = tmp_path / "dd-config.json"
    cfg.write_text(json.dumps({"logging": {"dir": str(tmp_path / "cfgdir")}}))
    monkeypatch.setenv("DD_CONFIG", str(cfg))
    monkeypatch.delenv("DD_DEFAULTS", raising=False)
    config.reset_config_cache()
    try:
        logger = logging_setup.setup("hookA")
        logger.emit("x")
        assert (tmp_path / "cfgdir" / f"dd-hooks-{_today()}.jsonl").is_file()
    finally:
        config.reset_config_cache()


def test_enabled_false_writes_nothing(tmp_path, monkeypatch):
    monkeypatch.delenv("DD_LOG_DIR", raising=False)
    cfg = tmp_path / "dd-config.json"
    cfg.write_text(json.dumps({"logging": {"enabled": False, "dir": str(tmp_path / "d")}}))
    monkeypatch.setenv("DD_CONFIG", str(cfg))
    monkeypatch.delenv("DD_DEFAULTS", raising=False)
    config.reset_config_cache()
    try:
        logger = logging_setup.setup("hookA")
        logger.emit("x")
        assert not list((tmp_path / "d").glob("*.jsonl")) if (tmp_path / "d").exists() else True
    finally:
        config.reset_config_cache()


def test_claude_logs_dir_walk_up():
    start = Path("/x/proj/.claude/skills/disciplined-development/hooks/lib/logging_setup.py")
    assert logging_setup._claude_logs_dir(start) == Path(
        "/x/proj/.claude/.dd-state/.logs"
    )
    # No .claude ancestor → None (caller falls back).
    assert logging_setup._claude_logs_dir(Path("/tmp/x/y.py")) is None


def test_reserved_field_clobber_dropped(tmp_path, capsys):
    logger = logging_setup.setup("hookA", log_dir=str(tmp_path))
    logger.emit("x", hook="EVIL", pid=-1, ok=1)
    rec = _records(tmp_path)[0]
    assert rec["hook"] == "hookA" and rec["pid"] != -1
    assert rec["ok"] == 1


def test_append_review_writes_reviews_jsonl(tmp_path, monkeypatch):
    monkeypatch.setenv("DD_LOG_DIR", str(tmp_path))
    logging_setup.append_review({"decision": "PASS", "duration_s": 12})
    logging_setup.append_review({"decision": "BLOCK", "p1": 1})
    f = tmp_path / "reviews.jsonl"
    assert f.is_file()
    recs = [json.loads(line) for line in f.read_text().splitlines() if line.strip()]
    assert [r["decision"] for r in recs] == ["PASS", "BLOCK"]
    assert all("ts" in r for r in recs)  # writer stamps ts


def test_append_review_silent_when_disabled(tmp_path, monkeypatch):
    monkeypatch.delenv("DD_LOG_DIR", raising=False)
    cfg = tmp_path / "dd-config.json"
    cfg.write_text(json.dumps({"logging": {"enabled": False, "dir": str(tmp_path / "r")}}))
    monkeypatch.setenv("DD_CONFIG", str(cfg))
    monkeypatch.delenv("DD_DEFAULTS", raising=False)
    config.reset_config_cache()
    try:
        logging_setup.append_review({"decision": "PASS"})
        assert not (tmp_path / "r" / "reviews.jsonl").exists()
    finally:
        config.reset_config_cache()


def test_append_review_never_raises(tmp_path, monkeypatch):
    blocker = tmp_path / "b"
    blocker.write_text("x")
    monkeypatch.setenv("DD_LOG_DIR", str(blocker / "sub"))
    logging_setup.append_review({"decision": "PASS"})  # no exception


def test_emit_never_raises_on_unwritable_dir(tmp_path):
    # Point at a path under a file (mkdir/open will fail); emit must not raise.
    blocker = tmp_path / "blocker"
    blocker.write_text("x")
    logger = logging_setup.setup("hookA", log_dir=str(blocker / "sub"))
    logger.emit("x")  # no exception
