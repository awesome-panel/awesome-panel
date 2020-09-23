"""The Training Analy_seriesis App provides functionality to

- upload a file
- view the route on a map
- see some basic metrics and charts
"""
# pylint: disable=duplicate-code
import pathlib
from typing import Optional

import hvplot.pandas  # pylint: disable=unused-import
import panel as pn

from application.pages.training_analysis.models.activity import Activity

# pylint: enable=duplicate-code
pn.extension("plotly")
DEFAULT_FIT_FILE = pathlib.Path(__file__).parent / "assets/files/zwift_watopia.fit"


class TrainingAnalysisApp(pn.Column):
    """The Training Analy_seriesis App enables a user to analyze his training and performance"""

    def __init__(self, activity_file: Optional[pathlib.Path] = None, **kwargs):
        self.activity = Activity()
        if activity_file:
            self.activity.file = activity_file.read_bytes()

        super().__init__(self.activity, **kwargs)


def view(
    activity_file: Optional[pathlib.Path] = None,
):
    """Run this to run the application"""
    return TrainingAnalysisApp(activity_file=activity_file)


if __name__.startswith("bokeh"):
    view(DEFAULT_FIT_FILE).servable()
