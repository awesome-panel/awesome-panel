"""Test All routes"""
import pytest

from application.pages import APP_ROUTES


@pytest.mark.parametrize("app_view", APP_ROUTES.values())
def test_page_can_be_constucted(app_view):
    """Test an app view"""
    # Given an app view

    # When we initialize it
    app_view()

    # Then everything should be fine
