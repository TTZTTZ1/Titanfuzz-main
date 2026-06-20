import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts import run_one_api_demo as demo  # noqa: E402


def make_args(out: str = "demo_runs/job") -> SimpleNamespace:
    return SimpleNamespace(
        api="torch.add",
        lib="torch",
        mode="normal",
        dry_run=False,
        out=out,
        job_id="job",
        qwen_model="../Qwen2.5-Coder-7B-Instruct",
        dtype="bfloat16",
        mut_model="facebook/incoder-1B",
        constraints_dir="experiment/torch",
        qwen_n_samples=1,
        qwen_min_valid=1,
        qwen_max_rounds=1,
        qwen_per_api_budget=1,
        qwen_validate_timeout=1,
        ev_max_valid=1,
        ev_batch_size=1,
        ev_timeout=1,
        cuda_device="0",
        random_seed=420,
        seed_pool_size=10,
        force_redo=False,
    )


def test_normal_mode_uses_formal_single_api_budget():
    cfg = demo.mode_defaults("normal")
    assert cfg["ev_max_valid"] == 200
    assert cfg["ev_batch_size"] == 100
    assert cfg["ev_timeout"] == 1000


def test_status_records_actual_mutation_model():
    with tempfile.TemporaryDirectory() as tmp:
        run = demo.DemoRun(make_args(), Path(tmp))
        assert run.status["mutation_model"] == make_args().mut_model


def test_status_records_effective_run_parameters():
    with tempfile.TemporaryDirectory() as tmp:
        args = make_args()
        run = demo.DemoRun(args, Path(tmp))
        assert run.status["parameters"]["ev_max_valid"] == args.ev_max_valid
        assert run.status["parameters"]["seed_pool_size"] == args.seed_pool_size
        assert run.status["parameters"]["qwen_per_api_budget"] == args.qwen_per_api_budget


def test_failed_stage_marks_later_execution_stages_skipped():
    with tempfile.TemporaryDirectory() as tmp:
        run = demo.DemoRun(make_args(), Path(tmp))
        run.mark_remaining_skipped("qwen_seed")
        assert run.status["stages"]["ev_generation"] == "skipped"
        assert run.status["stages"]["driver"] == "skipped"
        assert run.status["stages"]["summary"] == "pending"


def test_publish_results_replaces_only_selected_api_files():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        run = demo.DemoRun(make_args(), root)

        job_valid = run.results_root / "valid"
        job_seed = run.results_root / "seed"
        job_valid.mkdir(parents=True)
        job_seed.mkdir(parents=True)
        (job_valid / "torch.add_1.py").write_text("new valid", encoding="utf-8")
        (job_seed / "torch.add_seed1.py").write_text("new seed", encoding="utf-8")

        canonical_valid = root / "Results" / "torch" / "valid"
        canonical_seed = root / "Results" / "torch" / "seed"
        canonical_valid.mkdir(parents=True)
        canonical_seed.mkdir(parents=True)
        (canonical_valid / "torch.add_99.py").write_text("old valid", encoding="utf-8")
        (canonical_valid / "torch.mean_1.py").write_text("keep", encoding="utf-8")
        (canonical_seed / "torch.add_seed9.py").write_text("old seed", encoding="utf-8")

        run.publish_results_to_canonical()

        assert not (canonical_valid / "torch.add_99.py").exists()
        assert not (canonical_seed / "torch.add_seed9.py").exists()
        assert (canonical_valid / "torch.add_1.py").read_text(encoding="utf-8") == "new valid"
        assert (canonical_seed / "torch.add_seed1.py").read_text(encoding="utf-8") == "new seed"
        assert (canonical_valid / "torch.mean_1.py").read_text(encoding="utf-8") == "keep"


if __name__ == "__main__":
    test_normal_mode_uses_formal_single_api_budget()
    test_status_records_actual_mutation_model()
    test_status_records_effective_run_parameters()
    test_failed_stage_marks_later_execution_stages_skipped()
    test_publish_results_replaces_only_selected_api_files()
    print("ok")
