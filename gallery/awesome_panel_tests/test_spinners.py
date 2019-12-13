"""Test of the loading_io module of loading spinners"""
import time

import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp


def test_default_spinner():
    """## Show default spinner while python code is running

    It works on Tornado Server 5.1.1 but not 6.0.3. See [Discourse]
    (https://discourse.holoviz.org/t/how-can-i-show-spinner-when-code-is-running/30/2)
    """
    button = pn.widgets.Button(name="Load page", button_type="primary")
    spinner = pnx.spinners.Default()
    page = pn.Column(button)

    def click_handler(event):  # pylint: disable=unused-argument
        page[:] = [spinner]
        time.sleep(2.5)
        page[:] = [button]

    button.on_click(click_handler)

    return TestApp(test_default_spinner, page)


def test_facebook_spinner():
    """## Show Facebook spinner while python code is running

    It works on Tornado Server 5.1.1 but not 6.0.3. See [Discourse]
    (https://discourse.holoviz.org/t/how-can-i-show-spinner-when-code-is-running/30/2)
    """
    button = pn.widgets.Button(name="Load page", button_type="primary")
    spinner = pnx.spinners.Facebook()
    page = pn.Column(button)

    def click_handler(event):  # pylint: disable=unused-argument
        page[:] = [spinner]
        time.sleep(2.5)
        page[:] = [button]

    button.on_click(click_handler)

    return TestApp(test_default_spinner, page)


if __name__.startswith("bk"):
    test_default_spinner().servable()
    test_facebook_spinner().servable()
