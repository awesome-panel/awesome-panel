## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
import awesome_panel.models as models
import pytest
import panel as pn
import param

def test_can_construct_application_without_exceptions(application):
    pass

def test_application_has_template(application):
    assert isinstance(application.template, pn.Template)

def test_application_has_theme(application):
    assert isinstance(application.theme, models.Theme)

def test_application_has_title(application):
    isinstance(application.title, str)

def test_application_has_logo(application):
    isinstance(application.logo, str)

def test_application_has_url(application):
    isinstance(application.url, str)

def test_application_has_page(application):
    assert "page" in application.param
    assert isinstance(application.page, models.Page)
    assert isinstance(application.param.page.default, models.Page)

def test_application_has_menu_item(application):
    assert "menu_item" in application.param
    assert not application.menu_item
    assert isinstance(application.param.menu_item, param.ObjectSelector)


def test_application_has_source_link(application):
    assert "source_link" in application.param
    assert not application.source_link
    assert isinstance(application.param.source_link, param.ObjectSelector)

def test_application_has_social_link(application):
    assert "social_link" in application.param
    assert not application.social_link
    assert isinstance(application.param.social_link, param.ObjectSelector)

def test_application_has_progress(application):
    assert "progress" in application.param
    assert isinstance(application.progress, models.Progress)

def test_application_has_message(application):
    assert "message" in application.param
    assert isinstance(application.message, models.Message)