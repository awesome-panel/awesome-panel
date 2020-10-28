import panel as pn
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers

pn.extension("katex")


def create_figure(width):
    p = figure(height=200, width=width, tools="box_select")
    p.circle("petal_length", "petal_width", source=ColumnDataSource(flowers))
    # note: if one directly returns "p" here, it is transformed into Bokeh(Figure) only the first time
    return pn.pane.Bokeh(p)


pnl = pn.Row(create_figure(width=200))


def replace_plot(event):
    width = int(event.new)
    print("Replacing {}".format(str(pnl.objects[0])))
    pnl[0] = create_figure(width)


select = pn.widgets.RadioButtonGroup(name="Plot selection", options=["200", "400"])
select.param.watch(replace_plot, "value")

col = pn.Column(pnl, select)
col.servable()
