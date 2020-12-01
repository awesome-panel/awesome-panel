"""The Panel Component Explorer App helps you discover and learn about the Panel Components

I hope this can speed up the process of learning the power of Panel.

The Component Explorer currently supports the components that I have styled in the
[Fast.design](https://fast.design) style. I am in the process of adding the rest.
"""
import panel as pn
from awesome_panel_extensions.developer_tools.test_apps import PanelComponentExplorer

from application.config import site

APPLICATION = site.create_application(
    url="panel-component-explorer",
    name="Component Explorer",
    author="Marc Skov Madsen",
    introduction="An app for discovering and learning about the Panel components",
    description=__doc__,
    thumbnail_url="panel-component-explorer.png",
    code_url="panel_component_explorer.py",
    tags=["Panel", "Components"],
)


@site.add(APPLICATION)
def view():
    """Returns the Panel Component Explorer App"""
    pn.config.sizing_mode = "stretch_width"
    app = PanelComponentExplorer()
    app.view.main.insert(0, APPLICATION.intro_section())
    return app.view


if __name__.startswith("bokeh"):
    view().servable()
