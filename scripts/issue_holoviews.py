import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn
from streamz.dataframe import DataFrame as sDataFrame

hvplot_pane = pn.pane.HoloViews(sizing_mode="stretch_both")


def update_hvplot(data):
    data = pd.concat(data).reset_index()
    plot = data.hvplot(y="y")
    hvplot_pane.object = plot


df = sDataFrame(example=pd.DataFrame({"y": []}, index=pd.DatetimeIndex([])))
window_stream = df.cumsum().stream.sliding_window(50)

hvplot_sink = window_stream.sink(update_hvplot)


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
layout.main[0, 0:6] = pn.layout.Card(
    hvplot_pane, header="HOLOVIEWS/ BOKEH", sizing_mode="stretch_both"
)
layout.servable()
