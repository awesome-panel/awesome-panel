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
import panel as pn

from application import config
from awesome_panel.application.services import author_service, page_service, tag_service
from awesome_panel.application.templates import ApplicationTemplateBuilder
from awesome_panel.application.templates.material.material_template import MaterialTemplate


def view():

    tag_service.bulk_create(config.tags.TAGS)

    author_service.set_default_author(config.authors.MARC_SKOV_MADSEN)
    author_service.bulk_create(config.pages.authors.AUTHORS)

    page_service.set_default_page(config.pages.HOME)
    page_service.bulk_create(config.pages.PAGES)

    return ApplicationTemplateBuilder(
        title=config.application.TITLE,
        logo=config.application.LOGO,
        url=config.application.URL,
        pages=page_service.pages,
        template=MaterialTemplate,
        menu_items=config.menu_items.MENU_ITEMS,
        source_links=config.source_links.SOURCE_LINKS,
        social_links=config.social_links.SOCIAL_LINKS,
    ).create()


if __name__.startswith("bokeh"):
    view().servable()
else:
    APP_ROUTES = {"": view}
    pn.serve(APP_ROUTES, port=14033, dev=False, title="Awesome Panel")
