import panel as pn
import pandas as pd

table_data = pd.DataFrame([(1001, "Lorem"),], columns=["Header", "Header"])
pn.widgets.DataFrame(table_data).servable()
