import pathlib
from functools import lru_cache

from ..svg import fast_collapsed_icon, fast_expanded_icon  # type: ignore

PATH = pathlib.Path(__file__).parent

MENU_FAST_OTHER_PATH = PATH / "menu_fast_other.html"

_MENU_FAST_OTHER_HTML = MENU_FAST_OTHER_PATH.read_text(encoding="utf-8")


@lru_cache()
def menu_fast_html(app_html: str, accent: str = "#1f77b4") -> str:
    return (
        ('<fast-accordion id="menu">' + app_html + _MENU_FAST_OTHER_HTML + "</fast-accordion>")
        .replace("{ COLLAPSED_ICON }", fast_collapsed_icon(stroke=accent))
        .replace("{ EXPANDED_ICON }", fast_expanded_icon(stroke=accent))
    )


SHOELACE_TEMPLATE_PATH = PATH / "shoelace_template.html"
