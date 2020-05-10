import param

from awesome_panel.designer.panel_designer_app import PanelDesignerApp
from awesome_panel.designer import components
import pytest
import panel as pn

class MyComponent(pn.Column):
        pass

def test_can_construct_fixture(
    panel_designer_app, reload_services
):
    isinstance(panel_designer_app, PanelDesignerApp)
    assert panel_designer_app.param.reload_service.objects == reload_services


# endregion
# region: Actions


def test_has_view(panel_designer_app):
    assert panel_designer_app.view


def test_has_component_pane(panel_designer_app):
    assert panel_designer_app.component_pane


def test_has_designer_pane(panel_designer_app):
    assert panel_designer_app.designer_pane


def test_has_action_pane(panel_designer_app):
    assert panel_designer_app.action_pane


def test_has_settings_pane(panel_designer_app):
    assert panel_designer_app.settings_pane


def test_has_css_pane(panel_designer_app):
    assert panel_designer_app.css_pane is not None


def test_has_js_pane(panel_designer_app):
    assert panel_designer_app.js_pane is not None

def test_has_error_pane(panel_designer_app):
    assert panel_designer_app.error_pane