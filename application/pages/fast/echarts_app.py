"""ECharts App used to show case the Fast Templates"""
import panel as pn
import param
from panel.pane import ECharts

BOUNDS = (0, 100)


class EchartsApp(param.Parameterized):
    """An Echarts app that showcases the Echart component"""

    plot_type = param.ObjectSelector("bar", objects=["bar", "scatter"], label="Plot Type")

    shirt = param.Integer(default=5, bounds=BOUNDS)
    cardign = param.Integer(default=20, bounds=BOUNDS)
    chiffon_shirt = param.Integer(default=36, bounds=BOUNDS)
    pants = param.Integer(default=10, bounds=BOUNDS)
    heels = param.Integer(default=10, bounds=BOUNDS)
    socks = param.Integer(default=20, bounds=BOUNDS)

    def __init__(self, **params):
        super().__init__(**params)

        self.plot = ECharts(min_height=100, min_width=200, sizing_mode="stretch_both")

        self._update_plot()

    @param.depends(
        "plot_type",
        "shirt",
        "cardign",
        "chiffon_shirt",
        "pants",
        "heels",
        "socks",
        watch=True,
    )
    def _update_plot(self):
        echart = {
            "tooltip": {},
            "legend": {"data": ["Sales"]},
            "xAxis": {
                "data": ["shirt", "cardign", "chiffon shirt", "pants", "heels", "socks"],
                "axisLine": {"lineStyle": {"color": "#ccc"}},
            },
            "yAxis": {
                "axisLine": {"lineStyle": {"color": "#ccc"}},
            },
            "series": [
                {
                    "name": "Sales",
                    "type": self.plot_type,
                    "data": [
                        self.shirt,
                        self.cardign,
                        self.chiffon_shirt,
                        self.pants,
                        self.heels,
                        self.socks,
                    ],
                    "itemStyle": {"color": "#DF3874"},  # '#660C2D' # #86103B;
                }
            ],
            "responsive": True,
        }
        text_style = {"color": "#ccc"}
        update = ["legend", "xAxis", "yAxis"]
        for upd in update:
            echart[upd]["textStyle"] = text_style
        self.plot.object = echart

    def view(self) -> pn.Column:
        """Returns the view of the application

        Returns:
            pn.Column: The view of the app
        """
        settings_pane = pn.Param(
            self,
            show_name=False,
            width=200,
            sizing_mode="fixed",
        )

        return pn.Column(
            pn.pane.Markdown("## Echarts Plot"),
            pn.Row(settings_pane, self.plot, sizing_mode="stretch_both"),
        )
