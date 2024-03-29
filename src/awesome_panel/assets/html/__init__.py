"""Module containing paths to and text of html files"""
import pathlib
from functools import lru_cache

from ..svg import fast_collapsed_icon, fast_expanded_icon  # type: ignore

PATH = pathlib.Path(__file__).parent

MENU_FAST_OTHER_PATH = PATH / "menu_fast_other.html"

_MENU_FAST_OTHER_HTML = MENU_FAST_OTHER_PATH.read_text(encoding="utf-8")

MAIN_MENU = (PATH / "main_menu.html").read_text(encoding="utf8")


@lru_cache()
def menu_fast_html(accent: str = "#1f77b4") -> str:
    """Combines the specific app_html to other html into a fast html menu"""
    return MAIN_MENU.replace("#1f77b4", accent)


SHOELACE_TEMPLATE_PATH = PATH / "shoelace_template.html"
