"""[Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) provides profile reports
from Pandas DataFrames. I hope this provides you with an impression of how this can be integrated
in a [Panel](https://panel.holoviz.org/) context.

This app was originally created as a response to this [question on Discourse]\
(https://discourse.holoviz.org/t/cant-display-pandas-profiling-report/760/2).

This app is restricted to profile a **maximum of 200 rows** to minimize the impact on the server.

For more information take a look at the [Pandas Profiling Examples]\
(https://pandas-profiling.github.io/pandas-profiling/docs/master/\
rtd/pages/examples.html#showcasing-specific-features)."""
import html
from functools import lru_cache
from itertools import cycle

import pandas as pd
import panel as pn
import param
from pandas_profiling import ProfileReport
from panel.io.loading import start_loading_spinner, stop_loading_spinner

from awesome_panel import config

# pylint: disable=line-too-long
DEFAULT_TITLE = "Pandas Profiling Report"
EMPTY_HTML_REPORT = "<p>Click a button to generate a report</p>"
HTML_CREATING_REPORT = "<p>Creating Report ...</p>"
CSV_URLS = [
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/awesome_panel/assets/csv/perspective_viewer_data.csv",
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/awesome_panel/assets/csv/global_power_plant_database.csv",
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/awesome_panel/assets/csv/kickstarter_dashboard.csv",
]
GREEN = "#174c4f"
ORANGE = "#cc5c29"
LOGO_URL = "https://raw.githubusercontent.com/awesome-panel/awesome-panel-assets/93abd7c923c1435918461823411cee7807e63fe0/images/pandas-profiling_logo.png"
MAX_ROWS = 200
# pylint: enable=line-too-long

STYLE = """
<style>
.app-bar {
    color: #cc5c29;
}
.bk-root .id-random-report-button button {
    background-color: #cc5c29;
    border-color: #cc5c29;
    font-weight: 500;
}
.bk-root .id-random-report-button button:hover {
    background-color: #174c4f;
    border-color: #174c4f;
    color: #cc5c29;
    font-weight: 500;
}
iframe {
    width:100%;
    height:800px;
}
</style>
"""


class Config(param.Parameterized):
    """Pandas Profiling Configuration Settings"""

    title = param.String(default=DEFAULT_TITLE)
    minimal = param.Boolean(False)


class PandasProfilingApp(param.Parameterized):  # pylint: disable=too-many-instance-attributes
    """The PandasProfilingApp showcases how to integrate the Pandas Profiling Report with Panel"""

    csv_url = param.String(label="CSV URL")

    dataframe = param.DataFrame()
    report = param.ClassSelector(class_=ProfileReport)
    html_report = param.String()

    update_report = param.Action(label="UPDATE REPORT")
    random_report = param.Action(label="RANDOM REPORT")

    html_report_pane = param.ClassSelector(class_=pn.pane.HTML)
    view = param.Parameter()

    config = param.ClassSelector(class_=Config, instantiate=False)

    def __init__(self, **params):
        self._csv_urls_cycle = cycle(CSV_URLS)
        params["config"] = Config()
        params["update_report"] = self._update_report
        params["random_report"] = self._random_report

        super().__init__(**params)

        self.html_report_pane, self.view = self._get_view(self.config)

        self._set_random_csv_url()

    def _update_report(self, _=None):
        self._start_loading()
        self._generate_report()

        self.html_report_pane.object = HTML_CREATING_REPORT

        html_report = html.escape(self.html_report)
        self.html_report_pane.object = (
            f"""<iframe srcdoc="{html_report}" frameborder="0" allowfullscreen></iframe>"""
        )

        self._stop_loading()
        self.csv_url = self.csv_url

    def _stop_loading(self):
        stop_loading_spinner(self._tabs)

    def _start_loading(self):
        start_loading_spinner(self._tabs)

    def _random_report(self, _=None):
        self._start_loading()
        self._set_random_csv_url()
        self._update_report()

    def _get_view(self, conf):
        style = pn.pane.HTML(STYLE, width=0, height=0, margin=0, sizing_mode="fixed")
        app_bar = pn.Row(
            pn.pane.PNG(
                LOGO_URL,
                embed=False,
                height=50,
                width=62,
                sizing_mode="fixed",
                margin=(10, 0, 10, 25),
            ),
            pn.pane.Markdown(
                "# Pandas Profiling Report",
                sizing_mode="stretch_width",
                margin=(0, 0, 0, 25),
                align="center",
            ),
            sizing_mode="stretch_width",
            margin=(25, 0, 0, 0),
            css_classes=["app-bar"],
            background=GREEN,
        )
        widgets = {
            "csv_url": {
                "sizing_mode": "stretch_width",
            },
            "update_report": {
                "align": "end",
                "width": 150,
                "sizing_mode": "fixed",
                "button_type": "primary",
            },
            "random_report": {
                "button_type": "default",
                "align": "end",
                "width": 150,
                "sizing_mode": "fixed",
                "css_classes": ["id-random-report-button"],
            },
        }
        top_selections = pn.Param(
            self,
            parameters=["csv_url", "update_report", "random_report"],
            widgets=widgets,
            default_layout=pn.Row,
            show_name=False,
            sizing_mode="stretch_width",
        )

        html_report_pane = pn.pane.HTML(EMPTY_HTML_REPORT, height=900, sizing_mode="stretch_both")

        report_tab = pn.Column(
            top_selections,
            html_report_pane,
            sizing_mode="stretch_width",
            name="Report",
        )
        config_tab = pn.Param(
            conf, sizing_mode="stretch_width", name="Configuration", show_name=False
        )
        tabs = pn.Tabs(
            report_tab,
            config_tab,
        )
        self._tabs = tabs
        main = pn.Column(
            style,
            pn.Column(
                app_bar,
                pn.layout.HSpacer(),
                tabs,
            ),
        )
        return html_report_pane, main

    def _generate_report(self):
        self.html_report_pane.object = HTML_CREATING_REPORT
        self.dataframe, self.report, self.html_report = self._get_html_report(
            self.csv_url, self.config.minimal, self.config.title
        )

    @staticmethod
    @lru_cache(maxsize=128)
    def _get_html_report(url: str, minimal, title):
        dataframe = pd.read_csv(url, nrows=MAX_ROWS)
        report = ProfileReport(dataframe, minimal=minimal, title=title)
        return dataframe, report, report.to_html()

    def _set_random_csv_url(self):
        self.csv_url = next(self._csv_urls_cycle)

    def __str__(self):
        return "Pandas Profiler App"

    def __repr__(self):
        return self.__str__()


if __name__.startswith("bokeh"):
    app = config.extension(url="pandas_profiling_app")
    PandasProfilingApp().view.servable()