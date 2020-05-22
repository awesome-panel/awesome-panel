# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.application.models import Progress


def test_can_construct(progress):
    assert progress.value == 0
    assert progress.value_max == 100
    assert progress.message == ""
    assert progress.active_count == 0
    assert progress.active is False


def test_active_works():
    # Given
    progress = Progress(value=0, message="Loading...", active_count=1)
    # When/ Then
    assert progress.active is True
