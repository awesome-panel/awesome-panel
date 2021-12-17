"""Defines the Awesome Panel site"""
import pathlib

import panel as pn

# pylint: enable=line-too-long
from awesome_panel_extensions import site as _site
from awesome_panel_extensions.assets import svg_icons
from awesome_panel_extensions.site.models import Application
from panel import template as _template

# pylint: disable=line-too-long
from panel.template import FastGridTemplate, FastListTemplate
from panel.template.base import BasicTemplate

from . import _authors

# pylint: disable=protected-access
# Hack to solve:
_template.FastGridTemplate._resources = {
    k: v for k, v in _template.FastGridTemplate._resources.items() if k != "css"
}

ROOT_PATH = pathlib.Path(__file__).parent
ASSETS_PATH = ROOT_PATH.parent / "assets"
JS_PATH = ASSETS_PATH / "js"
CSS_PATH = ASSETS_PATH / "css"
HTML_PATH = ASSETS_PATH / "html"
LINKS_PATH = HTML_PATH / "links.html"
LINKS = LINKS_PATH.read_text(encoding="utf8")
LINKS_FAST_PATH = HTML_PATH / "links_fast.html"
SITE = "Awesome Panel"
FAVICON = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/"
    "2781d86d4ed141889d633748879a120d7d8e777a/assets/images/favicon.ico"
)
MAIN_MAX_WIDTH = "1148px"
DEFAULT_AUTHOR = "Marc Skov Madsen"

COLLAPSED_ICON = svg_icons.FAST_COLLAPSED_ICON
EXPANDED_ICON = svg_icons.FAST_EXPANDED_ICON
LINKS_FAST = (
    LINKS_FAST_PATH.read_text(encoding="utf")
    .replace("{ COLLAPSED_ICON }", COLLAPSED_ICON)
    .replace("{ EXPANDED_ICON }", EXPANDED_ICON)
)

# pylint: disable=line-too-long

# def _set_template_main(template: pn.template.BaseTemplate, main: List):
#     if isinstance(template, pn.template.ReactTemplate):
#         for index, item in enumerate(main):
#             template.main[index, 0] = item
#     else:
#         template.main[:] = main
THUMBNAILS_ROOT = (
    "https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/thumbnails/"
)
CODE_ROOT = "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/"
GIF_ROOT = (
    "https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications/"
)
MP4_ROOT = (
    "https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications/"
)

pn.template.FastListTemplate.param.theme.default = pn.template.fast.list.FastDarkTheme
pn.template.FastGridTemplate.param.theme.default = pn.template.fast.grid.FastDarkTheme


class AwesomePanelSite(_site.Site):
    """The Awesome Panel Site"""

    def create_application(  # pylint: disable=too-many-arguments
        self,
        **params,
    ) -> Application:
        """Returns an Application from specified params.

        If you specify the author and owner uid as a string it will automatically be converted into
        a User.

        Returns:
            Application: An application
        """
        if "thumbnail" in params:
            params["thumbnail"] = THUMBNAILS_ROOT + params["thumbnail"]
        if "resources" in params:
            resources = params["resources"]
            if "code" in resources:
                resources["code"] = CODE_ROOT + resources["code"]
            if "mp4" in resources:
                resources["mp4"] = MP4_ROOT + resources["mp4"]
            if "gif" in resources:
                resources["gif"] = GIF_ROOT + resources["gif"]
        return super().create_application(**params)

    def register_post_view(self, template: BasicTemplate, application: Application):
        super().register_post_view(template, application)
        if isinstance(template, (FastListTemplate, FastGridTemplate)):
            links = LINKS_FAST
        else:
            links = LINKS
        if hasattr(template, "sidebar"):
            menu = pn.pane.HTML(links, sizing_mode="stretch_width")
            template.sidebar.append(menu)
        if "documentation" in application.resources:
            template.meta_description = (
                application.resources["documentation"].replace("# ", "").lstrip()
            )
        template.meta_keywords = (
            "HoloViz, Panel, Python, Date, Models, Analytics, Visualization, Data Science, Science,"
            " Machine Learning, Apps, Dash, Streamlit, Voila, Bokeh, HoloViews, Matplotlib, Plotly"
        )
        template.meta_author = "Marc Skov Madsen"
        template.site = "Awesome Panel"


_site.site = AwesomePanelSite()
_site.site.users.extend(
    [
        _authors.ANDREW_HUANG,
        _authors.JOCHEM_SMIT,
        _authors.MARC_SKOV_MADSEN,
        _authors.STEPHEN_KILCOMMINS,
    ]
)
site = _site.site
