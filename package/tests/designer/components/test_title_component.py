# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from awesome_panel.designer.components import TitleComponent


@pytest.fixture
def title_component():
    return TitleComponent()


def test_constructor(title_component):
    assert isinstance(title_component, TitleComponent)
    assert "logo_url" in title_component.param
    assert "logo_spinning_url" in title_component.param
    assert "spinning" in title_component.param
