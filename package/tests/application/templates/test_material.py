from awesome_panel.application.templates import MaterialTemplate


def test_can_construct_template(application):
    MaterialTemplate(application=application)
