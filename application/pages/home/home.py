"""## The Home Page of awesome-panel.org"""
import pathlib

import panel as pn
from panel.pane import Markdown, Alert
from application.template import get_template

HEADER = """<h1>Awesome Panel
<img alt="Awesome Badge"
src="https://cdn.rawgit.com/sindresorhus/awesome/\
d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg">
</h1>"""
NEWS_PATH = pathlib.Path(__file__).parent / "news.md"

SECTIONS_PATH = pathlib.Path(__file__).parent / "home.md"
SECTIONS = SECTIONS_PATH.read_text()


def view():
    """The home view of awesome-panel.org"""
    NEWS = NEWS_PATH.read_text()

    pn.config.sizing_mode = "stretch_width"
    # header = Markdown(HEADER)
    # news = Alert(NEWS, alert_type="info")
    sections = Markdown(SECTIONS)

    main = [
        # header,
        # news,
        sections,
    ]
    template = get_template(title="", main=main)
    return template


if __name__.startswith("bokeh"):
    view().servable()
