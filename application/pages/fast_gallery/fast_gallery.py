"""The Awesome Panel Gallery based on the Fast Components"""
# pylint: disable=line-too-long
import panel as pn
from awesome_panel_extensions.frameworks.fast.templates.fast_gallery_template import (
    FastGalleryTemplate,
)

from application.config import site
from application.pages.about.about import APPLICATION

APPLICATION = site.create_application(
    url="gallery",
    name="Gallery",
    author="Marc Skov Madsen",
    description="""The Gallery provides a very visual overview to the applications and associated
    resources""",
    thumbnail_url="gallery.png",
    documentation_url="",
    code_url="fast_gallery/fast_gallery.py",
    gif_url="",
    mp4_url="",
)


@site.add(APPLICATION)
def view():
    """Return a FastGalleryTemplate"""
    pn.config.raw_css = [
        css for css in pn.config.raw_css if not css.startswith("/* CUSTOM TEMPLATE CSS */")
    ]
    return FastGalleryTemplate(
        site_name="Awesome Panel",
        site_url="/",
        name="Gallery",
        url="",
        description="""The purpose of the Awesome Panel Gallery is to inspire and help you create awesome analytics apps in <fast-anchor href="https://panel.holoviz.org" target="_blank" appearance="hypertext">Panel</fast-anchor> using the tools you know and love.""",
        background_image_url="https://ih1.redbubble.net/image.875683605.8623/ur,mug_lifestyle,tall_portrait,750x1000.jpg",
        items=site.applications,
        target="_self",
    )


if __name__.startswith("bokeh"):
    view().servable()
