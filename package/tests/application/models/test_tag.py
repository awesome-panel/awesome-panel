# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
def test_can_construct_tag(tag):
    assert isinstance(tag.name, str)
    assert repr(tag) == tag.name
    assert str(tag) == tag.name
    assert hash(tag) == hash(tag.name)
