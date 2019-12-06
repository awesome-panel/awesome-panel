"""Tests of the awesome_panel functionality"""
import panel as pn
import pytest

import awesome_panel.express as pnx


@pytest.mark.panel
def test_pn_navigation_button():
    """# Manual Test of the Navigation Buttons

    - Ordinary Button
    - Button With Font Awesome
    """
    # Given:
    pnx.fontawesome.extend()
    page = pnx.Header("Button Page", name="Button")
    page_font_awesome = pnx.Header("Font Awesome Page", name=" Font Awesome")
    page_outlet = pn.Column(page)
    button = pnx.NavigationButton(page=page, page_outlet=page_outlet)
    button_font_awesome = pnx.NavigationButton(
        page=page_font_awesome, page_outlet=page_outlet, css_classes=["pab", "pa-twitter"]
    )
    app = pn.Column(
        pnx.Markdown(test_pn_navigation_button.__doc__),
        button,
        button_font_awesome,
        page_outlet,
        width=400,
    )
    # When
    app.servable("test_pn_navigation")


@pytest.mark.panel
def test_pn_navigation():
    """# Manual Test of the Navigation Component

    - Page 1 is shown by default.
    - Can navigate to Page 1 and Page 2
    """
    page1 = pn.Row("# Page 1", name="Page 1")
    page2 = pn.Row("# Page 2", name="Page 2")

    pages = [page1, page2]
    content = pn.Column()
    sidebar = pn.Column()
    app = pn.Column(pnx.Markdown(test_pn_navigation.__doc__), sidebar, content)

    menu = pnx.NavigationMenu(pages=pages, page_outlet=content)
    sidebar.append(menu)
    app.servable("test_pn_navigation")


if __name__.startswith("bk"):
    test_pn_navigation_button()
    test_pn_navigation()
