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
from awesome_panel.application.models import Application
from awesome_panel.application.services import Services
from awesome_panel.application.components import ApplicationComponent
from awesome_panel.application.views import ApplicationView
from awesome_panel.application.templates import MaterialTemplate




def view():

    # services.tag_service.bulk_create(config.tags.TAGS)
    # services.author_service.set_default_author(config.authors.MARC_SKOV_MADSEN)
    # services.author_service.bulk_create(config.pages.authors.AUTHORS)

    services = Services()
    services.page_service.set_default_page(config.pages.HOME)
    services.page_service.bulk_create(config.pages.PAGES)
    services.page_service.param.page.objects = config.pages.PAGES
    services.page_service.param.page.default = config.pages.HOME
    services.page_service.page = config.pages.HOME
    services.theme_service.param.theme.objects = config.themes.THEMES
    services.theme_service.param.theme.default = config.themes.MATERIAL_GREEN_PURPLE_LIGHT
    services.theme_service.theme = config.themes.MATERIAL_GREEN_PURPLE_LIGHT

    application = Application(
        title=config.application.TITLE,
        logo=config.application.LOGO,
        url=config.application.URL,
        pages=services.page_service.pages,
        default_template=config.templates.MATERIAL_TEMPLATE,
        templates=config.templates.TEMPLATES,
    )
    # application_view = ApplicationView()

    # application_component = ApplicationComponent(application=application, services=services, view=application_view)

    template = MaterialTemplate(
        application=application, services=services
    )
    return template

if __name__.startswith("bokeh"):
    view().servable()
else:
    view().show()
    # APP_ROUTES = {"": view}
    # pn.serve(APP_ROUTES, port=14033, dev=False, title="Awesome Panel")
