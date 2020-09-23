"""## The About Page of awesome-panel.org"""
import pathlib

from panel import Column
from panel.pane import Markdown

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"


def view() -> Column:
    """The about view of awesome-panel.org"""
    return Column(
        Markdown(ABOUT_PATH.read_text()),
        sizing_mode="stretch_width",
        name="About",
    )
