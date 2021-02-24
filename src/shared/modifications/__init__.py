"""Contains various modifications, fixes, workarounds and hacks of Panel and other packages to
enable running this site.

Run the `src.modifications.apply` function to apply the modifications"""
import panel as pn
from awesome_panel_extensions.widgets.button import AwesomeButton

from ._server import get_server


def apply():
    """Applies all modifications.

    - Panel fixes
    - Load of awesome-panel-assets .js lib

    Run this before starting the server"""
    # Improvement to be able to pn.serve .py and ipynb files
    pn.io.server.get_server = get_server

    # Hack to get awesome-panel-extensions .js library loaded
    AwesomeButton()
