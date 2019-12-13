"""Test of the loading_io module of loading spinners"""
import time

import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp


def test_default_spinner():
    """## Show the default spinner"""
    default_spinner = pnx.spinners.DefaultSpinner()
    return TestApp(test_default_spinner, default_spinner)


def test_all_spinners():
    """## Show all spinners"""
    spinners_all = pn.Row(pnx.spinners.DefaultSpinner(), pnx.spinners.FacebookSpinner())
    return TestApp(test_all_spinners, spinners_all)


def test_spinner_while_python_executing():
    """## Show Facebook spinner while Python code is running

    It works on Tornado Server 5.1.1 but not 6.0.3. See
    [Discourse](https://discourse.holoviz.org/t/how-can-i-show-spinner-when-code-is-running/30/2)
    """
    button = pn.widgets.Button(name="Run Python Code", button_type="primary")
    spinner = pnx.spinners.FacebookSpinner()
    page = pn.Column(button)

    def click_handler(event):  # pylint: disable=unused-argument
        page[:] = [spinner]
        time.sleep(2.5)
        page[:] = [button]

    button.on_click(click_handler)

    return TestApp(test_spinner_while_python_executing, page)


def test_spinner_can_be_centered():
    """## Show spinner can be centered

    At the same time we can test if the spinner looks good on a dark background
    """
    spinner = pnx.spinners.FacebookSpinner()

    page = pn.Column(spinner.center(), width=400, height=400, background="gray",)
    return TestApp(test_spinner_can_be_centered, page)


def view() -> pn.Column:
    """View all tests"""
    return pn.Column(
        test_default_spinner(),
        test_all_spinners(),
        test_spinner_while_python_executing(),
        test_spinner_can_be_centered(),
    )


if __name__.startswith("bk"):
    view().servable()
