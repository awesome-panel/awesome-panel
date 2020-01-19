import pandas as pd
import panel as pn
import plotly.express as px

DATA = {
    "x": [1, 2, 3, 4,],
    "y": [2, 4, 6, 8,],
}
pn.extension("plotly")


def dataframe():
    return pd.DataFrame(DATA)


def chart():
    return px.line(dataframe(), x="x", y="y",)


def chart_fixed():
    return px.line(dataframe(), x="x", y="y", width=800, height=300,)


def chart_responsive_width():
    fig = chart()
    fig.update_layout(responsive=True)
    return fig


# def chart_responsive():
#     return chart().properties(width="container", height="container",)


def view():
    return pn.Column(
        chart(),
        chart_fixed(),
        chart_responsive_width(),
        # pn.Row(chart_responsive(), sizing_mode="stretch_width", height=400, background="pink"),
        sizing_mode="stretch_width",
        background="gray",
    )


view().servable()
