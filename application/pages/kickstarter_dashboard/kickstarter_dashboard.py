# pylint: disable=line-too-long
"""
The purpose of the Kickstarter Dashboard was to test if the claims regarding Bokeh as of Jan 2018 in the
[bokeh-dash-best-dashboard-framework](https://www.sicara.ai/blog/2018-01-30-bokeh-dash-best-dashboard-framework-python)
article holds for Panel and the HoloViews suite of tools as of Dec 2019.

The claims where

- Data in Bokeh becomes inconsistent
- Bokeh is slow for big datasets
- Cannot link charts to dataframe
- Interactions take a long time to develop

You can evaluate this dashboard and the code to make your personal evaluation of the above
statements in the Context of Panel.

You can find an alternative version of this Dashboard in Streamlit at
[awesome-streamlit.org](https://awesome-streamlit.org)
"""
import pathlib
from typing import List, Optional

import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import numpy as np
import pandas as pd
import panel as pn
import param

# pylint: enable=line-too-long
# pylint: disable=duplicate-code
from awesome_panel_extensions.site import site

# pylint: enable=duplicate-code
KICKSTARTER_PATH = pathlib.Path(__file__).parent / "kickstarter-cleaned.csv"
COLUMNS = [
    "created_at",
    "usd_pledged",
    "state",
    "category_slug",
]
DATE_COLUMNS = [
    "created_at",
]
N_SAMPLES = 10000
CMAP = {
    "canceled": "#E0BB5E",
    "failed": "#E1477E",
    "successful": "#31E040",
    "suspended": "#3D69E0",
}
APPLICATION = site.create_application(
    url="kick-starter-dashboard",
    name="Kickstarter Dashboard",
    author="Marc Skov Madsen",
    description="A dashboard with fast and responsive linked brushing of the plots",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/kickstarter_dashboard.png",
    code="https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/kickstarter_dashboard/kickstarter_dashboard.py",
    tags=["Bokeh", "Linked Brushing"],
)


class KickstarterDashboard(param.Parameterized):
    # pylint: disable=line-too-long
    """The purpose of the Kickstarter Dashboard is to test if the claims regarding Bokeh as of Jan 2018 in the
    [bokeh-dash-best-dashboard-framework](https://www.sicara.ai/blog/2018-01-30-bokeh-dash-best-dashboard-framework-python)
    article holds for Panel and the HoloViews suite of tools as of Dec 2019.

    The claims where

    - Data in Bokeh becomes inconsistent
    - Cannot link charts to dataframe
    - Bokeh is slow for big datasets
    - Interactions take a long time to develop

    You can evaluate this dashboard and the code to make your personal evaluation of the above
    statements.

    My evaluation is

    - the **first two statements does no longer hold**.
    - The third is up for discussion. I would also like the Dashboard updates to be a bit faster. Maybe it's because I don't yet know how to implement this efficiently.
    - The fourth I've also experienced
    see this [discussion](https://discourse.holoviz.org/t/how-to-create-a-parameterized-dashboard-with-seperation-between-data-transforms-and-data-views/53/13).

    I can see that I made a lot of mistakes because it takes time for me to understand how the api works.
    There is a lot to I need to learn across the HoloViz suite of tools."""
    # pylint: enable=line-too-long
    kickstarter_df = param.DataFrame()
    categories = param.ListSelector()
    scatter_df = param.DataFrame()
    bar_df = param.DataFrame()
    rangexy = param.ClassSelector(
        class_=hv.streams.RangeXY,
        default=hv.streams.RangeXY(),
    )

    def __init__(self, kickstarter_df: Optional[pd.DataFrame] = None, **kwargs):
        if not isinstance(
            kickstarter_df,
            pd.DataFrame,
        ):
            kickstarter_df = self.get_kickstarter_df()
        categories = self.get_categories(kickstarter_df)

        self.param.kickstarter_df.default = kickstarter_df
        self.param.categories.default = categories
        self.param.categories.objects = categories
        self.param.scatter_df.default = kickstarter_df
        self.param.bar_df.default = kickstarter_df

        super().__init__(**kwargs)

    @param.depends(
        "kickstarter_df",
        "categories",
        watch=True,
    )
    def _set_scatter_df(
        self,
    ):
        self.scatter_df = self.filter_on_categories(
            self.kickstarter_df,
            self.categories,
        )

    @param.depends("scatter_df")
    def scatter_plot_view(
        self,
    ):
        """A Reactive View of the scatter plot"""
        # Potential Improvements
        # Rename columns to Capitalized without under score
        # Add name of movie to hover tooltip
        scatter_plot = self.get_scatter_plot(self.scatter_df)
        # Please note that depending on how the scatter_plot is generated it might be a Scatter
        # or Ndoverlay objects
        # In the first case use scatter_plot. In the second case use scatter_plot.last
        self.rangexy.source = scatter_plot.last
        return scatter_plot

    @param.depends(
        "scatter_df",
        "rangexy.x_range",
        "rangexy.y_range",
        watch=True,
    )
    def _set_bar_df(
        self,
    ):
        """Update the bar_df dataframe"""
        self.bar_df = self.filter_on_ranges(
            self.scatter_df,
            self.rangexy.x_range,  # pylint: disable=no-member
            self.rangexy.y_range,  # pylint: disable=no-member
        )

    @param.depends("bar_df")
    def bar_chart_view(
        self,
    ):
        """A Reactive View of the Bar Chart"""
        return self.get_bar_chart(self.bar_df)

    def view(
        self,
    ):
        """A Reactive View of the KickstarterDashboard"""
        pn.config.sizing_mode = "stretch_width"
        template = pn.template.FastListTemplate(title="Kickstarter Dashboard", theme_toggle=False)
        template.sidebar[:] = [
            pn.pane.HTML("<h2>Settings</h2>"),
            pn.Param(
                self.param.categories,
                widgets={
                    "categories": {
                        "size": len(self.categories),
                    }
                },
            ),
        ]
        template.main[:] = [
            APPLICATION.intro_section(),
            pn.Row(
                pn.Column(self.scatter_plot_view, self.bar_chart_view, sizing_mode="stretch_width"),
            ),
        ]
        return template

    @staticmethod
    def _extract() -> pd.DataFrame:
        """Extracts the kickstarter data into a DataFrame

        Returns:
            pd.DataFrame -- A Dataframe of kickstarter data with
            columns=["created_at", "usd_pledged", "state", "category_slug"]
        """
        return pd.read_csv(
            KICKSTARTER_PATH,
            parse_dates=DATE_COLUMNS,
        )

    @staticmethod
    def _transform(
        source_data: pd.DataFrame,
        n_samples: int = N_SAMPLES,
    ) -> pd.DataFrame:
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

    @classmethod
    def get_kickstarter_df(
        cls,
    ) -> pd.DataFrame:
        """The Dataframe of Kickstarter Data

        Returns:
            [pd.DataFrame] -- The Dataframe of Kickstarter Data
        """
        source_data = cls._extract()
        kickstarter_df = cls._transform(source_data)
        return kickstarter_df

    @staticmethod
    def get_categories(
        kickstarter_df,
    ) -> List[str]:
        """The list of kickstarter broader categories

        Arguments:
            kickstarter_df {[type]} -- [description]

        Returns:
            List[str] -- [description]
        """
        return list(kickstarter_df["broader_category"].unique())

    @classmethod
    def filter_on_categories(
        cls,
        kickstarter_df: pd.DataFrame,
        categories: List[str],
    ) -> pd.DataFrame:
        """Filters the kickstarter_df by the specified categories

        Arguments:
            kickstarter_df {pd.DataFrame} -- A Kickstarter Dataframe
            categories {List[str]} -- The list of broader_category in the DataFrame

        Returns:
            pd.DataFrame -- The filtered DataFrame
        """
        if categories is None or categories == []:
            categories = cls.get_categories(kickstarter_df)
        categories_filter = kickstarter_df["broader_category"].isin(categories)
        return kickstarter_df[categories_filter]

    @staticmethod
    def filter_on_ranges(
        kickstarter_df: pd.DataFrame,
        x_range,
        y_range,
    ) -> pd.DataFrame:
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
            if not np.isnan(y_range[0]):
                sub_df = sub_df[kickstarter_df["usd_pledged"] >= y_range[0]]
            if not np.isnan(y_range[1]):
                sub_df = sub_df[kickstarter_df["usd_pledged"] <= y_range[1]]
        if x_range:
            if not np.isnan(x_range[0]):
                sub_df = sub_df[kickstarter_df["created_at"] >= x_range[0]]
            if not np.isnan(x_range[1]):
                sub_df = sub_df[kickstarter_df["created_at"] <= x_range[1]]
        return sub_df

    @staticmethod
    def get_scatter_plot(
        kickstarter_df: pd.DataFrame,
    ):  # pylint: disable=missing-return-type-doc
        """A Scatter plot of the kickstarter_df

        Arguments:
            kickstarter_df {pd.DataFrame} -- The DataFrame of kickstarter data

        Returns:
            [type] -- A Scatter plot
        """
        # Potential Improvements
        # Rename columns to Capitalized without under score
        # Add name of movie to hover tooltip
        kickstarter_df["color"] = kickstarter_df["state"]
        return kickstarter_df.hvplot.scatter(
            x="created_at",
            y="usd_pledged",
            # color="color",
            by="state",
            cmap=list(CMAP.values()),
            height=400,
            responsive=True,
            yformatter="%.1fM",
        )

    @staticmethod
    def get_bar_chart(
        kickstarter_df: pd.DataFrame,
    ):  # pylint: disable=missing-return-type-doc
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
            kickstarter_df[
                [
                    "broader_category",
                    "state",
                    "created_at",
                ]
            ]
            .groupby(
                [
                    "broader_category",
                    "state",
                ]
            )
            .count()
            .rename(columns={"created_at": "Number of projects"})
        )

        # Plot
        bar_chart = stacked_barchart_df.hvplot.bar(
            stacked=True,
            height=400,
            responsive=True,
            xlabel="Number of projects",
            cmap=CMAP,
        )
        return bar_chart


@site.add(APPLICATION)
def view() -> KickstarterDashboard:
    """A Reactive View of the KickstarterDashboard"""
    return KickstarterDashboard().view()


if __name__.startswith("bokeh"):
    view().servable("Kickstarter Dashboard")
