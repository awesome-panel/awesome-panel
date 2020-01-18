"""## The Issues Page of awesome-panel.org"""
import pathlib

from panel import Column

from awesome_panel.express.pane.panes import Markdown

ISSUES_PATH = pathlib.Path(__file__).parent / "issues.md"


def view() -> Column:
    """The issues view of awesome-panel.org"""
    return Column(Markdown(path=ISSUES_PATH), sizing_mode="stretch_both", name="Issues",)
