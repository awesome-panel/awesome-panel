"""Streaming is something that Panel supports really well

This application demonstrates how to use
[Streamz](https://streamz.readthedocs.io/en/latest/),
[Pandas](https://pandas.pydata.org/),
[Bokeh](https://docs.bokeh.org/en/latest/index.html),
[Holoviews](https://holoviews.org/),
[Altair](https://altair-viz.github.io/),
[Echart](https://echarts.apache.org/en/index.html) and
[Plotly](https://plotly.com/) for streaming.

The stream will STOP AFTER 1 MINUTE.
"""
from datetime import datetime

import altair as alt
import hvplot.pandas  # pylint: disable=unused-import
import numpy as np
import pandas as pd
import panel as pn
import plotly.express as px
from streamz.dataframe import DataFrame as sDataFrame

from application.config import site

alt.themes.enable("dark")

APPLICATION = site.create_application(
    url="streaming-plots",
    name="Streaming Plots",
    author="Marc Skov Madsen",
    introduction="Demonstrates Streaming with Panel",
    description=__doc__,
    thumbnail_url="streaming-plots.png",
    documentation_url="",
    code_url="streaming_plots/streaming_plots.py",
    gif_url="streaming-plots.gif",
    mp4_url="streaming-plots.mp4",
    tags=[
        "Streaming",
        "Streamz",
    ],
)


def _create_echarts(data):
    data = data.sort_index()
    return {
        "xAxis": {"type": "time"},
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": list(zip(list(data.index.values), list(data["y"]))),
                "type": "line",
                "showSymbol": False,
                "hoverAnimation": False,
            },
        ],
        "responsive": True,
    }


def _create_altair(data):
    data = data.reset_index()
    return (
        alt.Chart(data, height="container", width="container")
        .mark_line()
        .encode(
            x="index",
            y="y",
        )
    )


def _create_hvplot(data):
    # Hack:
    # hv.renderer("bokeh").theme = pn.template.react.DarkTheme.param.bokeh_theme.default
    return data.hvplot(y="y").opts(default_tools=[])


def _create_plotly(data):
    plot = px.line(data, y="y", height=310, template="plotly_dark")
    plot.layout.autosize = True
    plot.layout.plot_bgcolor = "#2a2a2a"
    plot.layout.paper_bgcolor = "#2a2a2a"
    plot.layout.xaxis.tickformat = "%H:%M:%S"
    return plot


# def _create_matplotlib(data):
#     data = pd.concat(data).reset_index()
#     plt.close('all')
#     fig = plt.Figure(figsize=(8, 6))
#     ax0 = fig.subplots()
#     data.plot(ax=ax0, x="index", y="y")
#     matplotlib_pane.object = fig
#     return fig


@site.add(APPLICATION)
def view():
    """Returns an instance of the Streaming Plots app"""
    pn.config.sizing_mode = "stretch_width"
    echart_pane = pn.pane.ECharts(theme="dark", sizing_mode="stretch_both")
    plotly_pane = pn.pane.Plotly(sizing_mode="stretch_both", config={"responsive": True})
    hvplot_pane = pn.pane.HoloViews(sizing_mode="stretch_both")
    altair_pane = pn.pane.Vega(sizing_mode="stretch_both")

    df_stream = sDataFrame(example=pd.DataFrame({"y": []}, index=pd.DatetimeIndex([])))
    df_window_stream = df_stream.cumsum().stream.sliding_window(50).map(pd.concat)

    def update_echarts(data):
        echart_pane.object = _create_echarts(data)

    def update_plotly(data):
        plotly_pane.object = _create_plotly(data)

    def update_altair(data):
        altair_pane.object = _create_altair(data)

    def update_hvplot(data):
        hvplot_pane.object = _create_hvplot(data)

    df_window_stream.sink(update_echarts)
    df_window_stream.sink(update_plotly)
    df_window_stream.sink(update_altair)
    df_window_stream.sink(update_hvplot)

    def emit():
        df_stream.emit(
            pd.DataFrame({"y": [np.random.randn()]}, index=pd.DatetimeIndex([datetime.utcnow()]))
        )

    emit()
    pn.state.add_periodic_callback(emit, period=250, count=240)  # Will stream for 1 mins

    layout = site.create_template(
        template="react",
        theme="dark",
        main_max_width="",
        row_height=100,
    )
    site_intro = APPLICATION.intro_section()
    layout.main[0:3, 0:6] = site_intro
    layout.main[3:7, 0:6] = pn.layout.Card(
        hvplot_pane, header="BOKEH via HOLOVIEWS", sizing_mode="stretch_both"
    )
    layout.main[3:7, 6:12] = pn.layout.Card(
        altair_pane, header="VEGA via ALTAIR", sizing_mode="stretch_both"
    )
    layout.main[7:11, 0:6] = pn.layout.Card(
        plotly_pane, header="PLOTLY", sizing_mode="stretch_both"
    )
    layout.main[7:11, 6:12] = pn.layout.Card(
        echart_pane, header="ECHART", sizing_mode="stretch_both"
    )
    return layout


if __name__.startswith("bokeh"):
    view().servable()
