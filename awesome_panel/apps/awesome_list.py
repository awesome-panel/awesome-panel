"""The Panel Awesome List as a Gallery"""
from awesome_panel_extensions.site.gallery import GalleryTemplate

from awesome_panel import config

if __name__.startswith("bokeh"):
    config.extension(url="awesome_list", template=None)

    GalleryTemplate(
        site="Awesome Panel",
        title="Awesome List",
        description="Awesome and Inspirational Resources",
        applications=config.AWESOME_APPLICATIONS,
    ).servable()
