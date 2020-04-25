## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.models import Page
import pytest

def test_page_has_top_bar(page):
    assert "top_bar" in page.param

def test_page_has_sidebar(page):
    assert "sidebar" in page.param

def test_page_has_main(page):
    assert "main" in page.param