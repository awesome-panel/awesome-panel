# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import pytest
import panel as pn

from awesome_panel.components import ApplicationComponent, PageComponent
from awesome_panel.models import Application, Page
from awesome_panel.templates import MaterialTemplate

from awesome_panel.models import (
    MenuItem,
    SocialLink,
    SourceLink,
    Theme,
)

TEMPLATES = [MaterialTemplate]
THEMES = [Theme(name="Dark")]
TITLE = "Awesome Panel"
LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
URL = "https://awesome-panel.org"
PAGES = [PageComponent(model=Page(name="Home"))]
MENU_ITEMS = [MenuItem(name="Item 1")]
SOURCE_LINKS = [SourceLink(name="GitHub")]
SOCIAL_LINKS = [SocialLink(name="Twitter")]
APPLICATION = Application(
            title=TITLE,
            logo=LOGO,
            url=URL,
            templates=TEMPLATES,
            themes=THEMES,
            pages=PAGES,
            menu_items=MENU_ITEMS,
            source_links=SOURCE_LINKS,
            social_links=SOCIAL_LINKS,
        )

def view():
    return ApplicationComponent(
        model=APPLICATION
    ).view()

pn.config.sizing_mode="stretch_width"
if __name__.startswith("__main__"):
    view().show()
if __name__.startswith("bokeh"):
    view().servable()
