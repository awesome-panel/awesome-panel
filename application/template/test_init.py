from application.template import _get_template_js, TEMPLATE_JS_ID, TEMPLATES
import pytest

@pytest.mark.parametrize(["templat"], [(template,) for template in TEMPLATES])
def test_get_template_js(templat):
    assert _get_template_js(templat).startswith(TEMPLATE_JS_ID)