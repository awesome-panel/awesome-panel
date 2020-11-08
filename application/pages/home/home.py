"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from panel.pane import Markdown

from application.config import site

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"
SECTIONS = SECTIONS_PATH.read_text()
APPLICATION = site.create_application(
    url="/",
    name="Awesome Panel",
    author="Marc Skov Madsen",
    introduction="An overview of awesome-panel.org and introduction to Panel.",
    description="The Home Page provides an introduction to Panel and awesome-panel.org.",
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
    main = [Markdown(SECTIONS)]
    template = site.create_template(main=main, main_max_width="900px")
    return template


if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    view().show(port=5007, open=False)
