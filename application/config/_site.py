import pathlib
from typing import List, Optional

import panel as pn
from awesome_panel_extensions.alpha.resource_view import \
    view as create_application_view
from awesome_panel_extensions.site import Site
from awesome_panel_extensions.site.application import Application
from panel.template.base import BasicTemplate

from . import _authors

ROOT_PATH = pathlib.Path(__file__).parent
ASSETS_PATH = ROOT_PATH.parent / "assets"
JS_PATH = ASSETS_PATH / "js"
CSS_PATH = ASSETS_PATH / "css"
HTML_PATH = ASSETS_PATH / "html"
LINKS_PATH = HTML_PATH / "links.html"
LINKS = LINKS_PATH.read_text()
SITE = "Awesome Panel"
FAVICON = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/"
    "2781d86d4ed141889d633748879a120d7d8e777a/assets/images/favicon.ico"
)
MAIN_MAX_WIDTH = "1148xp"
DEFAULT_AUTHOR="Marc Skov Madsen"

# def _set_template_main(template: pn.template.BaseTemplate, main: List):
#     if isinstance(template, pn.template.ReactTemplate):
#         for index, item in enumerate(main):
#             template.main[index, 0] = item
#     else:
#         template.main[:] = main
THUMBNAILS_ROOT = "https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/thumbnails/"
CODE_ROOT="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/"
GIF_ROOT="https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications"
MP4_ROOT="https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications"

class AwesomePanelSite(Site):
    """The Awesome Panel Site"""

    def register_clean_arguments(
        self,
        url: str,
        name: str,
        description: str,
        author: str,
        thumbnail_url: str,
        tags: List,
        documentation_url: str,
        code_url: str,
        gif_url: str,
        mp4_url: str,
        youtube_url: str = "",
    ):
        if not author:
            author=DEFAULT_AUTHOR
        if thumbnail_url and not thumbnail_url.startswith("http"):
            thumbnail_url = THUMBNAILS_ROOT + thumbnail_url
        if code_url and not code_url.startswith("http"):
            code_url=CODE_ROOT + code_url
            if not "Code" in tags:
                tags.append("Code")
        if gif_url and not gif_url.startswith("http"):
            gif_url=GIF_ROOT + gif_url
        if mp4_url and not mp4_url.startswith("http"):
            mp4_url=MP4_ROOT + mp4_url
        if not "Application" in tags:
            tags.append("Application")

    def register_pre_view(self, template: BasicTemplate, application: Application):
        intro_section = create_application_view(application)
        try:
            template.main.append(intro_section)
        except:
            template.main[0, 0:12]=intro_section

    def register_post_view(self, template: BasicTemplate, application: Application):
        super().register_post_view(template, application)

        if hasattr(template, "sidebar"):
            menu = pn.pane.HTML(LINKS, sizing_mode="stretch_width")
            template.sidebar.append(menu)

    def get_template(
        self, template: Optional[str] = None, theme: Optional[str] = None, **params
    ) -> pn.template.BaseTemplate:
        params["favicon"] = params.get("favicon", FAVICON)
        params["main_max_width"] = params.get("main_max_width", MAIN_MAX_WIDTH)
        return super().get_template(template=template, theme=theme, **params)


site = AwesomePanelSite(
    name=SITE,
    css_path = CSS_PATH,
    js_path = JS_PATH,
)

site.authors.extend(
    [
        _authors.JOCHEM_SMIT,
        _authors.MARC_SKOV_MADSEN,
    ]
)
