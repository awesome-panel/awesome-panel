import param

from awesome_panel.designer.components import ReloadComponent
from awesome_panel.designer import components
import pytest
import panel as pn

class MyComponent(pn.Column):
        pass

def test_can_construct():
    reload_component = ReloadComponent()
    assert not reload_component.css_path
    assert not reload_component.js_path
    assert reload_component.component == components.EmptyComponent
    assert not reload_component.component_parameters
    assert isinstance(reload_component.component_instance, components.EmptyComponent)
    assert reload_component.modules_to_reload == []


def test_fixture_is_as_expected(
    reload_component, component, component_parameters, css_path, js_path
):
    isinstance(reload_component, ReloadComponent)

    assert reload_component.component == component
    assert reload_component.component_parameters == component_parameters
    assert reload_component.component_instance

    assert reload_component.css_path == css_path
    assert reload_component.js_path == js_path


# endregion
# region: Actions


def test_can_reload_component(reload_component):
    # Given: I have my reload_component with an existing component_instance
    old_instance = reload_component.component_instance
    # When: I reload the component
    reload_component.reload_component_instance()
    # Then: I have a new component instance
    assert reload_component.component_instance != old_instance

def test_can_reload_reactive_component(reload_component):
    # Given: MyComponent
    # When
    reload_component.component = MyComponent
    reload_component.reload_component_instance()
    # Then
    assert isinstance(reload_component.component_instance, MyComponent)


def test_can_reload_css_file(reload_component):
    reload_component.reload_css_file()


def test_can_reload_js_file(reload_component):
    reload_component.reload_js_file()


def test_has_view(reload_component):
    assert reload_component.view


def test_has_component_pane(reload_component):
    assert reload_component.component_pane


def test_has_designer_pane(reload_component):
    assert reload_component.designer_pane


def test_has_action_pane(reload_component):
    assert reload_component.action_pane


def test_has_settings_pane(reload_component):
    assert reload_component.settings_pane


def test_has_css_pane(reload_component):
    assert reload_component.css_pane is not None


def test_has_js_pane(reload_component):
    assert reload_component.js_pane is not None


def test_has_error_pane(reload_component):
    assert reload_component.error_pane