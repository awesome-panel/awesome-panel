"""## Tests of the Bootstrap Dashboard Components"""
import pytest

# pylint: disable=redefined-outer-name,protected-access
import panel as pn
from gallery.bootstrap_dashboard import components


@pytest.mark.panel
def test_about():
    """## Test of the Bootstrap Dashboard About Page

    - The image should have a suitable size.
    """
    about = components.About()
    about.servable("test_about")

if __name__.startswith("bk"):
    test_about()
