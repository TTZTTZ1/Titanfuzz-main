"""Persistent review-candidate index backed by immutable API job files."""

from __future__ import annotations

import hashlib
import json
import os
import threading
from datetime import datetime
from pathlib import Path
from typing import Optional


ALLOWED_CATEGORIES = {"valid", "exception", "crash", "notarget", "hangs", "flaky"}
ALLOWED_STATES = {"pending_review", "reproduced", "needs_review", "rejected", "promoted"}
RECOMMEND_PATTERNS = (
    "internal assert",
    "check failed",
    "fatal",
    "device-side assert",
    "segmentation fault",
    "floating point exception",
    "double free",
    "invalid pointer",
    "invalid next size",
    "cpu/gpu",
    "varinconsistentcatch",
    "comparisonfail",
)


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def recommend_candidate(category: str, evidence: str) -> bool:
    if category in {"crash", "hangs"}:
        return True
    if category in {"notarget", "flaky", "valid"}:
        return False
    lowered = evidence.lower()
    return any(pattern in lowered for pattern in RECOMMEND_PATTERNS)


class CandidateStore:
    def __init__(self, repo_root: Path, index_path: Optional[Path] = None) -> None:
        self.repo_root = repo_root.resolve()
        self.jobs_root = (self.repo_root / "demo_runs" / "api_jobs").resolve()
        self.index_path = index_path or self.repo_root / "demo_runs" / "candidates" / "index.json"
        self._lock = threading.Lock()

    def _read(self) -> list[dict]:
        if not self.index_path.is_file():
            return []
        try:
            data = json.loads(self.index_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return []
        return data if isinstance(data, list) else []

    def _write(self, records: list[dict]) -> None:
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.index_path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(tmp, self.index_path)

    def list(self) -> list[dict]:
        return sorted(self._read(), key=lambda item: item.get("created_at", ""), reverse=True)

    def get(self, candidate_id: str) -> Optional[dict]:
        return next((item for item in self._read() if item.get("id") == candidate_id), None)

    def _validated_source(
        self,
        job_id: str,
        lib: str,
        api: str,
        category: str,
        source_path: Path,
    ) -> Path:
        if lib not in {"torch", "tf"}:
            raise ValueError("lib must be torch or tf")
        if category not in ALLOWED_CATEGORIES:
            raise ValueError("unsupported candidate category")
        source = source_path.resolve()
        if not source.is_file() or source.suffix != ".py":
            raise ValueError("candidate source must be an existing .py file")
        if not source.is_relative_to(self.jobs_root):
            raise ValueError("candidate source must be inside demo_runs/api_jobs")
        expected_root = self.jobs_root / job_id / "Results" / lib / category
        if not source.is_relative_to(expected_root.resolve()):
            raise ValueError("candidate source does not match job, library, or category")
        if source.stem.rsplit("_", 1)[0] != api:
            raise ValueError("candidate source does not match API")
        return source

    def add(
        self,
        *,
        job_id: str,
        lib: str,
        api: str,
        category: str,
        source_path: Path,
        note: str = "",
    ) -> dict:
        source = self._validated_source(job_id, lib, api, category, source_path)
        source_hash = sha256_file(source)
        evidence = source.read_text(encoding="utf-8", errors="replace")[:2000]
        with self._lock:
            records = self._read()
            existing = next(
                (
                    item
                    for item in records
                    if item.get("api") == api and item.get("source_sha256") == source_hash
                ),
                None,
            )
            if existing:
                return existing
            record = {
                "id": f"CAND-{len(records) + 1:04d}",
                "job_id": job_id,
                "lib": lib,
                "api": api,
                "category": category,
                "source_path": source.relative_to(self.repo_root).as_posix(),
                "source_sha256": source_hash,
                "status": "pending_review",
                "recommended": recommend_candidate(category, evidence),
                "error_summary": evidence[:500],
                "note": note.strip(),
                "created_at": now(),
                "updated_at": now(),
            }
            records.append(record)
            self._write(records)
            return record

    def update_status(self, candidate_id: str, status: str, note: Optional[str] = None) -> dict:
        if status not in ALLOWED_STATES:
            raise ValueError("unsupported candidate status")
        with self._lock:
            records = self._read()
            record = next((item for item in records if item.get("id") == candidate_id), None)
            if record is None:
                raise KeyError(candidate_id)
            record["status"] = status
            if note is not None:
                record["note"] = note.strip()
            record["updated_at"] = now()
            self._write(records)
            return record
