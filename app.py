# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
"""In this module we configure our awesome-panel.org app and serve it using the
awesome_panel.application framework.

The awesome_panel.application framework provides

- Templates: One or more Templates to layout your app(s). A template might provide `main`,
`sidebar`, `topbar` layouts where you can put your content.
- Components: Smaller constitutents used to create the Template or PageComponents
- Views: Layout+Styling of Components
- Services: Services that can be used by the Template and components. For example a progress_service
- Models: Like Application, Page, Author, Tag, Progress etc.
"""
import os
import platform

import panel as pn

import application.pages.dialog_template as dialog_template
from application import config
from application.pages.fast_gallery.fast_gallery import get_fast_gallery  # type: ignore

# links = ""
# for page in config.pages.NON_GALLERY_PAGES+config.pages.GALLERY_PAGES:
#     links += f"""\n<a href="{page.url}">{page.name}</a>"""
# print(links)
# breakpoint()

if __name__ == "__main__":
    address = os.getenv("BOKEH_ADDRESS", "0.0.0.0")
    APP_ROUTES = {
        **config.pages.URLS,
        "gallery": get_fast_gallery,
        "dialog-template": dialog_template.view,
    }
    if platform.system() == "Windows":
        pn.serve(APP_ROUTES, port=80, dev=False, title="Awesome Panel", address=address)
    else:
        pn.serve(
            APP_ROUTES, port=80, dev=False, title="Awesome Panel", address=address, num_procs=4
        )
