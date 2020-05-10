from awesome_panel.designer.models import ComponentConfiguration

def test_constructor():
    # When
    component_configuration = ComponentConfiguration()
    # Then
    assert component_configuration.parameters is None

def test_fixture_constructor(component_configuration):
    assert isinstance(component_configuration, ComponentConfiguration)