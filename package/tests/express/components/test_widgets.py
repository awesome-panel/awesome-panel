"""We test that new widgets like wired or material has the same parameters as the
corresponding panel original widgets in order for them to be useable via pn.Param"""
import panel as pn
import pytest

from awesome_panel.express.components import wired

# @Philippfr: Any of these parameters that are really needed in order to be able to use
# wired widget in Panel in general and with pn.Param in particular?
PARAMETERS_NOT_TO_TEST = {
    wired.FloatSlider: {
        "orientation",
        "bar_color",
        "callback_throttle",
        "tooltips",
        "value_throttled",
        "callback_policy",
        "direction",
        "show_value",
    },
    wired.Button: {"button_type"},
    wired.IconButton: {"button_type"},
    wired.Image: {"link_url", "default_layout", "embed", "style"},
    wired.IntSlider: {
        "orientation",
        "bar_color",
        "callback_throttle",
        "tooltips",
        "value_throttled",
        "callback_policy",
        "direction",
        "show_value",
    },
    wired.Progress: {"bar_color", "active"},
    wired.ProgressSpinner: {"max", "bar_color", "value"},
    wired.Toggle: {"button_type"},
    wired.Video: {
        "paused",
        "throttle",
        "time",
        "default_layout",
        "volume",
    },  # Todo: Feature Request to Wired for these Properties
}

ORIGINAL_NEW_LIST = [
    (pn.widgets.Button, wired.Button),
    (pn.widgets.Checkbox, wired.Checkbox),
    (pn.widgets.DatePicker, wired.DatePicker),
    (pn.layout.Divider, wired.Divider),
    (pn.widgets.FloatSlider, wired.FloatSlider),
    (pn.widgets.Button, wired.IconButton),
    (pn.pane.image.ImageBase, wired.Image),
    (pn.widgets.IntSlider, wired.IntSlider),
    (pn.widgets.LiteralInput, wired.LiteralInput),
    (pn.widgets.Progress, wired.Progress),
    (pn.widgets.Progress, wired.ProgressSpinner),
    (pn.widgets.Checkbox, wired.RadioButton),
    (pn.widgets.TextInput, wired.SearchInput),
    (pn.widgets.Select, wired.Select),
    (pn.widgets.TextInput, wired.TextInput),
    (pn.widgets.TextAreaInput, wired.TextAreaInput),
    (pn.widgets.Toggle, wired.Toggle),
    (pn.pane.Video, wired.Video),
]


def get_parameters_to_test(original, new):
    print(original, new)
    parameters = set(original.param.objects()) - set(pn.widgets.Widget.param.objects())
    if new in PARAMETERS_NOT_TO_TEST:
        parameters = parameters - PARAMETERS_NOT_TO_TEST[new]
    return parameters


def get_original_new_parameter_list():
    result = []
    for original, new in ORIGINAL_NEW_LIST:
        for parameter in get_parameters_to_test(original, new):
            result.append((original, new, parameter))
    return result


@pytest.mark.parametrize(["original", "new", "parameter"], get_original_new_parameter_list())
def test_original_and_new_widget_have_save_parameters(original, new, parameter):
    """The purpose of this test is to test that new (new) widgets can be used as drop in
    replacements for the original (original) Panel widgets"""
    assert hasattr(new, parameter), parameter
    assert isinstance(new.param[parameter], type(original.param[parameter]))
    assert original.param[parameter].default == new.param[parameter].default
