# pylint: disable=line-too-long
"""This app is based on the *`FastGridTemplate`* and the *Fast Components* provided by the
<fast-anchor href="https://awesome-panel.readthedocs.io/en/latest/packages/awesome-panel-extensions/index.html#fast"
appearance="hypertext" target="_blank">awesome-panel-extensions</fast-anchor>
package.

You can install the package via `pip install awesome-panel-extensions` and use the fast template
and components via `from awesome_panel_extensions.frameworks import fast`.

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
from awesome_panel_extensions.assets import svg_icons
from awesome_panel_extensions.frameworks.fast import (
    FastButton,
    FastCheckbox,
    FastLiteralInput,
    FastSwitch,
    FastTextAreaInput,
    FastTextInput,
)
from awesome_panel_extensions.frameworks.fast.templates.fast_grid_template import FastGridTemplate
from holoviews import opts

from application.config import site
from application.pages.fast.echarts_app import EchartsApp

hv.extension("bokeh")
ellipse_opts = opts.Ellipse(line_width=3, color="#DF3874")

APPLICATION = site.create_application(
    url="fast-grid-template",
    name="Fast Grid Template",
    author="Marc Skov Madsen",
    introduction="Demonstrates the FastGridTemplate and Fast Components",
    description=__doc__,
    thumbnail_url="fast-grid-template.png",
    documentation_url="",
    code_url="fast/fast_grid_template.py",
    gif_url="",
    mp4_url="",
    tags=["Fast", "Template"],
)


def _config_fast_size_mode():
    FastButton.param.sizing_mode.default = pn.config.sizing_mode
    FastCheckbox.param.sizing_mode.default = pn.config.sizing_mode
    FastSwitch.param.sizing_mode.default = pn.config.sizing_mode
    FastTextAreaInput.param.sizing_mode.default = pn.config.sizing_mode
    FastLiteralInput.param.sizing_mode.default = pn.config.sizing_mode
    FastTextInput.param.sizing_mode.default = pn.config.sizing_mode


COLLAPSED_ICON = svg_icons.FAST_COLLAPSED_ICON
EXPANDED_ICON = svg_icons.FAST_EXPANDED_ICON

# pylint: disable=line-too-long
NAVIGATION_HTML = f"""
<fast-accordion>
<fast-accordion-item slot="item" expanded>
    <fast-menu>
        <fast-menu-item onClick='window.open("https://awesome-panel.org", "_blank")'>Home</fast-menu-item>
        <fast-menu-item onClick='window.open("https://awesome-panel.org/gallery", "_blank")'>Gallery</fast-menu-item>
        <fast-menu-item onClick='window.open("https://awesome-panel.org/resources", "_blank")'>Awesome List</fast-menu-item>
        <fast-menu-item onClick='window.open("https://awesome-panel.org/about", "_blank")'>About</fast-menu-item>
    </fast-menu>
    <div slot="heading">
        <h4>Main</h4>
    </div>{ COLLAPSED_ICON }{ EXPANDED_ICON }
</fast-accordion-item>
<fast-accordion-item slot="item" expanded>
    <div slot="heading">
        <h3>Share on Social</h3>
    </div>
    <fast-menu>
        <fast-menu-item onClick='window.open("https://github.com/marcskovmadsen/awesome-panel", target="_blank")'>Star on Github</fast-menu-item>
        <fast-menu-item onClick='window.open("https://twitter.com/intent/tweet?url=https%3A%2F%2Fawesome-panel.org&amp;text=Checkout", target="_blank")'>Share on Twitter</fast-menu-item>
        <fast-menu-item onClick='window.open("http://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fawesome-panel.org&amp;title=Checkout", target="_blank")'>Share on LinkedIn</fast-menu-item>
        <fast-menu-item onClick='window.open("https://reddit.com/submit?url=https%3A%2F%2Fawesome-panel.org&amp;title=Checkout", target="_blank")'>Share on Reddit</fast-menu-item>
        <fast-menu-item onClick='window.open("https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fawesome-panel.org", target="_blank")'>Share on Facebook</fast-menu-item>
        <fast-menu-item onClick='window.open("mailto:?subject=https%3A%2F%2Fawesome-panel.org&amp;body=Checkout&nbsp;https%3A%2F%2Fawesome-panel.org", target="_blank")'>Share by mail</fast-menu-item>
    </fast-menu>
    { COLLAPSED_ICON }{ EXPANDED_ICON }
</fast-accordion-item>
</fast-accordion>
"""
# pylint: enable=line-too-long

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



def _create_navigation_menu():
    return pn.pane.HTML(NAVIGATION_HTML)


def _create_sidebar_items():
    return [
        pn.pane.Markdown("## Settings"),
        FastButton(name="Click Me"),
        FastCheckbox(name="Check Me"),
        FastSwitch(value=True, checked_message="Checked", unchecked_message="Unchecked"),
        _create_navigation_menu(),
    ]


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
    parameters=[
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
        "readonly": FastCheckbox
    }
    return _create_card(component=component, parameters=parameters, widgets=widgets)

def _create_card(component, parameters, widgets):
    parameters = [*parameters, "disabled", "width", "height", "sizing_mode"]
    widgets["name"] = FastTextInput
    widgets["disabled"] = FastCheckbox
    for index, name in enumerate(parameters):
        component.param[name].precedence = index
    component.width=200
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
    _config_fast_size_mode()

    app = FastGridTemplate(
        title="FastGridTemplate by awesome-panel.org",
    )

    app.main[0:8, 0:6] = APPLICATION.intro_section()
    app.main[0:8, 6:12] = _create_hvplot()
    app.main[8:15, 0:12] = EchartsApp().view()
    app.main[15:29, 0:3] = _create_fast_button_card()
    app.main[15:29, 3:6] = _create_fast_checkbox_card()
    app.main[15:29, 6:9] = _create_fast_literal_input_card()
    app.main[15:29, 9:12] = _create_fast_switch_card()
    app.sidebar.extend(_create_sidebar_items())
    return app


if __name__.startswith("bokeh"):
    view().servable()
view()
