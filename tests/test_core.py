import tempfile
from pathlib import Path

from devstudio5304_kit.core import Devstudio5304Tool


def test_plan_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        assert Devstudio5304Tool(tmp).plan() == []


def test_category_of_known_and_unknown():
    sorter = Devstudio5304Tool(".")
    assert sorter.category_of("a.png") == "images"
    assert sorter.category_of("a.unknown") == "other"


def test_apply_moves_files():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "note.md").write_text("hi", encoding="utf-8")
        moved = Devstudio5304Tool(tmp).apply()
        assert moved == [("note.md", "docs")]
        assert Path(tmp, "docs", "note.md").is_file()
