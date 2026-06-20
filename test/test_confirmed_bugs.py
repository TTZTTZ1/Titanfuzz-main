import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from webapp.confirmed_bugs import load_confirmed_records  # noqa: E402


def test_confirmed_index_excludes_entries_without_repro_source():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        good = root / "good"
        bad = root / "bad"
        good.mkdir()
        bad.mkdir()
        (good / "repro.py").write_text("print('ok')", encoding="utf-8")
        (good / "meta.json").write_text(json.dumps({"id": "BUG-1", "files": {"repro": "repro.py"}}), encoding="utf-8")
        (bad / "meta.json").write_text(json.dumps({"id": "BUG-2", "files": {"repro": "missing.py"}}), encoding="utf-8")
        index = root / "index.json"
        index.write_text(json.dumps([
            {"id": "BUG-1", "path": "good/meta.json", "severity": "High"},
            {"id": "BUG-2", "path": "bad/meta.json", "severity": "High"},
        ]), encoding="utf-8")

        records = load_confirmed_records(index, root)

        assert [record["id"] for record in records] == ["BUG-1"]
        assert "severity" not in records[0]


if __name__ == "__main__":
    test_confirmed_index_excludes_entries_without_repro_source()
    print("ok")
