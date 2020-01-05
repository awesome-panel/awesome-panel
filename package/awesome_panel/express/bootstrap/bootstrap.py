"""Bootstrap inspired functionality"""
import panel as pn

from awesome_panel.express._pane._panes import Markdown
from awesome_panel.express.assets import BOOTSTRAP_PANEL_EXPRESS_CSS

BOOTSTRAP_CSS_URL = "https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"

_EXTENDED = False


def extend():
    """## Extends Panel with functionality to use Bootstrap Inspired components and styles

    See [Get Bootstrap](https://getbootstrap.com/).

    For examples see also [W3C Bootstrap Tutorial]
    (https://www.w3schools.com/bootstrap4/default.asp)

    - We don't use the bootstrap javascript like jquery, popper and bootstrap because it does not
    play well with the Bookeh Layout Engine
    """
    global _EXTENDED  # pylint: disable=global-statement
    if not _EXTENDED:
        pn.config.raw_css.append(BOOTSTRAP_PANEL_EXPRESS_CSS.read_text())
        # pn.config.css_files.append(BOOTSTRAP_CSS_URL)
        _EXTENDED = True


class InfoAlert(Markdown):
    """

    An Info Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-info'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See https://github.com/holoviz/panel/issues/829
    """

    def __init__(
        self, text: str, **kwargs,
    ):
        """An Info Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-info'

        Arguments:
            text {str} -- Some MarkDown text

        """
        if "css_classes" in kwargs:
            if not "alert" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert")
            if not "alert-info" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert-info")
        else:
            kwargs["css_classes"] = ["alert", "alert-info"]
        super().__init__(text, **kwargs)

    raw_css = """
.bk.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}

.bk.alert-info {
    color: #0c5460;
    background-color: #d1ecf1;
    border-color: #bee5eb;
}

.bk.alert-info hr {
    border-top-color: #abdde5;
}
"""


class WarningAlert(pn.pane.Markdown):
    """An Warning Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-warning'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See https://github.com/holoviz/panel/issues/829
    """

    def __init__(
        self, text: str, **kwargs,
    ):
        """A Warning Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-warning'

        Arguments:
            text {str} -- Some MarkDown text

        """
        if "css_classes" in kwargs:
            if not "alert" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert")
            if not "alert-warning" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert-warning")
        else:
            kwargs["css_classes"] = ["alert", "alert-warning"]
        super().__init__(text, **kwargs)

    raw_css = """
.bk.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}

.bk.alert-warning {
    color: #856404;
    background-color: #fff3cd;
    border-color: #ffeeba;
}

.bk.alert-warning hr {
    border-top-color: #ffe8a1;
}
"""


class ErrorAlert(pn.pane.Markdown):
    """An Error Alert that renders Markdown

    CSS Styling can be done via the classes 'alert' and 'alert-error'. See the raw_css attribute

    Don't set sizing_mode="stretch_width" as this will result in problems.
    See [Issue 829](https://github.com/holoviz/panel/issues/829)
    """

    def __init__(
        self, text: str, **kwargs,
    ):
        """An Error Alert that renders Markdown

        CSS Styling can be done via the classes 'alert' and 'alert-error'

        Arguments:
            text {str} -- Some MarkDown text

        """
        if "css_classes" in kwargs:
            if not "alert" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert")
            if not "alert-error" in kwargs["css_classes"]:
                kwargs["css_classes"].append("alert-error")
        else:
            kwargs["css_classes"] = ["alert", "alert-error"]
        super().__init__(text, **kwargs)

    raw_css = """
.bk.alert {
    position: relative;
    padding: 0.75rem 1.25rem;
    border: 1px solid transparent;
    border-radius: 0.25rem;
}

.bk.alert-error {
    color: #721c24;
    background-color: #f8d7da;
    border-color: #f5c6cb;
}

.bk.alert-error hr {
    border-top-color: #f1b0b7;
}
"""
