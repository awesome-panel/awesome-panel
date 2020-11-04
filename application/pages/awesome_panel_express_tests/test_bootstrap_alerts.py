"""Tests of the Alert panes inspired by Bootstrap Alerts.

Please note that in order to use the bootstrap functionality you need to run
`awesome_panel.express.bootstrap.extend()` to import the relevant css.

Please note the css and javascript of Bootstrap and does not play well with Panel/ Bokeh in my
experience.

- The JavaScript we cannot use as it confuses the Bokeh layout engine
- The CSS has to be rewritten. So that is what I have to done the few things I need.
"""
import awesome_panel.express as pnx
import panel as pn
from awesome_panel.express.testing import TestApp

from application.config import site

pnx.bootstrap.extend()


def test_info_alert():
    """
    We can show an InfoAlert

    - Blue Div with normal and bold text
    - Full width by default
    - With a nice bottom margin
    """
    return TestApp(
        test_info_alert,
        pnx.InfoAlert("This is an **Info Alert**!"),
        sizing_mode="stretch_width",
    )


def test_warning_alert():
    """We can show a Warning Alert

    - Yellow Div with normal and bold text
    - Full width by default
    - With a nice bottom margin
    """
    return TestApp(
        test_warning_alert,
        pnx.WarningAlert("This is a **Warning Alert**!"),
        sizing_mode="stretch_width",
    )


def test_error_alert():
    """We can show an Error Alert

    - Red Div with normal and bold text
    - Full width by default
    - With a nice bottom margin
    """
    return TestApp(
        test_error_alert,
        pnx.ErrorAlert("This is an **Error Alert**!"),
        sizing_mode="stretch_width",
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    pn.config.sizing_mode = "stretch_width"
    main = [
        pn.pane.Markdown(__doc__),
        test_info_alert(),
        test_error_alert(),
        test_warning_alert(),
    ]
    return site.get_template(title="Test Bootstrap Alerts", main=main)


if __name__.startswith("bokeh"):
    view().servable()
