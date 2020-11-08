"""## The About Page of awesome-panel.org"""
import pathlib

from panel.pane import Markdown

from application.config import site

ABOUT_PATH = pathlib.Path(__file__).parent / "about.md"
ABOUT = ABOUT_PATH.read_text()

APPLICATION = site.create_application(
    url="about",
    name="About",
    author="Marc Skov Madsen",
    introduction="A short page about the why and who of awesome-panel.org",
    description=__doc__,
    thumbnail_url="about.png",
    documentation_url="",
    code_url="about/about.py",
    gif_url="",
    mp4_url="",
    tags=[
        "Code",
        "App In Gallery",
    ],
)

@site.add(APPLICATION)
def view():
    """The about view of awesome-panel.org"""
    main = [Markdown(ABOUT, sizing_mode="stretch_width")]
    template = site.create_template(title="About", main=main)
    return template


if __name__.startswith("bokeh"):
    view().servable()
