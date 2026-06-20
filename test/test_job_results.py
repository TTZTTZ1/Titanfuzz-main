import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.server import list_job_result_files  # noqa: E402


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


if __name__ == "__main__":
    test_job_result_files_are_scoped_to_selected_api()
    print("ok")
