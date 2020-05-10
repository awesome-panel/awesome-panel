import pathlib

import panel as pn
import param
import pytest

from awesome_panel.designer import PanelDesignerApp, services, components


FIXTURES = pathlib.Path(__file__).parent / "fixtures"
COMPONENT_CSS = FIXTURES / "component.css"
COMPONENT_JS = FIXTURES / "component.js"
COMPONENT2_JS = FIXTURES / "component2.js"

TITLE_COMPONENT = services.ReloadService(
    component=components.TitleComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
)
EMPTY_COMPONENT = services.ReloadService(
    component=components.EmptyComponent, css_path=COMPONENT_CSS, js_path=COMPONENT2_JS,
)
CENTERED_COMPONENT = services.ReloadService(
    component=components.CenteredComponent,
    css_path=COMPONENT_CSS,
    js_path=COMPONENT_JS,
    component_parameters={"component": components.TitleComponent()},
)

RELOAD_SERVICES = [
    TITLE_COMPONENT,
    EMPTY_COMPONENT,
    CENTERED_COMPONENT,
]


def test_app():
    return PanelDesignerApp(
        reload_services=RELOAD_SERVICES
    ).show()


if __name__.startswith("__main__") or __name__.startswith("bokeh"):
    test_app()
