"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from panel.pane import Markdown
from panel.template.base import Template

from application.config import site

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"
SECTIONS = SECTIONS_PATH.read_text()

# S = """
# <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />
# <style>
# h1 { font-family: "Open Sans"; font-size: 24px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px; }
# h2 { font-family: "Open Sans"; font-size: 20px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 21.4px; }
# h3 { font-family: "Open Sans"; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15.4px; }
# p { font-family: "Open Sans"; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; } blockquote { font-family: "Open Sans"; font-size: 21px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 30px; } pre { font-family: "Open Sans"; font-size: 13px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 18.5714px; }</style>
# """

@site.register(
    url="",
    name="Awesome Panel",
    author="Marc Skov Madsen",
    description="The Home Page provides an introduction to Panel and awesome-panel.org.",
    thumbnail_url="home.png",
    documentation_url="",
    code_url="home/home.py",
    gif_url="home.gif",
    mp4_url="home.mp4",
)
def view():
    """The home view of awesome-panel.org"""
    pn.config.sizing_mode = "stretch_width"
    main = [Markdown(SECTIONS)]
    template=site.get_template(main=main, main_max_width="900px")
    return template
    # return site.get_template(main=main, main_max_width="900px")

if __name__.startswith("bokeh"):
    view().servable()
if __name__ == "__main__":
    view().show(port=5007, open=False)
