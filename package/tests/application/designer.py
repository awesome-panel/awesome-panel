# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn

from awesome_panel.application.components.gallery_component import GalleryComponent
from awesome_panel.application.components.gallery_page_component import GalleryPageComponent
from awesome_panel.application.models import Author, Page, Tag
from awesome_panel.designer import Designer, ReloadService


def test_show():
    source = "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/app.py"
    thumbnail = (
        "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/"
        "assets/images/thumbnails/awesome-panel-org.png"
    )
    author = Author(
        name="panel",
        url="https://panel.pyviz.org/",
        github_url="https://github.com/holoviz/",
        github_avatar_url="https://avatars2.githubusercontent.com/u/51678735",
    )
    home_page_main = pn.pane.Markdown(name="Home")
    tags = [Tag(name="awesome")]
    home_page = Page(
        name="Home",
        author=author,
        description="The main page of the application",
        tags=tags,
        source_code_url=source,
        thumbnail_png_url=thumbnail,
        component=home_page_main,
    )

    reload_services = [
        ReloadService(component=GalleryPageComponent, component_parameters={"page": home_page}),
        ReloadService(
            component=GalleryComponent,
            component_parameters={"pages": [home_page for i in range(0, 6)]},
        ),
    ]

    Designer(reload_services=reload_services).view.show()


if __name__.startswith("__main__"):
    test_show()
