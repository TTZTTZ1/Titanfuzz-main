#!/usr/bin/env python3
"""Local presentation server for TensorGuard/TitanFuzz-main."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import mimetypes
import os
import platform
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, Optional
from urllib.parse import parse_qs, unquote, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
STATIC_ROOT = Path(__file__).resolve().parent / "static"

MANIFEST_PATH = REPO_ROOT / "prompt_library_manifest.json"
PAPER_BUG_ROOT = REPO_ROOT / "reports" / "paper_confirmed_bugs"
PAPER_BUG_INDEX = PAPER_BUG_ROOT / "index.json"
DEMO_ROOT = REPO_ROOT / "demo_runs"
API_JOB_ROOT = DEMO_ROOT / "api_jobs"
REPRO_JOB_ROOT = DEMO_ROOT / "repro_jobs"

API_LIST_PATHS = {
    "torch": REPO_ROOT / "data" / "torch_apis.txt",
    "tf": REPO_ROOT / "data" / "tf_apis.txt",
}
RESULTS_PATHS = {
    "torch": REPO_ROOT / "Results" / "torch",
    "tf": REPO_ROOT / "Results" / "tf",
}
RESULT_SUBDIRS = ("seed", "valid", "exception", "crash", "notarget", "hangs", "flaky")
TRACE_PATTERNS = (
    "Catch",
    "Fail",
    "INTERNAL ASSERT",
    "device-side assert",
    "invalid argument",
    "Segmentation fault",
    "Floating point exception",
    "free()",
    "Aborted",
    "Check failed",
)
REPRO_SUCCESS_PATTERNS = (
    "Segmentation fault",
    "Floating point exception",
    "Aborted",
    "Check failed",
    "INTERNAL ASSERT",
    "Assertion failure",
    "double free",
    "free():",
    "invalid next size",
    "device-side assert",
    "Fatal",
    "fatal",
)
API_STAGE_ORDER = ("prompt_check", "qwen_seed", "ev_generation", "driver", "summary")
REPRO_TIMEOUT_SECONDS = 60


def now() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def safe_name(value: str) -> str:
    keep = []
    for ch in value:
        keep.append(ch if ch.isalnum() or ch in "._-" else "_")
    name = "".join(keep).strip("._")
    return name or "item"


def display_bug_id(bug_id: str) -> str:
    return bug_id.removeprefix("PAPER-")


def rel(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_json(path: Path, default: Any) -> Any:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def write_response(handler: BaseHTTPRequestHandler, status: int, body: bytes, content_type: str) -> None:
    handler.send_response(status)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


def send_json(handler: BaseHTTPRequestHandler, payload: Any, status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
    write_response(handler, status, body, "application/json; charset=utf-8")


def send_text(handler: BaseHTTPRequestHandler, text: str, status: int = 200, content_type: str = "text/plain") -> None:
    write_response(handler, status, text.encode("utf-8"), f"{content_type}; charset=utf-8")


def load_manifest() -> dict:
    return read_json(MANIFEST_PATH, {"libraries": {"torch": {}, "tf": {}}, "total_apis": 0})


def load_api_list(lib: str) -> list[str]:
    path = API_LIST_PATHS.get(lib)
    if path is None or not path.is_file():
        return []
    apis = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            api = line.strip()
            if api and not api.startswith("#"):
                apis.append(api)
    return apis


def manifest_entry(lib: str, api: str) -> Optional[dict]:
    return load_manifest().get("libraries", {}).get(lib, {}).get(api)


def prompt_path(lib: str, api: str) -> Path:
    return REPO_ROOT / "experiment" / lib / api / "prompts" / "structured_info.txt"


def count_py(path: Path) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for child in path.iterdir() if child.is_file() and child.suffix == ".py")


def result_counts(results_dir: Path) -> dict:
    return {name: count_py(results_dir / name) for name in RESULT_SUBDIRS}


def api_result_counts(lib: str, api: str) -> dict:
    root = RESULTS_PATHS[lib]
    counts = {}
    for name in RESULT_SUBDIRS:
        folder = root / name
        if not folder.is_dir():
            counts[name] = 0
            continue
        total = 0
        for path in folder.iterdir():
            if not path.is_file() or path.suffix != ".py":
                continue
            if path.stem.rsplit("_", 1)[0] == api:
                total += 1
        counts[name] = total
    return counts


def results_api_set(lib: str) -> set[str]:
    root = RESULTS_PATHS[lib]
    known = set(load_api_list(lib))
    found = set()
    for subdir in RESULT_SUBDIRS:
        folder = root / subdir
        if not folder.is_dir():
            continue
        for path in folder.iterdir():
            if not path.is_file() or path.suffix != ".py":
                continue
            api_name = path.stem.rsplit("_", 1)[0]
            if api_name in known:
                found.add(api_name)
    return found


def trace_path(lib: str) -> Path:
    return RESULTS_PATHS[lib] / "trace.txt"


def trace_hit_count(path: Path) -> int:
    if not path.is_file():
        return 0
    total = 0
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if any(pattern in line for pattern in TRACE_PATTERNS):
                total += 1
    return total


def tail(path: Path, max_chars: int = 8000) -> str:
    if not path.is_file():
        return ""
    data = path.read_bytes()
    return data[-max_chars:].decode("utf-8", errors="replace")


def latest_summaries(root: Path, limit: int = 6) -> list[dict]:
    if not root.is_dir():
        return []
    paths = sorted(root.glob("**/summary.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    out = []
    for path in paths[:limit]:
        item = read_json(path, {})
        if item:
            item["_path"] = rel(path)
            out.append(item)
    return out


def overview_payload() -> dict:
    manifest = load_manifest()
    manifest_libs = manifest.get("libraries", {})
    api_lists = {lib: load_api_list(lib) for lib in ("torch", "tf")}
    api_counts = {lib: len(apis) for lib, apis in api_lists.items()}
    prompt_ready = {
        lib: sum(1 for api in apis if api in manifest_libs.get(lib, {}) or prompt_path(lib, api).is_file())
        for lib, apis in api_lists.items()
    }
    results = {}
    for lib in ("torch", "tf"):
        root = RESULTS_PATHS[lib]
        trace = trace_path(lib)
        results[lib] = {
            "path": rel(root),
            "exists": root.is_dir(),
            "api_count": len(results_api_set(lib)) if root.is_dir() else 0,
            "counts": result_counts(root),
            "trace_path": rel(trace),
            "trace_exists": trace.is_file(),
            "trace_hits": trace_hit_count(trace),
        }

    paper_bugs = load_paper_bugs()
    bug_by_framework: Dict[str, int] = {}
    for bug in paper_bugs:
        fw = bug.get("framework", "Unknown")
        bug_by_framework[fw] = bug_by_framework.get(fw, 0) + 1

    return {
        "api_total": sum(api_counts.values()),
        "api_by_lib": api_counts,
        "prompt_ready_total": sum(prompt_ready.values()),
        "prompt_ready_by_lib": prompt_ready,
        "results": results,
        "paper_bug_total": len(paper_bugs),
        "paper_bug_by_framework": bug_by_framework,
        "latest_api_jobs": latest_summaries(API_JOB_ROOT),
        "latest_repro_jobs": latest_repro_summaries(),
        "sources": {
            "torch_api_list": rel(API_LIST_PATHS["torch"]),
            "tf_api_list": rel(API_LIST_PATHS["tf"]),
            "prompt_library": "experiment/<lib>/<api>/prompts/",
            "api_jobs": rel(API_JOB_ROOT),
            "repro_jobs": rel(REPRO_JOB_ROOT),
        },
    }


def api_list_payload(lib: str, query: str = "", limit: int = 200) -> list[dict]:
    query_l = query.lower().strip()
    manifest_lib = load_manifest().get("libraries", {}).get(lib, {})
    apis = load_api_list(lib)
    if query_l:
        apis = [api for api in apis if query_l in api.lower()]
    out = []
    for api in apis[:limit]:
        entry = manifest_lib.get(api, {})
        ppath = prompt_path(lib, api)
        out.append(
            {
                "api": api,
                "lib": lib,
                "has_prompt": api in manifest_lib or ppath.is_file(),
                "prompt_path": rel(ppath),
                "result_counts": api_result_counts(lib, api),
                "has_results": any(api_result_counts(lib, api).values()),
                "manifest_entry": entry,
            }
        )
    return out


def api_detail_payload(lib: str, api: str) -> tuple[int, dict]:
    if lib not in ("torch", "tf"):
        return 400, {"error": "lib must be torch or tf"}
    if api not in load_api_list(lib):
        return 404, {"error": f"api not found in data/{lib}_apis.txt"}
    entry = manifest_entry(lib, api) or {}
    ppath = prompt_path(lib, api)
    counts = api_result_counts(lib, api)
    return 200, {
        "api": api,
        "lib": lib,
        "api_list": rel(API_LIST_PATHS[lib]),
        "has_prompt": bool(entry) or ppath.is_file(),
        "prompt_path": rel(ppath),
        "prompt_exists": ppath.is_file(),
        "results_path": rel(RESULTS_PATHS[lib]),
        "result_counts": counts,
        "has_results": any(counts.values()),
        "manifest_entry": entry,
    }


def start_api_job(payload: dict) -> tuple[int, dict]:
    lib = payload.get("lib", "torch")
    api = payload.get("api", "")
    mode = payload.get("mode", "demo")
    qwen_model = payload.get("qwen_model", "../Qwen2.5-Coder-7B-Instruct")
    mut_model = payload.get("mut_model", "facebook/incoder-6B")
    cuda_device = str(payload.get("cuda_device", "0"))

    if lib not in ("torch", "tf"):
        return 400, {"error": "lib must be torch or tf"}
    if mode not in ("demo", "normal"):
        return 400, {"error": "mode must be demo or normal"}
    if api not in load_api_list(lib):
        return 400, {"error": f"api not found in {rel(API_LIST_PATHS[lib])}"}
    if not prompt_path(lib, api).is_file() and manifest_entry(lib, api) is None:
        return 400, {"error": f"prompt library missing for {lib}:{api}"}

    ts = time.strftime("%Y%m%d_%H%M%S")
    job_id = f"api_{safe_name(lib)}_{safe_name(api)}_{ts}"
    out = API_JOB_ROOT / job_id
    out.mkdir(parents=True, exist_ok=True)
    server_log = out / "server_launch.log"
    cmd = [
        sys.executable,
        "scripts/run_one_api_demo.py",
        "--lib",
        lib,
        "--api",
        api,
        "--constraints_dir",
        f"experiment/{lib}",
        "--qwen_model",
        qwen_model,
        "--mut_model",
        mut_model,
        "--out",
        rel(out),
        "--mode",
        mode,
        "--job_id",
        job_id,
        "--cuda_device",
        cuda_device,
        "--force_redo",
    ]

    def _launch() -> None:
        with server_log.open("w", encoding="utf-8") as log:
            log.write("$ " + " ".join(cmd) + "\n\n")
            log.flush()
            subprocess.Popen(
                cmd,
                cwd=REPO_ROOT,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
            )

    threading.Thread(target=_launch, daemon=True).start()
    return 202, {"job_id": job_id, "out": rel(out)}


def find_api_job(job_id: str) -> Optional[Path]:
    direct = API_JOB_ROOT / job_id
    if direct.is_dir():
        return direct
    if not API_JOB_ROOT.is_dir():
        return None
    for status_path in API_JOB_ROOT.glob("**/status.json"):
        status = read_json(status_path, {})
        if status.get("job_id") == job_id:
            return status_path.parent
    return None


def api_job_payload(job_id: str) -> tuple[int, dict]:
    out = find_api_job(job_id)
    if out is None:
        return 404, {"error": "api job not found"}
    status = read_json(out / "status.json", {})
    summary = read_json(out / "summary.json", {})
    logs = {}
    if (out / "logs").is_dir():
        for path in sorted((out / "logs").glob("*.log")):
            logs[path.name] = tail(path)
    logs["server_launch.log"] = tail(out / "server_launch.log")
    return 200, {
        "job_id": job_id,
        "out": rel(out),
        "status": status,
        "summary": summary,
        "logs": logs,
    }


def load_paper_bugs() -> list[dict]:
    items = read_json(PAPER_BUG_INDEX, [])
    out = []
    for item in items:
        item = dict(item)
        meta_path = REPO_ROOT / item.get("path", "")
        if meta_path.is_file():
            meta = read_json(meta_path, {})
            item.update({k: v for k, v in meta.items() if k not in item or item[k] in ("", None)})
            item["meta_path"] = rel(meta_path)
        item["display_id"] = display_bug_id(str(item.get("id", "")))
        out.append(item)
    return out


def paper_bug_detail(bug_id: str) -> tuple[int, dict]:
    for item in read_json(PAPER_BUG_INDEX, []):
        if item.get("id") != bug_id:
            continue
        meta_path = REPO_ROOT / item.get("path", "")
        if not meta_path.is_file():
            return 404, {"error": "bug meta not found"}
        meta = read_json(meta_path, {})
        bug_dir = meta_path.parent
        repro = bug_dir / meta.get("files", {}).get("repro", "repro.py")
        report = bug_dir / meta.get("files", {}).get("report", "report.md")
        return 200, {
            "index": item,
            "meta": meta,
            "display_id": display_bug_id(bug_id),
            "bug_dir": rel(bug_dir),
            "repro_path": rel(repro),
            "report_path": rel(report),
            "repro_code": repro.read_text(encoding="utf-8", errors="replace") if repro.is_file() else "",
            "report_markdown": report.read_text(encoding="utf-8", errors="replace") if report.is_file() else "",
        }
    return 404, {"error": "confirmed bug not found"}


def read_body(handler: BaseHTTPRequestHandler) -> tuple[bool, dict]:
    length = int(handler.headers.get("Content-Length", "0"))
    raw = handler.rfile.read(length)
    try:
        payload = json.loads(raw.decode("utf-8")) if raw else {}
        if not isinstance(payload, dict):
            return False, {"error": "JSON body must be an object"}
        return True, payload
    except Exception:
        return False, {"error": "invalid JSON"}


def repro_status_template(job_id: str, bug_id: str, modes: list[str], out: Path) -> dict:
    return {
        "job_id": job_id,
        "bug_id": bug_id,
        "status": "pending",
        "started_at": now(),
        "updated_at": now(),
        "out": rel(out),
        "timeout_seconds": REPRO_TIMEOUT_SECONDS,
        "modes": {
            mode: {
                "status": "pending",
                "returncode": None,
                "timed_out": False,
                "log": rel(out / f"{mode}.log"),
                "started_at": None,
                "finished_at": None,
            }
            for mode in modes
        },
        "report": rel(out / "report.md"),
        "error": None,
    }


def run_repro_mode(repro: Path, mode: str, log_path: Path, timeout: int) -> dict:
    env = os.environ.copy()
    if mode == "cpu":
        env["CUDA_VISIBLE_DEVICES"] = ""
    elif mode == "gpu0":
        env["CUDA_VISIBLE_DEVICES"] = "0"
    else:
        raise ValueError(f"unknown mode: {mode}")

    cmd = [sys.executable, str(repro)]
    started = time.time()
    with log_path.open("w", encoding="utf-8") as log:
        log.write("$ " + " ".join(cmd) + "\n")
        log.write(f"CUDA_VISIBLE_DEVICES={env.get('CUDA_VISIBLE_DEVICES', '')!r}\n\n")
        log.flush()
        try:
            proc = subprocess.run(
                cmd,
                cwd=repro.parent,
                stdout=log,
                stderr=subprocess.STDOUT,
                env=env,
                text=True,
                timeout=timeout,
            )
            return {
                "status": "finished",
                "returncode": proc.returncode,
                "timed_out": False,
                "elapsed_seconds": round(time.time() - started, 3),
                "verdict": classify_repro_result(proc.returncode, False, tail(log_path)),
            }
        except subprocess.TimeoutExpired as exc:
            log.write(f"\n[TIMEOUT] exceeded {timeout}s\n")
            return {
                "status": "timeout",
                "returncode": None,
                "timed_out": True,
                "elapsed_seconds": round(time.time() - started, 3),
                "error": str(exc),
                "verdict": "timeout",
            }
        except Exception as exc:
            log.write(f"\n[SERVER ERROR] {exc}\n")
            return {
                "status": "failed",
                "returncode": None,
                "timed_out": False,
                "elapsed_seconds": round(time.time() - started, 3),
                "error": str(exc),
                "verdict": "needs_review",
            }


def classify_repro_result(returncode: Optional[int], timed_out: bool, log_text: str) -> str:
    if timed_out:
        return "timeout"
    if returncode == 0:
        return "not_reproduced"
    if returncode is None:
        return "needs_review"
    if any(pattern in log_text for pattern in REPRO_SUCCESS_PATTERNS):
        return "reproduced"
    return "needs_review"


def start_repro_job(bug_id: str, payload: dict) -> tuple[int, dict]:
    status_code, detail = paper_bug_detail(bug_id)
    if status_code != 200:
        return status_code, detail
    meta = detail["meta"]
    repro = REPO_ROOT / detail["repro_path"]
    if not repro.is_file():
        return 404, {"error": "repro.py not found"}

    requested = payload.get("modes", ["cpu", "gpu0"])
    if isinstance(requested, str):
        requested = [requested]
    modes = [mode for mode in requested if mode in ("cpu", "gpu0")]
    if not modes:
        return 400, {"error": "modes must include cpu or gpu0"}

    timeout = int(payload.get("timeout", REPRO_TIMEOUT_SECONDS) or REPRO_TIMEOUT_SECONDS)
    ts = time.strftime("%Y%m%d_%H%M%S")
    job_id = f"repro_{safe_name(display_bug_id(bug_id))}_{ts}"
    out = REPRO_JOB_ROOT / job_id
    out.mkdir(parents=True, exist_ok=True)
    status = repro_status_template(job_id, bug_id, modes, out)
    status["timeout_seconds"] = timeout
    status["meta"] = {
        "title": meta.get("title", ""),
        "framework": meta.get("framework", ""),
        "api": meta.get("api", ""),
        "bug_type": meta.get("bug_type", ""),
        "severity": meta.get("severity", ""),
    }
    write_json(out / "status.json", status)
    (out / "repro.py").write_text(repro.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")

    def _worker() -> None:
        current = read_json(out / "status.json", status)
        current["status"] = "running"
        current["updated_at"] = now()
        write_json(out / "status.json", current)
        for mode in modes:
            current = read_json(out / "status.json", current)
            current["modes"][mode]["status"] = "running"
            current["modes"][mode]["started_at"] = now()
            current["updated_at"] = now()
            write_json(out / "status.json", current)
            result = run_repro_mode(repro, mode, out / f"{mode}.log", timeout)
            current = read_json(out / "status.json", current)
            current["modes"][mode].update(result)
            current["modes"][mode]["finished_at"] = now()
            current["updated_at"] = now()
            write_json(out / "status.json", current)
        current = read_json(out / "status.json", current)
        current["status"] = "finished"
        current["updated_at"] = now()
        write_json(out / "status.json", current)

    threading.Thread(target=_worker, daemon=True).start()
    return 202, {"job_id": job_id, "out": rel(out)}


def find_repro_job(job_id: str) -> Optional[Path]:
    direct = REPRO_JOB_ROOT / job_id
    if direct.is_dir():
        return direct
    if not REPRO_JOB_ROOT.is_dir():
        return None
    for status_path in REPRO_JOB_ROOT.glob("**/status.json"):
        status = read_json(status_path, {})
        if status.get("job_id") == job_id:
            return status_path.parent
    return None


def repro_job_payload(job_id: str) -> tuple[int, dict]:
    out = find_repro_job(job_id)
    if out is None:
        return 404, {"error": "repro job not found"}
    status = read_json(out / "status.json", {})
    for mode, item in status.get("modes", {}).items():
        if item.get("verdict") or item.get("status") not in ("finished", "timeout", "failed"):
            continue
        item["verdict"] = classify_repro_result(
            item.get("returncode"),
            bool(item.get("timed_out")),
            tail(out / f"{mode}.log"),
        )
    logs = {}
    for name in ("cpu.log", "gpu0.log"):
        path = out / name
        if path.is_file():
            logs[name] = tail(path)
    report = out / "report.md"
    return 200, {
        "job_id": job_id,
        "out": rel(out),
        "status": status,
        "logs": logs,
        "report_exists": report.is_file(),
        "report_path": rel(report),
        "report_markdown": report.read_text(encoding="utf-8", errors="replace") if report.is_file() else "",
    }


def latest_repro_summaries(limit: int = 6) -> list[dict]:
    if not REPRO_JOB_ROOT.is_dir():
        return []
    paths = sorted(REPRO_JOB_ROOT.glob("**/status.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    out = []
    for path in paths[:limit]:
        status = read_json(path, {})
        if status:
            status["_path"] = rel(path)
            out.append(status)
    return out


def summarize_mode(status: dict, mode: str, out: Path) -> str:
    item = status.get("modes", {}).get(mode, {})
    log_name = f"{mode}.log"
    return "\n".join(
        [
            f"### {mode.upper()}",
            "",
            f"- Status: `{item.get('status', 'not-run')}`",
            f"- Return code: `{item.get('returncode')}`",
            f"- Timed out: `{item.get('timed_out', False)}`",
            f"- Log: `{rel(out / log_name)}`",
            "",
            "```text",
            tail(out / log_name, max_chars=12000).rstrip(),
            "```",
            "",
        ]
    )


def repro_conclusion(status: dict) -> str:
    modes = status.get("modes", {})
    finished = [m for m, item in modes.items() if item.get("status") in ("finished", "timeout", "failed")]
    if not finished:
        return "当前环境尚未运行复现。"
    reproduced = []
    not_reproduced = []
    timed_out = []
    needs_review = []
    for mode, item in modes.items():
        verdict = item.get("verdict")
        if not verdict and item.get("status") in ("finished", "timeout", "failed"):
            log_name = f"{mode}.log"
            verdict = classify_repro_result(item.get("returncode"), bool(item.get("timed_out")), tail(find_repro_job(status.get("job_id", "")) / log_name) if find_repro_job(status.get("job_id", "")) else "")
        if verdict == "reproduced":
            reproduced.append(mode)
        elif verdict == "not_reproduced":
            not_reproduced.append(mode)
        elif verdict == "timeout":
            timed_out.append(mode)
        elif verdict == "needs_review":
            needs_review.append(mode)
    parts = []
    if reproduced:
        parts.append(f"{', '.join(reproduced)} 在当前环境中复现到崩溃或断言类异常。")
    if not_reproduced:
        parts.append(f"{', '.join(not_reproduced)} 返回码为 0，当前环境未复现该异常，可能是版本差异或该后端未触发。")
    if timed_out:
        parts.append(f"{', '.join(timed_out)} 超时，需要人工确认。")
    if needs_review:
        parts.append(f"{', '.join(needs_review)} 返回异常但未命中内置判定关键词，需要人工查看日志。")
    return " ".join(parts) if parts else "复现状态无法从当前输出自动判断，请人工查看日志。"


def generate_repro_report(job_id: str) -> tuple[int, dict]:
    out = find_repro_job(job_id)
    if out is None:
        return 404, {"error": "repro job not found"}
    status = read_json(out / "status.json", {})
    bug_id = status.get("bug_id", "")
    detail_code, detail = paper_bug_detail(bug_id)
    if detail_code != 200:
        return detail_code, detail
    meta = detail["meta"]
    lines = [
        f"# Reproduction Report: {display_bug_id(bug_id)}",
        "",
        "## Bug",
        "",
        f"- Title: {meta.get('title', '')}",
        f"- Framework: `{meta.get('framework', '')}`",
        f"- API: `{meta.get('api', '')}`",
        f"- Type: `{meta.get('bug_type', '')}`",
        f"- Severity: `{meta.get('severity', '')}`",
        "",
        "## Current Environment",
        "",
        f"- Python executable: `{sys.executable}`",
        f"- Python version: `{platform.python_version()}`",
        f"- Platform: `{platform.platform()}`",
        f"- Working directory: `{rel(REPO_ROOT)}`",
        f"- Repro job: `{rel(out)}`",
        "",
        "## Expected Behavior",
        "",
        meta.get("expected", ""),
        "",
        "## Confirmed Observed Behavior",
        "",
        meta.get("observed", ""),
        "",
        "## Current Reproduction Conclusion",
        "",
        repro_conclusion(status),
        "",
        "## Reproduction Code",
        "",
        "```python",
        detail.get("repro_code", "").rstrip(),
        "```",
        "",
        "## Current Run Output",
        "",
    ]
    for mode in ("cpu", "gpu0"):
        lines.append(summarize_mode(status, mode, out))
    report = "\n".join(lines).rstrip() + "\n"
    report_path = out / "report.md"
    report_path.write_text(report, encoding="utf-8")
    status["report"] = rel(report_path)
    status["updated_at"] = now()
    write_json(out / "status.json", status)
    return 200, {"job_id": job_id, "report_path": rel(report_path), "report_markdown": report}


class Handler(BaseHTTPRequestHandler):
    server_version = "TensorGuardDemo/0.2"

    def log_message(self, fmt: str, *args: Any) -> None:
        return

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/":
            self.serve_static("index.html")
            return
        if path.startswith("/static/"):
            self.serve_static(path[len("/static/") :])
            return
        if path == "/api/overview":
            send_json(self, overview_payload())
            return
        if path == "/api/apis":
            self.api_apis(query)
            return
        if path == "/api/api-detail":
            self.api_api_detail(query)
            return
        if path.startswith("/api/api-jobs/"):
            status, payload = api_job_payload(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        if path in ("/api/confirmed-bugs", "/api/paper-bugs"):
            send_json(self, load_paper_bugs())
            return
        if path.startswith("/api/confirmed-bugs/") or path.startswith("/api/paper-bugs/"):
            status, payload = paper_bug_detail(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/repro-jobs/") and path.endswith("/report"):
            job_id = unquote(path.split("/")[-2])
            status, payload = generate_repro_report(job_id)
            send_json(self, payload, status=status)
            return
        if path.startswith("/api/repro-jobs/"):
            status, payload = repro_job_payload(unquote(path.rsplit("/", 1)[-1]))
            send_json(self, payload, status=status)
            return
        send_json(self, {"error": "not found"}, status=404)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        ok, payload = read_body(self)
        if not ok:
            send_json(self, payload, status=400)
            return
        if parsed.path == "/api/run-api":
            status, response = start_api_job(payload)
            send_json(self, response, status=status)
            return
        if (parsed.path.startswith("/api/confirmed-bugs/") or parsed.path.startswith("/api/paper-bugs/")) and parsed.path.endswith("/reproduce"):
            bug_id = unquote(parsed.path.split("/")[-2])
            status, response = start_repro_job(bug_id, payload)
            send_json(self, response, status=status)
            return
        if parsed.path.startswith("/api/repro-jobs/") and parsed.path.endswith("/report"):
            job_id = unquote(parsed.path.split("/")[-2])
            status, response = generate_repro_report(job_id)
            send_json(self, response, status=status)
            return
        send_json(self, {"error": "not found"}, status=404)

    def serve_static(self, name: str) -> None:
        clean = Path(name)
        if clean.is_absolute() or ".." in clean.parts:
            send_json(self, {"error": "invalid static path"}, status=400)
            return
        path = STATIC_ROOT / clean
        if not path.is_file():
            send_json(self, {"error": "static file not found"}, status=404)
            return
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        write_response(self, 200, path.read_bytes(), content_type)

    def api_apis(self, query: dict) -> None:
        lib = query.get("lib", ["torch"])[0]
        q = query.get("q", [""])[0]
        limit_raw = query.get("limit", ["200"])[0]
        try:
            limit = max(1, min(int(limit_raw), 1000))
        except ValueError:
            limit = 200
        if lib not in ("torch", "tf"):
            send_json(self, {"error": "lib must be torch or tf"}, status=400)
            return
        send_json(self, api_list_payload(lib, q, limit=limit))

    def api_api_detail(self, query: dict) -> None:
        lib = query.get("lib", ["torch"])[0]
        api = query.get("api", [""])[0]
        status, payload = api_detail_payload(lib, api)
        send_json(self, payload, status=status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve the TensorGuard demo workbench.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8008)
    args = parser.parse_args()

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"TensorGuard Demo: http://{args.host}:{args.port}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
