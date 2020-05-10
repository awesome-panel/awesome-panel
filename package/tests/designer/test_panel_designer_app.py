import param

from awesome_panel.designer.panel_designer_app import PanelDesignerApp
from awesome_panel.designer import components
import pytest
import panel as pn

class MyComponent(pn.Column):
        pass

def test_can_construct():
    panel_designer_app = PanelDesignerApp()
    assert panel_designer_app.title_component is not None
    assert not panel_designer_app.css_path
    assert not panel_designer_app.js_path
    assert panel_designer_app.component == components.EmptyComponent
    assert not panel_designer_app.component_parameters
    assert isinstance(panel_designer_app.component_instance, components.EmptyComponent)
    assert panel_designer_app.modules_to_reload == []


def test_fixture_is_as_expected(
    panel_designer_app, component, component_parameters, css_path, js_path
):
    isinstance(panel_designer_app, PanelDesignerApp)

    assert panel_designer_app.component == component
    assert panel_designer_app.component_parameters == component_parameters
    assert panel_designer_app.component_instance

    assert panel_designer_app.css_path == css_path
    assert panel_designer_app.js_path == js_path


# endregion
# region: Actions


def test_can_reload_component(panel_designer_app):
    # Given: I have my panel_designer_app with an existing component_instance
    old_instance = panel_designer_app.component_instance
    # When: I reload the component
    panel_designer_app.reload_component_instance()
    # Then: I have a new component instance
    assert panel_designer_app.component_instance != old_instance

def test_can_reload_reactive_component(panel_designer_app):
    # Given: MyComponent
    # When
    panel_designer_app.component = MyComponent
    panel_designer_app.reload_component_instance()
    # Then
    assert isinstance(panel_designer_app.component_instance, MyComponent)


def test_can_reload_css_file(panel_designer_app):
    panel_designer_app.reload_css_file()


def test_can_reload_js_file(panel_designer_app):
    panel_designer_app.reload_js_file()


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