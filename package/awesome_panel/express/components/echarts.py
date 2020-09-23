"""
# ECharts


[ECharts](https://www.echartsjs.com/en/index.html) is an open-sourced JavaScript
visualization tool, which can run fluently on PC and mobile devices.
It is compatible with most modern Web Browsers. Its also an **Apache incubator project**.
The library is very fast with a modern look and feel.

[Pyecharts](https://pyecharts.org/#/en-us/) is a Python api for using ECharts in Python
including Standalone, Flask, Django and Jupyter Notebooks.

Below we develop an `ECharts` pane capable of showing Echarts dicts and Pyecharts objects
**enabling us to develop awesome analytics apps using the power of Echarts, Panel and Python**.

**Author:**
[Marc Skov Madsen](https://datamodelsanalytics.com) ([awesome-panel.org](https://awesome-panel.org))

**Tags:**
[Panel](https://panel.holoviz.org/)
[Echarts](https://www.echartsjs.com/en/index.html)
[PyeChart](https://pyecharts.org/#/en-us/)
[Pane](https://panel.holoviz.org/user_guide/Components.html)
[Python](https://www.python.org/)

**Resources:**
[Echarts intro Video](https://www.youtube.com/watch?v=MF34Cgk5Rp0)
"""

import json
import sys

import param

from awesome_panel.express.pane.web_component import WebComponent

# Configure and import js in Notebook
ECHART_JS_NOTEBOOK = "https://pyecharts.github.io/jupyter-echarts/echarts/echarts.min.js"
# Configure js for server
ECHART_JS_SERVER = "https://cdn.bootcss.com/echarts/3.7.2/echarts.min.js"

ECHARTS_HTML = """\
<div class="echart" style="width:100%;height:100%;"></div>
<script type="text/javascript">
    var myScript = document.currentScript;
    var myDiv = myScript.parentElement.firstElementChild;
    var myChart = echarts.init(myDiv);
    myDiv.eChart = myChart;
    Object.defineProperty(myDiv, 'option', {
        get: function() { return null; },
        set: function(val) { this.eChart.setOption(val); this.eChart.resize();}
    });
    myDiv.after_layout = myChart.resize; // Resizes the chart after layout of parent element
</script>"""


class ECharts(WebComponent):  # pylint: disable=too-few-public-methods
    """# ECharts

    [ECharts](https://www.echartsjs.com/en/index.html) is an open-sourced JavaScript
    visualization tool, which can run fluently on PC and mobile devices.
    It is compatible with most modern Web Browsers. Its also an **Apache incubator project**.
    The library is very fast with a modern look and feel.

    [Pyecharts](https://pyecharts.org/#/en-us/) is a Python api for using ECharts in Python
    including Standalone, Flask, Django and Jupyter Notebooks.

    Below we develop an `ECharts` pane capable of showing Echarts dicts and Pyecharts objects
    **enabling us to develop awesome analytics apps using the power of Echarts, Panel and
    Python**."""

    html = param.String(ECHARTS_HTML)
    properties_to_watch = param.Dict({"option": "option"})

    echart = param.Parameter()
    option = param.Dict()

    def __init__(self, **params):
        if "echart" in params:
            params["option"] = self._to_echart_dict(params["echart"])
        super().__init__(**params)

    @classmethod
    def _to_echart_dict(cls, echart):
        if isinstance(echart, dict):
            return echart
        if "pyecharts" in sys.modules:
            import pyecharts  # pylint: disable=import-outside-toplevel,import-error

            if isinstance(echart, pyecharts.charts.chart.Chart):
                return json.loads(echart.dump_options())

        return {}

    @param.depends("echart", watch=True)
    def _update(self):
        self.option = self._to_echart_dict(self.echart)
