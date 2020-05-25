"""
# ECharts


[ECharts](https://www.echartsjs.com/en/index.html) is an open-sourced JavaScript
visualization tool, which can run fluently on PC and mobile devices.
It is compatible with most modern Web Browsers. Its also an **Apache incubator project**.
The library is very fast with a modern look and feel.

[Pyecharts](https://pyecharts.org/#/en-us/) is a Python api for using ECharts in Python
including Standalone, Flask, Django and Jupyter Notebooks.

Below we showcase an `ECharts` pane capable of showing Echarts dicts and Pyecharts objects
**enabling us to develop awesome analytics apps using the power of Echarts, Panel and Python**.

If you would like Panel to support WebComponents and ECharts then please upvote

- [Panel FR 1133](https://github.com/holoviz/panel/issues/1133) Add support for ECharts
- [Panel PR 1286](https://github.com/holoviz/panel/pull/1286) ECharts WebComponent Example
- [Panel PR 1252](https://github.com/holoviz/panel/pull/1252) Add WebComponent model and component

**Author:**
[Marc Skov Madsen](https://datamodelsanalytics.com) ([awesome-panel.org](https://awesome-panel.org))

**Tags:**
[Panel](https://panel.holoviz.org/),
[Echarts](https://www.echartsjs.com/en/index.html),
[PyeChart](https://pyecharts.org/#/en-us/),
[Pane](https://panel.holoviz.org/user_guide/Components.html),
[WebComponent](https://panel.holoviz.org/reference/panes/WebComponent.html),
[Python](https://www.python.org/)

**Resources:**
[Code](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/\
awesome_panel_express_tests/test_echarts.py),
[Echarts intro Video](https://www.youtube.com/watch?v=MF34Cgk5Rp0)
"""

import panel as pn
import param

from awesome_panel.express.components import ECharts
from awesome_panel.express.components.echarts import ECHART_JS_SERVER

BOUNDS = (0, 100)


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

        self.plot = ECharts(height=500)

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
                }
            ],
        }
        self.plot.echart = echart

    def view(self) -> pn.Column:
        """Returns the view of the application

        Returns:
            pn.Column: The view of the app
        """
        top_app_bar = pn.Row(
            pn.pane.PNG(
                "https://www.echartsjs.com/en/images/logo.png",
                sizing_mode="fixed",
                height=40,
                margin=(15, 0, 5, 25),
            ),
            pn.layout.VSpacer(),
            # pn.pane.PNG(
            #     "https://panel.holoviz.org/_static/logo_horizontal.png",
            #     sizing_mode="fixed",
            #     height=40,
            #     margin=(15, 0, 5, 25),
            # ),
            "",
            # pn.layout.VSpacer(),
            background="rgb(41, 60, 85)",
            height=70,
        )

        settings_pane = pn.Param(
            self,
            show_name=False,
            width=200,
            sizing_mode="stretch_height",
            background="rgb(245, 247, 250)",
        )

        return pn.Column(
            pn.pane.Markdown(__doc__),
            top_app_bar,
            pn.layout.HSpacer(height=50),
            pn.Row(self.plot, settings_pane,),
        )


def view():
    app = EchartsApp()
    return app.view()


if __name__.startswith("bokeh"):
    pn.config.js_files["echart"] = ECHART_JS_SERVER
    pn.config.sizing_mode = "stretch_width"
    app = EchartsApp()
    view = app.view().servable()
