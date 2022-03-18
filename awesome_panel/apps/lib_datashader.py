"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Datashader. It supports both light and dark theme.
"""
import hvplot.xarray  # pylint: disable=unused-import
import panel as pn
import xarray as xr

from awesome_panel import config

config.extension(url="lib_datashader")

ACCENT = config.ACCENT

if not "air" in pn.state.cache:
    air = pn.state.cache["air"] = xr.tutorial.open_dataset("air_temperature").load().air
else:
    air = pn.state.cache["air"]


def get_plot(accent_base_color=ACCENT):
    """Returns a datashaded hvplot"""
    plot = air.hvplot.scatter(
        "time",
        groupby=[],
        rasterize=True,
        dynspread=True,
        responsive=True,
        cmap="YlOrBr",
        colorbar=True,
    ) * air.mean(["lat", "lon"]).hvplot.line("time", color=accent_base_color, responsive=True)
    plot.opts(responsive=True, active_tools=["box_zoom"])
    return plot


PLOT = get_plot()

pn.pane.HoloViews(PLOT, min_height=500, sizing_mode="stretch_both").servable()
