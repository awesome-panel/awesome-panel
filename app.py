# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import pytest
import panel as pn

from awesome_panel.templates import MaterialTemplate
from awesome_panel.templates import ApplicationTemplateBuilder
from src.pages import home, about, issues, resources
import param
from awesome_panel.components import PageComponent as Page, ChangePageComponent
from awesome_panel.models import (
    MenuItem,
    SocialLink,
    SourceLink,
    Theme,
)
from src.pages.gallery import Gallery
from src.pages.gallery.kickstarter_dashboard.main import KickstarterDashboard

TITLE = "AWESOME PANEL"
LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
URL = "https://awesome-panel.org"
PAGES = [
    Page(name="Change Page", page=ChangePageComponent),
    Page(name="Home", page=home),
    Page(name="Gallery", page=pn.Column("# Gallery", pn.pane.Markdown("## App 1"), name="Gallery")),
    Page(name="About", page = about),
    Page(name="Issues", page = issues),
    Page(name="Resources", page = resources),
    # Page(name="Gallery", page = Gallery),
    Page(name="Kickstarter Dashboard", page = KickstarterDashboard)
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
