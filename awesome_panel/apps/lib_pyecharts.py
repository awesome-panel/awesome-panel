"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including PyECharts. It supports both light and dark theme.
"""
import json

import panel as pn
from pyecharts.charts import Bar

from awesome_panel import config

config.extension("echarts", url="lib_pyecharts")

ACCENT = config.ACCENT

def get_plot(accent_base_color=ACCENT):
    """Returns a PyECharts plot"""
    bar_plot = (
        Bar()
        .add_xaxis(["Helicoptors", "Planes", "Air Ballons"])
        .add_yaxis("Total In Flight", [50, 75, 25], color=accent_base_color)
    )

    # Workaround to make plot responsive
    bar_plot = json.loads(bar_plot.dump_options())
    bar_plot["responsive"] = True
    return bar_plot


theme = config.get_theme()
plot = get_plot()
pn.pane.ECharts(plot, min_height=500, sizing_mode="stretch_both", theme=theme).servable()
