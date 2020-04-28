## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.models import Tag

def test_can_construct_tag(tag):
    assert isinstance(tag.name, str)
    assert repr(tag) == tag.name
    assert str(tag) == tag.name
    assert hash(tag) == hash(tag.name)