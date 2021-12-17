"""## The Issues Page of awesome-panel.org"""
import pathlib

from panel import Column
from panel.pane import Markdown

ISSUES_PATH = pathlib.Path(__file__).parent / "issues.md"


def view() -> Column:
    """The issues view of awesome-panel.org"""
    return Column(
        Markdown(ISSUES_PATH.read_text(encoding="utf8")),
        sizing_mode="stretch_both",
        name="Issues",
    )
