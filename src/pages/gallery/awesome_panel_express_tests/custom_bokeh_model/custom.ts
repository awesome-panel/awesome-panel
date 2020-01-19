import { HTMLBox, HTMLBoxView } from "models/layouts/html_box"

import { div } from "core/dom"
import * as p from "core/properties"

export class CustomView extends HTMLBoxView {

    connect_signals(): void {
        super.connect_signals()

        // Set BokehJS listener so that when the Bokeh slider has a change
        // event, we can process the new data.
        this.connect(this.model.slider.change, () => {
            this.render()
            this.invalidate_layout()
        })
    }

    render(): void {
        // BokehjS Views create <div> elements by default, accessible as
        // ``this.el``. Many Bokeh views ignore this default <div>, and instead
        // do things like draw to the HTML canvas. In this case though, we change
        // the contents of the <div>, based on the current slider value.
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

export class Custom extends HTMLBox {
    slider: { value: string }

    // The ``__name__`` class attribute should generally match exactly the name
    // of the corresponding Python class. Note that if using TypeScript, this
    // will be automatically filled in during compilation, so except in some
    // special cases, this shouldn't be generally included manually, to avoid
    // typos, which would prohibit serialization/deserialization of this model.
    static __name__ = "Custom"

    static init_Custom(): void {
        // If there is an associated view, this is typically boilerplate.
        this.prototype.default_view = CustomView

        // The this.define() block adds corresponding "properties" to the JS model.
        // These should normally line up 1-1 with the Python model class. Most property
        // types have counterparts, e.g. bokeh.core.properties.String will be
        // ``p.String`` in the JS implementation. Any time the JS type system is not
        // yet as complete, you can use ``p.Any`` as a "wildcard" property type.
        this.define<Custom.Props>({
            text: [p.String],
            slider: [p.Any],
        })
    }
}
