"""In this module we test the MaterialTemplateBuilder"""
import pytest
from src.pages.gallery.material_template import material_template_builder as mtb

def test_get_component_script():
    # Given
    component = "mwc-button"
    version = "0.11"
    # When
    actual = mtb.test_get_component_script(component, version)
    # Then
    assert actual == <script type="module" src="https://unpkg.com/@material/mwc-button@0.14.1/mwc-button.js?module"></script>

