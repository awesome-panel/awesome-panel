# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import param

from awesome_panel.application import models


def test_can_construct_application_without_exceptions(application):
    # Then
    assert isinstance(application.title, str)
    assert isinstance(application.logo, str)
    assert isinstance(application.url, str)
    assert issubclass(application.template, pn.Template)

    assert "page" in application.param
    assert isinstance(application.page, models.Page)
    assert isinstance(application.param.page.default, models.Page)

    assert "menu_item" in application.param
    assert not application.menu_item
    assert isinstance(application.param.menu_item, param.ObjectSelector)

    assert "source_link" in application.param
    assert not application.source_link
    assert isinstance(application.param.source_link, param.ObjectSelector)

    assert "social_link" in application.param
    assert not application.social_link
    assert isinstance(application.param.social_link, param.ObjectSelector)

    assert "progress" in application.param
    assert isinstance(application.progress, models.Progress)

    assert "message" in application.param
    assert isinstance(application.message, models.Message)
