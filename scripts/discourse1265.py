import panel as pn
import numpy as np

pn.extension()


def generate_random_number(event=None):
    static_text.value = np.random.randint(low=100000, high=200000)


def toggle_periodic_callback(event):
    periodic_cb.start()


def update_period(event):
    periodic_cb.period = event.new


def abort(event):
    periodic_cb.stop()


static_text = pn.widgets.StaticText(name="Periodic Random Number Generator", value="000000")

generate_button = pn.widgets.Button(name="Generate New Number")
generate_button.on_click(generate_random_number)

start_button = pn.widgets.Button(name="start_button ", button_type="primary")

start_button.on_click(toggle_periodic_callback)

abort_button = pn.widgets.Button(name="Stop", button_type="danger")
abort_button.on_click(abort)

period = pn.widgets.Spinner(name="Period (ms)", value=500, step=50, start=50)
period.param.watch(update_period, "value")

periodic_cb = static_text.add_periodic_callback(
    generate_random_number, period=period.value, start=False
)  # period in milliseconds

col = pn.Column(period, start_button, abort_button, static_text)
col.servable()
