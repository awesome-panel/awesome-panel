import pandas as pd
import panel as pn
import plotly.express as px

pn.config.raw_css.append(
    """
table {
    width: 100%;
}
"""
)
data = {
    "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
    "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
}
dataframe = pd.DataFrame(data)
pane = pn.Pane(dataframe, sizing_mode="stretch_width")
app = pn.Column(pane, sizing_mode="stretch_width")
app.servable()
