"""## Tests of the Bootstrap Dashboard Components"""
# pylint: disable=redefined-outer-name,protected-access
import panel as pn
import pytest

from gallery.bootstrap_dashboard import components
from awesome_panel.express.

@pytest.mark.panel
def test_about():
    """## Test of the Bootstrap Dashboard About Page

    - The image should have a suitable size.
    """
    about = components.About()
    about.servable("test_about")


@pytest.mark.panel
def test_dashboard_plot():
    """Manual test that the width of the chart is full width"""
    dashboard = components.Dashboard()
    column = pn.Column(dashboard._chart_plotly(), width_policy="max", background="red")
    column.servable("test_dashboard_blot")


if __name__.startswith("bk"):
    test_about()
    test_dashboard_plot()
