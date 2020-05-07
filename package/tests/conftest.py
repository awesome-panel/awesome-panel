# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import pytest

from awesome_panel.application.components import (ApplicationComponent,
                                                  LoadingPageComponent,
                                                  PageComponent,
                                                  PageNavigationComponent,
                                                  ProgressSpinnerComponent)
from awesome_panel.application.models import (
    Application, Author, MenuItem, Message, Page, Progress, Resource,
    SocialLink, SourceLink, Tag, Template, Theme)
from awesome_panel.application.services import (
    AuthorService, MessageService, NavigationService, PageService,
    ProgressService, Services, TagService, ThemeService)
from awesome_panel.application.templates import MaterialTemplate
from awesome_panel.application.templates.application_template import \
    ApplicationTemplate
from awesome_panel.application.templates.material.material_template import (
    CSS_PATH, HTML_PATH)
from awesome_panel.application.views import ApplicationView


@pytest.fixture
def template():
    return Template(name="Material")


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
def home_page_main():
    return pn.pane.Markdown(name="Home")


@pytest.fixture
def gallery_page_main():
    return pn.Column(pn.pane.Markdown("Page 1"), pn.pane.Markdown("Page 2"))


@pytest.fixture
def page_main():
    return pn.pane.Markdown("Page")


@pytest.fixture
def home_page(author, tags, home_page_main):
    source = "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/app.py"
    thumbnail = (
        "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/"
        "assets/images/thumbnails/awesome-panel-org.png"
    )
    return Page(
        name="Home",
        author=author,
        description="The main page of the application",
        tags=tags,
        source_code_url=source,
        thumbnail_png_url=thumbnail,
        component=home_page_main,
    )


@pytest.fixture
def gallery_page(author, tags, gallery_page_main):
    source = "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/app.py"
    thumbnail = (
        "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/"
        "assets/images/thumbnails/awesome-panel-org.png"
    )
    return Page(
        name="Gallery",
        author=author,
        description="A page showing off all the pages",
        tags=tags,
        source_code_url=source,
        thumbnail_png_url=thumbnail,
        component=gallery_page_main,
    )


@pytest.fixture
def page(author, tags):
    source = "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/app.py"
    thumbnail = (
        "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/"
        "assets/images/thumbnails/awesome-panel-org.png"
    )
    return Page(
        name="Page",
        author=author,
        description="Any Page",
        tags=tags,
        source_code_url=source,
        thumbnail_png_url=thumbnail,
        component="Page",
    )


@pytest.fixture
def home_page_component(home_page_main):
    return PageComponent(name="Home", main=home_page_main, sidebar="sidebar")


@pytest.fixture
def gallery_page_component(gallery_page_main):
    return PageComponent(name="Gallery", main=gallery_page_main, sidebar="sidebar")


@pytest.fixture
def page_component(page_main):
    return PageComponent(name="Page", main=page_main, sidebar="sidebar")


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
    title, logo, url, home_page, pages, template, templates
):  # pylint: disable=too-many-arguments
    return Application(
        title=title,
        logo=logo,
        url=url,
        default_page=home_page,
        pages=pages,
        default_template=template,
        templates=templates,
    )


@pytest.fixture
def application_template(application, services):
    return ApplicationTemplate(application=application, services=services, template_path=HTML_PATH, css_path=CSS_PATH)


@pytest.fixture
def loading_page_component(progress_service, theme_service):
    return LoadingPageComponent(progress_service=progress_service, theme_service=theme_service)


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


@pytest.fixture
def message():
    return Message()


@pytest.fixture
def progress():
    return Progress()


@pytest.fixture
def tag_service(tags):
    _tag_service = TagService(tags=tags)
    return TagService()


@pytest.fixture
def author_service(authors):
    return AuthorService(authors=authors)


@pytest.fixture
def page_service(page, pages):
    return PageService(page=page, pages=pages)


@pytest.fixture
def progress_service(progress):
    return ProgressService(progress=progress)


@pytest.fixture
def navigation_service(page):
    return NavigationService(page=page)


@pytest.fixture
def message_service(message):
    return MessageService(message=message)


@pytest.fixture
def theme_service(theme, themes):
    return ThemeService(theme=theme, themes=themes)


@pytest.fixture
def services(progress_service, page_service, message_service, theme_service):
    return Services(
        progress_service=progress_service,
        page_service=page_service,
        message_service=message_service,
        theme_service=theme_service,
    )


@pytest.fixture
def progress_spinner_component(progress_service, theme_service):
    return ProgressSpinnerComponent(progress_service=progress_service, theme_service=theme_service)

@pytest.fixture
def application_view():
    return ApplicationView()

@pytest.fixture
def page_navigation_component(page_service):
    return PageNavigationComponent(page_service=page_service)

@pytest.fixture
def application_component(application, services, application_view):
    return ApplicationComponent(application=application, services=services, view=application_view)