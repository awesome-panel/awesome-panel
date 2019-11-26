import param
import panel as pn
import json
import urllib


class Url:
    def set_url_parameters(self) -> pn.Pane:
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
