"""
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

from application.config import site

CUSTOM_TS = pathlib.Path(__file__).parent / "custom_bokeh_model.ts"
CUSTOM_TS_STR = str(CUSTOM_TS.resolve())
TITLE = "Custom Bokeh Model"

class Custom(HTMLBox):
    """Example implementation of a Custom Bokeh Model"""

    __implementation__ = CUSTOM_TS_STR

    text = String(default="Custom text")

    slider = Instance(Slider)

@site.register(
    url="custom-bokeh-model",
    name=TITLE,
    author="Marc Skov Madsen",
    description=__doc__,
    thumbnail_url="custom_bokeh_model.png",
    documentation_url="",
    code_url="custom_bokeh_model/custom_bokeh_model.py",
    gif_url="",
    mp4_url="",
    tags=[
        "Code",
        "App In Gallery",
    ],
)
def view():
    """Run this to run the application"""
    slider = Slider(start=0, end=10, step=0.1, value=0, title="value")
    custom = Custom(text="Special Slider Display", slider=slider)
    layout = column(slider, custom, sizing_mode="stretch_width")

    pn.config.sizing_mode = "stretch_width"
    main = [site.get_intro_section(TITLE), pn.pane.Bokeh(layout)]
    pn.config.sizing_mode = "fixed"
    return site.get_template(title="Custom Model Model", main=main)


if __name__.startswith("bokeh"):
    view().servable()
