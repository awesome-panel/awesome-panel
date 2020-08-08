# Awesome Panel Extensions Package

The Awesome Panel Extensions package contains Panel Extensions that add to the power of Panel.

## Installation

You can install the package via

```python
pip install awesome-panel-extensions
```

Each individual extension might depend on additional packages. For example the `awesome_panel_extensions.panes.PandasProfileReport` depends on the [Pandas Profiling](https://github.com/pandas-profiling/pandas-profiling) package.

## Reference Gallery

Check out the extensions by clicking the images below.

### Panes

#### PandasProfileReport

[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fpanes%2FPandasProfileReport.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/panes/PandasProfileReport.ipynb)

[![PandasProfileReport](pandas-profile-report-notebook.png)](https://github.com/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/panes/PandasProfileReport.ipynb)

Use it via `awesome_panel_extensions.pane.PandasProfileReport`.

#### WebComponent

[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fpanes%2FWebComponent.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/panes/WebComponent.ipynb)

You can think of the `WebComponent` as a `HTML` pane that supports bidirectional communication and large data transfer.

You can use the `WebComponent` to quickly **plugin web component or javascript libraries**.

So if you are not satisfied with the look and feel of the existing Panel widgets then use the `WebComponent` to plug in your favourite set of widgets. Or if the `DataFrame` pane or widget is not enough for your use case, then plugin an alternative data table.

For an introduction to *web components* see [Web Components: the secret ingredient helping Power the web](https://www.youtube.com/watch?v=YBwgkr_Sbx0).

<a href="https://www.youtube.com/watch?v=YBwgkr_Sbx0" target="blank_"><img src="https://i.ytimg.com/vi/YBwgkr_Sbx0/hqdefault.jpg"></img></a>

Use it via `awesome_panel_extensions.web_component.WebComponent`.

### Widgets

#### LinkButtons

[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/marcskovmadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fwidgets%2FLinkButtons.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/marcskovmadsen/awesome-panel-extensions/blob/master/examples/reference/widgets/LinkButtons.ipynb)

[![LinkButtons](link_buttons.png)](https://nbviewer.jupyter.org/github/marcskovmadsen/awesome-panel-extensions/blob/master/examples/reference/widgets/LinkButtons.ipynb)

Use them via `awesome_panel_extensions.widgets.link_buttons`.

#### PerspectiveViewer

The `PerspectiveViewer` is perfect for interactive, streaming analytics of large amounts of data.

[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fwidgets%2FPerspectiveViewer.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/widgets/PerspectiveViewer.ipynb)

[![PerspectiveViewer](perspective-viewer-finos.gif)](https://mybinder.org/v2/gh/marcskovmadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fwidgets%2FPerspectiveViewer.ipynb)

Use it via `awesome_panel_extensions.widgets.perspective_viewer.PerspectiveViewer`

### Frameworks

#### Material

The Material Extensions are based on the [MWC Material Web Components](https://github.com/material-components/material-components-web-components) and [Material Design](https://material.io/design).

Please note that you need to add the Material `Extension` and `Stylesheet` components to you app to setup the js and css requirements.

Please also note that the Material Widgets **do not work in older browsers** like Internet Explorer.

#### Material Button

[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fframeworks%2Fmaterial%2FMaterialButton.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/frameworks/material/MaterialButton.ipynb)

[![Material Button](material-button.png)](https://mybinder.org/v2/gh/marcskovmadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fframeworks%2Fmaterial%2FMaterialButton.ipynb)

Use it via `awesome_panel_extensions.frameworks.material.Button`

#### Material Select

[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fframeworks%2Fmaterial%2FMaterialSelect.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/frameworks/material/MaterialSelect.ipynb)

[![Material Button](mwc-select.png)](https://mybinder.org/v2/gh/marcskovmadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fframeworks%2Fmaterial%2FMaterialSelect.ipynb)

Use it via `awesome_panel_extensions.frameworks.material.Select`

#### Material IntSlider

[<img src="https://mybinder.org/badge_logo.svg" style="height:25px;display:inline;margin:5px">](https://mybinder.org/v2/gh/MarcSkovMadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fframeworks%2Fmaterial%2FMaterialIntSlider.ipynb) [<img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" style="height:25px;display:inline;margin:5px">](https://nbviewer.jupyter.org/github/MarcSkovMadsen/awesome-panel-extensions/blob/master/examples/reference/frameworks/material/MaterialIntSlider.ipynb)

[![Material IntSlider](mwc-slider.png)](https://mybinder.org/v2/gh/marcskovmadsen/awesome-panel-extensions/master?filepath=examples%2Freference%2Fframeworks%2Fmaterial%2FMaterialIntSlider.ipynb)

Use it via `awesome_panel_extensions.frameworks.material.IntSlider`.

### Developer Tools

#### Awesome Panel Designer

The *Awesome Panel Designer* is my attempt to create an **efficient workflow for data exploration and development of data apps** in Python **from an editor or IDE**.

This is for **developing any Python object that Panel can display**:

- Strings, Markdown, HTML/ Css/ Javascript
- DataFrames
- Matplotlib, Vega/ Altair, ECharts, Deck.gl, Bokeh, Plotly, HvPlot/ HoloViews, ...
- Panel layouts, widgets, extensions and apps

Use it via `from awesome_panel_extensions.developer_tools.designer import Designer`.

For more info click the link below.

* [Awesome Panel Designer Docs](designer.md)

<video width="640" height="360" poster="__POSTER__.jpg" controls autoplay>
    <source src="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/docs/packages/awesome-panel-extensions/awesome-panel-designer-guide.mp4?raw=true" type="video/mp4" />
</video>
