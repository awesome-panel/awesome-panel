"""## The About Page of awesome-panel.org"""
import pathlib

from panel import Column

from awesome_panel.express._pane._panes import Markdown

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"


def view() -> Column:
    """The about view of awesome-panel.org"""
    return Column(Markdown(path=ABOUT_PATH), sizing_mode="stretch_width", name="About")
