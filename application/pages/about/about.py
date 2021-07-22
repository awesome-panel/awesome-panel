"""## The About Page of awesome-panel.org"""
import pathlib

import panel as pn
from awesome_panel_extensions.site import site
from panel.pane import Markdown

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
ABOUT = ABOUT_PATH.read_text()

# pylint: disable=line-too-long
APPLICATION = site.create_application(
    url="about",
    name="About",
    author="Marc Skov Madsen",
    thumbnail="about.png",
    description="A short page about the why and who of awesome-panel.org",
    description_long=__doc__,
    resources={
        "code": "about/about.py",
    },
    tags=[
        "Code",
        "App In Gallery",
    ],
)
# pylint: enable=line-too-long


@site.add(APPLICATION)
def view():
    """The about view of awesome-panel.org"""
    main = [Markdown(ABOUT, sizing_mode="stretch_width")]
    template = pn.template.FastListTemplate(
        site="Awesome Panel", title="About", main=main, main_max_width="900px"
    )
    return template


if __name__.startswith("bokeh"):
    view().servable()
