"""## The Gallery Page of awesome-panel.org"""
from panel import Column
from panel.layout import HSpacer
from panel.widgets import Button
import panel as pn

from awesome_panel.express import Title
from awesome_panel.express._pane._panes import Markdown
from awesome_panel.express.bootstrap import InfoAlert
from gallery import bootstrap_dashboard

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


INFO_TEXT = """\
Please **use FireFox, Safari or Edge** if you can. Alternatively you can use Chrome - but it's
[slower](https://github.com/bokeh/bokeh/issues/9515). Internet Explorer is not supported."""


def info():
    return Column(InfoAlert(text=INFO_TEXT), sizing_mode="stretch_width")


APPS = {"Info Alert": info, "Bootstrap Dashboard": bootstrap_dashboard.view}


class GalleryButton(Button):
    def __init__(self, name, page, page_outlet, **kwargs):
        super().__init__(name=name, button_type="primary", **kwargs)
        self.name = name
        self.page = page
        self.page_outlet = page_outlet

        def click_handler(event):
            title = Title(name)
            self.page_outlet.clear()
            self.page_outlet.append(title)
            self.page_outlet.append(self.page())

        self.on_click(click_handler)


class GalleryCard(Column):
    def __init__(self, name, page, page_outlet, **kwargs):
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


class Gallery:
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

