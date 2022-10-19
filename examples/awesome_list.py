"""The Panel Awesome List as a Gallery"""
from awesome_panel_extensions.site.gallery import GalleryTemplate

from awesome_panel import config

if __name__.startswith("bokeh"):
    config.extension(url="awesome_list", template=None)

    GalleryTemplate(
        site="Awesome Panel",
        site_url="./",
        title="Community Gallery",
        description="Awesome Panel resources by the community",
        applications=config.AWESOME_APPLICATIONS,
    ).servable()
