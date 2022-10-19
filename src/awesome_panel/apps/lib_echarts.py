"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including ECharts. It supports both light and dark theme.
"""
import panel as pn

from awesome_panel import config

config.extension("echarts", url="lib_echarts")


def get_plot():
    """Returns an ECharts plot"""
    return {
        "xAxis": {"data": ["2017-10-24", "2017-10-25", "2017-10-26", "2017-10-27"]},
        "yAxis": {},
        "series": [
            {
                "type": "k",
                "data": [
                    [20, 34, 10, 38],
                    [40, 35, 30, 50],
                    [31, 38, 33, 44],
                    [38, 15, 5, 42],
                ],
            }
        ],
        "responsive": True,
    }


plot = get_plot()
pn.pane.ECharts(plot, min_height=700, sizing_mode="stretch_both").servable()
