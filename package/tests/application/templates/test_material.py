# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
from awesome_panel.application.templates import MaterialTemplate


def test_can_construct_template(application, services):
    MaterialTemplate(application=application, services=services)
