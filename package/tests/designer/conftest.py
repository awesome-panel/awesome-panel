# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pathlib

import pytest
from awesome_panel.designer import Designer
from awesome_panel.designer.components.component_with_error import ComponentWithError
from awesome_panel.designer.services import ReloadService

from .fixtures.component import Component

FIXTURES = pathlib.Path(__file__).parent / "fixtures"
COMPONENT_CSS = FIXTURES / "component.css"
COMPONENT_JS = FIXTURES / "component.js"


@pytest.fixture
def css_path():
    return COMPONENT_CSS


@pytest.fixture
def js_path():
    return COMPONENT_JS


@pytest.fixture
def modules_to_reload():
    return []


@pytest.fixture
def component():
    return Component


@pytest.fixture
def component_with_error():
    return ComponentWithError


@pytest.fixture
def component_parameters(css_path, js_path, modules_to_reload):
    return {
        "css_path": css_path,
        "js_path": js_path,
        "modules_to_reload": modules_to_reload,
    }


@pytest.fixture
def reload_service(component, css_path, js_path, component_parameters):
    return ReloadService(
        component=component,
        css_path=css_path,
        js_path=js_path,
        component_parameters=component_parameters,
    )


@pytest.fixture
def reload_service_with_error(component_with_error):
    return ReloadService(component=component_with_error)


@pytest.fixture
def reload_services(reload_service, reload_service_with_error):
    return [reload_service, reload_service_with_error]


@pytest.fixture
def designer(reload_services):
    return Designer(reload_services=reload_services)
