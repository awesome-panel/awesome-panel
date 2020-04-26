# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import pytest
import panel as pn

from awesome_panel.templates import MaterialTemplate
from awesome_panel.templates.application_template import ApplicationTemplate
from awesome_panel.templates.material.material import HTML_PATH, CSS_PATH

from awesome_panel.components import ApplicationComponent, PageComponent

from awesome_panel.models import (
    Application,
    MenuItem,
    Page,
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
    return Page(name="Home")


@pytest.fixture
def gallery_page():
    return Page(name="Gallery")


@pytest.fixture
def page(home_page):
    return home_page


@pytest.fixture
def home_page_component(home_page):
    return PageComponent(model=home_page)


@pytest.fixture
def gallery_page_component(gallery_page):
    return PageComponent(model=gallery_page)


@pytest.fixture
def page_component(page):
    return PageComponent(model=page)


@pytest.fixture
def page_components(home_page_component, gallery_page_component):
    return [home_page_component, gallery_page_component]


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
def application_component(application):
    return ApplicationComponent(model=application)


@pytest.fixture
def application_template(application_component):
    return ApplicationTemplate(
        application=application_component, template_path=HTML_PATH, css_path=CSS_PATH
    )
