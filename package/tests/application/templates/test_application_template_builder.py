# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
from panel.template import Template

from awesome_panel.application.templates import ApplicationTemplateBuilder


def test_can_create_template_from_models(
    title, logo, url, page_components, menu_items, source_links, social_links
):
    # When
    actual = ApplicationTemplateBuilder(
        title=title,
        logo=logo,
        url=url,
        pages=page_components,
        menu_items=menu_items,
        source_links=source_links,
        social_links=social_links,
    ).create()
    # Then
    assert isinstance(actual, Template)
