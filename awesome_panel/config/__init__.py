"""Shared configuration and functionality for awesome_panel apps"""
from functools import wraps
from typing import Optional

import panel as pn
from awesome_panel_extensions.site.models import Application

from ..assets.html import menu_fast_html
from ..assets.yaml import APPLICATIONS_CONFIG_PATH, AWESOME_CONFIG_PATH

SITE = "Awesome Panel"

ACCENT = "#1f77b4"
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

AWESOME_APPLICATIONS = Application.read(AWESOME_CONFIG_PATH)
APPLICATIONS = Application.read(APPLICATIONS_CONFIG_PATH)
APPLICATIONS_MAP = {app.url: app for app in APPLICATIONS}
APPLICATIONS_MENU_MAP = {}

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
            return "  " + app.name
        return " " + app.name

    return app.category + app.name


def _get_app_menu_fast_html():
    for app in sorted(APPLICATIONS, key=_app_sort_key):
        category = app.category
        if not category in APPLICATIONS_MENU_MAP:
            APPLICATIONS_MENU_MAP[category] = [app]
        else:
            APPLICATIONS_MENU_MAP[category].append(app)

    html = ""
    for category, apps in APPLICATIONS_MENU_MAP.items():
        html += f"""
        <fast-accordion-item slot="item" expanded>
            <h3 slot="heading" style="margin:0px">{category}</h3>{{ COLLAPSED_ICON }}{{ EXPANDED_ICON }}
            <ul>
    """
        for app in apps:
            html += (
                f"""          <li><a apperance="stealth" href="{app.url}">{app.name}</a></li>\n"""
            )

        html += """
            </ul>
        </fast-accordion-item>    
    """
    return html


app_menu_fast_html = _get_app_menu_fast_html()


def get_theme() -> str:
    """Returns the name of the active theme"""
    template = pn.state.template
    theme = "dark" if template.theme == pn.template.DarkTheme else "default"
    return theme


def extension(
    *args,
    url,
    site=SITE,
    template: Optional[str] = "fast",
    accent_color=ACCENT,
    main_max_width=None,
    intro_section=True,
    sizing_mode="stretch_width",
    **kwargs,
) -> Application:
    """A customized version of pn.extension for this site"""
    pn.extension(*args, sizing_mode=sizing_mode, template=template, **kwargs)

    app = APPLICATIONS_MAP[url]

    if template:
        pn.state.template.site = site
        pn.state.template.title = app.name
        if template == "fast":
            pn.state.template.accent_base_color = accent_color
            pn.state.template.sidebar_footer = menu_fast_html(
                app_html=app_menu_fast_html, accent=accent_color
            )
        pn.state.template.header_background = accent_color
        if main_max_width:
            pn.state.template.main_max_width = main_max_width

    if intro_section:
        app.intro_section().servable()

    return app
