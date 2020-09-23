"""A Row consisting of a Progressbar and Str does not align vertically"""
import panel as pn

pn.extension()

progress_value = pn.Row(
    pn.widgets.Progress(
        value=20,
        width=200,
        align="center",
    ),
    pn.pane.Str("Running..."),
)
progress_active = pn.Row(
    pn.widgets.Progress(
        active=True,
        width=200,
        align="center",
    ),
    pn.pane.Str("Running..."),
)
app = pn.Column(
    __doc__,
    progress_value,
    progress_active,
)
app.servable()
