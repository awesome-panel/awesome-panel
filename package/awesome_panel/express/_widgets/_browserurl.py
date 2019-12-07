"""This module contains functionality to keep a param.Parametrized class
in sync with the browser url


"""
import urllib

import panel as pn


class BrowserUrlMixin:  # pylint: disable=too-few-public-methods
    """This Mixin enables parameters from a param.Parametrized Class to be shown in the url or the
    browser. For example like http://localhost/example_app?country=Norway

    Mix this class with the param.Parametrized class and add the set_browser_url_parameters HTML
    pane to your app in order to get url updates

    Example use case

    class _Country(pnx.BrowserUrlMixin, param.Parameterized):
        country = param.String()

        @param.depends("country")
        def set_browser_url_parameters(self):
            return super().set_browser_url_parameters()
    """

    def __init__(self, *args, **kwargs):
        super(BrowserUrlMixin, self).__init__(*args, **kwargs)
        self._get_browser_url_parameters()

    def _get_browser_url_parameters(self):
        """Sets the parameters from the browser url parameters"""
        for key, value in pn.state.session_args.items():
            if key in self._parameter_dict():
                value_str = value[0].decode("utf8")
                self.set_param(key, value_str)

    def set_browser_url_parameters(self) -> pn.pane.HTML:
        """A HTML Pane. Should be included in the app in order
        to update the browser url when a parameter changes.

        Returns:
            pn.pane.HTML -- A pane containing the javascript script to update the browser url
        """
        return pn.pane.HTML(self._browser_url_parameters_script())

    def _browser_url_parameters_script(self) -> str:
        if len(self.get_param_values()) > 1:  # type: ignore
            state = f'{{param: "{self._urlencode()}"}}'
            title = ""
            url = f"?{self._urlencode()}"

            return f"""<script>window.history.replaceState({state},"{title}","{url}");</script>"""
        return ""

    def _parameter_dict(self):
        return {item[0]: item[1] for item in self.get_param_values() if item[0] != "name"}

    def _urlencode(self):
        return urllib.parse.urlencode(self._parameter_dict())
