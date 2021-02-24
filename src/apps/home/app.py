"""## The Landing Page of the site"""
import pathlib

import panel as pn
from panel.pane import Markdown

from src.shared.templates import ListTemplate

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"


def _read_sections():
    sections = SECTIONS_PATH.read_text()
    sections = sections.split("##")
    sections[0] = Markdown(sections[0])
    for index in range(1, len(sections)):
        sections[index] = Markdown("#" + sections[index])
    return sections


def view():
    """Returns the landing page of the site"""
    pn.config.sizing_mode = "stretch_width"
    sections = _read_sections()
    return ListTemplate(title="Home", main=sections, main_max_width="900px")


if __name__.startswith("bokeh"):
    # Run the development server
    # python -m panel serve 'src/apps/home/home.py' --dev --show
    view().servable()
if __name__ == "__main__":
    # Run the server. Useful for integrated debugging in your Editor or IDE.
    # python 'src/apps/home/home.py'
    view().show(port=5007)
