"""## Font Awesome extension for Panel

As a user of Panel I would like to be able to use awesome layouts, formats and styles.

A part of this is being able to use [Font Awesome](https://fontawesome.com/) icons.

This module contains functionality for using Font Awesome as
[CSS Pseudo Elements](https://fontawesome.com/how-to-use/on-the-web/advanced/css-pseudo-elements)
"""
import urllib.request

import panel as pn
from awesome_panel.express.assets import FONTAWESOME_PANEL_EXPRESS_CSS

FONTAWESOME_CSS_URL = "https://use.fontawesome.com/releases/v5.11.2/css/all.css"

_EXTENDED = False

_FONTAWESOME_PANEL_EXPRESS_HEADER = """

div.bk.pas div.bk *::before, div.bk.pab div.bk *::before {
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
}
div.bk.pas div.bk *::before{
    font-family: "Font Awesome 5 Free";
}
div.bk.pab div.bk *::before {
    font-family:"Font Awesome 5 Brands"
}
"""


def extend():
    """## Extends Panel with functionality to use Font Awesome

    See [Font Awesome](https://fontawesome.com/) and
    [Font Awesome CSS Pseudo Elements]
    (https://fontawesome.com/how-to-use/on-the-web/advanced/css-pseudo-elements)
    for more information.

    To find icons refer to [Font Awesome Search]
    (https://fontawesome.com/icons/search).

    For examples refer to [W3C Font Awesome Intro]
    (https://www.w3schools.com/icons/fontawesome_icons_intro.asp)
    """
    global _EXTENDED  # pylint: disable=global-statement
    if not _EXTENDED:
        pn.config.raw_css.append(FONTAWESOME_PANEL_EXPRESS_CSS.read_text())
        pn.config.css_files.append(FONTAWESOME_CSS_URL)
        _EXTENDED = True


def get_fontawesome_panel_express() -> str:
    """Converts the official css file at FONTAWESOME_CSS_URL into it's panel
    representation

    Returns:
        str -- [description]
    """

    with urllib.request.urlopen(FONTAWESOME_CSS_URL) as file:
        fontawesome_css = file.read().decode("utf-8")

    return _to_fontawesome_panel_express(fontawesome_css)


def _to_fontawesome_panel_express(
    font_awesome_css: str,
) -> str:
    """Converts a css string like FONTAWESOME_CSS_URL into it's panel
    representation

    Returns:
        str -- [description]
    """
    css = font_awesome_css.replace(
        "}.",
        "}\n.",
    )
    lines_in = css.split("\n")
    lines_out = []
    for line in lines_in:
        if ":before{" in line:
            line = line.replace(
                ".fa-",
                "div.bk.pa-",
            )
            line = line.replace(
                ":before{",
                " div.bk *::before{",
            )
            lines_out.append(line)
    return _FONTAWESOME_PANEL_EXPRESS_HEADER + "\n".join(lines_out)
