"""Tests of the awesome_panel functionality"""
import awesome_panel.express as pnx
import panel as pn


def test_pn_navigation():
    """# Manual Test of the Navigation Component

    - Can select each the two pages
    """
    page1 = pn.Row("# Page 1", name="Page 1")
    page2 = pn.Row("# Page 2", name="Page 2")

    pages = [page1, page2]
    navigator = pnx.Navigator(pages=pages)
    app = pn.Column(test_pn_navigation.__doc__, navigator.menu, navigator.selected_page)
    app.servable("test_pn_navigation")


if __name__.startswith("bk"):
    test_pn_navigation()
