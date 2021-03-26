import time

import panel as pn
import param

pn.extension()


class TestButton(param.Parameterized):

    action = param.Action(lambda x: x._print_something())
    event = param.Event()

    updating = param.Boolean()
    view = param.Parameter(precedence=-1)

    def __init__(self, **params):
        super().__init__(**params)

        self.view = self._create_view()

    @param.depends("event", watch=True)
    def _print_something(self):
        if self.updating:
            return

        self.updating = True
        print(f"event: {self.event}, action: {self.action}")
        time.sleep(1)
        self.updating = False

    @param.depends("updating", watch=True)
    def toggle_loading(self):
        self._action_button.loading = self.updating
        self._event_button.loading = self.updating

    def _create_view(self):
        widgets = pn.Param(
            self,
            parameters=["action", "event", "updating"],
            widgets={
                "action": {"button_type": "primary"},
                "event": {"button_type": "success"},
                "updating": {"disabled": True},
            },
        )
        self._action_button = widgets[1]
        self._event_button = widgets[2]
        self._updating_checkbox = widgets[3]
        return widgets


test_button = TestButton()
template = pn.template.FastListTemplate(
    title="How to disable buttons in Panel? Parameterized Approach", theme="dark"
)
template.main[:] = [test_button.view]

template.servable()
