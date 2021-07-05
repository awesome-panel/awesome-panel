"""Alert panes inspired by Bootstrap Alerts.

This example was originally created to show how to create custom Bootstrap Alerts.
The Alerts have now been contributed to Panel. You can find the reference example
[here](https://panel.holoviz.org/reference/panes/Alert.html).
"""
import panel as pn
from awesome_panel.express.testing import TestApp

from awesome_panel_extensions.site import site

APPLICATION = site.create_application(
    url="bootstrap-alerts",
    name="Bootstrap Alerts",
    author="Marc Skov Madsen",
    description="Demonstrates the look and feel of the Panel Alerts",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/test_bootstrap_alerts.png",
    resources = {
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/awesome_panel_express_tests/test_bootstrap_alerts.py",
    },
    tags=["Bootstrap"],
)


def test_info_alert():
    """
    We can show an InfoAlert

    - Blue Div with normal and bold text
    - Full width by default
    - With a nice bottom margin
    """
    return TestApp(
        test_info_alert,
        pn.pane.Alert("This is an **Info Alert**!"),
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
        pn.pane.Alert("This is a **Warning Alert**!", alert_type="warning"),
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
        pn.pane.Alert("This is an **Error Alert**!", alert_type="danger"),
        sizing_mode="stretch_width",
    )


@site.add(APPLICATION)
def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    pn.config.sizing_mode = "stretch_width"
    main = [
        APPLICATION.intro_section(),
        test_info_alert(),
        test_error_alert(),
        test_warning_alert(),
    ]
    return pn.template.FastListTemplate(title="Test Bootstrap Alerts", main=main)


if __name__.startswith("bokeh"):
    view().servable()
