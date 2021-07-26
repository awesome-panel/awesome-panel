# pylint: disable=line-too-long
"""This app is based on the [`FastGridTemplate`]\
(https://panel.holoviz.org/reference/templates/FastGridTemplate.html#templates-gallery-fastgridtemplate) and the *Fast Components* provided by the
<fast-anchor href="https://awesome-panel.readthedocs.io/en/latest/packages/awesome-panel-extensions/index.html#fast" appearance="hypertext" target="_blank">awesome-panel-extensions</fast-anchor>
package.

You can install the package via `pip install awesome-panel-extensions` and use the fast components
via `from awesome_panel_extensions.frameworks import fast`.

We are also using some Panel Components with Fast like CSS styling.

## <a href="https://fast.design" target="_blank"><img src="https://explore.fast.design/e1e15bd85334e4346744078af2f52308.svg" style="vertical-align: middle; height: 32px;"></a>

Fast is the adaptive interface system for modern web experiences.

Interfaces built with FAST adapt to your design system and can be used with any modern UI Framework by leveraging industry standard Web Components.

Checkout the <fast-anchor href="https://explore.fast.design/components/fast-accordion" appearance="hypertext" target="_blank">Component Gallery</fast-anchor>.
"""
# pylint: enable=line-too-long
import holoviews as hv
import numpy as np
import panel as pn
from awesome_panel_extensions.frameworks.fast import (
    FastButton,
    FastCheckbox,
    FastLiteralInput,
    FastSwitch,
    FastTextInput,
)
from awesome_panel_extensions.site import site
from holoviews import opts
from panel.template import FastGridTemplate

from application.pages.fast.echarts_app import EchartsApp

hv.extension("bokeh")
ellipse_opts = opts.Ellipse(line_width=3, color="#DF3874")

APPLICATION = site.create_application(
    url="fast-grid-template",
    name="Fast Grid Template",
    author="Marc Skov Madsen",
    description="Demonstrates the FastGridTemplate and Fast Components",
    description_long=__doc__,
    thumbnail="fast-grid-template.png",
    resources={
        "code": "fast/fast_grid_template_app.py",
        "mp4": "fast_grid_template_app.mp4",
    },
    tags=["Fast", "Template"],
)


def _create_hvplot():
    # Generate some data
    cl1 = np.random.normal(loc=2, scale=0.2, size=(200, 200))
    cl2x = np.random.normal(loc=-2, scale=0.6, size=200)
    cl2y = np.random.normal(loc=-2, scale=0.1, size=200)
    cl3 = np.random.normal(loc=0, scale=1.5, size=(400, 400))
    # Create an overlay of points and ellipses
    clusters = (
        hv.Points(cl1).opts(color="blue")
        * hv.Points((cl2x, cl2y)).opts(color="green")
        * hv.Points(cl3).opts(color="#FDDC22")
    )
    plot = (
        clusters
        * hv.Ellipse(2, 2, 2).opts(ellipse_opts)
        * hv.Ellipse(-2, -2, (4, 2)).opts(ellipse_opts)
    )
    return pn.Column(
        pn.pane.Markdown("## HoloViews Plot"),
        pn.pane.HoloViews(plot, sizing_mode="stretch_both"),
        sizing_mode="stretch_both",
    )


def _create_fast_button_card():
    component = FastButton(name="Click me", appearance="accent")
    parameters = [
        "clicks",
        "name",
        "appearance",
        "button_type",
    ]
    widgets = {
        "clicks": {"disabled": True},
    }
    return _create_card(component=component, parameters=parameters, widgets=widgets)


def _create_fast_checkbox_card():
    component = FastCheckbox(name="Check me", value=False)
    parameters = [
        "value",
        "name",
        "readonly",
    ]
    widgets = {
        "value": FastCheckbox,
        "readonly": FastCheckbox,
    }
    return _create_card(component=component, parameters=parameters, widgets=widgets)


def _create_fast_literal_input_card():
    component = FastLiteralInput(
        name="Literal Input",
        type=(type, dict),
        value={"a": 1, "b": "Hello Fast"},
        placeholder="Enter a dict",
    )
    parameters = [
        "value",
        "name",
        # "type",
        "placeholder",
        "appearance",
        "serializer",
        "readonly",
    ]
    widgets = {
        "value": FastLiteralInput,
        "type": {"type": FastLiteralInput, "disabled": True},
        "placeholder": FastTextInput,
        "readonly": FastCheckbox,
    }
    return _create_card(component=component, parameters=parameters, widgets=widgets)


def _create_fast_switch_card():
    component = FastSwitch(
        name="Notify by Email",
        value=False,
        checked_message="On",
        unchecked_message="Off",
    )
    parameters = [
        "value",
        "name",
        "checked_message",
        "unchecked_message",
        "readonly",
    ]
    widgets = {
        "value": FastCheckbox,
        "checked_message": FastTextInput,
        "unchecked_message": FastTextInput,
        "readonly": FastCheckbox,
    }
    return _create_card(component=component, parameters=parameters, widgets=widgets)


def _create_card(component, parameters, widgets):
    component.sizing_mode="stretch_width"
    parameters = [*parameters, "disabled", "width", "height", "sizing_mode"]
    widgets["name"] = FastTextInput
    widgets["disabled"] = FastCheckbox
    for index, name in enumerate(parameters):
        component.param[name].precedence = index
    component.width = 200
    settings = pn.Param(
        component,
        parameters=parameters,
        widgets=widgets,
        show_name=False,
        sizing_mode="stretch_width",
    )
    return pn.Column(
        pn.pane.HTML(f"<h2>{component.__class__.name}</h2>"),
        pn.Row(component, height=60),
        pn.pane.HTML("<h3>Parameters</h3>"),
        settings,
        sizing_mode="stretch_both",
    )


@site.add(APPLICATION)
def view():
    """Returns the FastGridTemplate App"""
    pn.config.sizing_mode = "stretch_width"

    app = FastGridTemplate(
        title="FastGridTemplate by awesome-panel.org",
        row_height=55,
        prevent_collision=True,
        save_layout=True,
    )

    app.main[0:9, 0:6] = APPLICATION.intro_section()
    app.main[0:9, 6:12] = _create_hvplot()
    app.main[9:16, 0:12] = EchartsApp().view()
    app.main[16:30, 0:3] = _create_fast_button_card()
    app.main[16:30, 3:6] = _create_fast_checkbox_card()
    app.main[16:30, 6:9] = _create_fast_literal_input_card()
    app.main[16:30, 9:12] = _create_fast_switch_card()
    return app


if __name__.startswith("bokeh"):
    view().servable()
