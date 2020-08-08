# Awesome Panel Designer

The *Awesome Panel Designer* is my attempt to create an **efficient workflow for data exploration and development of data apps** in Python **from an editor or IDE**.

This is for **developing any Python object that Panel can display**:

- Strings, Markdown, HTML/ Css/ Javascript
- DataFrames
- Matplotlib, Vega/ Altair, ECharts, Deck.gl, Bokeh, Plotly, HvPlot/ HoloViews, ...
- Panel layouts, widgets, extensions and apps

<video width="100%" height="600" poster="__POSTER__.jpg" controls autoplay>
    <source src="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/docs/packages/awesome-panel-extensions/awesome-panel-designer-guide.mp4?raw=true" type="video/mp4" />
</video><br>

You can read the motivation for why I created the Awesome Panel Designer [here](#what-problem-does-the-designer-solve).

## How to use

1. Define your *components*, i.e. functions and classes. For example

```python
def matplotlib_plot():
    return "Plot"
```

2. Define the list of `components`
3. Add the list to the Designer via `designer=Designer(components=components)`.
    - Optionally you can configure a dictionary of input `parameters` like DataFrames to be used when reloading the component.
    - Optionally you can configure `css_file` or `js_file` to be reloaded.
    - Optionally you can configure additional `modules` to reload.
4. Add `designer.show()` to your code file
5. Run or debug the file from the IDE or terminal.
6. Navigate to [http://localhost:5007](http://localhost:5007) in your browser.

That is it. Now you can start the develop and test cycle.

- Change your code in the Editor.
- Click *reload* in the Designer.
- Take a look at how it looks in the Designer.

Please note that the list of component and the Designer should be in a seperate file. Not together in the same file as your components.

### Example

You will need to install some packages in order to try out the example

```bash
pip install panel awesome-panel-extensions pandas plotly altair hvplot holoviews matplotlib -U
```

The example consists of the two files `example_designer.py` and `example_components.py`.

#### example_designer.py

Please note you will need to adjust `from tests.developer_tools.designer.example.example_components import` to something that works in your environment.

```Python
"""Example that demonstrates the use of the Designer"""
import panel as pn
from bokeh.sampledata import unemployment1948

from awesome_panel_extensions.developer_tools.designer import (
    ComponentReloader, Designer)
# You will need to adjust the import below to something that works in your setting
from tests.developer_tools.designer.example.example_components import (
    altair_bar_plot, get_altair_bar_data, get_holoviews_plot,
    get_plotly_carshare_data, matplotlib_plot, plotly_carshare_plot)

pn.extension("vega", "plotly")

def _designer():
    # Define your components
    altair_reloader = ComponentReloader(
        component=altair_bar_plot, parameters={"data": get_altair_bar_data}
    )
    plotly_reloader = ComponentReloader(
        component=plotly_carshare_plot, parameters={"carshare": get_plotly_carshare_data()},
    )
    holoviews_reloader = ComponentReloader(
        component=get_holoviews_plot, parameters={"data": unemployment1948.data}
    )
    components = [
        matplotlib_plot, # Note: matplotlib_plot is not wrapped in ComponentReloader
        altair_reloader,
        holoviews_reloader,
        plotly_reloader,
    ]

    # Configure the Designer with you components
    return Designer(components=components)

_designer().show()
```

Please note that you only have to wrap your component in the `ComponentReloader` if you want to specify additional depencies like `parameters`, `css_file`, `js_file` or `modules`.

If you have a simple component like `matplotlib_plot` without dependencies you can run it via `Designer(matplotlib_plot).show()` or if you have two via `Designer(components=[matplotlib_plot1, matplotlib_plot2]).show()`.

Please also note that you can run the designer on another port than 5007 by specifying for example `_designer.show(port=5008)`.

#### example_components.py

```Python
import altair as alt
import hvplot.pandas
import numpy as np
import pandas as pd
import plotly.express as px
from matplotlib import cm
from matplotlib.backends.backend_agg import FigureCanvas  # not needed for mpl >= 3.1
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from panel.pane import plotly


def get_plotly_carshare_data():
    return px.data.carshare()


def plotly_carshare_plot(carshare):
    fig = px.scatter_mapbox(
        carshare,
        lat="centroid_lat",
        lon="centroid_lon",
        color="peak_hour",
        size="car_hours",
        color_continuous_scale=px.colors.cyclical.Phase,
        size_max=15,
        zoom=10,
        mapbox_style="carto-positron",
    )
    # Panel does currently not plot responsive Plotly plots well
    # https://github.com/holoviz/panel/issues/1514
    fig.layout.autosize = True
    return fig


def get_altair_bar_data():
    return pd.DataFrame(
        {
            "project": ["a", "b", "c", "d", "e", "f", "g"],
            "score": [25, 57, 23, 19, 8, 47, 8],
            "goal": [25, 47, 30, 27, 38, 19, 4],
        }
    )


def altair_bar_plot(data):
    bar_chart = alt.Chart(data).mark_bar().encode(x="project", y="score")

    tick_chart = (
        alt.Chart(data)
        .mark_tick(color="red", thickness=2, size=40 * 0.9,)  # controls width of tick.
        .encode(x="project", y="goal")
    )

    return (bar_chart + tick_chart).properties(width="container", height="container")


def matplotlib_plot():
    fig = Figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    FigureCanvas(fig)  # not needed for mpl >= 3.1

    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contourf(X, Y, Z, zdir="z", offset=-100, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir="x", offset=-40, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir="y", offset=40, cmap=cm.coolwarm)

    ax.set_xlabel("X")
    ax.set_xlim(-40, 40)
    ax.set_ylabel("Y")
    ax.set_ylim(-40, 40)
    ax.set_zlabel("Z")
    ax.set_zlim(-100, 100)
    return fig


def get_holoviews_plot(data):
    data = data.set_index("Year").drop("Annual", axis=1).transpose()
    return data.hvplot.heatmap(
        x="columns",
        y="index",
        title="US Unemployment 1948—2016",
        cmap=[
            "#75968f",
            "#a5bab7",
            "#c9d9d3",
            "#e2e2e2",
            "#dfccce",
            "#ddb7b1",
            "#cc7878",
            "#933b41",
            "#550b1d",
        ],
        xaxis="top",
        rot=70,
        responsive=True,
        height=800,
    ).opts(toolbar=None, fontsize={"title": 10, "xticks": 5, "yticks": 5},)
```

Thats it. Run the file via `python example_designer.py` or even better via the integrated debugger in your IDE.

## What Problem Does the Designer Solve

Below I will try to describe to motivation behind creating the Awesome Panel Designer.

### My Requirements for an Efficient Work Flow

I'm an experienced data scientist developer.

I want to be able to do rapid exploration and visualization like you can do in a Jupyter Notebook or in BI tools like Tableau or Power BI.

But I also want to develop robust code efficiently using a lot of tools a and best practices from Software Development. For example.

- An awesome editor like VS Code or PyCharm.
    - Integrated debugging.
    - Code navigation
    - Context help etc.
    - Search and navigation across large code bases
- Automated testing using Pytest.
    - Test Driven Development TDD with refactoring.
- Code Quality checks using Black, Pylint and MyPy
- Documentation with Docstrings and Sphinx.
- Collaboration on GitHub, Azure DevOps etc.
- The ability to break down my tools, visualizations, dashboards and apps into smaller components.
- Develop `reactive` applications where I can `subscribe` to `events` like in modern front end frameworks.
    - Panel with Param is perfect for that.
- Develop streaming applications.
    - Panel. HoloViews, Streamz and Param is perfect for that.
- Develop applications powered by Python and extensible from Python.
    - Not from the frontend in Javascript, Typescript, React, Vue, Angular etc.
        - My data friends and colleagues do not master these languages and frameworks. And my users do not care about Themes, Styles, Transitions etc. (I do though :-). So the frontend languages and frameworks become bottlenecks.
    - Panel, HoloViews, Streamz, Param are perfect because they are well integrated and Panel holds state on the Python side and can push from Python to Frontend. Something Voila also provides, but Streamlit and Dash do not.

### As Is: This Holds Me Back

#### Slow feedback cycle

I can't just update a code file and see the output update immediately.

- In my editor or terminal I have to wait for python to start or the Bokeh server to reload which takes +10 secs.
- I also have to reload data from file or database which can take a long time as well. Or alternative save sample datasets locally.
- In Jupyter Notebook I can `importlib.reload` or `%run` my code from code files. But it is tedius to setup, use and maintain in my experience.
- In BI Tools I can drag and drop components, browse parameters and update to see changes. I cant do that efficiently from an editor today. But using BI tools is not what I believe in for other than rapid prototyping. I believe in code and the power of Python for building long term, powerfull and flexible solutions.

##### Slow to browse through and update the parameters of my components

When running from my editor or the terminal its not that efficient to browse through the parameters of components and experiment with changes.

##### Cannot efficiently test what happens when changing parameters

Not possible in editor without doing a breakpoint and updating.

###### Cannot experiment efficiently with layout and styles

Sometimes you need a bit of styling via CSS I want to have a CSS file update it and see the changes. I did not have access to that. Or you need to change the layout of your app. Today that is simply too slow for me due to the slow reload times.

##### Notebook Experience is not efficient for me - not even inside editor

I simply don't find the notebook experience efficient even though a lot of work has been done to bring it to my favorite editor. I simply don't end up with production ready code from it.

But I actually strongly believe in Jupyter Notebooks for a lot of other people like analysts, engineers, traders and scientists. Thats one reason why I look to Panel and not Streamlit or Dash for example. Panel works great in Notebooks while Streamlit and Dash do not.

### To be: The Awesome Panel Designer

Take the best from all worlds and combine it into the `Awesome Panel Designer`.

- A live Python kernel with data extracted and parameters defined on start up. More can be added on the fly.
- Fast reloads after code changes.
- Work in favorite Editor and with code files
- WYSIWYG in browser.
- Files with css or javascript if needed.
- Parameter exploration via built in `pn.Param`.

I can run the `Designer` via `.show`, `.serve` and `.servable` providing a lot of flexibility.

Especially `.show` provides a very, very efficient experience when running together with the integrated debugger in my IDE. Something that has always been a pain for me with other Python frameworks.

## Roadmap: Ideas for improvement

- Add in watchdog to automatically reload when the code is changed.
- Add in the ability to reload the start up parameters and data.
- Add in the some style editor like a Material Design Style editor for easy styling.
- Implement more clever module reloading.
    - Right now I'm just reloading the module containing the component. But it works great.
- Improve parameter exploration via `pn.Param`.
- Make it easy to transfer changes from Parameters explorer back to code.

## Feedback: Please share your thoughts and ideas

- Am I reinventing the wheel?
- What is holding you back today when working with Python Data Exploration or with Panel?
- Could the `Designer` be something for you?
- How could it be improved?
- What works great in other stacks? Could we get some inspiration?
