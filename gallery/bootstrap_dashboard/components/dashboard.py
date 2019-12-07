import pandas as pd
import plotly.express as px

import awesome_panel.express as pnx
import panel as pn
from gallery.bootstrap_dashboard.components.core import holoviews_chart
from gallery.bootstrap_dashboard import services


class Dashboard:
    def __init__(self):
        pn.config.raw_css.append(
            """
        table {
            width: 95%;
        }
        """
        )

    def _chart_plotly(self):
        fig = px.line(services.get_chart_data(), x="Day", y="Orders")
        fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
        fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
        fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
        fig.layout.autosize = True
        return pn.Pane(fig, sizing_mode="stretch_width")

    def _table_pane_dataframe(self):
        return pn.Pane(services.get_table_data(), sizing_mode="stretch_width")

    def _table_widget_dataframe(self):
        return pn.widgets.DataFrame(self.table_data, sizing_mode="stretch_width")

    def view(self, name="Dashboard"):
        return pn.Column(
            pnx.Title("Dashboard"),
            pnx.Divider(),
            holoviews_chart(),
            pnx.Title("Section Title"),
            pnx.Divider(),
            self._table_pane_dataframe(),
            sizing_mode="stretch_width",
            name=name,
        )


if __name__.startswith("bk"):
    Dashboard().view().servable("column")
