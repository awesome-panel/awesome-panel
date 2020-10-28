"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from panel.pane import Markdown

from application.template import get_template

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"
SECTIONS = SECTIONS_PATH.read_text()


def view():
    """The home view of awesome-panel.org"""
    pn.config.sizing_mode = "stretch_width"
    sections = Markdown(SECTIONS)

    main = [
        sections,
    ]
    template = get_template(title="", main=main, main_max_width="900px")
    return template


if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    view().show()
