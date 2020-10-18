from typing import Tuple, Dict
from time import gmtime, strftime

import pandas as pd
import panel as pn
import param

pn.extension()

BY_STORM_SUMMARY = pd.DataFrame(
    {
        "Location": [
            "site1",
            "site2",
            "site1",
            "site2",
            "site1",
            "site2",
            "site1",
            "site2",
            "site1",
            "site2",
            "site1",
            "site2",
            "site3",
            "site3",
        ],
        "storm_number": [1, 1, 2, 2, 3, 3, 4, 4, 3, 3, 4, 4, 1, 2],
        "date_text": [
            "01Jan16",
            "07Jan16",
            "01Feb16",
            "04Feb16",
            "24Feb16",
            "17Feb16",
            "26Feb16",
            "02Mar16",
            "24Feb16",
            "17Feb16",
            "26Feb16",
            "02Mar16",
            "26Feb16",
            "02Mar16",
        ],
    }
)

NO_STORM_SELECTED_DICT = {
    "Select a location!": 0,
    "Select any location!": 1,
}


def get_discrete_storm_opts(by_storm_summary: pd.DataFrame, the_location: str) -> Tuple[Dict, int]:
    pk_data = by_storm_summary.loc[(by_storm_summary["Location"] == the_location)].reset_index()
    df2 = pk_data[["date_text", "storm_number"]].drop_duplicates().set_index("date_text")
    date_opts_dict = df2.to_dict()["storm_number"]
    return date_opts_dict


class ParameterizedStorm(param.Parameterized):
    by_storm_summary = param.DataFrame()
    single_location = param.ObjectSelector(
        label="Location for time-series plot",
        doc="A single location to plot time-series data from.",
    )
    single_storm_number = param.ObjectSelector(
        label="Storm for time-series plot",
        doc="A single storm to plot time-series data from.",
        objects={},
    )

    def __init__(self, by_storm_summary: pd.DataFrame):
        super().__init__(by_storm_summary=by_storm_summary)

        self._handle_by_storm_summary_change()
        self._handle_single_location_change()

    @param.depends("by_storm_summary", watch=True)
    def _handle_by_storm_summary_change(self):
        unique_locations = self.by_storm_summary["Location"].unique().tolist()
        print("by_storm_summary changed", unique_locations)
        self.param.single_location.objects = unique_locations
        if unique_locations:
            default_location = unique_locations[0]
            self.param.single_location.default = default_location
            if self.single_location not in unique_locations:
                self.single_location = default_location

    @param.depends("single_location", watch=True)
    def _handle_single_location_change(self):
        new_date_opts = get_discrete_storm_opts(
            by_storm_summary=self.by_storm_summary, the_location=self.single_location
        )

        # See https://github.com/holoviz/param/issues/398
        self.param["single_storm_number"].names = new_date_opts
        self.param["single_storm_number"].objects = list(new_date_opts.values())

        if new_date_opts:
            values = list(new_date_opts.values())
            default_single_storm_number = values[0]
            self.param["single_storm_number"].default = default_single_storm_number
            if not self.single_storm_number in values:
                self.single_storm_number = default_single_storm_number

    @param.depends(
        "single_location",
        "single_storm_number",
    )
    def view_states(self):
        text = (
            "Single Location {}".format(self.single_location)
            + "\nPossible single storm options: {}".format(
                self.param["single_storm_number"].objects
            )
            + "\nSingle Storm: {}".format(self.single_storm_number)
        )
        text_pane: pn.pane.Str = pn.pane.Str(object=text)
        return pn.Row(text_pane)


if __name__ == "__main__":
    the_storm_parmer = ParameterizedStorm(by_storm_summary=BY_STORM_SUMMARY)
    widget_pane = pn.Param(
        the_storm_parmer.param,
        parameters=["single_location", "single_storm_number"],
        widgets={
            "single_location": pn.widgets.Select,
            "single_storm_number": pn.widgets.DiscreteSlider,
        },
    )

    p = pn.Row(widget_pane, the_storm_parmer.view_states)
    p.show(port=5006)
