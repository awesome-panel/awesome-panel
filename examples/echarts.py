"""ECharts App used to show case the Fast Templates"""
import panel as pn
import param
from panel.pane import ECharts

from awesome_panel import config

BOUNDS = (0, 100)

ACCENT = config.ACCENT


class EchartsApp(pn.viewable.Viewer):
    """An Echarts app that showcases the Echart component"""

    plot_type = param.ObjectSelector("bar", objects=["bar", "scatter"], label="Plot Type")

    shirt = param.Integer(default=5, bounds=BOUNDS)
    cardign = param.Integer(default=20, bounds=BOUNDS)
    chiffon_shirt = param.Integer(default=36, bounds=BOUNDS)
    pants = param.Integer(default=10, bounds=BOUNDS)
    heels = param.Integer(default=10, bounds=BOUNDS)
    socks = param.Integer(default=20, bounds=BOUNDS)
    accent = param.Color(default=ACCENT, precedence=-1)

    def __init__(self, **params):
        super().__init__(**params)

        self.plot = ECharts(min_height=100, min_width=200, sizing_mode="stretch_both")

        self._update_plot()

        self._layout = self._get_layout()

    def __panel__(self):
        return self._layout

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
        dark_theme = pn.state.location.query_params.get("theme", "") == "dark"
        color = "#CCCCCC" if dark_theme else "#000000"

        echart = {
            "tooltip": {},
            "legend": {"data": ["Sales"]},
            "xAxis": {
                "data": ["shirt", "cardign", "chiffon shirt", "pants", "heels", "socks"],
                "axisLine": {"lineStyle": {"color": color}},
            },
            "yAxis": {
                "axisLine": {"lineStyle": {"color": color}},
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
                    "itemStyle": {"color": self.accent},  # '#660C2D' # #86103B;
                }
            ],
            "responsive": True,
        }
        text_style = {"color": color}
        update = ["legend", "xAxis", "yAxis"]
        for upd in update:
            echart[upd]["textStyle"] = text_style
        self.plot.object = echart

    def _get_layout(self) -> pn.Column:
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
            sizing_mode="stretch_both",
        )


if __name__.startswith("bokeh"):
    config.extension(url="echarts")

    EchartsApp().servable()
