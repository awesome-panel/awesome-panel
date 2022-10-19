"""Alert panes inspired by Bootstrap Alerts.

This example was originally created to show how to create custom Bootstrap Alerts.
The Alerts have now been contributed to Panel. You can find the reference example
[here](https://panel.holoviz.org/reference/panes/Alert.html).
"""
import panel as pn

from awesome_panel import config

config.extension(url="bootstrap_alerts")

pn.Column(
    """## InfoAlert

We can show an InfoAlert

- Blue Div with normal and bold text
- With a nice bottom margin
""",
    pn.pane.Alert("This is an **Info Alert**!"),
).servable()

pn.Column(
    """## WarningAlert

We can show a Warning Alert

- Yellow Div with normal and bold text
- With a nice bottom margin
""",
    pn.pane.Alert("This is a **Warning Alert**!", alert_type="warning"),
).servable()

pn.Column(
    """## ErrorAlert

We can show an Error Alert

- Red Div with normal and bold text
- With a nice bottom margin
""",
    pn.pane.Alert("This is an **Error Alert**!", alert_type="danger"),
).servable()
