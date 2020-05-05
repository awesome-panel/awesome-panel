# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import panel as pn
import param


def test_can_construct_application_template_with_exception(application, application_template):
    # Then
    assert application_template.application is application
    assert isinstance(application_template.menu, pn.layout.Reactive)
    assert isinstance(application_template.sidebar, pn.layout.Reactive)
    assert isinstance(application_template.main, pn.layout.Reactive)

    assert application_template.main.objects
    assert isinstance(application_template.param.select_title_page, param.Action)

    assert isinstance(application_template.spinner, pn.layout.Reactive)


def test_main_content_changes_when_page_changes(application_template, home_page, gallery_page):
    # Given
    assert application_template.application.page == home_page
    before = application_template.main.objects
    # When
    application_template.application.page = gallery_page
    after = application_template.main.objects
    # Then
    assert before != after
