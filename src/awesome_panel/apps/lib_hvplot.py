"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including hvplot. It supports both light and dark theme.
"""
import hvplot.pandas  # pylint: disable=unused-import
import panel as pn
from bokeh.sampledata.sprint import sprint

from awesome_panel import config

config.extension(url="lib_hvplot")


def get_plot():
    """Returns a hvplot plot"""
    return sprint.hvplot.violin(
        y="Time",
        by="Medal",
        c="Medal",
        ylabel="Sprint Time",
        cmap=["gold", "silver", "brown"],
        legend=False,
        responsive=True,
        padding=0.4,
    )


plot = get_plot()

pn.pane.HoloViews(plot, height=500, sizing_mode="stretch_both").servable()
