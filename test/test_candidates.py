import sys
import tempfile
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.candidates import CandidateStore, recommend_candidate  # noqa: E402
from webapp import server  # noqa: E402


def create_source(root: Path) -> Path:
    source = (
        root
        / "demo_runs"
        / "api_jobs"
        / "job1"
        / "Results"
        / "torch"
        / "crash"
        / "torch.add_1.py"
    )
    source.parent.mkdir(parents=True)
    source.write_text('"""INTERNAL ASSERT FAILED"""\nimport torch\n', encoding="utf-8")
    return source


def test_candidate_references_exact_job_source_and_deduplicates_hash():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = create_source(root)
        store = CandidateStore(root)
        first = store.add(
            job_id="job1",
            lib="torch",
            api="torch.add",
            category="crash",
            source_path=source,
        )
        second = store.add(
            job_id="job1",
            lib="torch",
            api="torch.add",
            category="crash",
            source_path=source,
        )
        assert first["id"] == second["id"]
        assert first["source_path"].endswith("torch.add_1.py")
        assert first["status"] == "pending_review"
        assert len(store.list()) == 1


def test_recommendation_excludes_notarget_and_plain_exception():
    assert recommend_candidate("crash", "") is True
    assert recommend_candidate("hangs", "") is True
    assert recommend_candidate("exception", "INTERNAL ASSERT FAILED") is True
    assert recommend_candidate("exception", "ValueError: invalid argument") is False
    assert recommend_candidate("notarget", "") is False


def test_server_creates_candidate_but_cannot_promote_it():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = create_source(root)
        store = CandidateStore(root)
        payload = {
            "job_id": "job1",
            "lib": "torch",
            "api": "torch.add",
            "category": "crash",
            "source_path": str(source),
        }
        with patch.object(server, "CANDIDATE_STORE", store):
            code, record = server.create_candidate(payload)
            assert code == 201
            code, response = server.update_candidate(record["id"], {"status": "promoted"})
            assert code == 400
            assert "unsupported" in response["error"]


if __name__ == "__main__":
    test_candidate_references_exact_job_source_and_deduplicates_hash()
    test_recommendation_excludes_notarget_and_plain_exception()
    test_server_creates_candidate_but_cannot_promote_it()
    print("ok")
