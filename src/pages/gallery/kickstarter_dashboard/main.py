"""# Kickstarter Dashboard

The purpose of the Kickstarter Dashboard was to test if the claims regarding Bokeh as of Jan 2018 in the
[bokeh-dash-best-dashboard-framework](https://www.sicara.ai/blog/2018-01-30-bokeh-dash-best-dashboard-framework-python)
article holds for Panel and the HoloViews suite of tools as of Dec 2019.

The claims where

- Data in Bokeh becomes inconsistent
- Bokeh is slow for big datasets
- Cannot link charts to dataframe
- Interactions take a long time to develop

You can evaluate this dashboard and the code to make your personal evaluation of the above
statements.

My evaluation is TBD
"""
import pathlib
from typing import List, Optional

import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn
import param

pn.extension()

KICKSTARTER_PATH = pathlib.Path(__file__).parent / "kickstarter-cleaned.csv"
COLUMNS = ["created_at", "usd_pledged", "state", "category_slug"]
# Picked with http://tristen.ca/hcl-picker/#/hlc/6/1.05/251C2A/E98F55
COLORS = ["#7DFB6D", "#C7B815", "#D4752E", "#C7583F"]
STATES = ["successful", "suspended", "failed", "canceled"]
DATE_COLUMNS = [
    "created_at",
]
N_SAMPLES = 1000
TITLE = "Kickstarter Dashboard"


class KickstarterDashboard(param.Parameterized):
    categories = param.ListSelector()
    kickstarter_df = param.DataFrame()
    scatter_df = param.DataFrame()
    bar_df = param.DataFrame()

    @param.depends("categories")
    def view_categories(self):
        return self.categories

    def __init__(self):
        self.param.kickstarter_df.default = get_kickstarter_df()
        self.param.categories.default = get_categories(self.kickstarter_df)
        self.param.categories.objects = self.param.categories.default
        self.param.scatter_df.default = self.param.kickstarter_df.default
        self.param.bar_df.default = self.param.kickstarter_df.default

    @param.depends("kickstarter_df", "categories")
    def set_scatter_df(self):
        self.scatter_df = filter_on_categories(self.kickstarter_df, self.categories)

    @param.depends("scatter_df")
    def scatter_plot(self):
        # Potential Improvements
        # Rename columns to Capitalized without under score
        # Add name of movie to hover tooltip

        # Plot
        scatter_plot = self.scatter_df.hvplot.scatter(
            x="created_at",
            y="usd_pledged",
            by="state",
            height=400,
            responsive=True,
            yformatter="%.1fM",
        )
        rangexy = hv.streams.RangeXY(source=scatter_plot)

        @param.depends(rangexy.param.x_range, rangexy.param.y_range)
        def set_bar_df(x_range, y_range):
            print(x_range, y_range)
            self.bar_df = filter_bar_df(self.scatter_df, x_range, y_range)

        return pn.Column(scatter_plot, set_bar_df, sizing_mode="stretch_width")

    @param.depends("bar_df")
    def bar_chart(self):
        return get_bar_chart(self.bar_df)

    def view(self):
        return pn.Column(
            __doc__,
            self.param.categories,
            self.scatter_plot,
            self.bar_chart,
            self.set_scatter_df,
            sizing_mode="stretch_width",
        )


def view():
    return KickstarterDashboard().view()


def _extract() -> pd.DataFrame:
    """Extracts the kickstarter data into a DataFrame

    Returns:
        pd.DataFrame -- A Dataframe of kickstarter data with columns=["created_at", "usd_pledged", "state", "category_slug"]
    """
    return pd.read_csv(KICKSTARTER_PATH, parse_dates=DATE_COLUMNS)


def _transform(source_data: pd.DataFrame, n_samples: int = N_SAMPLES) -> pd.DataFrame:
    """Transform the data by

    - adding broader_category,
    - converting usd_pledged to millions
    - sampling to n_samples

    Arguments:
        source_data {pd.DataFrame} -- The source kickstarter data

    Returns:
        pd.DataFrame -- The transformed DataFrame with
        columns=["created_at", "usd_pledged", "state", "category_slug", "broader_category"]
    """
    source_data["broader_category"] = source_data["category_slug"].str.split("/").str.get(0)
    source_data["usd_pledged"] = source_data["usd_pledged"] / 10 ** 6
    return source_data.sample(n_samples)


def get_kickstarter_df() -> pd.DataFrame():
    source_data = _extract()
    kickstarter_df = _transform(source_data)
    return kickstarter_df


def get_categories(kickstarter_df) -> List[str]:
    return list(kickstarter_df["broader_category"].unique())


def filter_on_categories(kickstarter_df, categories) -> pd.DataFrame:
    if categories is None or categories == []:
        categories = get_categories(kickstarter_df)
    categories_filter = kickstarter_df["broader_category"].isin(categories)
    return kickstarter_df[categories_filter]


def filter_bar_df(kickstarter_df, x_range, y_range) -> pd.DataFrame:
    sub_df = kickstarter_df
    if y_range:
        y_filter = (kickstarter_df["usd_pledged"] >= y_range[0]) & (
            kickstarter_df["usd_pledged"] <= y_range[1]
        )
        sub_df = sub_df[y_filter]
    if x_range:
        x_filter = (kickstarter_df["created_at"] >= x_range[0]) & (
            kickstarter_df["created_at"] <= x_range[1]
        )
        sub_df = sub_df[x_filter]
    return sub_df


def get_scatter_plot(kickstarter_df):
    # Potential Improvements
    # Rename columns to Capitalized without under score
    # Add name of movie to hover tooltip

    scatter_plot = kickstarter_df.hvplot.scatter(
        x="created_at", y="usd_pledged", by="state", height=400, responsive=True, yformatter="%.1fM"
    )
    return scatter_plot


def get_bar_chart(kickstarter_df):
    """Creates the bar_chart"""
    # Potential improvements
    # Sort by Number of Projects Desc to make it easier to see what large and small

    # Filter
    stacked_barchart_df = (
        kickstarter_df[["broader_category", "state", "created_at"]]
        .groupby(["broader_category", "state"])
        .count()
        .rename(columns={"created_at": "Number of projects"})
    )

    # Plot
    bar_chart = stacked_barchart_df.hvplot.bar(
        stacked=True, height=400, responsive=True, xlabel="Number of projects",
    )
    return bar_chart


if __name__.startswith("bk"):
    view().servable("Kickstarter Dashboard")
