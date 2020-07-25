# Bokeh Extensions

**Bokeh Extensions** supports efficient, bidirectional communication from the server (Python) to the browser (Javascript) and back. It also gives you access to all the super powers of modern front end framework languages (js or typescript), tooling and frameworks like React, Vue and Angular. The layouts, panes and widgets that ships with Panel are Bokeh extensions.

Please note that in order for Bokeh Extensions to compile you will need to have [node.js](https://nodejs.org) installed. You can install it directly from their web site or via `conda install -c conda-forge nodejs`.

Before you read on I would ask you to quickly study the offical Bokeh documentation [Extending Bokeh](https://docs.bokeh.org/en/latest/docs/user_guide/extensions.html). You don't need to code and run the examples. But you need to get a basic understanding of

- the existence and location of official Bokeh documentation
- what a Bokeh extension is and how it is developed.

We will now focus on Bokeh Extensions in a Panel context.

## Example

In this example we will create a Panel `HTMLButton` extension that enables a user
to catch a click event from any HTML element he/ she would like as shown below.

[![html_button.py](html-button.gif)](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/html_button/html_button.py)

The implentation consists of 3 files

- Panel extension file: [html_button.py](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/html_button/html_button.py).
- Bokeh extensions files: [html_button_model.py](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/html_button/html_button_model.py) and [html_button_model.ts](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/html_button/html_button_model.ts)

**[html_button.py](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/html_button/html_button.py)**

This is the Panel specific file. We need to import the Bokeh python extension and wrap that into a Panel extension.

```Python
import panel as pn
from panel.widgets.base import Widget
from . import html_button_model
import param

class HTMLButton(Widget):
    # Set the Bokeh model to use
    _widget_type = html_button_model.HTMLButton

    # Rename Panel Parameters -> Bokeh Model properties
    # Parameters like title that does not exist on the Bokeh model should be renamed to None
    _rename = {
        "title": None,
    }

    # Parameters to be mapped to Bokeh model properties
    object = param.String(default=html_button_model.DEFAULT_OBJECT)
    clicks = param.Integer(default=0)
```

**[html_button_model.py](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/html_button/html_button_model.py)**

```Python
import pathlib

from bokeh.core.properties import Int, String
from bokeh.layouts import column
from bokeh.models import HTMLBox

CUSTOM_TS = pathlib.Path(__file__).parent / "html_button_model.ts"
CUSTOM_TS_STR = str(CUSTOM_TS.resolve())

DEFAULT_OBJECT = "<button style='width:100%'>Click Me</button>"


class HTMLButton(HTMLBox):
    """Example implementation of a Custom Bokeh Model"""

    __implementation__ = CUSTOM_TS_STR

    object = String(default=DEFAULT_OBJECT)
    clicks = Int(default=0)
```

**[html_button_model.ts](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/html_button/html_button_model.ts)**

```typescript
// See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
import { HTMLBox, HTMLBoxView } from "models/layouts/html_box"

// See https://docs.bokeh.org/en/latest/docs/reference/core/properties.html
import * as p from "core/properties"

// The view of the Bokeh extension/ HTML element
// Here you can define how to render the model as well as react to model changes or View events.
export class HTMLButtonView extends HTMLBoxView {
    model: HTMLButton
    objectElement: any // Element

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.object.change, () => {
            this.render();
        })
    }

    render(): void {
        console.log("render")
        console.log(this.model)
        super.render()
        this.el.innerHTML = this.model.object
        this.objectElement = this.el.firstElementChild

        this.objectElement.addEventListener("click", () => {this.model.clicks+=1;}, false)
    }
}

export namespace HTMLButton {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        object: p.Property<string>,
        clicks: p.Property<number>,
    }
}

export interface HTMLButton extends HTMLButton.Attrs { }

// The Bokeh .ts model corresponding to the Bokeh .py model
export class HTMLButton extends HTMLBox {
    properties: HTMLButton.Props

    constructor(attrs?: Partial<HTMLButton.Attrs>) {
        super(attrs)
    }

    static init_HTMLButton(): void {
        this.prototype.default_view = HTMLButtonView;

        this.define<HTMLButton.Props>({
            object: [p.String, "<button style='width:100%'>Click Me</button>"],
            clicks: [p.Int, 0],
        })
    }
}
```

Finally we can use the new Widget in an example app.

```python
def _example_app():
    # Default Button
    html_button = HTMLButton()

    # Material Button
    material_js = (
        "https://cdn.jsdelivr.net/gh/marcskovmadsen/awesome-panel"
        "@be59521090b7c9d9ba5eb16e936034e412e2c86b/assets/js/mwc.bundled.js"
    )
    pn.config.js_files["material"]=material_js
    material_html = """\
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Material+Icons&display=block" rel="stylesheet">
<style>
mwc-button {
    --mdc-theme-primary: #4CAF50;
    --mdc-theme-on-primary: white;
}
</style>
    """
    material_html_pane = pn.pane.HTML(material_html, width=0, height=0, margin=0, sizing_mode="fixed")
    material_button = HTMLButton(object="<mwc-button style='width:100%' raised label='Panel' icon='favorite'></mwc-button>", height=40)

    # Image Button
    src = "https://github.com/holoviz/panel/raw/master/doc/_static/logo_stacked.png"
    image_style = "height:95%;cursor: pointer;border: 1px solid #ddd;border-radius: 4px;padding: 5px;"
    image_html = f"<img class='image-button' src='{src}' style='{image_style}'>"
    image_button = HTMLButton(object=image_html, height=100, align="center")

    # Bar
    bar = pn.pane.Markdown(
        "## Panel Extension: HTMLButton",
        background="black",
        sizing_mode="stretch_width",
        style={"color": "white", "padding-left": "25px", "padding-top": "10px"},
    )

    app = pn.Column(
        bar,
        material_html_pane,
        html_button,
        html_button.param.clicks,
        material_button,
        material_button.param.clicks,
        image_button,
        image_button.param.clicks,
        width=500,
    )
    return app

_example_app().servable()
```

## Other Examples

**Click the images** below to see the code.

[![Custom Bokeh Model](custom-bokeh-model.gif)](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/guide/custom_bokeh_model)

NOTE: THE CUSTOM BOKEH MODEL EXAMPLES NEEDS TO BE WRAPPED INTO A PANEL OBJECT. COMING UP.

## Official Panel Examples

Every layout, pane or widget in Panel is essentially a Bokeh Extension so a good place to get inspiration is to navigate the [Panel Reference Gallery](https://panel.holoviz.org/reference/index.html) to find an extension similar to the one you would like to implement and then study the code

[![Panel Reference Gallery](panel-reference-gallery.gif)](https://panel.holoviz.org/reference/index.html)

You can find the code of the Panel components on Github via

- [Panel Layouts](https://github.com/holoviz/panel/tree/master/panel/layout)
- [Panel Panes](https://github.com/holoviz/panel/tree/master/panel/pane)
- [Panel Widgets](https://github.com/holoviz/panel/tree/master/panel/widgets)

and the underlying Bokeh extensions via

- [Bokeh Model Widgets](https://github.com/bokeh/bokeh/tree/master/bokehjs/src/lib/models/widgets)
- [Panel Bokeh Models](https://github.com/holoviz/panel/tree/master/panel/models)

## Prebuilt Bokeh Extensions

There are two ways in which the Bokeh `.ts` models can be built.

- **Automatically** when you run the code.
  1. If you instantiate your extension before running `.servable` then the extension will automatically be built and registered by Panel/ Bokeh.
- **Manually** up front using the `panel build` or `bokeh build`command.
  2. This is referred to as *prebuilt Bokeh extensions*.

In this document I will describe how I setup the awesome-panel-extensions package for **prebuilt bokeh extensions**. **This was nescessary to distribute the extensions as a package.**

I hope this description can help others who would like to develop and share Bokeh Extensions for Panel.

Setting up prebuilt extensions using `Bokeh init --interactive` is described in the Bokeh Docs. See [Bokeh Pre-built extensions](https://docs.bokeh.org/en/latest/docs/user_guide/extensions.html).

### Steps for the `awesome-panel-extensions` Package as of 20200721 Panel 0.9.7/ Bokeh 2.1.1

I navigated to the `awesome_panel_extensions` inside the project.

```bash
cd awesome_panel_extensions
```

I ran `bokeh init --interactive`

```bash
$ bokeh init --interactive
Working directory: ...\awesome_panel_extensions
Wrote ...\awesome_panel_extensions\bokeh.ext.json
Create package.json? This will allow you to specify external dependencies. [y/n] y
  What's the extension's name? [awesome_panel_extensions]
  What's the extension's version? [0.0.1]
  What's the extension's description? [] A collection of awesome extensions for Panel
Wrote ...\awesome_panel_extensions\package.json
Create tsconfig.json? This will allow for customized configuration and improved IDE experience. [y/n] y
Wrote ...\awesome_panel_extensions\tsconfig.json
Created empty index.ts. This is the entry point of your extension.
You can build your extension with bokeh build
All done.
```

In the `package.json` I replaced

```ts
"dependencies": {
    "bokehjs": "^2.1.1"
  },
```

with

```ts
"dependencies": {
    "@bokeh/bokehjs": "^2.1.1"
  },
```

in order to import from bokehjs in the same way as Panel does. See [bokeh init issue](https://github.com/bokeh/bokeh/issues/10055) for more info.

I also replaced the `tsconfig.json` contents with

```ts
{
  "compilerOptions": {
    "noImplicitAny": true,
    "noImplicitThis": true,
    "noImplicitReturns": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "strictNullChecks": true,
    "strictBindCallApply": false,
    "strictFunctionTypes": false,
    "strictPropertyInitialization": false,
    "alwaysStrict": true,
    "noErrorTruncation": true,
    "noEmitOnError": false,
    "declaration": true,
    "sourceMap": true,
    "importHelpers": false,
    "experimentalDecorators": true,
    "module": "esnext",
    "moduleResolution": "node",
    "esModuleInterop": true,
    "resolveJsonModule": true,
    "skipLibCheck": true,
    "target": "ES2017",
    "lib": ["es2017", "dom", "dom.iterable"],
    "baseUrl": ".",
    "outDir": "./dist/lib",
    "paths": {
      "@bokehjs/*": [
        "./node_modules/@bokeh/bokehjs/build/js/lib/*",
        "./node_modules/@bokeh/bokehjs/build/js/types/*"
      ]
    }
  },
  "include": ["./**/*.ts"]
}
```

At least including the `paths` section is needed to be able to `import { div, label } from "@bokehjs/core/dom"` like @philippjfr does in Panel.

In the `index.ts` file I imported my models

```ts
import * as AwesomePanelExtensions from "./bokeh_extensions/"
export {AwesomePanelExtensions}

import {register_models} from "@bokehjs/base"
register_models(AwesomePanelExtensions as any)
```

In the `bokeh_extensions/index.ts` file I exported the `WebComponent`.

```ts
export {WebComponent} from "./web_component"
```

Then I could `build` my extension

```bash
$ panel build
Working directory: C:\repos\private\awesome-panel\package\awesome_panel
Using C:\repos\private\awesome-panel\package\awesome_panel\tsconfig.json
Compiling TypeScript (3 files)
Linking modules
Output written to C:\repos\private\awesome-panel\package\awesome_panel\dist
All done.
```

The result is in the `dist` folder.

I discovered I did not even have to do anything special to `serve` the `awesome_panel_extensions.js` file. It just works.

Finally I added `awesome_panel_extensions/node_modules/*`to my `.gitignore` file.

## FAQ

### Should I define default values on the Bokeh .ts, Bokeh .py or Panel .py Model

COMING UP.
