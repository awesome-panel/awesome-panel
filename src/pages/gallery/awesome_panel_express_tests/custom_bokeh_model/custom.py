"""One Super Power of Panel is that its actually extensible.

You can write custom Panes, Layouts and Widgets just the way that Panel is built. The starting point
is [Extending Bokeh](https://docs.bokeh.org/en/latest/docs/user_guide/extensions.html)
"""

import panel as pn
from bokeh.core.properties import Instance, String
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.models import HTMLBox, Slider

pn.extension()


class Custom(HTMLBox):

    __implementation__ = "custom.ts"

    text = String(default="Custom text")

    slider = Instance(Slider)


slider = Slider(start=0, end=10, step=0.1, value=0, title="value")

custom = Custom(text="Special Slider Display", slider=slider)

layout = column(slider, custom)


app = pn.pane.Bokeh(layout)
app.servable()
