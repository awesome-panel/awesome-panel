"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including HoloViews. It supports both light and dark theme.
"""
import holoviews as hv
import numpy as np
import panel as pn
from holoviews import opts, streams
from holoviews.plotting.links import DataLink

from awesome_panel import config

config.extension(url="lib_holoviews")

THEME = config.get_theme()
ACCENT = config.ACCENT


def get_plot(theme="default", accent_base_color=ACCENT):
    """Returns a HoloViews plot"""
    curve = hv.Curve(np.random.randn(10).cumsum()).opts(
        min_height=600,
        responsive=True,
        line_width=6,
        color=accent_base_color,
        # https://github.com/holoviz/holoviews/issues/5058
        # active_tools=["point_draw"]
    )
    if theme == "default":
        point_color = "black"
    else:
        point_color = "#E5E5E5"

    streams.CurveEdit(data=curve.columns(), source=curve, style={"color": point_color, "size": 10})

    table = hv.Table(curve).opts(editable=True)
    DataLink(curve, table)

    return (curve + table).opts(
        opts.Table(editable=True),
    )


plot = get_plot(THEME, ACCENT)
pn.pane.HoloViews(plot, height=600, sizing_mode="stretch_both").servable()
