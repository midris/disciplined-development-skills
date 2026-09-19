"""Prepare working manifests and freeze matching Git inputs without Git writes."""

import posixpath
from copy import deepcopy
from pathlib import Path

from skilltest.config import load_config

from . import Report, structural
from .formats import field, parse_json
from .operations import committed, encoded, identity, publish, require, selected
from .references import Context, canonical, regular_bytes
from .study import linked_files


def prepare(value, path, ctx, revision=None, compare=None, allowed=()):
    m = deepcopy(value)

    def refresh(ident):
        name = canonical(ident["path"])
        p = ctx.root / name
        if Path(name).is_absolute() or p.resolve().is_relative_to(ctx.root) is False:
            raise ValueError("Manifest inputs must belong to the repository")
        if p.resolve() == path.resolve():
            raise ValueError("A manifest cannot pin itself")
        raw = regular_bytes(p)
        if revision and committed(ctx, p, revision)[1] != raw:
            raise ValueError(f"Working bytes differ from selected revision: {name}")
        return identity(name, raw, version=ident.get("version"))

    for key, v in m["authorities"].items():
        m["authorities"][key] = (
            [refresh(x) for x in v] if isinstance(v, list) else refresh(v)
        )
    m["controller_only"] = [refresh(x) for x in m["controller_only"]]
    sources, configs, mounts = {}, {}, {}
    for condition in m["conditions"]:
        ident = condition["configuration"] = refresh(condition["configuration"])
        cp = ctx.root / ident["path"]
        declaration = parse_json(regular_bytes(cp))
        # Resolve source names before load_config reads them, disallowing repository escapes.
        names = [declaration["prompt"]] + [f["source"] for f in declaration["fixtures"]]
        for name in names:
            if not isinstance(name, str) or Path(name).is_absolute():
                raise ValueError("Configuration sources must be relative")
            resolved = canonical(
                posixpath.normpath(
                    posixpath.join(posixpath.dirname(ident["path"]), name)
                )
            )
            sources[resolved] = refresh(dict(path=resolved, version=None))
        cfg = load_config(cp)
        if compare and any(f.target.as_posix() == "@prompt" for f in cfg.fixtures):
            raise ValueError(
                "Paired checking reserves @prompt for the prompt; rename that fixture target"
            )
        configs[condition["id"]] = cfg
        mounts[condition["id"]] = {
            "@prompt": regular_bytes(cfg.prompt),
            **{f.target.as_posix(): regular_bytes(f.source) for f in cfg.fixtures},
        }
    if allowed and not compare:
        raise ValueError("--allow-difference requires --compare")
    if compare:
        if len(set(compare)) != 2 or not set(compare) <= configs.keys():
            raise ValueError("Compare two distinct declared conditions")
        left, right = compare
        if configs[left].execution != configs[right].execution:
            raise ValueError("Paired execution settings differ")
        names = mounts[left].keys() | mounts[right].keys()
        if not set(allowed) <= names:
            raise ValueError("Allowed difference names an unknown mounted target")
        differing = {n for n in names if mounts[left].get(n) != mounts[right].get(n)}
        if differing - set(allowed):
            raise ValueError(
                f"Undeclared paired differences: {sorted(differing - set(allowed))}"
            )
    m["subject_sources"] = [sources[k] for k in sorted(sources)]
    m["status"] = "frozen" if revision else "draft"
    m["source_revision"] = revision or ""
    # Structural check with a complete revision, then the same deep validator in
    # explicit working mode. The returned draft never claims frozen readiness.
    structural(
        encoded({**m, "source_revision": revision or "0" * 40}).decode(),
        path,
        ctx.report,
    )
    require(ctx.report)
    ctx.manifest(m, path, working=not bool(revision))
    require(ctx.report)
    return m


def generate(args):
    path = Path(args.manifest).absolute()
    ctx = Context(path, Report())
    m = prepare(
        parse_json(regular_bytes(path)),
        path,
        ctx,
        args.revision,
        args.compare,
        args.allow_difference,
    )
    publish(args.output, encoded(m))
    return Path(args.output).absolute()


def preparation(path, raw, report, batch):
    # Draft status is allowed; all other structural incompleteness remains visible.
    local = report
    kind, _ = structural(
        raw.replace("Status: draft", "Status: prepared", 1), path, local
    )
    if kind != "protocol":
        raise ValueError("Preparation requires a protocol")
    report.kind = kind
    if not report.structurally_valid or not report.complete or report.unsupported:
        return
    ctx = Context(path, local)
    text, body, planned = selected(path, batch, ctx)
    found = {}
    for _, p in linked_files(body, path):
        if p.suffix != ".json" or "manifest" not in p.name:
            continue
        m = prepare(parse_json(regular_bytes(p)), p, ctx)
        if m["case_id"] in found:
            raise ValueError("Multiple manifests for one case")
        if m["study_id"] != field(text, "Study ID"):
            raise ValueError("Manifest study differs from protocol")
        found[m["case_id"]] = m
    for case, condition, _, config in planned:
        if case not in found:
            raise ValueError(f"Missing manifest for {case}")
        conditions = {c["id"]: c for c in found[case]["conditions"]}
        if (
            condition not in conditions
            or conditions[condition]["configuration"]["path"] != config
        ):
            raise ValueError("Scheduled condition/configuration differs from manifest")
    require(local)
    report.kind = "protocol"
