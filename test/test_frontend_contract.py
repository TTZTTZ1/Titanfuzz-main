from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "webapp" / "static" / "index.html"
APP_JS = ROOT / "webapp" / "static" / "app.js"
STYLES = ROOT / "webapp" / "static" / "styles.css"


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
    for expected in ("apiStageTabs", "apiStageChart", "apiResultComposition", "gpuMonitor", "candidateResults", "apiDataCheck"):
        assert f'id="{expected}"' in html, expected


def test_frontend_loads_dependency_free_chart_module():
    html = INDEX.read_text(encoding="utf-8")
    assert '/static/charts.js' in html


def test_repro_workspace_has_explanation_evidence_and_report_regions():
    html = INDEX.read_text(encoding="utf-8")
    for expected in ("bugExplanation", "reproEvidence", "reproEnvironment", "reportPreview"):
        assert f'id="{expected}"' in html, expected
    assert "严重程度" not in html


def test_candidate_review_can_update_non_confirming_states():
    js = APP_JS.read_text(encoding="utf-8")
    assert "updateCandidateStatus" in js
    assert "/status" in js
    assert "rejected" in js


def test_frontend_uses_approved_blue_theme_tokens():
    css = STYLES.read_text(encoding="utf-8")
    for expected in (
        "--primary: #246bfd;",
        "--primary-soft: #eaf1ff;",
        "--shell: #131c2d;",
        "--canvas-start: #f8fbff;",
        "--canvas-mid: #edf4ff;",
        "--canvas-end: #f8f5ff;",
    ):
        assert expected in css, expected
    assert "background: linear-gradient(" in css
    assert "--teal:" not in css


def test_overview_keeps_dense_dashboard_structure():
    html = INDEX.read_text(encoding="utf-8")
    css = STYLES.read_text(encoding="utf-8")
    for expected in ("metric-strip", "overview-grid", "process-line", "evidence-surface"):
        assert expected in html, expected
    for expected in ("var(--shadow)", "backdrop-filter: blur", ".metric-strip", ".process-line"):
        assert expected in css, expected


def test_single_api_uses_blue_focus_and_stage_states():
    css = STYLES.read_text(encoding="utf-8")
    for expected in (
        "border-color: var(--primary)",
        ".stage-tab.active",
        "background: var(--primary);",
        ".match-item.active",
    ):
        assert expected in css, expected


def test_bug_workspace_preserves_evidence_hierarchy():
    html = INDEX.read_text(encoding="utf-8")
    css = STYLES.read_text(encoding="utf-8")
    for expected in ("repro-workspace", "behavior-compare", "code-evidence-surface", "report-surface"):
        assert expected in html, expected
    for expected in (
        ".behavior-panel.observed",
        "border-left: 3px solid var(--red)",
        ".behavior-panel.expected",
        "border-left: 3px solid var(--primary)",
        "background: rgba(248, 251, 255, .88)",
    ):
        assert expected in css, expected


def test_blue_theme_keeps_responsive_and_print_boundaries():
    css = STYLES.read_text(encoding="utf-8")
    for expected in (
        "@media (max-width: 1060px)",
        "@media (max-width: 720px)",
        "@media print",
        "@media (prefers-reduced-motion: reduce)",
    ):
        assert expected in css, expected


if __name__ == "__main__":
    test_frontend_has_no_hardcoded_gpu_or_environment_examples()
    test_frontend_has_three_primary_views()
    test_overview_uses_live_environment_surface()
    test_single_api_workspace_contains_stage_tabs_and_live_surfaces()
    test_frontend_loads_dependency_free_chart_module()
    test_repro_workspace_has_explanation_evidence_and_report_regions()
    test_candidate_review_can_update_non_confirming_states()
    test_frontend_uses_approved_blue_theme_tokens()
    test_overview_keeps_dense_dashboard_structure()
    test_single_api_uses_blue_focus_and_stage_states()
    test_bug_workspace_preserves_evidence_hierarchy()
    test_blue_theme_keeps_responsive_and_print_boundaries()
    print("ok")
