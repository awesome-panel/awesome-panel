"""Provides the MENU html string which is appended to all templates

Please note that the MENU only works in [Fast](https://www.fast.design/) based templates.

If you need some sort of custom MENU html string feel free to customize this code.
"""
from awesome_panel_extensions.frameworks.fast.fast_menu import to_menu

from src.shared import config

if config.applications:
    MENU = to_menu(
        config.applications.values(), accent_color=config.color_primary, expand=["Main"]
    ).replace("\n", "")
else:
    MENU = ""
