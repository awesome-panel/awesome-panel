import hvplot.pandas
import pandas as pd
import panel as pn
import param

data = {
    "obs": [1, 2, 3, 4, 5, 6, 7, 8],
    "label": ["a", "b", "a", "b", "a", "b", "a", "b"],
    "gene_identifier": ["1", "1", "2", "2", "2", "2", "1", "1"],
    "value": [1, 2, 2, 4, 7, 6, 9, 8],
}
des = pd.DataFrame(data)
gene_list = list(des["gene_identifier"].unique())
comparison_list = list(des["label"].unique())


class VolcanoPlots(param.Parameterized):
    comparison = param.Selector(objects=comparison_list)
    genes = param.Selector(objects=gene_list)

    source_data = param.DataFrame()
    transform_data = param.DataFrame()

    def __init__(self, **params):
        super().__init__(**params)

        self._plot_pane = pn.pane.HoloViews()
        self._selections_pane = pn.Param(self, parameters=["comparison", "genes"])
        self._table_pane = pn.pane.DataFrame(width=1000, max_rows=25)

        self._update()

    @param.depends("comparison", "genes", watch=True)
    def _update(self):
        source_data = self.source_data
        sub = source_data[source_data.label == self.comparison]
        sub = sub[sub.gene_identifier == self.genes]
        self.transform_data = sub

    @param.depends("transform_data", watch=True)
    def _update_plot(self):
        self._plot_pane.object = self.transform_data.hvplot.scatter(x="obs", y="value")

    @param.depends("transform_data", watch=True)
    def _update_table(self):
        self._table_pane.object = self.transform_data

    def panel(self):
        return pn.Column(pn.Row(self._selections_pane, self._plot_pane), self._table_pane)


obj = VolcanoPlots(source_data=des).panel().servable()
