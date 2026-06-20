import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.server import initial_api_status, list_job_result_files, unique_job_directory  # noqa: E402


def test_job_result_files_are_scoped_to_selected_api():
    with tempfile.TemporaryDirectory() as tmp:
        job = Path(tmp)
        crash = job / "Results" / "torch" / "crash"
        crash.mkdir(parents=True)
        (crash / "torch.add_1.py").write_text("raise RuntimeError('boom')", encoding="utf-8")
        (crash / "torch.mean_1.py").write_text("pass", encoding="utf-8")

        files = list_job_result_files(job, "torch", "torch.add")

        assert len(files["crash"]) == 1
        assert files["crash"][0]["name"] == "torch.add_1.py"
        assert "boom" in files["crash"][0]["source_excerpt"]
        assert files["valid"] == []


def test_job_directory_never_reuses_existing_run():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "job").mkdir()
        job_id, path = unique_job_directory(root, "job")
        assert job_id == "job_2"
        assert path.is_dir()


def test_web_job_is_pending_before_child_process_starts():
    status = initial_api_status("job", "torch", "torch.add", "demo", "qwen", "incoder", "0")
    assert status["status"] == "pending"
    assert status["stages"]["prompt_check"] == "pending"
    assert status["mutation_model"] == "incoder"


if __name__ == "__main__":
    test_job_result_files_are_scoped_to_selected_api()
    test_job_directory_never_reuses_existing_run()
    test_web_job_is_pending_before_child_process_starts()
    print("ok")
