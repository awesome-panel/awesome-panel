"""
The purpose of this app is to demonstrate that Panel works with the tools you know and love
&#10084;&#65039;, including Altair. It supports both light and dark theme.
"""
import altair as alt
import panel as pn
from vega_datasets import data

from awesome_panel import config

config.extension("vega", url="lib_altair")


def get_plot(theme="default"):
    """Returns an Altair plot"""
    if theme == "dark":
        alt.themes.enable("dark")
    else:
        alt.themes.enable("default")

    return (
        alt.Chart(data.cars())
        .mark_circle(size=60)
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        )
        .properties(
            height="container",
            width="container",
        )
        .interactive()
    )


plot = get_plot(theme=config.get_theme())

pn.pane.Vega(plot, height=500, sizing_mode="stretch_both").servable()
