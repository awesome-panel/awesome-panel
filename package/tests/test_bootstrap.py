"""Tests of the bootstrap inspired functionality"""
import pytest

import awesome_panel.express as pnx
import panel as pn

pnx.bootstrap.extend()


@pytest.mark.panel
def test_info_alert():
    """## test_info_alert

    - Blue Div with normal and bold text
    - Curently not full width
    """
    pn.config.raw_css.append(pnx.InfoAlert.raw_css)
    app = pn.Column(
        pnx.Markdown(test_info_alert.__doc__),
        pnx.InfoAlert("This is an **Info Alert**!"),
        sizing_mode="stretch_width",
    )

    app.servable(test_info_alert.__name__)


@pytest.mark.panel
def test_warning_alert():
    """## test_warning_alert

    - Yellow Div with normal and bold text
    - Curently not full width
    """
    pn.config.raw_css.append(pnx.WarningAlert.raw_css)
    app = pn.Column(
        pnx.Markdown(test_warning_alert.__doc__),
        pnx.WarningAlert("This is a **Warning Alert**!"),
        sizing_mode="stretch_width",
    )

    app.servable(test_warning_alert.__name__)


@pytest.mark.panel
def test_error_alert():
    """## test_error_alert

    - Red Div with normal and bold text
    - Curently not full width
    """
    pn.config.raw_css.append(pnx.ErrorAlert.raw_css)
    app = pn.Column(
        pnx.Markdown(test_error_alert.__doc__),
        pnx.ErrorAlert("This is an **Error Alert**!"),
        sizing_mode="stretch_width",
    )

    app.servable(test_error_alert.__name__)


@pytest.mark.panel
def test_info_alert_height_problem():
    """## test_info_alert_height_problem

    We saw that the height of InfoAlert Div was much greater than it needed to be.
    See [Issue 829](https://github.com/holoviz/panel/issues/829)
    """
    pn.config.raw_css.append(pnx.InfoAlert.raw_css)
    text = """\
Navigate to the **Dashboard Page** via the **Sidebar** to see the result.
Or Navigate to the **Limitations Page** to learn of some of the limitations of Panel that
I've experienced."""
    app = pn.Column(
        pnx.Markdown(test_info_alert_height_problem.__doc__),
        pnx.InfoAlert(text),
        sizing_mode="stretch_width",
    )

    app.servable(test_info_alert.__name__)


if __name__.startswith("bk"):
    test_info_alert()
    test_warning_alert()
    test_error_alert()
    test_info_alert_height_problem()
