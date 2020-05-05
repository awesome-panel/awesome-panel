"""In this module we implement the Toast model

The Toast model is basically a message and an action that can be sent to the Snackbar
"""
import param


class Toast(param.Parameterized):
    """The Toast model is basically a message and an action that can be sent to the Snackbar"""
    message = param.String()
    action = param.Action()
