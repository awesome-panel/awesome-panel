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
MAIN_MAX_WIDTH = "1148px"
DEFAULT_AUTHOR="Marc Skov Madsen"

# def _set_template_main(template: pn.template.BaseTemplate, main: List):
#     if isinstance(template, pn.template.ReactTemplate):
#         for index, item in enumerate(main):
#             template.main[index, 0] = item
#     else:
#         template.main[:] = main
THUMBNAILS_ROOT = "https://github.com/MarcSkovMadsen/awesome-panel/raw/master/assets/images/thumbnails/"
CODE_ROOT="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/"
GIF_ROOT="https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications/"
MP4_ROOT="https://github.com/MarcSkovMadsen/awesome-panel-assets/blob/master/awesome-panel/applications/"

class AwesomePanelSite(Site):
    """The Awesome Panel Site"""

    def register_pre_view(self, application: Application):
        app = application
        if not app.author:
            app.author=DEFAULT_AUTHOR
        if app.thumbnail_url and not app.thumbnail_url.startswith("http"):
            app.thumbnail_url = THUMBNAILS_ROOT + app.thumbnail_url
        if app.code_url and not app.code_url.startswith("http"):
            app.code_url=CODE_ROOT + app.code_url
            if not "Code" in app.tags:
                app.tags.append("Code")
        if app.gif_url and not app.gif_url.startswith("http"):
            app.gif_url=GIF_ROOT + app.gif_url
        if app.mp4_url and not app.mp4_url.startswith("http"):
            app.mp4_url=MP4_ROOT + app.mp4_url
        if not "Application" in app.tags:
            app.tags.append("Application")

        application.tags = list(sorted(application.tags))

        # intro_section = create_application_view(application)
        # try:
        #     template.main.append(intro_section)
        # except:
        #     template.main[0, 0:12]=intro_section

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

    def get_intro_section(self, name: str) -> pn.pane.HTML:
        html = self.get_application(name)._repr_html_()
        return pn.pane.HTML(html)


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
