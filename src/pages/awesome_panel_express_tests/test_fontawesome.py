"""Here we test the functionality of `awesome_panel.express.fontawesome`

Please note you need to run `fontawesome.extend()` in order to import the relevant css.
"""
# pylint: disable=protected-access
import panel as pn

import awesome_panel.express as pnx
from awesome_panel.express.testing import TestApp

pnx.fontawesome.extend()


def test_html_with_font_awesome():
    """Test that we can use HTML with font awesome icons"""
    text = """
    <ul style="margin: 0;">
        <li><i class="fas fa-user"></i> Login</li>
        <li><i class="fas fa-newspaper"></i> TPS Reports</li>
        <li><i class="fab fa-twitter"></i> Twitter</li>
    </ul>


    """
    html = pn.pane.HTML(text, sizing_mode="stretch_width",)
    return TestApp(test_html_with_font_awesome, html,)


def test_button_with_font_awesome():
    """Test that we can use buttons with a font awesome icon

    Please note that the 'f' in FontAwesome css classes needs to be changed to 'p' for Panel.
    For example to `css_classes=["pas", "pa-user"]`
    """
    button_user = pn.widgets.Button(name=" User", css_classes=["pas", "pa-user",],)
    button_newspaper = pn.widgets.Button(name=" News Paper", css_classes=["pas", "pa-newspaper",],)
    button_twitter = pn.widgets.Button(name=" Twitter", css_classes=["pab", "pa-twitter",],)

    return TestApp(test_button_with_font_awesome, button_user, button_newspaper, button_twitter,)


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        pn.pane.Markdown(__doc__), test_html_with_font_awesome(), test_button_with_font_awesome(),
    )


if __name__.startswith("bokeh"):
    view().servable("test fontawesome")
