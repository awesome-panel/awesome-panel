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
