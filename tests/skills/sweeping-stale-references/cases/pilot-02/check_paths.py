"""Controller-only facts for pilot 02; no semantic or overall skill verdict."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

CASE = Path(__file__).resolve().parent


def observe(root):
    root = Path(root).resolve()
    expected = json.loads((CASE / "expected.json").read_text())
    consumers = [dict(x, role="service", destination=expected["moved_to"])
                 for x in expected["required_consumers"] if x["kind"] != "shell"]
    independent = expected["independent_link"]
    consumers.append(dict(path=independent["path"], kind="markdown",
                          role="independent", destination=independent["target"]))
    observations = []
    for item in consumers:
        source = root / item["path"]
        record = {"path": item["path"], "role": item["role"], "targets": [],
                  "correct_target": None, "status": "needs_inspection"}
        try:
            text = source.read_text()
            # This case uses inline links. Other Markdown forms need inspection.
            targets = [t for t in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text)
                       if Path(urlsplit(t).path).name == "setup.md"]
            for target in targets:
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc:
                    raise ValueError("nonlocal target requires inspection")
                resolved = (source.parent / unquote(parsed.path)).resolve()
                record["targets"].append({"text": target, "resolved": str(resolved),
                                          "exists": resolved.is_file(),
                                          "intended": resolved == root / item["destination"]})
            if targets:
                record["correct_target"] = all(t["exists"] and t["intended"]
                                                for t in record["targets"])
                record["status"] = "observed"
        except (OSError, ValueError, KeyError, TypeError) as error:
            record["inspection_reason"] = str(error)
        observations.append(record)
    preserved = {}
    for name in expected["preserve"]:
        path = root / name
        preserved[name] = path.is_file() and path.read_bytes() == (CASE / "fixture" / name).read_bytes()
    return {"references": observations, "preserved_bytes": preserved,
            "old_path_present": (root / expected["moved_from"]).exists(),
            "limit": "Facts only. Unsupported forms, changed preservation bytes, Git history and semantic outcomes require inspection. Shell consumer must be executed separately on a disposable copy."}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_paths.py FIXTURE")
    print(json.dumps(observe(Path(sys.argv[1])), indent=2))
