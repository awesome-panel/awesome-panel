import hvplot.pandas
import pandas as pd
import panel as pn
import panel.widgets as pnw

pn.extension()
from bokeh.sampledata.autompg import autompg

autompgi = autompg.interactive()

year = pnw.IntSlider(start=70, end=82, value=70, name="Year")

out = (
    autompgi[autompgi["yr"] == year]
    .groupby("origin")
    .mean()
    .hvplot("origin", "mpg", kind="bar", ylim=(0, 50))
)

pn.pane.HoloViews(out).servable()
