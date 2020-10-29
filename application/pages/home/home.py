"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from panel.pane import Markdown

from application.template import get_template

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"
SECTIONS = SECTIONS_PATH.read_text()

# def _split_sections():
#     sections = []
#     section = None
#     for line in SECTIONS_PATH.read_text().splitlines():
#         if line.startswith("#"):
#             if section:
#                 sections.append(section)
#             section=line
#         else:
#             section+="\n"+line
#     return sections

# SECTIONS = _split_sections()


def view():
    """The home view of awesome-panel.org"""
    pn.config.sizing_mode = "stretch_width"
    # SECTIONS = _split_sections()
    sections = [Markdown(SECTIONS)]

    template = get_template(title="", main=sections, main_max_width="900px")
    return template


if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    view().show()
