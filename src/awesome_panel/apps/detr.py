"""[DE⫶TR:](https://github.com/facebookresearch/detr) by
[Facebook Research](https://research.fb.com/) provides End-to-End Object Detection with
Transformers.

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

from awesome_panel import config
from awesome_panel.apps.detr_utils.model import (
    CLASSES,
    detect,
    filter_boxes,
    get_transform_detr_and_device,
)

# Source: https://github.com/plotly/dash-detr/blob/master/random_urls.txt
RANDOM_URLS = [
    "http://farm5.staticflickr.com/4115/4808627642_46feddf8c3_z.jpg",
    "http://farm6.staticflickr.com/5060/5580489202_d43295ea0b_z.jpg",
    "http://farm5.staticflickr.com/4103/5200926590_b29e3d62fb_z.jpg",
    "http://farm1.staticflickr.com/40/124035573_3f564a25aa_z.jpg",
    "http://farm9.staticflickr.com/8468/8097377641_595d31201b_z.jpg",
    "http://farm8.staticflickr.com/7237/7000138695_2513fc8eda_z.jpg",
    "http://farm4.staticflickr.com/3034/2576825166_233687201d_z.jpg",
    "http://farm5.staticflickr.com/4044/4482245176_782b8932f7_z.jpg",
    "http://farm1.staticflickr.com/38/83651631_9224bb6450_z.jpg",
    "http://farm4.staticflickr.com/3651/3470749993_a1d0338644_z.jpg",
    "http://farm4.staticflickr.com/3185/3018575673_65a91be272_z.jpg",
    "http://farm9.staticflickr.com/8244/8513526968_27242c043b_z.jpg",
    "http://farm7.staticflickr.com/6076/6154897961_0d21ef0efe_z.jpg",
    "http://farm4.staticflickr.com/3212/4052516930_d8bc24404c_z.jpg",
    "http://farm5.staticflickr.com/4041/4604523114_6f06dcba15_z.jpg",
    "http://farm4.staticflickr.com/3140/2574052691_a596cf3d08_z.jpg",
    "http://farm3.staticflickr.com/2426/3904552439_363f28aa68_z.jpg",
]
DEFAULT_URL = RANDOM_URLS[0]

SUPPRESSION_ENABLED = False
SUPPRESSION_BOUNDS = (0.0, 1.0)
SUPPRESSION_DEFAULT = 0.5

CONFIDENCE_BOUNDS = (0.0, 1.0)
CONFIDENCE_DEFAULT = 0.7

STYLE = """
<style>
div.bk.app-bar {
    background-color: #3b5998;
    background-image: linear-gradient(rgb(78, 105, 162), rgb(59, 89, 152) 50%);
    border-bottom: 1px solid #133783;
    color: white;
</style>
"""

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

if not "detr" in pn.state.cache:
    pn.state.cache["detr"] = {}


class DETRApp(param.Parameterized):  # pylint: disable=too-many-instance-attributes
    "A Panel App for object detection using DE:TR:"
    title = param.String("DE:TR: Object Detection App")

    progress = param.Parameter()

    input_image_url = param.String(DEFAULT_URL, label="Input Image URL")
    run_detr = param.Action(label="Run DE:TR:")
    set_random_image = param.Action(label="Random Image")

    plot = param.Parameter()

    suppression_enabled = param.Boolean(SUPPRESSION_ENABLED, label="Enabled")
    suppression = param.Number(
        SUPPRESSION_DEFAULT,
        bounds=SUPPRESSION_BOUNDS,
        label="Non-maximum suppression (IoU)",
    )
    confidence = param.Number(
        CONFIDENCE_DEFAULT, bounds=CONFIDENCE_BOUNDS, label="Confidence Treshold"
    )

    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self.plot, self.view = self._get_view()
        self._start_progress()
        self.set_random_image = self._set_random_image
        self.run_detr = self._update_plot

        self.transform = None
        self.detr = None
        self.device = None
        pn.state.onload(self._init_on_load)

    def _init_on_load(self):
        self._start_progress()
        self.transform, self.detr, self.device = get_transform_detr_and_device()

        self.run_detr()  # pylint: disable=not-callable
        self._stop_progress()

    def _start_progress(self):
        self.app_section.loading = True

    def _stop_progress(self):
        self.app_section.loading = False

    def _get_view(self):
        style = pn.pane.HTML(STYLE, width=0, height=0, margin=0, sizing_mode="fixed")

        app_bar = pn.Row(
            pn.pane.Markdown("# " + self.title, sizing_mode="stretch_width", margin=(0, 0, 0, 25)),
            sizing_mode="stretch_width",
            margin=(25, 5, 0, 5),
            css_classes=["app-bar"],
        )

        top_selections = pn.Row(
            pn.Param(
                self,
                parameters=["input_image_url", "run_detr", "set_random_image"],
                widgets={
                    "set_random_image": {
                        "align": "end",
                        "width": 125,
                        "sizing_mode": "fixed",
                        "button_type": "primary",
                    },
                    "run_detr": {
                        "align": "end",
                        "width": 125,
                        "sizing_mode": "fixed",
                    },
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
            pn.Param(
                self,
                parameters=["suppression_enabled"],
                show_name=False,
            ),
        )
        plot = pn.pane.Plotly(height=600, config={"responsive": True})
        self.app_section = pn.Column(
            app_bar,
            top_selections,
            plot,
            bottom_selections,
        )
        view = pn.Column(
            style,
            self.app_section,
        )
        return plot, view

    def _set_random_image(self, _=None):
        self._start_progress()
        urls = RANDOM_URLS
        current_url = self.input_image_url
        new_url = current_url

        while current_url == new_url:
            new_url = random.choice(urls)
        self.input_image_url = new_url
        self._update_plot()

    def _update_plot(self, _=None):
        self._start_progress()
        if not self.input_image_url in pn.state.cache["detr"]:
            pn.state.cache["detr"][self.input_image_url] = get_figure(
                apply_nms=self.suppression_enabled,
                iou=self.suppression,
                confidence=self.confidence,
                url=self.input_image_url,
                transform=self.transform,
                detr=self.detr,
                device=self.device,
            )
        figure = pn.state.cache["detr"][self.input_image_url]
        self.plot.object = figure
        self._stop_progress()

    def __repr__(self):
        return "DETRApp()"


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


def get_figure(  # pylint: disable=too-many-arguments, too-many-locals
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
        image = Image.open(
            requests.get(url, stream=True, timeout=10).raw
        )  # pylint: disable=invalid-name
    except OSError:
        return go.Figure().update_layout(title="Invalid URL")

    tstart = time.time()

    scores, boxes = detect(image, detr, transform, device=device)
    scores, boxes = filter_boxes(scores, boxes, confidence=confidence, iou=iou, apply_nms=apply_nms)

    scores = scores.data.numpy()
    boxes = boxes.data.numpy()

    tend = time.time()

    fig = _pil_to_fig(image, showlegend=True, title=f"DETR Predictions ({tend-tstart:.2f}s)")
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
    config.extension(url="detr")

    DETRApp().view.servable()
