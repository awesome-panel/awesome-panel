# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
def view():
    import pytest
    import panel as pn

    from awesome_panel.application.templates import MaterialTemplate
    from awesome_panel.application.templates import ApplicationTemplateBuilder
    from application.pages import home, about, issues, resources
    import param
    from awesome_panel.application.components import PageComponent as Page, LoadingPageComponent
    from awesome_panel.application.models import (
        MenuItem,
        SocialLink,
        SourceLink,
        Theme,
        Author,
    )
    # from application.pages import Gallery
    from awesome_panel.application.services import author_service
    from application import config
    from awesome_panel.application.services import PAGE_SERVICE, AUTHOR_SERVICE
    # from application.pages.custom_bokeh_model.custom import Custom
    # Custom()

    TITLE = "AWESOME PANEL"
    LOGO = "https://panel.holoviz.org/_static/logo_horizontal.png"
    URL = "https://awesome-panel.org"

    LOADING_PAGE = Page(
        name="Loading Page",
        author=AUTHOR_SERVICE.default_author,
        component=LoadingPageComponent,
    )

    PAGES = PAGE_SERVICE.pages
    MENU_ITEMS = [MenuItem(name="Item 1")]
    SOURCE_LINKS = [SourceLink(name="GitHub")]
    SOCIAL_LINKS = [SocialLink(name="Twitter")]

    pn.config.sizing_mode="stretch_width"

    return  ApplicationTemplateBuilder(
        title=TITLE,
        logo=LOGO,
        url=URL,
        pages=PAGES,
        template=MaterialTemplate,
        menu_items=MENU_ITEMS,
        source_links=SOURCE_LINKS,
        social_links=SOCIAL_LINKS,
    ).create()


if __name__.startswith("__main__"):
    view().show()
if __name__.startswith("bokeh"):
    view().servable()
