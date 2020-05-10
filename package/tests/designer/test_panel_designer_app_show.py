import pathlib

import panel as pn
import param
import pytest

from awesome_panel.designer import PanelDesignerApp, services, components
from awesome_panel.express import Card
from awesome_panel.express.assets import BOOTSTRAP_PANEL_EXPRESS_CSS
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
STOPPED_COMPONENT = services.ReloadService(
    component=components.StoppedComponent,
    css_path=COMPONENT_CSS,
    js_path=COMPONENT_JS,
)
CARD_COMPONENT = services.ReloadService(
    component=Card,
    css_path=BOOTSTRAP_PANEL_EXPRESS_CSS,
    js_path=COMPONENT_JS,
    component_parameters={"header": "Test Card", "body": pn.pane.Markdown("Awesome Panel "*50), "collapsable": True},
)


RELOAD_SERVICES = [
    TITLE_COMPONENT,
    EMPTY_COMPONENT,
    CENTERED_COMPONENT,
    STOPPED_COMPONENT,
    CARD_COMPONENT,
]


def test_app():
    return PanelDesignerApp(
        reload_services=RELOAD_SERVICES
    ).show()


if __name__.startswith("__main__") or __name__.startswith("bokeh"):
    test_app()
