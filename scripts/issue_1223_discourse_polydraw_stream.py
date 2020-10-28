from random import randint

import holoviews as hv
import panel as pn
from holoviews import opts, streams

LINE = "red"
FILL1 = "green"
FILL2 = "fulvous"
FILL3 = "blue"

hv.extension("bokeh")
path = hv.Path([[(1, 5), (9, 5)]])
poly = hv.Polygons([[(2, 2), (5, 8), (8, 2)]])
path_stream = streams.PolyDraw(source=path, drag=True, show_vertices=True)
poly_stream = streams.PolyDraw(
    source=poly,
    drag=True,
    num_objects=4,
    show_vertices=True,
    styles={"fill_color": [FILL1, FILL2, FILL3]},
)


def get_plot(path, poly):
    return (path * poly).opts(
        opts.Polygons(fill_alpha=0.3, active_tools=["poly_draw"]),
        opts.Path(color=LINE, height=400, line_width=5, width=400),
    )


plot = get_plot(path, poly)
plot_pane = pn.pane.HoloViews(plot)


def update(*_):
    poly2 = hv.Polygons([[(randint(2, 5), randint(6, 9)), (4, 4), (8, 2)]])
    poly_stream.source = poly2
    plot_pane.object = get_plot(path, poly2)


button = pn.widgets.Button(name="RANDOM RESET")
button.on_click(callback=update)

pn.Column(plot_pane, button).servable()
