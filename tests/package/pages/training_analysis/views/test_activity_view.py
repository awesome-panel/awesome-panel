"""Test of the activity_view module"""
# pylint: disable=redefined-outer-name,protected-access
import panel as pn
import param

from application.pages.training_analysis.views import activity_view
from awesome_panel.express.testing import TestApp


def test_activity_view():
    """Test of the ActivityView constructor"""
    # Given
    class ActivityMock(param.Parameterized):
        """Mock of Activity Class"""

        file = param.FileSelector()

    view = activity_view.ActivityView(
        ActivityMock().param,
        "map_plot mock",
        "activity_plots mock",
    )
    return TestApp(
        test_activity_view,
        view,
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(test_activity_view())


if __name__.startswith("bokeh"):
    view().servable()
