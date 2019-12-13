import panel as pn
import time


def test_show_message_while_python_code_is_running():
    """## Message IS NOT shown while code is running"""
    button = pn.widgets.Button(name="Load page", button_type="primary")
    message = "Awesome Panel Loading..."
    page = pn.Column(button)

    def click_handler(event):
        page[:] = [message]
        # Run python Code
        time.sleep(5)
        # Update page
        page[:] = ["Success"]

    button.on_click(click_handler)
    return pn.Column(
        pn.pane.Markdown(test_show_message_while_python_code_is_running.__doc__), page,
    )


test_show_message_while_python_code_is_running().servable("Test Loading...")
