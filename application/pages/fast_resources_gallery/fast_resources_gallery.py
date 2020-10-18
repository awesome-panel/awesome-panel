"""The Awesome Panel Gallery based on the Fast Components"""
# pylint: disable=line-too-long
from awesome_panel_extensions.frameworks.fast.templates.fast_gallery_template import (
    FastGalleryTemplate,
)
from application.pages.fast_resources_gallery.resources import RESOURCES

ASSETS = (
    "https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications/"
)


def get_resources():
    """Returns a list of all Resources"""
    return sorted(RESOURCES)

def get_fast_gallery():
    """Return a FastGalleryTemplate"""
    return FastGalleryTemplate(
        site_name="Awesome Panel",
        site_url="https://awesome-panel.org",
        name="Resources",
        url="https://awesome-panel.org/resources",
        description="""The purpose of the Awesome Panel Resources is to inspire and help you create awesome analytics apps in <fast-anchor href="https://panel.holoviz.org" target="_blank" appearance="hypertext">Panel</fast-anchor> using the tools you know and love.""",
        background_image_url="https://ih1.redbubble.net/image.875683605.8623/ur,mug_lifestyle,tall_portrait,750x1000.jpg",
        items=get_resources(),
        target="_blank",
    )


if __name__.startswith("bokeh"):
    get_fast_gallery().servable()
