"""One Super Power of Panel is that its actually extensible.

You can write custom Panes, Layouts and Widgets just the way that Panel is built.

The starting point is the implementation of a Custom Bokeh Model which is described in
[Extending Bokeh](https://docs.bokeh.org/en/latest/docs/user_guide/extensions.html).

But I've not been able to follow the Bokeh User Guide as it seems out of date. See
[Bokeh Issue 9587](https://github.com/bokeh/bokeh/issues/9587).

It seems **the api of Custom Bokeh Models is changing** towards Bokeh v. 2.0.

The best starting point for Custom Bokeh Models is to get inspiration from

- [Bokeh Python Models](https://github.com/bokeh/bokeh/tree/master/bokeh/models)
- [Bokeh TypeScript Models]\
    (https://github.com/bokeh/bokeh/tree/master/bokehjs/application/lib/models)
- [Panel Models](https://github.com/holoviz/panel/tree/master/panel/models)

With some help I succeeded in creating the below Bokeh Custom Model.

Please note you need to instantiate the Custom Model before you run `.servable()` in order to get
it compiled.
"""

import pathlib

import panel as pn
from bokeh.core.properties import Instance, String
from bokeh.layouts import column
from bokeh.models import HTMLBox, Slider

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

    return pn.Column(__doc__, pn.pane.Bokeh(layout), width=500)


if __name__.startswith("bokeh"):
    view().servable()
