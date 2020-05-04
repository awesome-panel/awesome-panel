# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.application.models import Progress, Theme
from awesome_panel.application.components import ProgressSpinnerComponent

def test_can_construct(progress_service):
    # When
    progress_spinner_component = ProgressSpinnerComponent()
    # Then
    assert progress_spinner_component.progress_service == progress_service
    assert isinstance(progress_spinner_component.theme, Theme)

def test_fixtures_setup_as_expected(progress_spinner_component, progress_service, theme):
    assert progress_spinner_component.progress_service == progress_service
    assert progress_spinner_component.theme == theme
    assert theme.spinner_static_url in progress_spinner_component.object

def test_can_spin(progress_spinner_component):
    # When
    progress_spinner_component.progress_service.update(active_count=1)
    assert progress_spinner_component.theme.spinner_url in progress_spinner_component.object

    # When
    progress_spinner_component.progress_service.reset()
    assert progress_spinner_component.theme.spinner_static_url in progress_spinner_component.object

def test_can_convert_spinner_url_to_img_html(progress_spinner_component):
    # Given
    url = "abc"
    # When/ Then
    assert progress_spinner_component._to_img_html(url) == (
        "<img src='abc' style='height:100%' title=''></img>"
    )