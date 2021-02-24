"""Provides

- config: An instance of SiteConfig holding the current Site configuration
"""
import os
import pathlib

from src.shared._config import _create_site_config

_SITE_CONFIG_STR = os.getenv("SITE_CONFIG")
if _SITE_CONFIG_STR:
    config = _create_site_config(config_root=_SITE_CONFIG_STR)
else:
    config = _create_site_config(config_root=pathlib.Path(__file__).parent.parent / "config")
