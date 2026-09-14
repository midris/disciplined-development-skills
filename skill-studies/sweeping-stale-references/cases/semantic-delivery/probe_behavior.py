"""Observe runtime facts in an inspected disposable copy; never score prose.

The fixed module/function API belongs to this case. An unsupported refactor,
exception, or incomplete probe requires inspection rather than a skill verdict.
Subprocess isolation avoids ambient imports; it is not a security sandbox.
"""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


SCHEDULES = (
    ("delivery_fail", "delivery", "deliver", None),
    ("delivery_first", "delivery", "deliver", 1),
    ("delivery_second", "delivery", "deliver", 2),
    ("delivery_fourth", "delivery", "deliver", 4),
    ("download_fail", "download", "fetch", None),
    ("download_first", "download", "fetch", 1),
    ("download_third", "download", "fetch", 3),
)


def _probe(fixture):
    probes = {}
    for name, module, function, succeeds_on in SCHEDULES:
        # Fresh module per schedule avoids state leaking between observations.
        calls = []
        try:
            spec = importlib.util.spec_from_file_location(module, fixture / "src" / f"{module}.py")
            loaded = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(loaded)

            def transport():
                calls.append(len(calls) + 1)
                if len(calls) > 8:
                    raise RuntimeError("probe call limit exceeded")
                return succeeds_on is not None and len(calls) == succeeds_on

            returned = getattr(loaded, function)(transport)
            probes[name] = {
                "status": "observed" if type(returned) is bool else "needs_inspection",
                "calls": len(calls),
                "returned": returned if type(returned) is bool else repr(returned),
            }
        except Exception as error:
            probes[name] = {"status": "needs_inspection", "calls": None,
                            "returned": None, "error": f"{type(error).__name__}: {error}"}
    status = "observed" if all(p["status"] == "observed" for p in probes.values()) else "needs_inspection"
    return {"status": status, "probes": probes}


def observe(fixture, timeout=5):
    fixture = Path(fixture).resolve()
    try:
        result = subprocess.run(
            [sys.executable, "-I", "-B", str(Path(__file__).resolve()), "--probe", str(fixture)],
            cwd=fixture, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return {"status": "needs_inspection", "reason": "timeout", "probes": {}}
    except UnicodeDecodeError as error:
        return {"status": "needs_inspection", "reason": "unreadable_probe_output",
                "error": str(error), "probes": {}}
    except OSError as error:
        return {"status": "needs_inspection", "reason": str(error), "probes": {}}
    if result.returncode:
        return {"status": "needs_inspection", "reason": "probe_process_error",
                "exit_code": result.returncode, "stderr": result.stderr, "probes": {}}
    try:
        facts = json.loads(result.stdout)
    except ValueError:
        return {"status": "needs_inspection", "reason": "unreadable_probe_output",
                "stdout": result.stdout, "stderr": result.stderr, "probes": {}}
    # A module can exit successfully before our probe finishes, even after
    # printing valid JSON. Only a complete case-specific report is evidence.
    if not _complete_report(facts):
        return {"status": "needs_inspection", "reason": "incomplete_probe_output",
                "stdout": result.stdout, "stderr": result.stderr, "probes": {}}
    return facts


def _complete_report(facts):
    if not isinstance(facts, dict) or not isinstance(facts.get("probes"), dict):
        return False
    probes = facts["probes"]
    if set(probes) != {schedule[0] for schedule in SCHEDULES}:
        return False
    for probe in probes.values():
        if not isinstance(probe, dict) or not {"status", "calls", "returned"} <= probe.keys():
            return False
        if probe["status"] == "observed":
            if type(probe["calls"]) is not int or probe["calls"] < 0 or type(probe["returned"]) is not bool:
                return False
        elif probe["status"] != "needs_inspection":
            return False
    status = "observed" if all(p["status"] == "observed" for p in probes.values()) else "needs_inspection"
    return facts.get("status") == status


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--probe":
        print(json.dumps(_probe(Path(sys.argv[2]))))
    elif len(sys.argv) == 2:
        print(json.dumps(observe(Path(sys.argv[1])), indent=2))
    else:
        raise SystemExit("usage: probe_behavior.py DISPOSABLE_FIXTURE")
