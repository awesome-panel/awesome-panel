"""## The Resources Page of awesome-panel.org"""
import pathlib

from panel.pane import Markdown

from application.config import site

RESOURCES_PATH = pathlib.Path(__file__).parent / "resources.md"
RESOURCES = RESOURCES_PATH.read_text()


def view():
    """The resources view of awesome-panel.org"""
    main = [Markdown(RESOURCES, sizing_mode="stretch_width")]
    template = site.get_template(title="Resources", main=main)
    return template


if __name__.startswith("bokeh"):
    view().servable()
