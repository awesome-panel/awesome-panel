# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.application.components import ProgressSpinnerComponent


def test_can_construct(progress_spinner_component, progress_service, theme_service):
    # Then
    assert isinstance(progress_spinner_component, ProgressSpinnerComponent)
    assert progress_spinner_component.progress_service == progress_service
    assert progress_spinner_component.theme_service == theme_service
    assert hasattr(progress_spinner_component, "view")
    assert theme_service.theme.spinner_static_url in progress_spinner_component.view.object


def test_can_spin(progress_spinner_component, theme_service):
    # When
    progress_spinner_component.progress_service.update(active_count=1)
    assert theme_service.theme.spinner_url in progress_spinner_component.view.object

    # When
    progress_spinner_component.progress_service.reset()
    assert theme_service.theme.spinner_static_url in progress_spinner_component.view.object


def test_can_convert_spinner_url_to_img_html(progress_spinner_component):
    # Given
    url = "abc"
    # When/ Then
    assert progress_spinner_component._to_img_html(url) == (
        "<img src='abc' style='height:100%' title=''></img>"
    )
