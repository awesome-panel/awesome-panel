import time

import panel as pn

pn.extension()

# Create Domain Functions. I.e. the functions that solves your problem.
# For example extracting, transforming or loading data
# For examle creating visualizations


def print_something():
    print("something")
    time.sleep(1)


# Create Widgets and wire them together
updating_checkbox = pn.widgets.Checkbox(
    name="Updating",
    disabled=True,
)
action_button = pn.widgets.Button(name="Action", button_type="primary")
event_button = pn.widgets.Button(name="Event", button_type="success")


def start_updating():
    updating_checkbox.value = True
    action_button.disabled = True
    event_button.disabled = True


def stop_updating():
    action_button.disabled = False
    event_button.disabled = False
    updating_checkbox.value = False


def click_handler(event):
    if updating_checkbox.value:
        return

    start_updating()
    print_something()
    stop_updating()


action_button.on_click(click_handler)
event_button.on_click(click_handler)

# Create the Layout and serve the app

template = pn.template.FastListTemplate(
    title="How to disable buttons in Panel? Functional Approach", theme="dark"
)
template.main[:] = [pn.Column(action_button, event_button, updating_checkbox)]

template.servable()
