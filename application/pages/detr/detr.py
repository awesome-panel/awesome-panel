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
from awesome_panel_extensions.io.loading import start_loading_spinner, stop_loading_spinner
from PIL import Image

from application.config import site
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
APPLICATION = site.create_application(
    url="detr",
    name="DE:TR: Object Detection",
    author="Marc Skov Madsen",
    introduction="An image recognition app based on Facebook DE:TR and Plotly",
    description=__doc__,
    thumbnail_url="detr.png",
    documentation_url="",
    code_url="detr/detr.py",
    gif_url="",
    mp4_url="",
    tags=[
        "DE:TR",
        "Plotly",
    ],
)


class DETRApp(param.Parameterized):  # pylint: disable=too-many-instance-attributes
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
        start_loading_spinner(self.plot)

    def _stop_progress(self):
        stop_loading_spinner(self.plot)

    def _get_view(self):
        pn.config.sizing_mode = "stretch_width"
        style = pn.pane.HTML(config.STYLE, width=0, height=0, margin=0, sizing_mode="fixed")

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
        intro_section = APPLICATION.intro_section()
        main = [
            pn.Column(
                style,
                intro_section,
            ),
            pn.Column(
                app_bar,
                top_selections,
                plot,
                bottom_selections,
            ),
        ]
        template = site.create_template(
            title="Panel DE:TR",
            theme="default",
            main=main,
        )
        return plot, template

    def _set_random_image(self, _=None):
        self._start_progress()
        urls = config.RANDOM_URLS
        current_url = self.input_image_url
        new_url = current_url

        while current_url == new_url:
            new_url = random.choice(urls)
        self.input_image_url = new_url
        self._update_plot()

    def _update_plot(self, _=None):
        self._start_progress()
        figure = get_figure(
            apply_nms=self.suppression_enabled,
            iou=self.suppression,
            confidence=self.confidence,
            url=self.input_image_url,
            transform=self.transform,
            detr=self.detr,
            device=self.device,
        )
        self.plot.object = figure
        self._stop_progress()


@site.add(APPLICATION)
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
    view().servable()
if __name__.startswith("__main__"):
    # Run using python 'application\pages\detr\detr.py'
    view().show(port=5007)
