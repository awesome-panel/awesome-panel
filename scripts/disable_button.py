import time

import panel as pn

pn.extension()
import param


class TestButton(param.Parameterized):

    action = param.Action(lambda x: x._print_something())
    event = param.Event()

    updating = param.Boolean()

    @param.depends("event", watch=True)
    def _print_something(self):
        if self.updating:
            return

        self.updating = True
        print(f"event: {self.event}, action: {self.action}")
        time.sleep(1)
        self.updating = False


testbutton = TestButton()

widgets = pn.Param(testbutton.param, parameters=["action", "event", "updating"])
action_button = widgets[1]
event_button = widgets[2]
updating_checkbox = widgets[3]

action_button.button_type = "primary"
event_button.button_type = "primary"
updating_checkbox.disabled = True


@param.depends(testbutton.param.updating, watch=True)
def toggle_loading(updating):
    # action_button.disabled = updating
    # event_button.disabled = updating
    action_button.loading = updating
    event_button.loading = updating


template = pn.template.FastListTemplate(title="How to disable buttons in Panel?", theme="dark")
template.main[:] = [pn.Column(action_button, event_button, updating_checkbox)]

template.servable()
