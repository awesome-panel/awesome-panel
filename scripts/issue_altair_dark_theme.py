import altair as alt
import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn
from altair.vegalite.v4.schema.core import Data
from streamz.dataframe import DataFrame as sDataFrame

df = sDataFrame(example=pd.DataFrame({"y": []}, index=pd.DatetimeIndex([])))

plot_pane1 = pn.pane.ECharts(theme="dark", sizing_mode="stretch_both")
plot_pane2 = pn.pane.ECharts(theme="dark", sizing_mode="stretch_both")
hvplot_pane = pn.pane.HoloViews(sizing_mode="stretch_both")

alt.themes.enable("dark")
altair_pane = pn.pane.Vega(sizing_mode="stretch_both")


def update_echarts(data):
    data = pd.concat(data).reset_index()
    plot = {
        "xAxis": {"type": "category", "data": list(data.index.values)},
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": list(data["y"]),
                "type": "line",
                "showSymbol": False,
                "hoverAnimation": False,
            },
        ],
        "responsive": True,
    }
    plot_pane1.object = plot
    plot_pane2.object = plot


def update_altair(data):
    data = pd.concat(data).reset_index()
    plot = (
        alt.Chart(data, height="container", width="container")
        .mark_line()
        .encode(
            x="index",
            y="y",
        )
    )
    altair_pane.object = plot


def update_hvplot(data):
    data = pd.concat(data).reset_index()
    plot = data.hvplot(y="y")
    hvplot_pane.object = plot


window_stream = df.cumsum().stream.sliding_window(50)
echarts_sink = window_stream.sink(update_echarts)
altair_sink = window_stream.sink(update_altair)
hvplot_sink = window_stream.sink(update_hvplot)


def emit():
    df.emit(pd.DataFrame({"y": [np.random.randn()]}, index=pd.DatetimeIndex([pd.datetime.now()])))


pn.state.add_periodic_callback(emit, period=100, count=500)

layout = pn.template.ReactTemplate(
    site="Awesome Panel",
    title="Streaming w. Echarts",
    theme=pn.template.react.DarkTheme,
    row_height=200,
)
layout.main[0:2, 0:6] = plot_pane1
layout.main[0:2, 6:12] = plot_pane2
layout.main[2:4, 0:6] = pn.layout.Card(
    hvplot_pane, header="HOLOVIEWS/ BOKEH", sizing_mode="stretch_both"
)
layout.main[2:4, 6:12] = pn.layout.Card(altair_pane, header="ALTAIR", sizing_mode="stretch_both")
layout.servable()
