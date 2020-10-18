"""This module implements the ReloadService. The ReloadService is used by the Designer.
For each component you want access to in the Designer you should provide a seperate
Reload Service"""

import datetime
import importlib
import pathlib
import sys
import traceback

import param
from awesome_panel.designer.views import ErrorView


class ReloadService(param.Parameterized):  # pylint: disable=too-many-instance-attributes
    """The ReloadService is used by the Designer.
    For each component you want access to in the Designer you should provide a seperate
    Reload Service

    Args:
        component ([type]): For now the components that are know to be supported are

        - subclasses of `pn.reactive.Reactive`
        - subclasses of `param.Parameterized` with a `view` parameter which is a subclass of
        `pn.reactive.Reactive`

    Please NOTE that in order for the reload service to be able to reload the compoonent, the
    component specified cannot be defined in the __main__ file.

    Example
    -------

    ```python
    TITLE_COMPONENT = ReloadService(
        component=components.TitleComponent, css_path=COMPONENT_CSS, js_path=COMPONENT_JS,
    )
    EMPTY_COMPONENT = ReloadService(
        component=components.EmptyComponent, css_path=COMPONENT_CSS, js_path=COMPONENT2_JS,
    )
    ```"""

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

    def __init__(self, component, **params):
        if not isinstance(params, dict):
            params = {}
        params["component"] = component
        super().__init__(**params)

        try:
            name = self.component.name
        except AttributeError:
            name = self.component.__name__

        with param.edit_constant(self):
            self.name = name

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
                for mod in self.modules_to_reload:  # pylint: disable=not-an-iterable
                    importlib.reload(mod)

                mod = sys.modules[self.component.__module__]
                importlib.reload(mod)
                with param.edit_constant(self):
                    self.component = getattr(mod, self.component.__name__)

            if self.component_parameters:
                # pylint: disable=not-a-mapping
                self.component_instance = self.component(**self.component_parameters)
            else:
                self.component_instance = self.component()

            self._reset_error_message()
        except Exception as ex:  # pylint: disable=broad-except
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
        except Exception as ex:  # pylint: disable=broad-except
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
        except Exception as ex:  # pylint: disable=broad-except
            self._report_exception(ex)
        finally:
            self._signal_reload_end()

    def _signal_reload_start(self):
        self.reloading = True
        print("reload start", self.name, datetime.datetime.now())

    def _report_exception(self, ex):  # pylint: disable=unused-argument
        self.error_message = traceback.format_exc()
        self.component_instance = ErrorView(error_message=self.error_message)
        print(self.name, self.error_message)

    def _signal_reload_end(self):
        self.reloading = False
        with param.edit_constant(self):
            self.last_reload = str(datetime.datetime.now())
        print("reload end", self.name, datetime.datetime.now())

    def _reset_error_message(self):
        self.error_message = ""
