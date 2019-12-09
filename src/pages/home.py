"""## The Home Page of awesome-panel.org"""
from panel import Column
from awesome_panel.app import title_awesome
from awesome_panel.express._pane._panes import Markdown
import pathlib

HOME_PATH = pathlib.Path(__file__).parent / "home.md"


def view() -> Column:
    """The home view of awesome-panel.org"""
    return Column(Markdown(path=HOME_PATH), sizing_mode="stretch_width", name="Home")

