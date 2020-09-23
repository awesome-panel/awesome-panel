"""# Panel DE:TR:

[DE⫶TR:](https://github.com/facebookresearch/detr) by [Facebook Research](https://research.fb.com/)
provides End-to-End Object Detection with Transformers.

<img style="max-width:100%;height:260px;" \
src="https://github.com/facebookresearch/detr/raw/master/.github/DETR.png"/>

This app is heavily inspired by the [dash-detr](https://github.com/plotly/dash-detr) app.

I hope this provides you with an impression of how this can be implemented in a
[Panel](https://panel.holoviz.org/) context.

I have tried to mature the implementation by

- Adding documentation via Docstrings
- Cleaning up the code so that its satisfies simple code quality checks like Pylint and MyPy
- Implementing some basic tests

Please note this app is running on very low end, cheap hardware which explains the low performance.

**Author:**
[Marc Skov Madsen](https://datamodelsanalytics.com)

**Code:**
[App]\
(https://github.com/MarcSkovMadsen/awesome-panel/blob/master/application/pages/detr/detr.py),
[Tests]\
(https://github.com/MarcSkovMadsen/awesome-panel/blob/master/tests/application/detr/test_detr.py)

**Resources:**
[Dash DE:TR: Demo]\
(https://dash-gallery.plotly.host/dash-detr/)

**Tags:**
[Panel](https://panel.holoviz.org/),
[DE:TR:](https://github.com/facebookresearch/detr)
"""
import base64
import random
import time
from io import BytesIO
from typing import Optional, Set

import panel as pn
import param
import plotly.graph_objects as go
import requests
from PIL import Image

from application.pages.detr import config
from application.pages.detr.model import (
    CLASSES,
    detect,
    filter_boxes,
    get_transform_detr_and_device,
)

# colors for visualization
COLORS = [
    "#fe938c",
    "#86e7b8",
    "#f9ebe0",
    "#208aae",
    "#fe4a49",
    "#291711",
    "#5f4b66",
    "#b98b82",
    "#87f5fb",
    "#63326e",
] * 50


class DETRApp(param.Parameterized):
    "A Panel App for object detection using DE:TR:"
    title = param.String("DE:TR: Object Detection App")

    progress = param.Parameter()

    input_image_url = param.String(config.DEFAULT_URL, label="Input Image URL")
    run_detr = param.Action(label="Run DE:TR:")
    set_random_image = param.Action(label="Random Image")

    plot = param.Parameter()

    suppression_enabled = param.Boolean(config.SUPPRESSION_ENABLED, label="Enabled")
    suppression = param.Number(
        config.SUPPRESSION_DEFAULT,
        bounds=config.SUPPRESSION_BOUNDS,
        label="Non-maximum suppression (IoU)",
    )
    confidence = param.Number(
        config.CONFIDENCE_DEFAULT, bounds=config.CONFIDENCE_BOUNDS, label="Confidence Treshold"
    )

    view = param.Parameter()

    def __init__(self, **params):
        params["progress"], params["plot"], params["view"] = self._get_view()
        params["set_random_image"] = self._set_random_image
        params["run_detr"] = self._update_plot

        super().__init__(**params)

        self.transform, self.detr, self.device = get_transform_detr_and_device()

        self.run_detr()  # pylint: disable=not-callable

    def _get_view(self):
        style = pn.pane.HTML(config.STYLE, width=0, height=0, margin=0, sizing_mode="fixed")

        description = pn.pane.Markdown(__doc__)
        progress = pn.widgets.Progress(
            bar_color="secondary", width=285, sizing_mode="fixed", margin=(0, 5, 10, 5)
        )
        progress.active = False
        app_bar = pn.Row(
            pn.pane.Markdown(
                "# " + self.title, sizing_mode="stretch_width", margin=(None, None, None, 25)
            ),
            sizing_mode="stretch_width",
            margin=(25, 5, 0, 5),
            css_classes=["app-bar"],
        )

        top_selections = pn.Row(
            pn.Param(self, parameters=["input_image_url"], default_layout=pn.Row, show_name=False,),
            pn.Param(
                self,
                parameters=["run_detr", "set_random_image"],
                widgets={"set_random_image": {"button_type": "success"}},
                default_layout=pn.Row,
                show_name=False,
                width=300,
                margin=(14, 5, 5, 5),
                sizing_mode="fixed",
            ),
        )
        top_selections = pn.Row(
            pn.Param(
                self,
                parameters=["input_image_url", "run_detr", "set_random_image"],
                widgets={
                    "set_random_image": {
                        "button_type": "success",
                        "align": "end",
                        "width": 125,
                        "sizing_mode": "fixed",
                    },
                    "run_detr": {"align": "end", "width": 125, "sizing_mode": "fixed"},
                },
                default_layout=pn.Row,
                show_name=False,
                width=900,
            )
        )
        bottom_selections = pn.Column(
            pn.Param(
                self,
                parameters=["suppression", "confidence"],
                default_layout=pn.Row,
                show_name=False,
            ),
            pn.Param(self, parameters=["suppression_enabled"], show_name=False,),
        )
        plot = pn.pane.Plotly(height=600, config={"responsive": True})
        app_view = pn.Column(
            style,
            description,
            app_bar,
            pn.Row(pn.Spacer(), progress),
            top_selections,
            plot,
            bottom_selections,
        )
        return progress, plot, app_view

    def _set_random_image(self, _=None):
        urls = config.RANDOM_URLS
        current_url = self.input_image_url
        new_url = current_url

        while current_url == new_url:
            new_url = random.choice(urls)
        self.input_image_url = new_url
        self._update_plot()

    def _update_plot(self, _=None):
        self.progress.active = True
        self.plot.object = get_figure(
            apply_nms=self.suppression_enabled,
            iou=self.suppression,
            confidence=self.confidence,
            url=self.input_image_url,
            transform=self.transform,
            detr=self.detr,
            device=self.device,
        )
        self.progress.active = False


def view():
    """Used by the awesome-panel.org application to add it to the gallery"""
    return DETRApp().view


# region plotly.py helper functions


def _pil_to_b64(image: Image, enc="png") -> str:
    """Return base 64 encode html data string

    Args:
        image (Image): An Image
        enc (str, optional): Encoding. Defaults to "png".

    Returns:
        str: [description]
    """
    io_buf = BytesIO()
    image.save(io_buf, format=enc)
    encoded = base64.b64encode(io_buf.getvalue()).decode("utf-8")
    return f"data:img/{enc};base64, " + encoded


def _pil_to_fig(image: Image, showlegend=False, title: Optional[str] = None) -> go.Figure:
    """Return a plotly Figure containing the image

    Args:
        image (Image): The image to plot
        showlegend (bool, optional): Whether or not to show the legend. Defaults to False.
        title (Optional[str], optional): The title of the plot. Defaults to None.

    Returns:
        go.Figure: A plot Figure containgin the image
    """

    img_width, img_height = image.size
    fig = go.Figure()
    # This trace is added to help the autoresize logic work.
    fig.add_trace(
        go.Scatter(
            x=[img_width * 0.05, img_width * 0.95],
            y=[img_height * 0.95, img_height * 0.05],
            showlegend=False,
            mode="markers",
            marker_opacity=0,
            hoverinfo="none",
            legendgroup="Image",
        )
    )

    fig.add_layout_image(
        dict(
            source=_pil_to_b64(image),
            sizing="stretch",
            opacity=1,
            layer="below",
            x=0,
            y=0,
            xref="x",
            yref="y",
            sizex=img_width,
            sizey=img_height,
        )
    )

    # Adapt axes to the right width and height, lock aspect ratio
    fig.update_xaxes(showgrid=False, visible=False, constrain="domain", range=[0, img_width])

    fig.update_yaxes(
        showgrid=False, visible=False, scaleanchor="x", scaleratio=1, range=[img_height, 0]
    )

    fig.update_layout(title=title, showlegend=showlegend, autosize=True)

    return fig


def _add_bbox(  # pylint: disable=too-many-arguments
    fig,
    xx0,
    yy0,
    xx1,
    yy1,
    showlegend=True,
    name=None,
    color=None,
    opacity=0.5,
    group=None,
    text=None,
):
    fig.add_trace(
        go.Scatter(
            x=[xx0, xx1, xx1, xx0, xx0],
            y=[yy0, yy0, yy1, yy1, yy0],
            mode="lines",
            fill="toself",
            opacity=opacity,
            marker_color=color,
            hoveron="fills",
            name=name,
            hoverlabel_namelength=0,
            text=text,
            legendgroup=group,
            showlegend=showlegend,
        )
    )


def get_figure(  # pylint: disable=too-many-arguments
    apply_nms: bool, iou: float, confidence: float, url: str, detr, transform, device
) -> go.Figure:
    """Return a plotly figure of the specified url with objects identified and bounding boxes shown

    Args:
        apply_nms (bool): Whether or not to apply the iou value
        iou (float): The iou value. A number between 0 and 1.
        confidence (float): The confidence treshold. A number between 0 and 1
        url (str): The location of the image
        detr (Any): The DETR model
        transform (Any): The DETR transform
        device (Any): The DETR torch.device

    Returns:
        go.Figure: A plotly figure of the specified image
    """
    try:
        im = Image.open(requests.get(url, stream=True).raw)  # pylint: disable=invalid-name
    except OSError:
        return go.Figure().update_layout(title="Invalid URL")

    tstart = time.time()

    scores, boxes = detect(im, detr, transform, device=device)
    scores, boxes = filter_boxes(scores, boxes, confidence=confidence, iou=iou, apply_nms=apply_nms)

    scores = scores.data.numpy()
    boxes = boxes.data.numpy()

    tend = time.time()

    fig = _pil_to_fig(im, showlegend=True, title=f"DETR Predictions ({tend-tstart:.2f}s)")
    existing_classes: Set = set()

    for index in range(boxes.shape[0]):
        _add_bbox_to_figure(
            scores=scores, index=index, boxes=boxes, existing_classes=existing_classes, fig=fig
        )

    return fig


def _add_bbox_to_figure(scores, index, boxes, existing_classes, fig):
    class_id = scores[index].argmax()
    label = CLASSES[class_id]
    confidence = scores[index].max()
    xx0, yy0, xx1, yy1 = boxes[index]

    # only display legend when it's not in the existing classes
    showlegend = label not in existing_classes
    text = f"class={label}<br>confidence={confidence:.3f}"

    _add_bbox(
        fig,
        xx0,
        yy0,
        xx1,
        yy1,
        opacity=0.7,
        group=label,
        name=label,
        color=COLORS[class_id],
        showlegend=showlegend,
        text=text,
    )

    existing_classes.add(label)


# endregion plotly.py helper functions

if __name__.startswith("bokeh"):
    # Run using python -m panel serve 'application\pages\detr\detr.py' --dev --show
    # To get livereloda
    pn.config.sizing_mode = "stretch_width"
    view().servable()
if __name__.startswith("__main__"):
    # Run using python 'application\pages\detr\detr.py'
    # to edit using the Awesome Panel Designer
    from awesome_panel.designer import Designer, ReloadService

    pn.config.sizing_mode = "stretch_width"

    RELOADSERVICES = [ReloadService(component=DETRApp)]
    Designer(reload_services=RELOADSERVICES).view.show(port=5006)
