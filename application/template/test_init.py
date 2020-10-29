# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
import pytest

from application.template import TEMPLATE_JS_ID, TEMPLATES, _get_template_js


@pytest.mark.parametrize(["templat"], [(template,) for template in TEMPLATES])
def test_get_template_js(templat):
    assert _get_template_js(templat).startswith(TEMPLATE_JS_ID)
