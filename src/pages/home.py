"""## The Home Page of awesome-panel.org"""
import pathlib

from panel import Column

from awesome_panel.express._pane._panes import Markdown

HOME_PATH = pathlib.Path(__file__).parent / "home.md"


def view() -> Column:
    """The home view of awesome-panel.org"""
    return Column(Markdown(path=HOME_PATH), sizing_mode="stretch_both", name="Home",)
