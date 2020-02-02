"""Here we test functionality to open a Panel in a modal window.

The Modal can be used to focus some kind of information like text, images, charts or (parts of)
an interactive dashboard.

The implementation is inspired by

- [Css Tricks](https://css-tricks.com/considerations-styling-modal/)
    - [Code Pen](https://codepen.io/henchmen/embed/preview/PzQpvk)
- [Bootstrap](https://getbootstrap.com/docs/4.3/components/modal/)
"""

import panel as pn

from awesome_panel.express import InfoAlert
from awesome_panel.express.bootstrap.modal import Modal
from awesome_panel.express.testing import TestApp

TEXT1 = """\

The Modal can be used to focus some kind of information like text, images, charts or (parts of)
an interactive dashboard.

Click 'X' to close the Modal dialogue
"""
MODAL = Modal(title="Modal", body=[TEXT1],)

STYLE = pn.pane.HTML(f"<style>{MODAL.get_css()}</style>")

BODY_OPTIONS = {
    "text1": TEXT1,
    "text2": "text2 " * 3,
}


def test_modal():
    """A test that a modal can be opened using a button"""
    open_button = MODAL.get_open_modal_button("Open")
    return TestApp(test_modal, open_button,)


def test_modal_settings():
    """A test that the modal settings can be changed interactively.

    Try changing

    - The Title to 'Awesome Panel!'
    - The Body to `text1` and `text2`. THIS DOES CURRENTLY NOT LAYOUT NICELY.
    - The Modal width to 800
    """
    open_button = MODAL.get_open_modal_button("Open")

    options = list(BODY_OPTIONS)
    body_selector = pn.widgets.CheckBoxGroup(
        name="Select body of modal", value=options[0:1], options=options,
    )

    @pn.depends(
        body_selector, watch=True,
    )
    def set_modal_body(_,):  # pylint: disable=unused-variable
        if body_selector.value:
            # pylint: disable=not-an-iterable
            MODAL.body = [BODY_OPTIONS[option] for option in body_selector.value]
            # pylint: enable=not-an-iterable

    return TestApp(
        test_modal_settings,
        MODAL.param.title,
        pn.pane.Markdown("Body"),
        body_selector,
        MODAL.modal.param.width,
        open_button,
    )


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        STYLE,
        pn.pane.Markdown(__doc__),
        pn.pane.Markdown(
            "THIS IS CURRENTLY AN EXPERIMENT ONLY. USE THIS FOR INSPIRATION ONLY.",
            background="#d1ecf1",
        ),
        Divider(),
        test_modal(),
        Divider(),
        test_modal_settings(),
        MODAL.modal,
        MODAL.modal_overlay,
    )


if __name__.startswith("bk"):
    view().servable()
