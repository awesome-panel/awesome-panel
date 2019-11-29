from plotly import express as px
from gallery.bootstrap_dashboard import services
import panel as pn


def plotly_view():
    fig = px.line(services.get_chart_data(), x="Day", y="Orders")
    fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
    fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
    fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
    fig.layout.width = 1000
    fig.layout.autosize = True
    return pn.Column(
        "# Plotly",
        pn.Row(pn.layout.HSpacer(), fig, pn.layout.HSpacer(),),
        "Plotly cannot currently autosize to full width and be responsive",
        sizing_mode="stretch_width",
        name="Plotly",
    )

