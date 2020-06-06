"""Doc"""
import param
import panel as pn
import pandas as pd
from pandas_profiling import ProfileReport
from functools import lru_cache
from itertools import cycle

DEFAULT_TITLE = "Pandas Profiling Report"
EMPTY_HTML_REPORT = "<h2>No Report Generated</h2>"
HTML_REPORT_IN_PROGRESS = "<h2>Report Generation in Progress</h2>"
CSV_URLS = [
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/application/pages/awesome_panel_express_tests/PerspectiveViewerData.csv",
    "https://github.com/MarcSkovMadsen/awesome-panel/raw/master/application/pages/deck_global_power_plants/global_power_plant_database.csv",
]
GREEN = "#174c4f"
ORANGE = "#cc5c29"

STYLE = """
<style>
.app-bar {
    color: #cc5c29
}
</style>
"""

class PandasProfilingApp(param.Parameterized):
    title = param.String(default=DEFAULT_TITLE)

    csv_url = param.String()

    dataframe = param.DataFrame()
    report = param.ClassSelector(class_=ProfileReport)
    html_report = param.String()

    update_report = param.Action()
    random_report = param.Action()

    html_report_pane = param.ClassSelector(class_=pn.pane.HTML)
    view = param.ClassSelector(class_=pn.layout.Reactive)

    @staticmethod
    @lru_cache(maxsize=128)
    def _extract_dataframe_from_url(url):
        return pd.read_csv(url)

    def __init__(self, **params):
        self._csv_urls_cycle = cycle(CSV_URLS)

        params["update_report"] = self._update_report
        params["random_report"] = self._random_report
        params["html_report_pane"], params["view"] = self._get_view()

        super().__init__(**params)

        self._set_random_csv_url()

    def _update_report(self, _=None):
        self.html_report_pane.object = HTML_REPORT_IN_PROGRESS

        self._load_dataframe_from_url()
        self._generate_report()

        self.html_report_pane.object = self.html_report

    def _random_report(self, _=None):
        self._set_random_csv_url()
        self._update_report()

    def _get_view(self):
        style = pn.pane.HTML(STYLE, width=0, height=0, margin=0, sizing_mode="fixed")
        description = pn.pane.Markdown(__doc__)
        app_bar = pn.Row(
            pn.pane.Markdown(
                "# " + self.title, sizing_mode="stretch_width", margin=(None, None, None, 25)
            ),
            sizing_mode="stretch_width",
            margin=(25, 5, 0, 5),
            css_classes=["app-bar"],
            background=GREEN,
        )
        widgets = {
            "csv_url": {
                "sizing_mode": "stretch_width",
            },
            "update_report": {
                "align": "end", "width": 150, "sizing_mode": "fixed"
            },
            "random_report": {
                "button_type": "success",
                "align": "end", "width": 150, "sizing_mode": "fixed"
            }
        }
        top_selections = pn.Param(
            self,
            parameters=["csv_url", "update_report", "random_report"],
            widgets=widgets,
            default_layout=pn.Row,
            show_name=False,
            sizing_mode="stretch_width",
        )

        html_report_pane = pn.pane.HTML(EMPTY_HTML_REPORT)

        view = pn.Column(
            style,
            description,
            app_bar,
            top_selections,
            html_report_pane,
            sizing_mode="stretch_width",
            )

        return html_report_pane, view

    def _load_dataframe_from_url(self):
        if self.csv_url:
            self.dataframe = self._extract_dataframe_from_url(self.csv_url)
        else:
            self.dataframe = pd.DataFrame()

    def _generate_report(self):
        self.report = ProfileReport(self.dataframe)
        self.html_report = self.report.to_html()

    def _set_random_csv_url(self):
        self.csv_url = next(self._csv_urls_cycle)

    def __str__(self):
        return "Pandas Profiler App"

    def __repr__(self):
        return self.__str__()


def view():
    return PandasProfilingApp().view

if __name__.startswith("bokeh"):
    pn.config.sizing_mode="stretch_width"
    PandasProfilingApp().view.servable()
