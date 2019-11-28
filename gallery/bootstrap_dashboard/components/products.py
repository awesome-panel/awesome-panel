"""In module file we define the Products page"""
import panel as pn
import pandas as pd
import plotly.express as px
import holoviews as hv


class Products(pn.Column):
    def view(self, name="Products"):
        self.chart_data = self._chart_data()
        self.table_data = self._table_data()
        self.chart = self._chart()
        self.table = self._table()

        return pn.Column(
            pn.pane.Markdown("## Products"),
            self.chart,
            pn.pane.Markdown("## Section Title"),
            self.table,
            sizing_mode="stretch_width",
            name=name,
        )

    def _chart_data(self):
        chart_data = {
            "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
            "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
        }
        return pd.DataFrame(chart_data)

    def _chart(self):
        fig = px.line(self._chart_data(), x="Day", y="Orders")
        fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
        fig.layout.autosize = True
        fig.layout.paper_bgcolor = "rgba(0,0,0,0)"
        fig.layout.plot_bgcolor = "rgba(0,0,0,0)"
        return pn.pane.Plotly(fig)

    def _table_data(self):
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
        return pd.DataFrame(
            table_data, columns=["#", "Header", "Header", "Header", "Header"]
        ).set_index("#")

    def _table(self):
        return pn.Row(self.table_data, sizing_mode="stretch_width")

