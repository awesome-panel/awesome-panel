"""The Panel Component Explorer App helps you discover and learn about the Panel Components

I hope this can speed up the process of learning the power of Panel.

The Component Explorer currently supports the components that I have styled in the
[Fast.design](https://fast.design) style. I am in the process of adding the rest.
"""
import panel as pn
from awesome_panel_extensions.developer_tools.test_apps import PanelComponentExplorer

from awesome_panel_extensions.site import site

APPLICATION = site.create_application(
    url="panel-component-explorer",
    name="Component Explorer",
    author="Marc Skov Madsen",
    description="An app for discovering and learning about the Panel components",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/panel-component-explorer.png",
    resources = {
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/panel_component_explorer.py",
    },
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
