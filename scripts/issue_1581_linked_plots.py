## preliminaries ##

import holoviews as hv
import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn
from holoviews.selection import link_selections
from holoviews.util.transform import dim
from holoviews.operation.datashader import shade, rasterize

hv.extension("bokeh", width=100)
pn.extension(comms="vscode")

## create random walks (one location) ##
data_df = pd.DataFrame()
npoints = 15000
np.random.seed(71)
x = np.arange(npoints)
y1 = 1300 + 2.5 * np.random.randn(npoints).cumsum()
y2 = 1500 + 2 * np.random.randn(npoints).cumsum()
y3 = 3 + np.random.randn(npoints).cumsum()
data_df.loc[:, "x"] = x
data_df.loc[:, "rand1"] = y1
data_df.loc[:, "rand2"] = y2
data_df.loc[:, "rand3"] = y3

colors = hv.Cycle("Category10").values
dims = ["rand1", "rand2", "rand3"]
items = []
for c, dim in zip(colors, dims):
    item = data_df.hvplot(x="x", y=dim, kind="points", datashade=True, color=c).opts(height=200).hist(dim)
    item[0].opts(datashade=True)
    item[1].opts(color=c)
    items.append(item)
layout = hv.Layout(items)
link_selections(layout).cols(1)
data_df.hvplot(x="x", y=dim, kind="points", datashade=True)

plot1=data_df.hvplot(x="x", y=dim, kind="points", color=c).opts(height=200, width=500)
plot2=plot1.hist(dim)[1].opts(color=c)
plot1=data_df.hvplot(x="x", y=dim, kind="points", color=c, datashade=True).opts(height=200, width=500)
plot1 << plot2
