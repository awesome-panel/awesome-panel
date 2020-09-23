import pandas as pd
import panel as pn
import plotly.express as px

chart_data = {
    "Day": [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ],
    "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
}
fig = px.line(chart_data, x="Day", y="Orders")
fig.layout.autosize = True
plot = pn.pane.Plotly(fig, config={"responsive": True})
app = pn.Column(plot, sizing_mode="stretch_width", background="gray")
app.servable()
