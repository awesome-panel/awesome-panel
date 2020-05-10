import datetime
import importlib
import sys
import traceback
import pathlib
import param

from awesome_panel.designer.components.empty_component import EmptyComponent


class ReloadService(param.Parameterized):
    component = param.Parameter(allow_None=False)
    component_parameters = param.Dict()
    component_instance = param.Parameter()
    css_path = param.Parameter(constant=True)
    js_path = param.Parameter(constant=True)
    modules_to_reload = param.List()

    reload_component = param.Action(label="RELOAD COMPONENT")
    reload_css_file = param.Action(label="RELOAD CSS")
    reload_js_file = param.Action(label="RELOAD JS")

    css_text = param.String()
    js_text = param.String()

    reloading = param.Boolean(default=False)
    last_reload = param.String(constant=True)
    error_message = param.String()

    def __init__(self, **params):
        if "component" not in params:
            params["component"] = EmptyComponent
        super().__init__(**params)

        with param.edit_constant(self):
            self.name=self.component.name

        self.reload_component = self._reload_component
        self.reload_css_file = self._reload_css_file
        self.reload_js_file = self._reload_js_file

    def __repr__(self):
        return f"ReloadService({self.name})"

    def __str__(self):
        return f"ReloadService({self.name})"

    def _reload_component(self, _=None):
        try:
            self._signal_reload_start()

            if self.component_instance is not None:
                for mod in self.modules_to_reload:
                    importlib.reload(mod)

                mod = sys.modules[self.component.__module__]
                importlib.reload(mod)
                with param.edit_constant(self):
                    self.component = getattr(mod, self.component.__name__)

            if self.component_parameters:
                self.component_instance = self.component(**self.component_parameters)
            else:
                self.component_instance = self.component()

            self._reset_error_message()
        except Exception as ex:
            self._report_exception(ex)
        finally:
            self._signal_reload_end()

    def _reload_css_file(self, _=None):
        try:
            self._signal_reload_start()
            if not self.css_path:
                pass
            elif isinstance(self.css_path, pathlib.Path):
                self.css_text = self.css_path.read_text()
            else:
                raise NotImplementedError

            self._reset_error_message()
        except Exception as ex:
            self._report_exception(ex)
        finally:
            self._signal_reload_end()

    def _reload_js_file(self, _=None):
        try:
            self._signal_reload_start()
            if not self.js_path:
                pass
            elif isinstance(self.js_path, pathlib.Path):
                self.js_text = self.js_path.read_text()
            else:
                raise NotImplementedError

            self._reset_error_message()
        except Exception as ex:
            self._report_exception(ex)
        finally:
            self._signal_reload_end()

    def _signal_reload_start(self):
        self.reloading = True
        print("reload start", self.name, datetime.datetime.now())

    def _report_exception(self, ex):
        self.error_message = "# Error " + traceback.format_exc()
        print(self.name, self.error_message)

    def _signal_reload_end(self):
        self.reloading = False
        with param.edit_constant(self):
            self.last_reload = str(datetime.datetime.now())
        print("reload end", self.name, datetime.datetime.now())

    def _reset_error_message(self):
        self.error_message = ""
