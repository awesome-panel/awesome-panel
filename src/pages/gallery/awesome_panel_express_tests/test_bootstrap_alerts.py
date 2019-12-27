"""Tests of the Alert panes inspired by Bootstrap Alerts.

Please note that in order to use the bootstrap functionality you need to run
`awesome_panel.express.bootstrap.extend()` to import the relevant css.

Please note the css and javascript of Bootstrap and does not play well with Panel/ Bokeh in my
experience.

- The JavaScript we cannot use as it confuses the Bokeh layout engine
- The CSS has to be rewritten. So that is what I have to done the few things I need.
"""
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp

pnx.bootstrap.extend()


def test_info_alert():
    """We can show an InfoAlert

    - Blue Div with normal and bold text
    - Curently not full width
    """
    return TestApp(
        test_info_alert, pnx.InfoAlert("This is an **Info Alert**!"), sizing_mode="stretch_width",
    )


def test_warning_alert():
    """We can show a Warning Alert

    - Yellow Div with normal and bold text
    - Curently not full width
    """
    return TestApp(
        test_warning_alert,
        pnx.WarningAlert("This is a **Warning Alert**!"),
        sizing_mode="stretch_width",
    )


def test_error_alert():
    """We can show an Error Alert

    - Red Div with normal and bold text
    - Curently not full width
    """
    return TestApp(
        test_error_alert,
        pnx.ErrorAlert("This is an **Error Alert**!"),
        sizing_mode="stretch_width",
    )


def test_info_alert_height_problem():
    """The Bokeh Layout Engine does not layout the height of the Markdown Alerts very well.

    We see that the height of the InfoAlert is much greater than it needs to be. This is a general
    problem for the Panel Markdown pane. See [Issue 829](https://github.com/holoviz/panel/issues/829)
    """
    text = """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced."""
    return TestApp(
        test_info_alert_height_problem,
        pnx.InfoAlert(text, sizing_mode="stretch_width"),
        sizing_mode="stretch_width",
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        pnx.Markdown(__doc__),
        test_info_alert(),
        test_error_alert(),
        test_warning_alert(),
        test_info_alert_height_problem(),
        sizing_mode="stretch_width",
    )


if __name__.startswith("bk"):
    view().servable()
