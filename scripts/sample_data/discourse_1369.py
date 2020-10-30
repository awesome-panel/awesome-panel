import panel as pn

def test_alert():
    my_alert = pn.pane.Alert("foo", alert_type="primary")
    my_button = pn.widgets.Button(name="Toggle")
    def toggle(event):
        if my_alert.alert_type=="primary":
            my_alert.alert_type=="success"
        else:
            my_alert.alert_type="primary"
        my_alert.object = my_alert.alert_type

    my_button.on_click(toggle)

    pn.Row(my_alert, my_button).show()

test_alert()