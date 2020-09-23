"""In this module we model an activity

we chose to include the file of the activity as a attribute because

- An activity is very much it's activity (fit) file
- We would like to provide the user with the option of regaining the file of an Activity.
"""

import panel as pn
import param

from application.pages.training_analysis.plots import activity_plot
from application.pages.training_analysis.services import fit_file_services
from application.pages.training_analysis.views import activity_view
from application.pages.training_analysis.views.progress_view import progress


class Activity(param.Parameterized):
    """A model of an Activity

    Currently the Activity is based on data from a .fitfile
    """

    file = param.FileSelector(doc="A bytes object. Current only .fit files are supported")
    data = param.DataFrame(doc="The records of the file")

    @param.depends(
        "file",
        watch=True,
    )
    @progress.report(message="Parsing Activity File")
    def parse_file(
        self,
    ):
        """Converts the file to the training_data"""
        if self.file:
            self.data = fit_file_services.parse_fit_file(self.file)

    @param.depends("data")
    @progress.report(message="Creating Activity Plots")
    def activity_plots(
        self,
    ):
        """A layout of plots of the activity data. For example timestamp vs power.

        Returns:
            HoloViews: A layout of plots
        """
        return activity_plot.activity_plots(self.data)

    @param.depends("data")
    @progress.report(message="Creating Map")
    def map_plot(
        self,
    ):
        """The route on a map

        Returns:
                HoloViews: A plot of the route on a map.
        """
        return activity_plot.map_plot(self.data)

    def view(
        self,
    ) -> pn.viewable.Viewable:
        """A view of the Activity

        Returns:
            pn.viewable.Viewable: A view of the Activity
        """
        return activity_view.ActivityView(
            self.param,
            self.map_plot,
            self.activity_plots,
        )
