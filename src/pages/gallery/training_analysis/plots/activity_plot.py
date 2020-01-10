"""This module contains functionality to plot an Activity"""
from typing import List, Union, Optional

import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import plotly.express as px

DEFAULT_X_SERIES = ["timestamp"]
DEFAULT_Y_SERIES = ["power", "cadence"]


def map_plot(data: Union[pd.DataFrame, None]):
    """A map plotting the activity

    Args:
        data (pd.DataFrame): A DataFrame with columns 'lat' and 'long' sorted by time \
            ascending

    Returns:
        Plot: A plot showing a map of the activity route
    """
    if data is None or data.empty:
        return None

    fig = px.scatter_mapbox(data, lat="lat", lon="long")
    return fig


def activity_plot(data: pd.DataFrame, x_series: str = "timestamp", y_series: str = "power"):
    """A plot of two columns of the Activity Data

    Args:
        data (pd.DataFrame): [description]
        x_series (str, optional): The series on the x-axis. Defaults to "timestamp".
        y_series (str, optional): The series on the y-axis. Defaults to "power".

    Returns:
        Plot: A plot
    """
    return data.hvplot(x=x_series, y=y_series)


def activity_plots(
    data: Union[pd.DataFrame, None],
    x_series: Optional[List[str]] = None,
    y_series: Optional[List[str]] = None,
) -> hv.Layout:
    """A layout of plots

    Args:
        data (pd.DataFrame): The Activity Data
        x_series (Optional[List[str]]): The series to show on the x-axis. Defaults to \
            DEFAULT_X_SERIES.
        y_series (Optional[List[str]]): The series to show on the y-axis. Defaults to \
            DEFAULT_Y_SERIES.

    Returns:
        hv.Layout: A layout of plots
    """
    if data is None or data.empty:
        return None
    if not x_series:
        x_series = DEFAULT_X_SERIES
    if not y_series:
        y_series = DEFAULT_Y_SERIES

    layout = hv.Layout()

    for xss in x_series:
        for yss in y_series:
            layout.items.append(activity_plot(data, xss, yss))
    return layout
