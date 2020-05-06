from awesome_panel.application.components import ApplicationComponent

def test_can_construct(application_component, application, application_view, services):
    assert isinstance(application_component, ApplicationComponent)
    assert application_component.application == application
    assert application_component.view == application_view
    assert application_component.services == services

