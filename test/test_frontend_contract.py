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


def test_single_api_workspace_contains_stage_tabs_and_live_surfaces():
    html = INDEX.read_text(encoding="utf-8")
    for expected in ("apiStageTabs", "apiStageChart", "apiResultComposition", "gpuMonitor", "candidateResults"):
        assert f'id="{expected}"' in html, expected


def test_frontend_loads_dependency_free_chart_module():
    html = INDEX.read_text(encoding="utf-8")
    assert '/static/charts.js' in html


if __name__ == "__main__":
    test_frontend_has_no_hardcoded_gpu_or_environment_examples()
    test_frontend_has_three_primary_views()
    test_overview_uses_live_environment_surface()
    test_single_api_workspace_contains_stage_tabs_and_live_surfaces()
    test_frontend_loads_dependency_free_chart_module()
    print("ok")
