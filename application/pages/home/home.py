"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from panel.pane import Markdown

from awesome_panel_extensions.site import site

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
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/home.png",
    resources={
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/home/home.py",
        "gif": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/home.gif",
        "mp4": "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel-assets/master/awesome-panel/applications/home.mp4",

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
