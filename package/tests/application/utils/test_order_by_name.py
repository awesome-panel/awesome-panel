# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.utils import OrderByNameMixin


class Tag(OrderByNameMixin):  # pylint: disable=too-few-public-methods
    def __init__(self, name):
        self.name = name


def test_can_order():
    # Given
    tag_a = Tag(name="a")
    tag_b = Tag(name="b")
    tag_a2 = Tag(name="a")

    # Then
    assert tag_a < tag_b
    assert tag_a == tag_a2
