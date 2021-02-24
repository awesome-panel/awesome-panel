"""Provides customized and branded versions of the templates to be used in the site

Currently

- ListTemplate similar to VanillaTemplate shipped with Panel
- GridTemplate similar to ReactTemplate shipped with Panel
- GalleryTemplate a template for creating a Gallery.
"""
# This will make it much easier to customize your templates when you start wanting to brand your
# site.
import param
from awesome_panel_extensions.frameworks.fast.templates.fast_gallery_template import (
    FastGalleryTemplate as _FastGalleryTemplate,
)
from awesome_panel_extensions.frameworks.fast.templates.fast_grid_template import (
    FastGridTemplate as _FastGridTemplate,
)
from awesome_panel_extensions.frameworks.fast.templates.fast_list_template import (
    FastListTemplate as _FastListTemplate,
)

from src.shared import config
from src.shared._menu import MENU


class ListTemplate(_FastListTemplate):
    __doc__ = _FastListTemplate.__doc__

    site = param.String(config.site_name)
    sidebar_footer = param.String(MENU)


class GridTemplate(_FastGridTemplate):
    __doc__ = _FastGridTemplate.__doc__

    site = param.String(config.site_name)
    sidebar_footer = param.String(MENU)


class GalleryTemplate(_FastGalleryTemplate):
    __doc__ = _FastGalleryTemplate.__doc__

    site = param.String(config.site_name)
    title = param.String("Gallery")
    description = param.String(config.gallery_description)
