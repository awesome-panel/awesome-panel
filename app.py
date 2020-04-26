# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import pytest
import panel as pn

from awesome_panel.templates import MaterialTemplate
from awesome_panel.templates import ApplicationTemplateBuilder
from src.pages import home
import param
from awesome_panel.components import PageComponent as Page
from awesome_panel.models import (
    MenuItem,
    SocialLink,
    SourceLink,
    Theme,
)

TITLE = "AWESOME PANEL"
LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
URL = "https://awesome-panel.org"
PAGES = [
    Page(name="Home", page=home),
    Page(name="Gallery", page=pn.Column("# Gallery", pn.pane.Markdown("## App 1"), name="Gallery")),
]
MENU_ITEMS = [MenuItem(name="Item 1")]
SOURCE_LINKS = [SourceLink(name="GitHub")]
SOCIAL_LINKS = [SocialLink(name="Twitter")]

def view():
    return  ApplicationTemplateBuilder(
        title=TITLE,
        logo=LOGO,
        url=URL,
        pages=PAGES,
        template=MaterialTemplate,
        menu_items=MENU_ITEMS,
        source_links=SOURCE_LINKS,
        social_links=SOCIAL_LINKS,
    ).create()

pn.config.sizing_mode="stretch_width"
if __name__.startswith("__main__"):
    view().show()
if __name__.startswith("bokeh"):
    view().servable()
