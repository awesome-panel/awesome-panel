"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from panel.pane import Markdown

from application.config import site

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"
def read_sections():
    sections = SECTIONS_PATH.read_text()
    sections = sections.split("##")
    sections[0]=Markdown(sections[0])
    for index in range(1,len(sections)):
        sections[index]=Markdown("#"+sections[index])
    return sections
SECTIONS = read_sections()
APPLICATION = site.create_application(
    url="/",
    name="Awesome Panel",
    author="Marc Skov Madsen",
    introduction="An introduction to awesome-panel.org and Panel",
    description="An introduction to awesome-panel.org and Panel",
    thumbnail_url="home.png",
    documentation_url="",
    code_url="home/home.py",
    gif_url="home.gif",
    mp4_url="home.mp4",
)


@site.add(APPLICATION)
def view():
    """The home view of awesome-panel.org"""
    pn.config.sizing_mode = "stretch_width"
    SECTIONS = read_sections()
    template = site.create_template(main=SECTIONS, main_max_width="900px")
    return template


if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    breakpoint()
    view().show(port=5007, open=False)
