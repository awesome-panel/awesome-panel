"""The Training Analy_seriesis App provides functionality to

- upload a file
- view the route on a map
- see some basic metrics and charts
"""
# pylint: disable=duplicate-code
import pathlib
from typing import List, Optional, Union

import fitparse
import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn
import param
import plotly.express as px

from awesome_panel.express import ProgressExt
from src.pages.gallery.training_analysis.views.athlete_view import AthleteUpdateView
from src.pages.gallery.training_analysis.views.performance_curve_view import (
    PerformanceCurveUpdateView,
)

# pylint: enable=duplicate-code
pn.extension("plotly")
PROGRESS = ProgressExt()

UNIT_CONVERSION = {
    "speed": {"from": "10*6m/s", "to": "km/h", "factor": 0.0036},
    "enhanced_speed": {"from": "10*6m/s", "to": "km/h", "factor": 3.6},
    "altitude": {"from": "unknown", "to": "m", "factor": 0.03855343881175331},
    "position_long": {"from": "semicircles", "to": "degrees", "factor": (180.0 / 2 ** 31),},
    "position_lat": {"from": "semicircles", "to": "degrees", "factor": (180.0 / 2 ** 31),},
}

DEFAULT_FIT_FILE = pathlib.Path(__file__).parent / "files/zwift_watopia.fit"


class TrainingServices:
    """A Collection of services for working with training files and training data"""

    @classmethod
    def parse_fit_file(cls, file: Union[fitparse.base.FitFile, bytes, str]) -> pd.DataFrame:
        """Converts the bytes of a fit_file to a dataframe

        Args:
            file (Union[fitparse.base.FitFile, bytes, str]): The fit file to parse

        Raises:
            ValueError: If the file is not in a supported format

        Returns:
            pd.DataFrame: A DataFrame with the data
        """
        if isinstance(file, (bytes, str)):
            fit_file = fitparse.FitFile(file)
        elif isinstance(file, fitparse.base.FitFile):
            fit_file = file
        else:
            raise ValueError(f"{type(file)} is not supported!")

        return cls._parse_records(fit_file.get_messages("record"))

    @classmethod
    def _parse_records(cls, records):
        data = [record.get_values() for record in records]
        training_data = pd.DataFrame(data)
        cls._convert_units(training_data)
        return training_data

    @staticmethod
    def _convert_units(training_data_row: pd.DataFrame):
        columns = set(UNIT_CONVERSION.keys()).intersection(set(training_data_row.columns))
        for column in columns:
            training_data_row[column] *= UNIT_CONVERSION[column]["factor"]

    @staticmethod
    def plot(
        training_data: pd.DataFrame, x_series: str = "timestamp", y_series: str = "power",
    ):
        """Line plot of the training data

        Args:
            training_data (pd.DataFrame): A DataFrame with Training Data
            x_series (str, optional): The name of the column to show on the x-axis. Defaults to
            "timestamp".
            y_series (str, optional): The name of the column to show on the y-axis. Defaults to
            "power".

        Returns:
            HoloViews: A plot
        """
        return training_data.hvplot(x=x_series, y=y_series)

    @classmethod
    def plot_layout(
        cls,
        training_data: Optional[pd.DataFrame],
        x_series: Optional[List[str]] = None,
        y_series: Optional[List[str]] = None,
    ):
        """A layout of plots of the different measures like speed and power

        Args:
            training_data (Optional[pd.DataFrame]): The training data
            x_series (Optional[List[str]], optional): The column to plot on the x-axis. Defaults to
            None.
            y_series (Optional[List[str]], optional): The columns to plot on the y-axis. Defaults
            to None.

        Returns:
            HoloViews: A layout of multiple plots
        """
        if training_data is None or training_data.empty:
            return None
        if not x_series:
            x_series = ["timestamp"]
        if not y_series:
            y_series = ["power", "heart_rate", "speed", "cadence", "altitude"]

        plots = hv.Layout()
        for x_s in x_series:
            for y_s in y_series:
                plots += cls.plot(training_data, x_s, y_s)
        return plots.cols(1)

    @staticmethod
    def plot_map(  # pylint: disable=too-many-arguments
        training_data: Optional[pd.DataFrame],
        mapbox_style: str = "open-street-map",
        mapbox_zoom: int = 13,
        height: int = 400,
        width: int = 800,
        mode: str = "lines",
    ):
        """Plots the route onto a map

        Args:
            training_data (Optional[pd.DataFrame]): [description]
            mapbox_style (str, optional): [description]. Valid values are
            "open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain",
            "stamen-toner" or "stamen-watercolor". Defaults to "".
            mapbox_zoom (int, optional): The Zoom Level. Defaults to 13.
            height (int, optional): The height of the plot. Defaults to 400.
            width (int, optional): The width of the plot. Defaults to 800.
            mode (str, optional): The mode of the trace. Defaults to "lines".

        Returns:
            figure: A plot of the route on a map
        """
        if training_data is None or training_data.empty:
            return None
        position_lat_avg = training_data["position_lat"].mean()
        fig = px.scatter_mapbox(
            training_data,
            lat="position_lat",
            lon="position_long",
            color="power",
            color_continuous_scale=px.colors.cyclical.IceFire,
            height=height,
            width=width,
        )
        fig.update_traces(mode=mode)
        fig.update_layout(
            mapbox_style=mapbox_style,
            mapbox_zoom=mapbox_zoom,
            mapbox_center_lat=position_lat_avg,
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
        )
        return fig


class TrainingAnalysisApp(param.Parameterized):
    """The Training Analy_seriesis App enables a user to analyze his training and performance"""

    training_file = param.FileSelector()
    training_data = param.DataFrame()

    def __init__(self, training_file_path: Optional[pathlib.Path] = None, **kwargs):
        super().__init__(**kwargs)

        if training_file_path:
            self.training_file = training_file_path.read_bytes()

    @param.depends("training_file", watch=True)
    @PROGRESS.report(message="Parsing Training File")
    def parse_training_file(self):
        """Converts the training_file to the training_data"""
        self.training_data = TrainingServices.parse_fit_file(self.training_file)

    @param.depends("training_data")
    @PROGRESS.report(message="Parsing Training File")
    def plot_layout_view(self):
        """A layout of plots of the training data. For example timestamp vs power.

        Returns:
            HoloViews: A layout of plots
        """
        return TrainingServices.plot_layout(self.training_data)

    @param.depends("training_data")
    @PROGRESS.report(message="Creating Map")
    def plot_map_view(self):
        """The route on a map

        Returns:
                HoloViews: A plot of the route on a map.
        """
        return TrainingServices.plot_map(self.training_data)

    def view(self):
        """The main view of the TrainingAnalysisApp"""
        activity_view = pn.Column(
            pn.Param(
                self.param.training_file,
                widgets={"training_file": {"type": pn.widgets.FileInput, "accept": ".fit"}},
            ),
            PROGRESS.view,
            self.plot_map_view,
            self.plot_layout_view,
            sizing_mode="stretch_both",
        )
        athlete_view = pn.Tabs(
            ("General", AthleteUpdateView()), ("Power Curve", PerformanceCurveUpdateView())
        )

        return pn.Tabs(("Activity", activity_view), ("Athlete", athlete_view),)


def view(training_file_path: Optional[pathlib.Path] = None):
    """Run this to run the application"""
    return TrainingAnalysisApp(training_file_path=training_file_path).view()


if __name__.startswith("bk"):
    view(DEFAULT_FIT_FILE).servable()
