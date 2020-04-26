from awesome_panel.templates import MaterialTemplate

def test_can_construct_template(application_component):
    MaterialTemplate(application=application_component)