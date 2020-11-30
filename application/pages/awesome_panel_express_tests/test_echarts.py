"""[ECharts](https://www.echartsjs.com/en/index.html) is an open-sourced JavaScript
visualization tool, which can run fluently on PC and mobile devices. Its also an
**Apache incubator project**. The library is very fast with a modern look and feel.

[Pyecharts](https://pyecharts.org/#/en-us/) is a Python api for using ECharts in Python
including Standalone, Flask, Django and Jupyter Notebooks.

Checkout the [Echarts Gallery](https://echarts.apache.org/examples/en/index.html),
[Echarts intro Video](https://www.youtube.com/watch?v=MF34Cgk5Rp0) or the
[Panel Echarts Reference Guide](https://panel.holoviz.org/reference/panes/ECharts.html)
for more info.

Below we showcase an `ECharts` pane capable of showing Echarts dicts and Pyecharts objects
**enabling us to develop awesome analytics apps using the power of Echarts, Panel and Python**.
"""

import panel as pn
import param
from panel.pane import ECharts

from application.config import site

BOUNDS = (0, 100)
COLOR = "#E1477E"

APPLICATION = site.create_application(
    url="echarts",
    name="ECharts",
    author="Marc Skov Madsen",
    introduction="Demonstrates the look and feel of the Panel Echarts pane.",
    description=__doc__,
    thumbnail_url="test_echarts.png",
    documentation_url="",
    code_url="awesome_panel_express_tests/test_echarts.py",
    gif_url="",
    mp4_url="",
    tags=["ECharts", "PyECharts"],
)


class EchartsApp(param.Parameterized):
    """An Echarts app that showcases the Echart component"""

    title = param.String("Awesome Panel")
    plot_type = param.ObjectSelector("bar", objects=["bar", "scatter"], label="Plot Type")

    shirt = param.Integer(default=5, bounds=BOUNDS)
    cardign = param.Integer(default=20, bounds=BOUNDS)
    chiffon_shirt = param.Integer(default=36, bounds=BOUNDS)
    pants = param.Integer(default=10, bounds=BOUNDS)
    heels = param.Integer(default=10, bounds=BOUNDS)
    socks = param.Integer(default=20, bounds=BOUNDS)

    def __init__(self, **params):
        super().__init__(**params)

        self.plot = ECharts(height=500, min_width=200, sizing_mode="stretch_width")

        self._update_plot()

    @param.depends(
        "title",
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
            "title": {"text": self.title},
            "tooltip": {},
            "legend": {"data": ["Sales"]},
            "xAxis": {"data": ["shirt", "cardign", "chiffon shirt", "pants", "heels", "socks"]},
            "yAxis": {},
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
                    "itemStyle": {"color": "#A01346"},
                }
            ],
            "responsive": True,
        }
        self.plot.object = echart

    def view(self) -> pn.Column:
        """Returns the view of the application

        Returns:
            pn.Column: The view of the app
        """
        pn.config.sizing_mode = "stretch_width"
        pn.extension("echart")
        top_app_bar = pn.Row(
            pn.pane.PNG(
                "https://echarts.apache.org/en/images/logo.png",
                sizing_mode="fixed",
                height=40,
                margin=(15, 0, 5, 25),
                embed=False,
            ),
            pn.layout.VSpacer(),
            "",
            background="rgb(41, 60, 85)",
            height=70,
        )

        settings_pane = pn.Param(
            self,
            show_name=False,
            width=200,
            sizing_mode="fixed",
            background="rgb(245, 247, 250)",
        )

        main = [
            APPLICATION.intro_section(),
            pn.Column(
                top_app_bar,
                pn.layout.HSpacer(height=50),
                pn.Row(self.plot, settings_pane, sizing_mode="stretch_width"),
            ),
        ]
        return site.create_template(title="Test ECharts", theme="default", main=main)


@site.add(APPLICATION)
def view():
    return EchartsApp().view()


if __name__.startswith("bokeh"):
    view().servable()
