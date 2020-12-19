import awesome_panel_extensions
import panel as pn
from awesome_panel_extensions.widgets.button import AwesomeButton

button = AwesomeButton()


def view():
    pn.Column(
        pn.pane.Markdown("Hello World"),
    )


PREFIX = "sub/subsub"
ROUTES = {"": view}

pn.serve(ROUTES, port=5007, prefix=PREFIX)
