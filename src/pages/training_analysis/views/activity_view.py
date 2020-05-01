"""This module provides Views of Activities"""
import panel as pn
import param


class ActivityView(pn.Column):
    """A View of an Activity

    Args:
        parameters (param.parameterized.Parameters): A set of parameters containing a
        file parameter
        map_plot (pn.Viewable): A plot of an activity
        activity_plots (pn.Viewable): Plots of the activity
    """

    def __init__(
        self,
        parameters: param.parameterized.Parameters,
        map_plot: pn.viewable.Viewable,
        activity_plots: pn.viewable.Viewable,
    ):
        super().__init__(
            pn.Param(
                parameters.file,
                widgets={"file": {"type": pn.widgets.FileInput, "accept": ".fit",}},
            ),
            map_plot,
            activity_plots,
            sizing_mode="stretch_both",
        )
