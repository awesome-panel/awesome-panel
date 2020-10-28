"""Utilities used by awesome-panel.org"""
import pathlib
from typing import Dict, List, Optional

import panel as pn

from application.template.settings import SiteSettings

ROOT = pathlib.Path(__file__).parent

TEMPLATES: Dict[str, pn.template.BaseTemplate] = {
    "vanilla": pn.template.VanillaTemplate,
    "golden": pn.template.GoldenTemplate,
    "material": pn.template.MaterialTemplate,
    "bootstrap": pn.template.BootstrapTemplate,
    "react": pn.template.ReactTemplate,
}
DEFAULT_TEMPLATE = "material"
THEMES = {
    "vanilla": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "golden": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "bootstrap": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "react": {"default": pn.template.DefaultTheme, "dark": pn.template.DarkTheme},
    "material": {
        "default": pn.template.material.MaterialDefaultTheme,
        "dark": pn.template.material.MaterialDarkTheme,
    },
}
DEFAULT_THEME = "default"
TEMPLATE = "material"
THEME = "default"
SITE = "Awesome Panel"
FAVICON = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/"
    "2781d86d4ed141889d633748879a120d7d8e777a/assets/images/favicon.ico"
)
APPLICATION = {"About": "about"}

LINKS_PATH = ROOT / "links.html"
LINKS = LINKS_PATH.read_text()
TEMPLATE_CSS_ID = "/* CUSTOM TEMPLATE CSS */\n"


def _set_template_css(template, theme):
    # remove other site css
    pn.config.raw_css = [css for css in pn.config.raw_css if not css.startswith(TEMPLATE_CSS_ID)]

    files = [
        "all.css",
        f"all_{theme}.css",
        f"{template}.css",
        f"{template}_{theme}.css",
    ]
    for file in files:
        if not file in pn.state.cache:
            file_css_id = f"/* {file} */\n"
            text = TEMPLATE_CSS_ID + file_css_id + (ROOT / file).read_text()
        else:
            text = pn.state.cache[file]
            pn.state.cache.pop(file)
        pn.config.raw_css.append(text)


def _set_template_main(template: pn.template.BaseTemplate, main: List):
    if isinstance(template, pn.template.ReactTemplate):
        for index, item in enumerate(main):
            template.main[index, 0] = item
    else:
        template.main[:] = main


def _get_menu():
    return pn.pane.HTML(LINKS, sizing_mode="stretch_width")


def _get_params(value, class_):
    if isinstance(value, class_):
        return value
    if isinstance(value, tuple):
        value = [*value]
    elif not isinstance(value, list):
        value = [value]
    # Important to fx. convert @param.depends functions
    value = [pn.panel(item) for item in value]

    if class_ == pn.layout.ListLike:
        return class_(objects=value)
    if class_ == pn.layout.GridSpec:
        grid = class_(ncols=12)
        for index, item in enumerate(value):
            grid[index, :] = item
        return grid

    return value


def get_template(  # pylint: disable=too-many-arguments
    title: str,
    template: Optional[str] = None,
    theme: Optional[str] = None,
    favicon: str = FAVICON,
    main_max_width="1140px",
    site=SITE,
    **params,
) -> pn.template.BaseTemplate:
    """Returns the specified BaseTemplate

    Args:
        title (str, optional): The title of the app. Defaults to TITLE.
        template (str, optional): The name of the template. Defaults to TEMPLATE.
        theme (str, optional): The name of the theme. Defaults to THEME.
        favicon (str, optional): A link or path to a favicon. Defaults to FAVICON.
        main_max_width (str, optional): The max width of the main area. Defaults to "1140px".
        site (str, optional): The name of the site. Defaults to SITE.
        **params: Optional parameters

    Returns:
        pn.template.BaseTemplate: The specified Template
    """
    if not template:
        template = pn.state.session_args.get("template", TEMPLATE)
        if isinstance(template, list):
            template = template[0].decode("utf-8")
    template = template.strip("'").strip('"')
    if not theme:
        theme = pn.state.session_args.get("theme", THEME)
        if isinstance(theme, list):
            theme = theme[0].decode("utf-8")
    theme = theme.strip("'").strip('"')
    template_class = TEMPLATES.get(str(template), TEMPLATES[DEFAULT_TEMPLATE])
    # To be fixed with PR https://github.com/holoviz/panel/pull/1694
    if "header" in params:
        params["header"] = _get_params(params["header"], template_class.param.header.class_)
    if "main" in params:
        params["main"] = _get_params(params["main"], template_class.param.main.class_)
    if "sidebar" in params:
        params["sidebar"] = _get_params(params["sidebar"], template_class.param.sidebar.class_)
    if "modal" in params:
        params["modal"] = _get_params(params["modal"], template_class.param.modal.class_)

    _set_template_css(template, theme)

    site_settings = SiteSettings()

    template_instance = template_class(
        theme=THEMES.get(str(template), THEMES[DEFAULT_TEMPLATE]).get(str(theme), DEFAULT_THEME),
        title=title,
        favicon=favicon,
        main_max_width=main_max_width,
        site=site,
        **params,
    )
    template_instance.sidebar.append(_get_menu())

    header = [
        site_settings.js_panel,
        pn.Param(
            site_settings,
            parameters=["template", "toggle_theme"],
            default_layout=pn.Row,
            show_labels=False,
            show_name=False,
            sizing_mode="fixed",
            width=200,
        ),
    ]
    template_instance.header.extend(header)

    return template_instance


if __name__.startswith("bokeh"):
    _template = get_template(title="Test App")
    _set_template_main(_template, [pn.pane.Markdown("hello world")])
    _template.servable()
