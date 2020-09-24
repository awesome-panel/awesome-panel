"""In this module we test the views in the performance_view module"""

import awesome_panel.express as pnx
import panel as pn
from awesome_panel.express.testing import TestApp

from application.pages.training_analysis.views.performance_curve_view import (
    PerformanceCurveUpdateView,
)


def test_performance_curve_update_view():
    """The attributes of the Athlete can be edited"""
    return TestApp(
        test_performance_curve_update_view,
        PerformanceCurveUpdateView(),
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        pn.pane.Markdown(__doc__),
        test_performance_curve_update_view(),
    )


if __name__.startswith("bokeh"):
    view().servable("test_performance_curveview")
