import param
import panel as pn

class MultiParamApp(param.Parameterized):
    count = param.Integer(0)
    param1 = param.Integer(0)
    param2= param.Integer(0)
    update = param.Action()
    update_once = param.Action()
    update_once_disable_watchers = param.Action()
    reset = param.Action()

    view = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)

        self._updating = False

        self.update = self._update
        self.update_once = self._update_once
        self.update_once_disable_watchers = self._update_once_disable_watchers
        self.reset = self._reset

        self.view = pn.Param(self,
            widgets = {
                "update": {"button_type": "danger"},
                "update_once": {"button_type": "danger"},
                "update_once_disable_watchers": {"button_type": "success"},
            }
        )


    @param.depends("param1", "param2", watch=True)
    def _inc(self):
        if not self._updating:
            self.count += 1

    def _update(self, _=None):
        self.param1 = self.param1 +1
        self.param2 = self.param2 +1

    def _update_once(self, _=None):
        self.param.set_param(param1= self.param1+1, param2= self.param2+1)

    def _update_once_disable_watchers(self, _=None):
        self._updating = True
        self._update_once()
        self._updating = False
        self._inc()

    def _reset(self, _=None):
        self.count = 0

MultiParamApp().view.servable()