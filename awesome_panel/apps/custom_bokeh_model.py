"""
One super power of Panel is that its actually extensible. You can write custom Panes, Layouts and
Widgets using Bokeh Extensions. This is actually how Panel is developed.

If you want to learn how to create custom Bokeh/ Panel extensions you can
**[checkout the Awesome Panel Extensions Guide]\
(https://awesome-panel.readthedocs.io/en/latest/guides/awesome-panel-extensions-guide/index.html)**
"""


import panel as pn
from bokeh.core.properties import Instance, String
from bokeh.layouts import column
from bokeh.models import HTMLBox, Slider

from awesome_panel import config

IMPLEMENTATION_TS = """
import { HTMLBox, HTMLBoxView } from "models/layouts/html_box"

import { div } from "core/dom"
import * as p from "core/properties"
import { Slider } from "models/widgets/slider"

export class CustomView extends HTMLBoxView {
    model: Custom

    connect_signals(): void {
        console.info("connect_signals");
        super.connect_signals()

        this.connect(this.model.slider.change, () => {
            console.info("slider change call back");
            this.render();
        })
    }

    render(): void {
        console.info("render");
        super.render()

        this.el.appendChild(div({
            style: {
                padding: '2px',
                color: '#b88d8e',
                backgroundColor: '#2a3153',
            },
        }, `${this.model.text}: ${this.model.slider.value}`))
    }
}

export namespace Custom {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        slider: p.Property<Slider>
        text: p.Property<string>
    }
}

export interface Custom extends Custom.Attrs { }

export class Custom extends HTMLBox {
    properties: Custom.Props

    constructor(attrs?: Partial<Custom.Attrs>) {
        super(attrs)
    }

    static init_Custom(): void {
        this.prototype.default_view = CustomView;

        this.define<Custom.Props>({
            text: [p.String],
            slider: [p.Instance],
        })
    }
}
"""


class Custom(HTMLBox):
    """Example implementation of a Custom Bokeh Model"""

    __implementation__ = IMPLEMENTATION_TS

    text = String(default="Custom text")

    slider = Instance(Slider)


config.extension(url="custom_bokeh_model")

slider = Slider(start=0, end=10, step=0.1, value=0, title="value")
custom = Custom(text="Special Slider Display", slider=slider)
layout = column(slider, custom, sizing_mode="stretch_width")

pn.pane.Bokeh(layout).servable()
