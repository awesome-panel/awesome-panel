"""## The About Page of awesome-panel.org"""
import pathlib

from application.template import get_template
from panel.pane import Markdown

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
ABOUT = ABOUT_PATH.read_text()

def view():
    """The about view of awesome-panel.org"""
    main = [Markdown(ABOUT, sizing_mode="stretch_width")]
    template=get_template(title="About", main=main)
    return template

if __name__.startswith("bokeh"):
    view().servable()
