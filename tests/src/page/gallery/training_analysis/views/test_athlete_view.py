"""In this module we test the views in the athlete_view module"""

import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp
from src.pages.gallery.training_analysis.views.athlete_view import AthleteUpdateView


def test_athlete_edit_view():
    """The attributes of the Athlete can be edited"""
    return TestApp(test_athlete_edit_view, AthleteUpdateView(),)


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(pn.pane.Markdown(__doc__), test_athlete_edit_view(),)


if __name__.startswith("bk"):
    view().servable("test_athlete_view")
