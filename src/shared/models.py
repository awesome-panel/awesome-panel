"""Provides the following models used to create the site

- Application
- Person
- Resource
- SiteConfig
"""
# pylint: disable=unused-import

# We provide the models here in order to be able to (later) customize them


# Author will later be renamed to Person in the awesome-panel-extensions package
import param
from awesome_panel_extensions.site.application import Application
from awesome_panel_extensions.site.author import Author as Person
from awesome_panel_extensions.site.resource import Resource
from awesome_panel_extensions.site.site_config import SiteConfig
