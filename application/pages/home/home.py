"""## The Home Page of awesome-panel.org"""
import pathlib

from panel.pane import Markdown
from application.template import get_template

HOME_PATH = pathlib.Path(__file__).parent / "home.md"
HOME = HOME_PATH.read_text()

def view():
    """The home view of awesome-panel.org"""
    main = [Markdown(HOME, sizing_mode="stretch_width")]
    template=get_template(title="", main=main)
    return template


if __name__.startswith("bokeh"):
    view().servable()
