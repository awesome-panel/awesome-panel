"""## The Resources Page of awesome-panel.org"""
import pathlib

from panel import Column
from panel.pane import Markdown

RESOURCES_PATH = pathlib.Path(__file__).parent / "resources.md"


def view() -> Column:
    """The resources view of awesome-panel.org"""
    return Column(
        Markdown(RESOURCES_PATH.read_text()), sizing_mode="stretch_width", name="Resources",
    )
