# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from application.pages.detr.detr import DETRApp


def test_constructor(detr_app):
    assert isinstance(detr_app, DETRApp)


def test_can_update_url(detr_app):
    # Given
    old_url = detr_app.input_image_url
    event = {}
    # When
    detr_app.set_random_image(event)
    new_url = detr_app.input_image_url
    # Then
    assert new_url != old_url


def test_can_run_detr(detr_app):
    # Given
    event = {}
    detr_app.plot.object = None
    # When
    detr_app.run_detr(event)
    # Then
    assert detr_app.plot.object
