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

My evaluation is the **first three statements does no longer hold**. The fourth I've also experienced
see this [discussion](https://discourse.holoviz.org/t/how-to-create-a-parameterized-dashboard-with-seperation-between-data-transforms-and-data-views/53/13)

I can see that I made a lot of mistakes because it takes time to understand how the api works.
Right now I'm thinking that it's because I chose the most advanced way to implement this using `param` and reactive programme.
And I'm thinking that power of the whole Holoviz Ecosystem is also what makes it difficult to get started with.
"""
import pathlib
from typing import List

# import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn
import param

pn.extension()

KICKSTARTER_PATH = pathlib.Path(__file__).parent / "kickstarter-cleaned.csv"
COLUMNS = ["created_at", "usd_pledged", "state", "category_slug"]
# Picked with http://tristen.ca/hcl-picker/#/hlc/6/1.05/251C2A/E98F55
DATE_COLUMNS = [
    "created_at",
]
N_SAMPLES = 10000


class KickstarterDashboard(param.Parameterized):
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

My evaluation is the **first three statements does no longer hold**. The fourth I've also experienced
see this [discussion](https://discourse.holoviz.org/t/how-to-create-a-parameterized-dashboard-with-seperation-between-data-transforms-and-data-views/53/13)

I can see that I made a lot of mistakes because it takes time to understand how the api works.
Right now I'm thinking that it's because the wholo Holoviz Ecosystem is so powerfull that there is so much to learn.
"""

    kickstarter_df = param.DataFrame()
    categories = param.ListSelector()
    scatter_df = param.DataFrame()
    bar_df = param.DataFrame()

    def __init__(self, *args, **kwargs):
        kickstarter_df = self.get_kickstarter_df()
        categories = self.get_categories(kickstarter_df)

        self.param.kickstarter_df.default = kickstarter_df
        self.param.categories.default = categories
        self.param.categories.objects = categories
        self.param.scatter_df.default = kickstarter_df
        self.param.bar_df.default = kickstarter_df

        super().__init__(*args, **kwargs)

    @param.depends("kickstarter_df", "categories", watch=True)
    def _set_scatter_df(self):
        self.scatter_df = self._filter_on_categories(self.kickstarter_df, self.categories)

    @param.depends("scatter_df")
    def scatter_plot_view(self):
        """A Reactive View of the scatter plot"""
        # Potential Improvements
        # Rename columns to Capitalized without under score
        # Add name of movie to hover tooltip
        scatter_plot = self.get_scatter_plot(self.scatter_df)
        self.bar_df = self.scatter_df

        # rangexy = hv.streams.RangeXY(source=scatter_plot.last)

        # @param.depends(rangexy.param.x_range, rangexy.param.y_range, watch=True)
        # def set_bar_df(x_range, y_range):
        #     self.bar_df = _filter_bar_df(self.scatter_df, x_range, y_range)

        return scatter_plot

    @param.depends("bar_df")
    def bar_chart_view(self):
        """A Reactive View of the Bar Chart"""
        return self.get_bar_chart(self.bar_df)

    def view(self):
        """A Reactive View of the KickstarterDashboard"""
        return pn.Column(
            __doc__,
            self.param.categories,
            self.scatter_plot_view,
            self.bar_chart_view,
            sizing_mode="stretch_width",
        )

    def _extract(self) -> pd.DataFrame:
        """Extracts the kickstarter data into a DataFrame

        Returns:
            pd.DataFrame -- A Dataframe of kickstarter data with columns=["created_at", "usd_pledged", "state", "category_slug"]
        """
        return pd.read_csv(KICKSTARTER_PATH, parse_dates=DATE_COLUMNS)

    def _transform(self, source_data: pd.DataFrame, n_samples: int = N_SAMPLES) -> pd.DataFrame:
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

    def get_kickstarter_df(self) -> pd.DataFrame:
        """The Dataframe of Kickstarter Data

        Returns:
            [pd.DataFrame] -- The Dataframe of Kickstarter Data
        """
        source_data = self._extract()
        kickstarter_df = self._transform(source_data)
        return kickstarter_df

    def get_categories(self, kickstarter_df) -> List[str]:
        """The list of kickstarter broader categories

        Arguments:
            kickstarter_df {[type]} -- [description]

        Returns:
            List[str] -- [description]
        """
        return list(kickstarter_df["broader_category"].unique())

    def _filter_on_categories(
        self, kickstarter_df: pd.DataFrame, categories: List[str]
    ) -> pd.DataFrame:
        """Filters the kickstarter_df by the specified categories

        Arguments:
            kickstarter_df {pd.DataFrame} -- A Kickstarter Dataframe
            categories {List[str]} -- The list of broader_category in the DataFrame

        Returns:
            pd.DataFrame -- The filtered DataFrame
        """
        if categories is None or categories == []:
            categories = self.get_categories(kickstarter_df)
        categories_filter = kickstarter_df["broader_category"].isin(categories)
        return kickstarter_df[categories_filter]

    def _filter_bar_df(self, kickstarter_df: pd.DataFrame, x_range, y_range) -> pd.DataFrame:
        """Filter the kickstarter_df by x_range and y_range

        Arguments:
            kickstarter_df {pd.DataFrame} -- [description]
            x_range {[type]} -- The usd_pledged range
            y_range {[type]} -- The created_at range

        Returns:
            pd.DataFrame -- The filtered DataFrame
        """
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

    def get_scatter_plot(self, kickstarter_df: pd.DataFrame):
        """A Scatter plot of the kickstarter_df

        Arguments:
            kickstarter_df {pd.DataFrame} -- The DataFrame of kickstarter data

        """
        # Potential Improvements
        # Rename columns to Capitalized without under score
        # Add name of movie to hover tooltip

        return kickstarter_df.hvplot.scatter(
            x="created_at",
            y="usd_pledged",
            by="state",
            height=400,
            responsive=True,
            yformatter="%.1fM",
        )

    def get_bar_chart(self, kickstarter_df: pd.DataFrame):
        """A bar chart of the kickstarter_df

        Arguments:
            kickstarter_df {pd.DataFrame} -- A DataFrame of Kickstarter data

        Returns:
            [type] -- A bar chart of the kickstarter_df
        """
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


def view() -> KickstarterDashboard:
    """A Reactive View of the KickstarterDashboard"""
    return KickstarterDashboard().view()


if __name__.startswith("bk"):
    view().servable("Kickstarter Dashboard")
