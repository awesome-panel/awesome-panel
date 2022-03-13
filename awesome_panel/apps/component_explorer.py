"""The Panel Component Explorer App helps you discover and learn about the Panel Components

I hope this can speed up the process of learning the power of Panel.

The Component Explorer currently supports the components that I have styled in the
[Fast.design](https://fast.design) style. I am in the process of adding the rest.
"""
from awesome_panel_extensions.developer_tools.test_apps import PanelComponentExplorer

from awesome_panel import config

app = config.extension(url="component_explorer", template=None, intro_section=False)

SIDEBAR_FOOTER = config.menu_fast_html(app_html=config.app_menu_fast_html, accent=config.ACCENT)

explorer = PanelComponentExplorer()
explorer.view.main.insert(0, app.intro_section())
explorer.view.sidebar_footer = SIDEBAR_FOOTER

explorer.view.servable()
