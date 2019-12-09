"""## The Resources Page of awesome-panel.org"""
import pathlib

from panel import Column

from awesome_panel.express._pane._panes import Markdown

RESOURCES_PATH = pathlib.Path(__file__).parent / "resources.md"


def view() -> Column:
    """The resources view of awesome-panel.org"""
    return Column(Markdown(path=RESOURCES_PATH), sizing_mode="stretch_width", name="Resources")
