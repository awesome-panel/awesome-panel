# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import pytest
import panel as pn

from awesome_panel.templates import MaterialTemplate
from awesome_panel.templates.application_template import ApplicationTemplate
from awesome_panel.templates.material.material_template import HTML_PATH, CSS_PATH

from awesome_panel.components import PageComponent

from awesome_panel.models import (
    Application,
    MenuItem,
    SocialLink,
    SourceLink,
    Theme,
)


@pytest.fixture
def template():
    return MaterialTemplate


@pytest.fixture
def templates(template):
    return [template]


@pytest.fixture
def theme():
    return Theme(name="Dark")


@pytest.fixture
def themes(theme):
    return [theme]


@pytest.fixture
def title():
    return "Awesome Panel"


@pytest.fixture
def logo():
    return "https://panel.holoviz.org/_static/logo_horizontal.png"


@pytest.fixture
def url():
    return "https://awesome-panel.org"


@pytest.fixture
def home_page():
    return pn.pane.Markdown(name="Home")


@pytest.fixture
def gallery_page():
    return pn.Column(pn.pane.Markdown("Page 1"), pn.pane.Markdown("Page 2"))

@pytest.fixture
def page():
    return pn.pane.Markdown("Page")

@pytest.fixture
def home_page_component(home_page):
    return PageComponent(name="Home", page=home_page)


@pytest.fixture
def gallery_page_component(gallery_page):
    return PageComponent(name="Gallery", page=gallery_page)


@pytest.fixture
def page_component(page):
    return PageComponent(name="Page", page=page)

@pytest.fixture
def page_components(home_page_component, gallery_page_component, page_component):
    return [home_page_component, gallery_page_component, page_component]

@pytest.fixture
def pages(page, home_page, gallery_page):
    return [home_page, gallery_page, page]


@pytest.fixture
def menu_item():
    return MenuItem(name="Item 1")


@pytest.fixture
def menu_items(menu_item):
    return [menu_item]


@pytest.fixture
def source_link():
    return SourceLink(name="GitHub")


@pytest.fixture
def source_links(source_link):
    return [source_link]


@pytest.fixture
def social_link():
    return SocialLink(name="Twitter")


@pytest.fixture
def social_links(social_link):
    return [social_link]


@pytest.fixture
def application(
    title, logo, url, templates, themes, page_components, menu_items, source_links, social_links
):
    return Application(
        title=title,
        logo=logo,
        url=url,
        templates=templates,
        themes=themes,
        pages=page_components,
        menu_items=menu_items,
        source_links=source_links,
        social_links=social_links,
    )


@pytest.fixture
def application_template(application):
    return ApplicationTemplate(
        application=application, template_path=HTML_PATH, css_path=CSS_PATH
    )
