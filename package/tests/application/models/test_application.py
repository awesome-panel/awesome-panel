# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

from awesome_panel.application.models import Page, Template

def test_can_construct_application(application):
    # Then
    assert isinstance(application.title, str)
    assert isinstance(application.logo, str)
    assert isinstance(application.url, str)
    assert isinstance(application.pages, list)
    assert isinstance(application.default_page, Page)
    assert isinstance(application.templates, list)
    assert isinstance(application.default_template, Template)

