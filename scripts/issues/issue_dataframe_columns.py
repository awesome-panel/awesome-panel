import panel as pn
from yahooquery import Ticker

data = Ticker("ORSTED.CO").balance_sheet(frequency="annual")
app = pn.widgets.DataFrame(data, fit_columns=True, sizing_mode="stretch_width")
app.servable()
