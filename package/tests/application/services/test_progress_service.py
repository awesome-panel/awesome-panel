"""In this module we test the ProgressService

The purpose of the ProgressService is to enable one shared service for progress_service reporting across
the application.

The ProgressService provides

- A combination of a progress value and a a progress message and a progress_service type
- Easy to use functionality for
    - Function Annotation
    - Context Management
"""

# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel.application.models import Progress
from awesome_panel.application.services._progress_service import ProgressService

def test_can_be_constructed_with_default_values(progress_service):
    assert isinstance(progress_service, ProgressService)
    assert isinstance(progress_service.progress, Progress)


def test_can_be_constructed_with_custom_values():
    # When
    progress = Progress(value=10, message="hello world", active_count=10)
    progress_service = ProgressService(progress=progress)
    # Then
    assert progress_service.progress == progress


def test_can_update(progress_service):
    # When
    progress_service.update(
        20, "hello again",
    )
    # Then
    assert progress_service.progress.value == 20
    assert progress_service.progress.message == "hello again"


def test_can_reset(progress_service):
    # Given
    progress_service = ProgressService(value=10, message="hello world")
    # When
    progress_service.reset()
    # Then
    assert progress_service.progress.value == 0
    assert progress_service.progress.message == ""


def test_can_use_report_func_as_context_manager(progress_service):
    # When:
    def run():
        with progress_service.report(50, "running"):
            pass

        # Then:

    run()
    assert progress_service.progress.value == 0
    assert progress_service.progress.message == ""


def test_can_use_report_func_as_decorator(progress_service):
    # When:
    @progress_service.report(33, "calculation")
    def run():
        pass

    # Then:
    run()
    assert progress_service.progress.value == 0
    assert progress_service.progress.message == ""


def test_can_use_increment_func_as_context_manager(progress_service):
    # When:
    def run():
        with progress_service.increment(50, "incrementing ..."):
            pass

        # Then:

    # When/ Then:
    run()
    assert progress_service.progress.value == 50
    assert progress_service.progress.message == "incrementing ..."

    run()
    assert progress_service.progress.value == 0
    assert progress_service.progress.message == ""


def test_can_use_increment_func_as_decorator(progress_service):
    # Given:
    @progress_service.increment(50, "incrementing ...")
    def run():
        pass

    # When/ Then:
    run()
    assert progress_service.progress.value == 50
    assert progress_service.progress.message == "incrementing ..."

    run()
    assert progress_service.progress.value == 0
    assert progress_service.progress.message == ""

def test_can_use_active_count(progress_service):
    @progress_service.is_active("Loading...")
    def load():
        assert progress_service.progress.active_count == 1
        assert progress_service.progress.message == "Loading..."
        @progress_service.is_active("Transforming...")
        def transform():
            assert progress_service.progress.active_count == 2
            assert progress_service.progress.message == "Transforming..."
        assert progress_service.progress.active_count == 1
        assert progress_service.progress.message == "Loading..."
        transform()
        assert progress_service.progress.active_count == 1
        assert progress_service.progress.message == "Loading..."

    load()
    assert progress_service.progress.active_count == 0
    assert progress_service.progress.message == ""
