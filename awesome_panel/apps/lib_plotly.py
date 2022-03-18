"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Plotly. It supports both light and dark theme.
"""
import pandas as pd
import panel as pn
import plotly.express as px

from awesome_panel import config

config.extension("plotly", url="lib_plotly")

ACCENT = config.ACCENT
THEME = config.get_theme()
JSON_THEME = config.get_json_theme()


def get_plot(theme=THEME, accent_base_color=ACCENT):
    """Returns a Plotly Figure"""
    data = pd.DataFrame(
        [
            ("Monday", 7),
            ("Tuesday", 4),
            ("Wednesday", 9),
            ("Thursday", 4),
            ("Friday", 4),
            ("Saturday", 4),
            ("Sunday", 4),
        ],
        columns=["Day", "Orders"],
    )

    if theme == "dark":
        plotly_template = "plotly_dark"
    else:
        plotly_template = "plotly"

    fig = px.line(
        data,
        x="Day",
        y="Orders",
        template=plotly_template,
        color_discrete_sequence=(accent_base_color,),
    )
    fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
    fig.layout.autosize = True
    return fig


plot = get_plot()

plotly_pane = pn.pane.Plotly(
    plot, config={"responsive": True}, sizing_mode="stretch_both", height=700
).servable()


def hover_data(value, theme=JSON_THEME):
    """Returns the hover data"""
    if not value:
        value = {}
    return pn.pane.JSON(value, theme=theme, name="Hover Data", depth=3, height=200)


pn.Column(
    "## Hover data",
    pn.bind(hover_data, plotly_pane.param.hover_data),
).servable()
