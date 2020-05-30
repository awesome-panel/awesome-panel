# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from application.pages.detr.detr import DETRApp


@pytest.fixture
def detr_app():
    return DETRApp()
