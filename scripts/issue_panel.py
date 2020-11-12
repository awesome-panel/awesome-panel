import altair as alt
import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn
import plotly.express as px
from streamz.dataframe import DataFrame as sDataFrame

plotly_pane = pn.pane.Plotly(sizing_mode="stretch_both", config={"responsive": True})


def update_plotly(data):
    data = pd.concat(data).reset_index()
    plot = px.line(data, y="y", title="Plotly", template="plotly_dark")
    plot.layout.autosize = True
    plotly_pane.object = plot


df = sDataFrame(example=pd.DataFrame({"y": []}, index=pd.DatetimeIndex([])))
window_stream = df.cumsum().stream.sliding_window(50)

plotly_sink = window_stream.sink(update_plotly)


def emit():
    df.emit(pd.DataFrame({"y": [np.random.randn()]}, index=pd.DatetimeIndex([pd.datetime.now()])))


emit()
pn.state.add_periodic_callback(emit, period=100, count=500)

layout = pn.template.ReactTemplate(
    site="Awesome Panel",
    title="Streaming w. Echarts",
    theme=pn.template.react.DarkTheme,
    row_height=200,
)
layout.main[0:2, 0:6] = pn.layout.Card(plotly_pane, header="PLOTLY", sizing_mode="stretch_both")
layout.servable()
