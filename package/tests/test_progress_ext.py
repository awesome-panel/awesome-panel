"""In this module we test the ProgressExt widget

The purpose of the ProgressExt widget is to enable easier progress reporting using the existing
[`pn.widgets.Progress`](https://panel.pyviz.org/reference/widgets/Progress.html#gallery-progress)
widget.

The ProgressExt widget provides

- A combination of a progress value and a progress message
- Easy to use functionality for
    - Function Annotation
    - Context Management
"""

from awesome_panel.express import ProgressExt


def test_constructor():
    """We test the ProgressExt constructor"""
    # When
    progress = ProgressExt(value=10, message="hello world", bar_color="primary")
    # Then
    assert progress.value == 10
    assert progress.message == "hello world"
    assert progress.bar_color == "primary"


def test_update():
    """We test the ProgressExt update method"""
    # Given
    progress = ProgressExt()
    # When
    progress.update(20, "hello again")
    # Then
    assert progress.value == 20
    assert progress.message == "hello again"


def test_reset():
    """We test the ProgressExt reset method"""
    # Given
    progress = ProgressExt(value=10, message="hello world", bar_color="primary")
    # When
    progress.reset()
    # Then
    assert progress.value == 0
    assert progress.message == ""
    assert progress.bar_color == "primary"
