"""Google has developed the `model-viewer` web component for interactively viewing very large and
detailed 3D models.

In this example we will demonstrate how to use the it in a Panel application. It's available via the
[`awesome-panel-extensions`](https://pypi.org/project/awesome-panel-extensions/) package.

The ModelViewer component and example could potentially be extended a lot by giving access to all
the parameters of the `model-viewer`.

If you would like a `model-viewer` example notebook to be an integral part of the Panel gallery go
to GitHub and upvote [PR 1281](https://github.com/holoviz/panel/pull/1281).

You can find more information at
[modelviewer.dev](https://modelviewer.dev/),
[examples](https://modelviewer.dev/examples/tester.html),
[codelabs](https://codelabs.developers.google.com/codelabs/model-viewer/index.html?index=..%2F..index#0),
and [model-viewer Github](https://github.com/google/model-viewer/tree/master/packages/model-viewer)"""

import panel as pn
from awesome_panel_extensions.pane import ModelViewer

from awesome_panel_extensions.site import site

MODELVIEWER_LOGO = '<img src="https://avatars1.githubusercontent.com/u/1342004?v=4&amp;s=40" style="height:50px"></img>'
PANEL_LOGO = (
    '<img src="https://panel.holoviz.org/_static/logo_stacked.png" style="height:50px"></img>'
)
BLUE = "#5dbcd2"
GRAY = "#eeeeee"
APPLICATION = site.create_application(
    url="model-viewer",
    name="Model Viewer",
    author="Marc Skov Madsen",
    description="""Demonstrates the look and feel of the Google ModelViewer in your Panel app""",
    description_long=__doc__,
    thumbnail="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/assets/images/thumbnails/test_model_viewer.png",
    resources = {
        "code": "https://github.com/MarcSkovMadsen/awesome-panel/tree/master/application/pages/awesome_panel_express_tests/test_model_viewer.py",
    },
    tags=["model-viewer"],
)


def create_app(**params):
    pn.config.sizing_mode = "stretch_width"
    template = pn.template.FastListTemplate(title="Test Model Viewer")
    if "dark" in str(template.theme).lower():
        background = template.theme.style.neutral_fill_card_rest
    else:
        background = GRAY

    top_app_bar = pn.Column(
        pn.layout.Row(
            pn.pane.HTML(MODELVIEWER_LOGO, width=50, sizing_mode="fixed"),
            pn.pane.Markdown(
                "## model-viewer", width=250, sizing_mode="fixed", margin=(10, 5, 10, 5)
            ),
            sizing_mode="stretch_width",
        ),
        pn.layout.HSpacer(height=2),
        height=60,
        sizing_mode="stretch_width",
        background=background,
    )

    model_viewer = ModelViewer(height=500, width=650)

    settings_bar = pn.Param(
        model_viewer,
        parameters=["src", "height", "width", "exposure", "auto_rotate", "camera_controls"],
        width=200,
        sizing_mode="stretch_height",
        background=background,
    )

    template.main[:] = [
        APPLICATION.intro_section(),
        pn.Column(
            pn.pane.Alert("Downloading the model the first time might take a while!"),
            top_app_bar,
            pn.Row(model_viewer, pn.layout.HSpacer(), settings_bar, background=BLUE),
            model_viewer.css_pane,
            model_viewer.js_pane,
        ),
    ]
    return template


@site.add(APPLICATION)
def view():
    return create_app()


if __name__.startswith("bokeh"):
    view().servable()
