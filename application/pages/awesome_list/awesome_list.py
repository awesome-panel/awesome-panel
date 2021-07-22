"""The Panel Awesome List as a Gallery"""
import pathlib

from awesome_panel_extensions.site import site
from awesome_panel_extensions.site.gallery import GalleryTemplate
from awesome_panel_extensions.site.models import Application

APPLICATION = site.create_application(
    url="awesome-list",
    name="Awesome List",
    author="Marc Skov Madsen",
    description="The Awesome Panel list",
    description_long=__doc__,
    thumbnail="awesome-list.png",
    resources={
        "code": "awesome_list/awesome_list.py",
    },
    tags=[
        "Gallery",
    ],
)

AWESOME_FILE = pathlib.Path(__file__).parent / "awesome_list.yml"
RESOURCES = Application.read(AWESOME_FILE)


@site.add(APPLICATION)
def view():
    "Returns the Gallery Template"
    return GalleryTemplate(
        site="Awesome Panel",
        title="Awesome List",
        description="Awesome and Inspirational Resources",
        applications=RESOURCES,
    ).servable()


if __name__.startswith("bokeh"):
    view().servable()
