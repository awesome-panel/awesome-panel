"""## The Home Page of awesome-panel.org"""
import pathlib

from panel import Column
from panel.pane import Markdown

HOME_PATH = pathlib.Path(__file__).parent / "home.md"


def view() -> Column:
    """The home view of awesome-panel.org"""
    return Column(
        Markdown(HOME_PATH.read_text()),
        name="Home",
        sizing_mode="stretch_width",
    )


if __name__.startswith("bokeh"):
    view().servable()
