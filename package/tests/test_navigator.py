"""Tests of the awesome_panel functionality"""
import awesome_panel.express as pnx
import panel as pn


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
    app = pn.Column(test_pn_navigation.__doc__, sidebar, content)

    menu = pnx.NavigationMenu(pages=pages, page_outlet=content)
    sidebar.append(menu)
    app.servable("test_pn_navigation")


if __name__.startswith("bk"):
    test_pn_navigation()
