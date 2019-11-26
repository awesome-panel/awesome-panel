import param
import panel as pn
import json
import urllib


class UrlMixin:
    """This Mixin enables parameters from a param.Parametrized Class to be shown in the url or the
    browser. http://example

    Mix this class with the param.Parametrized class and add the set_browser_url_parameters HTML pane to
    your app in order to get url updates

    Example use case

    class _Country(pnx.param.UrlMixin, param.Parameterized):
        country = param.String()

        @param.depends("country")
        def set_browser_url_parameters(self):
            return super().set_browser_url_parameters()
    """

    def __init__(self):
        for key, value in pn.state.session_args.items():
            if key in self._parameter_dict():
                value_str = value[0].decode("utf8")
                self.set_param(key, value_str)

    def set_browser_url_parameters(self) -> pn.pane.HTML:
        if len(self.get_param_values()) > 1:
            state = '{test: "me"}'
            title = ""
            url = f"?{self._urlencode()}"

            script = f"""<script>window.history.replaceState({state},"{title}","{url}");</script>"""
        else:
            script = ""
        return pn.pane.HTML(script)

    def _parameter_dict(self):
        return {item[0]: item[1] for item in self.get_param_values() if item[0] != "name"}

    def _urlencode(self):
        return urllib.parse.urlencode(self._parameter_dict())
