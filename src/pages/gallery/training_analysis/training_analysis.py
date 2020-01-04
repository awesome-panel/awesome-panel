"""The Training Analysis App provides functionality to

- upload a file
- view the route on a map
- see some basic metrics and charts
"""
import pathlib
from typing import List, Optional, Union

import fitparse
import holoviews as hv
import hvplot.pandas
import pandas as pd
import panel as pn
import param
import plotly.express as px

pn.extension("plotly")

UNIT_CONVERSION = {
PROGRESS = ProgressExt()
    "enhanced_speed": {"from": "10*6m/s", "to": "km/h", "factor": 3.6},
    "altitude": {"from": "unknown", "to": "m", "factor": 0.03855343881175331},
    "position_long": {"from": "semicircles", "to": "degrees", "factor": (180.0 / 2 ** 31)},
    "position_lat": {"from": "semicircles", "to": "degrees", "factor": (180.0 / 2 ** 31)},
}

DEFAULT_FIT_FILE = pathlib.Path(__file__).parent / "files/zwift_watopia.fit"


class ProgressWithMessage(param.Parameterized):
    value = param.Integer()
    message = param.String()
    bar_color = param.String("info")

    def update(self, value: int, message: str):
        self.value = value
        self.message = message

    def reset(self):
        self.value = 0
        self.message = ""

    @param.depends("value", "message", "bar_color")
    def view(self):
        print("a")
        content = []
        if self.value:
            content.append(
                pn.widgets.Progress(value=self.value, bar_color=self.bar_color, align="center")
            )
        elif self.message:
            content.append(pn.widgets.Progress(active=True))
        if self.message:
            content.append(pn.pane.Str(self.message))
        return pn.Row(*content, sizing_mode="stretch_width")


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
        if isinstance(file, bytes) or isinstance(file, str):
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
    def plot(training_data: pd.DataFrame, x: str = "timestamp", y: str = "power"):
        return training_data.hvplot(x=x, y=y)

    @classmethod
    def plot_layout(
        cls,
        training_data: Optional[pd.DataFrame],
        xs: List[str] = ["timestamp"],
        ys: List[str] = ["power", "heart_rate", "speed", "cadence", "altitude"],
    ):
        if training_data is None or training_data.empty:
            return None

        plots = hv.Layout()
        for x in xs:
            for y in ys:
                plots += cls.plot(training_data, x, y)
        return plots.cols(1)

    @staticmethod
    def plot_map(
        training_data: Optional[pd.DataFrame],
        mapbox_style="open-street-map",
        mapbox_zoom=13,
        height=400,
        width=800,
        mode="lines",
    ):
        """Plots the training_data onto a map

        Args:
            training_data (Optional[pd.DataFrame]): [description]
            mapbox_style (str, optional): [description]. Valid values are
            "open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain",
            "stamen-toner" or "stamen-watercolor". Defaults to "".
            mapbox_zoom (int, optional): The Zoom Level. Defaults to 13.
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
            width=800,
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
    """The Training Analysis App enables a user to analyze his training and performance"""

    training_file = param.FileSelector()
    training_data = param.DataFrame()
    progress = param.ClassSelector(class_=ProgressWithMessage, default=ProgressWithMessage())

    def __init__(self, training_file_path: Optional[pathlib.Path] = None, **kwargs):
        super().__init__(**kwargs)

        if training_file_path:
            self.training_file = training_file_path.read_bytes()

    @param.depends("training_file", watch=True)
    def parse_training_file(self):
        """Converts the training_file to the training_data"""
        self.progress.message = "Parsing Training File"
        self.training_data = TrainingServices.parse_fit_file(self.training_file)
        self.progress.reset()

    @param.depends("training_data")
    def plots_view(self):
        self.progress.message = "Creating Performance Plots"
        plot = TrainingServices.plot_layout(self.training_data)
        self.progress.reset()
        return plot

    @param.depends("training_data")
    def plot_map(self):
        self.progress.message = "Creating Map"
        plot = TrainingServices.plot_map(self.training_data)
        self.progress.reset()
        return plot

    def view(self):
        """The main view of the TrainingAnalysisApp"""
        return pn.Column(
            pn.Param(
                self.param.training_file,
                widgets={"training_file": {"type": pn.widgets.FileInput, "accept": ".fit"}},
            ),
            self.progress.view,
            self.plot_map,
            self.plots_view,
            sizing_mode="stretch_both",
        )


def view(training_file_path: Optional[pathlib.Path] = None):
    """Run this to run the application"""
    return TrainingAnalysisApp(training_file_path=training_file_path).view()


if __name__.startswith("bk"):
    view().servable()
