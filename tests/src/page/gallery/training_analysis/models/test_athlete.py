"""In this module we test the Athlete model"""

from src.pages.gallery.training_analysis.models.athlete import Athlete


def test_constructor():
    """An Athlete model exists and can be constructed"""
    assert Athlete(name="Olga").name
