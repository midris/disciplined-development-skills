"""Small mechanical operations sharing the document checker and formats."""

import json
import os
import re
import subprocess
import tempfile
from hashlib import sha256
from pathlib import Path

from .references import regular_bytes
from .study import batch_sections, linked_files, scope


def require(report, complete=True):
    problems = [d for d in report.diagnostics if d.severity != "incomplete" or complete]
    if problems:
        raise ValueError("; ".join(f"{d.location}: {d.message}" for d in problems))


def identity(path, raw, revision=None, version="1"):
    return dict(
        path=str(path),
        sha256=sha256(raw).hexdigest(),
        version=version,
        **({"git_revision": revision} if revision else {}),
    )


def encoded(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def publish(path, raw, replace=False):
    """Publish a fully written file; an exclusive link prevents overwrite races."""
    path = Path(path)
    with tempfile.NamedTemporaryFile(
        dir=path.parent, prefix="." + path.name, delete=False
    ) as f:
        temp = Path(f.name)
        try:
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
        except BaseException:
            temp.unlink()
            raise
    try:
        if replace:
            os.replace(temp, path)
        else:
            os.link(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def read_document(path, kind, ctx):
    raw = regular_bytes(path)
    value = ctx.document(raw, path, kind)
    require(ctx.report)
    return value


def committed(ctx, path, revision):
    if not re.fullmatch("[0-9a-f]{40}", revision or ""):
        raise ValueError("A full commit revision is required")
    name = Path(path).absolute().relative_to(ctx.root).as_posix()
    mode = ctx.git_at(ctx.root, "ls-tree", revision, "--", name).decode().split()
    if not mode or mode[0] not in {"100644", "100755"}:
        raise ValueError(f"Committed regular file unavailable: {name}")
    raw = ctx.git_at(ctx.root, "show", f"{revision}:{name}")
    return identity(name, raw, revision), raw


def selected(path, batch, ctx, revision=None):
    raw = committed(ctx, path, revision)[1] if revision else regular_bytes(path)
    text = raw.decode("utf-8")
    body = batch_sections(text).get(batch)
    if body is None:
        raise ValueError(f"Unknown batch: {batch}")
    planned = scope(body, path, ctx)
    require(ctx.report)
    return text, body, planned


def definitions(body, path, ctx, revision=None):
    found = {}
    for _, p in linked_files(body, path):
        if p.suffix != ".json" or "manifest" not in p.name:
            continue
        ident, raw = (
            committed(ctx, p, revision) if revision else (None, regular_bytes(p))
        )
        m = ctx.document(raw, p, "manifest")
        require(ctx.report)
        ctx.manifest(m, p)
        require(ctx.report)
        if m["case_id"] in found:
            raise ValueError("Multiple collection manifests for one case")
        found[m["case_id"]] = (m, ident, p)
    return found


def membership(planned, records):
    keys = [r[:3] for r in planned]
    actual = [(a["case_id"], a["condition"], a["repetition"]) for a, _, _ in records]
    if any(a["retry_of"] is not None for a, _, _ in records) or actual != [
        k for k in keys if k in actual
    ]:
        raise ValueError(
            "Attempts differ from declared order/membership or contain retries"
        )


def configure(commands):
    p = commands.add_parser("retain")
    p.add_argument("protocol")
    p.add_argument("bundle")
    for name in ["batch", "index", "store", "revision"]:
        p.add_argument("--" + name, required=True)
    p.add_argument("--order", required=True, type=int)
    p = commands.add_parser("tables")
    p.add_argument("protocol")
    for name in ["batch", "index", "output"]:
        p.add_argument("--" + name, required=True)
    p.add_argument("--source-target")
    p.add_argument("--output-evidence")
    p = commands.add_parser("manifest")
    p.add_argument("manifest")
    p.add_argument("--output", required=True)
    p.add_argument("--revision")
    p.add_argument("--compare", nargs=2)
    p.add_argument("--allow-difference", action="append", default=[])


def run(args):
    try:
        if args.docs_command == "retain":
            from .retention import retain

            output = retain(args)
        elif args.docs_command == "tables":
            from .derived_tables import generate

            output = generate(args)
        else:
            from .manifest_tools import generate

            output = generate(args)
        print(output)
        return 0
    except (
        OSError,
        ValueError,
        TypeError,
        KeyError,
        AttributeError,
        UnicodeError,
        subprocess.SubprocessError,
    ) as error:
        print(f"Cannot {args.docs_command}: {error}")
        return 1
