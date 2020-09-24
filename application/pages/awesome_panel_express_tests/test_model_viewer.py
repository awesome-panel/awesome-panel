"""\
## Model Viewer

Google has developed the `model-viewer` web component for interactively viewing very large and
detailed 3D models.

In this example we will demonstrate how to use the it in a Panel appliccation.

The ModelViewer component and example could potentially be extended a lot by giving access to all
the parameters and models of the `model-viewer`.

If you would like a `model-viewer` example notebook to be an integral part of the Panel gallery go
to GitHub and upvote [PR 1281](https://github.com/holoviz/panel/pull/1281).

**Author:** [Marc Skov Madsen](datamodelsanalytics.com) ([awesome-panel.org](https://awesomepanel.org))

**Code**
[Test Model Viewer]\
(https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/\
awesome_panel_express_tests/test_model_viewer.py),
[ModelViewer Component](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/package/awesome_panel/\
express/components/model_viewer.py)

**Resources:**
[modelviewer.dev](https://modelviewer.dev/),
[examples](https://modelviewer.dev/examples/tester.html),
[codelabs](https://codelabs.developers.google.com/codelabs/model-viewer/index.html?index=..%2F..index#0),
[model-viewer Github](https://github.com/google/model-viewer/tree/master/packages/model-viewer)

**Tags:**
[model-viewer](https://modelviewer.dev/),
[Panel](https://panel.holoviz.org/index.html)
"""

import panel as pn
from awesome_panel.express.components import ModelViewer

MODELVIEWER_LOGO = '<img src="https://avatars1.githubusercontent.com/u/1342004?v=4&amp;s=40" style="height:50px"></img>'
PANEL_LOGO = (
    '<img src="https://panel.holoviz.org/_static/logo_stacked.png" style="height:50px"></img>'
)
BLUE = "#5dbcd2"
GRAY = "#eeeeee"


def create_app(**params):
    top_app_bar = pn.Column(
        pn.layout.Row(
            pn.pane.HTML(MODELVIEWER_LOGO, width=50, sizing_mode="fixed"),
            pn.pane.Markdown(
                "## model-viewer", width=250, sizing_mode="fixed", margin=(0, 5, 10, 5)
            ),
            # pn.pane.HTML(PANEL_LOGO, width=75),
            sizing_mode="stretch_width",
        ),
        pn.layout.HSpacer(height=2),
        height=60,
        sizing_mode="stretch_width",
        background=GRAY,
    )

    model_viewer = ModelViewer(height=500, width=650)

    settings_bar = pn.Param(
        model_viewer,
        parameters=["src", "height", "width", "exposure", "auto_rotate", "camera_controls"],
        width=200,
        sizing_mode="stretch_height",
        background=GRAY,
    )

    return pn.Column(
        pn.pane.Markdown(__doc__),
        top_app_bar,
        pn.Row(model_viewer, pn.layout.HSpacer(), settings_bar, background=BLUE),
        model_viewer.css_pane,
        model_viewer.js_pane,
        sizing_mode="stretch_width",
    )


def view():
    return create_app()


if __name__.startswith("bokeh"):
    view().servable()
