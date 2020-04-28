# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import panel as pn
import pytest

from awesome_panel.components import ChangePageComponent, PageComponent
from awesome_panel.models import (
    Application,
    Author,
    MenuItem,
    Page,
    Resource,
    SocialLink,
    SourceLink,
    Tag,
    Theme,
)
from awesome_panel.templates import MaterialTemplate
from awesome_panel.templates.application_template import ApplicationTemplate
from awesome_panel.templates.material.material_template import CSS_PATH, HTML_PATH


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
    return ApplicationTemplate(application=application, template_path=HTML_PATH, css_path=CSS_PATH)


@pytest.fixture
def change_page_component(page_component):
    return ChangePageComponent(page_component=page_component)


@pytest.fixture
def tag():
    return Tag(name="Panel")


@pytest.fixture
def tags(tag):
    return [tag]


@pytest.fixture
def author():
    return Author(
        name="panel",
        url="https://panel.pyviz.org/",
        github_url="https://github.com/holoviz/",
        github_avatar_url="https://avatars2.githubusercontent.com/u/51678735",
    )


@pytest.fixture
def authors(author):
    return [author]


@pytest.fixture
def resource(tags, author):
    return Resource(
            name="Panel",
            url="https://panel.pyviz.org/",
            thumbnail_png_path="",
            is_awesome=True,
            tags=tags,
            author=author,
        )
