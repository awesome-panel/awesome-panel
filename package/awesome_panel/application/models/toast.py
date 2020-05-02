import param

class Toast(param.Parameterized):
    message = param.String()
    action = param.Action()