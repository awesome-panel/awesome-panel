"""## The About Page of awesome-panel.org"""
import pathlib

from panel.pane import Markdown

from application.config import site

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
ABOUT = ABOUT_PATH.read_text()


def view():
    """The about view of awesome-panel.org"""
    main = [Markdown(ABOUT, sizing_mode="stretch_width")]
    template = site.get_template(title="About", main=main)
    return template


if __name__.startswith("bokeh"):
    view().servable()
