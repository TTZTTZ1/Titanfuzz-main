"""Validation helpers for the curated confirmed-bug index."""

from __future__ import annotations

import json
from pathlib import Path


def _read_object(path: Path):
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return value


def load_confirmed_records(index_path: Path, repo_root: Path) -> list[dict]:
    index = _read_object(index_path)
    if not isinstance(index, list):
        return []
    root = repo_root.resolve()
    records = []
    for raw in index:
        if not isinstance(raw, dict) or not raw.get("id") or not raw.get("path"):
            continue
        meta_path = (root / str(raw["path"])).resolve()
        if not meta_path.is_relative_to(root) or not meta_path.is_file():
            continue
        meta = _read_object(meta_path)
        if not isinstance(meta, dict) or meta.get("id") != raw.get("id"):
            continue
        repro_name = str(meta.get("files", {}).get("repro", "repro.py"))
        repro_path = (meta_path.parent / repro_name).resolve()
        if not repro_path.is_relative_to(meta_path.parent.resolve()) or not repro_path.is_file():
            continue
        record = {**raw, **meta}
        record.pop("severity", None)
        records.append(record)
    return records
