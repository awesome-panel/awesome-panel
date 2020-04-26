# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
import pytest
from awesome_panel.templates import ApplicationTemplateBuilder
from panel.template import Template


def test_can_create_template_from_models(title, logo, url, pages, menu_items, source_links, social_links):
    # When
    actual = ApplicationTemplateBuilder(
        title=title,
        logo=logo,
        url=url,
        pages=pages,
        menu_items=menu_items,
        source_links=source_links,
        social_links=social_links,
    ).create()
    # Then
    assert isinstance(actual, Template)