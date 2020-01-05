"""The DatePicker widget does not layout nicely"""

import panel as pn

app = pn.Column(__doc__, pn.widgets.DatePicker())
app.servable()
