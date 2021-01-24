import bokeh as bk
import pandas as pd
import panel as pn
from bokeh.models.formatters import DatetimeTickFormatter

data = {
    "x": [pd.Timestamp("2020-01-01"), pd.Timestamp("2020-01-02"), pd.Timestamp("2020-01-03")],
    "y": [2, 4, 5],
}
XFORMATTER = DatetimeTickFormatter(days=["%m %d, %Y"], hours=["%Y-%m-%d %H:%M"])
s1 = bk.plotting.figure(plot_width=500, plot_height=250, title=None)
s1.scatter(source=data)
s1.xaxis.formatter = XFORMATTER
s2 = bk.plotting.figure(plot_width=500, plot_height=250, title=None, x_range=s1.x_range)
s2.vbar(
    x="x",
    top="y",
    bottom=0,
    source=data,
)
s2.xaxis.formatter = XFORMATTER

p = bk.layouts.gridplot([[s1], [s2]])


pn.Column(p).servable()
