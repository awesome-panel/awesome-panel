import holoviews as hv
import hvplot.pandas
import pandas as pd
import panel as pn
import param
from plotly import express as px

pn.extension("plotly")  # Hack: See https://github.com/holoviz/panel/issues/840


def navigation_button(
    page, page_outlet,
):
    button = pn.widgets.Button(name=page.name)

    def navigate_to_page(event,):
        page_outlet.clear()
        page_outlet.append(page)

    button.on_click(navigate_to_page)
    return button


def get_chart_data():
    chart_data = {
        "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
        "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034,],
    }
    return pd.DataFrame(chart_data)


def holoviews_fig():
    data = get_chart_data()
    line_plot = data.hvplot.line(
        x="Day", y="Orders", width=None, line_color="#007BFF", line_width=6,
    )
    scatter_plot = data.hvplot.scatter(x="Day", y="Orders", width=None,).opts(
        marker="o", size=10, color="#007BFF",
    )
    fig = line_plot * scatter_plot
    gridstyle = {
        "grid_line_color": "black",
        "grid_line_width": 0.1,
    }
    fig.height = 500
    fig = fig.opts(
        responsive=True,
        toolbar=None,
        yticks=list(range(12000, 26000, 2000,)),
        ylim=(12000, 26000,),
        gridstyle=gridstyle,
        show_grid=True,
    )
    return fig


def holoviews_page() -> pn.Column:
    fig = holoviews_fig()
    return pn.Column(
        pn.pane.Markdown("# Holoviews"), fig, name="Holoviews", sizing_mode="stretch_both",
    )


def plotly_fig():
    fig = px.line(get_chart_data(), x="Day", y="Orders",)
    fig.update_traces(
        mode="lines+markers", marker=dict(size=10), line=dict(width=4),
    )
    fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
    fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
    fig.layout.width = 1000
    return fig


def plotly_page(*args, **kwargs) -> pn.Column:
    fig = plotly_fig()
    return pn.Column(pn.pane.Markdown("# Plotly"), fig, name="Plotly", sizing_mode="stretch_both",)


def main():
    issue = """# Issue

I can't see any difference in the Panel specific implementation of the Plotly and Holoviews pages.
Still only the Holoviews page shows! The Plotly page does not!"""
    home = pn.pane.Markdown(issue, name="Issue",)
    holoviews = holoviews_page()
    plotly = plotly_page()

    page_outlet = pn.Column(home, sizing_mode="stretch_both",)
    sidebar = pn.Column(
        navigation_button(home, page_outlet,),
        navigation_button(plotly, page_outlet,),
        navigation_button(holoviews, page_outlet,),
        pn.layout.HSpacer(),
        width=300,
        sizing_mode="stretch_height",
        background="lightgray",
    )
    app = pn.Row(sidebar, page_outlet, sizing_mode="stretch_both",)
    return app


if __name__.startswith("bokeh"):
    main().servable("issue")
    # plotly_page().servable("plotly_page stand alone works!")
