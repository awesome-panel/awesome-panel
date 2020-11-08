import numpy as np
import panel as pn
import plotly.graph_objs as go

pn.extension("plotly")
pn.config.sizing_mode = "stretch_width"


def create_plot():
    t = np.linspace(0, 10, 50)
    x, y, z = np.cos(t), np.sin(t), t
    fig = go.Figure(
        data=go.Scatter3d(x=x, y=y, z=z, mode="markers"), layout=dict(title="3D Scatter Plot")
    )
    fig.layout.autosize = True
    return fig


plot = create_plot()
plot_panel = pn.pane.Plotly(plot, config={"responsive": True}, sizing_mode="stretch_both")


@pn.depends(plot_panel.param.click_data, watch=True)
def print_hello_world(click_data):
    print("hello world", click_data)


@pn.depends(plot_panel.param.click_data)
def string_hello_world(click_data):
    return click_data


app = pn.Column(plot_panel, string_hello_world)

app.servable()
