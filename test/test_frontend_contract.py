from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "webapp" / "static" / "index.html"
APP_JS = ROOT / "webapp" / "static" / "app.js"


def test_frontend_has_no_hardcoded_gpu_or_environment_examples():
    source = APP_JS.read_text(encoding="utf-8") + INDEX.read_text(encoding="utf-8")
    for forbidden in ("NVIDIA A800", "NVIDIA L40", "PyTorch 2.11.0", "CUDA 13.0", "GPU0"):
        assert forbidden not in source, forbidden


def test_frontend_has_three_primary_views():
    html = INDEX.read_text(encoding="utf-8")
    assert 'id="overview"' in html
    assert 'id="apiRun"' in html
    assert 'id="bugReplay"' in html


def test_overview_uses_live_environment_surface():
    html = INDEX.read_text(encoding="utf-8")
    js = APP_JS.read_text(encoding="utf-8")
    assert 'id="environmentDrawer"' in html
    assert 'id="environmentContent"' in html
    assert '"/api/environment"' in js


if __name__ == "__main__":
    test_frontend_has_no_hardcoded_gpu_or_environment_examples()
    test_frontend_has_three_primary_views()
    test_overview_uses_live_environment_surface()
    print("ok")
