import pandas as pd
import panel as pn

table_data = pd.DataFrame([(1001, "Lorem",),], columns=["Header", "Header",],)
pn.widgets.DataFrame(table_data).servable()
