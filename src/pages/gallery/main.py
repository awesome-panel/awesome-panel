"""## The Gallery Page of awesome-panel.org"""
import importlib
import pathlib
from types import ModuleType
from typing import List

import panel as pn
from panel import Column
from panel.layout import HSpacer
from panel.widgets import Button

from awesome_panel import database
from awesome_panel.express import Divider, spinners
from awesome_panel.express.pane.panes import Markdown
from awesome_panel.express.bootstrap import InfoAlert
from awesome_panel.shared.models import Resource

ROOT = str(pathlib.Path.cwd())
# pylint: disable=line-too-long
TEXT = """\
# Awesome Panel Gallery ![Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

With this Gallery I hope to

- show you the power of Panel
- help lower the friction of using Panel
- inspire you to build awesome analytics apps in Python.

This Gallery is running on a low end server on Azure.
So the performance can be significantly improved if you have access to a higher end server.

If you have an awesome tool or app you wan't to show here you are very welcome. You can read how to
in the [Contribute](https://github.com/marcskovmadsen/awesome-panel#how-to-contribute-an-app-to-the-gallery)
section of the README."""
# pylint: enable=line-too-long

INFO_TEXT = """\
Please **use FireFox, Safari or Edge** if you can. Alternatively you can use Chrome - but it's
[slower](https://github.com/bokeh/bokeh/issues/9515). Internet Explorer is not supported."""


def info():
    """An InfoAlert with relevant text"""
    return Column(InfoAlert(text=INFO_TEXT), sizing_mode="stretch_width")


def page_code_url_to_html(page: Resource) -> str:
    """Converts a page to html link to the code with a font awesome icon

    Make sure to run pnx.fontawesome.extend() for this to work

    Arguments:
        page {Resource} -- A page

    Returns:
        str -- A html string linking to the code and with a nice fontawesome icon
    """
    return (
        f'<a href={page.url} target="_blank" title="Source Code">' '<i class="fas fa-code"></i></a>'
    )


def to_module_function(gallery_url: str) -> ModuleType:
    """Converts a link to a Python gallery file to a module string

    Arguments:
        gallery_url {str} -- The link to the Python gallery file

    Returns:
        Module -- The module string, for example 'gallery.boostrap_dashboard.main'
    """

    module_str = (
        gallery_url.replace(database.settings.GITHUB_BLOB_MASTER_URL, "")
        .replace(".py", "")
        .replace("/", ".")
        .replace("\\", ".")
    )
    return importlib.import_module(module_str)


class GalleryButton(Button):
    """## Button that loads page.

    When clicked the page of the GalleryButton loads"""

    def __init__(self, page: Resource, page_outlet, **kwargs):
        """## Button that loads page

        When clicked the page of the GalleryButton loads

        Arguments:
            name {[type]} -- The name/ text of the Button
            page {[type]} -- The page to load
            page_outlet {[type]} -- The page_outlet to load the page to
        """
        super().__init__(name=page.name, button_type="primary", **kwargs)
        self.page = page
        self.page_outlet = page_outlet

        def click_handler(event):  # pylint: disable=unused-argument
            text = (
                f"<h1>Gallery / {page.name}</h1>"
                f"<p>{page.author.to_html()}, {page_code_url_to_html(page)}</p>"
            )
            page_view = to_module_function(page.url).view()
            self.page_outlet[:] = [spinners.DefaultSpinner().center()]
            self.page_outlet[:] = [pn.pane.HTML(text), page_view]

        self.on_click(click_handler)


class GalleryCard(Column):
    """A Card consisting of an image and a button"""

    def __init__(self, page: Resource, page_outlet, **kwargs):
        """A Card consisting of an image and a button

        Arguments:
            name {[type]} -- The name of the card/ the text on the Button
            page {Resource} -- The page to load
            page_outlet {[type]} -- The page to load to
        """
        self.button = GalleryButton(page, page_outlet, width=365, align="center", **kwargs)
        spacer = pn.layout.HSpacer(height=5)
        super().__init__(
            spacer,
            pn.pane.PNG(page.thumbnail_path, width=360, height=272, align="center",),
            # spacer,
            self.button,
            spacer,
            name="gallery-item-" + page.name,
            width=400,
            margin=10,
            css_classes=["card"],
            **kwargs,
        )


class Gallery:  # pylint: disable=too-few-public-methods
    """The Gallery page"""

    def __init__(self, page_outlet: pn.Column, apps_in_gallery: List[Resource]):
        """Constructs a Gallery

        Arguments:
            page_outlet {pn.Column} -- A Column to hold the selected gallery page
            apps_in_gallery {List[Resource]} -- The list of apps to include in the gallery
        """
        self.page_outlet = page_outlet
        self.apps_in_gallery = apps_in_gallery

    def view(self) -> Column:
        """The gallery view of awesome-panel.org"""
        buttons = []
        for app in self.apps_in_gallery:
            buttons.append(GalleryCard(app, self.page_outlet))

        return Column(
            Markdown(TEXT),
            info(),
            HSpacer(height=25),
            Divider(),
            *buttons,
            name="Gallery",
            sizing_mode="stretch_width",
        )
