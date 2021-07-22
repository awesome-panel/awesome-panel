"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from awesome_panel_extensions.site import site
from panel.pane import Markdown

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"


def _read_sections():
    sections = SECTIONS_PATH.read_text()
    sections = sections.split("##")
    sections[0] = Markdown(sections[0])
    for index in range(1, len(sections)):
        sections[index] = Markdown("#" + sections[index], sizing_mode="stretch_width")
    return sections


SECTIONS = _read_sections()
APPLICATION = site.create_application(
    url="/",
    name="Awesome Panel",
    author="Marc Skov Madsen",
    description="An introduction to awesome-panel.org and Panel",
    description_long="An introduction to awesome-panel.org and Panel",
    thumbnail="home.png",
    resources={
        "code": "home/home.py",
        "gif": "home.gif",
        "mp4": "home.mp4",
    },
)


@site.add(APPLICATION)
def view():
    """The home view of awesome-panel.org"""
    pn.config.sizing_mode = "stretch_width"
    template = pn.template.FastListTemplate(main=SECTIONS, title="Home", main_max_width="900px")
    return template


if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    view().show(port=5007, open=False)
