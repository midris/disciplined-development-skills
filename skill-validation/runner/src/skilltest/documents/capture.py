"""Check runner-declared capture against the inventory being preserved."""

from functools import lru_cache
from importlib.resources import files
from pathlib import Path

from jsonschema import Draft202012Validator

from .formats import parse_json


@lru_cache(maxsize=1)
def validator():
    resource = files("skilltest").joinpath("_result.schema.json")
    raw = (
        resource.read_text(encoding="utf-8")
        if resource.is_file()
        else (Path(__file__).resolve().parents[3] / "result.schema.json").read_text(
            encoding="utf-8"
        )
    )
    return Draft202012Validator(parse_json(raw))


def verify_capture(result, entries):
    errors = list(validator().iter_errors(result))
    if errors:
        raise ValueError("Invalid runner record: " + errors[0].message)
    actual = {e["path"]: e for e in entries}
    for expected in result["artifacts"].values():
        name = expected["path"]
        found = actual.get(name)
        if "entries" not in expected:
            if found and found["type"] != "file":
                raise ValueError(f"Recorded file artifact is not regular: {name}")
            snapshot = dict(
                path=name,
                exists=found is not None,
                bytes=found["bytes"] if found else None,
                sha256=found["sha256"] if found else None,
            )
        else:
            exists = found is not None and found["type"] == "directory"
            children = [
                dict(
                    path=p[len(name) + 1 :],
                    type=e["type"],
                    bytes=e.get("bytes"),
                    sha256=e.get("sha256"),
                )
                for p, e in sorted(actual.items())
                if p.startswith(name + "/")
            ]
            snapshot = dict(
                path=name,
                exists=exists,
                empty=not children if exists else None,
                entries=children,
            )
        if snapshot != expected:
            raise ValueError(f"Captured artifact changed or disappeared: {name}")
