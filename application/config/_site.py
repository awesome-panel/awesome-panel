"""Defines the Awesome Panel site"""
import pathlib
from typing import List, Optional

import panel as pn
from awesome_panel_extensions.assets import svg_icons

# pylint: enable=line-too-long
from awesome_panel_extensions.site import Site
from awesome_panel_extensions.site.application import Application
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
LINKS = LINKS_PATH.read_text()
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
    LINKS_FAST_PATH.read_text()
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


class AwesomePanelSite(Site):
    """The Awesome Panel Site"""

    def create_application(  # pylint: disable=too-many-arguments
        self,
        url: str,
        name: str,
        introduction: str,
        description: str,
        author: str,
        thumbnail_url: str,
        code_url: str = "",
        documentation_url: str = "",
        gif_url: str = "",
        mp4_url: str = "",
        youtube_url: str = "",
        tags: Optional[List] = None,
    ) -> Application:
        app = super().create_application(
            url=url,
            name=name,
            introduction=introduction,
            description=description,
            author=author,
            thumbnail_url=thumbnail_url,
            code_url=code_url,
            documentation_url=documentation_url,
            gif_url=gif_url,
            mp4_url=mp4_url,
            youtube_url=youtube_url,
            tags=tags,
        )
        if not app.author:
            app.author = DEFAULT_AUTHOR
        if app.thumbnail_url and not app.thumbnail_url.startswith("http"):
            app.thumbnail_url = THUMBNAILS_ROOT + app.thumbnail_url
        if app.code_url and not app.code_url.startswith("http"):
            app.code_url = CODE_ROOT + app.code_url
            if not "Code" in app.tags:
                app.tags.append("Code")
        if app.gif_url and not app.gif_url.startswith("http"):
            app.gif_url = GIF_ROOT + app.gif_url
        if app.mp4_url and not app.mp4_url.startswith("http"):
            app.mp4_url = MP4_ROOT + app.mp4_url
        if not "Application" in app.tags:
            app.tags.append("Application")

        app.tags = list(sorted(app.tags))
        return app

    def register_post_view(self, template: BasicTemplate, application: Application):
        super().register_post_view(template, application)
        if isinstance(template, (FastListTemplate, FastGridTemplate)):
            links = LINKS_FAST
        else:
            links = LINKS
        if hasattr(template, "sidebar"):
            menu = pn.pane.HTML(links, sizing_mode="stretch_width")
            template.sidebar.append(menu)

        if isinstance(application.introduction, str):
            template.meta_description = application.introduction.replace("# ", "").lstrip()
        template.meta_keywords = (
            "HoloViz, Panel, Python, Date, Models, Analytics, Visualization, Data Science, Science,"
            " Machine Learning, Apps, Dash, Streamlit, Voila, Bokeh, HoloViews, Matplotlib, Plotly"
        )
        template.meta_author = "Marc Skov Madsen"

    def create_template(
        self, template: Optional[str] = None, theme: Optional[str] = None, **params
    ) -> pn.template.base.BasicTemplate:
        params["favicon"] = params.get("favicon", FAVICON)
        params["main_max_width"] = params.get("main_max_width", MAIN_MAX_WIDTH)
        return super().create_template(template=template, theme=theme, **params)


site = AwesomePanelSite(
    name=SITE,
    css_path=CSS_PATH,
    js_path=JS_PATH,
)

site.authors.extend(
    [
        _authors.ANDREW_HUANG,
        _authors.JOCHEM_SMIT,
        _authors.MARC_SKOV_MADSEN,
        _authors.STEPHEN_KILCOMMINS,
    ]
)
