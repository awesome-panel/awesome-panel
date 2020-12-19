import hvplot.pandas
import pandas as pd
import panel as pn
import panel.widgets as pnw
import xarray as xr

pn.extension()

ds = xr.tutorial.load_dataset("air_temperature")
df = ds.to_dataframe().reset_index().set_index("time")
start = df.index.min()
end = df.index.max()
value = start
dfi = df.interactive()
slider = pn.widgets.DateSlider(name="Time", value=value, start=start, end=end)
table = dfi[df.index == slider]
print(df.head())
app = pn.Column(table.hvplot(x="lat", y="lon").panel(), slider)
app.servable()
