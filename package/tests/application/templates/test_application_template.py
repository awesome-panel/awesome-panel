import panel as pn
import param

from awesome_panel.application.models import Theme


def test_can_construct_application_template_with_exception(application, application_template):
    # Then
    assert application_template.application is application
    assert isinstance(application_template.menu, pn.layout.Reactive)
    assert isinstance(application_template.sidebar, pn.layout.Reactive)
    assert isinstance(application_template.main, pn.layout.Reactive)

    assert application_template.main.objects
    assert isinstance(application_template.theme_css, pn.pane.HTML)
    assert isinstance(application_template.param.select_title_page, param.Action)

    assert isinstance(application_template.loading_page_component_main, pn.layout.Reactive)
    assert isinstance(application_template.spinner, pn.layout.Reactive)
    assert application_template.param.spinning.default is False

    assert isinstance(application.theme, Theme)


def test_main_content_changes_when_page_changes(
    application_template, home_page_component, gallery_page_component
):
    # Given
    assert application_template.application.page == home_page_component
    before = application_template.main.objects
    # When
    application_template.application.page = gallery_page_component
    after = application_template.main.objects
    # Then
    assert before != after


def test_can_start_spinning(application_template):
    # Given
    url = application_template.spinner.object
    # When
    application_template.spinning = True
    # Then
    assert application_template.spinner.object != url


def test_can_stop_spinning(application_template):
    # Given
    application_template.spinning = True
    url = application_template.spinner.object
    # When
    application_template.spinning = False
    # Then
    assert application_template.spinner.object != url
