"""[Tabulator](http://tabulator.info/) is a very powerful interactive javascript Table.

Panel provides the [`Tabulator`](https://panel.holoviz.org/reference/layouts/Tabs.html) widget.
The widget was first implemented and contributed by `awesome-panel.org`. Later Philipp did massive
improvements. It is now one of the most powerful widgets in Panel.
"""
import pathlib

import pandas as pd
import panel as pn
import param
from panel.widgets import Tabulator

from application.config import site

APPLICATION = site.create_application(
    url="tabulator",
    name="Tabulator",
    author="Marc Skov Madsen",
    introduction="Demonstrates the powerful Tabulator Table",
    description=__doc__,
    thumbnail_url="tabulator-app.png",
    documentation_url="",
    code_url="tabulator_app/tabulator_app.py",
    gif_url="tabulator-app.gif",
    mp4_url="tabulator-app.mp4",
    tags=[
        "Streaming",
        "Tabulator",
    ],
)

TABULATOR_DATA_PATH = pathlib.Path(__file__).parent / "tabulator_data.csv"
TABULATOR_THEME = {pn.template.theme.DefaultTheme: "site", pn.template.theme.DarkTheme: "midnight"}
TABULATOR_FORMATTERS = {
    "progress": {"type": "progress", "max": 100},
    "rating": {"type": "star", "min": 0, "max": 5},
    "car": {"type": "tickCross"},
}

if not "perspective-data" in pn.state.cache:
    pn.state.cache["perspective-data"] = (
        pd.read_csv(TABULATOR_DATA_PATH).fillna("nan").drop(columns=["id", "activity"])
    )

DATA = pn.state.cache["perspective-data"]


class TabulatorDataFrameApp(param.Parameterized):
    """Extension Implementation"""

    tabulator = param.Parameter()

    reset = param.Action(label="RESET")
    replace = param.Action(label="REPLACE")
    stream = param.Action(label="STREAM")
    patch = param.Action(label="PATCH")

    avg_rating = param.Number(default=0, constant=True)
    value_edits = param.Number(default=-1, constant=True)

    view = param.Parameter()

    def __init__(self, data: pd.DataFrame = DATA, **params):
        super().__init__(**params)
        self.data = data
        self.tabulator = params["tabulator"] = Tabulator(
            value=self.data.copy(deep=True).iloc[
                0:10,
            ],
            height=400,
            formatters=TABULATOR_FORMATTERS,
            sizing_mode="stretch_both",
            background="salmon",
        )
        self.sizing_mode = "stretch_width"
        self.height = 950

        self.rows_count = len(self.data)
        self.stream_count = 15

        self.reset = self._reset_action
        self.replace = self._replace_action
        self.stream = self._stream_action
        self.patch = self._patch_action
        self.view = self._create_view()
        self._update_avg_rating()
        self.tabulator.param.watch(self._update_avg_rating, "value")

    def _create_view(self):
        pn.config.sizing_mode = "stretch_width"
        template = pn.template.FastListTemplate(title="Tabulator")
        self.tabulator.theme = TABULATOR_THEME[template.theme]
        actions_pane = pn.Param(
            self,
            parameters=["reset", "replace", "stream", "patch"],
            name="Actions",
        )
        template.main[:] = [
            APPLICATION.intro_section(),
            self.tabulator,
        ]
        template.sidebar[:] = [
            self.tabulator.param.theme,
            self.tabulator.param.selection,
            actions_pane,
        ]
        return template

    def _reset_action(self, *_):
        value = self.data.copy(deep=True).iloc[
            0:10,
        ]
        self.tabulator.value = value

    def _replace_action(self, *_):
        # Please note that it is required that the index is reset
        # Please also remember to add drop=True. Otherwise stream and patch raises errors
        value = (
            self.data.copy(deep=True)
            .iloc[
                10:15,
            ]
            .reset_index(drop=True)
        )
        self.tabulator.value = value

    def _stream_action(self, *_):
        # Hack: See https://github.com/holoviz/panel/issues/2116#issuecomment-806154952
        tabulator = self.tabulator
        # pylint: disable=protected-access
        if len(tabulator._models) > 1:
            del tabulator._models[next(iter(tabulator._models))]

        if self.stream_count == len(self.data):
            self.stream_count = 15
            self._reset_action()
        else:
            stream_data = self.data.iloc[
                self.stream_count : self.stream_count + 1,
            ]
            self.tabulator.stream(stream_data)
            self.stream_count += 1

    def _patch_action(self, *_):
        def _patch(value):
            value += 10
            if value >= 100:
                return 0
            return value

        data = self.tabulator.value
        progress = data["progress"]
        new_progress = progress.map(_patch)
        self.tabulator.patch(new_progress)

    def _update_avg_rating(self, *_):
        with param.edit_constant(self):
            self.avg_rating = self.tabulator.value["rating"].mean()
            self.value_edits += 1

    def __repr__(self):
        return f"Tabulator({self.name})"

    def __str__(self):
        return f"Tabulator({self.name})"


@site.add(application=APPLICATION)
def view():
    """Return the TabulatorDataFrameApp

    Returns:
        TabulatorDataFrameApp: An instance of TabulatorDataFrameApp
    """
    return TabulatorDataFrameApp().view


if __name__.startswith("bokeh"):
    view().servable()
