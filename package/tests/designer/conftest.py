from awesome_panel.designer import PanelDesignerApp
import pathlib
import pytest
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
    return PanelDesignerApp

@pytest.fixture
def component_parameters(css_path, js_path, modules_to_reload):
    return {
        "css_path": css_path,
        "js_path": js_path,
        "modules_to_reload": modules_to_reload,
    }

@pytest.fixture
def panel_designer_app(css_path, js_path, modules_to_reload, component, component_parameters):
    return PanelDesignerApp(
        component=component,
        component_parameters=component_parameters,
        css_path=css_path,
        js_path=js_path,
        modules_to_reload=modules_to_reload,
    )