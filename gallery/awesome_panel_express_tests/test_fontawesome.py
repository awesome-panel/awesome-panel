"""Here we test the functionality of font awesome"""
# pylint: disable=protected-access
import pathlib

import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp

pnx.fontawesome.extend()


def test_html_with_font_awesome():
    """## Test that we can use HTML with font awesome icons"""
    text = """
    <ul style="margin: 0;">
        <li><i class="fas fa-user"></i> Login</li>
        <li><i class="fas fa-newspaper"></i> TPS Reports</li>
        <li><i class="fab fa-twitter"></i> Twitter</li>
    </ul>


    """
    html = pn.pane.HTML(text, sizing_mode="stretch_width")
    return TestApp(test_html_with_font_awesome, html)


def test_button_with_font_awesome():
    """## Test that we can use buttons with a font awesome icon"""
    button_user = pn.widgets.Button(name=" User", css_classes=["pas", "pa-user"],)
    button_newspaper = pn.widgets.Button(name=" News Paper", css_classes=["pas", "pa-newspaper"],)
    button_twitter = pn.widgets.Button(name=" Twitter", css_classes=["pab", "pa-twitter"],)

    return TestApp(test_button_with_font_awesome, button_user, button_newspaper, button_twitter,)


def view() -> pn.Column:
    """This function collect the tests into a Column"""
    return pn.Column(test_html_with_font_awesome(), test_button_with_font_awesome(),)


if __name__.startswith("bk"):
    view().servable("test fontawesome")
