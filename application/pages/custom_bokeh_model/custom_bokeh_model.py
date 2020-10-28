"""# Custom Panel Extensions

One super power of Panel is that its actually extensible. You can write custom Panes, Layouts and
Widgets using Bokeh Extensions. This is actually how Panel is developed.

If you want to learn how to create custom Bokeh/ Panel extensions you can read my guide \
[Panel Extensions Guide]\
(https://awesome-panel.readthedocs.io/en/latest/guides/awesome-panel-extensions-guide/index.html)
"""

import pathlib

import panel as pn
from bokeh.core.properties import Instance, String
from bokeh.layouts import column
from bokeh.models import HTMLBox, Slider

from application.template import get_template

CUSTOM_TS = pathlib.Path(__file__).parent / "custom_bokeh_model.ts"
CUSTOM_TS_STR = str(CUSTOM_TS.resolve())


class Custom(HTMLBox):
    """Example implementation of a Custom Bokeh Model"""

    __implementation__ = CUSTOM_TS_STR

    text = String(default="Custom text")

    slider = Instance(Slider)


def view():
    """Run this to run the application"""
    slider = Slider(start=0, end=10, step=0.1, value=0, title="value")
    custom = Custom(text="Special Slider Display", slider=slider)
    layout = column(slider, custom, sizing_mode="stretch_width")

    pn.config.sizing_mode = "stretch_width"
    main = [pn.pane.Markdown(__doc__), pn.pane.Bokeh(layout)]
    pn.config.sizing_mode = "fixed"
    return get_template(title="Custom Model Model", main=main)


if __name__.startswith("bokeh"):
    view().servable()
