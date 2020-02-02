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
    page = pnx.Header("Button Page", name="Button",)
    page_font_awesome = pnx.Header("Font Awesome Page", name=" Font Awesome",)
    page_outlet = pn.Column(page)
    button = pnx.NavigationButton(page=page, page_outlet=page_outlet,)
    button_font_awesome = pnx.NavigationButton(
        page=page_font_awesome, page_outlet=page_outlet, css_classes=["pab", "pa-twitter",],
    )
    app = pn.Column(
        pn.pane.Markdown(test_pn_navigation_button.__doc__),
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
    page1 = pn.pane.Markdown("## Page 1", name="Page 1",)
    page2 = pn.pane.Markdown("## Page 2", name="Page 2",)

    pages = [
        page1,
        page2,
    ]
    content = pn.Column()
    sidebar = pn.Column()
    app = pn.Column(pn.pane.Markdown(test_pn_navigation.__doc__), sidebar, content,)

    menu = pnx.NavigationMenu(pages=pages, page_outlet=content,)
    sidebar.append(menu)
    app.servable("test_pn_navigation")


@pytest.mark.panel
def test_pn_navigation_with_font_awesome():
    """# Manual Test of the Navigation Component with Font Awesome

    - The first button has no icon as we specified None
    - The second button has no icon as we specified an empty list
    - The third button has a twitter icon as specified
    """
    pnx.fontawesome.extend()
    page1 = pn.pane.Markdown("## None", name="Page None",)
    page2 = pn.pane.Markdown("## Empty", name="Page Empty",)
    page3 = pn.pane.Markdown("## Twitter", name=" Page Twitter",)

    pages = [
        page1,
        page2,
        page3,
    ]
    content = pn.Column()
    sidebar = pn.Column()
    app = pn.Column(
        pn.pane.Markdown(test_pn_navigation_with_font_awesome.__doc__), sidebar, content,
    )

    css_classes = [
        None,
        [],
        ["pab", "pa-twitter",],
    ]

    menu = pnx.NavigationMenu(pages=pages, page_outlet=content, css_classes=css_classes,)
    sidebar.append(menu)
    app.servable("test_pn_navigation_with_font_awesome")


if __name__.startswith("bk"):
    test_pn_navigation_button()
    test_pn_navigation()
    test_pn_navigation_with_font_awesome()
