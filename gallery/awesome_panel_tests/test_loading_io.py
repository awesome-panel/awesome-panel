"""Test of the loading_io module of loading spinners"""
import panel as pn
import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp
import time

BLUE = "#4099da"


def test_circle_spinner():
    """## Circle spinner"""
    pnx.spinners.extend()
    return TestApp(test_circle_spinner, pnx.spinners.loading_io.Circle())


def test_blue_circle_spinner():
    """## Blue Circle spinner"""
    pnx.spinners.extend()
    return TestApp(test_blue_circle_spinner, pnx.spinners.loading_io.Circle(color=BLUE))


def test_default_spinner():
    """## Default Spinner"""
    pnx.spinners.extend()
    return TestApp(test_default_spinner, pnx.spinners.Default(color=BLUE),)


def test_all_spinners():
    """## All Spinners"""
    pnx.spinners.extend()
    return TestApp(
        test_all_spinners,
        pn.Row(pnx.spinners.Circle(color=BLUE), pnx.spinners.Facebook(color=BLUE)),
    )


def test_show_message_while_python_code_is_running():
    """## Show message while python code is running

    It works on Tornado Server 5.1.1 but not 6.0.3. See [Discourse]
    (https://discourse.holoviz.org/t/how-can-i-show-spinner-when-code-is-running/30/2)
    """
    button = pn.widgets.Button(name="Load page", button_type="primary")
    message = "Awesome Panel Loading..."
    page = pn.Column(button)

    def click_handler(event):
        page[:] = [message]
        time.sleep(2.5)
        page[:] = [button]

    button.on_click(click_handler)
    return TestApp(test_show_message_while_python_code_is_running, page)


def test_show_spinner_while_python_code_is_running():
    """## Show spinner while python code is running

    It works on Tornado Server 5.1.1 but not 6.0.3. See [Discourse]
    (https://discourse.holoviz.org/t/how-can-i-show-spinner-when-code-is-running/30/2)
    """
    button = pn.widgets.Button(name="Load page", button_type="primary")
    spinner = pnx.spinners.Facebook()
    page = pn.Column(button)

    def click_handler(event): # pylint: disable=unused-argument
        page[:] = [spinner]
        time.sleep(2.5)
        page[:] = [button]

    button.on_click(click_handler)

    return TestApp(test_show_spinner_while_python_code_is_running, page)

def test_show_jpg_spinner_while_python_code_is_running():
    """## Show spinner while python code is running

    It works on Tornado Server 5.1.1 but not 6.0.3. See [Discourse]
    (https://discourse.holoviz.org/t/how-can-i-show-spinner-when-code-is-running/30/2)
    """
    button = pn.widgets.Button(name="Load page", button_type="primary")
    spinner = pn.pane.Markdown("![Spinner](https://www.cattani.it/wp-content/uploads/2016/08/ajax-loading.gif)", width=10, height=10)
    page = pn.Column(button)

    def click_handler(event): # pylint: disable=unused-argument
        page[:] = [spinner]
        time.sleep(2.5)
        page[:] = [button]

    button.on_click(click_handler)

    return TestApp(test_show_spinner_while_python_code_is_running, page)



def view():
    "# Gallery View"
    return pn.Column(
        test_circle_spinner(),
        test_blue_circle_spinner(),
        test_default_spinner(),
        test_all_spinners(),
        test_show_message_while_python_code_is_running(),
        test_show_spinner_while_python_code_is_running(),
        test_show_jpg_spinner_while_python_code_is_running(),
    )


if __name__.startswith("bk"):
    view().servable("test_loading_io")
