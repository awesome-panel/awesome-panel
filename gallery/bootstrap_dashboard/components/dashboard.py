from typing import List, NamedTuple

import pandas as pd
import plotly.express as px

import panel as pn

class Dashboard:
    def __init__(self):
        pn.config.raw_css.append(
            """
        table {
            width: 95%;
        }
        """
        )
        chart_data = {
            "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
            "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
        }
        self.chart_data = pd.DataFrame(chart_data)

        table_data = [
            (1001, "Lorem", "ipsum", "dolor", "sit"),
            (1002, "amet", "consectetur", "adipiscing", "elit"),
            (1003, "Integer", "nec", "odio", "Praesent"),
            (1003, "libero", "Sed", "cursus", "ante"),
            (1004, "dapibus", "diam", "Sed", "nisi"),
            (1005, "Nulla", "quis", "sem", "at"),
            (1006, "nibh", "elementum", "imperdiet", "Duis"),
            (1007, "sagittis", "ipsum", "Praesent", "mauris"),
            (1008, "Fusce", "nec", "tellus", "sed"),
            (1009, "augue", "semper", "porta", "Mauris"),
            (1010, "massa", "Vestibulum", "lacinia", "arcu"),
            (1011, "eget", "nulla", "Class", "aptent"),
            (1012, "taciti", "sociosqu", "ad", "litora"),
            (1013, "torquent", "per", "conubia", "nostra"),
            (1014, "per", "inceptos", "himenaeos", "Curabitur"),
            (1015, "sodales", "ligula", "in", "libero"),
        ]
        self.table_data = pd.DataFrame(
            table_data, columns=["Header0", "Header1", "Header2", "Header3", "Header4"]
        ).set_index("Header0")

    def _chart_plotly(self):
        fig = px.line(self.chart_data, x="Day", y="Orders")
        fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
        fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
        fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
        fig.layout.autosize = True
        return pn.Pane(fig, sizing_mode="stretch_width")

    def _table_pane_dataframe(self):
        return pn.Pane(self.table_data, sizing_mode="stretch_width")

    def _table_widget_dataframe(self):
        return pn.widgets.DataFrame(self.table_data, sizing_mode="stretch_width")

    def view(self, name="Dashboard"):
        return pn.Column(
            pn.pane.Markdown("## Plot - Plotly"),
            self._chart_plotly(),
            pn.pane.Markdown("## Table - pane.DataFrame"),
            self._table_pane_dataframe(),
            pn.pane.Markdown("## Table - widget.DataFrame"),
            self._table_widget_dataframe(),
            sizing_mode="stretch_width",
            name=name,
        )


if __name__.startswith("bk"):
    Dashboard().view().servable("column")
