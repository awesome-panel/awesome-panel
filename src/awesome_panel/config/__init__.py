"""Shared configuration and functionality for awesome_panel apps"""
from functools import wraps
from typing import Optional, Union

import panel as pn
from awesome_panel_extensions.site.gallery import GalleryTemplate
from awesome_panel_extensions.site.models import Application
from panel.template import FastGridTemplate, FastListTemplate

from ..assets.html import menu_fast_html
from ..assets.yaml import APPLICATIONS_CONFIG_PATH, AWESOME_CONFIG_PATH

SITE = "Awesome Panel"

ACCENT = "#1f77b4"  # "#E1477E"
PALETTE = [
    ACCENT,
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]

# pylint: disable=line-too-long
FAVICON = "https://raw.githubusercontent.com/awesome-panel/awesome-panel-assets/320297ccb92773da099f6b97d267cc0433b67c23/favicon/ap-1f77b4.ico"
# pylint: enable=line-too-long

AWESOME_APPLICATIONS = Application.read(AWESOME_CONFIG_PATH)
APPLICATIONS = Application.read(APPLICATIONS_CONFIG_PATH)
APPLICATIONS_MAP = {app.url: app for app in APPLICATIONS}

pn.state.cache["cached"] = {}

CACHE = pn.state.cache["cached"]


def cached(func):
    """
    Decorator that caches the results of the function call.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Generate the cache key from the function's arguments.
        key_parts = [func.__name__] + list(args) + [k + "-" + v for k, v in kwargs.items()]
        key = "-".join(key_parts)
        result = CACHE.get(key)

        if result is None:
            # Run the function and cache the result for next time.
            result = func(*args, **kwargs)
            CACHE[key] = result

        return result

    return wrapper


def _app_sort_key(app: Application):
    if app.category == "Main":
        if app.name == "Home":
            return "   " + app.name
        return "  " + app.name
    if app.category == "Getting Started":
        return " " + app.name

    return (app.category + app.name).lower()


app_menu_fast_html = menu_fast_html()


def get_theme() -> str:
    """Returns the name of the active theme"""
    template = pn.state.template
    theme = "dark" if (template and template.theme == pn.template.DarkTheme) else "default"
    return theme


def get_json_theme() -> str:
    """Returns the name of the active theme"""
    if get_theme() == "dark":
        return "dark"
    return "light"


_TEMPLATES = [FastGridTemplate, FastListTemplate, GalleryTemplate]

# pylint: disable=line-too-long
FOLLOW_ON_TWITTER = """[![Follow on Twitter](https://img.shields.io/twitter/follow/MarcSkovMadsen.svg?style=social)](https://twitter.com/MarcSkovMadsen)"""
GITHUB_STARS = "[![GitHub stars](https://img.shields.io/github/stars/MarcSkovMadsen/awesome-panel.svg?style=social&label=Star&maxAge=2592000)](https://github.com/awesome-panel/awesome-panel/stargazers/)"
# pylint: enable=line-too-long


def get_header():
    """Returns a component to be added to the template header"""
    return pn.Row(
        pn.layout.Spacer(sizing_mode="stretch_width"),
        pn.pane.Markdown(GITHUB_STARS, sizing_mode="fixed", width=75),
        pn.pane.Markdown(FOLLOW_ON_TWITTER, sizing_mode="fixed", width=230),
        pn.layout.VSpacer(width=4),
        height=86,
        sizing_mode="stretch_width",
    )


def add_header(template: pn.template.BaseTemplate):
    """Adds a component to the header"""
    template.header.append(get_header())


for _template in _TEMPLATES:
    _template.param.favicon.default = FAVICON
    _template.param.site.default = "Awesome Panel"
    _template.param.accent_base_color.default = ACCENT

    if not _template == GalleryTemplate:
        _template.param.header_background.default = ACCENT
        _template.param.sidebar_footer.default = menu_fast_html(accent=ACCENT)


def extension(
    *args,
    url,
    site=SITE,
    template: Optional[Union[str, pn.template.BaseTemplate]] = "fast",
    accent_color=ACCENT,
    main_max_width=None,
    intro_section=True,
    favicon=FAVICON,
    sizing_mode="stretch_width",
    **kwargs,
) -> Application:
    """A customized version of pn.extension for this site"""
    if isinstance(template, str) or not template:
        pn.extension(*args, sizing_mode=sizing_mode, template=template, **kwargs)
        if template:
            template = pn.state.template
    else:
        pn.extension(*args, sizing_mode=sizing_mode, **kwargs)

    app = APPLICATIONS_MAP[url]

    if isinstance(template, pn.template.BaseTemplate):
        template.site = site
        template.favicon = favicon
        template.title = app.name
        template.site_url = "./"

        template.header_background = accent_color

        if main_max_width:
            template.main_max_width = main_max_width
        if isinstance(template, (pn.template.FastListTemplate, pn.template.FastGridTemplate)):
            template.accent_base_color = accent_color
            template.sidebar_footer = menu_fast_html(accent=accent_color)
            add_header(template)

    if intro_section and template not in [pn.template.FastGridTemplate]:
        app.intro_section().servable()

    return app
