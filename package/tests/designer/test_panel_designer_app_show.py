import pathlib

import panel as pn
import param
import pytest

from awesome_panel.designer.panel_designer_app import PanelDesignerApp
from awesome_panel.designer import components

FIXTURES = pathlib.Path(__file__).parent / "fixtures"
COMPONENT_CSS = FIXTURES / "component.css"
COMPONENT_JS = FIXTURES / "component.js"

COMPONENT_CONFIG = {
    components.TitleComponent: {
        "component": components.TitleComponent,
        "css_path": COMPONENT_CSS,
        "js_path": COMPONENT_JS,
    },
    components.CenteredComponent: {
        "component": components.CenteredComponent,
        "css_path": COMPONENT_CSS,
        "js_path": COMPONENT_JS,
        "component_parameters": {
            "component": components.TitleComponent()
        }
    }
}

def test_app():
    component = components.TitleComponent
    config = COMPONENT_CONFIG[component]
    return PanelDesignerApp(
        **config
    ).show()

if __name__.startswith("__main__") or __name__.startswith("bokeh"):
    test_app()