from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "webapp" / "frontend"


def test_vue_frontend_has_build_contract():
    package = (FRONTEND / "package.json").read_text(encoding="utf-8")
    vite = (FRONTEND / "vite.config.ts").read_text(encoding="utf-8")

    assert '"build": "vue-tsc --noEmit && vite build"' in package
    assert 'outDir: "../static"' in vite
    assert 'base: command === "build" ? "/static/" : "/"' in vite


def test_python_static_root_is_unchanged():
    server = (ROOT / "webapp" / "server.py").read_text(encoding="utf-8")

    assert 'STATIC_ROOT = Path(__file__).resolve().parent / "static"' in server


if __name__ == "__main__":
    test_vue_frontend_has_build_contract()
    test_python_static_root_is_unchanged()
    print("frontend build contract: OK")
