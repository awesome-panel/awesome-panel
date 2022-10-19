"""[Tabulator](http://tabulator.info/) is a very powerful interactive javascript Table.

Panel provides the [`Tabulator`](https://panel.holoviz.org/reference/layouts/Tabs.html) widget.
The widget was first implemented and contributed by `awesome-panel.org`. Later Philipp did massive
improvements. It is now one of the most powerful widgets in Panel.
"""

import pandas as pd
import panel as pn
import param
from panel.widgets import Tabulator

from awesome_panel import config
from awesome_panel.assets.csv import TABULATOR_DATA_PATH
from awesome_panel.config import cached

TABULATOR_THEME = {pn.template.theme.DefaultTheme: "site", pn.template.theme.DarkTheme: "midnight"}
TABULATOR_FORMATTERS = {
    "progress": {"type": "progress", "max": 100},
    "rating": {"type": "star", "min": 0, "max": 5},
    "car": {"type": "tickCross"},
}


@cached
def _get_data():
    return pd.read_csv(TABULATOR_DATA_PATH).fillna("nan").drop(columns=["id", "activity"])


DATA = _get_data()


class TabulatorDataFrameApp(param.Parameterized):  # pylint: disable = too-many-instance-attributes
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
        self.tabulator.theme = TABULATOR_THEME[pn.state.template.theme]
        actions_pane = pn.Param(
            self,
            parameters=["reset", "replace", "stream", "patch"],
            name="Actions",
        )
        return pn.Column(
            pn.Column(
                self.tabulator.param.theme,
                self.tabulator.param.selection,
                actions_pane,
            ),
            self.tabulator,
        )

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
        # Patch is broken. See https://github.com/holoviz/panel/issues/3084
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


if __name__.startswith("bokeh"):
    config.extension("tabulator", url="tabulator")

    TabulatorDataFrameApp().view.servable()
