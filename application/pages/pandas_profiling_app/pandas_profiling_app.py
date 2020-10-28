"""# Pandas Profiling with Panel

[Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) provides profile reports
from Pandas DataFrames. I hope this provides you with an impression of how this can be integrated
in a [Panel](https://panel.holoviz.org/) context.

This app was originally created as a response to this [question on Discourse]\
(https://discourse.holoviz.org/t/cant-display-pandas-profiling-report/760/2).

This app is restricted to profile a **maximum of 200 rows** to minimize the impact on the server.

**Author:**
[Marc Skov Madsen](https://datamodelsanalytics.com)

**Code:**
[App]\
(https://github.com/MarcSkovMadsen/awesome-panel/blob/master/\
application/pages/pandas_profiling_app/pandas_profiling_app.py),
[Tests]\
(https://github.com/MarcSkovMadsen/awesome-panel/blob/master/\
tests/application/tests/test_pandas_profiling_app.py)

**Resources:**
[Pandas Profiling Examples]\
(https://pandas-profiling.github.io/pandas-profiling/docs/master/\
rtd/pages/examples.html#showcasing-specific-features)

**Tags:**
[Panel](https://panel.holoviz.org/),
[Pandas](https://pandas.pydata.org/),
"""
import html
from functools import lru_cache
from itertools import cycle

import pandas as pd
import panel as pn
import param
from pandas_profiling import ProfileReport

from application.template import get_template

# pylint: disable=line-too-long
DEFAULT_TITLE = "Pandas Profiling Report"
EMPTY_HTML_REPORT = "<p>Click a button to generate a report</p>"
HTML_LOADING_DATA = "<p>Loading data (1 of 4) ...</p>"
HTML_CREATING_PROFILER = "<p>Creating Profiler (2 of 4) ...</p>"
HTML_GENERATING_REPORT = "<p>Generating Report (3 of 4) ...</p>"
HTML_LOADING_REPORT = "<p>Loading Report (4 of 4) ...</p>"
CSV_URLS = [
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/application/pages/awesome_panel_express_tests/PerspectiveViewerData.csv",
    "https://github.com/MarcSkovMadsen/awesome-panel/raw/master/application/pages/deck_global_power_plants/global_power_plant_database.csv",
    "https://github.com/MarcSkovMadsen/awesome-panel/raw/master/application/pages/kickstarter_dashboard/kickstarter-cleaned.csv",
    "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Annual%20CO2%20emissions%20-%20(Global%20Carbon%20Project%20%26%20CDIAC%2C%202019)/Annual%20CO2%20emissions%20-%20(Global%20Carbon%20Project%20%26%20CDIAC%2C%202019).csv",
    "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Land%20surface%20temperature%20anomaly-%20Berkley%20Earth/Land%20surface%20temperature%20anomaly-%20Berkley%20Earth.csv",
    "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Number%20of%20polio%20cases%20per%20one%20million%20population%20-%20WHO%20(2017)/Number%20of%20polio%20cases%20per%20one%20million%20population%20-%20WHO%20(2017).csv",
]
GREEN = "#174c4f"
ORANGE = "#cc5c29"
LOGO_URL = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/application/pages/pandas_profiling_app/pandas_profiler_logo.png"
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


class PandasProfilingApp(param.Parameterized):
    """The PandasProfilingApp showcases how to integrate the Pandas Profiling Report with Panel"""

    csv_url = param.String(label="CSV URL")

    dataframe = param.DataFrame()
    report = param.ClassSelector(class_=ProfileReport)
    html_report = param.String()

    update_report = param.Action(label="UPDATE REPORT")
    random_report = param.Action(label="RANDOM REPORT")

    progress = param.Parameter()
    html_report_pane = param.ClassSelector(class_=pn.pane.HTML)
    view = param.Parameter()

    config = param.ClassSelector(class_=Config, instantiate=False)

    def __init__(self, **params):
        self._csv_urls_cycle = cycle(CSV_URLS)
        params["config"] = Config()
        params["update_report"] = self._update_report
        params["random_report"] = self._random_report
        params["progress"], params["html_report_pane"], params["view"] = self._get_view(
            params["config"]
        )

        super().__init__(**params)

        self._set_random_csv_url()

    def _update_report(self, _=None):
        self.progress.active = True

        self._generate_report()

        self.html_report_pane.object = HTML_LOADING_REPORT

        html_report = html.escape(self.html_report)
        self.html_report_pane.object = (
            f"""<iframe srcdoc="{html_report}" frameborder="0" allowfullscreen></iframe>"""
        )

        self.progress.active = False
        self.csv_url = self.csv_url

    def _random_report(self, _=None):
        self.progress.active = True
        self._set_random_csv_url()
        self._update_report()

    def _get_view(self, config):
        pn.config.sizing_mode = "stretch_width"
        style = pn.pane.HTML(STYLE, width=0, height=0, margin=0, sizing_mode="fixed")
        description = pn.pane.Markdown(__doc__)
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
            margin=(25, 5, 0, 5),
            css_classes=["app-bar"],
            background=GREEN,
        )
        progress = pn.widgets.Progress(
            bar_color="secondary", width=335, sizing_mode="fixed", margin=(0, 5, 10, 5)
        )
        progress.active = False
        widgets = {
            "csv_url": {
                "sizing_mode": "stretch_width",
            },
            "update_report": {"align": "end", "width": 150, "sizing_mode": "fixed"},
            "random_report": {
                "button_type": "success",
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
            config, sizing_mode="stretch_width", name="Configuration", show_name=False
        )
        tabs = pn.Tabs(
            report_tab,
            config_tab,
        )

        main = [
            style,
            description,
            app_bar,
            pn.Row(pn.layout.HSpacer(), progress, sizing_mode="stretch_width"),
            tabs,
            pn.layout.HSpacer(height=400),  # Gives better scrolling
        ]
        _view = get_template(title="Pandas Profiling App", main=main)

        return progress, html_report_pane, _view

    def _generate_report(self):
        print(self.csv_url, self.config.title, self.config.minimal)
        self.html_report_pane.object = HTML_LOADING_DATA
        self.dataframe = self._get_dataframe(self.csv_url)
        self.html_report_pane.object = HTML_CREATING_PROFILER
        self.report = self._get_profile_report(self.csv_url, self.config.title, self.config.minimal)
        self.html_report_pane.object = HTML_GENERATING_REPORT
        self.html_report = self._get_html_report(
            self.csv_url, self.config.title, self.config.minimal
        )

    @staticmethod
    @lru_cache(maxsize=128)
    def _get_dataframe(url):
        return pd.read_csv(url, nrows=MAX_ROWS)

    @lru_cache(maxsize=128)
    def _get_profile_report(self, url, title, minimal):
        print(url, title, minimal)
        return ProfileReport(self.dataframe, minimal=minimal, title=title)

    @lru_cache(maxsize=128)
    def _get_html_report(self, url, title, minimal):
        print(url, title, minimal)
        return self.report.to_html()

    def _set_random_csv_url(self):
        self.csv_url = next(self._csv_urls_cycle)

    def __str__(self):
        return "Pandas Profiler App"

    def __repr__(self):
        return self.__str__()


def view():
    """Function used by the awesome-panel.org application"""
    return PandasProfilingApp().view


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"
    PandasProfilingApp().view.servable()
