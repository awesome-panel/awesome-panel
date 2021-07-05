"""The awesome panel resources list provides a list of awesome resources for Panel"""
import pathlib

import panel as pn
from panel.pane import Markdown

from awesome_panel_extensions.site import site

RESOURCES_PATH = pathlib.Path(__file__).parent / "resources.md"
RESOURCES = RESOURCES_PATH.read_text()
APPLICATION = site.create_application(
    url="awesome-list",
    name="Awesome List",
    author="Marc Skov Madsen",
    description="""A list of Awesome Panel Resources created by the community""",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/resources.png",

    code="https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/resources/resources.py",

    mp4="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/",
    tags=[
        "Code",
        "App In Gallery",
    ],
)


@site.add(APPLICATION)
def view():
    """The resources view of awesome-panel.org"""
    main = [Markdown(RESOURCES, sizing_mode="stretch_width")]
    template = pn.template.FastListTemplate(main=main)
    return template


if __name__.startswith("bokeh"):
    view().servable()
