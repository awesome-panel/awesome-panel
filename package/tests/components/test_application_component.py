from awesome_panel.components import ApplicationComponent, Component
from awesome_panel.models import Application

def test_can_construct_application_component(application_component):
    assert isinstance(application_component, ApplicationComponent)
    assert isinstance(application_component.model, Application)