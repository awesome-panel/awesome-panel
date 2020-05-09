from awesome_panel.designer.components import TitleComponent
import pytest

@pytest.fixture
def title_component():
    return TitleComponent()

def test_constructor(title_component):
    assert isinstance(title_component, TitleComponent)
    assert "title_html" in title_component.param
    assert "logo_url" in title_component.param
    assert "logo_spinning_url" in title_component.param
    assert "spinning" in title_component.param