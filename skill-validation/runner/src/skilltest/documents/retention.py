"""Verify and retain a stopped runner bundle before registering its attempt."""

import os
import shutil
import stat
import tempfile
from datetime import datetime
from pathlib import Path

from . import Report
from .formats import field, parse_json
from .operations import (
    committed,
    definitions,
    encoded,
    identity,
    membership,
    publish,
    read_document,
    require,
    selected,
)
from .references import Context, regular_bytes
from .study import index as check_index


def inventory(base):
    entries = []
    if base.is_symlink() or not base.is_dir():
        raise ValueError("Bundle must be a directory, not a symlink")

    def visit(folder):
        for p in sorted(folder.iterdir()):
            info = p.lstat()
            e = dict(
                path=p.relative_to(base).as_posix(),
                mode=oct(stat.S_IMODE(info.st_mode)),
            )
            if stat.S_ISLNK(info.st_mode):
                e.update(type="symlink", target=os.readlink(p))
            elif stat.S_ISDIR(info.st_mode):
                e.update(type="directory")
            elif stat.S_ISREG(info.st_mode):
                raw = regular_bytes(p)
                e.update(type="file", bytes=len(raw), sha256=identity(p, raw)["sha256"])
            else:
                raise ValueError(f"Special file cannot be retained: {p}")
            entries.append(e)
            if e["type"] == "directory":
                visit(p)

    visit(base)
    return entries


def retain(args):
    path = Path(args.protocol).absolute()
    ctx = Context(path, Report())
    text, body, planned = selected(path, args.batch, ctx, args.revision)
    ctx.document(text.encode(), path, "protocol")
    require(ctx.report)
    if not 1 <= args.order <= len(planned):
        raise ValueError("Order is outside the selected schedule")
    case, condition, rep, config_path = planned[args.order - 1]
    defs = definitions(body, path, ctx, args.revision)
    if case not in defs:
        raise ValueError("No frozen collection manifest for selected case")
    manifest, mi, mp = defs[case]
    conditions, _, configs = ctx.manifest(manifest, mp)
    if manifest["study_id"] != field(text, "Study ID") or condition not in conditions:
        raise ValueError("Study/condition differs from selected manifest")
    if conditions[condition]["configuration"]["path"] != config_path:
        raise ValueError("Scheduled configuration differs from manifest")
    source = Path(args.bundle).absolute()
    store = Path(args.store).absolute()
    index = Path(args.index).absolute()
    if source.is_symlink() or store.is_symlink() or index.is_symlink():
        raise ValueError("Source, store and index must not be symlinks")
    source, store = source.resolve(), store.resolve()
    if (
        store.is_relative_to(ctx.root)
        or source.is_relative_to(store)
        or store.is_relative_to(source)
    ):
        raise ValueError(
            "Store must be outside the repository and disjoint from source"
        )
    before = inventory(source)
    mechanical = parse_json(regular_bytes(source / "result.json"))
    invoked = mechanical.get("execution", {}).get("invocation_started")
    error = mechanical.get("infrastructure_error")
    if (
        mechanical.get("schema_version") != "0.4"
        or mechanical.get("status") not in {"COMPLETED", "INFRA_ERROR"}
        or not mechanical.get("finished_at")
        or type(invoked) is not bool
    ):
        raise ValueError(
            "Require a terminal version-0.4 result with a known invocation charge"
        )
    datetime.fromisoformat(mechanical["finished_at"])
    if error and (
        error.get("code") == "PROVIDER_CLEANUP_FAILED"
        or "cleanup" in error.get("message", "").lower()
    ):
        raise ValueError(
            "Unresolved provider cleanup; wait for the runner and inspect it"
        )
    if (
        mechanical.get("run_id") != source.name
        or mechanical.get("test", {}).get("id") != configs[condition]["id"]
    ):
        raise ValueError("Runner identity differs from bundle/configuration")
    if parse_json(regular_bytes(source / "config.json")) != configs[condition]:
        raise ValueError("Retained configuration differs from frozen configuration")
    dest = store / source.name
    inv_path = store / (source.name + ".inventory.json")
    if dest.exists() or dest.is_symlink() or inv_path.exists() or inv_path.is_symlink():
        raise ValueError(
            "Destination already exists; inspect rather than overwrite/adopt it"
        )
    store.mkdir(parents=True, exist_ok=True)
    lock = index.with_name(index.name + ".lock")
    # Exclusive lock protects cooperating registrations; no automatic stale-lock removal.
    with lock.open("x"):
        pass
    published = False
    try:
        original = regular_bytes(index) if index.exists() else None
        value = (
            read_document(index, "index", ctx)
            if original is not None
            else dict(
                format_version="1",
                index_id=f"{manifest['study_id']}-{args.batch}",
                study_id=manifest["study_id"],
                batch_id=args.batch,
                attempts=[],
            )
        )
        if (value["study_id"], value["batch_id"]) != (manifest["study_id"], args.batch):
            raise ValueError("Index belongs to another study/batch")
        records = check_index(value, index, ctx)
        require(ctx.report, complete=False)
        membership(planned, records)
        if any(
            a["run_id"] == source.name
            or (a["case_id"], a["condition"], a["repetition"]) == (case, condition, rep)
            for a in value["attempts"]
        ):
            raise ValueError("Duplicate run or attempt slot")
        attempt = dict(
            attempt_id=f"{args.batch}-{case}-{condition}-{rep}-1",
            case_id=case,
            condition=condition,
            repetition=rep,
            attempt_number=1,
            retry_of=None,
            manifest=mi,
            authorization=dict(
                artifact=committed(ctx, path, args.revision)[0],
                selector=f"Batch: {args.batch}; order {args.order}",
            ),
            run_id=source.name,
            allocation=dict(pool="subject", charge=int(invoked)),
            limitations=[f"Runner status: {mechanical['status']}; assessment pending."],
            bundle=dict(path=str(dest), inventory=None, verified=True),
            result=None,
        )
        membership(planned, [*records, (attempt, None, manifest)])
        with tempfile.TemporaryDirectory(dir=store, prefix=".retain-") as temp:
            stage = Path(temp) / source.name
            shutil.copytree(source, stage, symlinks=True)
            if inventory(stage) != before or inventory(source) != before:
                raise ValueError(
                    "Source changed or copied inventory differs; no registration written"
                )
            # mkdir reserves the destination without replacing an existing directory.
            dest.mkdir()
            published = True
            stage_mode = stat.S_IMODE(stage.stat().st_mode)
            stage.chmod(stage_mode | stat.S_IWUSR | stat.S_IXUSR)
            for p in stage.iterdir():
                p.rename(dest / p.name)
            stage.chmod(stage_mode)
            shutil.copystat(stage, dest)
            if inventory(dest) != before:
                raise ValueError("Published inventory differs")
            inv_raw = encoded(
                dict(format_version="1", bundle=str(dest), entries=before)
            )
            publish(inv_path, inv_raw)
            attempt["bundle"]["inventory"] = identity(inv_path, inv_raw)
            value["attempts"].append(attempt)
            # Check published references through the same checker consumers use.
            fresh = Context(path, Report())
            check_index(value, index, fresh)
            require(fresh.report, complete=False)
            if (regular_bytes(index) if index.exists() else None) != original:
                raise ValueError("Index changed during registration")
            publish(index, encoded(value), replace=original is not None)
        return index
    except BaseException as error:
        if published:
            raise ValueError(
                f"{error}; unregistered bundle retained for inspection at {dest}"
            ) from error
        raise
    finally:
        lock.unlink()
