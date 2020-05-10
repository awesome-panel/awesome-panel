import pathlib

import panel as pn
import param
import pytest

from awesome_panel.designer import PanelDesignerApp, models, components


FIXTURES = pathlib.Path(__file__).parent / "fixtures"
COMPONENT_CSS = FIXTURES / "component.css"
COMPONENT_JS = FIXTURES / "component.js"

TITLE_COMPONENT = models.ComponentConfiguration(
    component=components.TitleComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
)
CENTERED_COMPONENT = models.ComponentConfiguration(
    component=components.CenteredComponent,
    css_path=COMPONENT_CSS,
    js_path=COMPONENT_JS,
    parameters={"component": components.TitleComponent()},
)

COMPONENT_CONFIGS = [
    TITLE_COMPONENT,
    CENTERED_COMPONENT,
]


def test_app():
    config = TITLE_COMPONENT
    return PanelDesignerApp(
        component=config.component,
        css_path=config.css_path,
        js_path=config.js_path,
        component_parameters=config.parameters,
    ).show()


if __name__.startswith("__main__") or __name__.startswith("bokeh"):
    test_app()
