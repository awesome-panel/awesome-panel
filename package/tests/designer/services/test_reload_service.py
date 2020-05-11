# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import param

from awesome_panel.designer.services import ReloadService


class MyComponent(pn.Column):
    pass


class ComponentWithError(pn.Column):
    def __init__(self, **params):
        super().__init__(**params)
        raise ValueError()


def test_can_construct_fixture(reload_service):
    assert isinstance(reload_service, ReloadService)


def test_can_reload_component(reload_service, component):
    # Given: I have my reload_service with an existing component_instance
    old_instance = reload_service.component_instance
    # When: I reload the component
    reload_service.reload_component()
    new_instance = reload_service.component_instance
    # Then: I have a new component instance
    assert not reload_service.error_message
    assert isinstance(new_instance, component)
    assert reload_service.component_instance != old_instance


def test_can_reload_reactive_component(reload_service):
    # Given: MyComponent
    old_instance = reload_service.component_instance
    # When
    reload_service.component = MyComponent
    reload_service.reload_component()
    new_instance = reload_service.component_instance
    # Then: I have a new component instance
    assert not reload_service.error_message
    assert isinstance(new_instance, MyComponent)
    assert reload_service.component_instance != old_instance


def test_can_reload_css_file(reload_service):
    # Given
    reload_service.css_text = "dummy"
    # When
    reload_service.reload_css_file()
    # Then
    assert reload_service.css_text != "dummy"


def test_can_reload_js_file(reload_service):
    # Given
    reload_service.js_text = "dummy"
    # When
    reload_service.reload_js_file()
    # Then
    assert reload_service.js_text != "dummy"


def test_can_communicate_reloading_progress(reload_service):
    assert isinstance(reload_service.param.reloading, param.Boolean)


def test_can_handle_reload_error(reload_service):
    # Given
    reload_service.component = ComponentWithError
    # When
    reload_service.reload_component()
    # Then
    assert reload_service.error_message
