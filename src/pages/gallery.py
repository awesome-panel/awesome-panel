"""## The Gallery Page of awesome-panel.org"""
from panel import Column, depends, Spacer
from panel.widgets import Select
import panel as pn

from awesome_panel.express._pane._panes import Markdown
from awesome_panel.express.bootstrap import InfoAlert
from gallery.bootstrap_dashboard import components, app

TEXT = """\
# Awesome Panel Gallery ![Awesome Badge](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

I hope this gallery can show case the power of Panel and inspire you as you build awesome analytics apps in Panel.

If you have an awesome tool or app you wan't to show case here you are very welcome.
You can do so via a [pull request](https://github.com/MarcSkovMadsen/awesome-panel/pulls)."""

INFO_TEXT = """\
Please **use FireFox, Safari or Edge** if you can.

Alternatively you can use Chrome - but it's
[slower](https://github.com/bokeh/bokeh/issues/9515).

This page does not render nicely in Internet Explorer and it's not supported.

Please **have patience** as some of the apps can take 10-30 seconds to load.
"""


def info():
    return Column(InfoAlert(text=INFO_TEXT), sizing_mode="stretch_width")


APPS = {"Info Alert": info, "Bootstrap Dashboard": app.main, "DataFrame": components.dataframe_view}


def view() -> Column:
    """The gallery view of awesome-panel.org"""
    app_selection = Select(name="Select app", options=list(APPS.keys()))

    @pn.depends(app_selection.param.value)
    def selected_app(value):
        return APPS[value]()

    return Column(
        Markdown(TEXT),
        app_selection,
        Spacer(height=50),
        selected_app,
        sizing_mode="stretch_both",
        name="Gallery",
    )
