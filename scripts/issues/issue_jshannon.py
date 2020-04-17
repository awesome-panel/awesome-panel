# %% Import libraries.
# Import third party libraries.
import numpy as np
import pandas as pd
import panel as pn
import plotly.graph_objects as go


# %% Define functions.
def random_walk(stdev=0.03):
    """
    Summary
    -------
    Function creating a `pandas` DataFrame of 3 columns, each containing random
    walk data based on provided standard deviation.

    """
    df = pd.DataFrame(np.random.normal(1, 0.03, (100, 3)), columns="JAS BPL AKK".split())
    df.loc[0] = 1
    df = df.cumprod()
    df *= 40
    return df


def plotly_graph(df):
    """
    Summary
    -------
    Function to create a `plotly` graph with a provided DataFrame.

    """
    fig = go.Figure()
    for c in df.columns:
        trace = go.Scatter(x=df.index, y=df[c].values, mode="lines+markers", name=c)
        fig.add_trace(trace)
    fig.update_layout(hovermode="x")
    return fig


def panel_wrapper(stdev=0.03, dummy_catagory="default"):
    """
    Summary
    -------
    Wrapper function to allow `panel` to redraw `plotly` graphs based on web
    visualization parameter inputs.

    """
    return plotly_graph(random_walk(stdev=stdev))


def main(method_num):
    # Method 1: Quickly create a web visualization with Python back-end
    #           support.
    if method_num == 1:
        # NOTE: Documentation states, "Initializes the pyviz notebook extension
        #       to allow plotting with bokeh and enable comms." It seems that
        #       `panel.extension` is not required when generating web
        #        visualizations with the `.show()` method.
        pn.extension()
        pn.interact(panel_wrapper).show()
    # Method 2: Adjust the layout of the quick creation in Method 1.
    if method_num == 2:
        i = pn.interact(panel_wrapper)
        text = "<br>\n# Random Walk as a Function of Standard Deviation"
        p = pn.Row(i[1][0], pn.Column(text, i[0][0]))
        p.show()
    # Method 3, 4, & 5: Explicitly build the panel objects.
    if method_num == 3 or method_num == 4 or method_num == 5:
        c_opts = ["default", "optimized", "calibrated", "variable"]
        dummy_catagory = pn.widgets.RadioButtonGroup(
            name="dummy_catagory", value="default", options=c_opts
        )
        stdev = pn.widgets.FloatSlider(name="stdev", value=0.03, start=0, end=0.1, step=0.01)

        @pn.depends(stdev, dummy_catagory)
        def reactive_panel(stdev, dummy_catagory):
            return panel_wrapper(stdev, dummy_catagory)

        text = "<br>\n# Random Walk as a Function of Standard Deviation"
        widgets = pn.Column(text, stdev, dummy_catagory)
        p_rw = pn.Row(reactive_panel, widgets)
    # Method 3: Deploy a web visualization with a Python server.
    if method_num == 3:
        p_rw.show()
    # Method 4: Deploy a web visualization with data embedded in HTML.
    # NOTE: This stand alone version works with the following web browsers:
    #           - Chrome Version 80.0.3987.122
    #           - Microsoft Edge 41.16299.1480.0
    #       This stand alone version does not work with the following web
    #       browsers:
    #           - Internet Explorer Version 11.1685.16299.0.
    if method_num == 4:
        f_out = "test.html"
        p_rw.save(f_out, title="This is a test", embed=True, max_opts=10)
    # Method 5: Deploy a web visualization referencing json data files.
    if method_num == 5:
        f_out = "test_json.html"
        p_rw.save(f_out, title="This is a test", embed=True, max_opts=10, embed_json=True)
    return 0


# %% Execute script.
if __name__ == "__main__":
    # Select input 1 - 5. See source code notes in main() for more info.
    _ = main(5)
