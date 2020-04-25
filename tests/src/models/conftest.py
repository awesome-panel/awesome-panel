# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import pytest
import panel as pn

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
    return pn.Template()


@pytest.fixture
def templates(template):
    return [template]


@pytest.fixture
def theme():
    return Theme()


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
def page():
    return Page()


@pytest.fixture
def pages(page):
    return [page]


@pytest.fixture
def menu_item():
    return MenuItem()


@pytest.fixture
def menu_items(menu_item):
    return [menu_item]


@pytest.fixture
def source_link():
    return SourceLink()


@pytest.fixture
def source_links(source_link):
    return [source_link]


@pytest.fixture
def social_link():
    return SocialLink

@pytest.fixture
def social_links(social_link):
    return [social_link]

@pytest.fixture
def application(templates, themes, pages, menu_items, source_links, social_links):
    return Application(
        templates=templates,
        themes=themes,
        pages=pages,
        menu_items=menu_items,
        source_links=source_links,
        social_links=social_links,
    )
