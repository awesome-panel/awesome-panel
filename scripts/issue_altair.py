import altair as alt
import numpy as np
import pandas as pd
import panel as pn


def make_plot():
    # Example heatmap from
    # https://altair-viz.github.io/gallery/simple_heatmap.html
    # with increased width/height

    # Compute x^2 + y^2 across a 2D grid
    x, y = np.meshgrid(range(-5, 5), range(-5, 5))
    z = x ** 2 + y ** 2

    # Convert this grid to columnar data expected by Altair
    source = pd.DataFrame({"x": x.ravel(), "y": y.ravel(), "z": z.ravel()})

    return pn.pane.Vega(
        alt.Chart(source)
        .mark_rect()
        .encode(x="x:O", y="y:O", color="z:Q")
        .properties(
            height=500,
            width="container",
        ),
        sizing_mode="stretch_width",
    )


plots = []
for i in range(5):
    plots.append(make_plot())

pn.serve(pn.Row(objects=plots), port=5007)
