# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
from awesome_panel.designer.designer import Designer


class MyComponent(pn.Column):
    pass


def test_can_construct_fixture(designer, reload_services):
    isinstance(designer, Designer)
    assert designer.param.reload_service.objects == reload_services


# endregion
# region: Actions


def test_has_view(designer):
    assert designer.view


def test_has_component_pane(designer):
    assert designer.component_pane


def test_has_designer_pane(designer):
    assert designer.designer_pane


def test_has_action_pane(designer):
    assert designer.action_pane


def test_has_settings_pane(designer):
    assert designer.settings_pane


def test_has_css_pane(designer):
    assert designer.css_pane is not None


def test_has_js_pane(designer):
    assert designer.js_pane is not None


def test_has_error_pane(designer):
    assert designer.error_pane
