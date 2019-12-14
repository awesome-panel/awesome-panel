"""## The Gallery Page of awesome-panel.org"""
import importlib
import inspect
import pathlib
from types import ModuleType

import panel as pn
from panel import Column
from panel.layout import HSpacer
from panel.widgets import Button

from awesome_panel.app.services import module_to_github_url
from awesome_panel import database
from awesome_panel.express import spinners
from awesome_panel.express._pane._panes import Markdown
from awesome_panel.express.bootstrap import InfoAlert

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

If you have an awesome tool or app you wan't to show here you are very welcome.
You can do so via a [pull request](https://github.com/MarcSkovMadsen/awesome-panel/pulls)."""
# pylint: enable=line-too-long

INFO_TEXT = """\
Please **use FireFox, Safari or Edge** if you can. Alternatively you can use Chrome - but it's
[slower](https://github.com/bokeh/bokeh/issues/9515). Internet Explorer is not supported."""


def info():
    """An InfoAlert with relevant text"""
    return Column(InfoAlert(text=INFO_TEXT), sizing_mode="stretch_width")


def to_module_function(gallery_url: str) -> ModuleType:
    """Converts a link to a python gallery file to a module string

    Arguments:
        gallery_url {str} -- The link to the python gallery file

    Returns:
        Module -- The module string, for example 'gallery.boostrap_dashboard.main'
    """

    module_str = (
        gallery_url.replace(database.settings.GITHUB_URL, "")
        .replace(".py", "")
        .replace("/", ".")
        .replace("\\", ".")
    )
    return importlib.import_module(module_str)


# pylint: disable=line-too-long
APPS = {
    app.name: to_module_function(app.url).view for app in database.apps_in_gallery.APPS_IN_GALLERY  # type: ignore
}
# pylint: enable=line-too-long


class GalleryButton(Button):
    """## Button that loads page.

    When clicked the page of the GalleryButton loads"""

    def __init__(self, name, page, page_outlet, **kwargs):
        """## Button that loads page

        When clicked the page of the GalleryButton loads

        Arguments:
            name {[type]} -- The name/ text of the Button
            page {[type]} -- The page to load
            page_outlet {[type]} -- The page_outlet to load the page to
        """
        super().__init__(name=name, button_type="primary", **kwargs)
        self.name = name
        self.page = page
        self.page_outlet = page_outlet

        def click_handler(event):  # pylint: disable=unused-argument
            file_url = module_to_github_url(self.page)
            text = (
                f'<h2>{name}&nbsp;<a href={file_url} target="_blank" title="Source Code">'
                '<i class="fas fa-code"></i></a></h2>'
            )

            self.page_outlet[:] = [spinners.DefaultSpinner().center()]
            self.page_outlet[:] = [text, self.page()]

        self.on_click(click_handler)


class GalleryCard(Column):
    """A Card consisting of an image and a button"""

    def __init__(self, name, page, page_outlet, **kwargs):
        """A Card consisting of an image and a button

        Arguments:
            name {[type]} -- The name of the card/ the text on the Button
            page {[type]} -- The page to load
            page_outlet {[type]} -- The page to load to
        """
        self.button = GalleryButton(name, page, page_outlet, width=365, align="center", **kwargs)
        spacer = pn.layout.HSpacer(height=5)
        super().__init__(
            spacer,
            pn.pane.PNG(
                "gallery/bootstrap_dashboard/bootstrap_dashboard.png",
                width=360,
                height=272,
                align="center",
            ),
            # spacer,
            self.button,
            spacer,
            name="gallery-item-" + name,
            width=400,
            margin=10,
            css_classes=["card"],
            **kwargs,
        )


class Gallery:  # pylint: disable=too-few-public-methods
    """The Gallery page"""

    def __init__(self, page_outlet: pn.Column):
        self.page_outlet = page_outlet

    def view(self) -> Column:
        """The gallery view of awesome-panel.org"""
        buttons = []
        for name, page in APPS.items():
            buttons.append(GalleryCard(name, page, self.page_outlet))

        gallery = Column(
            Markdown(TEXT),
            info(),
            HSpacer(height=50),
            *buttons,
            name="Gallery",
            sizing_mode="stretch_width",
        )

        return gallery
